# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class AcceleratorAreas(AbstractModel):
    r"""加速地域信息

    """

    def __init__(self):
        r"""
        :param _AccelerateRegion: 加速地域。
        :type AccelerateRegion: str
        :param _Bandwidth: 带宽。
        :type Bandwidth: int
        :param _IspType: 支持'BGP', '三网', '精品'，默认BGP。
        :type IspType: str
        :param _IpVersion: 仅支持IPv4，默认是IPv4。
        :type IpVersion: str
        :param _AcceleratorAreaId: 加速地域ID。
        :type AcceleratorAreaId: str
        :param _IpAddress: IP。
        :type IpAddress: list of str
        :param _IpAddressInfoSet: IP信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpAddressInfoSet: list of IpAddressInfoSet
        """
        self._AccelerateRegion = None
        self._Bandwidth = None
        self._IspType = None
        self._IpVersion = None
        self._AcceleratorAreaId = None
        self._IpAddress = None
        self._IpAddressInfoSet = None

    @property
    def AccelerateRegion(self):
        r"""加速地域。
        :rtype: str
        """
        return self._AccelerateRegion

    @AccelerateRegion.setter
    def AccelerateRegion(self, AccelerateRegion):
        self._AccelerateRegion = AccelerateRegion

    @property
    def Bandwidth(self):
        r"""带宽。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IspType(self):
        r"""支持'BGP', '三网', '精品'，默认BGP。
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def IpVersion(self):
        r"""仅支持IPv4，默认是IPv4。
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def AcceleratorAreaId(self):
        r"""加速地域ID。
        :rtype: str
        """
        return self._AcceleratorAreaId

    @AcceleratorAreaId.setter
    def AcceleratorAreaId(self, AcceleratorAreaId):
        self._AcceleratorAreaId = AcceleratorAreaId

    @property
    def IpAddress(self):
        r"""IP。
        :rtype: list of str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def IpAddressInfoSet(self):
        r"""IP信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IpAddressInfoSet
        """
        return self._IpAddressInfoSet

    @IpAddressInfoSet.setter
    def IpAddressInfoSet(self, IpAddressInfoSet):
        self._IpAddressInfoSet = IpAddressInfoSet


    def _deserialize(self, params):
        self._AccelerateRegion = params.get("AccelerateRegion")
        self._Bandwidth = params.get("Bandwidth")
        self._IspType = params.get("IspType")
        self._IpVersion = params.get("IpVersion")
        self._AcceleratorAreaId = params.get("AcceleratorAreaId")
        self._IpAddress = params.get("IpAddress")
        if params.get("IpAddressInfoSet") is not None:
            self._IpAddressInfoSet = []
            for item in params.get("IpAddressInfoSet"):
                obj = IpAddressInfoSet()
                obj._deserialize(item)
                self._IpAddressInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceleratorRegionSet(AbstractModel):
    r"""可加速地域信息

    """

    def __init__(self):
        r"""
        :param _Name: <p>地域中文名称。</p>
        :type Name: str
        :param _IsAvailable: <p>是否可用；0：不可用，1:可用。</p>
        :type IsAvailable: int
        :param _Region: <p>地域信息。</p>
        :type Region: str
        :param _AreaName: <p>地区名称。</p>
        :type AreaName: str
        :param _IsChinaMainland: <p>是否中国地域。</p>
        :type IsChinaMainland: int
        :param _SupportIspType: <p>支持IspType类型。</p>
        :type SupportIspType: list of str
        :param _IsTencentRegion: <p>是否腾讯地域。</p>
        :type IsTencentRegion: int
        """
        self._Name = None
        self._IsAvailable = None
        self._Region = None
        self._AreaName = None
        self._IsChinaMainland = None
        self._SupportIspType = None
        self._IsTencentRegion = None

    @property
    def Name(self):
        r"""<p>地域中文名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsAvailable(self):
        r"""<p>是否可用；0：不可用，1:可用。</p>
        :rtype: int
        """
        return self._IsAvailable

    @IsAvailable.setter
    def IsAvailable(self, IsAvailable):
        self._IsAvailable = IsAvailable

    @property
    def Region(self):
        r"""<p>地域信息。</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AreaName(self):
        r"""<p>地区名称。</p>
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName

    @property
    def IsChinaMainland(self):
        r"""<p>是否中国地域。</p>
        :rtype: int
        """
        return self._IsChinaMainland

    @IsChinaMainland.setter
    def IsChinaMainland(self, IsChinaMainland):
        self._IsChinaMainland = IsChinaMainland

    @property
    def SupportIspType(self):
        r"""<p>支持IspType类型。</p>
        :rtype: list of str
        """
        return self._SupportIspType

    @SupportIspType.setter
    def SupportIspType(self, SupportIspType):
        self._SupportIspType = SupportIspType

    @property
    def IsTencentRegion(self):
        r"""<p>是否腾讯地域。</p>
        :rtype: int
        """
        return self._IsTencentRegion

    @IsTencentRegion.setter
    def IsTencentRegion(self, IsTencentRegion):
        self._IsTencentRegion = IsTencentRegion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IsAvailable = params.get("IsAvailable")
        self._Region = params.get("Region")
        self._AreaName = params.get("AreaName")
        self._IsChinaMainland = params.get("IsChinaMainland")
        self._SupportIspType = params.get("SupportIspType")
        self._IsTencentRegion = params.get("IsTencentRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerateAreasRequest(AbstractModel):
    r"""CreateAccelerateAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _AcceleratorAreas: 加速地域信息。
        :type AcceleratorAreas: list of AcceleratorAreas
        """
        self._GlobalAcceleratorId = None
        self._AcceleratorAreas = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AcceleratorAreas(self):
        r"""加速地域信息。
        :rtype: list of AcceleratorAreas
        """
        return self._AcceleratorAreas

    @AcceleratorAreas.setter
    def AcceleratorAreas(self, AcceleratorAreas):
        self._AcceleratorAreas = AcceleratorAreas


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        if params.get("AcceleratorAreas") is not None:
            self._AcceleratorAreas = []
            for item in params.get("AcceleratorAreas"):
                obj = AcceleratorAreas()
                obj._deserialize(item)
                self._AcceleratorAreas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccelerateAreasResponse(AbstractModel):
    r"""CreateAccelerateAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateEndpointGroupRequest(AbstractModel):
    r"""CreateEndpointGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _EndpointGroupType: 终端节点组类型。支持VIRTUAL，DEFAULT。
        :type EndpointGroupType: str
        :param _EndpointGroupConfiguration: 终端节点组配置。
        :type EndpointGroupConfiguration: :class:`tencentcloud.ga2.v20250115.models.EndpointGroupConfiguration`
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupType = None
        self._EndpointGroupConfiguration = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupType(self):
        r"""终端节点组类型。支持VIRTUAL，DEFAULT。
        :rtype: str
        """
        return self._EndpointGroupType

    @EndpointGroupType.setter
    def EndpointGroupType(self, EndpointGroupType):
        self._EndpointGroupType = EndpointGroupType

    @property
    def EndpointGroupConfiguration(self):
        r"""终端节点组配置。
        :rtype: :class:`tencentcloud.ga2.v20250115.models.EndpointGroupConfiguration`
        """
        return self._EndpointGroupConfiguration

    @EndpointGroupConfiguration.setter
    def EndpointGroupConfiguration(self, EndpointGroupConfiguration):
        self._EndpointGroupConfiguration = EndpointGroupConfiguration


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupType = params.get("EndpointGroupType")
        if params.get("EndpointGroupConfiguration") is not None:
            self._EndpointGroupConfiguration = EndpointGroupConfiguration()
            self._EndpointGroupConfiguration._deserialize(params.get("EndpointGroupConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEndpointGroupResponse(AbstractModel):
    r"""CreateEndpointGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _EndpointGroupId: 终端节点组实例ID。
        :type EndpointGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._EndpointGroupId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def EndpointGroupId(self):
        r"""终端节点组实例ID。
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        self._RequestId = params.get("RequestId")


class CreateForwardingPolicyRequest(AbstractModel):
    r"""CreateForwardingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _Host: 域名。
        :type Host: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Host = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Host(self):
        r"""域名。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardingPolicyResponse(AbstractModel):
    r"""CreateForwardingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _ForwardingPolicyId: 七层转发策略ID。
        :type ForwardingPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ForwardingPolicyId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ForwardingPolicyId(self):
        r"""七层转发策略ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._RequestId = params.get("RequestId")


class CreateForwardingRuleRequest(AbstractModel):
    r"""CreateForwardingRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>监听器ID。</p>
        :type ListenerId: str
        :param _ForwardingPolicyId: <p>策略ID。</p>
        :type ForwardingPolicyId: str
        :param _RuleConditions: <p>七层转发规则条件信息。</p>
        :type RuleConditions: list of RuleCondition
        :param _RuleActions: <p>七层转发规则行为信息。</p>
        :type RuleActions: list of RuleAction
        :param _OriginHeaders: <p>回源Header信息。</p>
        :type OriginHeaders: list of OriginHeader
        :param _EnableOriginSni: <p>是否开启回源sni。</p>
        :type EnableOriginSni: bool
        :param _OriginSni: <p>回源sni。</p>
        :type OriginSni: str
        :param _OriginHost: <p>回源host。</p>
        :type OriginHost: str
        :param _ResponseHeaders: <p>源站响应头</p>
        :type ResponseHeaders: list of ResponseHeaders
        :param _HideResponseHeaders: <p>删除源站响应头</p>
        :type HideResponseHeaders: list of HideResponseHeaders
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._RuleConditions = None
        self._RuleActions = None
        self._OriginHeaders = None
        self._EnableOriginSni = None
        self._OriginSni = None
        self._OriginHost = None
        self._ResponseHeaders = None
        self._HideResponseHeaders = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>监听器ID。</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""<p>策略ID。</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def RuleConditions(self):
        r"""<p>七层转发规则条件信息。</p>
        :rtype: list of RuleCondition
        """
        return self._RuleConditions

    @RuleConditions.setter
    def RuleConditions(self, RuleConditions):
        self._RuleConditions = RuleConditions

    @property
    def RuleActions(self):
        r"""<p>七层转发规则行为信息。</p>
        :rtype: list of RuleAction
        """
        return self._RuleActions

    @RuleActions.setter
    def RuleActions(self, RuleActions):
        self._RuleActions = RuleActions

    @property
    def OriginHeaders(self):
        r"""<p>回源Header信息。</p>
        :rtype: list of OriginHeader
        """
        return self._OriginHeaders

    @OriginHeaders.setter
    def OriginHeaders(self, OriginHeaders):
        self._OriginHeaders = OriginHeaders

    @property
    def EnableOriginSni(self):
        r"""<p>是否开启回源sni。</p>
        :rtype: bool
        """
        return self._EnableOriginSni

    @EnableOriginSni.setter
    def EnableOriginSni(self, EnableOriginSni):
        self._EnableOriginSni = EnableOriginSni

    @property
    def OriginSni(self):
        r"""<p>回源sni。</p>
        :rtype: str
        """
        return self._OriginSni

    @OriginSni.setter
    def OriginSni(self, OriginSni):
        self._OriginSni = OriginSni

    @property
    def OriginHost(self):
        r"""<p>回源host。</p>
        :rtype: str
        """
        return self._OriginHost

    @OriginHost.setter
    def OriginHost(self, OriginHost):
        self._OriginHost = OriginHost

    @property
    def ResponseHeaders(self):
        r"""<p>源站响应头</p>
        :rtype: list of ResponseHeaders
        """
        return self._ResponseHeaders

    @ResponseHeaders.setter
    def ResponseHeaders(self, ResponseHeaders):
        self._ResponseHeaders = ResponseHeaders

    @property
    def HideResponseHeaders(self):
        r"""<p>删除源站响应头</p>
        :rtype: list of HideResponseHeaders
        """
        return self._HideResponseHeaders

    @HideResponseHeaders.setter
    def HideResponseHeaders(self, HideResponseHeaders):
        self._HideResponseHeaders = HideResponseHeaders


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        if params.get("RuleConditions") is not None:
            self._RuleConditions = []
            for item in params.get("RuleConditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleConditions.append(obj)
        if params.get("RuleActions") is not None:
            self._RuleActions = []
            for item in params.get("RuleActions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._RuleActions.append(obj)
        if params.get("OriginHeaders") is not None:
            self._OriginHeaders = []
            for item in params.get("OriginHeaders"):
                obj = OriginHeader()
                obj._deserialize(item)
                self._OriginHeaders.append(obj)
        self._EnableOriginSni = params.get("EnableOriginSni")
        self._OriginSni = params.get("OriginSni")
        self._OriginHost = params.get("OriginHost")
        if params.get("ResponseHeaders") is not None:
            self._ResponseHeaders = []
            for item in params.get("ResponseHeaders"):
                obj = ResponseHeaders()
                obj._deserialize(item)
                self._ResponseHeaders.append(obj)
        if params.get("HideResponseHeaders") is not None:
            self._HideResponseHeaders = []
            for item in params.get("HideResponseHeaders"):
                obj = HideResponseHeaders()
                obj._deserialize(item)
                self._HideResponseHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateForwardingRuleResponse(AbstractModel):
    r"""CreateForwardingRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>异步任务ID。</p>
        :type TaskId: str
        :param _ForwardingRuleId: <p>七层转发规则ID。</p>
        :type ForwardingRuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ForwardingRuleId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>异步任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ForwardingRuleId(self):
        r"""<p>七层转发规则ID。</p>
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        self._RequestId = params.get("RequestId")


class CreateGlobalAcceleratorRequest(AbstractModel):
    r"""CreateGlobalAccelerator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>名称，最大长度不能超过60个字节。</p>
        :type Name: str
        :param _InstanceChargeType: <p>计费模式，PREPAID：表示预付费，即包年包月，POSTPAID：表示后付费，即按量计费。默认：POSTPAID。当前仅支持后付费。</p>
        :type InstanceChargeType: str
        :param _Description: <p>描述信息，最大长度不能超过100个字节。</p>
        :type Description: str
        :param _CrossBorderType: <p>跨境类型；HighQuality：精品BGP-IP跨境；Unicom：联通专线跨境。</p>
        :type CrossBorderType: str
        :param _CrossBorderPromiseFlag: <p>此Flag代表签署跨境服务承诺书。当使用跨境服务时候，此字段必传。True：代表签署。</p>
        :type CrossBorderPromiseFlag: bool
        :param _Tags: <p>标签信息</p>
        :type Tags: list of Tag
        """
        self._Name = None
        self._InstanceChargeType = None
        self._Description = None
        self._CrossBorderType = None
        self._CrossBorderPromiseFlag = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>名称，最大长度不能超过60个字节。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def InstanceChargeType(self):
        r"""<p>计费模式，PREPAID：表示预付费，即包年包月，POSTPAID：表示后付费，即按量计费。默认：POSTPAID。当前仅支持后付费。</p>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Description(self):
        r"""<p>描述信息，最大长度不能超过100个字节。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CrossBorderType(self):
        r"""<p>跨境类型；HighQuality：精品BGP-IP跨境；Unicom：联通专线跨境。</p>
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def CrossBorderPromiseFlag(self):
        r"""<p>此Flag代表签署跨境服务承诺书。当使用跨境服务时候，此字段必传。True：代表签署。</p>
        :rtype: bool
        """
        return self._CrossBorderPromiseFlag

    @CrossBorderPromiseFlag.setter
    def CrossBorderPromiseFlag(self, CrossBorderPromiseFlag):
        self._CrossBorderPromiseFlag = CrossBorderPromiseFlag

    @property
    def Tags(self):
        r"""<p>标签信息</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Description = params.get("Description")
        self._CrossBorderType = params.get("CrossBorderType")
        self._CrossBorderPromiseFlag = params.get("CrossBorderPromiseFlag")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlobalAcceleratorResponse(AbstractModel):
    r"""CreateGlobalAccelerator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID。</p>
        :type TaskId: str
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._GlobalAcceleratorId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    r"""CreateListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _Name: <p>名称，最大长度不能超过60个字节。</p>
        :type Name: str
        :param _PortRanges: <p>端口范围。</p>
        :type PortRanges: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        :param _Description: <p>描述信息，最大长度不能超过100个字节。</p>
        :type Description: str
        :param _ListenerType: <p>监听类型，默认为智能路由。</p>
        :type ListenerType: str
        :param _Protocol: <p>协议，默认为TCP。</p>
        :type Protocol: str
        :param _IdleTimeout: <p>连接空闲等待时间。</p>
        :type IdleTimeout: int
        :param _GetRealIpType: <p>四层获取源IP方式，支持&#39;TOA&#39;, &#39;ProxyProtocol&#39;。</p>
        :type GetRealIpType: str
        :param _ClientAffinity: <p>是否开启会话保持。</p>
        :type ClientAffinity: str
        :param _RequestTimeout: <p>请求超时时间。</p>
        :type RequestTimeout: int
        :param _XForwardedForRealIp: <p>是否打开七层获取源IP方式。</p>
        :type XForwardedForRealIp: bool
        :param _CertificationType: <p>解析方式。UNIDIRECTIONAL：双向。MUTUAL：单向。</p>
        :type CertificationType: str
        :param _CipherPolicyId: <p>加密算法套件。</p>
        :type CipherPolicyId: str
        :param _ServerCertificates: <p>服务器证书。</p>
        :type ServerCertificates: list of str
        :param _ClientCaCertificates: <p>客户端证书。</p>
        :type ClientCaCertificates: list of str
        :param _HttpVersion: <p>HTTPS监听器支持选择版本</p><p>枚举值：</p><ul><li>HTTP/1.1： HTTP/1.1</li><li>HTTP/2： HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._GlobalAcceleratorId = None
        self._Name = None
        self._PortRanges = None
        self._Description = None
        self._ListenerType = None
        self._Protocol = None
        self._IdleTimeout = None
        self._GetRealIpType = None
        self._ClientAffinity = None
        self._RequestTimeout = None
        self._XForwardedForRealIp = None
        self._CertificationType = None
        self._CipherPolicyId = None
        self._ServerCertificates = None
        self._ClientCaCertificates = None
        self._HttpVersion = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Name(self):
        r"""<p>名称，最大长度不能超过60个字节。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PortRanges(self):
        r"""<p>端口范围。</p>
        :rtype: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        """
        return self._PortRanges

    @PortRanges.setter
    def PortRanges(self, PortRanges):
        self._PortRanges = PortRanges

    @property
    def Description(self):
        r"""<p>描述信息，最大长度不能超过100个字节。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ListenerType(self):
        r"""<p>监听类型，默认为智能路由。</p>
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def Protocol(self):
        r"""<p>协议，默认为TCP。</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IdleTimeout(self):
        r"""<p>连接空闲等待时间。</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def GetRealIpType(self):
        r"""<p>四层获取源IP方式，支持&#39;TOA&#39;, &#39;ProxyProtocol&#39;。</p>
        :rtype: str
        """
        return self._GetRealIpType

    @GetRealIpType.setter
    def GetRealIpType(self, GetRealIpType):
        self._GetRealIpType = GetRealIpType

    @property
    def ClientAffinity(self):
        r"""<p>是否开启会话保持。</p>
        :rtype: str
        """
        return self._ClientAffinity

    @ClientAffinity.setter
    def ClientAffinity(self, ClientAffinity):
        self._ClientAffinity = ClientAffinity

    @property
    def RequestTimeout(self):
        r"""<p>请求超时时间。</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def XForwardedForRealIp(self):
        r"""<p>是否打开七层获取源IP方式。</p>
        :rtype: bool
        """
        return self._XForwardedForRealIp

    @XForwardedForRealIp.setter
    def XForwardedForRealIp(self, XForwardedForRealIp):
        self._XForwardedForRealIp = XForwardedForRealIp

    @property
    def CertificationType(self):
        r"""<p>解析方式。UNIDIRECTIONAL：双向。MUTUAL：单向。</p>
        :rtype: str
        """
        return self._CertificationType

    @CertificationType.setter
    def CertificationType(self, CertificationType):
        self._CertificationType = CertificationType

    @property
    def CipherPolicyId(self):
        r"""<p>加密算法套件。</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def ServerCertificates(self):
        r"""<p>服务器证书。</p>
        :rtype: list of str
        """
        return self._ServerCertificates

    @ServerCertificates.setter
    def ServerCertificates(self, ServerCertificates):
        self._ServerCertificates = ServerCertificates

    @property
    def ClientCaCertificates(self):
        r"""<p>客户端证书。</p>
        :rtype: list of str
        """
        return self._ClientCaCertificates

    @ClientCaCertificates.setter
    def ClientCaCertificates(self, ClientCaCertificates):
        self._ClientCaCertificates = ClientCaCertificates

    @property
    def HttpVersion(self):
        r"""<p>HTTPS监听器支持选择版本</p><p>枚举值：</p><ul><li>HTTP/1.1： HTTP/1.1</li><li>HTTP/2： HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Name = params.get("Name")
        if params.get("PortRanges") is not None:
            self._PortRanges = PortRanges()
            self._PortRanges._deserialize(params.get("PortRanges"))
        self._Description = params.get("Description")
        self._ListenerType = params.get("ListenerType")
        self._Protocol = params.get("Protocol")
        self._IdleTimeout = params.get("IdleTimeout")
        self._GetRealIpType = params.get("GetRealIpType")
        self._ClientAffinity = params.get("ClientAffinity")
        self._RequestTimeout = params.get("RequestTimeout")
        self._XForwardedForRealIp = params.get("XForwardedForRealIp")
        self._CertificationType = params.get("CertificationType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._ServerCertificates = params.get("ServerCertificates")
        self._ClientCaCertificates = params.get("ClientCaCertificates")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    r"""CreateListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID。</p>
        :type TaskId: str
        :param _ListenerId: <p>监听器ID。</p>
        :type ListenerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._ListenerId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ListenerId(self):
        r"""<p>监听器ID。</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class DeleteAccelerateAreasRequest(AbstractModel):
    r"""DeleteAccelerateAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _AcceleratorAreaIds: 加速地域ID。
        :type AcceleratorAreaIds: list of str
        """
        self._GlobalAcceleratorId = None
        self._AcceleratorAreaIds = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AcceleratorAreaIds(self):
        r"""加速地域ID。
        :rtype: list of str
        """
        return self._AcceleratorAreaIds

    @AcceleratorAreaIds.setter
    def AcceleratorAreaIds(self, AcceleratorAreaIds):
        self._AcceleratorAreaIds = AcceleratorAreaIds


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._AcceleratorAreaIds = params.get("AcceleratorAreaIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccelerateAreasResponse(AbstractModel):
    r"""DeleteAccelerateAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteEndpointGroupsRequest(AbstractModel):
    r"""DeleteEndpointGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _EndpointGroupIds: 终端节点组ID。
        :type EndpointGroupIds: list of str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupIds = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupIds(self):
        r"""终端节点组ID。
        :rtype: list of str
        """
        return self._EndpointGroupIds

    @EndpointGroupIds.setter
    def EndpointGroupIds(self, EndpointGroupIds):
        self._EndpointGroupIds = EndpointGroupIds


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupIds = params.get("EndpointGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndpointGroupsResponse(AbstractModel):
    r"""DeleteEndpointGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteForwardingPolicyRequest(AbstractModel):
    r"""DeleteForwardingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ForwardingPolicyId: 策略ID。
        :type ForwardingPolicyId: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""策略ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardingPolicyResponse(AbstractModel):
    r"""DeleteForwardingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteForwardingRuleRequest(AbstractModel):
    r"""DeleteForwardingRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ForwardingPolicyId: 策略ID。
        :type ForwardingPolicyId: str
        :param _ForwardingRuleId: 七层转发规则ID。
        :type ForwardingRuleId: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._ForwardingRuleId = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""策略ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def ForwardingRuleId(self):
        r"""七层转发规则ID。
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteForwardingRuleResponse(AbstractModel):
    r"""DeleteForwardingRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteGlobalAcceleratorRequest(AbstractModel):
    r"""DeleteGlobalAccelerator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        """
        self._GlobalAcceleratorId = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlobalAcceleratorResponse(AbstractModel):
    r"""DeleteGlobalAccelerator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    r"""DeleteListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    r"""DeleteListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DescribeAccelerateAreasRequest(AbstractModel):
    r"""DescribeAccelerateAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _Offset: 偏移量。
        :type Offset: int
        :param _Limit: 符合条件实例数量。
        :type Limit: int
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""符合条件实例数量。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccelerateAreasResponse(AbstractModel):
    r"""DescribeAccelerateAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccelerateAreaSet: 加速地域信息。
        :type AccelerateAreaSet: list of AcceleratorAreas
        :param _TotalCount: 实例个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccelerateAreaSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccelerateAreaSet(self):
        r"""加速地域信息。
        :rtype: list of AcceleratorAreas
        """
        return self._AccelerateAreaSet

    @AccelerateAreaSet.setter
    def AccelerateAreaSet(self, AccelerateAreaSet):
        self._AccelerateAreaSet = AccelerateAreaSet

    @property
    def TotalCount(self):
        r"""实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccelerateAreaSet") is not None:
            self._AccelerateAreaSet = []
            for item in params.get("AccelerateAreaSet"):
                obj = AcceleratorAreas()
                obj._deserialize(item)
                self._AccelerateAreaSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAccelerateRegionsRequest(AbstractModel):
    r"""DescribeAccelerateRegions请求参数结构体

    """


class DescribeAccelerateRegionsResponse(AbstractModel):
    r"""DescribeAccelerateRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AcceleratorRegionSet: 加速地域信息。
        :type AcceleratorRegionSet: list of AcceleratorRegionSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AcceleratorRegionSet = None
        self._RequestId = None

    @property
    def AcceleratorRegionSet(self):
        r"""加速地域信息。
        :rtype: list of AcceleratorRegionSet
        """
        return self._AcceleratorRegionSet

    @AcceleratorRegionSet.setter
    def AcceleratorRegionSet(self, AcceleratorRegionSet):
        self._AcceleratorRegionSet = AcceleratorRegionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AcceleratorRegionSet") is not None:
            self._AcceleratorRegionSet = []
            for item in params.get("AcceleratorRegionSet"):
                obj = AcceleratorRegionSet()
                obj._deserialize(item)
                self._AcceleratorRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCrossBorderSettlementRequest(AbstractModel):
    r"""DescribeCrossBorderSettlement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _AccelerateRegion: 加速地域。
        :type AccelerateRegion: str
        :param _EndpointGroupRegion: 终端节点组地域。
        :type EndpointGroupRegion: str
        :param _SettlementMonth: 账单年月时间。
        :type SettlementMonth: int
        """
        self._GlobalAcceleratorId = None
        self._AccelerateRegion = None
        self._EndpointGroupRegion = None
        self._SettlementMonth = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AccelerateRegion(self):
        r"""加速地域。
        :rtype: str
        """
        return self._AccelerateRegion

    @AccelerateRegion.setter
    def AccelerateRegion(self, AccelerateRegion):
        self._AccelerateRegion = AccelerateRegion

    @property
    def EndpointGroupRegion(self):
        r"""终端节点组地域。
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def SettlementMonth(self):
        r"""账单年月时间。
        :rtype: int
        """
        return self._SettlementMonth

    @SettlementMonth.setter
    def SettlementMonth(self, SettlementMonth):
        self._SettlementMonth = SettlementMonth


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._AccelerateRegion = params.get("AccelerateRegion")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        self._SettlementMonth = params.get("SettlementMonth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBorderSettlementResponse(AbstractModel):
    r"""DescribeCrossBorderSettlement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Traffic: 流量用量，单位是GB；精度为保留小数点6位。
        :type Traffic: float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Traffic = None
        self._RequestId = None

    @property
    def Traffic(self):
        r"""流量用量，单位是GB；精度为保留小数点6位。
        :rtype: float
        """
        return self._Traffic

    @Traffic.setter
    def Traffic(self, Traffic):
        self._Traffic = Traffic

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Traffic = params.get("Traffic")
        self._RequestId = params.get("RequestId")


class DescribeEndpointGroupsRequest(AbstractModel):
    r"""DescribeEndpointGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤条件。  endpoint-group-id- String -（过滤条件）终端节点组实例ID。endpoint-group-type- String -（过滤条件）终端节点组实例类型。
        :type Filters: list of Filter
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件。  endpoint-group-id- String -（过滤条件）终端节点组实例ID。endpoint-group-type- String -（过滤条件）终端节点组实例类型。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeEndpointGroupsResponse(AbstractModel):
    r"""DescribeEndpointGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EndpointGroupConfigurationSet: 符合条件的终端节点组。
        :type EndpointGroupConfigurationSet: list of EndpointGroupConfigurationSet
        :param _TotalCount: 符合条件的实例个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EndpointGroupConfigurationSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def EndpointGroupConfigurationSet(self):
        r"""符合条件的终端节点组。
        :rtype: list of EndpointGroupConfigurationSet
        """
        return self._EndpointGroupConfigurationSet

    @EndpointGroupConfigurationSet.setter
    def EndpointGroupConfigurationSet(self, EndpointGroupConfigurationSet):
        self._EndpointGroupConfigurationSet = EndpointGroupConfigurationSet

    @property
    def TotalCount(self):
        r"""符合条件的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EndpointGroupConfigurationSet") is not None:
            self._EndpointGroupConfigurationSet = []
            for item in params.get("EndpointGroupConfigurationSet"):
                obj = EndpointGroupConfigurationSet()
                obj._deserialize(item)
                self._EndpointGroupConfigurationSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeForwardingPolicyRequest(AbstractModel):
    r"""DescribeForwardingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardingPolicyResponse(AbstractModel):
    r"""DescribeForwardingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ForwardingPolicySet: 符合条件的策略信息。
        :type ForwardingPolicySet: list of ForwardingPolicySet
        :param _TotalCount: 符合条件的实例个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ForwardingPolicySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ForwardingPolicySet(self):
        r"""符合条件的策略信息。
        :rtype: list of ForwardingPolicySet
        """
        return self._ForwardingPolicySet

    @ForwardingPolicySet.setter
    def ForwardingPolicySet(self, ForwardingPolicySet):
        self._ForwardingPolicySet = ForwardingPolicySet

    @property
    def TotalCount(self):
        r"""符合条件的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ForwardingPolicySet") is not None:
            self._ForwardingPolicySet = []
            for item in params.get("ForwardingPolicySet"):
                obj = ForwardingPolicySet()
                obj._deserialize(item)
                self._ForwardingPolicySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeForwardingRuleRequest(AbstractModel):
    r"""DescribeForwardingRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ForwardingPolicyId: 七层转发规则ID。
        :type ForwardingPolicyId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._Offset = None
        self._Limit = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""七层转发规则ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeForwardingRuleResponse(AbstractModel):
    r"""DescribeForwardingRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ForwardingRuleSet: 符合条件的规则信息。
        :type ForwardingRuleSet: list of ForwardingRuleSet
        :param _TotalCount: 符合条件的实例个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ForwardingRuleSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ForwardingRuleSet(self):
        r"""符合条件的规则信息。
        :rtype: list of ForwardingRuleSet
        """
        return self._ForwardingRuleSet

    @ForwardingRuleSet.setter
    def ForwardingRuleSet(self, ForwardingRuleSet):
        self._ForwardingRuleSet = ForwardingRuleSet

    @property
    def TotalCount(self):
        r"""符合条件的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ForwardingRuleSet") is not None:
            self._ForwardingRuleSet = []
            for item in params.get("ForwardingRuleSet"):
                obj = ForwardingRuleSet()
                obj._deserialize(item)
                self._ForwardingRuleSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeGlobalAcceleratorsRequest(AbstractModel):
    r"""DescribeGlobalAccelerators请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤条件。<li>global-accelerator-id - String -（过滤条件）全球加速实例ID。</li> <li>global-accelerator-state - String -（过滤条件）全球加速实例状态。</li>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件。<li>global-accelerator-id - String -（过滤条件）全球加速实例ID。</li> <li>global-accelerator-state - String -（过滤条件）全球加速实例状态。</li>
        :rtype: list of Filter
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
        


class DescribeGlobalAcceleratorsResponse(AbstractModel):
    r"""DescribeGlobalAccelerators返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorSet: 符合条件的全球加速实例。
        :type GlobalAcceleratorSet: list of GlobalAcceleratorSet
        :param _TotalCount: 符合条件的实例个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GlobalAcceleratorSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def GlobalAcceleratorSet(self):
        r"""符合条件的全球加速实例。
        :rtype: list of GlobalAcceleratorSet
        """
        return self._GlobalAcceleratorSet

    @GlobalAcceleratorSet.setter
    def GlobalAcceleratorSet(self, GlobalAcceleratorSet):
        self._GlobalAcceleratorSet = GlobalAcceleratorSet

    @property
    def TotalCount(self):
        r"""符合条件的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GlobalAcceleratorSet") is not None:
            self._GlobalAcceleratorSet = []
            for item in params.get("GlobalAcceleratorSet"):
                obj = GlobalAcceleratorSet()
                obj._deserialize(item)
                self._GlobalAcceleratorSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    r"""DescribeListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤条件。  listener-id- String -（过滤条件）监听器实例ID。
        :type Filters: list of Filter
        """
        self._GlobalAcceleratorId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Offset(self):
        r"""偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件。  listener-id- String -（过滤条件）监听器实例ID。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
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
        


class DescribeListenersResponse(AbstractModel):
    r"""DescribeListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerSet: 符合条件的监听器实例。
        :type ListenerSet: list of ListenerSet
        :param _TotalCount: 符合条件的实例个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ListenerSet(self):
        r"""符合条件的监听器实例。
        :rtype: list of ListenerSet
        """
        return self._ListenerSet

    @ListenerSet.setter
    def ListenerSet(self, ListenerSet):
        self._ListenerSet = ListenerSet

    @property
    def TotalCount(self):
        r"""符合条件的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ListenerSet") is not None:
            self._ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = ListenerSet()
                obj._deserialize(item)
                self._ListenerSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    r"""DescribeTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
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
        


class DescribeTaskResultResponse(AbstractModel):
    r"""DescribeTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class EndpointConfigurations(AbstractModel):
    r"""终端节点配置

    """

    def __init__(self):
        r"""
        :param _EndpointType: <p>域名类型。可选值&#39;Domain&#39;, &#39;PublicIp&#39;。</p>
        :type EndpointType: str
        :param _EndpointService: <p>域名。</p>
        :type EndpointService: str
        :param _Weight: <p>权重。</p>
        :type Weight: int
        :param _HealthCheckStatus: <p>健康检查状态；HEALTH：健康；UNHEALTH：不健康。</p>
        :type HealthCheckStatus: str
        """
        self._EndpointType = None
        self._EndpointService = None
        self._Weight = None
        self._HealthCheckStatus = None

    @property
    def EndpointType(self):
        r"""<p>域名类型。可选值&#39;Domain&#39;, &#39;PublicIp&#39;。</p>
        :rtype: str
        """
        return self._EndpointType

    @EndpointType.setter
    def EndpointType(self, EndpointType):
        self._EndpointType = EndpointType

    @property
    def EndpointService(self):
        r"""<p>域名。</p>
        :rtype: str
        """
        return self._EndpointService

    @EndpointService.setter
    def EndpointService(self, EndpointService):
        self._EndpointService = EndpointService

    @property
    def Weight(self):
        r"""<p>权重。</p>
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def HealthCheckStatus(self):
        r"""<p>健康检查状态；HEALTH：健康；UNHEALTH：不健康。</p>
        :rtype: str
        """
        return self._HealthCheckStatus

    @HealthCheckStatus.setter
    def HealthCheckStatus(self, HealthCheckStatus):
        self._HealthCheckStatus = HealthCheckStatus


    def _deserialize(self, params):
        self._EndpointType = params.get("EndpointType")
        self._EndpointService = params.get("EndpointService")
        self._Weight = params.get("Weight")
        self._HealthCheckStatus = params.get("HealthCheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointGroupConfiguration(AbstractModel):
    r"""终端节点组配置

    """

    def __init__(self):
        r"""
        :param _Name: <p>名称，最大长度不能超过60个字节。</p>
        :type Name: str
        :param _EndpointGroupRegion: <p>地域。</p>
        :type EndpointGroupRegion: str
        :param _EndpointConfigurations: <p>终端节点配置。</p>
        :type EndpointConfigurations: list of EndpointConfigurations
        :param _CheckType: <p>检查协议。支持&#39;TCP&#39;, &#39;HTTP&#39;, &#39;HTTPS&#39;, &#39;PING&#39;, &#39;CUSTOM&#39;。</p>
        :type CheckType: str
        :param _Description: <p>描述信息，最大长度不能超过100个字节。</p>
        :type Description: str
        :param _CheckPort: <p>检查端口。</p>
        :type CheckPort: str
        :param _ContextType: <p>检查内容。</p>
        :type ContextType: str
        :param _CheckSendContext: <p>检查请求。</p>
        :type CheckSendContext: str
        :param _CheckRecvContext: <p>检查返回结果。</p>
        :type CheckRecvContext: str
        :param _EnableHealthCheck: <p>是否开启健康检查。</p>
        :type EnableHealthCheck: bool
        :param _ConnectTimeout: <p>响应超时时间。</p>
        :type ConnectTimeout: int
        :param _HealthCheckInterval: <p>健康检查间隔。</p>
        :type HealthCheckInterval: int
        :param _UnhealthyThreshold: <p>不健康阀值。</p>
        :type UnhealthyThreshold: int
        :param _HealthyThreshold: <p>健康阈值。</p>
        :type HealthyThreshold: int
        :param _ForwardProtocol: <p>回源协议。</p>
        :type ForwardProtocol: str
        :param _CheckDomain: <p>检查域名。</p>
        :type CheckDomain: str
        :param _CheckPath: <p>检查URL。</p>
        :type CheckPath: str
        :param _CheckMethod: <p>请求方式。</p>
        :type CheckMethod: str
        :param _StatusMask: <p>状态检测码。</p>
        :type StatusMask: list of str
        :param _PortOverrides: <p>端口映射。</p>
        :type PortOverrides: list of PortOverride
        :param _IspType: <p>运用商类型。</p>
        :type IspType: str
        :param _CipherPolicyId: <p>HPPTS加密算法套件</p>
        :type CipherPolicyId: str
        :param _HttpVersion: <p>HTTPS回源协议支持选择[&#39;HTTP/1.1&#39;, &#39;HTTP/2&#39;]</p><p>枚举值：</p><ul><li>HTTP/1.1： 版本HTTP/1.1</li><li>HTTP/2： 版本HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._Name = None
        self._EndpointGroupRegion = None
        self._EndpointConfigurations = None
        self._CheckType = None
        self._Description = None
        self._CheckPort = None
        self._ContextType = None
        self._CheckSendContext = None
        self._CheckRecvContext = None
        self._EnableHealthCheck = None
        self._ConnectTimeout = None
        self._HealthCheckInterval = None
        self._UnhealthyThreshold = None
        self._HealthyThreshold = None
        self._ForwardProtocol = None
        self._CheckDomain = None
        self._CheckPath = None
        self._CheckMethod = None
        self._StatusMask = None
        self._PortOverrides = None
        self._IspType = None
        self._CipherPolicyId = None
        self._HttpVersion = None

    @property
    def Name(self):
        r"""<p>名称，最大长度不能超过60个字节。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EndpointGroupRegion(self):
        r"""<p>地域。</p>
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def EndpointConfigurations(self):
        r"""<p>终端节点配置。</p>
        :rtype: list of EndpointConfigurations
        """
        return self._EndpointConfigurations

    @EndpointConfigurations.setter
    def EndpointConfigurations(self, EndpointConfigurations):
        self._EndpointConfigurations = EndpointConfigurations

    @property
    def CheckType(self):
        r"""<p>检查协议。支持&#39;TCP&#39;, &#39;HTTP&#39;, &#39;HTTPS&#39;, &#39;PING&#39;, &#39;CUSTOM&#39;。</p>
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def Description(self):
        r"""<p>描述信息，最大长度不能超过100个字节。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CheckPort(self):
        r"""<p>检查端口。</p>
        :rtype: str
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        r"""<p>检查内容。</p>
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def CheckSendContext(self):
        r"""<p>检查请求。</p>
        :rtype: str
        """
        return self._CheckSendContext

    @CheckSendContext.setter
    def CheckSendContext(self, CheckSendContext):
        self._CheckSendContext = CheckSendContext

    @property
    def CheckRecvContext(self):
        r"""<p>检查返回结果。</p>
        :rtype: str
        """
        return self._CheckRecvContext

    @CheckRecvContext.setter
    def CheckRecvContext(self, CheckRecvContext):
        self._CheckRecvContext = CheckRecvContext

    @property
    def EnableHealthCheck(self):
        r"""<p>是否开启健康检查。</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def ConnectTimeout(self):
        r"""<p>响应超时时间。</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheckInterval(self):
        r"""<p>健康检查间隔。</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def UnhealthyThreshold(self):
        r"""<p>不健康阀值。</p>
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def HealthyThreshold(self):
        r"""<p>健康阈值。</p>
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def ForwardProtocol(self):
        r"""<p>回源协议。</p>
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def CheckDomain(self):
        r"""<p>检查域名。</p>
        :rtype: str
        """
        return self._CheckDomain

    @CheckDomain.setter
    def CheckDomain(self, CheckDomain):
        self._CheckDomain = CheckDomain

    @property
    def CheckPath(self):
        r"""<p>检查URL。</p>
        :rtype: str
        """
        return self._CheckPath

    @CheckPath.setter
    def CheckPath(self, CheckPath):
        self._CheckPath = CheckPath

    @property
    def CheckMethod(self):
        r"""<p>请求方式。</p>
        :rtype: str
        """
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def StatusMask(self):
        r"""<p>状态检测码。</p>
        :rtype: list of str
        """
        return self._StatusMask

    @StatusMask.setter
    def StatusMask(self, StatusMask):
        self._StatusMask = StatusMask

    @property
    def PortOverrides(self):
        r"""<p>端口映射。</p>
        :rtype: list of PortOverride
        """
        return self._PortOverrides

    @PortOverrides.setter
    def PortOverrides(self, PortOverrides):
        self._PortOverrides = PortOverrides

    @property
    def IspType(self):
        r"""<p>运用商类型。</p>
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def CipherPolicyId(self):
        r"""<p>HPPTS加密算法套件</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""<p>HTTPS回源协议支持选择[&#39;HTTP/1.1&#39;, &#39;HTTP/2&#39;]</p><p>枚举值：</p><ul><li>HTTP/1.1： 版本HTTP/1.1</li><li>HTTP/2： 版本HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        if params.get("EndpointConfigurations") is not None:
            self._EndpointConfigurations = []
            for item in params.get("EndpointConfigurations"):
                obj = EndpointConfigurations()
                obj._deserialize(item)
                self._EndpointConfigurations.append(obj)
        self._CheckType = params.get("CheckType")
        self._Description = params.get("Description")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._CheckSendContext = params.get("CheckSendContext")
        self._CheckRecvContext = params.get("CheckRecvContext")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._CheckDomain = params.get("CheckDomain")
        self._CheckPath = params.get("CheckPath")
        self._CheckMethod = params.get("CheckMethod")
        self._StatusMask = params.get("StatusMask")
        if params.get("PortOverrides") is not None:
            self._PortOverrides = []
            for item in params.get("PortOverrides"):
                obj = PortOverride()
                obj._deserialize(item)
                self._PortOverrides.append(obj)
        self._IspType = params.get("IspType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndpointGroupConfigurationSet(AbstractModel):
    r"""终端节点组信息

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>监听器实例ID。</p>
        :type ListenerId: str
        :param _EndpointGroupId: <p>终端节点组ID。</p>
        :type EndpointGroupId: str
        :param _Name: <p>名称。</p>
        :type Name: str
        :param _EndpointGroupRegion: <p>地域。</p>
        :type EndpointGroupRegion: str
        :param _Description: <p>描述。</p>
        :type Description: str
        :param _EndpointConfigurations: <p>终端节点信息。</p>
        :type EndpointConfigurations: list of EndpointConfigurations
        :param _EnableHealthCheck: <p>是否开启健康检查。</p>
        :type EnableHealthCheck: bool
        :param _ConnectTimeout: <p>响应超时时间。</p>
        :type ConnectTimeout: int
        :param _HealthCheckInterval: <p>健康检查间隔。</p>
        :type HealthCheckInterval: int
        :param _UnhealthyThreshold: <p>不健康阈值。</p>
        :type UnhealthyThreshold: int
        :param _HealthyThreshold: <p>健康阈值。</p>
        :type HealthyThreshold: int
        :param _CheckType: <p>检查协议。</p>
        :type CheckType: str
        :param _CheckPort: <p>检查端口。</p>
        :type CheckPort: int
        :param _ContextType: <p>检查内容。</p>
        :type ContextType: str
        :param _CheckSendContext: <p>检查请求。</p>
        :type CheckSendContext: str
        :param _CheckRecvContext: <p>检查返回结果。</p>
        :type CheckRecvContext: str
        :param _CheckDomain: <p>检查域名。</p>
        :type CheckDomain: str
        :param _CheckPath: <p>检查URL。</p>
        :type CheckPath: str
        :param _CheckMethod: <p>请求方式。</p>
        :type CheckMethod: str
        :param _StatusMask: <p>状态检测码。</p>
        :type StatusMask: list of str
        :param _EndpointGroupType: <p>终端节点组类型。</p>
        :type EndpointGroupType: str
        :param _ForwardProtocol: <p>回源协议。</p>
        :type ForwardProtocol: str
        :param _PortOverrides: <p>端口映射信息。</p>
        :type PortOverrides: list of PortOverride
        :param _VirtualExistForwardingRuleFlag: <p>自定义终端节点组是否绑定七层转发规则。</p>
        :type VirtualExistForwardingRuleFlag: bool
        :param _OriginPublicIps: <p>出终端节点组公网IP。</p>
        :type OriginPublicIps: list of str
        :param _IspType: <p>运营商类型；中国移动(CMCC)，中国联通(CUCC)，中国电信(CTCC)。</p>
        :type IspType: str
        :param _CipherPolicyId: <p>HPPTS加密算法套件</p>
        :type CipherPolicyId: str
        :param _HttpVersion: <p>仅HTTPS回源协议支持选择[&#39;HTTP/1.1&#39;, &#39;HTTP/2&#39;]</p><p>枚举值：</p><ul><li>HTTP/1.1： 版本HTTP/1.1</li><li>HTTP/2： 版本HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupId = None
        self._Name = None
        self._EndpointGroupRegion = None
        self._Description = None
        self._EndpointConfigurations = None
        self._EnableHealthCheck = None
        self._ConnectTimeout = None
        self._HealthCheckInterval = None
        self._UnhealthyThreshold = None
        self._HealthyThreshold = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._CheckSendContext = None
        self._CheckRecvContext = None
        self._CheckDomain = None
        self._CheckPath = None
        self._CheckMethod = None
        self._StatusMask = None
        self._EndpointGroupType = None
        self._ForwardProtocol = None
        self._PortOverrides = None
        self._VirtualExistForwardingRuleFlag = None
        self._OriginPublicIps = None
        self._IspType = None
        self._CipherPolicyId = None
        self._HttpVersion = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>监听器实例ID。</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupId(self):
        r"""<p>终端节点组ID。</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def Name(self):
        r"""<p>名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EndpointGroupRegion(self):
        r"""<p>地域。</p>
        :rtype: str
        """
        return self._EndpointGroupRegion

    @EndpointGroupRegion.setter
    def EndpointGroupRegion(self, EndpointGroupRegion):
        self._EndpointGroupRegion = EndpointGroupRegion

    @property
    def Description(self):
        r"""<p>描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EndpointConfigurations(self):
        r"""<p>终端节点信息。</p>
        :rtype: list of EndpointConfigurations
        """
        return self._EndpointConfigurations

    @EndpointConfigurations.setter
    def EndpointConfigurations(self, EndpointConfigurations):
        self._EndpointConfigurations = EndpointConfigurations

    @property
    def EnableHealthCheck(self):
        r"""<p>是否开启健康检查。</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def ConnectTimeout(self):
        r"""<p>响应超时时间。</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheckInterval(self):
        r"""<p>健康检查间隔。</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def UnhealthyThreshold(self):
        r"""<p>不健康阈值。</p>
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def HealthyThreshold(self):
        r"""<p>健康阈值。</p>
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def CheckType(self):
        r"""<p>检查协议。</p>
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        r"""<p>检查端口。</p>
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        r"""<p>检查内容。</p>
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def CheckSendContext(self):
        r"""<p>检查请求。</p>
        :rtype: str
        """
        return self._CheckSendContext

    @CheckSendContext.setter
    def CheckSendContext(self, CheckSendContext):
        self._CheckSendContext = CheckSendContext

    @property
    def CheckRecvContext(self):
        r"""<p>检查返回结果。</p>
        :rtype: str
        """
        return self._CheckRecvContext

    @CheckRecvContext.setter
    def CheckRecvContext(self, CheckRecvContext):
        self._CheckRecvContext = CheckRecvContext

    @property
    def CheckDomain(self):
        r"""<p>检查域名。</p>
        :rtype: str
        """
        return self._CheckDomain

    @CheckDomain.setter
    def CheckDomain(self, CheckDomain):
        self._CheckDomain = CheckDomain

    @property
    def CheckPath(self):
        r"""<p>检查URL。</p>
        :rtype: str
        """
        return self._CheckPath

    @CheckPath.setter
    def CheckPath(self, CheckPath):
        self._CheckPath = CheckPath

    @property
    def CheckMethod(self):
        r"""<p>请求方式。</p>
        :rtype: str
        """
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def StatusMask(self):
        r"""<p>状态检测码。</p>
        :rtype: list of str
        """
        return self._StatusMask

    @StatusMask.setter
    def StatusMask(self, StatusMask):
        self._StatusMask = StatusMask

    @property
    def EndpointGroupType(self):
        r"""<p>终端节点组类型。</p>
        :rtype: str
        """
        return self._EndpointGroupType

    @EndpointGroupType.setter
    def EndpointGroupType(self, EndpointGroupType):
        self._EndpointGroupType = EndpointGroupType

    @property
    def ForwardProtocol(self):
        r"""<p>回源协议。</p>
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def PortOverrides(self):
        r"""<p>端口映射信息。</p>
        :rtype: list of PortOverride
        """
        return self._PortOverrides

    @PortOverrides.setter
    def PortOverrides(self, PortOverrides):
        self._PortOverrides = PortOverrides

    @property
    def VirtualExistForwardingRuleFlag(self):
        r"""<p>自定义终端节点组是否绑定七层转发规则。</p>
        :rtype: bool
        """
        return self._VirtualExistForwardingRuleFlag

    @VirtualExistForwardingRuleFlag.setter
    def VirtualExistForwardingRuleFlag(self, VirtualExistForwardingRuleFlag):
        self._VirtualExistForwardingRuleFlag = VirtualExistForwardingRuleFlag

    @property
    def OriginPublicIps(self):
        r"""<p>出终端节点组公网IP。</p>
        :rtype: list of str
        """
        return self._OriginPublicIps

    @OriginPublicIps.setter
    def OriginPublicIps(self, OriginPublicIps):
        self._OriginPublicIps = OriginPublicIps

    @property
    def IspType(self):
        r"""<p>运营商类型；中国移动(CMCC)，中国联通(CUCC)，中国电信(CTCC)。</p>
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType

    @property
    def CipherPolicyId(self):
        r"""<p>HPPTS加密算法套件</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""<p>仅HTTPS回源协议支持选择[&#39;HTTP/1.1&#39;, &#39;HTTP/2&#39;]</p><p>枚举值：</p><ul><li>HTTP/1.1： 版本HTTP/1.1</li><li>HTTP/2： 版本HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        self._Name = params.get("Name")
        self._EndpointGroupRegion = params.get("EndpointGroupRegion")
        self._Description = params.get("Description")
        if params.get("EndpointConfigurations") is not None:
            self._EndpointConfigurations = []
            for item in params.get("EndpointConfigurations"):
                obj = EndpointConfigurations()
                obj._deserialize(item)
                self._EndpointConfigurations.append(obj)
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._CheckSendContext = params.get("CheckSendContext")
        self._CheckRecvContext = params.get("CheckRecvContext")
        self._CheckDomain = params.get("CheckDomain")
        self._CheckPath = params.get("CheckPath")
        self._CheckMethod = params.get("CheckMethod")
        self._StatusMask = params.get("StatusMask")
        self._EndpointGroupType = params.get("EndpointGroupType")
        self._ForwardProtocol = params.get("ForwardProtocol")
        if params.get("PortOverrides") is not None:
            self._PortOverrides = []
            for item in params.get("PortOverrides"):
                obj = PortOverride()
                obj._deserialize(item)
                self._PortOverrides.append(obj)
        self._VirtualExistForwardingRuleFlag = params.get("VirtualExistForwardingRuleFlag")
        self._OriginPublicIps = params.get("OriginPublicIps")
        self._IspType = params.get("IspType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。当值类型为布尔类型时，可直接取值为字符串"TRUE"或 "FALSE"。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。当值类型为布尔类型时，可直接取值为字符串"TRUE"或 "FALSE"。
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
        


class ForwardingPolicySet(AbstractModel):
    r"""七层转发策略信息

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ForwardingPolicyId: 策略ID。
        :type ForwardingPolicyId: str
        :param _Host: 域名。
        :type Host: str
        :param _DefaultHostFlag: 是否为默认域名。
        :type DefaultHostFlag: bool
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._Host = None
        self._DefaultHostFlag = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""策略ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def Host(self):
        r"""域名。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def DefaultHostFlag(self):
        r"""是否为默认域名。
        :rtype: bool
        """
        return self._DefaultHostFlag

    @DefaultHostFlag.setter
    def DefaultHostFlag(self, DefaultHostFlag):
        self._DefaultHostFlag = DefaultHostFlag


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._Host = params.get("Host")
        self._DefaultHostFlag = params.get("DefaultHostFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardingRuleSet(AbstractModel):
    r"""七层转发规则信息

    """

    def __init__(self):
        r"""
        :param _RuleCondition: 七层转发规则条件信息。
        :type RuleCondition: list of RuleCondition
        :param _RuleAction: 七层转发规则行为信息。
        :type RuleAction: list of RuleAction
        :param _EnableOriginSni: 是否开启回源Sni。
        :type EnableOriginSni: bool
        :param _OriginSni: 回源Sni。
        :type OriginSni: str
        :param _OriginHeaders: 回源Herder信息。
        :type OriginHeaders: list of OriginHeader
        :param _OriginHost: 回源Host。
        :type OriginHost: str
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ForwardingPolicyId: 七层转发策略ID。
        :type ForwardingPolicyId: str
        :param _ForwardingRuleId: 七层转发规则ID。
        :type ForwardingRuleId: str
        """
        self._RuleCondition = None
        self._RuleAction = None
        self._EnableOriginSni = None
        self._OriginSni = None
        self._OriginHeaders = None
        self._OriginHost = None
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._ForwardingRuleId = None

    @property
    def RuleCondition(self):
        r"""七层转发规则条件信息。
        :rtype: list of RuleCondition
        """
        return self._RuleCondition

    @RuleCondition.setter
    def RuleCondition(self, RuleCondition):
        self._RuleCondition = RuleCondition

    @property
    def RuleAction(self):
        r"""七层转发规则行为信息。
        :rtype: list of RuleAction
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def EnableOriginSni(self):
        r"""是否开启回源Sni。
        :rtype: bool
        """
        return self._EnableOriginSni

    @EnableOriginSni.setter
    def EnableOriginSni(self, EnableOriginSni):
        self._EnableOriginSni = EnableOriginSni

    @property
    def OriginSni(self):
        r"""回源Sni。
        :rtype: str
        """
        return self._OriginSni

    @OriginSni.setter
    def OriginSni(self, OriginSni):
        self._OriginSni = OriginSni

    @property
    def OriginHeaders(self):
        r"""回源Herder信息。
        :rtype: list of OriginHeader
        """
        return self._OriginHeaders

    @OriginHeaders.setter
    def OriginHeaders(self, OriginHeaders):
        self._OriginHeaders = OriginHeaders

    @property
    def OriginHost(self):
        r"""回源Host。
        :rtype: str
        """
        return self._OriginHost

    @OriginHost.setter
    def OriginHost(self, OriginHost):
        self._OriginHost = OriginHost

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""七层转发策略ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def ForwardingRuleId(self):
        r"""七层转发规则ID。
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId


    def _deserialize(self, params):
        if params.get("RuleCondition") is not None:
            self._RuleCondition = []
            for item in params.get("RuleCondition"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleCondition.append(obj)
        if params.get("RuleAction") is not None:
            self._RuleAction = []
            for item in params.get("RuleAction"):
                obj = RuleAction()
                obj._deserialize(item)
                self._RuleAction.append(obj)
        self._EnableOriginSni = params.get("EnableOriginSni")
        self._OriginSni = params.get("OriginSni")
        if params.get("OriginHeaders") is not None:
            self._OriginHeaders = []
            for item in params.get("OriginHeaders"):
                obj = OriginHeader()
                obj._deserialize(item)
                self._OriginHeaders.append(obj)
        self._OriginHost = params.get("OriginHost")
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlobalAcceleratorSet(AbstractModel):
    r"""全球加速实例信息

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _Name: <p>全球加速实例名称。</p>
        :type Name: str
        :param _Description: <p>全球加速实例描述。</p>
        :type Description: str
        :param _CreateTime: <p>全球加速实例创建时间。</p>
        :type CreateTime: str
        :param _State: <p>全球加速实例状态。</p>
        :type State: str
        :param _InstanceChargeType: <p>全球加速实例付费类型。</p>
        :type InstanceChargeType: str
        :param _DdosId: <p>全球加速实例DdosId。</p>
        :type DdosId: str
        :param _ListenerCounts: <p>所属加速实例监听器个数。</p>
        :type ListenerCounts: int
        :param _AcceleratorAreaCounts: <p>所属加速实例加速地域个数。</p>
        :type AcceleratorAreaCounts: int
        :param _Status: <p>全球加速实例状态。</p>
        :type Status: str
        :param _Cname: <p>域名。</p>
        :type Cname: str
        :param _CrossBorderType: <p>跨境类型；HighQuality（精品跨境）、Unicom（联通跨境）、NotAvailable（未开通）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossBorderType: str
        :param _TagSet: <p>标签信息。</p>
        :type TagSet: list of Tag
        """
        self._GlobalAcceleratorId = None
        self._Name = None
        self._Description = None
        self._CreateTime = None
        self._State = None
        self._InstanceChargeType = None
        self._DdosId = None
        self._ListenerCounts = None
        self._AcceleratorAreaCounts = None
        self._Status = None
        self._Cname = None
        self._CrossBorderType = None
        self._TagSet = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Name(self):
        r"""<p>全球加速实例名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>全球加速实例描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""<p>全球加速实例创建时间。</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def State(self):
        r"""<p>全球加速实例状态。</p>
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def InstanceChargeType(self):
        r"""<p>全球加速实例付费类型。</p>
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def DdosId(self):
        r"""<p>全球加速实例DdosId。</p>
        :rtype: str
        """
        return self._DdosId

    @DdosId.setter
    def DdosId(self, DdosId):
        self._DdosId = DdosId

    @property
    def ListenerCounts(self):
        r"""<p>所属加速实例监听器个数。</p>
        :rtype: int
        """
        return self._ListenerCounts

    @ListenerCounts.setter
    def ListenerCounts(self, ListenerCounts):
        self._ListenerCounts = ListenerCounts

    @property
    def AcceleratorAreaCounts(self):
        r"""<p>所属加速实例加速地域个数。</p>
        :rtype: int
        """
        return self._AcceleratorAreaCounts

    @AcceleratorAreaCounts.setter
    def AcceleratorAreaCounts(self, AcceleratorAreaCounts):
        self._AcceleratorAreaCounts = AcceleratorAreaCounts

    @property
    def Status(self):
        r"""<p>全球加速实例状态。</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Cname(self):
        r"""<p>域名。</p>
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def CrossBorderType(self):
        r"""<p>跨境类型；HighQuality（精品跨境）、Unicom（联通跨境）、NotAvailable（未开通）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def TagSet(self):
        r"""<p>标签信息。</p>
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._State = params.get("State")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._DdosId = params.get("DdosId")
        self._ListenerCounts = params.get("ListenerCounts")
        self._AcceleratorAreaCounts = params.get("AcceleratorAreaCounts")
        self._Status = params.get("Status")
        self._Cname = params.get("Cname")
        self._CrossBorderType = params.get("CrossBorderType")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HideResponseHeaders(AbstractModel):
    r"""隐藏Header

    """

    def __init__(self):
        r"""
        :param _Key: <p>key</p>
        :type Key: str
        :param _Value: <p>value</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>key</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>value</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpAddressInfoSet(AbstractModel):
    r"""加速地域公网IP信息

    """

    def __init__(self):
        r"""
        :param _IpAddress: IP地址。
        :type IpAddress: str
        :param _IspType: IP类型。
        :type IspType: str
        """
        self._IpAddress = None
        self._IspType = None

    @property
    def IpAddress(self):
        r"""IP地址。
        :rtype: str
        """
        return self._IpAddress

    @IpAddress.setter
    def IpAddress(self, IpAddress):
        self._IpAddress = IpAddress

    @property
    def IspType(self):
        r"""IP类型。
        :rtype: str
        """
        return self._IspType

    @IspType.setter
    def IspType(self, IspType):
        self._IspType = IspType


    def _deserialize(self, params):
        self._IpAddress = params.get("IpAddress")
        self._IspType = params.get("IspType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerSet(AbstractModel):
    r"""监听器信息

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _Name: 监听器名称。
        :type Name: str
        :param _Description: 监听器描述。
        :type Description: str
        :param _Protocol: 协议。
        :type Protocol: str
        :param _PortRanges: 端口范围。
        :type PortRanges: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        :param _XForwardedForRealIp: 是否打开七层获取源IP方式。
        :type XForwardedForRealIp: bool
        :param _ClientAffinity: 开启会话保持。
        :type ClientAffinity: str
        :param _ClientAffinityTime: 会话保持时间。
        :type ClientAffinityTime: int
        :param _CertificationType: SSL解析方式。
        :type CertificationType: str
        :param _ServerCertificates: 服务器证书。
        :type ServerCertificates: list of str
        :param _ClientCaCertificates: 客户端证书。
        :type ClientCaCertificates: list of str
        :param _CipherPolicyId: TLS密码套件包。
        :type CipherPolicyId: str
        :param _HttpVersion: HTTP版本。
        :type HttpVersion: str
        :param _RequestTimeout: 请求超时时间。
        :type RequestTimeout: int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ListenerType: 监听路由类型。
        :type ListenerType: str
        :param _Status: 监听器状态。
        :type Status: str
        :param _EndpointGroupCounts: 所属监听器终端节点组个数。
        :type EndpointGroupCounts: int
        :param _GetRealIpType: 四层获取源IP方式。
        :type GetRealIpType: str
        :param _IdleTimeout: 连接超时时间。
        :type IdleTimeout: int
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Name = None
        self._Description = None
        self._Protocol = None
        self._PortRanges = None
        self._XForwardedForRealIp = None
        self._ClientAffinity = None
        self._ClientAffinityTime = None
        self._CertificationType = None
        self._ServerCertificates = None
        self._ClientCaCertificates = None
        self._CipherPolicyId = None
        self._HttpVersion = None
        self._RequestTimeout = None
        self._CreateTime = None
        self._ListenerType = None
        self._Status = None
        self._EndpointGroupCounts = None
        self._GetRealIpType = None
        self._IdleTimeout = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Name(self):
        r"""监听器名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""监听器描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Protocol(self):
        r"""协议。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PortRanges(self):
        r"""端口范围。
        :rtype: :class:`tencentcloud.ga2.v20250115.models.PortRanges`
        """
        return self._PortRanges

    @PortRanges.setter
    def PortRanges(self, PortRanges):
        self._PortRanges = PortRanges

    @property
    def XForwardedForRealIp(self):
        r"""是否打开七层获取源IP方式。
        :rtype: bool
        """
        return self._XForwardedForRealIp

    @XForwardedForRealIp.setter
    def XForwardedForRealIp(self, XForwardedForRealIp):
        self._XForwardedForRealIp = XForwardedForRealIp

    @property
    def ClientAffinity(self):
        r"""开启会话保持。
        :rtype: str
        """
        return self._ClientAffinity

    @ClientAffinity.setter
    def ClientAffinity(self, ClientAffinity):
        self._ClientAffinity = ClientAffinity

    @property
    def ClientAffinityTime(self):
        r"""会话保持时间。
        :rtype: int
        """
        return self._ClientAffinityTime

    @ClientAffinityTime.setter
    def ClientAffinityTime(self, ClientAffinityTime):
        self._ClientAffinityTime = ClientAffinityTime

    @property
    def CertificationType(self):
        r"""SSL解析方式。
        :rtype: str
        """
        return self._CertificationType

    @CertificationType.setter
    def CertificationType(self, CertificationType):
        self._CertificationType = CertificationType

    @property
    def ServerCertificates(self):
        r"""服务器证书。
        :rtype: list of str
        """
        return self._ServerCertificates

    @ServerCertificates.setter
    def ServerCertificates(self, ServerCertificates):
        self._ServerCertificates = ServerCertificates

    @property
    def ClientCaCertificates(self):
        r"""客户端证书。
        :rtype: list of str
        """
        return self._ClientCaCertificates

    @ClientCaCertificates.setter
    def ClientCaCertificates(self, ClientCaCertificates):
        self._ClientCaCertificates = ClientCaCertificates

    @property
    def CipherPolicyId(self):
        r"""TLS密码套件包。
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""HTTP版本。
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion

    @property
    def RequestTimeout(self):
        r"""请求超时时间。
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ListenerType(self):
        r"""监听路由类型。
        :rtype: str
        """
        return self._ListenerType

    @ListenerType.setter
    def ListenerType(self, ListenerType):
        self._ListenerType = ListenerType

    @property
    def Status(self):
        r"""监听器状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EndpointGroupCounts(self):
        r"""所属监听器终端节点组个数。
        :rtype: int
        """
        return self._EndpointGroupCounts

    @EndpointGroupCounts.setter
    def EndpointGroupCounts(self, EndpointGroupCounts):
        self._EndpointGroupCounts = EndpointGroupCounts

    @property
    def GetRealIpType(self):
        r"""四层获取源IP方式。
        :rtype: str
        """
        return self._GetRealIpType

    @GetRealIpType.setter
    def GetRealIpType(self, GetRealIpType):
        self._GetRealIpType = GetRealIpType

    @property
    def IdleTimeout(self):
        r"""连接超时时间。
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Protocol = params.get("Protocol")
        if params.get("PortRanges") is not None:
            self._PortRanges = PortRanges()
            self._PortRanges._deserialize(params.get("PortRanges"))
        self._XForwardedForRealIp = params.get("XForwardedForRealIp")
        self._ClientAffinity = params.get("ClientAffinity")
        self._ClientAffinityTime = params.get("ClientAffinityTime")
        self._CertificationType = params.get("CertificationType")
        self._ServerCertificates = params.get("ServerCertificates")
        self._ClientCaCertificates = params.get("ClientCaCertificates")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        self._RequestTimeout = params.get("RequestTimeout")
        self._CreateTime = params.get("CreateTime")
        self._ListenerType = params.get("ListenerType")
        self._Status = params.get("Status")
        self._EndpointGroupCounts = params.get("EndpointGroupCounts")
        self._GetRealIpType = params.get("GetRealIpType")
        self._IdleTimeout = params.get("IdleTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerateAreasRequest(AbstractModel):
    r"""ModifyAccelerateAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _AcceleratorAreas: 加速地域信息。
        :type AcceleratorAreas: list of AcceleratorAreas
        """
        self._GlobalAcceleratorId = None
        self._AcceleratorAreas = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def AcceleratorAreas(self):
        r"""加速地域信息。
        :rtype: list of AcceleratorAreas
        """
        return self._AcceleratorAreas

    @AcceleratorAreas.setter
    def AcceleratorAreas(self, AcceleratorAreas):
        self._AcceleratorAreas = AcceleratorAreas


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        if params.get("AcceleratorAreas") is not None:
            self._AcceleratorAreas = []
            for item in params.get("AcceleratorAreas"):
                obj = AcceleratorAreas()
                obj._deserialize(item)
                self._AcceleratorAreas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccelerateAreasResponse(AbstractModel):
    r"""ModifyAccelerateAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyEndpointGroupRequest(AbstractModel):
    r"""ModifyEndpointGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>监听器ID。</p>
        :type ListenerId: str
        :param _EndpointGroupId: <p>终端节点组ID。</p>
        :type EndpointGroupId: str
        :param _EndpointConfigurations: <p>终端节点配置。</p>
        :type EndpointConfigurations: list of EndpointConfigurations
        :param _Name: <p>名称，最大长度不能超过60个字节。</p>
        :type Name: str
        :param _Description: <p>描述信息，最大长度不能超过100个字节。</p>
        :type Description: str
        :param _EnableHealthCheck: <p>是否开启健康检查。</p>
        :type EnableHealthCheck: bool
        :param _ConnectTimeout: <p>响应超时时间。</p>
        :type ConnectTimeout: int
        :param _HealthCheckInterval: <p>健康检查间隔。</p>
        :type HealthCheckInterval: int
        :param _UnhealthyThreshold: <p>不健康阀值。</p>
        :type UnhealthyThreshold: int
        :param _HealthyThreshold: <p>健康阀值。</p>
        :type HealthyThreshold: int
        :param _CheckType: <p>检查协议。</p>
        :type CheckType: str
        :param _CheckPort: <p>检查端口。</p>
        :type CheckPort: int
        :param _ContextType: <p>检查内容。</p>
        :type ContextType: str
        :param _CheckSendContext: <p>检查请求。</p>
        :type CheckSendContext: str
        :param _CheckRecvContext: <p>检查返回结果。</p>
        :type CheckRecvContext: str
        :param _CheckDomain: <p>检查域名。</p>
        :type CheckDomain: str
        :param _CheckPath: <p>检查URL。</p>
        :type CheckPath: str
        :param _CheckMethod: <p>请求方式。</p>
        :type CheckMethod: str
        :param _StatusMask: <p>状态检测码。</p>
        :type StatusMask: list of str
        :param _ForwardProtocol: <p>回源协议。</p>
        :type ForwardProtocol: str
        :param _PortOverrides: <p>端口映射。</p>
        :type PortOverrides: list of PortOverride
        :param _CipherPolicyId: <p>HPPTS加密算法套件</p>
        :type CipherPolicyId: str
        :param _HttpVersion: <p>仅HTTPS回源协议支持选择[&#39;HTTP/1.1&#39;, &#39;HTTP/2&#39;]</p><p>枚举值：</p><ul><li>HTTP/1.1： 版本HTTP/1.1</li><li>HTTP/2： 版本HTTP/2</li></ul>
        :type HttpVersion: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._EndpointGroupId = None
        self._EndpointConfigurations = None
        self._Name = None
        self._Description = None
        self._EnableHealthCheck = None
        self._ConnectTimeout = None
        self._HealthCheckInterval = None
        self._UnhealthyThreshold = None
        self._HealthyThreshold = None
        self._CheckType = None
        self._CheckPort = None
        self._ContextType = None
        self._CheckSendContext = None
        self._CheckRecvContext = None
        self._CheckDomain = None
        self._CheckPath = None
        self._CheckMethod = None
        self._StatusMask = None
        self._ForwardProtocol = None
        self._PortOverrides = None
        self._CipherPolicyId = None
        self._HttpVersion = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>监听器ID。</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def EndpointGroupId(self):
        r"""<p>终端节点组ID。</p>
        :rtype: str
        """
        return self._EndpointGroupId

    @EndpointGroupId.setter
    def EndpointGroupId(self, EndpointGroupId):
        self._EndpointGroupId = EndpointGroupId

    @property
    def EndpointConfigurations(self):
        r"""<p>终端节点配置。</p>
        :rtype: list of EndpointConfigurations
        """
        return self._EndpointConfigurations

    @EndpointConfigurations.setter
    def EndpointConfigurations(self, EndpointConfigurations):
        self._EndpointConfigurations = EndpointConfigurations

    @property
    def Name(self):
        r"""<p>名称，最大长度不能超过60个字节。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>描述信息，最大长度不能超过100个字节。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnableHealthCheck(self):
        r"""<p>是否开启健康检查。</p>
        :rtype: bool
        """
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def ConnectTimeout(self):
        r"""<p>响应超时时间。</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def HealthCheckInterval(self):
        r"""<p>健康检查间隔。</p>
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def UnhealthyThreshold(self):
        r"""<p>不健康阀值。</p>
        :rtype: int
        """
        return self._UnhealthyThreshold

    @UnhealthyThreshold.setter
    def UnhealthyThreshold(self, UnhealthyThreshold):
        self._UnhealthyThreshold = UnhealthyThreshold

    @property
    def HealthyThreshold(self):
        r"""<p>健康阀值。</p>
        :rtype: int
        """
        return self._HealthyThreshold

    @HealthyThreshold.setter
    def HealthyThreshold(self, HealthyThreshold):
        self._HealthyThreshold = HealthyThreshold

    @property
    def CheckType(self):
        r"""<p>检查协议。</p>
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType

    @property
    def CheckPort(self):
        r"""<p>检查端口。</p>
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        r"""<p>检查内容。</p>
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def CheckSendContext(self):
        r"""<p>检查请求。</p>
        :rtype: str
        """
        return self._CheckSendContext

    @CheckSendContext.setter
    def CheckSendContext(self, CheckSendContext):
        self._CheckSendContext = CheckSendContext

    @property
    def CheckRecvContext(self):
        r"""<p>检查返回结果。</p>
        :rtype: str
        """
        return self._CheckRecvContext

    @CheckRecvContext.setter
    def CheckRecvContext(self, CheckRecvContext):
        self._CheckRecvContext = CheckRecvContext

    @property
    def CheckDomain(self):
        r"""<p>检查域名。</p>
        :rtype: str
        """
        return self._CheckDomain

    @CheckDomain.setter
    def CheckDomain(self, CheckDomain):
        self._CheckDomain = CheckDomain

    @property
    def CheckPath(self):
        r"""<p>检查URL。</p>
        :rtype: str
        """
        return self._CheckPath

    @CheckPath.setter
    def CheckPath(self, CheckPath):
        self._CheckPath = CheckPath

    @property
    def CheckMethod(self):
        r"""<p>请求方式。</p>
        :rtype: str
        """
        return self._CheckMethod

    @CheckMethod.setter
    def CheckMethod(self, CheckMethod):
        self._CheckMethod = CheckMethod

    @property
    def StatusMask(self):
        r"""<p>状态检测码。</p>
        :rtype: list of str
        """
        return self._StatusMask

    @StatusMask.setter
    def StatusMask(self, StatusMask):
        self._StatusMask = StatusMask

    @property
    def ForwardProtocol(self):
        r"""<p>回源协议。</p>
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def PortOverrides(self):
        r"""<p>端口映射。</p>
        :rtype: list of PortOverride
        """
        return self._PortOverrides

    @PortOverrides.setter
    def PortOverrides(self, PortOverrides):
        self._PortOverrides = PortOverrides

    @property
    def CipherPolicyId(self):
        r"""<p>HPPTS加密算法套件</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def HttpVersion(self):
        r"""<p>仅HTTPS回源协议支持选择[&#39;HTTP/1.1&#39;, &#39;HTTP/2&#39;]</p><p>枚举值：</p><ul><li>HTTP/1.1： 版本HTTP/1.1</li><li>HTTP/2： 版本HTTP/2</li></ul>
        :rtype: str
        """
        return self._HttpVersion

    @HttpVersion.setter
    def HttpVersion(self, HttpVersion):
        self._HttpVersion = HttpVersion


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._EndpointGroupId = params.get("EndpointGroupId")
        if params.get("EndpointConfigurations") is not None:
            self._EndpointConfigurations = []
            for item in params.get("EndpointConfigurations"):
                obj = EndpointConfigurations()
                obj._deserialize(item)
                self._EndpointConfigurations.append(obj)
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._UnhealthyThreshold = params.get("UnhealthyThreshold")
        self._HealthyThreshold = params.get("HealthyThreshold")
        self._CheckType = params.get("CheckType")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._CheckSendContext = params.get("CheckSendContext")
        self._CheckRecvContext = params.get("CheckRecvContext")
        self._CheckDomain = params.get("CheckDomain")
        self._CheckPath = params.get("CheckPath")
        self._CheckMethod = params.get("CheckMethod")
        self._StatusMask = params.get("StatusMask")
        self._ForwardProtocol = params.get("ForwardProtocol")
        if params.get("PortOverrides") is not None:
            self._PortOverrides = []
            for item in params.get("PortOverrides"):
                obj = PortOverride()
                obj._deserialize(item)
                self._PortOverrides.append(obj)
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._HttpVersion = params.get("HttpVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEndpointGroupResponse(AbstractModel):
    r"""ModifyEndpointGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID。</p>
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyForwardingPolicyRequest(AbstractModel):
    r"""ModifyForwardingPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _ListenerId: 监听器ID。
        :type ListenerId: str
        :param _ForwardingPolicyId: 策略ID。
        :type ForwardingPolicyId: str
        :param _Host: 域名。
        :type Host: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._Host = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""监听器ID。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""策略ID。
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def Host(self):
        r"""域名。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardingPolicyResponse(AbstractModel):
    r"""ModifyForwardingPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyForwardingRuleRequest(AbstractModel):
    r"""ModifyForwardingRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>监听器ID。</p>
        :type ListenerId: str
        :param _ForwardingPolicyId: <p>策略ID。</p>
        :type ForwardingPolicyId: str
        :param _ForwardingRuleId: <p>七层转发规则ID。</p>
        :type ForwardingRuleId: str
        :param _RuleConditions: <p>七层转发规则条件信息。</p>
        :type RuleConditions: list of RuleCondition
        :param _RuleActions: <p>七层转发规则行为信息。</p>
        :type RuleActions: list of RuleAction
        :param _OriginHeaders: <p>回源Header信息。</p>
        :type OriginHeaders: list of OriginHeader
        :param _EnableOriginSni: <p>是否开启回源sni。</p>
        :type EnableOriginSni: bool
        :param _OriginSni: <p>回源sni。</p>
        :type OriginSni: str
        :param _OriginHost: <p>回源host。</p>
        :type OriginHost: str
        :param _ResponseHeaders: <p>源站响应头</p>
        :type ResponseHeaders: list of ResponseHeaders
        :param _HideResponseHeaders: <p>删除源站响应头</p>
        :type HideResponseHeaders: list of HideResponseHeaders
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._ForwardingPolicyId = None
        self._ForwardingRuleId = None
        self._RuleConditions = None
        self._RuleActions = None
        self._OriginHeaders = None
        self._EnableOriginSni = None
        self._OriginSni = None
        self._OriginHost = None
        self._ResponseHeaders = None
        self._HideResponseHeaders = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>监听器ID。</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ForwardingPolicyId(self):
        r"""<p>策略ID。</p>
        :rtype: str
        """
        return self._ForwardingPolicyId

    @ForwardingPolicyId.setter
    def ForwardingPolicyId(self, ForwardingPolicyId):
        self._ForwardingPolicyId = ForwardingPolicyId

    @property
    def ForwardingRuleId(self):
        r"""<p>七层转发规则ID。</p>
        :rtype: str
        """
        return self._ForwardingRuleId

    @ForwardingRuleId.setter
    def ForwardingRuleId(self, ForwardingRuleId):
        self._ForwardingRuleId = ForwardingRuleId

    @property
    def RuleConditions(self):
        r"""<p>七层转发规则条件信息。</p>
        :rtype: list of RuleCondition
        """
        return self._RuleConditions

    @RuleConditions.setter
    def RuleConditions(self, RuleConditions):
        self._RuleConditions = RuleConditions

    @property
    def RuleActions(self):
        r"""<p>七层转发规则行为信息。</p>
        :rtype: list of RuleAction
        """
        return self._RuleActions

    @RuleActions.setter
    def RuleActions(self, RuleActions):
        self._RuleActions = RuleActions

    @property
    def OriginHeaders(self):
        r"""<p>回源Header信息。</p>
        :rtype: list of OriginHeader
        """
        return self._OriginHeaders

    @OriginHeaders.setter
    def OriginHeaders(self, OriginHeaders):
        self._OriginHeaders = OriginHeaders

    @property
    def EnableOriginSni(self):
        r"""<p>是否开启回源sni。</p>
        :rtype: bool
        """
        return self._EnableOriginSni

    @EnableOriginSni.setter
    def EnableOriginSni(self, EnableOriginSni):
        self._EnableOriginSni = EnableOriginSni

    @property
    def OriginSni(self):
        r"""<p>回源sni。</p>
        :rtype: str
        """
        return self._OriginSni

    @OriginSni.setter
    def OriginSni(self, OriginSni):
        self._OriginSni = OriginSni

    @property
    def OriginHost(self):
        r"""<p>回源host。</p>
        :rtype: str
        """
        return self._OriginHost

    @OriginHost.setter
    def OriginHost(self, OriginHost):
        self._OriginHost = OriginHost

    @property
    def ResponseHeaders(self):
        r"""<p>源站响应头</p>
        :rtype: list of ResponseHeaders
        """
        return self._ResponseHeaders

    @ResponseHeaders.setter
    def ResponseHeaders(self, ResponseHeaders):
        self._ResponseHeaders = ResponseHeaders

    @property
    def HideResponseHeaders(self):
        r"""<p>删除源站响应头</p>
        :rtype: list of HideResponseHeaders
        """
        return self._HideResponseHeaders

    @HideResponseHeaders.setter
    def HideResponseHeaders(self, HideResponseHeaders):
        self._HideResponseHeaders = HideResponseHeaders


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._ForwardingPolicyId = params.get("ForwardingPolicyId")
        self._ForwardingRuleId = params.get("ForwardingRuleId")
        if params.get("RuleConditions") is not None:
            self._RuleConditions = []
            for item in params.get("RuleConditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._RuleConditions.append(obj)
        if params.get("RuleActions") is not None:
            self._RuleActions = []
            for item in params.get("RuleActions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._RuleActions.append(obj)
        if params.get("OriginHeaders") is not None:
            self._OriginHeaders = []
            for item in params.get("OriginHeaders"):
                obj = OriginHeader()
                obj._deserialize(item)
                self._OriginHeaders.append(obj)
        self._EnableOriginSni = params.get("EnableOriginSni")
        self._OriginSni = params.get("OriginSni")
        self._OriginHost = params.get("OriginHost")
        if params.get("ResponseHeaders") is not None:
            self._ResponseHeaders = []
            for item in params.get("ResponseHeaders"):
                obj = ResponseHeaders()
                obj._deserialize(item)
                self._ResponseHeaders.append(obj)
        if params.get("HideResponseHeaders") is not None:
            self._HideResponseHeaders = []
            for item in params.get("HideResponseHeaders"):
                obj = HideResponseHeaders()
                obj._deserialize(item)
                self._HideResponseHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyForwardingRuleResponse(AbstractModel):
    r"""ModifyForwardingRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>异步任务ID。</p>
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>异步任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyGlobalAcceleratorRequest(AbstractModel):
    r"""ModifyGlobalAccelerator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: 全球加速实例ID。
        :type GlobalAcceleratorId: str
        :param _Name: 名称，最大长度不能超过60个字节。
        :type Name: str
        :param _Description: 描述信息，最大长度不能超过100个字节。
        :type Description: str
        :param _CrossBorderType: 跨境类型。
        :type CrossBorderType: str
        :param _CrossBorderPromiseFlag: 代表是否跨境服务承诺。
        :type CrossBorderPromiseFlag: bool
        """
        self._GlobalAcceleratorId = None
        self._Name = None
        self._Description = None
        self._CrossBorderType = None
        self._CrossBorderPromiseFlag = None

    @property
    def GlobalAcceleratorId(self):
        r"""全球加速实例ID。
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def Name(self):
        r"""名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述信息，最大长度不能超过100个字节。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CrossBorderType(self):
        r"""跨境类型。
        :rtype: str
        """
        return self._CrossBorderType

    @CrossBorderType.setter
    def CrossBorderType(self, CrossBorderType):
        self._CrossBorderType = CrossBorderType

    @property
    def CrossBorderPromiseFlag(self):
        r"""代表是否跨境服务承诺。
        :rtype: bool
        """
        return self._CrossBorderPromiseFlag

    @CrossBorderPromiseFlag.setter
    def CrossBorderPromiseFlag(self, CrossBorderPromiseFlag):
        self._CrossBorderPromiseFlag = CrossBorderPromiseFlag


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._CrossBorderType = params.get("CrossBorderType")
        self._CrossBorderPromiseFlag = params.get("CrossBorderPromiseFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlobalAcceleratorResponse(AbstractModel):
    r"""ModifyGlobalAccelerator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    r"""ModifyListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlobalAcceleratorId: <p>全球加速实例ID。</p>
        :type GlobalAcceleratorId: str
        :param _ListenerId: <p>监听器ID。</p>
        :type ListenerId: str
        :param _Name: <p>名称，最大长度不能超过60个字节。</p>
        :type Name: str
        :param _Description: <p>描述信息，最大长度不能超过100个字节。</p>
        :type Description: str
        :param _IdleTimeout: <p>连接空闲等待时间。</p>
        :type IdleTimeout: int
        :param _ClientAffinity: <p>是否开启会话保持。</p>
        :type ClientAffinity: str
        :param _ClientAffinityTime: <p>会话保持时间。</p>
        :type ClientAffinityTime: int
        :param _RequestTimeout: <p>请求超时时间。</p>
        :type RequestTimeout: int
        :param _XForwardedForRealIp: <p>是否打开七层获取源IP方式。</p>
        :type XForwardedForRealIp: bool
        :param _CertificationType: <p>解析方式。UNIDIRECTIONAL：双向。MUTUAL：单向。</p>
        :type CertificationType: str
        :param _CipherPolicyId: <p>加密算法套件。</p>
        :type CipherPolicyId: str
        :param _ServerCertificates: <p>服务器证书。</p>
        :type ServerCertificates: list of str
        :param _ClientCaCertificates: <p>客户端证书。</p>
        :type ClientCaCertificates: list of str
        :param _GetRealIpType: <p>四层获取源IP方式。</p>
        :type GetRealIpType: str
        """
        self._GlobalAcceleratorId = None
        self._ListenerId = None
        self._Name = None
        self._Description = None
        self._IdleTimeout = None
        self._ClientAffinity = None
        self._ClientAffinityTime = None
        self._RequestTimeout = None
        self._XForwardedForRealIp = None
        self._CertificationType = None
        self._CipherPolicyId = None
        self._ServerCertificates = None
        self._ClientCaCertificates = None
        self._GetRealIpType = None

    @property
    def GlobalAcceleratorId(self):
        r"""<p>全球加速实例ID。</p>
        :rtype: str
        """
        return self._GlobalAcceleratorId

    @GlobalAcceleratorId.setter
    def GlobalAcceleratorId(self, GlobalAcceleratorId):
        self._GlobalAcceleratorId = GlobalAcceleratorId

    @property
    def ListenerId(self):
        r"""<p>监听器ID。</p>
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Name(self):
        r"""<p>名称，最大长度不能超过60个字节。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>描述信息，最大长度不能超过100个字节。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdleTimeout(self):
        r"""<p>连接空闲等待时间。</p>
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ClientAffinity(self):
        r"""<p>是否开启会话保持。</p>
        :rtype: str
        """
        return self._ClientAffinity

    @ClientAffinity.setter
    def ClientAffinity(self, ClientAffinity):
        self._ClientAffinity = ClientAffinity

    @property
    def ClientAffinityTime(self):
        r"""<p>会话保持时间。</p>
        :rtype: int
        """
        return self._ClientAffinityTime

    @ClientAffinityTime.setter
    def ClientAffinityTime(self, ClientAffinityTime):
        self._ClientAffinityTime = ClientAffinityTime

    @property
    def RequestTimeout(self):
        r"""<p>请求超时时间。</p>
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def XForwardedForRealIp(self):
        r"""<p>是否打开七层获取源IP方式。</p>
        :rtype: bool
        """
        return self._XForwardedForRealIp

    @XForwardedForRealIp.setter
    def XForwardedForRealIp(self, XForwardedForRealIp):
        self._XForwardedForRealIp = XForwardedForRealIp

    @property
    def CertificationType(self):
        r"""<p>解析方式。UNIDIRECTIONAL：双向。MUTUAL：单向。</p>
        :rtype: str
        """
        return self._CertificationType

    @CertificationType.setter
    def CertificationType(self, CertificationType):
        self._CertificationType = CertificationType

    @property
    def CipherPolicyId(self):
        r"""<p>加密算法套件。</p>
        :rtype: str
        """
        return self._CipherPolicyId

    @CipherPolicyId.setter
    def CipherPolicyId(self, CipherPolicyId):
        self._CipherPolicyId = CipherPolicyId

    @property
    def ServerCertificates(self):
        r"""<p>服务器证书。</p>
        :rtype: list of str
        """
        return self._ServerCertificates

    @ServerCertificates.setter
    def ServerCertificates(self, ServerCertificates):
        self._ServerCertificates = ServerCertificates

    @property
    def ClientCaCertificates(self):
        r"""<p>客户端证书。</p>
        :rtype: list of str
        """
        return self._ClientCaCertificates

    @ClientCaCertificates.setter
    def ClientCaCertificates(self, ClientCaCertificates):
        self._ClientCaCertificates = ClientCaCertificates

    @property
    def GetRealIpType(self):
        r"""<p>四层获取源IP方式。</p>
        :rtype: str
        """
        return self._GetRealIpType

    @GetRealIpType.setter
    def GetRealIpType(self, GetRealIpType):
        self._GetRealIpType = GetRealIpType


    def _deserialize(self, params):
        self._GlobalAcceleratorId = params.get("GlobalAcceleratorId")
        self._ListenerId = params.get("ListenerId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ClientAffinity = params.get("ClientAffinity")
        self._ClientAffinityTime = params.get("ClientAffinityTime")
        self._RequestTimeout = params.get("RequestTimeout")
        self._XForwardedForRealIp = params.get("XForwardedForRealIp")
        self._CertificationType = params.get("CertificationType")
        self._CipherPolicyId = params.get("CipherPolicyId")
        self._ServerCertificates = params.get("ServerCertificates")
        self._ClientCaCertificates = params.get("ClientCaCertificates")
        self._GetRealIpType = params.get("GetRealIpType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    r"""ModifyListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: <p>任务ID。</p>
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""<p>任务ID。</p>
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class OriginHeader(AbstractModel):
    r"""回源Header信息

    """

    def __init__(self):
        r"""
        :param _Key: 键。
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""键。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortOverride(AbstractModel):
    r"""端口映射

    """

    def __init__(self):
        r"""
        :param _ListenerPort: 监听端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerPort: int
        :param _EndpointPort: 映射端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndpointPort: int
        """
        self._ListenerPort = None
        self._EndpointPort = None

    @property
    def ListenerPort(self):
        r"""监听端口。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def EndpointPort(self):
        r"""映射端口。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EndpointPort

    @EndpointPort.setter
    def EndpointPort(self, EndpointPort):
        self._EndpointPort = EndpointPort


    def _deserialize(self, params):
        self._ListenerPort = params.get("ListenerPort")
        self._EndpointPort = params.get("EndpointPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortRanges(AbstractModel):
    r"""端口范围

    """

    def __init__(self):
        r"""
        :param _FromPort: 起始端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type FromPort: int
        :param _ToPort: 终点端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type ToPort: int
        """
        self._FromPort = None
        self._ToPort = None

    @property
    def FromPort(self):
        r"""起始端口。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def ToPort(self):
        r"""终点端口。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeaders(AbstractModel):
    r"""响应Header

    """

    def __init__(self):
        r"""
        :param _Key: <p>key</p>
        :type Key: str
        :param _Value: <p>value</p>
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>key</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>value</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleAction(AbstractModel):
    r"""七层转发规则行为信息

    """

    def __init__(self):
        r"""
        :param _RuleActionType: 七层转发规则行为类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleActionType: str
        :param _RuleActionValue: 七层转发规则行为值
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleActionValue: str
        """
        self._RuleActionType = None
        self._RuleActionValue = None

    @property
    def RuleActionType(self):
        r"""七层转发规则行为类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleActionType

    @RuleActionType.setter
    def RuleActionType(self, RuleActionType):
        self._RuleActionType = RuleActionType

    @property
    def RuleActionValue(self):
        r"""七层转发规则行为值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleActionValue

    @RuleActionValue.setter
    def RuleActionValue(self, RuleActionValue):
        self._RuleActionValue = RuleActionValue


    def _deserialize(self, params):
        self._RuleActionType = params.get("RuleActionType")
        self._RuleActionValue = params.get("RuleActionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    r"""七层转发规则条件信息

    """

    def __init__(self):
        r"""
        :param _RuleConditionType: 七层转发规则条件类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleConditionType: str
        :param _RuleConditionValue: 七层转发规则条件值
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleConditionValue: list of str
        """
        self._RuleConditionType = None
        self._RuleConditionValue = None

    @property
    def RuleConditionType(self):
        r"""七层转发规则条件类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleConditionType

    @RuleConditionType.setter
    def RuleConditionType(self, RuleConditionType):
        self._RuleConditionType = RuleConditionType

    @property
    def RuleConditionValue(self):
        r"""七层转发规则条件值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RuleConditionValue

    @RuleConditionValue.setter
    def RuleConditionValue(self, RuleConditionValue):
        self._RuleConditionValue = RuleConditionValue


    def _deserialize(self, params):
        self._RuleConditionType = params.get("RuleConditionType")
        self._RuleConditionValue = params.get("RuleConditionValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签键值对

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        