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
        :param _AccessRegion: 加速地域。
        :type AccessRegion: str
        :param _Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param _Concurrent: 通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param _NetworkType: 网络类型，可取值：normal、cn2，默认值为normal
        :type NetworkType: str
        """
        self._AccessRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._NetworkType = None

    @property
    def AccessRegion(self):
        """加速地域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def Bandwidth(self):
        """通道带宽上限，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        """通道并发量上限，表示同时在线的连接数，单位：万。
        :rtype: int
        """
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def NetworkType(self):
        """网络类型，可取值：normal、cn2，默认值为normal
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType


    def _deserialize(self, params):
        self._AccessRegion = params.get("AccessRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._NetworkType = params.get("NetworkType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRegionDetial(AbstractModel):
    """根据源站查询的可用加速区域信息及对应的可选带宽和并发量。

    """

    def __init__(self):
        r"""
        :param _RegionId: 区域ID
        :type RegionId: str
        :param _RegionName: 区域的中文或英文名称
        :type RegionName: str
        :param _ConcurrentList: 可选的并发量取值数组
        :type ConcurrentList: list of int
        :param _BandwidthList: 可选的带宽取值数组
        :type BandwidthList: list of int
        :param _RegionArea: 机房所属大区
        :type RegionArea: str
        :param _RegionAreaName: 机房所属大区名
        :type RegionAreaName: str
        :param _IDCType: 机房类型, dc表示DataCenter数据中心, ec表示EdgeComputing边缘节点
        :type IDCType: str
        :param _FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
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
        :type FeatureBitmap: int
        """
        self._RegionId = None
        self._RegionName = None
        self._ConcurrentList = None
        self._BandwidthList = None
        self._RegionArea = None
        self._RegionAreaName = None
        self._IDCType = None
        self._FeatureBitmap = None

    @property
    def RegionId(self):
        """区域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """区域的中文或英文名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ConcurrentList(self):
        """可选的并发量取值数组
        :rtype: list of int
        """
        return self._ConcurrentList

    @ConcurrentList.setter
    def ConcurrentList(self, ConcurrentList):
        self._ConcurrentList = ConcurrentList

    @property
    def BandwidthList(self):
        """可选的带宽取值数组
        :rtype: list of int
        """
        return self._BandwidthList

    @BandwidthList.setter
    def BandwidthList(self, BandwidthList):
        self._BandwidthList = BandwidthList

    @property
    def RegionArea(self):
        """机房所属大区
        :rtype: str
        """
        return self._RegionArea

    @RegionArea.setter
    def RegionArea(self, RegionArea):
        self._RegionArea = RegionArea

    @property
    def RegionAreaName(self):
        """机房所属大区名
        :rtype: str
        """
        return self._RegionAreaName

    @RegionAreaName.setter
    def RegionAreaName(self, RegionAreaName):
        self._RegionAreaName = RegionAreaName

    @property
    def IDCType(self):
        """机房类型, dc表示DataCenter数据中心, ec表示EdgeComputing边缘节点
        :rtype: str
        """
        return self._IDCType

    @IDCType.setter
    def IDCType(self, IDCType):
        self._IDCType = IDCType

    @property
    def FeatureBitmap(self):
        """特性位图，每个bit位代表一种特性，其中：
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
        :rtype: int
        """
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ConcurrentList = params.get("ConcurrentList")
        self._BandwidthList = params.get("BandwidthList")
        self._RegionArea = params.get("RegionArea")
        self._RegionAreaName = params.get("RegionAreaName")
        self._IDCType = params.get("IDCType")
        self._FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRegionDomainConf(AbstractModel):
    """域名就近接入配置

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID。
        :type RegionId: str
        :param _NationCountryInnerList: 就近接入区域国家内部编码，编码列表可通过DescribeCountryAreaMapping接口获取。
        :type NationCountryInnerList: list of str
        """
        self._RegionId = None
        self._NationCountryInnerList = None

    @property
    def RegionId(self):
        """地域ID。
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def NationCountryInnerList(self):
        """就近接入区域国家内部编码，编码列表可通过DescribeCountryAreaMapping接口获取。
        :rtype: list of str
        """
        return self._NationCountryInnerList

    @NationCountryInnerList.setter
    def NationCountryInnerList(self, NationCountryInnerList):
        self._NationCountryInnerList = NationCountryInnerList


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._NationCountryInnerList = params.get("NationCountryInnerList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRealServersRequest(AbstractModel):
    """AddRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 源站对应的项目ID
        :type ProjectId: int
        :param _RealServerIP: 源站对应的IP或域名
        :type RealServerIP: list of str
        :param _RealServerName: 源站名称
        :type RealServerName: str
        :param _TagSet: 标签列表
        :type TagSet: list of TagPair
        """
        self._ProjectId = None
        self._RealServerIP = None
        self._RealServerName = None
        self._TagSet = None

    @property
    def ProjectId(self):
        """源站对应的项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RealServerIP(self):
        """源站对应的IP或域名
        :rtype: list of str
        """
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerName(self):
        """源站名称
        :rtype: str
        """
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerName = params.get("RealServerName")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRealServersResponse(AbstractModel):
    """AddRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RealServerSet: 源站信息列表
        :type RealServerSet: list of NewRealServer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RealServerSet = None
        self._RequestId = None

    @property
    def RealServerSet(self):
        """源站信息列表
        :rtype: list of NewRealServer
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

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
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = NewRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._RequestId = params.get("RequestId")


class BanAndRecoverProxyRequest(AbstractModel):
    """BanAndRecoverProxy请求参数结构体

    """


class BanAndRecoverProxyResponse(AbstractModel):
    """BanAndRecoverProxy返回参数结构体

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


class BandwidthPriceGradient(AbstractModel):
    """带宽梯度价格

    """

    def __init__(self):
        r"""
        :param _BandwidthRange: 带宽范围。
        :type BandwidthRange: list of int
        :param _BandwidthUnitPrice: 在对应带宽范围内的单宽单价，单位：元/Mbps/天。
        :type BandwidthUnitPrice: float
        :param _DiscountBandwidthUnitPrice: 带宽折扣价，单位：元/Mbps/天。
        :type DiscountBandwidthUnitPrice: float
        """
        self._BandwidthRange = None
        self._BandwidthUnitPrice = None
        self._DiscountBandwidthUnitPrice = None

    @property
    def BandwidthRange(self):
        """带宽范围。
        :rtype: list of int
        """
        return self._BandwidthRange

    @BandwidthRange.setter
    def BandwidthRange(self, BandwidthRange):
        self._BandwidthRange = BandwidthRange

    @property
    def BandwidthUnitPrice(self):
        """在对应带宽范围内的单宽单价，单位：元/Mbps/天。
        :rtype: float
        """
        return self._BandwidthUnitPrice

    @BandwidthUnitPrice.setter
    def BandwidthUnitPrice(self, BandwidthUnitPrice):
        self._BandwidthUnitPrice = BandwidthUnitPrice

    @property
    def DiscountBandwidthUnitPrice(self):
        """带宽折扣价，单位：元/Mbps/天。
        :rtype: float
        """
        return self._DiscountBandwidthUnitPrice

    @DiscountBandwidthUnitPrice.setter
    def DiscountBandwidthUnitPrice(self, DiscountBandwidthUnitPrice):
        self._DiscountBandwidthUnitPrice = DiscountBandwidthUnitPrice


    def _deserialize(self, params):
        self._BandwidthRange = params.get("BandwidthRange")
        self._BandwidthUnitPrice = params.get("BandwidthUnitPrice")
        self._DiscountBandwidthUnitPrice = params.get("DiscountBandwidthUnitPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindListenerRealServersRequest(AbstractModel):
    """BindListenerRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _RealServerBindSet: 待绑定源站列表。如果该监听器的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self._ListenerId = None
        self._RealServerBindSet = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RealServerBindSet(self):
        """待绑定源站列表。如果该监听器的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。
        :rtype: list of RealServerBindSetReq
        """
        return self._RealServerBindSet

    @RealServerBindSet.setter
    def RealServerBindSet(self, RealServerBindSet):
        self._RealServerBindSet = RealServerBindSet


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        if params.get("RealServerBindSet") is not None:
            self._RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self._RealServerBindSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindListenerRealServersResponse(AbstractModel):
    """BindListenerRealServers返回参数结构体

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


class BindRealServer(AbstractModel):
    """已绑定的源站信息

    """

    def __init__(self):
        r"""
        :param _RealServerId: 源站ID
        :type RealServerId: str
        :param _RealServerIP: 源站IP或者域名
        :type RealServerIP: str
        :param _RealServerWeight: 该源站所占权重
        :type RealServerWeight: int
        :param _RealServerStatus: 源站健康检查状态，其中：
0表示正常；
1表示异常。
未开启健康检查状态时，该状态始终为正常。
        :type RealServerStatus: int
        :param _RealServerPort: 源站的端口号
        :type RealServerPort: int
        :param _DownIPList: 当源站为域名时，域名被解析成一个或者多个IP，该字段表示其中异常的IP列表。状态异常，但该字段为空时，表示域名解析异常。
        :type DownIPList: list of str
        :param _RealServerFailoverRole: 源站主备角色：master表示主，slave表示备，该参数必须在监听器打开了源站主备模式。
        :type RealServerFailoverRole: str
        """
        self._RealServerId = None
        self._RealServerIP = None
        self._RealServerWeight = None
        self._RealServerStatus = None
        self._RealServerPort = None
        self._DownIPList = None
        self._RealServerFailoverRole = None

    @property
    def RealServerId(self):
        """源站ID
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerIP(self):
        """源站IP或者域名
        :rtype: str
        """
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerWeight(self):
        """该源站所占权重
        :rtype: int
        """
        return self._RealServerWeight

    @RealServerWeight.setter
    def RealServerWeight(self, RealServerWeight):
        self._RealServerWeight = RealServerWeight

    @property
    def RealServerStatus(self):
        """源站健康检查状态，其中：
0表示正常；
1表示异常。
未开启健康检查状态时，该状态始终为正常。
        :rtype: int
        """
        return self._RealServerStatus

    @RealServerStatus.setter
    def RealServerStatus(self, RealServerStatus):
        self._RealServerStatus = RealServerStatus

    @property
    def RealServerPort(self):
        """源站的端口号
        :rtype: int
        """
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def DownIPList(self):
        """当源站为域名时，域名被解析成一个或者多个IP，该字段表示其中异常的IP列表。状态异常，但该字段为空时，表示域名解析异常。
        :rtype: list of str
        """
        return self._DownIPList

    @DownIPList.setter
    def DownIPList(self, DownIPList):
        self._DownIPList = DownIPList

    @property
    def RealServerFailoverRole(self):
        """源站主备角色：master表示主，slave表示备，该参数必须在监听器打开了源站主备模式。
        :rtype: str
        """
        return self._RealServerFailoverRole

    @RealServerFailoverRole.setter
    def RealServerFailoverRole(self, RealServerFailoverRole):
        self._RealServerFailoverRole = RealServerFailoverRole


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerWeight = params.get("RealServerWeight")
        self._RealServerStatus = params.get("RealServerStatus")
        self._RealServerPort = params.get("RealServerPort")
        self._DownIPList = params.get("DownIPList")
        self._RealServerFailoverRole = params.get("RealServerFailoverRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRealServerInfo(AbstractModel):
    """添加源站的源站信息返回值

    """

    def __init__(self):
        r"""
        :param _RealServerIP: 源站的IP或域名
        :type RealServerIP: str
        :param _RealServerId: 源站ID
        :type RealServerId: str
        :param _RealServerName: 源站名称
        :type RealServerName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _TagSet: 标签列表
        :type TagSet: list of TagPair
        """
        self._RealServerIP = None
        self._RealServerId = None
        self._RealServerName = None
        self._ProjectId = None
        self._TagSet = None

    @property
    def RealServerIP(self):
        """源站的IP或域名
        :rtype: str
        """
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerId(self):
        """源站ID
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerName(self):
        """源站名称
        :rtype: str
        """
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerId = params.get("RealServerId")
        self._RealServerName = params.get("RealServerName")
        self._ProjectId = params.get("ProjectId")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRuleRealServersRequest(AbstractModel):
    """BindRuleRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 转发规则ID
        :type RuleId: str
        :param _RealServerBindSet: 需要绑定的源站信息列表。
如果已经存在绑定的源站，则会覆盖更新成这个源站列表。
当不带该字段时，表示解绑该规则上的所有源站。
如果该规则的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self._RuleId = None
        self._RealServerBindSet = None

    @property
    def RuleId(self):
        """转发规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RealServerBindSet(self):
        """需要绑定的源站信息列表。
如果已经存在绑定的源站，则会覆盖更新成这个源站列表。
当不带该字段时，表示解绑该规则上的所有源站。
如果该规则的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。
        :rtype: list of RealServerBindSetReq
        """
        return self._RealServerBindSet

    @RealServerBindSet.setter
    def RealServerBindSet(self, RealServerBindSet):
        self._RealServerBindSet = RealServerBindSet


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        if params.get("RealServerBindSet") is not None:
            self._RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self._RealServerBindSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRuleRealServersResponse(AbstractModel):
    """BindRuleRealServers返回参数结构体

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


class Certificate(AbstractModel):
    """服务器证书

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _CertificateName: 证书名称（旧参数，请使用CertificateAlias）。
        :type CertificateName: str
        :param _CertificateType: 证书类型。
        :type CertificateType: int
        :param _CertificateAlias: 证书名称。
        :type CertificateAlias: str
        :param _CreateTime: 证书创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type CreateTime: int
        :param _BeginTime: 证书生效起始时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type BeginTime: int
        :param _EndTime: 证书过期时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type EndTime: int
        :param _IssuerCN: 证书签发者通用名称。
        :type IssuerCN: str
        :param _SubjectCN: 证书主题通用名称。
        :type SubjectCN: str
        """
        self._CertificateId = None
        self._CertificateName = None
        self._CertificateType = None
        self._CertificateAlias = None
        self._CreateTime = None
        self._BeginTime = None
        self._EndTime = None
        self._IssuerCN = None
        self._SubjectCN = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateName(self):
        """证书名称（旧参数，请使用CertificateAlias）。
        :rtype: str
        """
        return self._CertificateName

    @CertificateName.setter
    def CertificateName(self, CertificateName):
        self._CertificateName = CertificateName

    @property
    def CertificateType(self):
        """证书类型。
        :rtype: int
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def CertificateAlias(self):
        """证书名称。
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CreateTime(self):
        """证书创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BeginTime(self):
        """证书生效起始时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """证书过期时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IssuerCN(self):
        """证书签发者通用名称。
        :rtype: str
        """
        return self._IssuerCN

    @IssuerCN.setter
    def IssuerCN(self, IssuerCN):
        self._IssuerCN = IssuerCN

    @property
    def SubjectCN(self):
        """证书主题通用名称。
        :rtype: str
        """
        return self._SubjectCN

    @SubjectCN.setter
    def SubjectCN(self, SubjectCN):
        self._SubjectCN = SubjectCN


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateName = params.get("CertificateName")
        self._CertificateType = params.get("CertificateType")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CreateTime = params.get("CreateTime")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._IssuerCN = params.get("IssuerCN")
        self._SubjectCN = params.get("SubjectCN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateAliasInfo(AbstractModel):
    """证书别名信息

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _CertificateAlias: 证书别名
        :type CertificateAlias: str
        """
        self._CertificateId = None
        self._CertificateAlias = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateAlias(self):
        """证书别名
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateDetail(AbstractModel):
    """证书详情，包括证书ID， 证书名字，证书类型，证书内容以及密钥内容。

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _CertificateType: 证书类型。
        :type CertificateType: int
        :param _CertificateAlias: 证书名字。
        :type CertificateAlias: str
        :param _CertificateContent: 证书内容。
        :type CertificateContent: str
        :param _CertificateKey: 密钥内容。仅当证书类型为SSL证书时，返回该字段。
        :type CertificateKey: str
        :param _CreateTime: 创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type CreateTime: int
        :param _BeginTime: 证书生效起始时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type BeginTime: int
        :param _EndTime: 证书过期时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type EndTime: int
        :param _IssuerCN: 证书签发者通用名称。
        :type IssuerCN: str
        :param _SubjectCN: 证书主题通用名称。
        :type SubjectCN: str
        """
        self._CertificateId = None
        self._CertificateType = None
        self._CertificateAlias = None
        self._CertificateContent = None
        self._CertificateKey = None
        self._CreateTime = None
        self._BeginTime = None
        self._EndTime = None
        self._IssuerCN = None
        self._SubjectCN = None

    @property
    def CertificateId(self):
        """证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateType(self):
        """证书类型。
        :rtype: int
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def CertificateAlias(self):
        """证书名字。
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CertificateContent(self):
        """证书内容。
        :rtype: str
        """
        return self._CertificateContent

    @CertificateContent.setter
    def CertificateContent(self, CertificateContent):
        self._CertificateContent = CertificateContent

    @property
    def CertificateKey(self):
        """密钥内容。仅当证书类型为SSL证书时，返回该字段。
        :rtype: str
        """
        return self._CertificateKey

    @CertificateKey.setter
    def CertificateKey(self, CertificateKey):
        self._CertificateKey = CertificateKey

    @property
    def CreateTime(self):
        """创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def BeginTime(self):
        """证书生效起始时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._BeginTime

    @BeginTime.setter
    def BeginTime(self, BeginTime):
        self._BeginTime = BeginTime

    @property
    def EndTime(self):
        """证书过期时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def IssuerCN(self):
        """证书签发者通用名称。
        :rtype: str
        """
        return self._IssuerCN

    @IssuerCN.setter
    def IssuerCN(self, IssuerCN):
        self._IssuerCN = IssuerCN

    @property
    def SubjectCN(self):
        """证书主题通用名称。
        :rtype: str
        """
        return self._SubjectCN

    @SubjectCN.setter
    def SubjectCN(self, SubjectCN):
        self._SubjectCN = SubjectCN


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateType = params.get("CertificateType")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CertificateContent = params.get("CertificateContent")
        self._CertificateKey = params.get("CertificateKey")
        self._CreateTime = params.get("CreateTime")
        self._BeginTime = params.get("BeginTime")
        self._EndTime = params.get("EndTime")
        self._IssuerCN = params.get("IssuerCN")
        self._SubjectCN = params.get("SubjectCN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckProxyCreateRequest(AbstractModel):
    """CheckProxyCreate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRegion: 通道的接入(加速)区域。取值可通过接口DescribeAccessRegionsByDestRegion获取到
        :type AccessRegion: str
        :param _RealServerRegion: 通道的源站区域。取值可通过接口DescribeDestRegions获取到
        :type RealServerRegion: str
        :param _Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param _Concurrent: 通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param _GroupId: 如果在通道组下创建通道，需要填写通道组的ID
        :type GroupId: str
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _NetworkType: 网络类型，可取值：normal、cn2，默认值normal
        :type NetworkType: str
        :param _PackageType: 通道套餐类型。Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        :param _Http3Supported: 该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :type Http3Supported: int
        """
        self._AccessRegion = None
        self._RealServerRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._GroupId = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def AccessRegion(self):
        """通道的接入(加速)区域。取值可通过接口DescribeAccessRegionsByDestRegion获取到
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def RealServerRegion(self):
        """通道的源站区域。取值可通过接口DescribeDestRegions获取到
        :rtype: str
        """
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def Bandwidth(self):
        """通道带宽上限，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        """通道并发量上限，表示同时在线的连接数，单位：万。
        :rtype: int
        """
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def GroupId(self):
        """如果在通道组下创建通道，需要填写通道组的ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        """网络类型，可取值：normal、cn2，默认值normal
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        """通道套餐类型。Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        """该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._AccessRegion = params.get("AccessRegion")
        self._RealServerRegion = params.get("RealServerRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._GroupId = params.get("GroupId")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckProxyCreateResponse(AbstractModel):
    """CheckProxyCreate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CheckFlag: 查询能否创建给定配置的通道，1可以创建，0不可创建。
        :type CheckFlag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CheckFlag = None
        self._RequestId = None

    @property
    def CheckFlag(self):
        """查询能否创建给定配置的通道，1可以创建，0不可创建。
        :rtype: int
        """
        return self._CheckFlag

    @CheckFlag.setter
    def CheckFlag(self, CheckFlag):
        self._CheckFlag = CheckFlag

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
        self._CheckFlag = params.get("CheckFlag")
        self._RequestId = params.get("RequestId")


class CloseProxiesRequest(AbstractModel):
    """CloseProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: （旧参数，请切换到ProxyIds）通道的实例ID。
        :type InstanceIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _ProxyIds: （新参数）通道的实例ID。
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）通道的实例ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        """（新参数）通道的实例ID。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxiesResponse(AbstractModel):
    """CloseProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: 非运行状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        """非运行状态下的通道实例ID列表，不可开启。
        :rtype: list of str
        """
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        """开启操作失败的通道实例ID列表。
        :rtype: list of str
        """
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

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
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class CloseProxyGroupRequest(AbstractModel):
    """CloseProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组的实例 ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """通道组的实例 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxyGroupResponse(AbstractModel):
    """CloseProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: 非运行状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        """非运行状态下的通道实例ID列表，不可开启。
        :rtype: list of str
        """
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        """开启操作失败的通道实例ID列表。
        :rtype: list of str
        """
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

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
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class CloseSecurityPolicyRequest(AbstractModel):
    """CloseSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID。操作通道组时无需填此参数。
        :type ProxyId: str
        :param _PolicyId: 安全组策略ID。操作通道组时须填此参数。
        :type PolicyId: str
        """
        self._ProxyId = None
        self._PolicyId = None

    @property
    def ProxyId(self):
        """通道ID。操作通道组时无需填此参数。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def PolicyId(self):
        """安全组策略ID。操作通道组时须填此参数。
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseSecurityPolicyResponse(AbstractModel):
    """CloseSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID，可以通过DescribeAsyncTaskStatus 查询流程执行进展和状态
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步流程ID，可以通过DescribeAsyncTaskStatus 查询流程执行进展和状态
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


class CountryAreaMap(AbstractModel):
    """国家地区映射关系（名称和编码）

    """

    def __init__(self):
        r"""
        :param _NationCountryName: 国家名称。
        :type NationCountryName: str
        :param _NationCountryInnerCode: 国家编码。
        :type NationCountryInnerCode: str
        :param _GeographicalZoneName: 地区名称。
        :type GeographicalZoneName: str
        :param _GeographicalZoneInnerCode: 地区编码。
        :type GeographicalZoneInnerCode: str
        :param _ContinentName: 大洲名称。
        :type ContinentName: str
        :param _ContinentInnerCode: 大洲编码。
        :type ContinentInnerCode: str
        :param _Remark: 标注信息
        :type Remark: str
        """
        self._NationCountryName = None
        self._NationCountryInnerCode = None
        self._GeographicalZoneName = None
        self._GeographicalZoneInnerCode = None
        self._ContinentName = None
        self._ContinentInnerCode = None
        self._Remark = None

    @property
    def NationCountryName(self):
        """国家名称。
        :rtype: str
        """
        return self._NationCountryName

    @NationCountryName.setter
    def NationCountryName(self, NationCountryName):
        self._NationCountryName = NationCountryName

    @property
    def NationCountryInnerCode(self):
        """国家编码。
        :rtype: str
        """
        return self._NationCountryInnerCode

    @NationCountryInnerCode.setter
    def NationCountryInnerCode(self, NationCountryInnerCode):
        self._NationCountryInnerCode = NationCountryInnerCode

    @property
    def GeographicalZoneName(self):
        """地区名称。
        :rtype: str
        """
        return self._GeographicalZoneName

    @GeographicalZoneName.setter
    def GeographicalZoneName(self, GeographicalZoneName):
        self._GeographicalZoneName = GeographicalZoneName

    @property
    def GeographicalZoneInnerCode(self):
        """地区编码。
        :rtype: str
        """
        return self._GeographicalZoneInnerCode

    @GeographicalZoneInnerCode.setter
    def GeographicalZoneInnerCode(self, GeographicalZoneInnerCode):
        self._GeographicalZoneInnerCode = GeographicalZoneInnerCode

    @property
    def ContinentName(self):
        """大洲名称。
        :rtype: str
        """
        return self._ContinentName

    @ContinentName.setter
    def ContinentName(self, ContinentName):
        self._ContinentName = ContinentName

    @property
    def ContinentInnerCode(self):
        """大洲编码。
        :rtype: str
        """
        return self._ContinentInnerCode

    @ContinentInnerCode.setter
    def ContinentInnerCode(self, ContinentInnerCode):
        self._ContinentInnerCode = ContinentInnerCode

    @property
    def Remark(self):
        """标注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._NationCountryName = params.get("NationCountryName")
        self._NationCountryInnerCode = params.get("NationCountryInnerCode")
        self._GeographicalZoneName = params.get("GeographicalZoneName")
        self._GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self._ContinentName = params.get("ContinentName")
        self._ContinentInnerCode = params.get("ContinentInnerCode")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateType: 证书类型。其中：
0，表示基础认证配置；
1，表示客户端CA证书；
2，服务器SSL证书；
3，表示源站CA证书；
4，表示通道SSL证书。
        :type CertificateType: int
        :param _CertificateContent: 证书内容。采用url编码。其中：
当证书类型为基础认证配置时，该参数填写用户名/密码对。格式：“用户名：密码”，例如：root:FSGdT。其中密码使用htpasswd或者openssl，例如：openssl passwd -crypt 123456。
当证书类型为CA/SSL证书时，该参数填写证书内容，格式为pem。
        :type CertificateContent: str
        :param _CertificateAlias: 证书名称
        :type CertificateAlias: str
        :param _CertificateKey: 密钥内容。采用url编码。仅当证书类型为SSL证书时，需要填写该参数。格式为pem。
        :type CertificateKey: str
        """
        self._CertificateType = None
        self._CertificateContent = None
        self._CertificateAlias = None
        self._CertificateKey = None

    @property
    def CertificateType(self):
        """证书类型。其中：
0，表示基础认证配置；
1，表示客户端CA证书；
2，服务器SSL证书；
3，表示源站CA证书；
4，表示通道SSL证书。
        :rtype: int
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def CertificateContent(self):
        """证书内容。采用url编码。其中：
当证书类型为基础认证配置时，该参数填写用户名/密码对。格式：“用户名：密码”，例如：root:FSGdT。其中密码使用htpasswd或者openssl，例如：openssl passwd -crypt 123456。
当证书类型为CA/SSL证书时，该参数填写证书内容，格式为pem。
        :rtype: str
        """
        return self._CertificateContent

    @CertificateContent.setter
    def CertificateContent(self, CertificateContent):
        self._CertificateContent = CertificateContent

    @property
    def CertificateAlias(self):
        """证书名称
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def CertificateKey(self):
        """密钥内容。采用url编码。仅当证书类型为SSL证书时，需要填写该参数。格式为pem。
        :rtype: str
        """
        return self._CertificateKey

    @CertificateKey.setter
    def CertificateKey(self, CertificateKey):
        self._CertificateKey = CertificateKey


    def _deserialize(self, params):
        self._CertificateType = params.get("CertificateType")
        self._CertificateContent = params.get("CertificateContent")
        self._CertificateAlias = params.get("CertificateAlias")
        self._CertificateKey = params.get("CertificateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        """证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CreateCustomHeaderRequest(AbstractModel):
    """CreateCustomHeader请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则id
        :type RuleId: str
        :param _Headers: 新增的header名称和内容列表， ‘’$remote_addr‘’会被解析替换成客户端ip，其他值原样透传到源站。
        :type Headers: list of HttpHeaderParam
        """
        self._RuleId = None
        self._Headers = None

    @property
    def RuleId(self):
        """规则id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Headers(self):
        """新增的header名称和内容列表， ‘’$remote_addr‘’会被解析替换成客户端ip，其他值原样透传到源站。
        :rtype: list of HttpHeaderParam
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomHeaderResponse(AbstractModel):
    """CreateCustomHeader返回参数结构体

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


class CreateDomainErrorPageInfoRequest(AbstractModel):
    """CreateDomainErrorPageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _Domain: 域名
        :type Domain: str
        :param _ErrorNos: 原始错误码
        :type ErrorNos: list of int
        :param _Body: 新的响应包体
        :type Body: str
        :param _NewErrorNo: 新错误码
        :type NewErrorNo: int
        :param _ClearHeaders: 需要删除的响应头
        :type ClearHeaders: list of str
        :param _SetHeaders: 需要设置的响应头
        :type SetHeaders: list of HttpHeaderParam
        """
        self._ListenerId = None
        self._Domain = None
        self._ErrorNos = None
        self._Body = None
        self._NewErrorNo = None
        self._ClearHeaders = None
        self._SetHeaders = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
    def ErrorNos(self):
        """原始错误码
        :rtype: list of int
        """
        return self._ErrorNos

    @ErrorNos.setter
    def ErrorNos(self, ErrorNos):
        self._ErrorNos = ErrorNos

    @property
    def Body(self):
        """新的响应包体
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def NewErrorNo(self):
        """新错误码
        :rtype: int
        """
        return self._NewErrorNo

    @NewErrorNo.setter
    def NewErrorNo(self, NewErrorNo):
        self._NewErrorNo = NewErrorNo

    @property
    def ClearHeaders(self):
        """需要删除的响应头
        :rtype: list of str
        """
        return self._ClearHeaders

    @ClearHeaders.setter
    def ClearHeaders(self, ClearHeaders):
        self._ClearHeaders = ClearHeaders

    @property
    def SetHeaders(self):
        """需要设置的响应头
        :rtype: list of HttpHeaderParam
        """
        return self._SetHeaders

    @SetHeaders.setter
    def SetHeaders(self, SetHeaders):
        self._SetHeaders = SetHeaders


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._ErrorNos = params.get("ErrorNos")
        self._Body = params.get("Body")
        self._NewErrorNo = params.get("NewErrorNo")
        self._ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self._SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._SetHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainErrorPageInfoResponse(AbstractModel):
    """CreateDomainErrorPageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorPageId: 错误定制响应的配置ID
        :type ErrorPageId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorPageId = None
        self._RequestId = None

    @property
    def ErrorPageId(self):
        """错误定制响应的配置ID
        :rtype: str
        """
        return self._ErrorPageId

    @ErrorPageId.setter
    def ErrorPageId(self, ErrorPageId):
        self._ErrorPageId = ErrorPageId

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
        self._ErrorPageId = params.get("ErrorPageId")
        self._RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _Domain: 需要创建的域名，一个监听器下最大支持100个域名。
        :type Domain: str
        :param _CertificateId: 服务器证书，用于客户端与GAAP的HTTPS的交互。
        :type CertificateId: str
        :param _ClientCertificateId: 客户端CA证书，用于客户端与GAAP的HTTPS的交互。
仅当采用双向认证的方式时，需要设置该字段或PolyClientCertificateIds字段。
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: 客户端CA证书，用于客户端与GAAP的HTTPS的交互。
仅当采用双向认证的方式时，需要设置该字段或ClientCertificateId字段。
        :type PolyClientCertificateIds: list of str
        :param _Http3Supported: 是否开启Http3特性的标识，其中：
0，表示不开启Http3；
1，表示开启Http3。
默认不开启Http3。可以通过SetDomainHttp3开启。
        :type Http3Supported: int
        :param _IsDefaultServer: 是否作为默认域名，默认为“否”
        :type IsDefaultServer: bool
        """
        self._ListenerId = None
        self._Domain = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None
        self._Http3Supported = None
        self._IsDefaultServer = None

    @property
    def ListenerId(self):
        """监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        """需要创建的域名，一个监听器下最大支持100个域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertificateId(self):
        """服务器证书，用于客户端与GAAP的HTTPS的交互。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        """客户端CA证书，用于客户端与GAAP的HTTPS的交互。
仅当采用双向认证的方式时，需要设置该字段或PolyClientCertificateIds字段。
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        """客户端CA证书，用于客户端与GAAP的HTTPS的交互。
仅当采用双向认证的方式时，需要设置该字段或ClientCertificateId字段。
        :rtype: list of str
        """
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds

    @property
    def Http3Supported(self):
        """是否开启Http3特性的标识，其中：
0，表示不开启Http3；
1，表示开启Http3。
默认不开启Http3。可以通过SetDomainHttp3开启。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def IsDefaultServer(self):
        """是否作为默认域名，默认为“否”
        :rtype: bool
        """
        return self._IsDefaultServer

    @IsDefaultServer.setter
    def IsDefaultServer(self, IsDefaultServer):
        self._IsDefaultServer = IsDefaultServer


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self._Http3Supported = params.get("Http3Supported")
        self._IsDefaultServer = params.get("IsDefaultServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回参数结构体

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


class CreateGlobalDomainDnsRequest(AbstractModel):
    """CreateGlobalDomainDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _ProxyIdList: 通道ID列表
        :type ProxyIdList: list of str
        :param _NationCountryInnerCodes: 国家ID列表
        :type NationCountryInnerCodes: list of str
        """
        self._DomainId = None
        self._ProxyIdList = None
        self._NationCountryInnerCodes = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def ProxyIdList(self):
        """通道ID列表
        :rtype: list of str
        """
        return self._ProxyIdList

    @ProxyIdList.setter
    def ProxyIdList(self, ProxyIdList):
        self._ProxyIdList = ProxyIdList

    @property
    def NationCountryInnerCodes(self):
        """国家ID列表
        :rtype: list of str
        """
        return self._NationCountryInnerCodes

    @NationCountryInnerCodes.setter
    def NationCountryInnerCodes(self, NationCountryInnerCodes):
        self._NationCountryInnerCodes = NationCountryInnerCodes


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._ProxyIdList = params.get("ProxyIdList")
        self._NationCountryInnerCodes = params.get("NationCountryInnerCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalDomainDnsResponse(AbstractModel):
    """CreateGlobalDomainDns返回参数结构体

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


class CreateGlobalDomainRequest(AbstractModel):
    """CreateGlobalDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 域名所属项目ID
        :type ProjectId: int
        :param _DefaultValue: 域名默认入口
        :type DefaultValue: str
        :param _Alias: 别名
        :type Alias: str
        :param _TagSet: 标签列表
        :type TagSet: list of TagPair
        """
        self._ProjectId = None
        self._DefaultValue = None
        self._Alias = None
        self._TagSet = None

    @property
    def ProjectId(self):
        """域名所属项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DefaultValue(self):
        """域名默认入口
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Alias(self):
        """别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._DefaultValue = params.get("DefaultValue")
        self._Alias = params.get("Alias")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalDomainResponse(AbstractModel):
    """CreateGlobalDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainId = None
        self._RequestId = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

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
        self._DomainId = params.get("DomainId")
        self._RequestId = params.get("RequestId")


class CreateHTTPListenerRequest(AbstractModel):
    """CreateHTTPListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复
        :type Port: int
        :param _ProxyId: 通道ID，与GroupId不能同时设置，对应为通道创建监听器
        :type ProxyId: str
        :param _GroupId: 通道组ID，与ProxyId不能同时设置，对应为通道组创建监听器
        :type GroupId: str
        """
        self._ListenerName = None
        self._Port = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ProxyId(self):
        """通道ID，与GroupId不能同时设置，对应为通道创建监听器
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """通道组ID，与ProxyId不能同时设置，对应为通道组创建监听器
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHTTPListenerResponse(AbstractModel):
    """CreateHTTPListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 创建的监听器ID
        :type ListenerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerId = None
        self._RequestId = None

    @property
    def ListenerId(self):
        """创建的监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class CreateHTTPSListenerRequest(AbstractModel):
    """CreateHTTPSListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复
        :type Port: int
        :param _CertificateId: 服务器证书ID
        :type CertificateId: str
        :param _ForwardProtocol: 加速通道转发到源站的协议类型：HTTP | HTTPS
        :type ForwardProtocol: str
        :param _ProxyId: 通道ID，与GroupId之间只能设置一个。表示创建通道的监听器。
        :type ProxyId: str
        :param _AuthType: 认证类型，其中：
0，单向认证；
1，双向认证。
默认使用单向认证。
        :type AuthType: int
        :param _ClientCertificateId: 客户端CA单证书ID，仅当双向认证时设置该参数或PolyClientCertificateIds参数
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: 新的客户端多CA证书ID，仅当双向认证时设置该参数或设置ClientCertificateId参数
        :type PolyClientCertificateIds: list of str
        :param _GroupId: 通道组ID，与ProxyId之间只能设置一个。表示创建通道组的监听器。
        :type GroupId: str
        :param _Http3Supported: 支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
该功能的启停无法在监听器创建完毕后再修改。
        :type Http3Supported: int
        """
        self._ListenerName = None
        self._Port = None
        self._CertificateId = None
        self._ForwardProtocol = None
        self._ProxyId = None
        self._AuthType = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None
        self._GroupId = None
        self._Http3Supported = None

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CertificateId(self):
        """服务器证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ForwardProtocol(self):
        """加速通道转发到源站的协议类型：HTTP | HTTPS
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def ProxyId(self):
        """通道ID，与GroupId之间只能设置一个。表示创建通道的监听器。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def AuthType(self):
        """认证类型，其中：
0，单向认证；
1，双向认证。
默认使用单向认证。
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ClientCertificateId(self):
        """客户端CA单证书ID，仅当双向认证时设置该参数或PolyClientCertificateIds参数
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        """新的客户端多CA证书ID，仅当双向认证时设置该参数或设置ClientCertificateId参数
        :rtype: list of str
        """
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds

    @property
    def GroupId(self):
        """通道组ID，与ProxyId之间只能设置一个。表示创建通道组的监听器。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Http3Supported(self):
        """支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
该功能的启停无法在监听器创建完毕后再修改。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._CertificateId = params.get("CertificateId")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._ProxyId = params.get("ProxyId")
        self._AuthType = params.get("AuthType")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self._GroupId = params.get("GroupId")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHTTPSListenerResponse(AbstractModel):
    """CreateHTTPSListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 创建的监听器ID
        :type ListenerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerId = None
        self._RequestId = None

    @property
    def ListenerId(self):
        """创建的监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class CreateProxyGroupDomainRequest(AbstractModel):
    """CreateProxyGroupDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 需要开启域名的通道组ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """需要开启域名的通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyGroupDomainResponse(AbstractModel):
    """CreateProxyGroupDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID。
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        """通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateProxyGroupRequest(AbstractModel):
    """CreateProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 通道组所属项目ID
        :type ProjectId: int
        :param _GroupName: 通道组别名
        :type GroupName: str
        :param _RealServerRegion: 源站地域，参考接口 [https://cloud.tencent.com/document/api/608/36964] 返回参数RegionDetail中的RegionId
        :type RealServerRegion: str
        :param _TagSet: 标签列表
        :type TagSet: list of TagPair
        :param _AccessRegionSet: 加速地域列表，包括加速地域名，及该地域对应的带宽和并发配置。
        :type AccessRegionSet: list of AccessConfiguration
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _PackageType: 通道组套餐类型，可取值：Thunder、Accelerator，默认值Thunder
        :type PackageType: str
        :param _Http3Supported: 该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道组默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :type Http3Supported: int
        """
        self._ProjectId = None
        self._GroupName = None
        self._RealServerRegion = None
        self._TagSet = None
        self._AccessRegionSet = None
        self._IPAddressVersion = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def ProjectId(self):
        """通道组所属项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def GroupName(self):
        """通道组别名
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def RealServerRegion(self):
        """源站地域，参考接口 [https://cloud.tencent.com/document/api/608/36964] 返回参数RegionDetail中的RegionId
        :rtype: str
        """
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AccessRegionSet(self):
        """加速地域列表，包括加速地域名，及该地域对应的带宽和并发配置。
        :rtype: list of AccessConfiguration
        """
        return self._AccessRegionSet

    @AccessRegionSet.setter
    def AccessRegionSet(self, AccessRegionSet):
        self._AccessRegionSet = AccessRegionSet

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        """通道组套餐类型，可取值：Thunder、Accelerator，默认值Thunder
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        """该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道组默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._GroupName = params.get("GroupName")
        self._RealServerRegion = params.get("RealServerRegion")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("AccessRegionSet") is not None:
            self._AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessConfiguration()
                obj._deserialize(item)
                self._AccessRegionSet.append(obj)
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyGroupResponse(AbstractModel):
    """CreateProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        """通道组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateProxyRequest(AbstractModel):
    """CreateProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 通道的项目ID。
        :type ProjectId: int
        :param _ProxyName: 通道名称。
        :type ProxyName: str
        :param _AccessRegion: 接入地域。
        :type AccessRegion: str
        :param _Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param _Concurrent: 通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param _RealServerRegion: 源站地域。当GroupId存在时，源站地域为通道组的源站地域,此时可不填该字段。当GroupId不存在时，需要填写该字段
        :type RealServerRegion: str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _GroupId: 通道所在的通道组ID，当在通道组中创建通道时必带，否则忽略该字段。
        :type GroupId: str
        :param _TagSet: 通道需要添加的标签列表。
        :type TagSet: list of TagPair
        :param _ClonedProxyId: 被复制的通道ID。只有处于运行中状态的通道可以被复制。
当设置该参数时，表示复制该通道。
        :type ClonedProxyId: str
        :param _BillingType: 计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）
        :type BillingType: int
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _NetworkType: 网络类型，normal表示常规BGP，cn2表示精品BGP，triple表示三网
        :type NetworkType: str
        :param _PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        :param _Http3Supported: 该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :type Http3Supported: int
        """
        self._ProjectId = None
        self._ProxyName = None
        self._AccessRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._RealServerRegion = None
        self._ClientToken = None
        self._GroupId = None
        self._TagSet = None
        self._ClonedProxyId = None
        self._BillingType = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def ProjectId(self):
        """通道的项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProxyName(self):
        """通道名称。
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def AccessRegion(self):
        """接入地域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def Bandwidth(self):
        """通道带宽上限，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        """通道并发量上限，表示同时在线的连接数，单位：万。
        :rtype: int
        """
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def RealServerRegion(self):
        """源站地域。当GroupId存在时，源站地域为通道组的源站地域,此时可不填该字段。当GroupId不存在时，需要填写该字段
        :rtype: str
        """
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def GroupId(self):
        """通道所在的通道组ID，当在通道组中创建通道时必带，否则忽略该字段。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TagSet(self):
        """通道需要添加的标签列表。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def ClonedProxyId(self):
        """被复制的通道ID。只有处于运行中状态的通道可以被复制。
当设置该参数时，表示复制该通道。
        :rtype: str
        """
        return self._ClonedProxyId

    @ClonedProxyId.setter
    def ClonedProxyId(self, ClonedProxyId):
        self._ClonedProxyId = ClonedProxyId

    @property
    def BillingType(self):
        """计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        """网络类型，normal表示常规BGP，cn2表示精品BGP，triple表示三网
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        """通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        """该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProxyName = params.get("ProxyName")
        self._AccessRegion = params.get("AccessRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._RealServerRegion = params.get("RealServerRegion")
        self._ClientToken = params.get("ClientToken")
        self._GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._ClonedProxyId = params.get("ClonedProxyId")
        self._BillingType = params.get("BillingType")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyResponse(AbstractModel):
    """CreateProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 通道的实例ID。
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """通道的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 7层监听器ID
        :type ListenerId: str
        :param _Domain: 转发规则的域名
        :type Domain: str
        :param _Path: 转发规则的路径
        :type Path: str
        :param _RealServerType: 转发规则对应源站的类型，支持IP和DOMAIN类型。
        :type RealServerType: str
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数。
        :type Scheduler: str
        :param _HealthCheck: 规则是否开启健康检查，1开启，0关闭。
        :type HealthCheck: int
        :param _CheckParams: 源站健康检查相关参数
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param _ForwardProtocol: 加速通道转发到源站的协议类型：支持HTTP或HTTPS。
不传递该字段时表示使用对应监听器的ForwardProtocol。
        :type ForwardProtocol: str
        :param _ForwardHost: 回源Host。加速通道转发到源站的host，不设置该参数时，使用默认的host设置，即客户端发起的http请求的host。
        :type ForwardHost: str
        :param _ServerNameIndicationSwitch: 服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。创建HTTP监听器转发规则时，SNI功能默认关闭。
        :type ServerNameIndicationSwitch: str
        :param _ServerNameIndication: 服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
        :type ServerNameIndication: str
        :param _ForcedRedirect: HTTP强制跳转HTTPS。输入当前规则对应的域名与地址。
        :type ForcedRedirect: str
        """
        self._ListenerId = None
        self._Domain = None
        self._Path = None
        self._RealServerType = None
        self._Scheduler = None
        self._HealthCheck = None
        self._CheckParams = None
        self._ForwardProtocol = None
        self._ForwardHost = None
        self._ServerNameIndicationSwitch = None
        self._ServerNameIndication = None
        self._ForcedRedirect = None

    @property
    def ListenerId(self):
        """7层监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        """转发规则的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Path(self):
        """转发规则的路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def RealServerType(self):
        """转发规则对应源站的类型，支持IP和DOMAIN类型。
        :rtype: str
        """
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        """规则是否开启健康检查，1开启，0关闭。
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckParams(self):
        """源站健康检查相关参数
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        """
        return self._CheckParams

    @CheckParams.setter
    def CheckParams(self, CheckParams):
        self._CheckParams = CheckParams

    @property
    def ForwardProtocol(self):
        """加速通道转发到源站的协议类型：支持HTTP或HTTPS。
不传递该字段时表示使用对应监听器的ForwardProtocol。
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def ForwardHost(self):
        """回源Host。加速通道转发到源站的host，不设置该参数时，使用默认的host设置，即客户端发起的http请求的host。
        :rtype: str
        """
        return self._ForwardHost

    @ForwardHost.setter
    def ForwardHost(self, ForwardHost):
        self._ForwardHost = ForwardHost

    @property
    def ServerNameIndicationSwitch(self):
        """服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。创建HTTP监听器转发规则时，SNI功能默认关闭。
        :rtype: str
        """
        return self._ServerNameIndicationSwitch

    @ServerNameIndicationSwitch.setter
    def ServerNameIndicationSwitch(self, ServerNameIndicationSwitch):
        self._ServerNameIndicationSwitch = ServerNameIndicationSwitch

    @property
    def ServerNameIndication(self):
        """服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
        :rtype: str
        """
        return self._ServerNameIndication

    @ServerNameIndication.setter
    def ServerNameIndication(self, ServerNameIndication):
        self._ServerNameIndication = ServerNameIndication

    @property
    def ForcedRedirect(self):
        """HTTP强制跳转HTTPS。输入当前规则对应的域名与地址。
        :rtype: str
        """
        return self._ForcedRedirect

    @ForcedRedirect.setter
    def ForcedRedirect(self, ForcedRedirect):
        self._ForcedRedirect = ForcedRedirect


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._Path = params.get("Path")
        self._RealServerType = params.get("RealServerType")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self._CheckParams = RuleCheckParams()
            self._CheckParams._deserialize(params.get("CheckParams"))
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._ForwardHost = params.get("ForwardHost")
        self._ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self._ServerNameIndication = params.get("ServerNameIndication")
        self._ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 创建转发规则成功返回规则ID
        :type RuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._RequestId = None

    @property
    def RuleId(self):
        """创建转发规则成功返回规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

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
        self._RuleId = params.get("RuleId")
        self._RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DefaultAction: 默认策略：ACCEPT或DROP
        :type DefaultAction: str
        :param _ProxyId: 加速通道ID
        :type ProxyId: str
        :param _GroupId: 通道组ID
        :type GroupId: str
        """
        self._DefaultAction = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def DefaultAction(self):
        """默认策略：ACCEPT或DROP
        :rtype: str
        """
        return self._DefaultAction

    @DefaultAction.setter
    def DefaultAction(self, DefaultAction):
        self._DefaultAction = DefaultAction

    @property
    def ProxyId(self):
        """加速通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """通道组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._DefaultAction = params.get("DefaultAction")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateSecurityRulesRequest(AbstractModel):
    """CreateSecurityRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        :param _RuleList: 访问规则列表
        :type RuleList: list of SecurityPolicyRuleIn
        """
        self._PolicyId = None
        self._RuleList = None

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleList(self):
        """访问规则列表
        :rtype: list of SecurityPolicyRuleIn
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleIn()
                obj._deserialize(item)
                self._RuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityRulesResponse(AbstractModel):
    """CreateSecurityRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIdList: 规则ID列表
        :type RuleIdList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleIdList = None
        self._RequestId = None

    @property
    def RuleIdList(self):
        """规则ID列表
        :rtype: list of str
        """
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList

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
        self._RuleIdList = params.get("RuleIdList")
        self._RequestId = params.get("RequestId")


class CreateTCPListenersRequest(AbstractModel):
    """CreateTCPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerName: 监听器名称。
        :type ListenerName: str
        :param _Ports: 监听器端口列表。
        :type Ports: list of int non-negative
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _HealthCheck: 源站是否开启健康检查：1开启，0关闭，UDP监听器不支持健康检查
        :type HealthCheck: int
        :param _RealServerType: 监听器绑定源站类型。IP表示IP地址，DOMAIN表示域名。
        :type RealServerType: str
        :param _ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param _GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param _DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param _ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param _RealServerPorts: 源站端口列表，该参数仅支持v1版本监听器和通道组监听器。
        :type RealServerPorts: list of int non-negative
        :param _ClientIPMethod: 监听器获取客户端 IP 的方式，0表示 TOA, 1表示Proxy Protocol
        :type ClientIPMethod: int
        :param _FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param _HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        """
        self._ListenerName = None
        self._Ports = None
        self._Scheduler = None
        self._HealthCheck = None
        self._RealServerType = None
        self._ProxyId = None
        self._GroupId = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._RealServerPorts = None
        self._ClientIPMethod = None
        self._FailoverSwitch = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None

    @property
    def ListenerName(self):
        """监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Ports(self):
        """监听器端口列表。
        :rtype: list of int non-negative
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        """源站是否开启健康检查：1开启，0关闭，UDP监听器不支持健康检查
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def RealServerType(self):
        """监听器绑定源站类型。IP表示IP地址，DOMAIN表示域名。
        :rtype: str
        """
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def ProxyId(self):
        """通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DelayLoop(self):
        """源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        """源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def RealServerPorts(self):
        """源站端口列表，该参数仅支持v1版本监听器和通道组监听器。
        :rtype: list of int non-negative
        """
        return self._RealServerPorts

    @RealServerPorts.setter
    def RealServerPorts(self, RealServerPorts):
        self._RealServerPorts = RealServerPorts

    @property
    def ClientIPMethod(self):
        """监听器获取客户端 IP 的方式，0表示 TOA, 1表示Proxy Protocol
        :rtype: int
        """
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def FailoverSwitch(self):
        """源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :rtype: int
        """
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthyThreshold(self):
        """健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        """不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Ports = params.get("Ports")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        self._RealServerType = params.get("RealServerType")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._RealServerPorts = params.get("RealServerPorts")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTCPListenersResponse(AbstractModel):
    """CreateTCPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 返回监听器ID
        :type ListenerIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        """返回监听器ID
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

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
        self._ListenerIds = params.get("ListenerIds")
        self._RequestId = params.get("RequestId")


class CreateUDPListenersRequest(AbstractModel):
    """CreateUDPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Ports: 监听器端口列表
        :type Ports: list of int non-negative
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _RealServerType: 监听器绑定源站类型。IP表示IP地址，DOMAIN表示域名。
        :type RealServerType: str
        :param _ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param _GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param _RealServerPorts: 源站端口列表，该参数仅支持v1版本监听器和通道组监听器
        :type RealServerPorts: list of int non-negative
        :param _DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param _ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param _HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param _HealthCheck: 源站是否开启健康检查：1开启，0关闭。
        :type HealthCheck: int
        :param _CheckType: UDP源站健康类型。PORT表示检查端口，PING表示PING。
        :type CheckType: str
        :param _CheckPort: UDP源站健康检查探测端口。
        :type CheckPort: int
        :param _ContextType: UDP源站健康检查端口探测报文类型：TEXT表示文本。仅在健康检查类型为PORT时使用。
        :type ContextType: str
        :param _SendContext: UDP源站健康检查端口探测发送报文。仅在健康检查类型为PORT时使用。
        :type SendContext: str
        :param _RecvContext: UDP源站健康检查端口探测接收报文。仅在健康检查类型为PORT时使用。
        :type RecvContext: str
        """
        self._ListenerName = None
        self._Ports = None
        self._Scheduler = None
        self._RealServerType = None
        self._ProxyId = None
        self._GroupId = None
        self._RealServerPorts = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._HealthCheck = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Ports(self):
        """监听器端口列表
        :rtype: list of int non-negative
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def RealServerType(self):
        """监听器绑定源站类型。IP表示IP地址，DOMAIN表示域名。
        :rtype: str
        """
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def ProxyId(self):
        """通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RealServerPorts(self):
        """源站端口列表，该参数仅支持v1版本监听器和通道组监听器
        :rtype: list of int non-negative
        """
        return self._RealServerPorts

    @RealServerPorts.setter
    def RealServerPorts(self, RealServerPorts):
        self._RealServerPorts = RealServerPorts

    @property
    def DelayLoop(self):
        """源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        """源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthyThreshold(self):
        """健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        """不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        """源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :rtype: int
        """
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthCheck(self):
        """源站是否开启健康检查：1开启，0关闭。
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckType(self):
        """UDP源站健康类型。PORT表示检查端口，PING表示PING。
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        """UDP源站健康检查探测端口。
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        """UDP源站健康检查端口探测报文类型：TEXT表示文本。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        """UDP源站健康检查端口探测发送报文。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        """UDP源站健康检查端口探测接收报文。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext


    def _deserialize(self, params):
        self._ListenerName = params.get("ListenerName")
        self._Ports = params.get("Ports")
        self._Scheduler = params.get("Scheduler")
        self._RealServerType = params.get("RealServerType")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._RealServerPorts = params.get("RealServerPorts")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthCheck = params.get("HealthCheck")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUDPListenersResponse(AbstractModel):
    """CreateUDPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 返回监听器ID
        :type ListenerIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        """返回监听器ID
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

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
        self._ListenerIds = params.get("ListenerIds")
        self._RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 需要删除的证书ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """需要删除的证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回参数结构体

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


class DeleteDomainErrorPageInfoRequest(AbstractModel):
    """DeleteDomainErrorPageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorPageId: 定制错误响应页的唯一ID，请参考CreateDomainErrorPageInfo的响应
        :type ErrorPageId: str
        """
        self._ErrorPageId = None

    @property
    def ErrorPageId(self):
        """定制错误响应页的唯一ID，请参考CreateDomainErrorPageInfo的响应
        :rtype: str
        """
        return self._ErrorPageId

    @ErrorPageId.setter
    def ErrorPageId(self, ErrorPageId):
        self._ErrorPageId = ErrorPageId


    def _deserialize(self, params):
        self._ErrorPageId = params.get("ErrorPageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainErrorPageInfoResponse(AbstractModel):
    """DeleteDomainErrorPageInfo返回参数结构体

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


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _Domain: 需要删除的域名
        :type Domain: str
        :param _Force: 是否强制删除已绑定源站的转发规则，0非强制，1强制。
当采用非强制删除时，如果域名下已有规则绑定了源站，则无法删除。
        :type Force: int
        """
        self._ListenerId = None
        self._Domain = None
        self._Force = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        """需要删除的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Force(self):
        """是否强制删除已绑定源站的转发规则，0非强制，1强制。
当采用非强制删除时，如果域名下已有规则绑定了源站，则无法删除。
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回参数结构体

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


class DeleteGlobalDomainDnsRequest(AbstractModel):
    """DeleteGlobalDomainDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DnsRecordId: 解析记录的ID
        :type DnsRecordId: int
        """
        self._DnsRecordId = None

    @property
    def DnsRecordId(self):
        """解析记录的ID
        :rtype: int
        """
        return self._DnsRecordId

    @DnsRecordId.setter
    def DnsRecordId(self, DnsRecordId):
        self._DnsRecordId = DnsRecordId


    def _deserialize(self, params):
        self._DnsRecordId = params.get("DnsRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalDomainDnsResponse(AbstractModel):
    """DeleteGlobalDomainDns返回参数结构体

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


class DeleteGlobalDomainRequest(AbstractModel):
    """DeleteGlobalDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        """
        self._DomainId = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalDomainResponse(AbstractModel):
    """DeleteGlobalDomain返回参数结构体

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


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 待删除的监听器ID列表
        :type ListenerIds: list of str
        :param _Force: 已绑定源站的监听器是否允许强制删除，1：允许， 0：不允许
        :type Force: int
        :param _GroupId: 通道组ID，该参数和ProxyId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param _ProxyId: 通道ID，该参数和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        """
        self._ListenerIds = None
        self._Force = None
        self._GroupId = None
        self._ProxyId = None

    @property
    def ListenerIds(self):
        """待删除的监听器ID列表
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Force(self):
        """已绑定源站的监听器是否允许强制删除，1：允许， 0：不允许
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def GroupId(self):
        """通道组ID，该参数和ProxyId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ProxyId(self):
        """通道ID，该参数和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._Force = params.get("Force")
        self._GroupId = params.get("GroupId")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenersResponse(AbstractModel):
    """DeleteListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OperationFailedListenerSet: 删除操作失败的监听器ID列表
        :type OperationFailedListenerSet: list of str
        :param _OperationSucceedListenerSet: 删除操作成功的监听器ID列表
        :type OperationSucceedListenerSet: list of str
        :param _InvalidStatusListenerSet: 无效的监听器ID列表，如：监听器不存在，监听器对应实例不匹配
        :type InvalidStatusListenerSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OperationFailedListenerSet = None
        self._OperationSucceedListenerSet = None
        self._InvalidStatusListenerSet = None
        self._RequestId = None

    @property
    def OperationFailedListenerSet(self):
        """删除操作失败的监听器ID列表
        :rtype: list of str
        """
        return self._OperationFailedListenerSet

    @OperationFailedListenerSet.setter
    def OperationFailedListenerSet(self, OperationFailedListenerSet):
        self._OperationFailedListenerSet = OperationFailedListenerSet

    @property
    def OperationSucceedListenerSet(self):
        """删除操作成功的监听器ID列表
        :rtype: list of str
        """
        return self._OperationSucceedListenerSet

    @OperationSucceedListenerSet.setter
    def OperationSucceedListenerSet(self, OperationSucceedListenerSet):
        self._OperationSucceedListenerSet = OperationSucceedListenerSet

    @property
    def InvalidStatusListenerSet(self):
        """无效的监听器ID列表，如：监听器不存在，监听器对应实例不匹配
        :rtype: list of str
        """
        return self._InvalidStatusListenerSet

    @InvalidStatusListenerSet.setter
    def InvalidStatusListenerSet(self, InvalidStatusListenerSet):
        self._InvalidStatusListenerSet = InvalidStatusListenerSet

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
        self._OperationFailedListenerSet = params.get("OperationFailedListenerSet")
        self._OperationSucceedListenerSet = params.get("OperationSucceedListenerSet")
        self._InvalidStatusListenerSet = params.get("InvalidStatusListenerSet")
        self._RequestId = params.get("RequestId")


class DeleteProxyGroupRequest(AbstractModel):
    """DeleteProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 需要删除的通道组ID。
        :type GroupId: str
        :param _Force: 强制删除标识。其中：
0，不强制删除，
1，强制删除。
默认为0，当通道组中存在通道或通道组中存在监听器/规则绑定了源站时，且Force为0时，该操作会返回失败。
        :type Force: int
        """
        self._GroupId = None
        self._Force = None

    @property
    def GroupId(self):
        """需要删除的通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Force(self):
        """强制删除标识。其中：
0，不强制删除，
1，强制删除。
默认为0，当通道组中存在通道或通道组中存在监听器/规则绑定了源站时，且Force为0时，该操作会返回失败。
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProxyGroupResponse(AbstractModel):
    """DeleteProxyGroup返回参数结构体

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


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 7层监听器ID
        :type ListenerId: str
        :param _RuleId: 转发规则ID
        :type RuleId: str
        :param _Force: 是否可以强制删除已绑定源站的转发规则，0非强制，1强制
        :type Force: int
        """
        self._ListenerId = None
        self._RuleId = None
        self._Force = None

    @property
    def ListenerId(self):
        """7层监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleId(self):
        """转发规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Force(self):
        """是否可以强制删除已绑定源站的转发规则，0非强制，1强制
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RuleId = params.get("RuleId")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

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


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: str
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        """策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy返回参数结构体

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


class DeleteSecurityRulesRequest(AbstractModel):
    """DeleteSecurityRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        :param _RuleIdList: 访问规则ID列表
        :type RuleIdList: list of str
        """
        self._PolicyId = None
        self._RuleIdList = None

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleIdList(self):
        """访问规则ID列表
        :rtype: list of str
        """
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityRulesResponse(AbstractModel):
    """DeleteSecurityRules返回参数结构体

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


class DescribeAccessRegionsByDestRegionRequest(AbstractModel):
    """DescribeAccessRegionsByDestRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DestRegion: 源站区域：接口DescribeDestRegions返回DestRegionSet中的RegionId字段值
        :type DestRegion: str
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        """
        self._DestRegion = None
        self._IPAddressVersion = None
        self._PackageType = None

    @property
    def DestRegion(self):
        """源站区域：接口DescribeDestRegions返回DestRegionSet中的RegionId字段值
        :rtype: str
        """
        return self._DestRegion

    @DestRegion.setter
    def DestRegion(self, DestRegion):
        self._DestRegion = DestRegion

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        """通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._DestRegion = params.get("DestRegion")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRegionsByDestRegionResponse(AbstractModel):
    """DescribeAccessRegionsByDestRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可用加速区域数量
        :type TotalCount: int
        :param _AccessRegionSet: 可用加速区域信息列表
        :type AccessRegionSet: list of AccessRegionDetial
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccessRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """可用加速区域数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessRegionSet(self):
        """可用加速区域信息列表
        :rtype: list of AccessRegionDetial
        """
        return self._AccessRegionSet

    @AccessRegionSet.setter
    def AccessRegionSet(self, AccessRegionSet):
        self._AccessRegionSet = AccessRegionSet

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
        if params.get("AccessRegionSet") is not None:
            self._AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessRegionDetial()
                obj._deserialize(item)
                self._AccessRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAccessRegionsRequest(AbstractModel):
    """DescribeAccessRegions请求参数结构体

    """


class DescribeAccessRegionsResponse(AbstractModel):
    """DescribeAccessRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 加速区域总数
        :type TotalCount: int
        :param _AccessRegionSet: 加速区域详情列表
        :type AccessRegionSet: list of RegionDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccessRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """加速区域总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessRegionSet(self):
        """加速区域详情列表
        :rtype: list of RegionDetail
        """
        return self._AccessRegionSet

    @AccessRegionSet.setter
    def AccessRegionSet(self, AccessRegionSet):
        self._AccessRegionSet = AccessRegionSet

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
        if params.get("AccessRegionSet") is not None:
            self._AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._AccessRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuthSignatureRequest(AbstractModel):
    """DescribeAuthSignature请求参数结构体

    """


class DescribeAuthSignatureResponse(AbstractModel):
    """DescribeAuthSignature返回参数结构体

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


class DescribeBlackHeaderRequest(AbstractModel):
    """DescribeBlackHeader请求参数结构体

    """


class DescribeBlackHeaderResponse(AbstractModel):
    """DescribeBlackHeader返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlackHeaders: 禁用的自定义header列表
        :type BlackHeaders: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlackHeaders = None
        self._RequestId = None

    @property
    def BlackHeaders(self):
        """禁用的自定义header列表
        :rtype: list of str
        """
        return self._BlackHeaders

    @BlackHeaders.setter
    def BlackHeaders(self, BlackHeaders):
        self._BlackHeaders = BlackHeaders

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
        self._BlackHeaders = params.get("BlackHeaders")
        self._RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        """证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateDetail: 证书详情。
        :type CertificateDetail: :class:`tencentcloud.gaap.v20180529.models.CertificateDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateDetail = None
        self._RequestId = None

    @property
    def CertificateDetail(self):
        """证书详情。
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CertificateDetail`
        """
        return self._CertificateDetail

    @CertificateDetail.setter
    def CertificateDetail(self, CertificateDetail):
        self._CertificateDetail = CertificateDetail

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
        if params.get("CertificateDetail") is not None:
            self._CertificateDetail = CertificateDetail()
            self._CertificateDetail._deserialize(params.get("CertificateDetail"))
        self._RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateType: 证书类型。其中：
0，表示基础认证配置；
1，表示客户端CA证书；
2，表示服务器SSL证书；
3，表示源站CA证书；
4，表示通道SSL证书。
-1，所有类型。
默认为-1。
        :type CertificateType: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 限制数量，默认为20。
        :type Limit: int
        """
        self._CertificateType = None
        self._Offset = None
        self._Limit = None

    @property
    def CertificateType(self):
        """证书类型。其中：
0，表示基础认证配置；
1，表示客户端CA证书；
2，表示服务器SSL证书；
3，表示源站CA证书；
4，表示通道SSL证书。
-1，所有类型。
默认为-1。
        :rtype: int
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数量，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._CertificateType = params.get("CertificateType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateSet: 服务器证书列表，包括证书ID 和证书名称。
        :type CertificateSet: list of Certificate
        :param _TotalCount: 满足查询条件的服务器证书总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def CertificateSet(self):
        """服务器证书列表，包括证书ID 和证书名称。
        :rtype: list of Certificate
        """
        return self._CertificateSet

    @CertificateSet.setter
    def CertificateSet(self, CertificateSet):
        self._CertificateSet = CertificateSet

    @property
    def TotalCount(self):
        """满足查询条件的服务器证书总数量。
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
        if params.get("CertificateSet") is not None:
            self._CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = Certificate()
                obj._deserialize(item)
                self._CertificateSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCountryAreaMappingRequest(AbstractModel):
    """DescribeCountryAreaMapping请求参数结构体

    """


class DescribeCountryAreaMappingResponse(AbstractModel):
    """DescribeCountryAreaMapping返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CountryAreaMappingList: 国家地区编码映射表。
        :type CountryAreaMappingList: list of CountryAreaMap
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CountryAreaMappingList = None
        self._RequestId = None

    @property
    def CountryAreaMappingList(self):
        """国家地区编码映射表。
        :rtype: list of CountryAreaMap
        """
        return self._CountryAreaMappingList

    @CountryAreaMappingList.setter
    def CountryAreaMappingList(self, CountryAreaMappingList):
        self._CountryAreaMappingList = CountryAreaMappingList

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
        if params.get("CountryAreaMappingList") is not None:
            self._CountryAreaMappingList = []
            for item in params.get("CountryAreaMappingList"):
                obj = CountryAreaMap()
                obj._deserialize(item)
                self._CountryAreaMappingList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCrossBorderProxiesRequest(AbstractModel):
    """DescribeCrossBorderProxies请求参数结构体

    """


class DescribeCrossBorderProxiesResponse(AbstractModel):
    """DescribeCrossBorderProxies返回参数结构体

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


class DescribeCustomHeaderRequest(AbstractModel):
    """DescribeCustomHeader请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        """规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomHeaderResponse(AbstractModel):
    """DescribeCustomHeader返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则id
        :type RuleId: str
        :param _Headers: 自定义header列表
        :type Headers: list of HttpHeaderParam
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleId = None
        self._Headers = None
        self._RequestId = None

    @property
    def RuleId(self):
        """规则id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Headers(self):
        """自定义header列表
        :rtype: list of HttpHeaderParam
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

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
        self._RuleId = params.get("RuleId")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDestRegionsRequest(AbstractModel):
    """DescribeDestRegions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QualityType: 通道质量:0表示金牌，1表示银牌。默认不传该参数，表示金牌。本参数确定查询指定通道质量的源站区域
        :type QualityType: int
        """
        self._QualityType = None

    @property
    def QualityType(self):
        """通道质量:0表示金牌，1表示银牌。默认不传该参数，表示金牌。本参数确定查询指定通道质量的源站区域
        :rtype: int
        """
        return self._QualityType

    @QualityType.setter
    def QualityType(self, QualityType):
        self._QualityType = QualityType


    def _deserialize(self, params):
        self._QualityType = params.get("QualityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDestRegionsResponse(AbstractModel):
    """DescribeDestRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 源站区域总数
        :type TotalCount: int
        :param _DestRegionSet: 源站区域详情列表
        :type DestRegionSet: list of RegionDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DestRegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """源站区域总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DestRegionSet(self):
        """源站区域详情列表
        :rtype: list of RegionDetail
        """
        return self._DestRegionSet

    @DestRegionSet.setter
    def DestRegionSet(self, DestRegionSet):
        self._DestRegionSet = DestRegionSet

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
        if params.get("DestRegionSet") is not None:
            self._DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._DestRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoByIdsRequest(AbstractModel):
    """DescribeDomainErrorPageInfoByIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorPageIds: 定制错误ID列表，最多支持10个
        :type ErrorPageIds: list of str
        """
        self._ErrorPageIds = None

    @property
    def ErrorPageIds(self):
        """定制错误ID列表，最多支持10个
        :rtype: list of str
        """
        return self._ErrorPageIds

    @ErrorPageIds.setter
    def ErrorPageIds(self, ErrorPageIds):
        self._ErrorPageIds = ErrorPageIds


    def _deserialize(self, params):
        self._ErrorPageIds = params.get("ErrorPageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainErrorPageInfoByIdsResponse(AbstractModel):
    """DescribeDomainErrorPageInfoByIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorPageSet: 定制错误响应配置集
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorPageSet = None
        self._RequestId = None

    @property
    def ErrorPageSet(self):
        """定制错误响应配置集
        :rtype: list of DomainErrorPageInfo
        """
        return self._ErrorPageSet

    @ErrorPageSet.setter
    def ErrorPageSet(self, ErrorPageSet):
        self._ErrorPageSet = ErrorPageSet

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
        if params.get("ErrorPageSet") is not None:
            self._ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self._ErrorPageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoRequest(AbstractModel):
    """DescribeDomainErrorPageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _Domain: 域名
        :type Domain: str
        """
        self._ListenerId = None
        self._Domain = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainErrorPageInfoResponse(AbstractModel):
    """DescribeDomainErrorPageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrorPageSet: 定制错误响应配置集
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrorPageSet = None
        self._RequestId = None

    @property
    def ErrorPageSet(self):
        """定制错误响应配置集
        :rtype: list of DomainErrorPageInfo
        """
        return self._ErrorPageSet

    @ErrorPageSet.setter
    def ErrorPageSet(self, ErrorPageSet):
        self._ErrorPageSet = ErrorPageSet

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
        if params.get("ErrorPageSet") is not None:
            self._ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self._ErrorPageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGlobalDomainDnsRequest(AbstractModel):
    """DescribeGlobalDomainDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        """
        self._DomainId = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalDomainDnsResponse(AbstractModel):
    """DescribeGlobalDomainDns返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalDnsList: DNS解析记录详细信息列表
        :type GlobalDnsList: list of GlobalDns
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GlobalDnsList = None
        self._RequestId = None

    @property
    def GlobalDnsList(self):
        """DNS解析记录详细信息列表
        :rtype: list of GlobalDns
        """
        return self._GlobalDnsList

    @GlobalDnsList.setter
    def GlobalDnsList(self, GlobalDnsList):
        self._GlobalDnsList = GlobalDnsList

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
        if params.get("GlobalDnsList") is not None:
            self._GlobalDnsList = []
            for item in params.get("GlobalDnsList"):
                obj = GlobalDns()
                obj._deserialize(item)
                self._GlobalDnsList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGlobalDomainsRequest(AbstractModel):
    """DescribeGlobalDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页数量限制
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，域名会被拉取出来。
        :type TagSet: list of TagPair
        """
        self._ProjectId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._TagSet = None

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页数量限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagSet(self):
        """标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，域名会被拉取出来。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlobalDomainsResponse(AbstractModel):
    """DescribeGlobalDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 域名信息列表
        :type Domains: list of Domain
        :param _TotalCount: 总记录数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Domains(self):
        """域名信息列表
        :rtype: list of Domain
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalCount(self):
        """总记录数
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
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = Domain()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGroupAndStatisticsProxyRequest(AbstractModel):
    """DescribeGroupAndStatisticsProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupAndStatisticsProxyResponse(AbstractModel):
    """DescribeGroupAndStatisticsProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupSet: 可以统计的通道组信息
        :type GroupSet: list of GroupStatisticsInfo
        :param _TotalCount: 通道组数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GroupSet(self):
        """可以统计的通道组信息
        :rtype: list of GroupStatisticsInfo
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def TotalCount(self):
        """通道组数量
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
        if params.get("GroupSet") is not None:
            self._GroupSet = []
            for item in params.get("GroupSet"):
                obj = GroupStatisticsInfo()
                obj._deserialize(item)
                self._GroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGroupDomainConfigRequest(AbstractModel):
    """DescribeGroupDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupDomainConfigResponse(AbstractModel):
    """DescribeGroupDomainConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRegionList: 域名解析就近接入配置列表。
        :type AccessRegionList: list of DomainAccessRegionDict
        :param _DefaultDnsIp: 默认访问Ip。
        :type DefaultDnsIp: str
        :param _GroupId: 通道组ID。
        :type GroupId: str
        :param _AccessRegionCount: 接入地域的配置的总数。
        :type AccessRegionCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessRegionList = None
        self._DefaultDnsIp = None
        self._GroupId = None
        self._AccessRegionCount = None
        self._RequestId = None

    @property
    def AccessRegionList(self):
        """域名解析就近接入配置列表。
        :rtype: list of DomainAccessRegionDict
        """
        return self._AccessRegionList

    @AccessRegionList.setter
    def AccessRegionList(self, AccessRegionList):
        self._AccessRegionList = AccessRegionList

    @property
    def DefaultDnsIp(self):
        """默认访问Ip。
        :rtype: str
        """
        return self._DefaultDnsIp

    @DefaultDnsIp.setter
    def DefaultDnsIp(self, DefaultDnsIp):
        self._DefaultDnsIp = DefaultDnsIp

    @property
    def GroupId(self):
        """通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def AccessRegionCount(self):
        """接入地域的配置的总数。
        :rtype: int
        """
        return self._AccessRegionCount

    @AccessRegionCount.setter
    def AccessRegionCount(self, AccessRegionCount):
        self._AccessRegionCount = AccessRegionCount

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
        if params.get("AccessRegionList") is not None:
            self._AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = DomainAccessRegionDict()
                obj._deserialize(item)
                self._AccessRegionList.append(obj)
        self._DefaultDnsIp = params.get("DefaultDnsIp")
        self._GroupId = params.get("GroupId")
        self._AccessRegionCount = params.get("AccessRegionCount")
        self._RequestId = params.get("RequestId")


class DescribeHTTPListenersRequest(AbstractModel):
    """DescribeHTTPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :type ProxyId: str
        :param _GroupId: 通道组ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :type GroupId: str
        :param _ListenerId: 过滤条件，按照监听器ID进行精确查询。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :type ListenerId: str
        :param _ListenerName: 过滤条件，按照监听器名称进行精确查询
        :type ListenerName: str
        :param _Port: 过滤条件，按照监听器端口进行精确查询
        :type Port: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 限制数量，默认为20个
        :type Limit: int
        :param _SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :type SearchValue: str
        """
        self._ProxyId = None
        self._GroupId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._SearchValue = None

    @property
    def ProxyId(self):
        """通道ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """通道组ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ListenerId(self):
        """过滤条件，按照监听器ID进行精确查询。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """过滤条件，按照监听器名称进行精确查询
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """过滤条件，按照监听器端口进行精确查询
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数量，默认为20个
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchValue(self):
        """过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHTTPListenersResponse(AbstractModel):
    """DescribeHTTPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 监听器数量
        :type TotalCount: int
        :param _ListenerSet: HTTP监听器列表
        :type ListenerSet: list of HTTPListener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """监听器数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        """HTTP监听器列表
        :rtype: list of HTTPListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

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
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHTTPSListenersRequest(AbstractModel):
    """DescribeHTTPSListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :type ProxyId: str
        :param _GroupId: 通道组ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :type GroupId: str
        :param _ListenerId: 过滤条件，根据监听器ID进行精确查询。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :type ListenerId: str
        :param _ListenerName: 过滤条件，根据监听器名称进行精确查询。
        :type ListenerName: str
        :param _Port: 过滤条件，根据监听器端口进行精确查询。
        :type Port: int
        :param _Offset: 偏移量， 默认为0
        :type Offset: int
        :param _Limit: 限制数量，默认为20
        :type Limit: int
        :param _SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询
        :type SearchValue: str
        :param _Http3Supported: 支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
该功能的启停无法在监听器创建完毕后再修改。
        :type Http3Supported: int
        """
        self._ProxyId = None
        self._GroupId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._SearchValue = None
        self._Http3Supported = None

    @property
    def ProxyId(self):
        """通道ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """通道组ID。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ListenerId(self):
        """过滤条件，根据监听器ID进行精确查询。ListenerId、ProxyId、GroupId须至少填写一个，且ProxyId与GroupId至多只能填写其中一个。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """过滤条件，根据监听器名称进行精确查询。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """过滤条件，根据监听器端口进行精确查询。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Offset(self):
        """偏移量， 默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数量，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchValue(self):
        """过滤条件，支持按照端口或监听器名称进行模糊查询
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Http3Supported(self):
        """支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
该功能的启停无法在监听器创建完毕后再修改。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchValue = params.get("SearchValue")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHTTPSListenersResponse(AbstractModel):
    """DescribeHTTPSListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 监听器数量
        :type TotalCount: int
        :param _ListenerSet: HTTPS监听器列表
        :type ListenerSet: list of HTTPSListener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """监听器数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        """HTTPS监听器列表
        :rtype: list of HTTPSListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

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
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPSListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerRealServersRequest(AbstractModel):
    """DescribeListenerRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        """
        self._ListenerId = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerRealServersResponse(AbstractModel):
    """DescribeListenerRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可绑定源站的个数
        :type TotalCount: int
        :param _RealServerSet: 源站信息列表
        :type RealServerSet: list of RealServer
        :param _BindRealServerTotalCount: 已绑定源站的个数
        :type BindRealServerTotalCount: int
        :param _BindRealServerSet: 已绑定源站信息列表
        :type BindRealServerSet: list of BindRealServer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealServerSet = None
        self._BindRealServerTotalCount = None
        self._BindRealServerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """可绑定源站的个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealServerSet(self):
        """源站信息列表
        :rtype: list of RealServer
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def BindRealServerTotalCount(self):
        """已绑定源站的个数
        :rtype: int
        """
        return self._BindRealServerTotalCount

    @BindRealServerTotalCount.setter
    def BindRealServerTotalCount(self, BindRealServerTotalCount):
        self._BindRealServerTotalCount = BindRealServerTotalCount

    @property
    def BindRealServerSet(self):
        """已绑定源站信息列表
        :rtype: list of BindRealServer
        """
        return self._BindRealServerSet

    @BindRealServerSet.setter
    def BindRealServerSet(self, BindRealServerSet):
        self._BindRealServerSet = BindRealServerSet

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
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self._BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._BindRealServerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenerStatisticsRequest(AbstractModel):
    """DescribeListenerStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _MetricNames: 统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets。
        :type MetricNames: list of str
        :param _Granularity: 监控粒度，目前支持300，3600，86400，单位：秒。
查询时间范围不超过1天，支持最小粒度300秒；
查询间范围不超过7天，支持最小粒度3600秒；
查询间范围超过7天，支持最小粒度86400秒。
        :type Granularity: int
        """
        self._ListenerId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Granularity = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
    def MetricNames(self):
        """统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets。
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Granularity(self):
        """监控粒度，目前支持300，3600，86400，单位：秒。
查询时间范围不超过1天，支持最小粒度300秒；
查询间范围不超过7天，支持最小粒度3600秒；
查询间范围超过7天，支持最小粒度86400秒。
        :rtype: int
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerStatisticsResponse(AbstractModel):
    """DescribeListenerStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatisticsData: 通道组统计数据
        :type StatisticsData: list of MetricStatisticsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        """通道组统计数据
        :rtype: list of MetricStatisticsInfo
        """
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

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
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxiesRequest(AbstractModel):
    """DescribeProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: （旧参数，请切换到ProxyIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤条件。   
每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定InstanceIds和Filters。 
ProjectId - String - 是否必填：否 -（过滤条件）按照项目ID过滤。   
AccessRegion - String - 是否必填：否 - （过滤条件）按照接入地域过滤。    
RealServerRegion - String - 是否必填：否 - （过滤条件）按照源站地域过滤。
GroupId - String - 是否必填：否 - （过滤条件）按照通道组ID过滤。
IPAddressVersion - String - 是否必填：否 - （过滤条件）按照IP版本过滤。
PackageType - String - 是否必填：否 - （过滤条件）按照通道套餐类型过滤。
        :type Filters: list of Filter
        :param _ProxyIds: （新参数，替代InstanceIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :type ProxyIds: list of str
        :param _TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，通道会被拉取出来。
        :type TagSet: list of TagPair
        :param _Independent: 当该字段为1时，仅拉取非通道组的通道，
当该字段为0时，仅拉取通道组的通道，
不存在该字段时，拉取所有通道，包括独立通道和通道组通道。
        :type Independent: int
        :param _Order: 输出通道列表的排列顺序。取值范围：
asc：升序排列；
desc：降序排列。
默认为降序。
        :type Order: str
        :param _OrderField: 通道列表排序的依据字段。取值范围：
create_time：依据通道的创建时间排序；
proxy_id：依据通道的ID排序；
bandwidth：依据通道带宽上限排序；
concurrent_connections：依据通道并发排序；
默认按通道创建时间排序。
        :type OrderField: str
        """
        self._InstanceIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._ProxyIds = None
        self._TagSet = None
        self._Independent = None
        self._Order = None
        self._OrderField = None

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤条件。   
每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定InstanceIds和Filters。 
ProjectId - String - 是否必填：否 -（过滤条件）按照项目ID过滤。   
AccessRegion - String - 是否必填：否 - （过滤条件）按照接入地域过滤。    
RealServerRegion - String - 是否必填：否 - （过滤条件）按照源站地域过滤。
GroupId - String - 是否必填：否 - （过滤条件）按照通道组ID过滤。
IPAddressVersion - String - 是否必填：否 - （过滤条件）按照IP版本过滤。
PackageType - String - 是否必填：否 - （过滤条件）按照通道套餐类型过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ProxyIds(self):
        """（新参数，替代InstanceIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds

    @property
    def TagSet(self):
        """标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，通道会被拉取出来。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Independent(self):
        """当该字段为1时，仅拉取非通道组的通道，
当该字段为0时，仅拉取通道组的通道，
不存在该字段时，拉取所有通道，包括独立通道和通道组通道。
        :rtype: int
        """
        return self._Independent

    @Independent.setter
    def Independent(self, Independent):
        self._Independent = Independent

    @property
    def Order(self):
        """输出通道列表的排列顺序。取值范围：
asc：升序排列；
desc：降序排列。
默认为降序。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """通道列表排序的依据字段。取值范围：
create_time：依据通道的创建时间排序；
proxy_id：依据通道的ID排序；
bandwidth：依据通道带宽上限排序；
concurrent_connections：依据通道并发排序；
默认按通道创建时间排序。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ProxyIds = params.get("ProxyIds")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._Independent = params.get("Independent")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesResponse(AbstractModel):
    """DescribeProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 通道个数。
        :type TotalCount: int
        :param _InstanceSet: （旧参数，请切换到ProxySet）通道实例信息列表。
        :type InstanceSet: list of ProxyInfo
        :param _ProxySet: （新参数）通道实例信息列表。
        :type ProxySet: list of ProxyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._ProxySet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """通道个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """（旧参数，请切换到ProxySet）通道实例信息列表。
        :rtype: list of ProxyInfo
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def ProxySet(self):
        """（新参数）通道实例信息列表。
        :rtype: list of ProxyInfo
        """
        return self._ProxySet

    @ProxySet.setter
    def ProxySet(self, ProxySet):
        self._ProxySet = ProxySet

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        if params.get("ProxySet") is not None:
            self._ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self._ProxySet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxiesStatusRequest(AbstractModel):
    """DescribeProxiesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: （旧参数，请切换到ProxyIds）通道ID列表。
        :type InstanceIds: list of str
        :param _ProxyIds: （新参数）通道ID列表。
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）通道ID列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProxyIds(self):
        """（新参数）通道ID列表。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesStatusResponse(AbstractModel):
    """DescribeProxiesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceStatusSet: 通道状态列表。
        :type InstanceStatusSet: list of ProxyStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceStatusSet = None
        self._RequestId = None

    @property
    def InstanceStatusSet(self):
        """通道状态列表。
        :rtype: list of ProxyStatus
        """
        return self._InstanceStatusSet

    @InstanceStatusSet.setter
    def InstanceStatusSet(self, InstanceStatusSet):
        self._InstanceStatusSet = InstanceStatusSet

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
        if params.get("InstanceStatusSet") is not None:
            self._InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = ProxyStatus()
                obj._deserialize(item)
                self._InstanceStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyAndStatisticsListenersRequest(AbstractModel):
    """DescribeProxyAndStatisticsListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        """
        self._ProjectId = None

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyAndStatisticsListenersResponse(AbstractModel):
    """DescribeProxyAndStatisticsListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxySet: 可以统计的通道信息
        :type ProxySet: list of ProxySimpleInfo
        :param _TotalCount: 通道数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ProxySet(self):
        """可以统计的通道信息
        :rtype: list of ProxySimpleInfo
        """
        return self._ProxySet

    @ProxySet.setter
    def ProxySet(self, ProxySet):
        self._ProxySet = ProxySet

    @property
    def TotalCount(self):
        """通道数量
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
        if params.get("ProxySet") is not None:
            self._ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self._ProxySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeProxyDetailRequest(AbstractModel):
    """DescribeProxyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 需查询的通道ID。
        :type ProxyId: str
        """
        self._ProxyId = None

    @property
    def ProxyId(self):
        """需查询的通道ID。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyDetailResponse(AbstractModel):
    """DescribeProxyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyDetail: 通道详情信息。
        :type ProxyDetail: :class:`tencentcloud.gaap.v20180529.models.ProxyInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyDetail = None
        self._RequestId = None

    @property
    def ProxyDetail(self):
        """通道详情信息。
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ProxyInfo`
        """
        return self._ProxyDetail

    @ProxyDetail.setter
    def ProxyDetail(self, ProxyDetail):
        self._ProxyDetail = ProxyDetail

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
        if params.get("ProxyDetail") is not None:
            self._ProxyDetail = ProxyInfo()
            self._ProxyDetail._deserialize(params.get("ProxyDetail"))
        self._RequestId = params.get("RequestId")


class DescribeProxyGroupDetailsRequest(AbstractModel):
    """DescribeProxyGroupDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID。
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupDetailsResponse(AbstractModel):
    """DescribeProxyGroupDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyGroupDetail: 通道组详细信息。
        :type ProxyGroupDetail: :class:`tencentcloud.gaap.v20180529.models.ProxyGroupDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyGroupDetail = None
        self._RequestId = None

    @property
    def ProxyGroupDetail(self):
        """通道组详细信息。
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ProxyGroupDetail`
        """
        return self._ProxyGroupDetail

    @ProxyGroupDetail.setter
    def ProxyGroupDetail(self, ProxyGroupDetail):
        self._ProxyGroupDetail = ProxyGroupDetail

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
        if params.get("ProxyGroupDetail") is not None:
            self._ProxyGroupDetail = ProxyGroupDetail()
            self._ProxyGroupDetail._deserialize(params.get("ProxyGroupDetail"))
        self._RequestId = params.get("RequestId")


class DescribeProxyGroupListRequest(AbstractModel):
    """DescribeProxyGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认值为0。
        :type Offset: int
        :param _Limit: 返回数量，默认值为20，最大值为100。
        :type Limit: int
        :param _ProjectId: 项目ID。取值范围：
-1，该用户下所有项目
0，默认项目
其他值，指定的项目
        :type ProjectId: int
        :param _Filters: 过滤条件。   
每次请求的Filter.Values的上限为5。
RealServerRegion - String - 是否必填：否 -（过滤条件）按照源站地域过滤，可参考DescribeDestRegions接口返回结果中的RegionId。
PackageType - String - 是否必填：否 - （过滤条件）通道组类型，Thunder表示标准通道组，Accelerator表示银牌加速通道组。
        :type Filters: list of Filter
        :param _TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，该通道组会被拉取出来。
        :type TagSet: list of TagPair
        """
        self._Offset = None
        self._Limit = None
        self._ProjectId = None
        self._Filters = None
        self._TagSet = None

    @property
    def Offset(self):
        """偏移量，默认值为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ProjectId(self):
        """项目ID。取值范围：
-1，该用户下所有项目
0，默认项目
其他值，指定的项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Filters(self):
        """过滤条件。   
每次请求的Filter.Values的上限为5。
RealServerRegion - String - 是否必填：否 -（过滤条件）按照源站地域过滤，可参考DescribeDestRegions接口返回结果中的RegionId。
PackageType - String - 是否必填：否 - （过滤条件）通道组类型，Thunder表示标准通道组，Accelerator表示银牌加速通道组。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TagSet(self):
        """标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，该通道组会被拉取出来。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ProjectId = params.get("ProjectId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupListResponse(AbstractModel):
    """DescribeProxyGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 通道组总数。
        :type TotalCount: int
        :param _ProxyGroupList: 通道组列表。
        :type ProxyGroupList: list of ProxyGroupInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ProxyGroupList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """通道组总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ProxyGroupList(self):
        """通道组列表。
        :rtype: list of ProxyGroupInfo
        """
        return self._ProxyGroupList

    @ProxyGroupList.setter
    def ProxyGroupList(self, ProxyGroupList):
        self._ProxyGroupList = ProxyGroupList

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
        if params.get("ProxyGroupList") is not None:
            self._ProxyGroupList = []
            for item in params.get("ProxyGroupList"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self._ProxyGroupList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyGroupStatisticsRequest(AbstractModel):
    """DescribeProxyGroupStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID
        :type GroupId: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _MetricNames: 统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets
        :type MetricNames: list of str
        :param _Granularity: 监控粒度，目前支持60，300，3600，86400，单位：秒。
当时间范围不超过1天，支持最小粒度60秒；
当时间范围不超过7天，支持最小粒度3600秒；
当时间范围不超过30天，支持最小粒度86400秒。
        :type Granularity: int
        """
        self._GroupId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Granularity = None

    @property
    def GroupId(self):
        """通道组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

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
    def MetricNames(self):
        """统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Granularity(self):
        """监控粒度，目前支持60，300，3600，86400，单位：秒。
当时间范围不超过1天，支持最小粒度60秒；
当时间范围不超过7天，支持最小粒度3600秒；
当时间范围不超过30天，支持最小粒度86400秒。
        :rtype: int
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupStatisticsResponse(AbstractModel):
    """DescribeProxyGroupStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatisticsData: 通道组统计数据
        :type StatisticsData: list of MetricStatisticsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        """通道组统计数据
        :rtype: list of MetricStatisticsInfo
        """
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

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
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProxyStatisticsRequest(AbstractModel):
    """DescribeProxyStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID
        :type ProxyId: str
        :param _StartTime: 起始时间(2019-03-25 12:00:00)
        :type StartTime: str
        :param _EndTime: 结束时间(2019-03-25 12:00:00)
        :type EndTime: str
        :param _MetricNames: 统计指标名称列表，支持: 
入带宽:InBandwidth, 
出带宽:OutBandwidth, 
并发:Concurrent, 
入包量:InPackets, 
出包量:OutPackets, 
丢包率:PacketLoss, 
延迟:Latency，
HTTP请求量：HttpQPS, 
HTTP请求量利用率：HttpQPSPercent,
HTTPS请求量：HttpsQPS,
HTTPS请求量利用率：HttpsQPSPercent
        :type MetricNames: list of str
        :param _Granularity: 监控粒度，目前支持60，300，3600，86400，单位：秒。
当时间范围不超过3天，支持最小粒度60秒；
当时间范围不超过7天，支持最小粒度300秒；
当时间范围不超过30天，支持最小粒度3600秒。
        :type Granularity: int
        :param _Isp: 运营商（通道为三网通道时有效），支持CMCC，CUCC，CTCC，传空值或不传则合并三个运营商数据
        :type Isp: str
        """
        self._ProxyId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricNames = None
        self._Granularity = None
        self._Isp = None

    @property
    def ProxyId(self):
        """通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def StartTime(self):
        """起始时间(2019-03-25 12:00:00)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间(2019-03-25 12:00:00)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricNames(self):
        """统计指标名称列表，支持: 
入带宽:InBandwidth, 
出带宽:OutBandwidth, 
并发:Concurrent, 
入包量:InPackets, 
出包量:OutPackets, 
丢包率:PacketLoss, 
延迟:Latency，
HTTP请求量：HttpQPS, 
HTTP请求量利用率：HttpQPSPercent,
HTTPS请求量：HttpsQPS,
HTTPS请求量利用率：HttpsQPSPercent
        :rtype: list of str
        """
        return self._MetricNames

    @MetricNames.setter
    def MetricNames(self, MetricNames):
        self._MetricNames = MetricNames

    @property
    def Granularity(self):
        """监控粒度，目前支持60，300，3600，86400，单位：秒。
当时间范围不超过3天，支持最小粒度60秒；
当时间范围不超过7天，支持最小粒度300秒；
当时间范围不超过30天，支持最小粒度3600秒。
        :rtype: int
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity

    @property
    def Isp(self):
        """运营商（通道为三网通道时有效），支持CMCC，CUCC，CTCC，传空值或不传则合并三个运营商数据
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricNames = params.get("MetricNames")
        self._Granularity = params.get("Granularity")
        self._Isp = params.get("Isp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyStatisticsResponse(AbstractModel):
    """DescribeProxyStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatisticsData: 通道统计数据
        :type StatisticsData: list of MetricStatisticsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        """通道统计数据
        :rtype: list of MetricStatisticsInfo
        """
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

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
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRealServerStatisticsRequest(AbstractModel):
    """DescribeRealServerStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RealServerId: 源站ID
        :type RealServerId: str
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _RuleId: L7层规则ID
        :type RuleId: str
        :param _WithinTime: 统计时长，单位：小时。仅支持最近1,3,6,12,24小时的统计查询
        :type WithinTime: int
        :param _StartTime: 统计开始时间(2020-08-19 00:00:00)
        :type StartTime: str
        :param _EndTime: 统计结束时间(2020-08-19 23:59:59)
        :type EndTime: str
        :param _Granularity: 统计的数据粒度，单位：秒，仅支持1分钟-60和5分钟-300粒度
        :type Granularity: int
        """
        self._RealServerId = None
        self._ListenerId = None
        self._RuleId = None
        self._WithinTime = None
        self._StartTime = None
        self._EndTime = None
        self._Granularity = None

    @property
    def RealServerId(self):
        """源站ID
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleId(self):
        """L7层规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def WithinTime(self):
        """统计时长，单位：小时。仅支持最近1,3,6,12,24小时的统计查询
        :rtype: int
        """
        return self._WithinTime

    @WithinTime.setter
    def WithinTime(self, WithinTime):
        self._WithinTime = WithinTime

    @property
    def StartTime(self):
        """统计开始时间(2020-08-19 00:00:00)
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间(2020-08-19 23:59:59)
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Granularity(self):
        """统计的数据粒度，单位：秒，仅支持1分钟-60和5分钟-300粒度
        :rtype: int
        """
        return self._Granularity

    @Granularity.setter
    def Granularity(self, Granularity):
        self._Granularity = Granularity


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._ListenerId = params.get("ListenerId")
        self._RuleId = params.get("RuleId")
        self._WithinTime = params.get("WithinTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServerStatisticsResponse(AbstractModel):
    """DescribeRealServerStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StatisticsData: 指定监听器的源站状态统计数据
        :type StatisticsData: list of StatisticsDataInfo
        :param _RsStatisticsData: 多个源站状态统计数据
        :type RsStatisticsData: list of MetricStatisticsInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StatisticsData = None
        self._RsStatisticsData = None
        self._RequestId = None

    @property
    def StatisticsData(self):
        """指定监听器的源站状态统计数据
        :rtype: list of StatisticsDataInfo
        """
        return self._StatisticsData

    @StatisticsData.setter
    def StatisticsData(self, StatisticsData):
        self._StatisticsData = StatisticsData

    @property
    def RsStatisticsData(self):
        """多个源站状态统计数据
        :rtype: list of MetricStatisticsInfo
        """
        return self._RsStatisticsData

    @RsStatisticsData.setter
    def RsStatisticsData(self, RsStatisticsData):
        self._RsStatisticsData = RsStatisticsData

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
        if params.get("StatisticsData") is not None:
            self._StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self._StatisticsData.append(obj)
        if params.get("RsStatisticsData") is not None:
            self._RsStatisticsData = []
            for item in params.get("RsStatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self._RsStatisticsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRealServersRequest(AbstractModel):
    """DescribeRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 查询源站的所属项目ID，-1表示所有项目
        :type ProjectId: int
        :param _SearchValue: 需要查询的源站IP或域名，支持模糊匹配
        :type SearchValue: str
        :param _Offset: 偏移量，默认值是0
        :type Offset: int
        :param _Limit: 返回数量，默认为20个，最大值为50个
        :type Limit: int
        :param _TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，源站会被拉取出来。
        :type TagSet: list of TagPair
        :param _Filters: 过滤条件。filter的name取值(RealServerName,RealServerIP)
        :type Filters: list of Filter
        """
        self._ProjectId = None
        self._SearchValue = None
        self._Offset = None
        self._Limit = None
        self._TagSet = None
        self._Filters = None

    @property
    def ProjectId(self):
        """查询源站的所属项目ID，-1表示所有项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def SearchValue(self):
        """需要查询的源站IP或域名，支持模糊匹配
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def Offset(self):
        """偏移量，默认值是0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20个，最大值为50个
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagSet(self):
        """标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，源站会被拉取出来。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Filters(self):
        """过滤条件。filter的name取值(RealServerName,RealServerIP)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._SearchValue = params.get("SearchValue")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServersResponse(AbstractModel):
    """DescribeRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RealServerSet: 源站信息列表
        :type RealServerSet: list of BindRealServerInfo
        :param _TotalCount: 查询得到的源站数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RealServerSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RealServerSet(self):
        """源站信息列表
        :rtype: list of BindRealServerInfo
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def TotalCount(self):
        """查询得到的源站数量
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
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServerInfo()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRealServersStatusRequest(AbstractModel):
    """DescribeRealServersStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RealServerIds: 源站ID列表
        :type RealServerIds: list of str
        """
        self._RealServerIds = None

    @property
    def RealServerIds(self):
        """源站ID列表
        :rtype: list of str
        """
        return self._RealServerIds

    @RealServerIds.setter
    def RealServerIds(self, RealServerIds):
        self._RealServerIds = RealServerIds


    def _deserialize(self, params):
        self._RealServerIds = params.get("RealServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServersStatusResponse(AbstractModel):
    """DescribeRealServersStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回源站查询结果的个数
        :type TotalCount: int
        :param _RealServerStatusSet: 源站被绑定状态列表
        :type RealServerStatusSet: list of RealServerStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealServerStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回源站查询结果的个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealServerStatusSet(self):
        """源站被绑定状态列表
        :rtype: list of RealServerStatus
        """
        return self._RealServerStatusSet

    @RealServerStatusSet.setter
    def RealServerStatusSet(self, RealServerStatusSet):
        self._RealServerStatusSet = RealServerStatusSet

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
        if params.get("RealServerStatusSet") is not None:
            self._RealServerStatusSet = []
            for item in params.get("RealServerStatusSet"):
                obj = RealServerStatus()
                obj._deserialize(item)
                self._RealServerStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionAndPriceRequest(AbstractModel):
    """DescribeRegionAndPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        """
        self._IPAddressVersion = None
        self._PackageType = None

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        """通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType


    def _deserialize(self, params):
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionAndPriceResponse(AbstractModel):
    """DescribeRegionAndPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 源站区域总数
        :type TotalCount: int
        :param _DestRegionSet: 源站区域详情列表
        :type DestRegionSet: list of RegionDetail
        :param _BandwidthUnitPrice: 通道带宽费用梯度价格
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param _Currency: 带宽价格货币类型：
CNY 人民币
USD 美元
        :type Currency: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DestRegionSet = None
        self._BandwidthUnitPrice = None
        self._Currency = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """源站区域总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DestRegionSet(self):
        """源站区域详情列表
        :rtype: list of RegionDetail
        """
        return self._DestRegionSet

    @DestRegionSet.setter
    def DestRegionSet(self, DestRegionSet):
        self._DestRegionSet = DestRegionSet

    @property
    def BandwidthUnitPrice(self):
        """通道带宽费用梯度价格
        :rtype: list of BandwidthPriceGradient
        """
        return self._BandwidthUnitPrice

    @BandwidthUnitPrice.setter
    def BandwidthUnitPrice(self, BandwidthUnitPrice):
        self._BandwidthUnitPrice = BandwidthUnitPrice

    @property
    def Currency(self):
        """带宽价格货币类型：
CNY 人民币
USD 美元
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

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
        if params.get("DestRegionSet") is not None:
            self._DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self._DestRegionSet.append(obj)
        if params.get("BandwidthUnitPrice") is not None:
            self._BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self._BandwidthUnitPrice.append(obj)
        self._Currency = params.get("Currency")
        self._RequestId = params.get("RequestId")


class DescribeResourcesByTagRequest(AbstractModel):
    """DescribeResourcesByTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
        :type TagKey: str
        :param _TagValue: 标签值。
        :type TagValue: str
        :param _ResourceType: 资源类型，其中：
Proxy表示通道；
ProxyGroup表示通道组；
RealServer表示源站。
不指定该字段则查询该标签下所有资源。
        :type ResourceType: str
        """
        self._TagKey = None
        self._TagValue = None
        self._ResourceType = None

    @property
    def TagKey(self):
        """标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值。
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceType(self):
        """资源类型，其中：
Proxy表示通道；
ProxyGroup表示通道组；
RealServer表示源站。
不指定该字段则查询该标签下所有资源。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagResponse(AbstractModel):
    """DescribeResourcesByTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源总数
        :type TotalCount: int
        :param _ResourceSet: 标签对应的资源列表
        :type ResourceSet: list of TagResourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """资源总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceSet(self):
        """标签对应的资源列表
        :rtype: list of TagResourceInfo
        """
        return self._ResourceSet

    @ResourceSet.setter
    def ResourceSet(self, ResourceSet):
        self._ResourceSet = ResourceSet

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
        if params.get("ResourceSet") is not None:
            self._ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = TagResourceInfo()
                obj._deserialize(item)
                self._ResourceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRuleRealServersRequest(AbstractModel):
    """DescribeRuleRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 转发规则ID
        :type RuleId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为1000。
        :type Limit: int
        """
        self._RuleId = None
        self._Offset = None
        self._Limit = None

    @property
    def RuleId(self):
        """转发规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleRealServersResponse(AbstractModel):
    """DescribeRuleRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 可绑定的源站个数
        :type TotalCount: int
        :param _RealServerSet: 可绑定的源站信息列表
        :type RealServerSet: list of RealServer
        :param _BindRealServerTotalCount: 已绑定的源站个数
        :type BindRealServerTotalCount: int
        :param _BindRealServerSet: 已绑定的源站信息列表
        :type BindRealServerSet: list of BindRealServer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RealServerSet = None
        self._BindRealServerTotalCount = None
        self._BindRealServerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """可绑定的源站个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RealServerSet(self):
        """可绑定的源站信息列表
        :rtype: list of RealServer
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def BindRealServerTotalCount(self):
        """已绑定的源站个数
        :rtype: int
        """
        return self._BindRealServerTotalCount

    @BindRealServerTotalCount.setter
    def BindRealServerTotalCount(self, BindRealServerTotalCount):
        self._BindRealServerTotalCount = BindRealServerTotalCount

    @property
    def BindRealServerSet(self):
        """已绑定的源站信息列表
        :rtype: list of BindRealServer
        """
        return self._BindRealServerSet

    @BindRealServerSet.setter
    def BindRealServerSet(self, BindRealServerSet):
        self._BindRealServerSet = BindRealServerSet

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
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self._BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._BindRealServerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesByRuleIdsRequest(AbstractModel):
    """DescribeRulesByRuleIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIds: 规则ID列表。最多支持10个规则。
        :type RuleIds: list of str
        """
        self._RuleIds = None

    @property
    def RuleIds(self):
        """规则ID列表。最多支持10个规则。
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesByRuleIdsResponse(AbstractModel):
    """DescribeRulesByRuleIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的规则总个数。
        :type TotalCount: int
        :param _RuleSet: 返回的规则列表。
        :type RuleSet: list of RuleInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的规则总个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RuleSet(self):
        """返回的规则列表。
        :rtype: list of RuleInfo
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet

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
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 7层监听器Id。
        :type ListenerId: str
        """
        self._ListenerId = None

    @property
    def ListenerId(self):
        """7层监听器Id。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainRuleSet: 按照域名分类的规则信息列表
        :type DomainRuleSet: list of DomainRuleSet
        :param _TotalCount: 该监听器下的域名总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainRuleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainRuleSet(self):
        """按照域名分类的规则信息列表
        :rtype: list of DomainRuleSet
        """
        return self._DomainRuleSet

    @DomainRuleSet.setter
    def DomainRuleSet(self, DomainRuleSet):
        self._DomainRuleSet = DomainRuleSet

    @property
    def TotalCount(self):
        """该监听器下的域名总数
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
        if params.get("DomainRuleSet") is not None:
            self._DomainRuleSet = []
            for item in params.get("DomainRuleSet"):
                obj = DomainRuleSet()
                obj._deserialize(item)
                self._DomainRuleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyDetailRequest(AbstractModel):
    """DescribeSecurityPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyDetailResponse(AbstractModel):
    """DescribeSecurityPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param _Status: 安全策略状态：
BOUND，已开启安全策略
UNBIND，已关闭安全策略
BINDING，安全策略开启中
UNBINDING，安全策略关闭中。
        :type Status: str
        :param _DefaultAction: 默认策略：ACCEPT或DROP。
        :type DefaultAction: str
        :param _PolicyId: 策略ID
        :type PolicyId: str
        :param _RuleList: 规则列表
        :type RuleList: list of SecurityPolicyRuleOut
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyId = None
        self._Status = None
        self._DefaultAction = None
        self._PolicyId = None
        self._RuleList = None
        self._RequestId = None

    @property
    def ProxyId(self):
        """通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Status(self):
        """安全策略状态：
BOUND，已开启安全策略
UNBIND，已关闭安全策略
BINDING，安全策略开启中
UNBINDING，安全策略关闭中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DefaultAction(self):
        """默认策略：ACCEPT或DROP。
        :rtype: str
        """
        return self._DefaultAction

    @DefaultAction.setter
    def DefaultAction(self, DefaultAction):
        self._DefaultAction = DefaultAction

    @property
    def PolicyId(self):
        """策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleList(self):
        """规则列表
        :rtype: list of SecurityPolicyRuleOut
        """
        return self._RuleList

    @RuleList.setter
    def RuleList(self, RuleList):
        self._RuleList = RuleList

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
        self._ProxyId = params.get("ProxyId")
        self._Status = params.get("Status")
        self._DefaultAction = params.get("DefaultAction")
        self._PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self._RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self._RuleList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityRulesRequest(AbstractModel):
    """DescribeSecurityRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityRuleIds: 安全规则ID列表。总数不能超过20个。
        :type SecurityRuleIds: list of str
        """
        self._SecurityRuleIds = None

    @property
    def SecurityRuleIds(self):
        """安全规则ID列表。总数不能超过20个。
        :rtype: list of str
        """
        return self._SecurityRuleIds

    @SecurityRuleIds.setter
    def SecurityRuleIds(self, SecurityRuleIds):
        self._SecurityRuleIds = SecurityRuleIds


    def _deserialize(self, params):
        self._SecurityRuleIds = params.get("SecurityRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityRulesResponse(AbstractModel):
    """DescribeSecurityRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的安全规则详情总数。
        :type TotalCount: int
        :param _SecurityRuleSet: 返回的安全规则详情列表。
        :type SecurityRuleSet: list of SecurityPolicyRuleOut
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecurityRuleSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的安全规则详情总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecurityRuleSet(self):
        """返回的安全规则详情列表。
        :rtype: list of SecurityPolicyRuleOut
        """
        return self._SecurityRuleSet

    @SecurityRuleSet.setter
    def SecurityRuleSet(self, SecurityRuleSet):
        self._SecurityRuleSet = SecurityRuleSet

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
        if params.get("SecurityRuleSet") is not None:
            self._SecurityRuleSet = []
            for item in params.get("SecurityRuleSet"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self._SecurityRuleSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTCPListenersRequest(AbstractModel):
    """DescribeTCPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type ProxyId: str
        :param _ListenerId: 过滤条件，根据监听器ID精确查询。
当设置了ProxyId时，会检查该监听器是否归属于该通道。
当设置了GroupId时，会检查该监听器是否归属于该通道组。
        :type ListenerId: str
        :param _ListenerName: 过滤条件，根据监听器名称精确查询
        :type ListenerName: str
        :param _Port: 过滤条件，根据监听器端口精确查询
        :type Port: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 限制数量，默认为20
        :type Limit: int
        :param _GroupId: 过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type GroupId: str
        :param _SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :type SearchValue: str
        """
        self._ProxyId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._SearchValue = None

    @property
    def ProxyId(self):
        """过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerId(self):
        """过滤条件，根据监听器ID精确查询。
当设置了ProxyId时，会检查该监听器是否归属于该通道。
当设置了GroupId时，会检查该监听器是否归属于该通道组。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """过滤条件，根据监听器名称精确查询
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """过滤条件，根据监听器端口精确查询
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数量，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def GroupId(self):
        """过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchValue(self):
        """过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTCPListenersResponse(AbstractModel):
    """DescribeTCPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足条件的监听器总个数
        :type TotalCount: int
        :param _ListenerSet: TCP监听器列表
        :type ListenerSet: list of TCPListener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """满足条件的监听器总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        """TCP监听器列表
        :rtype: list of TCPListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

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
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TCPListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，值为异步接口返回的RequestId，此参数不能传空值。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """任务ID，值为异步接口返回的RequestId，此参数不能传空值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态：RUNNING，FAIL，SUCCESS
        :type Status: str
        :param _TaskId: 任务ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._TaskId = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态：RUNNING，FAIL，SUCCESS
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        """任务ID
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
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeUDPListenersRequest(AbstractModel):
    """DescribeUDPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type ProxyId: str
        :param _ListenerId: 过滤条件，根据监听器ID精确查询。
当设置了ProxyId时，会检查该监听器是否归属于该通道。
当设置了GroupId时，会检查该监听器是否归属于该通道组。
        :type ListenerId: str
        :param _ListenerName: 过滤条件，根据监听器名称精确查询
        :type ListenerName: str
        :param _Port: 过滤条件，根据监听器端口精确查询
        :type Port: int
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 限制数量，默认为20
        :type Limit: int
        :param _GroupId: 过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type GroupId: str
        :param _SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :type SearchValue: str
        """
        self._ProxyId = None
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Offset = None
        self._Limit = None
        self._GroupId = None
        self._SearchValue = None

    @property
    def ProxyId(self):
        """过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerId(self):
        """过滤条件，根据监听器ID精确查询。
当设置了ProxyId时，会检查该监听器是否归属于该通道。
当设置了GroupId时，会检查该监听器是否归属于该通道组。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """过滤条件，根据监听器名称精确查询
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """过滤条件，根据监听器端口精确查询
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限制数量，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def GroupId(self):
        """过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def SearchValue(self):
        """过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._GroupId = params.get("GroupId")
        self._SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUDPListenersResponse(AbstractModel):
    """DescribeUDPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 监听器个数
        :type TotalCount: int
        :param _ListenerSet: UDP监听器列表
        :type ListenerSet: list of UDPListener
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ListenerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """监听器个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ListenerSet(self):
        """UDP监听器列表
        :rtype: list of UDPListener
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

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
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = UDPListener()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DestroyProxiesRequest(AbstractModel):
    """DestroyProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Force: 强制删除标识。
1，强制删除该通道列表，无论是否已经绑定了源站；
0，如果已绑定了源站，则无法删除。
删除多通道时，如果该标识为0，只有所有的通道都没有绑定源站，才允许删除。
        :type Force: int
        :param _InstanceIds: （旧参数，请切换到ProxyIds）通道实例ID列表。
        :type InstanceIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _ProxyIds: （新参数）通道实例ID列表。
        :type ProxyIds: list of str
        """
        self._Force = None
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def Force(self):
        """强制删除标识。
1，强制删除该通道列表，无论是否已经绑定了源站；
0，如果已绑定了源站，则无法删除。
删除多通道时，如果该标识为0，只有所有的通道都没有绑定源站，才允许删除。
        :rtype: int
        """
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）通道实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        """（新参数）通道实例ID列表。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._Force = params.get("Force")
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyProxiesResponse(AbstractModel):
    """DestroyProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: 处于不可销毁状态下的通道实例ID列表。
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: 销毁操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        """处于不可销毁状态下的通道实例ID列表。
        :rtype: list of str
        """
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        """销毁操作失败的通道实例ID列表。
        :rtype: list of str
        """
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

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
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class DisableGlobalDomainRequest(AbstractModel):
    """DisableGlobalDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        """
        self._DomainId = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableGlobalDomainResponse(AbstractModel):
    """DisableGlobalDomain返回参数结构体

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


class Domain(AbstractModel):
    """统一域名信息

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _FullDomain: 完整域名记录
        :type FullDomain: str
        :param _Alias: 别名
        :type Alias: str
        :param _Type: 类型
        :type Type: str
        :param _Status: 状态，1表示关闭，0表示开启，2表示关闭中，3表示开启中
        :type Status: int
        :param _ProjectId: 所属项目
        :type ProjectId: int
        :param _DefaultValue: 默认入口
        :type DefaultValue: str
        :param _ProxyCount: 通道数量
        :type ProxyCount: int
        :param _CreateTime: 创建时间，使用UNIX时间戳
        :type CreateTime: int
        :param _UpdateTime: 更新时间，使用UNIX时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _TagSet: 标签列表
        :type TagSet: list of TagPair
        :param _BanStatus: 封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
        :type BanStatus: str
        """
        self._DomainId = None
        self._FullDomain = None
        self._Alias = None
        self._Type = None
        self._Status = None
        self._ProjectId = None
        self._DefaultValue = None
        self._ProxyCount = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TagSet = None
        self._BanStatus = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def FullDomain(self):
        """完整域名记录
        :rtype: str
        """
        return self._FullDomain

    @FullDomain.setter
    def FullDomain(self, FullDomain):
        self._FullDomain = FullDomain

    @property
    def Alias(self):
        """别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Type(self):
        """类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        """状态，1表示关闭，0表示开启，2表示关闭中，3表示开启中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        """所属项目
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def DefaultValue(self):
        """默认入口
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def ProxyCount(self):
        """通道数量
        :rtype: int
        """
        return self._ProxyCount

    @ProxyCount.setter
    def ProxyCount(self, ProxyCount):
        self._ProxyCount = ProxyCount

    @property
    def CreateTime(self):
        """创建时间，使用UNIX时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间，使用UNIX时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def BanStatus(self):
        """封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
        :rtype: str
        """
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._FullDomain = params.get("FullDomain")
        self._Alias = params.get("Alias")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._DefaultValue = params.get("DefaultValue")
        self._ProxyCount = params.get("ProxyCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._BanStatus = params.get("BanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAccessRegionDict(AbstractModel):
    """域名解析就近访问配置详情

    """

    def __init__(self):
        r"""
        :param _NationCountryInnerList: 就近接入区域
        :type NationCountryInnerList: list of NationCountryInnerInfo
        :param _ProxyList: 加速区域通道列表
        :type ProxyList: list of ProxyIdDict
        :param _RegionId: 加速区域ID
        :type RegionId: str
        :param _GeographicalZoneInnerCode: 加速区域内部编码
        :type GeographicalZoneInnerCode: str
        :param _ContinentInnerCode: 加速区域所属大洲内部编码
        :type ContinentInnerCode: str
        :param _RegionName: 加速区域别名
        :type RegionName: str
        """
        self._NationCountryInnerList = None
        self._ProxyList = None
        self._RegionId = None
        self._GeographicalZoneInnerCode = None
        self._ContinentInnerCode = None
        self._RegionName = None

    @property
    def NationCountryInnerList(self):
        """就近接入区域
        :rtype: list of NationCountryInnerInfo
        """
        return self._NationCountryInnerList

    @NationCountryInnerList.setter
    def NationCountryInnerList(self, NationCountryInnerList):
        self._NationCountryInnerList = NationCountryInnerList

    @property
    def ProxyList(self):
        """加速区域通道列表
        :rtype: list of ProxyIdDict
        """
        return self._ProxyList

    @ProxyList.setter
    def ProxyList(self, ProxyList):
        self._ProxyList = ProxyList

    @property
    def RegionId(self):
        """加速区域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def GeographicalZoneInnerCode(self):
        """加速区域内部编码
        :rtype: str
        """
        return self._GeographicalZoneInnerCode

    @GeographicalZoneInnerCode.setter
    def GeographicalZoneInnerCode(self, GeographicalZoneInnerCode):
        self._GeographicalZoneInnerCode = GeographicalZoneInnerCode

    @property
    def ContinentInnerCode(self):
        """加速区域所属大洲内部编码
        :rtype: str
        """
        return self._ContinentInnerCode

    @ContinentInnerCode.setter
    def ContinentInnerCode(self, ContinentInnerCode):
        self._ContinentInnerCode = ContinentInnerCode

    @property
    def RegionName(self):
        """加速区域别名
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName


    def _deserialize(self, params):
        if params.get("NationCountryInnerList") is not None:
            self._NationCountryInnerList = []
            for item in params.get("NationCountryInnerList"):
                obj = NationCountryInnerInfo()
                obj._deserialize(item)
                self._NationCountryInnerList.append(obj)
        if params.get("ProxyList") is not None:
            self._ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyIdDict()
                obj._deserialize(item)
                self._ProxyList.append(obj)
        self._RegionId = params.get("RegionId")
        self._GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self._ContinentInnerCode = params.get("ContinentInnerCode")
        self._RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainErrorPageInfo(AbstractModel):
    """域名的定制错误响应配置

    """

    def __init__(self):
        r"""
        :param _ErrorPageId: 错误定制响应的配置ID
        :type ErrorPageId: str
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _Domain: 域名
        :type Domain: str
        :param _ErrorNos: 原始错误码
        :type ErrorNos: list of int
        :param _NewErrorNo: 新的错误码
        :type NewErrorNo: int
        :param _ClearHeaders: 需要清理的响应头
        :type ClearHeaders: list of str
        :param _SetHeaders: 需要设置的响应头
        :type SetHeaders: list of HttpHeaderParam
        :param _Body: 设置的响应体(不包括 HTTP头)
        :type Body: str
        :param _Status: 规则状态,0为成功
        :type Status: int
        """
        self._ErrorPageId = None
        self._ListenerId = None
        self._Domain = None
        self._ErrorNos = None
        self._NewErrorNo = None
        self._ClearHeaders = None
        self._SetHeaders = None
        self._Body = None
        self._Status = None

    @property
    def ErrorPageId(self):
        """错误定制响应的配置ID
        :rtype: str
        """
        return self._ErrorPageId

    @ErrorPageId.setter
    def ErrorPageId(self, ErrorPageId):
        self._ErrorPageId = ErrorPageId

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
    def ErrorNos(self):
        """原始错误码
        :rtype: list of int
        """
        return self._ErrorNos

    @ErrorNos.setter
    def ErrorNos(self, ErrorNos):
        self._ErrorNos = ErrorNos

    @property
    def NewErrorNo(self):
        """新的错误码
        :rtype: int
        """
        return self._NewErrorNo

    @NewErrorNo.setter
    def NewErrorNo(self, NewErrorNo):
        self._NewErrorNo = NewErrorNo

    @property
    def ClearHeaders(self):
        """需要清理的响应头
        :rtype: list of str
        """
        return self._ClearHeaders

    @ClearHeaders.setter
    def ClearHeaders(self, ClearHeaders):
        self._ClearHeaders = ClearHeaders

    @property
    def SetHeaders(self):
        """需要设置的响应头
        :rtype: list of HttpHeaderParam
        """
        return self._SetHeaders

    @SetHeaders.setter
    def SetHeaders(self, SetHeaders):
        self._SetHeaders = SetHeaders

    @property
    def Body(self):
        """设置的响应体(不包括 HTTP头)
        :rtype: str
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Status(self):
        """规则状态,0为成功
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ErrorPageId = params.get("ErrorPageId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._ErrorNos = params.get("ErrorNos")
        self._NewErrorNo = params.get("NewErrorNo")
        self._ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self._SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self._SetHeaders.append(obj)
        self._Body = params.get("Body")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainRuleSet(AbstractModel):
    """按照域名分类的7层监听器转发规则信息

    """

    def __init__(self):
        r"""
        :param _Domain: 转发规则域名。
        :type Domain: str
        :param _RuleSet: 该域名对应的转发规则列表。
        :type RuleSet: list of RuleInfo
        :param _CertificateId: 该域名对应的服务器证书ID，值为default时，表示使用默认证书（监听器配置的证书）。
        :type CertificateId: str
        :param _CertificateAlias: 该域名对应服务器证书名称。
        :type CertificateAlias: str
        :param _ClientCertificateId: 该域名对应的客户端证书ID，值为default时，表示使用默认证书（监听器配置的证书）。
        :type ClientCertificateId: str
        :param _ClientCertificateAlias: 该域名对应客户端证书名称。
        :type ClientCertificateAlias: str
        :param _BasicAuthConfId: 该域名对应基础认证配置ID。
        :type BasicAuthConfId: str
        :param _BasicAuth: 基础认证开关，其中：
0，表示未开启；
1，表示已开启。
        :type BasicAuth: int
        :param _BasicAuthConfAlias: 该域名对应基础认证配置名称。
        :type BasicAuthConfAlias: str
        :param _RealServerCertificateId: 该域名对应源站认证证书ID。
        :type RealServerCertificateId: str
        :param _RealServerAuth: 源站认证开关，其中：
0，表示未开启；
1，表示已开启。
        :type RealServerAuth: int
        :param _RealServerCertificateAlias: 该域名对应源站认证证书名称。
        :type RealServerCertificateAlias: str
        :param _GaapCertificateId: 该域名对应通道认证证书ID。
        :type GaapCertificateId: str
        :param _GaapAuth: 通道认证开关，其中：
0，表示未开启；
1，表示已开启。
        :type GaapAuth: int
        :param _GaapCertificateAlias: 该域名对应通道认证证书名称。
        :type GaapCertificateAlias: str
        :param _RealServerCertificateDomain: 源站认证域名。
        :type RealServerCertificateDomain: str
        :param _PolyClientCertificateAliasInfo: 多客户端证书时，返回多个证书的id和别名
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        :param _PolyRealServerCertificateAliasInfo: 多源站证书时，返回多个证书的id和别名
        :type PolyRealServerCertificateAliasInfo: list of CertificateAliasInfo
        :param _DomainStatus: 域名的状态。
0表示运行中，
1表示变更中，
2表示删除中。
        :type DomainStatus: int
        :param _BanStatus: 封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
        :type BanStatus: str
        :param _Http3Supported: Http3特性标识，其中：
0表示关闭；
1表示启用。
        :type Http3Supported: int
        :param _IsDefaultServer: 是否为默认域名
        :type IsDefaultServer: bool
        :param _TLSCiphers: TLS套件包
        :type TLSCiphers: str
        :param _TLSSupportVersion: TLS版本
        :type TLSSupportVersion: list of str
        """
        self._Domain = None
        self._RuleSet = None
        self._CertificateId = None
        self._CertificateAlias = None
        self._ClientCertificateId = None
        self._ClientCertificateAlias = None
        self._BasicAuthConfId = None
        self._BasicAuth = None
        self._BasicAuthConfAlias = None
        self._RealServerCertificateId = None
        self._RealServerAuth = None
        self._RealServerCertificateAlias = None
        self._GaapCertificateId = None
        self._GaapAuth = None
        self._GaapCertificateAlias = None
        self._RealServerCertificateDomain = None
        self._PolyClientCertificateAliasInfo = None
        self._PolyRealServerCertificateAliasInfo = None
        self._DomainStatus = None
        self._BanStatus = None
        self._Http3Supported = None
        self._IsDefaultServer = None
        self._TLSCiphers = None
        self._TLSSupportVersion = None

    @property
    def Domain(self):
        """转发规则域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RuleSet(self):
        """该域名对应的转发规则列表。
        :rtype: list of RuleInfo
        """
        return self._RuleSet

    @RuleSet.setter
    def RuleSet(self, RuleSet):
        self._RuleSet = RuleSet

    @property
    def CertificateId(self):
        """该域名对应的服务器证书ID，值为default时，表示使用默认证书（监听器配置的证书）。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateAlias(self):
        """该域名对应服务器证书名称。
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def ClientCertificateId(self):
        """该域名对应的客户端证书ID，值为default时，表示使用默认证书（监听器配置的证书）。
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def ClientCertificateAlias(self):
        """该域名对应客户端证书名称。
        :rtype: str
        """
        return self._ClientCertificateAlias

    @ClientCertificateAlias.setter
    def ClientCertificateAlias(self, ClientCertificateAlias):
        self._ClientCertificateAlias = ClientCertificateAlias

    @property
    def BasicAuthConfId(self):
        """该域名对应基础认证配置ID。
        :rtype: str
        """
        return self._BasicAuthConfId

    @BasicAuthConfId.setter
    def BasicAuthConfId(self, BasicAuthConfId):
        self._BasicAuthConfId = BasicAuthConfId

    @property
    def BasicAuth(self):
        """基础认证开关，其中：
0，表示未开启；
1，表示已开启。
        :rtype: int
        """
        return self._BasicAuth

    @BasicAuth.setter
    def BasicAuth(self, BasicAuth):
        self._BasicAuth = BasicAuth

    @property
    def BasicAuthConfAlias(self):
        """该域名对应基础认证配置名称。
        :rtype: str
        """
        return self._BasicAuthConfAlias

    @BasicAuthConfAlias.setter
    def BasicAuthConfAlias(self, BasicAuthConfAlias):
        self._BasicAuthConfAlias = BasicAuthConfAlias

    @property
    def RealServerCertificateId(self):
        """该域名对应源站认证证书ID。
        :rtype: str
        """
        return self._RealServerCertificateId

    @RealServerCertificateId.setter
    def RealServerCertificateId(self, RealServerCertificateId):
        self._RealServerCertificateId = RealServerCertificateId

    @property
    def RealServerAuth(self):
        """源站认证开关，其中：
0，表示未开启；
1，表示已开启。
        :rtype: int
        """
        return self._RealServerAuth

    @RealServerAuth.setter
    def RealServerAuth(self, RealServerAuth):
        self._RealServerAuth = RealServerAuth

    @property
    def RealServerCertificateAlias(self):
        """该域名对应源站认证证书名称。
        :rtype: str
        """
        return self._RealServerCertificateAlias

    @RealServerCertificateAlias.setter
    def RealServerCertificateAlias(self, RealServerCertificateAlias):
        self._RealServerCertificateAlias = RealServerCertificateAlias

    @property
    def GaapCertificateId(self):
        """该域名对应通道认证证书ID。
        :rtype: str
        """
        return self._GaapCertificateId

    @GaapCertificateId.setter
    def GaapCertificateId(self, GaapCertificateId):
        self._GaapCertificateId = GaapCertificateId

    @property
    def GaapAuth(self):
        """通道认证开关，其中：
0，表示未开启；
1，表示已开启。
        :rtype: int
        """
        return self._GaapAuth

    @GaapAuth.setter
    def GaapAuth(self, GaapAuth):
        self._GaapAuth = GaapAuth

    @property
    def GaapCertificateAlias(self):
        """该域名对应通道认证证书名称。
        :rtype: str
        """
        return self._GaapCertificateAlias

    @GaapCertificateAlias.setter
    def GaapCertificateAlias(self, GaapCertificateAlias):
        self._GaapCertificateAlias = GaapCertificateAlias

    @property
    def RealServerCertificateDomain(self):
        """源站认证域名。
        :rtype: str
        """
        return self._RealServerCertificateDomain

    @RealServerCertificateDomain.setter
    def RealServerCertificateDomain(self, RealServerCertificateDomain):
        self._RealServerCertificateDomain = RealServerCertificateDomain

    @property
    def PolyClientCertificateAliasInfo(self):
        """多客户端证书时，返回多个证书的id和别名
        :rtype: list of CertificateAliasInfo
        """
        return self._PolyClientCertificateAliasInfo

    @PolyClientCertificateAliasInfo.setter
    def PolyClientCertificateAliasInfo(self, PolyClientCertificateAliasInfo):
        self._PolyClientCertificateAliasInfo = PolyClientCertificateAliasInfo

    @property
    def PolyRealServerCertificateAliasInfo(self):
        """多源站证书时，返回多个证书的id和别名
        :rtype: list of CertificateAliasInfo
        """
        return self._PolyRealServerCertificateAliasInfo

    @PolyRealServerCertificateAliasInfo.setter
    def PolyRealServerCertificateAliasInfo(self, PolyRealServerCertificateAliasInfo):
        self._PolyRealServerCertificateAliasInfo = PolyRealServerCertificateAliasInfo

    @property
    def DomainStatus(self):
        """域名的状态。
0表示运行中，
1表示变更中，
2表示删除中。
        :rtype: int
        """
        return self._DomainStatus

    @DomainStatus.setter
    def DomainStatus(self, DomainStatus):
        self._DomainStatus = DomainStatus

    @property
    def BanStatus(self):
        """封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
        :rtype: str
        """
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def Http3Supported(self):
        """Http3特性标识，其中：
0表示关闭；
1表示启用。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def IsDefaultServer(self):
        """是否为默认域名
        :rtype: bool
        """
        return self._IsDefaultServer

    @IsDefaultServer.setter
    def IsDefaultServer(self, IsDefaultServer):
        self._IsDefaultServer = IsDefaultServer

    @property
    def TLSCiphers(self):
        """TLS套件包
        :rtype: str
        """
        return self._TLSCiphers

    @TLSCiphers.setter
    def TLSCiphers(self, TLSCiphers):
        self._TLSCiphers = TLSCiphers

    @property
    def TLSSupportVersion(self):
        """TLS版本
        :rtype: list of str
        """
        return self._TLSSupportVersion

    @TLSSupportVersion.setter
    def TLSSupportVersion(self, TLSSupportVersion):
        self._TLSSupportVersion = TLSSupportVersion


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("RuleSet") is not None:
            self._RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self._RuleSet.append(obj)
        self._CertificateId = params.get("CertificateId")
        self._CertificateAlias = params.get("CertificateAlias")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._ClientCertificateAlias = params.get("ClientCertificateAlias")
        self._BasicAuthConfId = params.get("BasicAuthConfId")
        self._BasicAuth = params.get("BasicAuth")
        self._BasicAuthConfAlias = params.get("BasicAuthConfAlias")
        self._RealServerCertificateId = params.get("RealServerCertificateId")
        self._RealServerAuth = params.get("RealServerAuth")
        self._RealServerCertificateAlias = params.get("RealServerCertificateAlias")
        self._GaapCertificateId = params.get("GaapCertificateId")
        self._GaapAuth = params.get("GaapAuth")
        self._GaapCertificateAlias = params.get("GaapCertificateAlias")
        self._RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self._PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self._PolyClientCertificateAliasInfo.append(obj)
        if params.get("PolyRealServerCertificateAliasInfo") is not None:
            self._PolyRealServerCertificateAliasInfo = []
            for item in params.get("PolyRealServerCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self._PolyRealServerCertificateAliasInfo.append(obj)
        self._DomainStatus = params.get("DomainStatus")
        self._BanStatus = params.get("BanStatus")
        self._Http3Supported = params.get("Http3Supported")
        self._IsDefaultServer = params.get("IsDefaultServer")
        self._TLSCiphers = params.get("TLSCiphers")
        self._TLSSupportVersion = params.get("TLSSupportVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGlobalDomainRequest(AbstractModel):
    """EnableGlobalDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        """
        self._DomainId = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGlobalDomainResponse(AbstractModel):
    """EnableGlobalDomain返回参数结构体

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


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件
        :type Name: str
        :param _Values: 过滤值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """过滤条件
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """过滤值
        :rtype: list of str
        """
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
        


class GlobalDns(AbstractModel):
    """统一域名解析的DNS记录

    """

    def __init__(self):
        r"""
        :param _DnsRecordId: 解析记录ID
        :type DnsRecordId: int
        :param _CountryAreaList: 域名就近接入地域信息列表
        :type CountryAreaList: list of CountryAreaMap
        :param _AccessList: 域名解析对应的通道接入点信息列表
        :type AccessList: list of ProxyAccessInfo
        :param _Status: 解析状态：1表示运行中，2表示创建中，3表示修改中，4表示删除中
        :type Status: int
        """
        self._DnsRecordId = None
        self._CountryAreaList = None
        self._AccessList = None
        self._Status = None

    @property
    def DnsRecordId(self):
        """解析记录ID
        :rtype: int
        """
        return self._DnsRecordId

    @DnsRecordId.setter
    def DnsRecordId(self, DnsRecordId):
        self._DnsRecordId = DnsRecordId

    @property
    def CountryAreaList(self):
        """域名就近接入地域信息列表
        :rtype: list of CountryAreaMap
        """
        return self._CountryAreaList

    @CountryAreaList.setter
    def CountryAreaList(self, CountryAreaList):
        self._CountryAreaList = CountryAreaList

    @property
    def AccessList(self):
        """域名解析对应的通道接入点信息列表
        :rtype: list of ProxyAccessInfo
        """
        return self._AccessList

    @AccessList.setter
    def AccessList(self, AccessList):
        self._AccessList = AccessList

    @property
    def Status(self):
        """解析状态：1表示运行中，2表示创建中，3表示修改中，4表示删除中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._DnsRecordId = params.get("DnsRecordId")
        if params.get("CountryAreaList") is not None:
            self._CountryAreaList = []
            for item in params.get("CountryAreaList"):
                obj = CountryAreaMap()
                obj._deserialize(item)
                self._CountryAreaList.append(obj)
        if params.get("AccessList") is not None:
            self._AccessList = []
            for item in params.get("AccessList"):
                obj = ProxyAccessInfo()
                obj._deserialize(item)
                self._AccessList.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupStatisticsInfo(AbstractModel):
    """可以显示统计数据的通道组和对应通道信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID
        :type GroupId: str
        :param _GroupName: 通道组名称
        :type GroupName: str
        :param _ProxySet: 通道组下通道列表
        :type ProxySet: list of ProxySimpleInfo
        """
        self._GroupId = None
        self._GroupName = None
        self._ProxySet = None

    @property
    def GroupId(self):
        """通道组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """通道组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProxySet(self):
        """通道组下通道列表
        :rtype: list of ProxySimpleInfo
        """
        return self._ProxySet

    @ProxySet.setter
    def ProxySet(self, ProxySet):
        self._ProxySet = ProxySet


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        if params.get("ProxySet") is not None:
            self._ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self._ProxySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPListener(AbstractModel):
    """HTTP类型监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器端口
        :type Port: int
        :param _CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param _Protocol: 监听器协议， HTTP表示HTTP，HTTPS表示HTTPS，此结构取值HTTP
        :type Protocol: str
        :param _ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param _ProxyId: 监听器的通道ID，如果监听器属于通道组，则为null
        :type ProxyId: str
        :param _GroupId: 监听器的通道组ID，如果监听器属于通道，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._CreateTime = None
        self._Protocol = None
        self._ListenerStatus = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def CreateTime(self):
        """监听器创建时间，Unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Protocol(self):
        """监听器协议， HTTP表示HTTP，HTTPS表示HTTPS，此结构取值HTTP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        """监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :rtype: int
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def ProxyId(self):
        """监听器的通道ID，如果监听器属于通道组，则为null
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """监听器的通道组ID，如果监听器属于通道，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._CreateTime = params.get("CreateTime")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPSListener(AbstractModel):
    """HTTPS类型监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器端口
        :type Port: int
        :param _Protocol: 监听器协议， HTTP表示HTTP，HTTPS表示HTTPS，此结构取值HTTPS
        :type Protocol: str
        :param _ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param _CertificateId: 监听器服务器SSL证书ID
        :type CertificateId: str
        :param _ForwardProtocol: 监听器后端转发源站协议
        :type ForwardProtocol: str
        :param _CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param _CertificateAlias: 服务器SSL证书的别名
        :type CertificateAlias: str
        :param _ClientCertificateId: 监听器客户端CA证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertificateId: str
        :param _AuthType: 监听器认证方式。其中，
0表示单向认证；
1表示双向认证。
        :type AuthType: int
        :param _ClientCertificateAlias: 客户端CA证书别名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertificateAlias: str
        :param _PolyClientCertificateAliasInfo: 多客户端CA证书别名信息
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        :param _Http3Supported: 是否支持Http3，其中：
0，不支持Http3接入；
1，持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
        :type Http3Supported: int
        :param _ProxyId: 监听器的通道ID，如果监听器属于通道组，则为null
        :type ProxyId: str
        :param _GroupId: 监听器的通道组ID，如果监听器属于通道，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _TLSSupportVersion: 支持的TLS版本
        :type TLSSupportVersion: list of str
        :param _TLSCiphers: 支持的TLS密码套件
        :type TLSCiphers: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Protocol = None
        self._ListenerStatus = None
        self._CertificateId = None
        self._ForwardProtocol = None
        self._CreateTime = None
        self._CertificateAlias = None
        self._ClientCertificateId = None
        self._AuthType = None
        self._ClientCertificateAlias = None
        self._PolyClientCertificateAliasInfo = None
        self._Http3Supported = None
        self._ProxyId = None
        self._GroupId = None
        self._TLSSupportVersion = None
        self._TLSCiphers = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        """监听器协议， HTTP表示HTTP，HTTPS表示HTTPS，此结构取值HTTPS
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        """监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :rtype: int
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def CertificateId(self):
        """监听器服务器SSL证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ForwardProtocol(self):
        """监听器后端转发源站协议
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def CreateTime(self):
        """监听器创建时间，Unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CertificateAlias(self):
        """服务器SSL证书的别名
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias

    @property
    def ClientCertificateId(self):
        """监听器客户端CA证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def AuthType(self):
        """监听器认证方式。其中，
0表示单向认证；
1表示双向认证。
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ClientCertificateAlias(self):
        """客户端CA证书别名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientCertificateAlias

    @ClientCertificateAlias.setter
    def ClientCertificateAlias(self, ClientCertificateAlias):
        self._ClientCertificateAlias = ClientCertificateAlias

    @property
    def PolyClientCertificateAliasInfo(self):
        """多客户端CA证书别名信息
        :rtype: list of CertificateAliasInfo
        """
        return self._PolyClientCertificateAliasInfo

    @PolyClientCertificateAliasInfo.setter
    def PolyClientCertificateAliasInfo(self, PolyClientCertificateAliasInfo):
        self._PolyClientCertificateAliasInfo = PolyClientCertificateAliasInfo

    @property
    def Http3Supported(self):
        """是否支持Http3，其中：
0，不支持Http3接入；
1，持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def ProxyId(self):
        """监听器的通道ID，如果监听器属于通道组，则为null
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """监听器的通道组ID，如果监听器属于通道，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TLSSupportVersion(self):
        """支持的TLS版本
        :rtype: list of str
        """
        return self._TLSSupportVersion

    @TLSSupportVersion.setter
    def TLSSupportVersion(self, TLSSupportVersion):
        self._TLSSupportVersion = TLSSupportVersion

    @property
    def TLSCiphers(self):
        """支持的TLS密码套件
        :rtype: str
        """
        return self._TLSCiphers

    @TLSCiphers.setter
    def TLSCiphers(self, TLSCiphers):
        self._TLSCiphers = TLSCiphers


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._CertificateId = params.get("CertificateId")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._CreateTime = params.get("CreateTime")
        self._CertificateAlias = params.get("CertificateAlias")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._AuthType = params.get("AuthType")
        self._ClientCertificateAlias = params.get("ClientCertificateAlias")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self._PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self._PolyClientCertificateAliasInfo.append(obj)
        self._Http3Supported = params.get("Http3Supported")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        self._TLSSupportVersion = params.get("TLSSupportVersion")
        self._TLSCiphers = params.get("TLSCiphers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderParam(AbstractModel):
    """描述HTTP的包头参数

    """

    def __init__(self):
        r"""
        :param _HeaderName: HTTP头名
        :type HeaderName: str
        :param _HeaderValue: HTTP头值
        :type HeaderValue: str
        """
        self._HeaderName = None
        self._HeaderValue = None

    @property
    def HeaderName(self):
        """HTTP头名
        :rtype: str
        """
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        """HTTP头值
        :rtype: str
        """
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue


    def _deserialize(self, params):
        self._HeaderName = params.get("HeaderName")
        self._HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPDetail(AbstractModel):
    """ip信息详情

    """

    def __init__(self):
        r"""
        :param _IP: IP字符串
        :type IP: str
        :param _Provider: 供应商，BGP表示默认，CMCC表示中国移动，CUCC表示中国联通，CTCC表示中国电信
        :type Provider: str
        :param _Bandwidth: 带宽
        :type Bandwidth: int
        """
        self._IP = None
        self._Provider = None
        self._Bandwidth = None

    @property
    def IP(self):
        """IP字符串
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Provider(self):
        """供应商，BGP表示默认，CMCC表示中国移动，CUCC表示中国联通，CTCC表示中国电信
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def Bandwidth(self):
        """带宽
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Provider = params.get("Provider")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateProxyRequest(AbstractModel):
    """InquiryPriceCreateProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessRegion: 加速区域名称。
        :type AccessRegion: str
        :param _Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param _DestRegion: （旧参数，请切换到RealServerRegion）源站区域名称。
        :type DestRegion: str
        :param _Concurrency: （此参数为旧参数，请填写新参数Concurrent，二者必须填写一个）通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrency: int
        :param _RealServerRegion: （新参数）源站区域名称。
        :type RealServerRegion: str
        :param _Concurrent: （新参数）通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param _BillingType: 计费方式，0表示按带宽计费，1表示按流量计费。默认按带宽计费
        :type BillingType: int
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _NetworkType: 网络类型，可取值：normal、cn2，默认值normal
        :type NetworkType: str
        :param _PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        :param _Http3Supported: 该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :type Http3Supported: int
        """
        self._AccessRegion = None
        self._Bandwidth = None
        self._DestRegion = None
        self._Concurrency = None
        self._RealServerRegion = None
        self._Concurrent = None
        self._BillingType = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._Http3Supported = None

    @property
    def AccessRegion(self):
        """加速区域名称。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def Bandwidth(self):
        """通道带宽上限，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def DestRegion(self):
        """（旧参数，请切换到RealServerRegion）源站区域名称。
        :rtype: str
        """
        return self._DestRegion

    @DestRegion.setter
    def DestRegion(self, DestRegion):
        self._DestRegion = DestRegion

    @property
    def Concurrency(self):
        """（此参数为旧参数，请填写新参数Concurrent，二者必须填写一个）通道并发量上限，表示同时在线的连接数，单位：万。
        :rtype: int
        """
        return self._Concurrency

    @Concurrency.setter
    def Concurrency(self, Concurrency):
        self._Concurrency = Concurrency

    @property
    def RealServerRegion(self):
        """（新参数）源站区域名称。
        :rtype: str
        """
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def Concurrent(self):
        """（新参数）通道并发量上限，表示同时在线的连接数，单位：万。
        :rtype: int
        """
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def BillingType(self):
        """计费方式，0表示按带宽计费，1表示按流量计费。默认按带宽计费
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        """网络类型，可取值：normal、cn2，默认值normal
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        """通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        """该字段已废弃，当IPAddressVersion为IPv4时，所创建的通道默认支持Http3.0；当为IPv6，默认不支持Http3.0。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported


    def _deserialize(self, params):
        self._AccessRegion = params.get("AccessRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._DestRegion = params.get("DestRegion")
        self._Concurrency = params.get("Concurrency")
        self._RealServerRegion = params.get("RealServerRegion")
        self._Concurrent = params.get("Concurrent")
        self._BillingType = params.get("BillingType")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateProxyResponse(AbstractModel):
    """InquiryPriceCreateProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyDailyPrice: 通道基础费用价格，单位：元/天。
        :type ProxyDailyPrice: float
        :param _BandwidthUnitPrice: 通道带宽费用梯度价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param _DiscountProxyDailyPrice: 通道基础费用折扣价格，单位：元/天。
        :type DiscountProxyDailyPrice: float
        :param _Currency: 价格使用的货币，支持人民币，美元等。
        :type Currency: str
        :param _FlowUnitPrice: 通道的流量费用价格，单位: 元/GB
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowUnitPrice: float
        :param _DiscountFlowUnitPrice: 通道的流量费用折扣价格，单位:元/GB
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountFlowUnitPrice: float
        :param _Cn2BandwidthPrice: 精品BGP的带宽费用价格，单位: 元/Mbps/天
        :type Cn2BandwidthPrice: float
        :param _Cn2BandwidthPriceWithDiscount: 精品BGP的折后带宽费用价格，单位: 元/Mbps/天
        :type Cn2BandwidthPriceWithDiscount: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProxyDailyPrice = None
        self._BandwidthUnitPrice = None
        self._DiscountProxyDailyPrice = None
        self._Currency = None
        self._FlowUnitPrice = None
        self._DiscountFlowUnitPrice = None
        self._Cn2BandwidthPrice = None
        self._Cn2BandwidthPriceWithDiscount = None
        self._RequestId = None

    @property
    def ProxyDailyPrice(self):
        """通道基础费用价格，单位：元/天。
        :rtype: float
        """
        return self._ProxyDailyPrice

    @ProxyDailyPrice.setter
    def ProxyDailyPrice(self, ProxyDailyPrice):
        self._ProxyDailyPrice = ProxyDailyPrice

    @property
    def BandwidthUnitPrice(self):
        """通道带宽费用梯度价格。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BandwidthPriceGradient
        """
        return self._BandwidthUnitPrice

    @BandwidthUnitPrice.setter
    def BandwidthUnitPrice(self, BandwidthUnitPrice):
        self._BandwidthUnitPrice = BandwidthUnitPrice

    @property
    def DiscountProxyDailyPrice(self):
        """通道基础费用折扣价格，单位：元/天。
        :rtype: float
        """
        return self._DiscountProxyDailyPrice

    @DiscountProxyDailyPrice.setter
    def DiscountProxyDailyPrice(self, DiscountProxyDailyPrice):
        self._DiscountProxyDailyPrice = DiscountProxyDailyPrice

    @property
    def Currency(self):
        """价格使用的货币，支持人民币，美元等。
        :rtype: str
        """
        return self._Currency

    @Currency.setter
    def Currency(self, Currency):
        self._Currency = Currency

    @property
    def FlowUnitPrice(self):
        """通道的流量费用价格，单位: 元/GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._FlowUnitPrice

    @FlowUnitPrice.setter
    def FlowUnitPrice(self, FlowUnitPrice):
        self._FlowUnitPrice = FlowUnitPrice

    @property
    def DiscountFlowUnitPrice(self):
        """通道的流量费用折扣价格，单位:元/GB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._DiscountFlowUnitPrice

    @DiscountFlowUnitPrice.setter
    def DiscountFlowUnitPrice(self, DiscountFlowUnitPrice):
        self._DiscountFlowUnitPrice = DiscountFlowUnitPrice

    @property
    def Cn2BandwidthPrice(self):
        """精品BGP的带宽费用价格，单位: 元/Mbps/天
        :rtype: float
        """
        return self._Cn2BandwidthPrice

    @Cn2BandwidthPrice.setter
    def Cn2BandwidthPrice(self, Cn2BandwidthPrice):
        self._Cn2BandwidthPrice = Cn2BandwidthPrice

    @property
    def Cn2BandwidthPriceWithDiscount(self):
        """精品BGP的折后带宽费用价格，单位: 元/Mbps/天
        :rtype: float
        """
        return self._Cn2BandwidthPriceWithDiscount

    @Cn2BandwidthPriceWithDiscount.setter
    def Cn2BandwidthPriceWithDiscount(self, Cn2BandwidthPriceWithDiscount):
        self._Cn2BandwidthPriceWithDiscount = Cn2BandwidthPriceWithDiscount

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
        self._ProxyDailyPrice = params.get("ProxyDailyPrice")
        if params.get("BandwidthUnitPrice") is not None:
            self._BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self._BandwidthUnitPrice.append(obj)
        self._DiscountProxyDailyPrice = params.get("DiscountProxyDailyPrice")
        self._Currency = params.get("Currency")
        self._FlowUnitPrice = params.get("FlowUnitPrice")
        self._DiscountFlowUnitPrice = params.get("DiscountFlowUnitPrice")
        self._Cn2BandwidthPrice = params.get("Cn2BandwidthPrice")
        self._Cn2BandwidthPriceWithDiscount = params.get("Cn2BandwidthPriceWithDiscount")
        self._RequestId = params.get("RequestId")


class ListenerInfo(AbstractModel):
    """内部接口使用，返回可以查询统计数据的监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器监听端口
        :type Port: int
        :param _Protocol: 监听器协议类型
        :type Protocol: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._Protocol = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器监听端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        """监听器协议类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricStatisticsInfo(AbstractModel):
    """单指标的统计数据

    """

    def __init__(self):
        r"""
        :param _MetricName: 指标名称
        :type MetricName: str
        :param _MetricData: 指标统计数据
        :type MetricData: list of StatisticsDataInfo
        """
        self._MetricName = None
        self._MetricData = None

    @property
    def MetricName(self):
        """指标名称
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MetricData(self):
        """指标统计数据
        :rtype: list of StatisticsDataInfo
        """
        return self._MetricData

    @MetricData.setter
    def MetricData(self, MetricData):
        self._MetricData = MetricData


    def _deserialize(self, params):
        self._MetricName = params.get("MetricName")
        if params.get("MetricData") is not None:
            self._MetricData = []
            for item in params.get("MetricData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self._MetricData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAttributesRequest(AbstractModel):
    """ModifyCertificateAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _CertificateAlias: 证书名字。长度不超过50个字符。
        :type CertificateAlias: str
        """
        self._CertificateId = None
        self._CertificateAlias = None

    @property
    def CertificateId(self):
        """证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateAlias(self):
        """证书名字。长度不超过50个字符。
        :rtype: str
        """
        return self._CertificateAlias

    @CertificateAlias.setter
    def CertificateAlias(self, CertificateAlias):
        self._CertificateAlias = CertificateAlias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAttributesResponse(AbstractModel):
    """ModifyCertificateAttributes返回参数结构体

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


class ModifyCertificateRequest(AbstractModel):
    """ModifyCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器实例ID
        :type ListenerId: str
        :param _Domain: 需要修改证书的域名
        :type Domain: str
        :param _CertificateId: 新的服务器证书ID。其中：
当CertificateId=default时，表示使用监听器的证书。
        :type CertificateId: str
        :param _ClientCertificateId: 新的客户端证书ID。其中：
当ClientCertificateId=default时，表示使用监听器的证书。
仅当采用双向认证方式时，需要设置该参数或者PolyClientCertificateIds。
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: 新的多客户端证书ID列表。其中：
仅当采用双向认证方式时，需要设置该参数或ClientCertificateId参数。
        :type PolyClientCertificateIds: list of str
        """
        self._ListenerId = None
        self._Domain = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None

    @property
    def ListenerId(self):
        """监听器实例ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        """需要修改证书的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertificateId(self):
        """新的服务器证书ID。其中：
当CertificateId=default时，表示使用监听器的证书。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        """新的客户端证书ID。其中：
当ClientCertificateId=default时，表示使用监听器的证书。
仅当采用双向认证方式时，需要设置该参数或者PolyClientCertificateIds。
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        """新的多客户端证书ID列表。其中：
仅当采用双向认证方式时，需要设置该参数或ClientCertificateId参数。
        :rtype: list of str
        """
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateResponse(AbstractModel):
    """ModifyCertificate返回参数结构体

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


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 7层监听器ID
        :type ListenerId: str
        :param _OldDomain: 修改前的域名信息
        :type OldDomain: str
        :param _NewDomain: 修改后的域名信息
        :type NewDomain: str
        :param _CertificateId: 服务器SSL证书ID，仅适用于version3.0的通道。其中：
不带该字段时，表示使用原证书；
携带该字段时并且CertificateId=default，表示使用监听器证书；
其他情况，使用该CertificateId指定的证书。
        :type CertificateId: str
        :param _ClientCertificateId: 客户端CA证书ID，仅适用于version3.0的通道。其中：
不带该字段和PolyClientCertificateIds时，表示使用原证书；
携带该字段时并且ClientCertificateId=default，表示使用监听器证书；
其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: 客户端CA证书ID，仅适用于version3.0的通道。其中：
不带该字段和ClientCertificateId时，表示使用原证书；
携带该字段时并且ClientCertificateId=default，表示使用监听器证书；
其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。
        :type PolyClientCertificateIds: list of str
        :param _IsDefaultServer: 是否作为默认域名，默认为“否”
        :type IsDefaultServer: bool
        """
        self._ListenerId = None
        self._OldDomain = None
        self._NewDomain = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None
        self._IsDefaultServer = None

    @property
    def ListenerId(self):
        """7层监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def OldDomain(self):
        """修改前的域名信息
        :rtype: str
        """
        return self._OldDomain

    @OldDomain.setter
    def OldDomain(self, OldDomain):
        self._OldDomain = OldDomain

    @property
    def NewDomain(self):
        """修改后的域名信息
        :rtype: str
        """
        return self._NewDomain

    @NewDomain.setter
    def NewDomain(self, NewDomain):
        self._NewDomain = NewDomain

    @property
    def CertificateId(self):
        """服务器SSL证书ID，仅适用于version3.0的通道。其中：
不带该字段时，表示使用原证书；
携带该字段时并且CertificateId=default，表示使用监听器证书；
其他情况，使用该CertificateId指定的证书。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        """客户端CA证书ID，仅适用于version3.0的通道。其中：
不带该字段和PolyClientCertificateIds时，表示使用原证书；
携带该字段时并且ClientCertificateId=default，表示使用监听器证书；
其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        """客户端CA证书ID，仅适用于version3.0的通道。其中：
不带该字段和ClientCertificateId时，表示使用原证书；
携带该字段时并且ClientCertificateId=default，表示使用监听器证书；
其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。
        :rtype: list of str
        """
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds

    @property
    def IsDefaultServer(self):
        """是否作为默认域名，默认为“否”
        :rtype: bool
        """
        return self._IsDefaultServer

    @IsDefaultServer.setter
    def IsDefaultServer(self, IsDefaultServer):
        self._IsDefaultServer = IsDefaultServer


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._OldDomain = params.get("OldDomain")
        self._NewDomain = params.get("NewDomain")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self._IsDefaultServer = params.get("IsDefaultServer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain返回参数结构体

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


class ModifyGlobalDomainAttributeRequest(AbstractModel):
    """ModifyGlobalDomainAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _Alias: 别名
        :type Alias: str
        :param _DefaultValue: 默认入口
        :type DefaultValue: str
        """
        self._DomainId = None
        self._ProjectId = None
        self._Alias = None
        self._DefaultValue = None

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Alias(self):
        """别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def DefaultValue(self):
        """默认入口
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue


    def _deserialize(self, params):
        self._DomainId = params.get("DomainId")
        self._ProjectId = params.get("ProjectId")
        self._Alias = params.get("Alias")
        self._DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalDomainAttributeResponse(AbstractModel):
    """ModifyGlobalDomainAttribute返回参数结构体

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


class ModifyGlobalDomainDnsRequest(AbstractModel):
    """ModifyGlobalDomainDns请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DnsRecordId: 解析记录ID
        :type DnsRecordId: int
        :param _DomainId: 域名ID
        :type DomainId: str
        :param _NationCountryInnerCodes: 国家ID列表
        :type NationCountryInnerCodes: list of str
        :param _ProxyIdList: 通道ID列表
        :type ProxyIdList: list of str
        """
        self._DnsRecordId = None
        self._DomainId = None
        self._NationCountryInnerCodes = None
        self._ProxyIdList = None

    @property
    def DnsRecordId(self):
        """解析记录ID
        :rtype: int
        """
        return self._DnsRecordId

    @DnsRecordId.setter
    def DnsRecordId(self, DnsRecordId):
        self._DnsRecordId = DnsRecordId

    @property
    def DomainId(self):
        """域名ID
        :rtype: str
        """
        return self._DomainId

    @DomainId.setter
    def DomainId(self, DomainId):
        self._DomainId = DomainId

    @property
    def NationCountryInnerCodes(self):
        """国家ID列表
        :rtype: list of str
        """
        return self._NationCountryInnerCodes

    @NationCountryInnerCodes.setter
    def NationCountryInnerCodes(self, NationCountryInnerCodes):
        self._NationCountryInnerCodes = NationCountryInnerCodes

    @property
    def ProxyIdList(self):
        """通道ID列表
        :rtype: list of str
        """
        return self._ProxyIdList

    @ProxyIdList.setter
    def ProxyIdList(self, ProxyIdList):
        self._ProxyIdList = ProxyIdList


    def _deserialize(self, params):
        self._DnsRecordId = params.get("DnsRecordId")
        self._DomainId = params.get("DomainId")
        self._NationCountryInnerCodes = params.get("NationCountryInnerCodes")
        self._ProxyIdList = params.get("ProxyIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalDomainDnsResponse(AbstractModel):
    """ModifyGlobalDomainDns返回参数结构体

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


class ModifyGroupDomainConfigRequest(AbstractModel):
    """ModifyGroupDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组ID。
        :type GroupId: str
        :param _DefaultDnsIp: 域名解析默认访问IP或域名。
        :type DefaultDnsIp: str
        :param _AccessRegionList: 就近接入区域配置。
        :type AccessRegionList: list of AccessRegionDomainConf
        """
        self._GroupId = None
        self._DefaultDnsIp = None
        self._AccessRegionList = None

    @property
    def GroupId(self):
        """通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def DefaultDnsIp(self):
        """域名解析默认访问IP或域名。
        :rtype: str
        """
        return self._DefaultDnsIp

    @DefaultDnsIp.setter
    def DefaultDnsIp(self, DefaultDnsIp):
        self._DefaultDnsIp = DefaultDnsIp

    @property
    def AccessRegionList(self):
        """就近接入区域配置。
        :rtype: list of AccessRegionDomainConf
        """
        return self._AccessRegionList

    @AccessRegionList.setter
    def AccessRegionList(self, AccessRegionList):
        self._AccessRegionList = AccessRegionList


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._DefaultDnsIp = params.get("DefaultDnsIp")
        if params.get("AccessRegionList") is not None:
            self._AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = AccessRegionDomainConf()
                obj._deserialize(item)
                self._AccessRegionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupDomainConfigResponse(AbstractModel):
    """ModifyGroupDomainConfig返回参数结构体

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


class ModifyHTTPListenerAttributeRequest(AbstractModel):
    """ModifyHTTPListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 需要修改的监听器ID
        :type ListenerId: str
        :param _ListenerName: 新的监听器名称
        :type ListenerName: str
        :param _ProxyId: 通道ID
        :type ProxyId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._ProxyId = None

    @property
    def ListenerId(self):
        """需要修改的监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """新的监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ProxyId(self):
        """通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHTTPListenerAttributeResponse(AbstractModel):
    """ModifyHTTPListenerAttribute返回参数结构体

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


class ModifyHTTPSListenerAttributeRequest(AbstractModel):
    """ModifyHTTPSListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ProxyId: 通道ID， 若为单通道监听器，此项必须填写
        :type ProxyId: str
        :param _ListenerName: 修改后的监听器名称
        :type ListenerName: str
        :param _ForwardProtocol: 监听器后端转发与源站之间的协议类型
        :type ForwardProtocol: str
        :param _CertificateId: 修改后的监听器服务器证书ID
        :type CertificateId: str
        :param _ClientCertificateId: 修改后的监听器客户端证书ID，不支持多客户端证书，多客户端证书新采用PolyClientCertificateIds字段
        :type ClientCertificateId: str
        :param _PolyClientCertificateIds: 新字段,修改后的监听器客户端证书ID
        :type PolyClientCertificateIds: list of str
        """
        self._ListenerId = None
        self._ProxyId = None
        self._ListenerName = None
        self._ForwardProtocol = None
        self._CertificateId = None
        self._ClientCertificateId = None
        self._PolyClientCertificateIds = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ProxyId(self):
        """通道ID， 若为单通道监听器，此项必须填写
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerName(self):
        """修改后的监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ForwardProtocol(self):
        """监听器后端转发与源站之间的协议类型
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def CertificateId(self):
        """修改后的监听器服务器证书ID
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ClientCertificateId(self):
        """修改后的监听器客户端证书ID，不支持多客户端证书，多客户端证书新采用PolyClientCertificateIds字段
        :rtype: str
        """
        return self._ClientCertificateId

    @ClientCertificateId.setter
    def ClientCertificateId(self, ClientCertificateId):
        self._ClientCertificateId = ClientCertificateId

    @property
    def PolyClientCertificateIds(self):
        """新字段,修改后的监听器客户端证书ID
        :rtype: list of str
        """
        return self._PolyClientCertificateIds

    @PolyClientCertificateIds.setter
    def PolyClientCertificateIds(self, PolyClientCertificateIds):
        self._PolyClientCertificateIds = PolyClientCertificateIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ProxyId = params.get("ProxyId")
        self._ListenerName = params.get("ListenerName")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._CertificateId = params.get("CertificateId")
        self._ClientCertificateId = params.get("ClientCertificateId")
        self._PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHTTPSListenerAttributeResponse(AbstractModel):
    """ModifyHTTPSListenerAttribute返回参数结构体

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


class ModifyProxiesAttributeRequest(AbstractModel):
    """ModifyProxiesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: （旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。
        :type InstanceIds: list of str
        :param _ProxyName: 通道名称。可任意命名，但不得超过32个字符。
        :type ProxyName: str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _ProxyIds: （新参数）一个或多个待操作的通道ID。
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ProxyName = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ProxyName(self):
        """通道名称。可任意命名，但不得超过32个字符。
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        """（新参数）一个或多个待操作的通道ID。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ProxyName = params.get("ProxyName")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxiesAttributeResponse(AbstractModel):
    """ModifyProxiesAttribute返回参数结构体

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


class ModifyProxiesProjectRequest(AbstractModel):
    """ModifyProxiesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 需要修改到的项目ID。
        :type ProjectId: int
        :param _InstanceIds: （旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。
        :type InstanceIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _ProxyIds: （新参数）一个或多个待操作的通道ID。
        :type ProxyIds: list of str
        """
        self._ProjectId = None
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def ProjectId(self):
        """需要修改到的项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        """（新参数）一个或多个待操作的通道ID。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxiesProjectResponse(AbstractModel):
    """ModifyProxiesProject返回参数结构体

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


class ModifyProxyConfigurationRequest(AbstractModel):
    """ModifyProxyConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: （旧参数，请切换到ProxyId）通道的实例ID。
        :type InstanceId: str
        :param _Bandwidth: 需要调整到的目标带宽，单位：Mbps。
Bandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到
        :type Bandwidth: int
        :param _Concurrent: 需要调整到的目标并发值，单位：万。
Bandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到
        :type Concurrent: int
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _ProxyId: （新参数）通道的实例ID。
        :type ProxyId: str
        :param _BillingType: 计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）
        :type BillingType: int
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._Concurrent = None
        self._ClientToken = None
        self._ProxyId = None
        self._BillingType = None

    @property
    def InstanceId(self):
        """（旧参数，请切换到ProxyId）通道的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        """需要调整到的目标带宽，单位：Mbps。
Bandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        """需要调整到的目标并发值，单位：万。
Bandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到
        :rtype: int
        """
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyId(self):
        """（新参数）通道的实例ID。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def BillingType(self):
        """计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._ClientToken = params.get("ClientToken")
        self._ProxyId = params.get("ProxyId")
        self._BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyConfigurationResponse(AbstractModel):
    """ModifyProxyConfiguration返回参数结构体

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


class ModifyProxyGroupAttributeRequest(AbstractModel):
    """ModifyProxyGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 需要修改的通道组ID。
        :type GroupId: str
        :param _GroupName: 修改后的通道组名称：不超过30个字符，否则修改失败。
        :type GroupName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        """
        self._GroupId = None
        self._GroupName = None
        self._ProjectId = None

    @property
    def GroupId(self):
        """需要修改的通道组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        """修改后的通道组名称：不超过30个字符，否则修改失败。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyGroupAttributeResponse(AbstractModel):
    """ModifyProxyGroupAttribute返回参数结构体

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


class ModifyRealServerNameRequest(AbstractModel):
    """ModifyRealServerName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RealServerName: 源站名称
        :type RealServerName: str
        :param _RealServerId: 源站ID
        :type RealServerId: str
        """
        self._RealServerName = None
        self._RealServerId = None

    @property
    def RealServerName(self):
        """源站名称
        :rtype: str
        """
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def RealServerId(self):
        """源站ID
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId


    def _deserialize(self, params):
        self._RealServerName = params.get("RealServerName")
        self._RealServerId = params.get("RealServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRealServerNameResponse(AbstractModel):
    """ModifyRealServerName返回参数结构体

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


class ModifyRuleAttributeRequest(AbstractModel):
    """ModifyRuleAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _RuleId: 转发规则ID
        :type RuleId: str
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _HealthCheck: 源站健康检查开关，其中：
1，开启；
0，关闭。
        :type HealthCheck: int
        :param _CheckParams: 健康检查配置参数
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param _Path: 转发规则路径
        :type Path: str
        :param _ForwardProtocol: 加速通道转发到源站的协议类型，支持：default, HTTP和HTTPS。
当ForwardProtocol=default时，表示使用对应监听器的ForwardProtocol。
        :type ForwardProtocol: str
        :param _ForwardHost: 回源Host。加速通道转发到源站的请求中携带的host。
当ForwardHost=default时，使用规则的域名，其他情况为该字段所设置的值。
        :type ForwardHost: str
        :param _ServerNameIndicationSwitch: 服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
        :type ServerNameIndicationSwitch: str
        :param _ServerNameIndication: 服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
        :type ServerNameIndication: str
        :param _ForcedRedirect: HTTP强制跳转HTTPS。输入当前规则对应的域名与地址。
        :type ForcedRedirect: str
        """
        self._ListenerId = None
        self._RuleId = None
        self._Scheduler = None
        self._HealthCheck = None
        self._CheckParams = None
        self._Path = None
        self._ForwardProtocol = None
        self._ForwardHost = None
        self._ServerNameIndicationSwitch = None
        self._ServerNameIndication = None
        self._ForcedRedirect = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RuleId(self):
        """转发规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        """源站健康检查开关，其中：
1，开启；
0，关闭。
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckParams(self):
        """健康检查配置参数
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        """
        return self._CheckParams

    @CheckParams.setter
    def CheckParams(self, CheckParams):
        self._CheckParams = CheckParams

    @property
    def Path(self):
        """转发规则路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def ForwardProtocol(self):
        """加速通道转发到源站的协议类型，支持：default, HTTP和HTTPS。
当ForwardProtocol=default时，表示使用对应监听器的ForwardProtocol。
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def ForwardHost(self):
        """回源Host。加速通道转发到源站的请求中携带的host。
当ForwardHost=default时，使用规则的域名，其他情况为该字段所设置的值。
        :rtype: str
        """
        return self._ForwardHost

    @ForwardHost.setter
    def ForwardHost(self, ForwardHost):
        self._ForwardHost = ForwardHost

    @property
    def ServerNameIndicationSwitch(self):
        """服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
        :rtype: str
        """
        return self._ServerNameIndicationSwitch

    @ServerNameIndicationSwitch.setter
    def ServerNameIndicationSwitch(self, ServerNameIndicationSwitch):
        self._ServerNameIndicationSwitch = ServerNameIndicationSwitch

    @property
    def ServerNameIndication(self):
        """服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
        :rtype: str
        """
        return self._ServerNameIndication

    @ServerNameIndication.setter
    def ServerNameIndication(self, ServerNameIndication):
        self._ServerNameIndication = ServerNameIndication

    @property
    def ForcedRedirect(self):
        """HTTP强制跳转HTTPS。输入当前规则对应的域名与地址。
        :rtype: str
        """
        return self._ForcedRedirect

    @ForcedRedirect.setter
    def ForcedRedirect(self, ForcedRedirect):
        self._ForcedRedirect = ForcedRedirect


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._RuleId = params.get("RuleId")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self._CheckParams = RuleCheckParams()
            self._CheckParams._deserialize(params.get("CheckParams"))
        self._Path = params.get("Path")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._ForwardHost = params.get("ForwardHost")
        self._ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self._ServerNameIndication = params.get("ServerNameIndication")
        self._ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleAttributeResponse(AbstractModel):
    """ModifyRuleAttribute返回参数结构体

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


class ModifySecurityRuleRequest(AbstractModel):
    """ModifySecurityRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AliasName: 规则名：不得超过30个字符，超过部分会被截断。
        :type AliasName: str
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        :param _RuleAction: 安全规则动作
        :type RuleAction: str
        :param _SourceCidr: 规则关联地址，格式需要满足CIDR网络地址规范
        :type SourceCidr: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _DestPortRange: 端口范围，支持以下格式
单个端口: 80
多个端口: 80,443
连续端口: 3306-20000
所有端口: ALL
        :type DestPortRange: str
        """
        self._RuleId = None
        self._AliasName = None
        self._PolicyId = None
        self._RuleAction = None
        self._SourceCidr = None
        self._Protocol = None
        self._DestPortRange = None

    @property
    def RuleId(self):
        """规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AliasName(self):
        """规则名：不得超过30个字符，超过部分会被截断。
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def RuleAction(self):
        """安全规则动作
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def SourceCidr(self):
        """规则关联地址，格式需要满足CIDR网络地址规范
        :rtype: str
        """
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr

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
    def DestPortRange(self):
        """端口范围，支持以下格式
单个端口: 80
多个端口: 80,443
连续端口: 3306-20000
所有端口: ALL
        :rtype: str
        """
        return self._DestPortRange

    @DestPortRange.setter
    def DestPortRange(self, DestPortRange):
        self._DestPortRange = DestPortRange


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AliasName = params.get("AliasName")
        self._PolicyId = params.get("PolicyId")
        self._RuleAction = params.get("RuleAction")
        self._SourceCidr = params.get("SourceCidr")
        self._Protocol = params.get("Protocol")
        self._DestPortRange = params.get("DestPortRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityRuleResponse(AbstractModel):
    """ModifySecurityRule返回参数结构体

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


class ModifyTCPListenerAttributeRequest(AbstractModel):
    """ModifyTCPListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param _ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。注意：lrtt需要开通白名单；RealServerType 为 DOMAIN 不支持wrr 和 lrtt。
        :type Scheduler: str
        :param _DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param _ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param _HealthCheck: 是否开启健康检查，1开启，0关闭。
        :type HealthCheck: int
        :param _FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param _HealthyThreshold: 健康阈值，表示连续检查成功多少次数后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: 不健康阈值，表示连续检查失败次数后认定源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        """
        self._ListenerId = None
        self._GroupId = None
        self._ProxyId = None
        self._ListenerName = None
        self._Scheduler = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthCheck = None
        self._FailoverSwitch = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def GroupId(self):
        """通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ProxyId(self):
        """通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。注意：lrtt需要开通白名单；RealServerType 为 DOMAIN 不支持wrr 和 lrtt。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def DelayLoop(self):
        """源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        """源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheck(self):
        """是否开启健康检查，1开启，0关闭。
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def FailoverSwitch(self):
        """源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :rtype: int
        """
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthyThreshold(self):
        """健康阈值，表示连续检查成功多少次数后认定源站健康。范围为1到10
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        """不健康阈值，表示连续检查失败次数后认定源站不健康。范围为1到10
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._GroupId = params.get("GroupId")
        self._ProxyId = params.get("ProxyId")
        self._ListenerName = params.get("ListenerName")
        self._Scheduler = params.get("Scheduler")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheck = params.get("HealthCheck")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTCPListenerAttributeResponse(AbstractModel):
    """ModifyTCPListenerAttribute返回参数结构体

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


class ModifyUDPListenerAttributeRequest(AbstractModel):
    """ModifyUDPListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param _ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param _ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param _HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param _HealthCheck: 源站是否开启健康检查：1开启，0关闭。
        :type HealthCheck: int
        :param _CheckType: UDP源站健康类型。PORT表示检查端口，PING表示PING。
        :type CheckType: str
        :param _CheckPort: UDP源站健康检查探测端口。
        :type CheckPort: int
        :param _ContextType: UDP源站健康检查端口探测报文类型：TEXT表示文本。仅在健康检查类型为PORT时使用。
        :type ContextType: str
        :param _SendContext: UDP源站健康检查端口探测发送报文。仅在健康检查类型为PORT时使用。
        :type SendContext: str
        :param _RecvContext: UDP源站健康检查端口探测接收报文。仅在健康检查类型为PORT时使用。
        :type RecvContext: str
        """
        self._ListenerId = None
        self._GroupId = None
        self._ProxyId = None
        self._ListenerName = None
        self._Scheduler = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._HealthCheck = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def GroupId(self):
        """通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ProxyId(self):
        """通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def DelayLoop(self):
        """源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        """源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthyThreshold(self):
        """健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        """不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        """源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :rtype: int
        """
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthCheck(self):
        """源站是否开启健康检查：1开启，0关闭。
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckType(self):
        """UDP源站健康类型。PORT表示检查端口，PING表示PING。
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        """UDP源站健康检查探测端口。
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        """UDP源站健康检查端口探测报文类型：TEXT表示文本。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        """UDP源站健康检查端口探测发送报文。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        """UDP源站健康检查端口探测接收报文。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._GroupId = params.get("GroupId")
        self._ProxyId = params.get("ProxyId")
        self._ListenerName = params.get("ListenerName")
        self._Scheduler = params.get("Scheduler")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthCheck = params.get("HealthCheck")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUDPListenerAttributeResponse(AbstractModel):
    """ModifyUDPListenerAttribute返回参数结构体

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


class NationCountryInnerInfo(AbstractModel):
    """就近接入的国家地区详情

    """

    def __init__(self):
        r"""
        :param _NationCountryName: 国家名
        :type NationCountryName: str
        :param _NationCountryInnerCode: 国家内部编码
        :type NationCountryInnerCode: str
        """
        self._NationCountryName = None
        self._NationCountryInnerCode = None

    @property
    def NationCountryName(self):
        """国家名
        :rtype: str
        """
        return self._NationCountryName

    @NationCountryName.setter
    def NationCountryName(self, NationCountryName):
        self._NationCountryName = NationCountryName

    @property
    def NationCountryInnerCode(self):
        """国家内部编码
        :rtype: str
        """
        return self._NationCountryInnerCode

    @NationCountryInnerCode.setter
    def NationCountryInnerCode(self, NationCountryInnerCode):
        self._NationCountryInnerCode = NationCountryInnerCode


    def _deserialize(self, params):
        self._NationCountryName = params.get("NationCountryName")
        self._NationCountryInnerCode = params.get("NationCountryInnerCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewRealServer(AbstractModel):
    """新添加源站信息

    """

    def __init__(self):
        r"""
        :param _RealServerId: 源站ID
        :type RealServerId: str
        :param _RealServerIP: 源站ip或域名
        :type RealServerIP: str
        """
        self._RealServerId = None
        self._RealServerIP = None

    @property
    def RealServerId(self):
        """源站ID
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerIP(self):
        """源站ip或域名
        :rtype: str
        """
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._RealServerIP = params.get("RealServerIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxiesRequest(AbstractModel):
    """OpenProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: （旧参数，请切换到ProxyIds）通道的实例ID列表。
        :type InstanceIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param _ProxyIds: （新参数）通道的实例ID列表。
        :type ProxyIds: list of str
        """
        self._InstanceIds = None
        self._ClientToken = None
        self._ProxyIds = None

    @property
    def InstanceIds(self):
        """（旧参数，请切换到ProxyIds）通道的实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def ProxyIds(self):
        """（新参数）通道的实例ID列表。
        :rtype: list of str
        """
        return self._ProxyIds

    @ProxyIds.setter
    def ProxyIds(self, ProxyIds):
        self._ProxyIds = ProxyIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ClientToken = params.get("ClientToken")
        self._ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxiesResponse(AbstractModel):
    """OpenProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: 非关闭状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        """非关闭状态下的通道实例ID列表，不可开启。
        :rtype: list of str
        """
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        """开启操作失败的通道实例ID列表。
        :rtype: list of str
        """
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

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
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class OpenProxyGroupRequest(AbstractModel):
    """OpenProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组实例 ID
        :type GroupId: str
        """
        self._GroupId = None

    @property
    def GroupId(self):
        """通道组实例 ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxyGroupResponse(AbstractModel):
    """OpenProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvalidStatusInstanceSet: 非关闭状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param _OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvalidStatusInstanceSet = None
        self._OperationFailedInstanceSet = None
        self._RequestId = None

    @property
    def InvalidStatusInstanceSet(self):
        """非关闭状态下的通道实例ID列表，不可开启。
        :rtype: list of str
        """
        return self._InvalidStatusInstanceSet

    @InvalidStatusInstanceSet.setter
    def InvalidStatusInstanceSet(self, InvalidStatusInstanceSet):
        self._InvalidStatusInstanceSet = InvalidStatusInstanceSet

    @property
    def OperationFailedInstanceSet(self):
        """开启操作失败的通道实例ID列表。
        :rtype: list of str
        """
        return self._OperationFailedInstanceSet

    @OperationFailedInstanceSet.setter
    def OperationFailedInstanceSet(self, OperationFailedInstanceSet):
        self._OperationFailedInstanceSet = OperationFailedInstanceSet

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
        self._InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self._OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self._RequestId = params.get("RequestId")


class OpenSecurityPolicyRequest(AbstractModel):
    """OpenSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProxyId: 需开启安全策略的通道ID
        :type ProxyId: str
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self._ProxyId = None
        self._PolicyId = None

    @property
    def ProxyId(self):
        """需开启安全策略的通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenSecurityPolicyResponse(AbstractModel):
    """OpenSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步流程ID，可以通过DescribeAsyncTaskStatus接口查询流程运行状态
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步流程ID，可以通过DescribeAsyncTaskStatus接口查询流程运行状态
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


class ProxyAccessInfo(AbstractModel):
    """加速通道接入点详细信息(包含id、地域、ip等）

    """

    def __init__(self):
        r"""
        :param _RegionId: 地域ID
        :type RegionId: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _ProxyId: 通道ID
        :type ProxyId: str
        :param _Vip: 通道接入ip
        :type Vip: str
        :param _VipList: 三网通道VIP列表
        :type VipList: list of IPDetail
        :param _SourceRegionIdcType: 接入点IDC类型。ec或dc
        :type SourceRegionIdcType: str
        """
        self._RegionId = None
        self._RegionName = None
        self._ProxyId = None
        self._Vip = None
        self._VipList = None
        self._SourceRegionIdcType = None

    @property
    def RegionId(self):
        """地域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def ProxyId(self):
        """通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Vip(self):
        """通道接入ip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VipList(self):
        """三网通道VIP列表
        :rtype: list of IPDetail
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList

    @property
    def SourceRegionIdcType(self):
        """接入点IDC类型。ec或dc
        :rtype: str
        """
        return self._SourceRegionIdcType

    @SourceRegionIdcType.setter
    def SourceRegionIdcType(self, SourceRegionIdcType):
        self._SourceRegionIdcType = SourceRegionIdcType


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._ProxyId = params.get("ProxyId")
        self._Vip = params.get("Vip")
        if params.get("VipList") is not None:
            self._VipList = []
            for item in params.get("VipList"):
                obj = IPDetail()
                obj._deserialize(item)
                self._VipList.append(obj)
        self._SourceRegionIdcType = params.get("SourceRegionIdcType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupDetail(AbstractModel):
    """通道组详情信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProxyNum: 通道组中通道数量
        :type ProxyNum: int
        :param _Status: 通道组状态：
0表示正常运行；
1表示创建中；
4表示销毁中；
11表示迁移中；
12表示部分部署中。
        :type Status: int
        :param _OwnerUin: 归属Uin
        :type OwnerUin: str
        :param _CreateUin: 创建Uin
        :type CreateUin: str
        :param _GroupName: 通道名称
        :type GroupName: str
        :param _DnsDefaultIp: 通道组域名解析默认IP
        :type DnsDefaultIp: str
        :param _Domain: 通道组域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _RealServerRegionInfo: 目标地域
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _IsOldGroup: 是否老通道组，2018-08-03之前创建的通道组为老通道组
        :type IsOldGroup: bool
        :param _GroupId: 通道组ID
        :type GroupId: str
        :param _TagSet: 标签列表
        :type TagSet: list of TagPair
        :param _PolicyId: 安全策略ID，当设置了安全策略时，存在该字段。
        :type PolicyId: str
        :param _Version: 通道组版本
        :type Version: str
        :param _ClientIPMethod: 通道获取客户端IP的方式，0表示TOA，1表示Proxy Protocol
        :type ClientIPMethod: list of int
        :param _IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param _PackageType: 通道组套餐类型：Thunder表示标准通道组，Accelerator表示银牌加速通道组，CrossBorder表示跨境通道组。
        :type PackageType: str
        :param _Http3Supported: 支持Http3特性的标识，其中：
0表示关闭；
1表示启用。
        :type Http3Supported: int
        :param _FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
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
        :param _IsSupportTLSChoice: 是否支持设置TLS设置
0表示不支持；
1表示支持。
        :type IsSupportTLSChoice: int
        """
        self._CreateTime = None
        self._ProjectId = None
        self._ProxyNum = None
        self._Status = None
        self._OwnerUin = None
        self._CreateUin = None
        self._GroupName = None
        self._DnsDefaultIp = None
        self._Domain = None
        self._RealServerRegionInfo = None
        self._IsOldGroup = None
        self._GroupId = None
        self._TagSet = None
        self._PolicyId = None
        self._Version = None
        self._ClientIPMethod = None
        self._IPAddressVersion = None
        self._PackageType = None
        self._Http3Supported = None
        self._FeatureBitmap = None
        self._IsSupportTLSChoice = None

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProxyNum(self):
        """通道组中通道数量
        :rtype: int
        """
        return self._ProxyNum

    @ProxyNum.setter
    def ProxyNum(self, ProxyNum):
        self._ProxyNum = ProxyNum

    @property
    def Status(self):
        """通道组状态：
0表示正常运行；
1表示创建中；
4表示销毁中；
11表示迁移中；
12表示部分部署中。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        """归属Uin
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def CreateUin(self):
        """创建Uin
        :rtype: str
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def GroupName(self):
        """通道名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def DnsDefaultIp(self):
        """通道组域名解析默认IP
        :rtype: str
        """
        return self._DnsDefaultIp

    @DnsDefaultIp.setter
    def DnsDefaultIp(self, DnsDefaultIp):
        self._DnsDefaultIp = DnsDefaultIp

    @property
    def Domain(self):
        """通道组域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RealServerRegionInfo(self):
        """目标地域
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        """
        return self._RealServerRegionInfo

    @RealServerRegionInfo.setter
    def RealServerRegionInfo(self, RealServerRegionInfo):
        self._RealServerRegionInfo = RealServerRegionInfo

    @property
    def IsOldGroup(self):
        """是否老通道组，2018-08-03之前创建的通道组为老通道组
        :rtype: bool
        """
        return self._IsOldGroup

    @IsOldGroup.setter
    def IsOldGroup(self, IsOldGroup):
        self._IsOldGroup = IsOldGroup

    @property
    def GroupId(self):
        """通道组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def TagSet(self):
        """标签列表
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def PolicyId(self):
        """安全策略ID，当设置了安全策略时，存在该字段。
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Version(self):
        """通道组版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ClientIPMethod(self):
        """通道获取客户端IP的方式，0表示TOA，1表示Proxy Protocol
        :rtype: list of int
        """
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def IPAddressVersion(self):
        """IP版本，可取值：IPv4、IPv6，默认值IPv4
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def PackageType(self):
        """通道组套餐类型：Thunder表示标准通道组，Accelerator表示银牌加速通道组，CrossBorder表示跨境通道组。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def Http3Supported(self):
        """支持Http3特性的标识，其中：
0表示关闭；
1表示启用。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def FeatureBitmap(self):
        """特性位图，每个bit位代表一种特性，其中：
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
        :rtype: int
        """
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap

    @property
    def IsSupportTLSChoice(self):
        """是否支持设置TLS设置
0表示不支持；
1表示支持。
        :rtype: int
        """
        return self._IsSupportTLSChoice

    @IsSupportTLSChoice.setter
    def IsSupportTLSChoice(self, IsSupportTLSChoice):
        self._IsSupportTLSChoice = IsSupportTLSChoice


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._ProxyNum = params.get("ProxyNum")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateUin = params.get("CreateUin")
        self._GroupName = params.get("GroupName")
        self._DnsDefaultIp = params.get("DnsDefaultIp")
        self._Domain = params.get("Domain")
        if params.get("RealServerRegionInfo") is not None:
            self._RealServerRegionInfo = RegionDetail()
            self._RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self._IsOldGroup = params.get("IsOldGroup")
        self._GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._PolicyId = params.get("PolicyId")
        self._Version = params.get("Version")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._PackageType = params.get("PackageType")
        self._Http3Supported = params.get("Http3Supported")
        self._FeatureBitmap = params.get("FeatureBitmap")
        self._IsSupportTLSChoice = params.get("IsSupportTLSChoice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """通道组详情列表

    """

    def __init__(self):
        r"""
        :param _GroupId: 通道组id
        :type GroupId: str
        :param _Domain: 通道组域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _GroupName: 通道组名称
        :type GroupName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _RealServerRegionInfo: 目标地域
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _Status: 通道组状态。
其中，
RUNNING表示运行中；
CREATING表示创建中；
DESTROYING表示销毁中；
MOVING表示通道迁移中；
CLOSED表示已关闭；
CHANGING表示部分部署中。
        :type Status: str
        :param _TagSet: 标签列表。
        :type TagSet: list of TagPair
        :param _Version: 通道组版本
        :type Version: str
        :param _CreateTime: 创建时间
        :type CreateTime: int
        :param _ProxyType: 通道组是否包含微软通道
        :type ProxyType: int
        :param _Http3Supported: 支持Http3特性的标识，其中：
0表示关闭；
1表示启用。
        :type Http3Supported: int
        :param _FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
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
        self._GroupId = None
        self._Domain = None
        self._GroupName = None
        self._ProjectId = None
        self._RealServerRegionInfo = None
        self._Status = None
        self._TagSet = None
        self._Version = None
        self._CreateTime = None
        self._ProxyType = None
        self._Http3Supported = None
        self._FeatureBitmap = None

    @property
    def GroupId(self):
        """通道组id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Domain(self):
        """通道组域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def GroupName(self):
        """通道组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def RealServerRegionInfo(self):
        """目标地域
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        """
        return self._RealServerRegionInfo

    @RealServerRegionInfo.setter
    def RealServerRegionInfo(self, RealServerRegionInfo):
        self._RealServerRegionInfo = RealServerRegionInfo

    @property
    def Status(self):
        """通道组状态。
其中，
RUNNING表示运行中；
CREATING表示创建中；
DESTROYING表示销毁中；
MOVING表示通道迁移中；
CLOSED表示已关闭；
CHANGING表示部分部署中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TagSet(self):
        """标签列表。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Version(self):
        """通道组版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CreateTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProxyType(self):
        """通道组是否包含微软通道
        :rtype: int
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def Http3Supported(self):
        """支持Http3特性的标识，其中：
0表示关闭；
1表示启用。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def FeatureBitmap(self):
        """特性位图，每个bit位代表一种特性，其中：
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
        :rtype: int
        """
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Domain = params.get("Domain")
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        if params.get("RealServerRegionInfo") is not None:
            self._RealServerRegionInfo = RegionDetail()
            self._RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self._Status = params.get("Status")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._Version = params.get("Version")
        self._CreateTime = params.get("CreateTime")
        self._ProxyType = params.get("ProxyType")
        self._Http3Supported = params.get("Http3Supported")
        self._FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyIdDict(AbstractModel):
    """通道ID

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID
        :type ProxyId: str
        """
        self._ProxyId = None

    @property
    def ProxyId(self):
        """通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInfo(AbstractModel):
    """通道信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: （旧参数，请使用ProxyId）通道实例ID。
        :type InstanceId: str
        :param _CreateTime: 创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type CreateTime: int
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _ProxyName: 通道名称。
        :type ProxyName: str
        :param _AccessRegion: 接入地域。
        :type AccessRegion: str
        :param _RealServerRegion: 源站地域。
        :type RealServerRegion: str
        :param _Bandwidth: 带宽，单位：Mbps。
        :type Bandwidth: int
        :param _Concurrent: 并发，单位：万个/秒。
        :type Concurrent: int
        :param _Status: 通道状态。其中：
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
        :param _Domain: 接入域名。
        :type Domain: str
        :param _IP: 接入IP。
        :type IP: str
        :param _Version: 通道版本号：1.0，2.0，3.0。
        :type Version: str
        :param _ProxyId: （新参数）通道实例ID。
        :type ProxyId: str
        :param _Scalarable: 1，该通道可缩扩容；0，该通道无法缩扩容。
        :type Scalarable: int
        :param _SupportProtocols: 支持的协议类型。
        :type SupportProtocols: list of str
        :param _GroupId: 通道组ID，当通道归属于某一通道组时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _PolicyId: 安全策略ID，当设置了安全策略时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        :param _AccessRegionInfo: 接入地域详细信息，包括地域ID和地域名。
        :type AccessRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _RealServerRegionInfo: 源站地域详细信息，包括地域ID和地域名。
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param _ForwardIP: 通道转发IP
        :type ForwardIP: str
        :param _TagSet: 标签列表，不存在标签时，该字段为空列表。
        :type TagSet: list of TagPair
        :param _SupportSecurity: 是否支持安全组配置
        :type SupportSecurity: int
        :param _BillingType: 计费类型: 0表示按带宽计费  1表示按流量计费。
        :type BillingType: int
        :param _RelatedGlobalDomains: 关联了解析的域名列表
        :type RelatedGlobalDomains: list of str
        :param _ModifyConfigTime: 配置变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyConfigTime: int
        :param _ProxyType: 通道类型，100表示THUNDER通道，103表示微软合作通道
        :type ProxyType: int
        :param _ClientIPMethod: 通道获取客户端IP的方式，0表示TOA，1表示Proxy Protocol
        :type ClientIPMethod: list of int
        :param _IPAddressVersion: IP版本：IPv4、IPv6
        :type IPAddressVersion: str
        :param _NetworkType: 网络类型：normal表示常规BGP，cn2表示精品BGP，triple表示三网，secure_eip表示定制安全EIP
        :type NetworkType: str
        :param _PackageType: 通道套餐类型：Thunder表示标准通道，Accelerator表示银牌加速通道，
CrossBorder表示跨境通道。
        :type PackageType: str
        :param _BanStatus: 封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
        :type BanStatus: str
        :param _IPList: IP列表
        :type IPList: list of IPDetail
        :param _Http3Supported: 支持Http3协议的标识，其中：
0表示关闭；
1表示启用。
        :type Http3Supported: int
        :param _InBanBlacklist: 是否在封禁黑名单中，其中：0表示不在黑名单中，1表示在黑名单中。
        :type InBanBlacklist: int
        :param _FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
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
        :param _IsAutoScaleProxy: 是否是开启了auto scale的通道，0表示否，1表示是。
        :type IsAutoScaleProxy: int
        :param _IsSupportTLSChoice: 是否允许设置TLS配置
0表示不支持；
1表示支持。
        :type IsSupportTLSChoice: int
        """
        self._InstanceId = None
        self._CreateTime = None
        self._ProjectId = None
        self._ProxyName = None
        self._AccessRegion = None
        self._RealServerRegion = None
        self._Bandwidth = None
        self._Concurrent = None
        self._Status = None
        self._Domain = None
        self._IP = None
        self._Version = None
        self._ProxyId = None
        self._Scalarable = None
        self._SupportProtocols = None
        self._GroupId = None
        self._PolicyId = None
        self._AccessRegionInfo = None
        self._RealServerRegionInfo = None
        self._ForwardIP = None
        self._TagSet = None
        self._SupportSecurity = None
        self._BillingType = None
        self._RelatedGlobalDomains = None
        self._ModifyConfigTime = None
        self._ProxyType = None
        self._ClientIPMethod = None
        self._IPAddressVersion = None
        self._NetworkType = None
        self._PackageType = None
        self._BanStatus = None
        self._IPList = None
        self._Http3Supported = None
        self._InBanBlacklist = None
        self._FeatureBitmap = None
        self._IsAutoScaleProxy = None
        self._IsSupportTLSChoice = None

    @property
    def InstanceId(self):
        """（旧参数，请使用ProxyId）通道实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreateTime(self):
        """创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProjectId(self):
        """项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProxyName(self):
        """通道名称。
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def AccessRegion(self):
        """接入地域。
        :rtype: str
        """
        return self._AccessRegion

    @AccessRegion.setter
    def AccessRegion(self, AccessRegion):
        self._AccessRegion = AccessRegion

    @property
    def RealServerRegion(self):
        """源站地域。
        :rtype: str
        """
        return self._RealServerRegion

    @RealServerRegion.setter
    def RealServerRegion(self, RealServerRegion):
        self._RealServerRegion = RealServerRegion

    @property
    def Bandwidth(self):
        """带宽，单位：Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Concurrent(self):
        """并发，单位：万个/秒。
        :rtype: int
        """
        return self._Concurrent

    @Concurrent.setter
    def Concurrent(self, Concurrent):
        self._Concurrent = Concurrent

    @property
    def Status(self):
        """通道状态。其中：
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
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Domain(self):
        """接入域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IP(self):
        """接入IP。
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Version(self):
        """通道版本号：1.0，2.0，3.0。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ProxyId(self):
        """（新参数）通道实例ID。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def Scalarable(self):
        """1，该通道可缩扩容；0，该通道无法缩扩容。
        :rtype: int
        """
        return self._Scalarable

    @Scalarable.setter
    def Scalarable(self, Scalarable):
        self._Scalarable = Scalarable

    @property
    def SupportProtocols(self):
        """支持的协议类型。
        :rtype: list of str
        """
        return self._SupportProtocols

    @SupportProtocols.setter
    def SupportProtocols(self, SupportProtocols):
        self._SupportProtocols = SupportProtocols

    @property
    def GroupId(self):
        """通道组ID，当通道归属于某一通道组时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PolicyId(self):
        """安全策略ID，当设置了安全策略时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def AccessRegionInfo(self):
        """接入地域详细信息，包括地域ID和地域名。
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        """
        return self._AccessRegionInfo

    @AccessRegionInfo.setter
    def AccessRegionInfo(self, AccessRegionInfo):
        self._AccessRegionInfo = AccessRegionInfo

    @property
    def RealServerRegionInfo(self):
        """源站地域详细信息，包括地域ID和地域名。
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        """
        return self._RealServerRegionInfo

    @RealServerRegionInfo.setter
    def RealServerRegionInfo(self, RealServerRegionInfo):
        self._RealServerRegionInfo = RealServerRegionInfo

    @property
    def ForwardIP(self):
        """通道转发IP
        :rtype: str
        """
        return self._ForwardIP

    @ForwardIP.setter
    def ForwardIP(self, ForwardIP):
        self._ForwardIP = ForwardIP

    @property
    def TagSet(self):
        """标签列表，不存在标签时，该字段为空列表。
        :rtype: list of TagPair
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def SupportSecurity(self):
        """是否支持安全组配置
        :rtype: int
        """
        return self._SupportSecurity

    @SupportSecurity.setter
    def SupportSecurity(self, SupportSecurity):
        self._SupportSecurity = SupportSecurity

    @property
    def BillingType(self):
        """计费类型: 0表示按带宽计费  1表示按流量计费。
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def RelatedGlobalDomains(self):
        """关联了解析的域名列表
        :rtype: list of str
        """
        return self._RelatedGlobalDomains

    @RelatedGlobalDomains.setter
    def RelatedGlobalDomains(self, RelatedGlobalDomains):
        self._RelatedGlobalDomains = RelatedGlobalDomains

    @property
    def ModifyConfigTime(self):
        """配置变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ModifyConfigTime

    @ModifyConfigTime.setter
    def ModifyConfigTime(self, ModifyConfigTime):
        self._ModifyConfigTime = ModifyConfigTime

    @property
    def ProxyType(self):
        """通道类型，100表示THUNDER通道，103表示微软合作通道
        :rtype: int
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType

    @property
    def ClientIPMethod(self):
        """通道获取客户端IP的方式，0表示TOA，1表示Proxy Protocol
        :rtype: list of int
        """
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def IPAddressVersion(self):
        """IP版本：IPv4、IPv6
        :rtype: str
        """
        return self._IPAddressVersion

    @IPAddressVersion.setter
    def IPAddressVersion(self, IPAddressVersion):
        self._IPAddressVersion = IPAddressVersion

    @property
    def NetworkType(self):
        """网络类型：normal表示常规BGP，cn2表示精品BGP，triple表示三网，secure_eip表示定制安全EIP
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def PackageType(self):
        """通道套餐类型：Thunder表示标准通道，Accelerator表示银牌加速通道，
CrossBorder表示跨境通道。
        :rtype: str
        """
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def BanStatus(self):
        """封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
        :rtype: str
        """
        return self._BanStatus

    @BanStatus.setter
    def BanStatus(self, BanStatus):
        self._BanStatus = BanStatus

    @property
    def IPList(self):
        """IP列表
        :rtype: list of IPDetail
        """
        return self._IPList

    @IPList.setter
    def IPList(self, IPList):
        self._IPList = IPList

    @property
    def Http3Supported(self):
        """支持Http3协议的标识，其中：
0表示关闭；
1表示启用。
        :rtype: int
        """
        return self._Http3Supported

    @Http3Supported.setter
    def Http3Supported(self, Http3Supported):
        self._Http3Supported = Http3Supported

    @property
    def InBanBlacklist(self):
        """是否在封禁黑名单中，其中：0表示不在黑名单中，1表示在黑名单中。
        :rtype: int
        """
        return self._InBanBlacklist

    @InBanBlacklist.setter
    def InBanBlacklist(self, InBanBlacklist):
        self._InBanBlacklist = InBanBlacklist

    @property
    def FeatureBitmap(self):
        """特性位图，每个bit位代表一种特性，其中：
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
        :rtype: int
        """
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap

    @property
    def IsAutoScaleProxy(self):
        """是否是开启了auto scale的通道，0表示否，1表示是。
        :rtype: int
        """
        return self._IsAutoScaleProxy

    @IsAutoScaleProxy.setter
    def IsAutoScaleProxy(self, IsAutoScaleProxy):
        self._IsAutoScaleProxy = IsAutoScaleProxy

    @property
    def IsSupportTLSChoice(self):
        """是否允许设置TLS配置
0表示不支持；
1表示支持。
        :rtype: int
        """
        return self._IsSupportTLSChoice

    @IsSupportTLSChoice.setter
    def IsSupportTLSChoice(self, IsSupportTLSChoice):
        self._IsSupportTLSChoice = IsSupportTLSChoice


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CreateTime = params.get("CreateTime")
        self._ProjectId = params.get("ProjectId")
        self._ProxyName = params.get("ProxyName")
        self._AccessRegion = params.get("AccessRegion")
        self._RealServerRegion = params.get("RealServerRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._Concurrent = params.get("Concurrent")
        self._Status = params.get("Status")
        self._Domain = params.get("Domain")
        self._IP = params.get("IP")
        self._Version = params.get("Version")
        self._ProxyId = params.get("ProxyId")
        self._Scalarable = params.get("Scalarable")
        self._SupportProtocols = params.get("SupportProtocols")
        self._GroupId = params.get("GroupId")
        self._PolicyId = params.get("PolicyId")
        if params.get("AccessRegionInfo") is not None:
            self._AccessRegionInfo = RegionDetail()
            self._AccessRegionInfo._deserialize(params.get("AccessRegionInfo"))
        if params.get("RealServerRegionInfo") is not None:
            self._RealServerRegionInfo = RegionDetail()
            self._RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self._ForwardIP = params.get("ForwardIP")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._SupportSecurity = params.get("SupportSecurity")
        self._BillingType = params.get("BillingType")
        self._RelatedGlobalDomains = params.get("RelatedGlobalDomains")
        self._ModifyConfigTime = params.get("ModifyConfigTime")
        self._ProxyType = params.get("ProxyType")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._IPAddressVersion = params.get("IPAddressVersion")
        self._NetworkType = params.get("NetworkType")
        self._PackageType = params.get("PackageType")
        self._BanStatus = params.get("BanStatus")
        if params.get("IPList") is not None:
            self._IPList = []
            for item in params.get("IPList"):
                obj = IPDetail()
                obj._deserialize(item)
                self._IPList.append(obj)
        self._Http3Supported = params.get("Http3Supported")
        self._InBanBlacklist = params.get("InBanBlacklist")
        self._FeatureBitmap = params.get("FeatureBitmap")
        self._IsAutoScaleProxy = params.get("IsAutoScaleProxy")
        self._IsSupportTLSChoice = params.get("IsSupportTLSChoice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxySimpleInfo(AbstractModel):
    """内部接口使用，返回可以查询统计数据的通道和对应的监听器信息

    """

    def __init__(self):
        r"""
        :param _ProxyId: 通道ID
        :type ProxyId: str
        :param _ProxyName: 通道名称
        :type ProxyName: str
        :param _ListenerList: 监听器列表
        :type ListenerList: list of ListenerInfo
        """
        self._ProxyId = None
        self._ProxyName = None
        self._ListenerList = None

    @property
    def ProxyId(self):
        """通道ID
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def ProxyName(self):
        """通道名称
        :rtype: str
        """
        return self._ProxyName

    @ProxyName.setter
    def ProxyName(self, ProxyName):
        self._ProxyName = ProxyName

    @property
    def ListenerList(self):
        """监听器列表
        :rtype: list of ListenerInfo
        """
        return self._ListenerList

    @ListenerList.setter
    def ListenerList(self, ListenerList):
        self._ListenerList = ListenerList


    def _deserialize(self, params):
        self._ProxyId = params.get("ProxyId")
        self._ProxyName = params.get("ProxyName")
        if params.get("ListenerList") is not None:
            self._ListenerList = []
            for item in params.get("ListenerList"):
                obj = ListenerInfo()
                obj._deserialize(item)
                self._ListenerList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyStatus(AbstractModel):
    """通道状态信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 通道实例ID。
        :type InstanceId: str
        :param _Status: 通道状态。
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
        self._InstanceId = None
        self._Status = None

    @property
    def InstanceId(self):
        """通道实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Status(self):
        """通道状态。
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
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServer(AbstractModel):
    """查询监听器或者规则相关的源站信息，不包括tag信息

    """

    def __init__(self):
        r"""
        :param _RealServerIP: 源站的IP或域名
        :type RealServerIP: str
        :param _RealServerId: 源站ID
        :type RealServerId: str
        :param _RealServerName: 源站名称
        :type RealServerName: str
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _InBanBlacklist: 是否在封禁黑名单中，其中：0表示不在黑名单中，1表示在黑名单中。
        :type InBanBlacklist: int
        """
        self._RealServerIP = None
        self._RealServerId = None
        self._RealServerName = None
        self._ProjectId = None
        self._InBanBlacklist = None

    @property
    def RealServerIP(self):
        """源站的IP或域名
        :rtype: str
        """
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerId(self):
        """源站ID
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerName(self):
        """源站名称
        :rtype: str
        """
        return self._RealServerName

    @RealServerName.setter
    def RealServerName(self, RealServerName):
        self._RealServerName = RealServerName

    @property
    def ProjectId(self):
        """项目ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InBanBlacklist(self):
        """是否在封禁黑名单中，其中：0表示不在黑名单中，1表示在黑名单中。
        :rtype: int
        """
        return self._InBanBlacklist

    @InBanBlacklist.setter
    def InBanBlacklist(self, InBanBlacklist):
        self._InBanBlacklist = InBanBlacklist


    def _deserialize(self, params):
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerId = params.get("RealServerId")
        self._RealServerName = params.get("RealServerName")
        self._ProjectId = params.get("ProjectId")
        self._InBanBlacklist = params.get("InBanBlacklist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServerBindSetReq(AbstractModel):
    """绑定的源站信息

    """

    def __init__(self):
        r"""
        :param _RealServerId: 源站id
        :type RealServerId: str
        :param _RealServerPort: 源站端口
        :type RealServerPort: int
        :param _RealServerIP: 源站IP
        :type RealServerIP: str
        :param _RealServerWeight: 源站权重
        :type RealServerWeight: int
        :param _RealServerFailoverRole: 源站主备角色：master表示主，slave表示备，该参数必须在监听器打开了源站主备模式。
        :type RealServerFailoverRole: str
        """
        self._RealServerId = None
        self._RealServerPort = None
        self._RealServerIP = None
        self._RealServerWeight = None
        self._RealServerFailoverRole = None

    @property
    def RealServerId(self):
        """源站id
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def RealServerPort(self):
        """源站端口
        :rtype: int
        """
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def RealServerIP(self):
        """源站IP
        :rtype: str
        """
        return self._RealServerIP

    @RealServerIP.setter
    def RealServerIP(self, RealServerIP):
        self._RealServerIP = RealServerIP

    @property
    def RealServerWeight(self):
        """源站权重
        :rtype: int
        """
        return self._RealServerWeight

    @RealServerWeight.setter
    def RealServerWeight(self, RealServerWeight):
        self._RealServerWeight = RealServerWeight

    @property
    def RealServerFailoverRole(self):
        """源站主备角色：master表示主，slave表示备，该参数必须在监听器打开了源站主备模式。
        :rtype: str
        """
        return self._RealServerFailoverRole

    @RealServerFailoverRole.setter
    def RealServerFailoverRole(self, RealServerFailoverRole):
        self._RealServerFailoverRole = RealServerFailoverRole


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._RealServerPort = params.get("RealServerPort")
        self._RealServerIP = params.get("RealServerIP")
        self._RealServerWeight = params.get("RealServerWeight")
        self._RealServerFailoverRole = params.get("RealServerFailoverRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServerStatus(AbstractModel):
    """源站绑定信息查询，BindStatus， 0: 未被绑定 1：被规则或者监听器绑定

    """

    def __init__(self):
        r"""
        :param _RealServerId: 源站ID。
        :type RealServerId: str
        :param _BindStatus: 0表示未被绑定 1表示被规则或者监听器绑定。
        :type BindStatus: int
        :param _ProxyId: 绑定此源站的通道ID，没有绑定时为空字符串。
        :type ProxyId: str
        :param _GroupId: 绑定此源站的通道组ID，没有绑定时为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
        self._RealServerId = None
        self._BindStatus = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def RealServerId(self):
        """源站ID。
        :rtype: str
        """
        return self._RealServerId

    @RealServerId.setter
    def RealServerId(self, RealServerId):
        self._RealServerId = RealServerId

    @property
    def BindStatus(self):
        """0表示未被绑定 1表示被规则或者监听器绑定。
        :rtype: int
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def ProxyId(self):
        """绑定此源站的通道ID，没有绑定时为空字符串。
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """绑定此源站的通道组ID，没有绑定时为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._RealServerId = params.get("RealServerId")
        self._BindStatus = params.get("BindStatus")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionDetail(AbstractModel):
    """区域信息详情

    """

    def __init__(self):
        r"""
        :param _RegionId: 区域ID
        :type RegionId: str
        :param _RegionName: 区域英文名或中文名
        :type RegionName: str
        :param _RegionArea: 机房所属大区
        :type RegionArea: str
        :param _RegionAreaName: 机房所属大区名
        :type RegionAreaName: str
        :param _IDCType: 机房类型, dc表示DataCenter数据中心, ec表示EdgeComputing边缘节点
        :type IDCType: str
        :param _FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
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
        :type FeatureBitmap: int
        :param _SupportFeature: 接入区域支持的能力
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportFeature: :class:`tencentcloud.gaap.v20180529.models.SupportFeature`
        """
        self._RegionId = None
        self._RegionName = None
        self._RegionArea = None
        self._RegionAreaName = None
        self._IDCType = None
        self._FeatureBitmap = None
        self._SupportFeature = None

    @property
    def RegionId(self):
        """区域ID
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def RegionName(self):
        """区域英文名或中文名
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionArea(self):
        """机房所属大区
        :rtype: str
        """
        return self._RegionArea

    @RegionArea.setter
    def RegionArea(self, RegionArea):
        self._RegionArea = RegionArea

    @property
    def RegionAreaName(self):
        """机房所属大区名
        :rtype: str
        """
        return self._RegionAreaName

    @RegionAreaName.setter
    def RegionAreaName(self, RegionAreaName):
        self._RegionAreaName = RegionAreaName

    @property
    def IDCType(self):
        """机房类型, dc表示DataCenter数据中心, ec表示EdgeComputing边缘节点
        :rtype: str
        """
        return self._IDCType

    @IDCType.setter
    def IDCType(self, IDCType):
        self._IDCType = IDCType

    @property
    def FeatureBitmap(self):
        """特性位图，每个bit位代表一种特性，其中：
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
        :rtype: int
        """
        return self._FeatureBitmap

    @FeatureBitmap.setter
    def FeatureBitmap(self, FeatureBitmap):
        self._FeatureBitmap = FeatureBitmap

    @property
    def SupportFeature(self):
        """接入区域支持的能力
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.gaap.v20180529.models.SupportFeature`
        """
        return self._SupportFeature

    @SupportFeature.setter
    def SupportFeature(self, SupportFeature):
        self._SupportFeature = SupportFeature


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._RegionName = params.get("RegionName")
        self._RegionArea = params.get("RegionArea")
        self._RegionAreaName = params.get("RegionAreaName")
        self._IDCType = params.get("IDCType")
        self._FeatureBitmap = params.get("FeatureBitmap")
        if params.get("SupportFeature") is not None:
            self._SupportFeature = SupportFeature()
            self._SupportFeature._deserialize(params.get("SupportFeature"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRealServersRequest(AbstractModel):
    """RemoveRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RealServerIds: 源站Id列表
        :type RealServerIds: list of str
        """
        self._RealServerIds = None

    @property
    def RealServerIds(self):
        """源站Id列表
        :rtype: list of str
        """
        return self._RealServerIds

    @RealServerIds.setter
    def RealServerIds(self, RealServerIds):
        self._RealServerIds = RealServerIds


    def _deserialize(self, params):
        self._RealServerIds = params.get("RealServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRealServersResponse(AbstractModel):
    """RemoveRealServers返回参数结构体

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


class RuleCheckParams(AbstractModel):
    """7层监听器转发规则健康检查相关参数

    """

    def __init__(self):
        r"""
        :param _DelayLoop: 健康检查的时间间隔
        :type DelayLoop: int
        :param _ConnectTimeout: 健康检查的响应超时时间
        :type ConnectTimeout: int
        :param _Path: 健康检查的检查路径
        :type Path: str
        :param _Method: 健康检查的方法，GET/HEAD
        :type Method: str
        :param _StatusCode: 确认源站正常的返回码，可选范围[100, 200, 300, 400, 500]
        :type StatusCode: list of int non-negative
        :param _Domain: 健康检查的检查域名。
当调用ModifyRuleAttribute时，不支持修改该参数。
        :type Domain: str
        :param _FailedCountInter: 源站服务失败统计频率
        :type FailedCountInter: int
        :param _FailedThreshold: 源站健康性检查阀值，超过该阀值会屏蔽服务
        :type FailedThreshold: int
        :param _BlockInter: 源站健康性检测超出阀值后，屏蔽的时间
        :type BlockInter: int
        """
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._Path = None
        self._Method = None
        self._StatusCode = None
        self._Domain = None
        self._FailedCountInter = None
        self._FailedThreshold = None
        self._BlockInter = None

    @property
    def DelayLoop(self):
        """健康检查的时间间隔
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        """健康检查的响应超时时间
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def Path(self):
        """健康检查的检查路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        """健康检查的方法，GET/HEAD
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def StatusCode(self):
        """确认源站正常的返回码，可选范围[100, 200, 300, 400, 500]
        :rtype: list of int non-negative
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def Domain(self):
        """健康检查的检查域名。
当调用ModifyRuleAttribute时，不支持修改该参数。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def FailedCountInter(self):
        """源站服务失败统计频率
        :rtype: int
        """
        return self._FailedCountInter

    @FailedCountInter.setter
    def FailedCountInter(self, FailedCountInter):
        self._FailedCountInter = FailedCountInter

    @property
    def FailedThreshold(self):
        """源站健康性检查阀值，超过该阀值会屏蔽服务
        :rtype: int
        """
        return self._FailedThreshold

    @FailedThreshold.setter
    def FailedThreshold(self, FailedThreshold):
        self._FailedThreshold = FailedThreshold

    @property
    def BlockInter(self):
        """源站健康性检测超出阀值后，屏蔽的时间
        :rtype: int
        """
        return self._BlockInter

    @BlockInter.setter
    def BlockInter(self, BlockInter):
        self._BlockInter = BlockInter


    def _deserialize(self, params):
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._Domain = params.get("Domain")
        self._FailedCountInter = params.get("FailedCountInter")
        self._FailedThreshold = params.get("FailedThreshold")
        self._BlockInter = params.get("BlockInter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """7层监听器转发规则信息

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则信息
        :type RuleId: str
        :param _ListenerId: 监听器信息
        :type ListenerId: str
        :param _Domain: 规则域名
        :type Domain: str
        :param _Path: 规则路径
        :type Path: str
        :param _RealServerType: 源站类型
        :type RealServerType: str
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _HealthCheck: 是否开启健康检查标志，1表示开启，0表示关闭
        :type HealthCheck: int
        :param _RuleStatus: 规则状态，0表示运行中，1表示创建中，2表示销毁中，3表示绑定解绑源站中，4表示配置更新中
        :type RuleStatus: int
        :param _CheckParams: 健康检查相关参数
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param _RealServerSet: 已绑定的源站相关信息
        :type RealServerSet: list of BindRealServer
        :param _BindStatus: 源站的服务状态，0表示异常，1表示正常。
未开启健康检查时，该状态始终未正常。
只要有一个源站健康状态为异常时，该状态为异常，具体源站的状态请查看RealServerSet。
        :type BindStatus: int
        :param _ForwardHost: 通道转发到源站的请求所携带的host，其中default表示直接转发接收到的host。
        :type ForwardHost: str
        :param _ServerNameIndicationSwitch: 服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerNameIndicationSwitch: str
        :param _ServerNameIndication: 服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerNameIndication: str
        :param _ForcedRedirect: 强转HTTPS指示，当传递值为https:时表示强转为https
注意：此字段可能返回 null，表示取不到有效值。
        :type ForcedRedirect: str
        """
        self._RuleId = None
        self._ListenerId = None
        self._Domain = None
        self._Path = None
        self._RealServerType = None
        self._Scheduler = None
        self._HealthCheck = None
        self._RuleStatus = None
        self._CheckParams = None
        self._RealServerSet = None
        self._BindStatus = None
        self._ForwardHost = None
        self._ServerNameIndicationSwitch = None
        self._ServerNameIndication = None
        self._ForcedRedirect = None

    @property
    def RuleId(self):
        """规则信息
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def ListenerId(self):
        """监听器信息
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        """规则域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Path(self):
        """规则路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def RealServerType(self):
        """源站类型
        :rtype: str
        """
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def HealthCheck(self):
        """是否开启健康检查标志，1表示开启，0表示关闭
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def RuleStatus(self):
        """规则状态，0表示运行中，1表示创建中，2表示销毁中，3表示绑定解绑源站中，4表示配置更新中
        :rtype: int
        """
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def CheckParams(self):
        """健康检查相关参数
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        """
        return self._CheckParams

    @CheckParams.setter
    def CheckParams(self, CheckParams):
        self._CheckParams = CheckParams

    @property
    def RealServerSet(self):
        """已绑定的源站相关信息
        :rtype: list of BindRealServer
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def BindStatus(self):
        """源站的服务状态，0表示异常，1表示正常。
未开启健康检查时，该状态始终未正常。
只要有一个源站健康状态为异常时，该状态为异常，具体源站的状态请查看RealServerSet。
        :rtype: int
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def ForwardHost(self):
        """通道转发到源站的请求所携带的host，其中default表示直接转发接收到的host。
        :rtype: str
        """
        return self._ForwardHost

    @ForwardHost.setter
    def ForwardHost(self, ForwardHost):
        self._ForwardHost = ForwardHost

    @property
    def ServerNameIndicationSwitch(self):
        """服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerNameIndicationSwitch

    @ServerNameIndicationSwitch.setter
    def ServerNameIndicationSwitch(self, ServerNameIndicationSwitch):
        self._ServerNameIndicationSwitch = ServerNameIndicationSwitch

    @property
    def ServerNameIndication(self):
        """服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerNameIndication

    @ServerNameIndication.setter
    def ServerNameIndication(self, ServerNameIndication):
        self._ServerNameIndication = ServerNameIndication

    @property
    def ForcedRedirect(self):
        """强转HTTPS指示，当传递值为https:时表示强转为https
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ForcedRedirect

    @ForcedRedirect.setter
    def ForcedRedirect(self, ForcedRedirect):
        self._ForcedRedirect = ForcedRedirect


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._Path = params.get("Path")
        self._RealServerType = params.get("RealServerType")
        self._Scheduler = params.get("Scheduler")
        self._HealthCheck = params.get("HealthCheck")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("CheckParams") is not None:
            self._CheckParams = RuleCheckParams()
            self._CheckParams._deserialize(params.get("CheckParams"))
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._BindStatus = params.get("BindStatus")
        self._ForwardHost = params.get("ForwardHost")
        self._ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self._ServerNameIndication = params.get("ServerNameIndication")
        self._ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRuleIn(AbstractModel):
    """安全策略规则（入参）

    """

    def __init__(self):
        r"""
        :param _SourceCidr: 请求来源IP或IP段。
        :type SourceCidr: str
        :param _Action: 策略：允许（ACCEPT）或拒绝（DROP）
        :type Action: str
        :param _AliasName: 规则别名
        :type AliasName: str
        :param _Protocol: 协议：TCP或UDP，ALL表示所有协议
        :type Protocol: str
        :param _DestPortRange: 目标端口，填写格式举例：
单个端口: 80
多个端口: 80,443
连续端口: 3306-20000
所有端口: ALL
        :type DestPortRange: str
        """
        self._SourceCidr = None
        self._Action = None
        self._AliasName = None
        self._Protocol = None
        self._DestPortRange = None

    @property
    def SourceCidr(self):
        """请求来源IP或IP段。
        :rtype: str
        """
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr

    @property
    def Action(self):
        """策略：允许（ACCEPT）或拒绝（DROP）
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def AliasName(self):
        """规则别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def Protocol(self):
        """协议：TCP或UDP，ALL表示所有协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DestPortRange(self):
        """目标端口，填写格式举例：
单个端口: 80
多个端口: 80,443
连续端口: 3306-20000
所有端口: ALL
        :rtype: str
        """
        return self._DestPortRange

    @DestPortRange.setter
    def DestPortRange(self, DestPortRange):
        self._DestPortRange = DestPortRange


    def _deserialize(self, params):
        self._SourceCidr = params.get("SourceCidr")
        self._Action = params.get("Action")
        self._AliasName = params.get("AliasName")
        self._Protocol = params.get("Protocol")
        self._DestPortRange = params.get("DestPortRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRuleOut(AbstractModel):
    """安全策略规则（出参）

    """

    def __init__(self):
        r"""
        :param _Action: 策略：允许（ACCEPT）或拒绝（DROP）
        :type Action: str
        :param _SourceCidr: 请求来源Ip或Ip段
        :type SourceCidr: str
        :param _AliasName: 规则别名
        :type AliasName: str
        :param _DestPortRange: 目标端口范围
        :type DestPortRange: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Protocol: 要匹配的协议类型（TCP/UDP）
        :type Protocol: str
        :param _PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self._Action = None
        self._SourceCidr = None
        self._AliasName = None
        self._DestPortRange = None
        self._RuleId = None
        self._Protocol = None
        self._PolicyId = None

    @property
    def Action(self):
        """策略：允许（ACCEPT）或拒绝（DROP）
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def SourceCidr(self):
        """请求来源Ip或Ip段
        :rtype: str
        """
        return self._SourceCidr

    @SourceCidr.setter
    def SourceCidr(self, SourceCidr):
        self._SourceCidr = SourceCidr

    @property
    def AliasName(self):
        """规则别名
        :rtype: str
        """
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def DestPortRange(self):
        """目标端口范围
        :rtype: str
        """
        return self._DestPortRange

    @DestPortRange.setter
    def DestPortRange(self, DestPortRange):
        self._DestPortRange = DestPortRange

    @property
    def RuleId(self):
        """规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Protocol(self):
        """要匹配的协议类型（TCP/UDP）
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PolicyId(self):
        """安全策略ID
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._SourceCidr = params.get("SourceCidr")
        self._AliasName = params.get("AliasName")
        self._DestPortRange = params.get("DestPortRange")
        self._RuleId = params.get("RuleId")
        self._Protocol = params.get("Protocol")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAuthenticationRequest(AbstractModel):
    """SetAuthentication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _Domain: 需要进行高级配置的域名，该域名为监听器下的转发规则的域名。
        :type Domain: str
        :param _BasicAuth: 基础认证开关，其中：
0，关闭基础认证；
1，开启基础认证。
默认为0。
        :type BasicAuth: int
        :param _GaapAuth: 通道认证开关，用于源站对Gaap的认证，其中：
0，关闭通道认证；
1，开启通道认证。
默认为0。
        :type GaapAuth: int
        :param _RealServerAuth: 源站认证开关，用于Gaap对服务器的认证，其中：
0，关闭源站认证；
1，开启源站认证。
默认为0。
        :type RealServerAuth: int
        :param _BasicAuthConfId: 基础认证配置ID，从证书管理页获取。
        :type BasicAuthConfId: str
        :param _GaapCertificateId: 通道SSL证书ID，从证书管理页获取。
        :type GaapCertificateId: str
        :param _RealServerCertificateId: 源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数
        :type RealServerCertificateId: str
        :param _RealServerCertificateDomain: 该字段已废弃，请使用创建规则和修改规则中的SNI功能。
        :type RealServerCertificateDomain: str
        :param _PolyRealServerCertificateIds: 多源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数
        :type PolyRealServerCertificateIds: list of str
        :param _TLSSupportVersion: TLS支持的版本
支持TLSv1，TLSv1.1,TLSv1.2,TLSv1.3
        :type TLSSupportVersion: list of str
        :param _TLSCiphers: 支持的TLS密码套件，可选值为：
[GAAP_TLS_CIPHERS_WIDE,GAAPTLS_CIPHERS_GENERAL,GAAPTLS_CIPHERS_STRICT]
        :type TLSCiphers: str
        """
        self._ListenerId = None
        self._Domain = None
        self._BasicAuth = None
        self._GaapAuth = None
        self._RealServerAuth = None
        self._BasicAuthConfId = None
        self._GaapCertificateId = None
        self._RealServerCertificateId = None
        self._RealServerCertificateDomain = None
        self._PolyRealServerCertificateIds = None
        self._TLSSupportVersion = None
        self._TLSCiphers = None

    @property
    def ListenerId(self):
        """监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domain(self):
        """需要进行高级配置的域名，该域名为监听器下的转发规则的域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def BasicAuth(self):
        """基础认证开关，其中：
0，关闭基础认证；
1，开启基础认证。
默认为0。
        :rtype: int
        """
        return self._BasicAuth

    @BasicAuth.setter
    def BasicAuth(self, BasicAuth):
        self._BasicAuth = BasicAuth

    @property
    def GaapAuth(self):
        """通道认证开关，用于源站对Gaap的认证，其中：
0，关闭通道认证；
1，开启通道认证。
默认为0。
        :rtype: int
        """
        return self._GaapAuth

    @GaapAuth.setter
    def GaapAuth(self, GaapAuth):
        self._GaapAuth = GaapAuth

    @property
    def RealServerAuth(self):
        """源站认证开关，用于Gaap对服务器的认证，其中：
0，关闭源站认证；
1，开启源站认证。
默认为0。
        :rtype: int
        """
        return self._RealServerAuth

    @RealServerAuth.setter
    def RealServerAuth(self, RealServerAuth):
        self._RealServerAuth = RealServerAuth

    @property
    def BasicAuthConfId(self):
        """基础认证配置ID，从证书管理页获取。
        :rtype: str
        """
        return self._BasicAuthConfId

    @BasicAuthConfId.setter
    def BasicAuthConfId(self, BasicAuthConfId):
        self._BasicAuthConfId = BasicAuthConfId

    @property
    def GaapCertificateId(self):
        """通道SSL证书ID，从证书管理页获取。
        :rtype: str
        """
        return self._GaapCertificateId

    @GaapCertificateId.setter
    def GaapCertificateId(self, GaapCertificateId):
        self._GaapCertificateId = GaapCertificateId

    @property
    def RealServerCertificateId(self):
        """源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数
        :rtype: str
        """
        return self._RealServerCertificateId

    @RealServerCertificateId.setter
    def RealServerCertificateId(self, RealServerCertificateId):
        self._RealServerCertificateId = RealServerCertificateId

    @property
    def RealServerCertificateDomain(self):
        """该字段已废弃，请使用创建规则和修改规则中的SNI功能。
        :rtype: str
        """
        return self._RealServerCertificateDomain

    @RealServerCertificateDomain.setter
    def RealServerCertificateDomain(self, RealServerCertificateDomain):
        self._RealServerCertificateDomain = RealServerCertificateDomain

    @property
    def PolyRealServerCertificateIds(self):
        """多源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数
        :rtype: list of str
        """
        return self._PolyRealServerCertificateIds

    @PolyRealServerCertificateIds.setter
    def PolyRealServerCertificateIds(self, PolyRealServerCertificateIds):
        self._PolyRealServerCertificateIds = PolyRealServerCertificateIds

    @property
    def TLSSupportVersion(self):
        """TLS支持的版本
支持TLSv1，TLSv1.1,TLSv1.2,TLSv1.3
        :rtype: list of str
        """
        return self._TLSSupportVersion

    @TLSSupportVersion.setter
    def TLSSupportVersion(self, TLSSupportVersion):
        self._TLSSupportVersion = TLSSupportVersion

    @property
    def TLSCiphers(self):
        """支持的TLS密码套件，可选值为：
[GAAP_TLS_CIPHERS_WIDE,GAAPTLS_CIPHERS_GENERAL,GAAPTLS_CIPHERS_STRICT]
        :rtype: str
        """
        return self._TLSCiphers

    @TLSCiphers.setter
    def TLSCiphers(self, TLSCiphers):
        self._TLSCiphers = TLSCiphers


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Domain = params.get("Domain")
        self._BasicAuth = params.get("BasicAuth")
        self._GaapAuth = params.get("GaapAuth")
        self._RealServerAuth = params.get("RealServerAuth")
        self._BasicAuthConfId = params.get("BasicAuthConfId")
        self._GaapCertificateId = params.get("GaapCertificateId")
        self._RealServerCertificateId = params.get("RealServerCertificateId")
        self._RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        self._PolyRealServerCertificateIds = params.get("PolyRealServerCertificateIds")
        self._TLSSupportVersion = params.get("TLSSupportVersion")
        self._TLSCiphers = params.get("TLSCiphers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAuthenticationResponse(AbstractModel):
    """SetAuthentication返回参数结构体

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


class SetTlsVersionRequest(AbstractModel):
    """SetTlsVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _TLSSupportVersion: TLS版本,可选TLSv1、TLSv1.1、TLSv1.2、TLSv1.3
        :type TLSSupportVersion: list of str
        :param _TLSCiphers: 密码套件包,可选 GAAP_TLS_CIPHERS_STRICT，GAAP_TLS_CIPHERS_GENERAL，GAAP_TLS_CIPHERS_WIDE(默认)
        :type TLSCiphers: str
        """
        self._ListenerId = None
        self._TLSSupportVersion = None
        self._TLSCiphers = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def TLSSupportVersion(self):
        """TLS版本,可选TLSv1、TLSv1.1、TLSv1.2、TLSv1.3
        :rtype: list of str
        """
        return self._TLSSupportVersion

    @TLSSupportVersion.setter
    def TLSSupportVersion(self, TLSSupportVersion):
        self._TLSSupportVersion = TLSSupportVersion

    @property
    def TLSCiphers(self):
        """密码套件包,可选 GAAP_TLS_CIPHERS_STRICT，GAAP_TLS_CIPHERS_GENERAL，GAAP_TLS_CIPHERS_WIDE(默认)
        :rtype: str
        """
        return self._TLSCiphers

    @TLSCiphers.setter
    def TLSCiphers(self, TLSCiphers):
        self._TLSCiphers = TLSCiphers


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._TLSSupportVersion = params.get("TLSSupportVersion")
        self._TLSCiphers = params.get("TLSCiphers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetTlsVersionResponse(AbstractModel):
    """SetTlsVersion返回参数结构体

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


class StatisticsDataInfo(AbstractModel):
    """统计数据信息

    """

    def __init__(self):
        r"""
        :param _Time: 对应的时间点
        :type Time: int
        :param _Data: 统计数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self._Time = None
        self._Data = None

    @property
    def Time(self):
        """对应的时间点
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Data(self):
        """统计数据值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportFeature(AbstractModel):
    """加速区域支持的能力，包括支持的网络类型等等。

    """

    def __init__(self):
        r"""
        :param _NetworkType: 接入区域支持的网络类型列表，normal表示支持常规BGP，cn2表示精品BGP，triple表示三网，secure_eip表示定制安全eip。
        :type NetworkType: list of str
        """
        self._NetworkType = None

    @property
    def NetworkType(self):
        """接入区域支持的网络类型列表，normal表示支持常规BGP，cn2表示精品BGP，triple表示三网，secure_eip表示定制安全eip。
        :rtype: list of str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType


    def _deserialize(self, params):
        self._NetworkType = params.get("NetworkType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCPListener(AbstractModel):
    """TCP类型监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器端口
        :type Port: int
        :param _RealServerPort: 监听器转发源站端口，仅对版本为1.0的通道有效
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param _RealServerType: 监听器绑定源站类型
        :type RealServerType: str
        :param _Protocol: 监听器协议， TCP
        :type Protocol: str
        :param _ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _ConnectTimeout: 源站健康检查响应超时时间，单位：秒
        :type ConnectTimeout: int
        :param _DelayLoop: 源站健康检查时间间隔，单位：秒
        :type DelayLoop: int
        :param _HealthCheck: 监听器是否开启健康检查，其中：
0表示关闭；
1表示开启
        :type HealthCheck: int
        :param _BindStatus: 监听器绑定的源站状态， 其中：
0表示异常；
1表示正常。
        :type BindStatus: int
        :param _RealServerSet: 监听器绑定的源站信息
        :type RealServerSet: list of BindRealServer
        :param _CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param _ClientIPMethod: 监听器获取客户端 IP 的方式，0表示TOA, 1表示Proxy Protocol
        :type ClientIPMethod: int
        :param _HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param _SessionPersist: 是否开启会话保持选项：0关闭， 非0开启，非0值为会话保持时间
        :type SessionPersist: int
        :param _ProxyId: 监听器的通道ID，如果监听器属于通道组，则为null
        :type ProxyId: str
        :param _GroupId: 监听器的通道组ID，如果监听器属于通道，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._RealServerPort = None
        self._RealServerType = None
        self._Protocol = None
        self._ListenerStatus = None
        self._Scheduler = None
        self._ConnectTimeout = None
        self._DelayLoop = None
        self._HealthCheck = None
        self._BindStatus = None
        self._RealServerSet = None
        self._CreateTime = None
        self._ClientIPMethod = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._SessionPersist = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RealServerPort(self):
        """监听器转发源站端口，仅对版本为1.0的通道有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def RealServerType(self):
        """监听器绑定源站类型
        :rtype: str
        """
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Protocol(self):
        """监听器协议， TCP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        """监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :rtype: int
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def ConnectTimeout(self):
        """源站健康检查响应超时时间，单位：秒
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def DelayLoop(self):
        """源站健康检查时间间隔，单位：秒
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def HealthCheck(self):
        """监听器是否开启健康检查，其中：
0表示关闭；
1表示开启
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def BindStatus(self):
        """监听器绑定的源站状态， 其中：
0表示异常；
1表示正常。
        :rtype: int
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def RealServerSet(self):
        """监听器绑定的源站信息
        :rtype: list of BindRealServer
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def CreateTime(self):
        """监听器创建时间，Unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ClientIPMethod(self):
        """监听器获取客户端 IP 的方式，0表示TOA, 1表示Proxy Protocol
        :rtype: int
        """
        return self._ClientIPMethod

    @ClientIPMethod.setter
    def ClientIPMethod(self, ClientIPMethod):
        self._ClientIPMethod = ClientIPMethod

    @property
    def HealthyThreshold(self):
        """健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        """不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        """源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :rtype: int
        """
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def SessionPersist(self):
        """是否开启会话保持选项：0关闭， 非0开启，非0值为会话保持时间
        :rtype: int
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def ProxyId(self):
        """监听器的通道ID，如果监听器属于通道组，则为null
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """监听器的通道组ID，如果监听器属于通道，则为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._RealServerPort = params.get("RealServerPort")
        self._RealServerType = params.get("RealServerType")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._Scheduler = params.get("Scheduler")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._DelayLoop = params.get("DelayLoop")
        self._HealthCheck = params.get("HealthCheck")
        self._BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ClientIPMethod = params.get("ClientIPMethod")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._SessionPersist = params.get("SessionPersist")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagPair(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
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
        


class TagResourceInfo(AbstractModel):
    """标签对应资源信息

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型，其中：
Proxy表示通道，
ProxyGroup表示通道组，
RealServer表示源站
        :type ResourceType: str
        :param _ResourceId: 资源ID
        :type ResourceId: str
        """
        self._ResourceType = None
        self._ResourceId = None

    @property
    def ResourceType(self):
        """资源类型，其中：
Proxy表示通道，
ProxyGroup表示通道组，
RealServer表示源站
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UDPListener(AbstractModel):
    """UDP类型监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _Port: 监听器端口
        :type Port: int
        :param _RealServerPort: 监听器转发源站端口，仅V1版本通道或通道组监听器有效
        :type RealServerPort: int
        :param _RealServerType: 监听器绑定源站类型
        :type RealServerType: str
        :param _Protocol: 监听器协议， UDP
        :type Protocol: str
        :param _ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param _Scheduler: 监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :type Scheduler: str
        :param _BindStatus: 监听器绑定源站状态， 0表示正常，1表示IP异常，2表示域名解析异常
        :type BindStatus: int
        :param _RealServerSet: 监听器绑定的源站信息
        :type RealServerSet: list of BindRealServer
        :param _CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param _SessionPersist: 是否开启会话保持选项：0关闭， 非0开启，非0值为会话保持时间
        :type SessionPersist: int
        :param _DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param _ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param _HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param _UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        :param _FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param _HealthCheck: 源站是否开启健康检查：1开启，0关闭。
        :type HealthCheck: int
        :param _CheckType: UDP源站健康类型。PORT表示检查端口，PING表示PING。
        :type CheckType: str
        :param _CheckPort: UDP源站健康检查探测端口。
        :type CheckPort: int
        :param _ContextType: UDP源站健康检查端口探测报文类型：TEXT表示文本。仅在健康检查类型为PORT时使用。
        :type ContextType: str
        :param _SendContext: UDP源站健康检查端口探测发送报文。仅在健康检查类型为PORT时使用。
        :type SendContext: str
        :param _RecvContext: UDP源站健康检查端口探测接收报文。仅在健康检查类型为PORT时使用。
        :type RecvContext: str
        :param _ProxyId: 监听器的通道ID，如果监听器属于通道组，则为null
        :type ProxyId: str
        :param _GroupId: 监听器的通道组ID，如果监听器属于通道，则为null
        :type GroupId: str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Port = None
        self._RealServerPort = None
        self._RealServerType = None
        self._Protocol = None
        self._ListenerStatus = None
        self._Scheduler = None
        self._BindStatus = None
        self._RealServerSet = None
        self._CreateTime = None
        self._SessionPersist = None
        self._DelayLoop = None
        self._ConnectTimeout = None
        self._HealthyThreshold = None
        self._UnhealthyThreshold = None
        self._FailoverSwitch = None
        self._HealthCheck = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None
        self._ProxyId = None
        self._GroupId = None

    @property
    def ListenerId(self):
        """监听器ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Port(self):
        """监听器端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def RealServerPort(self):
        """监听器转发源站端口，仅V1版本通道或通道组监听器有效
        :rtype: int
        """
        return self._RealServerPort

    @RealServerPort.setter
    def RealServerPort(self, RealServerPort):
        self._RealServerPort = RealServerPort

    @property
    def RealServerType(self):
        """监听器绑定源站类型
        :rtype: str
        """
        return self._RealServerType

    @RealServerType.setter
    def RealServerType(self, RealServerType):
        self._RealServerType = RealServerType

    @property
    def Protocol(self):
        """监听器协议， UDP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerStatus(self):
        """监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :rtype: int
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def Scheduler(self):
        """监听器源站访问策略，其中：rr表示轮询；wrr表示加权轮询；lc表示最小连接数；lrtt表示最小时延。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def BindStatus(self):
        """监听器绑定源站状态， 0表示正常，1表示IP异常，2表示域名解析异常
        :rtype: int
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def RealServerSet(self):
        """监听器绑定的源站信息
        :rtype: list of BindRealServer
        """
        return self._RealServerSet

    @RealServerSet.setter
    def RealServerSet(self, RealServerSet):
        self._RealServerSet = RealServerSet

    @property
    def CreateTime(self):
        """监听器创建时间，Unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SessionPersist(self):
        """是否开启会话保持选项：0关闭， 非0开启，非0值为会话保持时间
        :rtype: int
        """
        return self._SessionPersist

    @SessionPersist.setter
    def SessionPersist(self, SessionPersist):
        self._SessionPersist = SessionPersist

    @property
    def DelayLoop(self):
        """源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :rtype: int
        """
        return self._DelayLoop

    @DelayLoop.setter
    def DelayLoop(self, DelayLoop):
        self._DelayLoop = DelayLoop

    @property
    def ConnectTimeout(self):
        """源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthyThreshold(self):
        """健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def UnhealthyThreshold(self):
        """不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def FailoverSwitch(self):
        """源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :rtype: int
        """
        return self._FailoverSwitch

    @FailoverSwitch.setter
    def FailoverSwitch(self, FailoverSwitch):
        self._FailoverSwitch = FailoverSwitch

    @property
    def HealthCheck(self):
        """源站是否开启健康检查：1开启，0关闭。
        :rtype: int
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def CheckType(self):
        """UDP源站健康类型。PORT表示检查端口，PING表示PING。
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        """UDP源站健康检查探测端口。
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        """UDP源站健康检查端口探测报文类型：TEXT表示文本。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        """UDP源站健康检查端口探测发送报文。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        """UDP源站健康检查端口探测接收报文。仅在健康检查类型为PORT时使用。
        :rtype: str
        """
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext

    @property
    def ProxyId(self):
        """监听器的通道ID，如果监听器属于通道组，则为null
        :rtype: str
        """
        return self._ProxyId

    @ProxyId.setter
    def ProxyId(self, ProxyId):
        self._ProxyId = ProxyId

    @property
    def GroupId(self):
        """监听器的通道组ID，如果监听器属于通道，则为null
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Port = params.get("Port")
        self._RealServerPort = params.get("RealServerPort")
        self._RealServerType = params.get("RealServerType")
        self._Protocol = params.get("Protocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._Scheduler = params.get("Scheduler")
        self._BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self._RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self._RealServerSet.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._SessionPersist = params.get("SessionPersist")
        self._DelayLoop = params.get("DelayLoop")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._FailoverSwitch = params.get("FailoverSwitch")
        self._HealthCheck = params.get("HealthCheck")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        self._ProxyId = params.get("ProxyId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        