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


class Address(AbstractModel):
    """描述 EIP 信息

    """

    def __init__(self):
        r"""
        :param _AddressId: EIP的ID，是EIP的唯一标识。
        :type AddressId: str
        :param _AddressName: EIP名称。
        :type AddressName: str
        :param _AddressStatus: EIP状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)
        :type AddressStatus: str
        :param _AddressIp: 外网IP地址
        :type AddressIp: str
        :param _InstanceId: 绑定的资源实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _CreatedTime: 创建时间。ISO 8601 格式：YYYY-MM-DDTHH:mm:ss.sssZ
        :type CreatedTime: str
        :param _NetworkInterfaceId: 绑定的弹性网卡ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkInterfaceId: str
        :param _PrivateAddressIp: 绑定的资源内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateAddressIp: str
        :param _IsArrears: 资源隔离状态。true表示eip处于隔离状态，false表示资源处于未隔离状态
        :type IsArrears: bool
        :param _IsBlocked: 资源封堵状态。true表示eip处于封堵状态，false表示eip处于未封堵状态
        :type IsBlocked: bool
        :param _IsEipDirectConnection: eip是否支持直通模式。true表示eip支持直通模式，false表示资源不支持直通模式
        :type IsEipDirectConnection: bool
        :param _AddressType: eip资源类型，包括"CalcIP","WanIP","EIP","AnycastEIP"。其中"CalcIP"表示设备ip，“WanIP”表示普通公网ip，“EIP”表示弹性公网ip，“AnycastEip”表示加速EIP
        :type AddressType: str
        :param _CascadeRelease: eip是否在解绑后自动释放。true表示eip将会在解绑后自动释放，false表示eip在解绑后不会自动释放
        :type CascadeRelease: bool
        :param _InternetServiceProvider: 运营商，CTCC电信，CUCC联通，CMCC移动
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetServiceProvider: str
        :param _Bandwidth: 带宽上限
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _PayMode: 计费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        """
        self._AddressId = None
        self._AddressName = None
        self._AddressStatus = None
        self._AddressIp = None
        self._InstanceId = None
        self._CreatedTime = None
        self._NetworkInterfaceId = None
        self._PrivateAddressIp = None
        self._IsArrears = None
        self._IsBlocked = None
        self._IsEipDirectConnection = None
        self._AddressType = None
        self._CascadeRelease = None
        self._InternetServiceProvider = None
        self._Bandwidth = None
        self._PayMode = None

    @property
    def AddressId(self):
        """EIP的ID，是EIP的唯一标识。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressName(self):
        """EIP名称。
        :rtype: str
        """
        return self._AddressName

    @AddressName.setter
    def AddressName(self, AddressName):
        self._AddressName = AddressName

    @property
    def AddressStatus(self):
        """EIP状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)
        :rtype: str
        """
        return self._AddressStatus

    @AddressStatus.setter
    def AddressStatus(self, AddressStatus):
        self._AddressStatus = AddressStatus

    @property
    def AddressIp(self):
        """外网IP地址
        :rtype: str
        """
        return self._AddressIp

    @AddressIp.setter
    def AddressIp(self, AddressIp):
        self._AddressIp = AddressIp

    @property
    def InstanceId(self):
        """绑定的资源实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CreatedTime(self):
        """创建时间。ISO 8601 格式：YYYY-MM-DDTHH:mm:ss.sssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NetworkInterfaceId(self):
        """绑定的弹性网卡ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateAddressIp(self):
        """绑定的资源内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateAddressIp

    @PrivateAddressIp.setter
    def PrivateAddressIp(self, PrivateAddressIp):
        self._PrivateAddressIp = PrivateAddressIp

    @property
    def IsArrears(self):
        """资源隔离状态。true表示eip处于隔离状态，false表示资源处于未隔离状态
        :rtype: bool
        """
        return self._IsArrears

    @IsArrears.setter
    def IsArrears(self, IsArrears):
        self._IsArrears = IsArrears

    @property
    def IsBlocked(self):
        """资源封堵状态。true表示eip处于封堵状态，false表示eip处于未封堵状态
        :rtype: bool
        """
        return self._IsBlocked

    @IsBlocked.setter
    def IsBlocked(self, IsBlocked):
        self._IsBlocked = IsBlocked

    @property
    def IsEipDirectConnection(self):
        """eip是否支持直通模式。true表示eip支持直通模式，false表示资源不支持直通模式
        :rtype: bool
        """
        return self._IsEipDirectConnection

    @IsEipDirectConnection.setter
    def IsEipDirectConnection(self, IsEipDirectConnection):
        self._IsEipDirectConnection = IsEipDirectConnection

    @property
    def AddressType(self):
        """eip资源类型，包括"CalcIP","WanIP","EIP","AnycastEIP"。其中"CalcIP"表示设备ip，“WanIP”表示普通公网ip，“EIP”表示弹性公网ip，“AnycastEip”表示加速EIP
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def CascadeRelease(self):
        """eip是否在解绑后自动释放。true表示eip将会在解绑后自动释放，false表示eip在解绑后不会自动释放
        :rtype: bool
        """
        return self._CascadeRelease

    @CascadeRelease.setter
    def CascadeRelease(self, CascadeRelease):
        self._CascadeRelease = CascadeRelease

    @property
    def InternetServiceProvider(self):
        """运营商，CTCC电信，CUCC联通，CMCC移动
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InternetServiceProvider

    @InternetServiceProvider.setter
    def InternetServiceProvider(self, InternetServiceProvider):
        self._InternetServiceProvider = InternetServiceProvider

    @property
    def Bandwidth(self):
        """带宽上限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def PayMode(self):
        """计费模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._AddressId = params.get("AddressId")
        self._AddressName = params.get("AddressName")
        self._AddressStatus = params.get("AddressStatus")
        self._AddressIp = params.get("AddressIp")
        self._InstanceId = params.get("InstanceId")
        self._CreatedTime = params.get("CreatedTime")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._PrivateAddressIp = params.get("PrivateAddressIp")
        self._IsArrears = params.get("IsArrears")
        self._IsBlocked = params.get("IsBlocked")
        self._IsEipDirectConnection = params.get("IsEipDirectConnection")
        self._AddressType = params.get("AddressType")
        self._CascadeRelease = params.get("CascadeRelease")
        self._InternetServiceProvider = params.get("InternetServiceProvider")
        self._Bandwidth = params.get("Bandwidth")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressInfo(AbstractModel):
    """ip地址相关信息结构体。

    """

    def __init__(self):
        r"""
        :param _PublicIPAddressInfo: 实例的外网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        :param _PrivateIPAddressInfo: 实例的内网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PrivateIPAddressInfo`
        :param _PublicIPv6AddressInfo: 实例的外网ipv6相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIPv6AddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        self._PublicIPAddressInfo = None
        self._PrivateIPAddressInfo = None
        self._PublicIPv6AddressInfo = None

    @property
    def PublicIPAddressInfo(self):
        """实例的外网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        return self._PublicIPAddressInfo

    @PublicIPAddressInfo.setter
    def PublicIPAddressInfo(self, PublicIPAddressInfo):
        self._PublicIPAddressInfo = PublicIPAddressInfo

    @property
    def PrivateIPAddressInfo(self):
        """实例的内网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PrivateIPAddressInfo`
        """
        return self._PrivateIPAddressInfo

    @PrivateIPAddressInfo.setter
    def PrivateIPAddressInfo(self, PrivateIPAddressInfo):
        self._PrivateIPAddressInfo = PrivateIPAddressInfo

    @property
    def PublicIPv6AddressInfo(self):
        """实例的外网ipv6相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`
        """
        return self._PublicIPv6AddressInfo

    @PublicIPv6AddressInfo.setter
    def PublicIPv6AddressInfo(self, PublicIPv6AddressInfo):
        self._PublicIPv6AddressInfo = PublicIPv6AddressInfo


    def _deserialize(self, params):
        if params.get("PublicIPAddressInfo") is not None:
            self._PublicIPAddressInfo = PublicIPAddressInfo()
            self._PublicIPAddressInfo._deserialize(params.get("PublicIPAddressInfo"))
        if params.get("PrivateIPAddressInfo") is not None:
            self._PrivateIPAddressInfo = PrivateIPAddressInfo()
            self._PrivateIPAddressInfo._deserialize(params.get("PrivateIPAddressInfo"))
        if params.get("PublicIPv6AddressInfo") is not None:
            self._PublicIPv6AddressInfo = PublicIPAddressInfo()
            self._PublicIPv6AddressInfo._deserialize(params.get("PublicIPv6AddressInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateSpecification(AbstractModel):
    """IP地址模板

    """

    def __init__(self):
        r"""
        :param _AddressId: IP地址ID，例如：eipm-2uw6ujo6。
        :type AddressId: str
        :param _AddressGroupId: IP地址组ID，例如：eipmg-2uw6ujo6。
        :type AddressGroupId: str
        """
        self._AddressId = None
        self._AddressGroupId = None

    @property
    def AddressId(self):
        """IP地址ID，例如：eipm-2uw6ujo6。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressGroupId(self):
        """IP地址组ID，例如：eipmg-2uw6ujo6。
        :rtype: str
        """
        return self._AddressGroupId

    @AddressGroupId.setter
    def AddressGroupId(self, AddressGroupId):
        self._AddressGroupId = AddressGroupId


    def _deserialize(self, params):
        self._AddressId = params.get("AddressId")
        self._AddressGroupId = params.get("AddressGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressCount: EIP数量。默认值：1。
        :type AddressCount: int
        :param _InternetServiceProvider: CMCC：中国移动
CTCC：中国电信
CUCC：中国联通
        :type InternetServiceProvider: str
        :param _InternetMaxBandwidthOut: 1 Mbps 至 5000 Mbps，默认值：1 Mbps。
        :type InternetMaxBandwidthOut: int
        :param _Tags: 需要关联的标签列表。
        :type Tags: list of Tag
        :param _InstanceId: 要绑定的实例 ID。
        :type InstanceId: str
        :param _NetworkInterfaceId: 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。
        :type NetworkInterfaceId: str
        :param _PrivateIpAddress: 要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。
        :type PrivateIpAddress: str
        """
        self._EcmRegion = None
        self._AddressCount = None
        self._InternetServiceProvider = None
        self._InternetMaxBandwidthOut = None
        self._Tags = None
        self._InstanceId = None
        self._NetworkInterfaceId = None
        self._PrivateIpAddress = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressCount(self):
        """EIP数量。默认值：1。
        :rtype: int
        """
        return self._AddressCount

    @AddressCount.setter
    def AddressCount(self, AddressCount):
        self._AddressCount = AddressCount

    @property
    def InternetServiceProvider(self):
        """CMCC：中国移动
CTCC：中国电信
CUCC：中国联通
        :rtype: str
        """
        return self._InternetServiceProvider

    @InternetServiceProvider.setter
    def InternetServiceProvider(self, InternetServiceProvider):
        self._InternetServiceProvider = InternetServiceProvider

    @property
    def InternetMaxBandwidthOut(self):
        """1 Mbps 至 5000 Mbps，默认值：1 Mbps。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Tags(self):
        """需要关联的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        """要绑定的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NetworkInterfaceId(self):
        """要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddress(self):
        """要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressCount = params.get("AddressCount")
        self._InternetServiceProvider = params.get("InternetServiceProvider")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressSet: 申请到的 EIP 的唯一 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressSet: list of str
        :param _TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressSet = None
        self._TaskId = None
        self._RequestId = None

    @property
    def AddressSet(self):
        """申请到的 EIP 的唯一 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

    @property
    def TaskId(self):
        """异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
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
        self._AddressSet = params.get("AddressSet")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class AllocateIpv6AddressesBandwidthRequest(AbstractModel):
    """AllocateIpv6AddressesBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域。
        :type EcmRegion: str
        :param _Ipv6Addresses: 需要开通公网访问能力的IPV6地址。
        :type Ipv6Addresses: list of str
        :param _InternetMaxBandwidthOut: 带宽，单位Mbps，默认是1Mbps。
        :type InternetMaxBandwidthOut: int
        :param _InternetChargeType: 网络计费模式，当前支持 BANDWIDTH_PACKAGE。
        :type InternetChargeType: str
        """
        self._EcmRegion = None
        self._Ipv6Addresses = None
        self._InternetMaxBandwidthOut = None
        self._InternetChargeType = None

    @property
    def EcmRegion(self):
        """ECM 地域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Ipv6Addresses(self):
        """需要开通公网访问能力的IPV6地址。
        :rtype: list of str
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses

    @property
    def InternetMaxBandwidthOut(self):
        """带宽，单位Mbps，默认是1Mbps。
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def InternetChargeType(self):
        """网络计费模式，当前支持 BANDWIDTH_PACKAGE。
        :rtype: str
        """
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._Ipv6Addresses = params.get("Ipv6Addresses")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._InternetChargeType = params.get("InternetChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateIpv6AddressesBandwidthResponse(AbstractModel):
    """AllocateIpv6AddressesBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressSet: 弹性公网 IPV6 的唯一 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressSet: list of str
        :param _TaskId: 异步任务TaskId。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AddressSet = None
        self._TaskId = None
        self._RequestId = None

    @property
    def AddressSet(self):
        """弹性公网 IPV6 的唯一 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

    @property
    def TaskId(self):
        """异步任务TaskId。
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
        self._AddressSet = params.get("AddressSet")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Area(AbstractModel):
    """区域信息

    """

    def __init__(self):
        r"""
        :param _AreaId: 区域ID
        :type AreaId: str
        :param _AreaName: 区域名称
        :type AreaName: str
        """
        self._AreaId = None
        self._AreaName = None

    @property
    def AreaId(self):
        """区域ID
        :rtype: str
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId

    @property
    def AreaName(self):
        """区域名称
        :rtype: str
        """
        return self._AreaName

    @AreaName.setter
    def AreaName(self, AreaName):
        self._AreaName = AreaName


    def _deserialize(self, params):
        self._AreaId = params.get("AreaId")
        self._AreaName = params.get("AreaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _NetworkInterfaceId: 弹性网卡实例ID，形如：eni-1snva0vd。目前只支持主网卡上分配。
        :type NetworkInterfaceId: str
        :param _Ipv6Addresses: 指定的IPv6地址列表，单次最多指定10个。与入参Ipv6AddressCount合并计算配额。与Ipv6AddressCount必填一个。
        :type Ipv6Addresses: list of Ipv6Address
        :param _Ipv6AddressCount: 自动分配IPv6地址个数，内网IP地址个数总和不能超过配数。与入参Ipv6Addresses合并计算配额。与Ipv6Addresses必填一个。
        :type Ipv6AddressCount: int
        :param _ISPType: ipv6运营商如下：
CTCC：中国电信
CUCC：中国联通
CMCC：中国移动
        :type ISPType: str
        :param _SkipCheckIPv6Address: 是否跳过校验一个网卡只能分配一个IPv6 CIDR。该字段通常为true（用于兼容存量子机只有一个地址的情形）。
        :type SkipCheckIPv6Address: bool
        :param _SkipAllocateBandwidth: 是否跳过自动开通公网带宽。通常为true(根据运营系统的用户配置来决定是否自动开通，以支持当前子机购买时的行为）。
        :type SkipAllocateBandwidth: bool
        :param _Ipv6ISP: 该字段没有使用（已过期）。
        :type Ipv6ISP: str
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._Ipv6Addresses = None
        self._Ipv6AddressCount = None
        self._ISPType = None
        self._SkipCheckIPv6Address = None
        self._SkipAllocateBandwidth = None
        self._Ipv6ISP = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，形如：eni-1snva0vd。目前只支持主网卡上分配。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def Ipv6Addresses(self):
        """指定的IPv6地址列表，单次最多指定10个。与入参Ipv6AddressCount合并计算配额。与Ipv6AddressCount必填一个。
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses

    @property
    def Ipv6AddressCount(self):
        """自动分配IPv6地址个数，内网IP地址个数总和不能超过配数。与入参Ipv6Addresses合并计算配额。与Ipv6Addresses必填一个。
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def ISPType(self):
        """ipv6运营商如下：
CTCC：中国电信
CUCC：中国联通
CMCC：中国移动
        :rtype: str
        """
        return self._ISPType

    @ISPType.setter
    def ISPType(self, ISPType):
        self._ISPType = ISPType

    @property
    def SkipCheckIPv6Address(self):
        """是否跳过校验一个网卡只能分配一个IPv6 CIDR。该字段通常为true（用于兼容存量子机只有一个地址的情形）。
        :rtype: bool
        """
        return self._SkipCheckIPv6Address

    @SkipCheckIPv6Address.setter
    def SkipCheckIPv6Address(self, SkipCheckIPv6Address):
        self._SkipCheckIPv6Address = SkipCheckIPv6Address

    @property
    def SkipAllocateBandwidth(self):
        """是否跳过自动开通公网带宽。通常为true(根据运营系统的用户配置来决定是否自动开通，以支持当前子机购买时的行为）。
        :rtype: bool
        """
        return self._SkipAllocateBandwidth

    @SkipAllocateBandwidth.setter
    def SkipAllocateBandwidth(self, SkipAllocateBandwidth):
        self._SkipAllocateBandwidth = SkipAllocateBandwidth

    @property
    def Ipv6ISP(self):
        warnings.warn("parameter `Ipv6ISP` is deprecated", DeprecationWarning) 

        """该字段没有使用（已过期）。
        :rtype: str
        """
        return self._Ipv6ISP

    @Ipv6ISP.setter
    def Ipv6ISP(self, Ipv6ISP):
        warnings.warn("parameter `Ipv6ISP` is deprecated", DeprecationWarning) 

        self._Ipv6ISP = Ipv6ISP


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._ISPType = params.get("ISPType")
        self._SkipCheckIPv6Address = params.get("SkipCheckIPv6Address")
        self._SkipAllocateBandwidth = params.get("SkipAllocateBandwidth")
        self._Ipv6ISP = params.get("Ipv6ISP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesResponse(AbstractModel):
    """AssignIpv6Addresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ipv6AddressSet: 分配给弹性网卡的IPv6地址列表。
        :type Ipv6AddressSet: list of Ipv6Address
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ipv6AddressSet = None
        self._RequestId = None

    @property
    def Ipv6AddressSet(self):
        """分配给弹性网卡的IPv6地址列表。
        :rtype: list of Ipv6Address
        """
        return self._Ipv6AddressSet

    @Ipv6AddressSet.setter
    def Ipv6AddressSet(self, Ipv6AddressSet):
        self._Ipv6AddressSet = Ipv6AddressSet

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
        if params.get("Ipv6AddressSet") is not None:
            self._Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6AddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class AssignIpv6CidrBlockRequest(AbstractModel):
    """AssignIpv6CidrBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。	
        :type VpcId: str
        :param _ISPType: 网络运营商类型 'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
        :type ISPType: str
        :param _EcmRegion: ECM地域。
        :type EcmRegion: str
        """
        self._VpcId = None
        self._ISPType = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """`VPC`实例`ID`，形如：`vpc-f49l6u0z`。	
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ISPType(self):
        """网络运营商类型 'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
        :rtype: str
        """
        return self._ISPType

    @ISPType.setter
    def ISPType(self, ISPType):
        self._ISPType = ISPType

    @property
    def EcmRegion(self):
        """ECM地域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._ISPType = params.get("ISPType")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6CidrBlockResponse(AbstractModel):
    """AssignIpv6CidrBlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ipv6CidrBlock: 分配的 `IPv6` 网段。形如：`3402:4e00:20:1000::/56`。	
        :type Ipv6CidrBlock: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ipv6CidrBlock = None
        self._RequestId = None

    @property
    def Ipv6CidrBlock(self):
        """分配的 `IPv6` 网段。形如：`3402:4e00:20:1000::/56`。	
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

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
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._RequestId = params.get("RequestId")


class AssignIpv6CidrBlocksRequest(AbstractModel):
    """AssignIpv6CidrBlocks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。	
        :type VpcId: str
        :param _ISPTypes: 网络运营商类型 取值范围:'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
        :type ISPTypes: list of ISPTypeItem
        :param _EcmRegion: ECM地域。
        :type EcmRegion: str
        """
        self._VpcId = None
        self._ISPTypes = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """`VPC`实例`ID`，形如：`vpc-f49l6u0z`。	
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ISPTypes(self):
        """网络运营商类型 取值范围:'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
        :rtype: list of ISPTypeItem
        """
        return self._ISPTypes

    @ISPTypes.setter
    def ISPTypes(self, ISPTypes):
        self._ISPTypes = ISPTypes

    @property
    def EcmRegion(self):
        """ECM地域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        if params.get("ISPTypes") is not None:
            self._ISPTypes = []
            for item in params.get("ISPTypes"):
                obj = ISPTypeItem()
                obj._deserialize(item)
                self._ISPTypes.append(obj)
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6CidrBlocksResponse(AbstractModel):
    """AssignIpv6CidrBlocks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IPv6CidrBlockSet: IPv6网段和所属运营商。	
        :type IPv6CidrBlockSet: list of ISPIPv6CidrBlock
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IPv6CidrBlockSet = None
        self._RequestId = None

    @property
    def IPv6CidrBlockSet(self):
        """IPv6网段和所属运营商。	
        :rtype: list of ISPIPv6CidrBlock
        """
        return self._IPv6CidrBlockSet

    @IPv6CidrBlockSet.setter
    def IPv6CidrBlockSet(self, IPv6CidrBlockSet):
        self._IPv6CidrBlockSet = IPv6CidrBlockSet

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
        if params.get("IPv6CidrBlockSet") is not None:
            self._IPv6CidrBlockSet = []
            for item in params.get("IPv6CidrBlockSet"):
                obj = ISPIPv6CidrBlock()
                obj._deserialize(item)
                self._IPv6CidrBlockSet.append(obj)
        self._RequestId = params.get("RequestId")


class AssignIpv6SubnetCidrBlockRequest(AbstractModel):
    """AssignIpv6SubnetCidrBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。	
        :type VpcId: str
        :param _Ipv6SubnetCidrBlocks: 分配 `IPv6` 子网段列表。
        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock
        :param _EcmRegion: ECM地域。
        :type EcmRegion: str
        """
        self._VpcId = None
        self._Ipv6SubnetCidrBlocks = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。	
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Ipv6SubnetCidrBlocks(self):
        """分配 `IPv6` 子网段列表。
        :rtype: list of Ipv6SubnetCidrBlock
        """
        return self._Ipv6SubnetCidrBlocks

    @Ipv6SubnetCidrBlocks.setter
    def Ipv6SubnetCidrBlocks(self, Ipv6SubnetCidrBlocks):
        self._Ipv6SubnetCidrBlocks = Ipv6SubnetCidrBlocks

    @property
    def EcmRegion(self):
        """ECM地域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self._Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self._Ipv6SubnetCidrBlocks.append(obj)
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6SubnetCidrBlockResponse(AbstractModel):
    """AssignIpv6SubnetCidrBlock返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ipv6SubnetCidrBlockSet: 分配 `IPv6` 子网段列表。	
        :type Ipv6SubnetCidrBlockSet: list of Ipv6SubnetCidrBlock
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ipv6SubnetCidrBlockSet = None
        self._RequestId = None

    @property
    def Ipv6SubnetCidrBlockSet(self):
        """分配 `IPv6` 子网段列表。	
        :rtype: list of Ipv6SubnetCidrBlock
        """
        return self._Ipv6SubnetCidrBlockSet

    @Ipv6SubnetCidrBlockSet.setter
    def Ipv6SubnetCidrBlockSet(self, Ipv6SubnetCidrBlockSet):
        self._Ipv6SubnetCidrBlockSet = Ipv6SubnetCidrBlockSet

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
        if params.get("Ipv6SubnetCidrBlockSet") is not None:
            self._Ipv6SubnetCidrBlockSet = []
            for item in params.get("Ipv6SubnetCidrBlockSet"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self._Ipv6SubnetCidrBlockSet.append(obj)
        self._RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        :param _PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。与SecondaryPrivateIpAddressCount至少提供一个。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param _SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，与PrivateIpAddresses至少提供一个。内网IP地址个数总和不能超过配额数
        :type SecondaryPrivateIpAddressCount: int
        """
        self._NetworkInterfaceId = None
        self._EcmRegion = None
        self._PrivateIpAddresses = None
        self._SecondaryPrivateIpAddressCount = None

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def PrivateIpAddresses(self):
        """指定的内网IP信息，单次最多指定10个。与SecondaryPrivateIpAddressCount至少提供一个。
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def SecondaryPrivateIpAddressCount(self):
        """新申请的内网IP地址个数，与PrivateIpAddresses至少提供一个。内网IP地址个数总和不能超过配额数
        :rtype: int
        """
        return self._SecondaryPrivateIpAddressCount

    @SecondaryPrivateIpAddressCount.setter
    def SecondaryPrivateIpAddressCount(self, SecondaryPrivateIpAddressCount):
        self._SecondaryPrivateIpAddressCount = SecondaryPrivateIpAddressCount


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._EcmRegion = params.get("EcmRegion")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        self._SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivateIpAddressSet: 内网IP详细信息。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivateIpAddressSet = None
        self._RequestId = None

    @property
    def PrivateIpAddressSet(self):
        """内网IP详细信息。
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddressSet

    @PrivateIpAddressSet.setter
    def PrivateIpAddressSet(self, PrivateIpAddressSet):
        self._PrivateIpAddressSet = PrivateIpAddressSet

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
        if params.get("PrivateIpAddressSet") is not None:
            self._PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class AssistantCidr(AbstractModel):
    """VPC辅助CIDR信息。

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。形如：vpc-6v2ht8q5
        :type VpcId: str
        :param _CidrBlock: 辅助CIDR。形如：172.16.0.0/16
        :type CidrBlock: str
        :param _AssistantType: 辅助CIDR类型（0：普通辅助CIDR，1：容器辅助CIDR），默认都是0。
        :type AssistantType: int
        :param _SubnetSet: 辅助CIDR拆分的子网。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetSet: list of Subnet
        """
        self._VpcId = None
        self._CidrBlock = None
        self._AssistantType = None
        self._SubnetSet = None

    @property
    def VpcId(self):
        """VPC实例ID。形如：vpc-6v2ht8q5
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CidrBlock(self):
        """辅助CIDR。形如：172.16.0.0/16
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def AssistantType(self):
        """辅助CIDR类型（0：普通辅助CIDR，1：容器辅助CIDR），默认都是0。
        :rtype: int
        """
        return self._AssistantType

    @AssistantType.setter
    def AssistantType(self, AssistantType):
        self._AssistantType = AssistantType

    @property
    def SubnetSet(self):
        """辅助CIDR拆分的子网。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Subnet
        """
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._CidrBlock = params.get("CidrBlock")
        self._AssistantType = params.get("AssistantType")
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :type AddressId: str
        :param _InstanceId: 要绑定的实例 ID。
        :type InstanceId: str
        :param _NetworkInterfaceId: 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。
        :type NetworkInterfaceId: str
        :param _PrivateIpAddress: 要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。
        :type PrivateIpAddress: str
        """
        self._EcmRegion = None
        self._AddressId = None
        self._InstanceId = None
        self._NetworkInterfaceId = None
        self._PrivateIpAddress = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressId(self):
        """标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def InstanceId(self):
        """要绑定的实例 ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def NetworkInterfaceId(self):
        """要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddress(self):
        """要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressId = params.get("AddressId")
        self._InstanceId = params.get("InstanceId")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
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


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要绑定的安全组ID，类似esg-efil73jd，只支持绑定单个安全组。
        :type SecurityGroupIds: list of str
        :param _InstanceIds: 被绑定的实例ID，类似ein-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """要绑定的安全组ID，类似esg-efil73jd，只支持绑定单个安全组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """被绑定的实例ID，类似ein-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

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


class AttachDisksRequest(AbstractModel):
    """AttachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云服务器实例ID。云盘将被挂载到此云服务器上，通过[DescribeInstances](/document/product/213/15728)接口查询。
        :type InstanceId: str
        :param _DiskIds: 将要被挂载的弹性云盘ID。通过[DescribeDisks](/document/product/362/16315)接口查询。单次最多可挂载10块弹性云盘。
        :type DiskIds: list of str
        :param _DeleteWithInstance: 可选参数，不传该参数则仅执行挂载操作。传入`True`时，会在挂载成功后将云硬盘设置为随云主机销毁模式，仅对按量计费云硬盘有效。
        :type DeleteWithInstance: bool
        :param _AttachMode: 可选参数，用于控制云盘挂载时使用的挂载模式，目前仅对黑石裸金属机型有效。取值范围：<br><li>PF<br><li>VF
        :type AttachMode: str
        """
        self._InstanceId = None
        self._DiskIds = None
        self._DeleteWithInstance = None
        self._AttachMode = None

    @property
    def InstanceId(self):
        """云服务器实例ID。云盘将被挂载到此云服务器上，通过[DescribeInstances](/document/product/213/15728)接口查询。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskIds(self):
        """将要被挂载的弹性云盘ID。通过[DescribeDisks](/document/product/362/16315)接口查询。单次最多可挂载10块弹性云盘。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def DeleteWithInstance(self):
        """可选参数，不传该参数则仅执行挂载操作。传入`True`时，会在挂载成功后将云硬盘设置为随云主机销毁模式，仅对按量计费云硬盘有效。
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def AttachMode(self):
        """可选参数，用于控制云盘挂载时使用的挂载模式，目前仅对黑石裸金属机型有效。取值范围：<br><li>PF<br><li>VF
        :rtype: str
        """
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskIds = params.get("DiskIds")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._AttachMode = params.get("AttachMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachDisksResponse(AbstractModel):
    """AttachDisks返回参数结构体

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


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _InstanceId: 实例ID。形如：ein-r8hr2upy。
        :type InstanceId: str
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._InstanceId = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def InstanceId(self):
        """实例ID。形如：ein-r8hr2upy。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._InstanceId = params.get("InstanceId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface返回参数结构体

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


class Backend(AbstractModel):
    """负责均衡后端信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 后端服务的唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Port: 后端服务的监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param _RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RegisteredTime: str
        :param _EniId: 弹性网卡唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EniId: str
        :param _PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param _InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        """
        self._InstanceId = None
        self._Port = None
        self._Weight = None
        self._PrivateIpAddresses = None
        self._RegisteredTime = None
        self._EniId = None
        self._PublicIpAddresses = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """后端服务的唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Port(self):
        """后端服务的监听端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        """后端服务的转发权重，取值范围：[0, 100]，默认为 10。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def PrivateIpAddresses(self):
        """后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def RegisteredTime(self):
        """后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegisteredTime

    @RegisteredTime.setter
    def RegisteredTime(self, RegisteredTime):
        self._RegisteredTime = RegisteredTime

    @property
    def EniId(self):
        """弹性网卡唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def PublicIpAddresses(self):
        """后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def InstanceName(self):
        """后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._RegisteredTime = params.get("RegisteredTime")
        self._EniId = params.get("EniId")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param _Targets: 解绑目标
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        """负载均衡ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        """解绑目标
        :rtype: list of BatchTarget
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: 解绑失败的监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FailListenerIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        """解绑失败的监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

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
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ModifyList: 要批量修改权重的列表
        :type ModifyList: list of TargetsWeightRule
        """
        self._LoadBalancerId = None
        self._ModifyList = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyList(self):
        """要批量修改权重的列表
        :rtype: list of TargetsWeightRule
        """
        return self._ModifyList

    @ModifyList.setter
    def ModifyList(self, ModifyList):
        self._ModifyList = ModifyList


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self._ModifyList = []
            for item in params.get("ModifyList"):
                obj = TargetsWeightRule()
                obj._deserialize(item)
                self._ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight返回参数结构体

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


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡ID
        :type LoadBalancerId: str
        :param _Targets: 绑定目标
        :type Targets: list of BatchTarget
        """
        self._LoadBalancerId = None
        self._Targets = None

    @property
    def LoadBalancerId(self):
        """负载均衡ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Targets(self):
        """绑定目标
        :rtype: list of BatchTarget
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailListenerIdSet: 绑定失败的监听器ID，如为空表示全部绑定成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailListenerIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailListenerIdSet = None
        self._RequestId = None

    @property
    def FailListenerIdSet(self):
        """绑定失败的监听器ID，如为空表示全部绑定成功。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FailListenerIdSet

    @FailListenerIdSet.setter
    def FailListenerIdSet(self, FailListenerIdSet):
        self._FailListenerIdSet = FailListenerIdSet

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
        self._FailListenerIdSet = params.get("FailListenerIdSet")
        self._RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """负责均衡批量目标项

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _Port: 绑定端口
        :type Port: int
        :param _InstanceId: 子机ID
        :type InstanceId: str
        :param _EniIp: 弹性网卡ip
        :type EniIp: str
        :param _Weight: 子机权重，范围[0, 100]。绑定时如果不存在，则默认为10。
        :type Weight: int
        """
        self._ListenerId = None
        self._Port = None
        self._InstanceId = None
        self._EniIp = None
        self._Weight = None

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
    def Port(self):
        """绑定端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        """子机ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EniIp(self):
        """弹性网卡ip
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Weight(self):
        """子机权重，范围[0, 100]。绑定时如果不存在，则默认为10。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._EniIp = params.get("EniIp")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class City(AbstractModel):
    """城市信息

    """

    def __init__(self):
        r"""
        :param _CityId: 城市ID
        :type CityId: str
        :param _CityName: 城市名称
        :type CityName: str
        """
        self._CityId = None
        self._CityName = None

    @property
    def CityId(self):
        """城市ID
        :rtype: str
        """
        return self._CityId

    @CityId.setter
    def CityId(self, CityId):
        self._CityId = CityId

    @property
    def CityName(self):
        """城市名称
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName


    def _deserialize(self, params):
        self._CityId = params.get("CityId")
        self._CityName = params.get("CityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Country(AbstractModel):
    """国家信息

    """

    def __init__(self):
        r"""
        :param _CountryId: 国家ID
        :type CountryId: str
        :param _CountryName: 国家名称
        :type CountryName: str
        """
        self._CountryId = None
        self._CountryName = None

    @property
    def CountryId(self):
        """国家ID
        :rtype: str
        """
        return self._CountryId

    @CountryId.setter
    def CountryId(self, CountryId):
        self._CountryId = CountryId

    @property
    def CountryName(self):
        """国家名称
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName


    def _deserialize(self, params):
        self._CountryId = params.get("CountryId")
        self._CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksRequest(AbstractModel):
    """CreateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 实例所在的位置。通过该参数可以指定实例所属可用区，所属项目。若不指定项目，将在默认项目下进行创建。
        :type Placement: :class:`tencentcloud.ecm.v20190719.models.Placement`
        :param _DiskChargeType: 云硬盘计费类型。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDCPAID：独享集群付费<br>各类型价格请参考云硬盘[价格总览](/document/product/362/2413)。
        :type DiskChargeType: str
        :param _DiskType: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :type DiskType: str
        :param _DiskName: 云盘显示名称。不传则默认为“未命名”。最大长度不能超60个字节。
        :type DiskName: str
        :param _Tags: 云盘绑定的标签。
        :type Tags: list of Tag
        :param _DiskChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数指定包年包月云盘的购买时长、是否设置自动续费等属性。<br>创建预付费云盘该参数必传，创建按小时后付费云盘无需传该参数。
        :type DiskChargePrepaid: :class:`tencentcloud.ecm.v20190719.models.DiskChargePrepaid`
        :param _DiskCount: 创建云硬盘数量，不传则默认为1。单次请求最多可创建的云盘数有限制，具体参见[云硬盘使用限制](https://cloud.tencent.com/doc/product/362/5145)。
        :type DiskCount: int
        :param _ThroughputPerformance: 可选参数。使用此参数可给云硬盘购买额外的性能。<br>当前仅支持极速型云盘（CLOUD_TSSD）和增强型SSD云硬盘（CLOUD_HSSD）
        :type ThroughputPerformance: int
        :param _DiskSize: 云硬盘大小，单位为GB。<br><li>如果传入`SnapshotId`则可不传`DiskSize`，此时新建云盘的大小为快照大小<br><li>如果传入`SnapshotId`同时传入`DiskSize`，则云盘大小必须大于或等于快照大小<br><li>云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :type DiskSize: int
        :param _Shareable: 可选参数，默认为False。传入True时，云盘将创建为共享型云盘。
        :type Shareable: bool
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _Encrypt: 传入该参数用于创建加密云盘，取值固定为ENCRYPT。
        :type Encrypt: str
        :param _SnapshotId: 快照ID，如果传入则根据此快照创建云硬盘，快照类型必须为数据盘快照，可通过[DescribeSnapshots](/document/product/362/15647)接口查询快照，见输出参数DiskUsage解释。
        :type SnapshotId: str
        """
        self._Placement = None
        self._DiskChargeType = None
        self._DiskType = None
        self._DiskName = None
        self._Tags = None
        self._DiskChargePrepaid = None
        self._DiskCount = None
        self._ThroughputPerformance = None
        self._DiskSize = None
        self._Shareable = None
        self._ClientToken = None
        self._Encrypt = None
        self._SnapshotId = None

    @property
    def Placement(self):
        """实例所在的位置。通过该参数可以指定实例所属可用区，所属项目。若不指定项目，将在默认项目下进行创建。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def DiskChargeType(self):
        """云硬盘计费类型。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>CDCPAID：独享集群付费<br>各类型价格请参考云硬盘[价格总览](/document/product/362/2413)。
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def DiskType(self):
        """硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskName(self):
        """云盘显示名称。不传则默认为“未命名”。最大长度不能超60个字节。
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def Tags(self):
        """云盘绑定的标签。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DiskChargePrepaid(self):
        """预付费模式，即包年包月相关参数设置。通过该参数指定包年包月云盘的购买时长、是否设置自动续费等属性。<br>创建预付费云盘该参数必传，创建按小时后付费云盘无需传该参数。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DiskChargePrepaid`
        """
        return self._DiskChargePrepaid

    @DiskChargePrepaid.setter
    def DiskChargePrepaid(self, DiskChargePrepaid):
        self._DiskChargePrepaid = DiskChargePrepaid

    @property
    def DiskCount(self):
        """创建云硬盘数量，不传则默认为1。单次请求最多可创建的云盘数有限制，具体参见[云硬盘使用限制](https://cloud.tencent.com/doc/product/362/5145)。
        :rtype: int
        """
        return self._DiskCount

    @DiskCount.setter
    def DiskCount(self, DiskCount):
        self._DiskCount = DiskCount

    @property
    def ThroughputPerformance(self):
        """可选参数。使用此参数可给云硬盘购买额外的性能。<br>当前仅支持极速型云盘（CLOUD_TSSD）和增强型SSD云硬盘（CLOUD_HSSD）
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def DiskSize(self):
        """云硬盘大小，单位为GB。<br><li>如果传入`SnapshotId`则可不传`DiskSize`，此时新建云盘的大小为快照大小<br><li>如果传入`SnapshotId`同时传入`DiskSize`，则云盘大小必须大于或等于快照大小<br><li>云盘大小取值范围参见云硬盘[产品分类](/document/product/362/2353)的说明。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def Shareable(self):
        """可选参数，默认为False。传入True时，云盘将创建为共享型云盘。
        :rtype: bool
        """
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def Encrypt(self):
        """传入该参数用于创建加密云盘，取值固定为ENCRYPT。
        :rtype: str
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def SnapshotId(self):
        """快照ID，如果传入则根据此快照创建云硬盘，快照类型必须为数据盘快照，可通过[DescribeSnapshots](/document/product/362/15647)接口查询快照，见输出参数DiskUsage解释。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._DiskChargeType = params.get("DiskChargeType")
        self._DiskType = params.get("DiskType")
        self._DiskName = params.get("DiskName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("DiskChargePrepaid") is not None:
            self._DiskChargePrepaid = DiskChargePrepaid()
            self._DiskChargePrepaid._deserialize(params.get("DiskChargePrepaid"))
        self._DiskCount = params.get("DiskCount")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._DiskSize = params.get("DiskSize")
        self._Shareable = params.get("Shareable")
        self._ClientToken = params.get("ClientToken")
        self._Encrypt = params.get("Encrypt")
        self._SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDisksResponse(AbstractModel):
    """CreateDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIdSet: 创建的云硬盘ID列表。
        :type DiskIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiskIdSet = None
        self._RequestId = None

    @property
    def DiskIdSet(self):
        """创建的云硬盘ID列表。
        :rtype: list of str
        """
        return self._DiskIdSet

    @DiskIdSet.setter
    def DiskIdSet(self, DiskIdSet):
        self._DiskIdSet = DiskIdSet

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
        self._DiskIdSet = params.get("DiskIdSet")
        self._RequestId = params.get("RequestId")


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: HAVIP所在私有网络ID。
        :type VpcId: str
        :param _SubnetId: HAVIP所在子网ID。
        :type SubnetId: str
        :param _HaVipName: HAVIP名称。
        :type HaVipName: str
        :param _Vip: 指定虚拟IP地址，必须在VPC网段内且未被占用。不指定则自动分配。
        :type Vip: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._HaVipName = None
        self._Vip = None

    @property
    def VpcId(self):
        """HAVIP所在私有网络ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """HAVIP所在子网ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def HaVipName(self):
        """HAVIP名称。
        :rtype: str
        """
        return self._HaVipName

    @HaVipName.setter
    def HaVipName(self, HaVipName):
        self._HaVipName = HaVipName

    @property
    def Vip(self):
        """指定虚拟IP地址，必须在VPC网段内且未被占用。不指定则自动分配。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._HaVipName = params.get("HaVipName")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HaVip: HAVIP对象。
        :type HaVip: :class:`tencentcloud.ecm.v20190719.models.HaVip`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HaVip = None
        self._RequestId = None

    @property
    def HaVip(self):
        """HAVIP对象。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HaVip`
        """
        return self._HaVip

    @HaVip.setter
    def HaVip(self, HaVip):
        self._HaVip = HaVip

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
        if params.get("HaVip") is not None:
            self._HaVip = HaVip()
            self._HaVip._deserialize(params.get("HaVip"))
        self._RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageName: 镜像名称。
        :type ImageName: str
        :param _InstanceId: 需要制作镜像的实例ID。
        :type InstanceId: str
        :param _ImageDescription: 镜像描述。
        :type ImageDescription: str
        :param _ForcePoweroff: 是否执行强制关机以制作镜像。取值范围：
TRUE：表示自动关机后制作镜像
FALSE：表示开机状态制作，目前不支持，需要先手动关机
默认取值：FALSE。
        :type ForcePoweroff: str
        """
        self._ImageName = None
        self._InstanceId = None
        self._ImageDescription = None
        self._ForcePoweroff = None

    @property
    def ImageName(self):
        """镜像名称。
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def InstanceId(self):
        """需要制作镜像的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageDescription(self):
        """镜像描述。
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ForcePoweroff(self):
        """是否执行强制关机以制作镜像。取值范围：
TRUE：表示自动关机后制作镜像
FALSE：表示开机状态制作，目前不支持，需要先手动关机
默认取值：FALSE。
        :rtype: str
        """
        return self._ForcePoweroff

    @ForcePoweroff.setter
    def ForcePoweroff(self, ForcePoweroff):
        self._ForcePoweroff = ForcePoweroff


    def _deserialize(self, params):
        self._ImageName = params.get("ImageName")
        self._InstanceId = params.get("InstanceId")
        self._ImageDescription = params.get("ImageDescription")
        self._ForcePoweroff = params.get("ForcePoweroff")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务id
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


class CreateKeyPairRequest(AbstractModel):
    """CreateKeyPair请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyName: 密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :type KeyName: str
        """
        self._KeyName = None

    @property
    def KeyName(self):
        """密钥对名称，可由数字，字母和下划线组成，长度不超过25个字符。
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName


    def _deserialize(self, params):
        self._KeyName = params.get("KeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyPairResponse(AbstractModel):
    """CreateKeyPair返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyPair: 密钥对信息。
        :type KeyPair: :class:`tencentcloud.ecm.v20190719.models.KeyPair`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyPair = None
        self._RequestId = None

    @property
    def KeyPair(self):
        """密钥对信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.KeyPair`
        """
        return self._KeyPair

    @KeyPair.setter
    def KeyPair(self, KeyPair):
        self._KeyPair = KeyPair

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
        if params.get("KeyPair") is not None:
            self._KeyPair = KeyPair()
            self._KeyPair._deserialize(params.get("KeyPair"))
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _Ports: 要将监听器创建到哪些端口，每个端口对应一个新的监听器
        :type Ports: list of int
        :param _Protocol: 监听器协议： TCP | UDP
        :type Protocol: str
        :param _ListenerNames: 要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数
        :type ListenerNames: list of str
        :param _HealthCheck: 健康检查相关参数
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param _SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param _Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :type Scheduler: str
        :param _SessionType: 会话保持类型。不传或传NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。QUIC_CID只支持UDP协议。
        :type SessionType: str
        :param _EndPorts: 批量端口段的结束端口，必须和Ports长度一样。
        :type EndPorts: list of int
        """
        self._LoadBalancerId = None
        self._Ports = None
        self._Protocol = None
        self._ListenerNames = None
        self._HealthCheck = None
        self._SessionExpireTime = None
        self._Scheduler = None
        self._SessionType = None
        self._EndPorts = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Ports(self):
        """要将监听器创建到哪些端口，每个端口对应一个新的监听器
        :rtype: list of int
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Protocol(self):
        """监听器协议： TCP | UDP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ListenerNames(self):
        """要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数
        :rtype: list of str
        """
        return self._ListenerNames

    @ListenerNames.setter
    def ListenerNames(self, ListenerNames):
        self._ListenerNames = ListenerNames

    @property
    def HealthCheck(self):
        """健康检查相关参数
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def SessionExpireTime(self):
        """会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :rtype: int
        """
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def Scheduler(self):
        """监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionType(self):
        """会话保持类型。不传或传NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。QUIC_CID只支持UDP协议。
        :rtype: str
        """
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def EndPorts(self):
        """批量端口段的结束端口，必须和Ports长度一样。
        :rtype: list of int
        """
        return self._EndPorts

    @EndPorts.setter
    def EndPorts(self, EndPorts):
        self._EndPorts = EndPorts


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._Ports = params.get("Ports")
        self._Protocol = params.get("Protocol")
        self._ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._Scheduler = params.get("Scheduler")
        self._SessionType = params.get("SessionType")
        self._EndPorts = params.get("EndPorts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 创建的监听器的唯一标识数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerIds = None
        self._RequestId = None

    @property
    def ListenerIds(self):
        """创建的监听器的唯一标识数组
注意：此字段可能返回 null，表示取不到有效值。
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


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM区域，形如ap-xian-ecm。
        :type EcmRegion: str
        :param _LoadBalancerType: 负载均衡实例的网络类型。目前只支持传入OPEN，表示公网属性。
        :type LoadBalancerType: str
        :param _VipIsp: CMCC | CTCC | CUCC，分别对应 移动 | 电信 | 联通。
        :type VipIsp: str
        :param _LoadBalancerName: 负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-50 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _VpcId: 负载均衡后端目标设备所属的网络 ID，如vpc-12345678。
        :type VpcId: str
        :param _Number: 创建负载均衡的个数，默认值 1。
        :type Number: int
        :param _InternetAccessible: 负载均衡的带宽限制等信息。
        :type InternetAccessible: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        :param _SecurityGroups: 安全组。
        :type SecurityGroups: list of str
        :param _AddressIPVersion: 仅适用于公网负载均衡。IP版本，可取值：IPV4、IPv6FullChain，默认值 IPV4。说明：取值为IPv6FullChain，表示为IPv6版本。
        :type AddressIPVersion: str
        :param _SubnetId: 在购买IPV6负载均衡实例的情况下，必须指定子网 ID, 此参数必填；IPv4实例不支持该参数。
        :type SubnetId: str
        """
        self._EcmRegion = None
        self._LoadBalancerType = None
        self._VipIsp = None
        self._LoadBalancerName = None
        self._VpcId = None
        self._Number = None
        self._InternetAccessible = None
        self._Tags = None
        self._SecurityGroups = None
        self._AddressIPVersion = None
        self._SubnetId = None

    @property
    def EcmRegion(self):
        """ECM区域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def LoadBalancerType(self):
        """负载均衡实例的网络类型。目前只支持传入OPEN，表示公网属性。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def VipIsp(self):
        """CMCC | CTCC | CUCC，分别对应 移动 | 电信 | 联通。
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def LoadBalancerName(self):
        """负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-50 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def VpcId(self):
        """负载均衡后端目标设备所属的网络 ID，如vpc-12345678。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Number(self):
        """创建负载均衡的个数，默认值 1。
        :rtype: int
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def InternetAccessible(self):
        """负载均衡的带宽限制等信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        """
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def Tags(self):
        """标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SecurityGroups(self):
        """安全组。
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def AddressIPVersion(self):
        """仅适用于公网负载均衡。IP版本，可取值：IPV4、IPv6FullChain，默认值 IPV4。说明：取值为IPv6FullChain，表示为IPv6版本。
        :rtype: str
        """
        return self._AddressIPVersion

    @AddressIPVersion.setter
    def AddressIPVersion(self, AddressIPVersion):
        self._AddressIPVersion = AddressIPVersion

    @property
    def SubnetId(self):
        """在购买IPV6负载均衡实例的情况下，必须指定子网 ID, 此参数必填；IPv4实例不支持该参数。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._VipIsp = params.get("VipIsp")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._VpcId = params.get("VpcId")
        self._Number = params.get("Number")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = LoadBalancerInternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SecurityGroups = params.get("SecurityGroups")
        self._AddressIPVersion = params.get("AddressIPVersion")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 由负载均衡实例ID组成的数组
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerIds = None
        self._RequestId = None

    @property
    def LoadBalancerIds(self):
        """由负载均衡实例ID组成的数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

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
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._RequestId = params.get("RequestId")


class CreateModuleRequest(AbstractModel):
    """CreateModule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleName: 模块名称，如视频直播模块。限制：模块名称不得以空格开头，长度不得超过60个字符。
        :type ModuleName: str
        :param _DefaultBandWidth: 默认带宽，单位：Mbps。范围不得超过带宽上下限，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :type DefaultBandWidth: int
        :param _DefaultImageId: 默认镜像。
        :type DefaultImageId: str
        :param _InstanceType: 机型ID。
        :type InstanceType: str
        :param _DefaultSystemDiskSize: 默认系统盘大小，单位：GB，默认大小为50GB。范围不得超过系统盘上下限制，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :type DefaultSystemDiskSize: int
        :param _DefaultDataDiskSize: 默认数据盘大小，单位：GB。范围不得超过数据盘范围大小，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :type DefaultDataDiskSize: int
        :param _CloseIpDirect: 是否关闭IP直通。取值范围：
true：表示关闭IP直通
false：表示开通IP直通
        :type CloseIpDirect: bool
        :param _TagSpecification: 标签列表。
        :type TagSpecification: list of TagSpecification
        :param _SecurityGroups: 模块默认安全组列表
        :type SecurityGroups: list of str
        :param _DefaultBandWidthIn: 默认入带宽，单位：Mbps。范围不得超过带宽上下限，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :type DefaultBandWidthIn: int
        :param _DisableWanIp: 是否禁止分配外网IP
        :type DisableWanIp: bool
        :param _SystemDisk: 系统盘信息。
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: 数据盘信息。
        :type DataDisks: list of DataDisk
        """
        self._ModuleName = None
        self._DefaultBandWidth = None
        self._DefaultImageId = None
        self._InstanceType = None
        self._DefaultSystemDiskSize = None
        self._DefaultDataDiskSize = None
        self._CloseIpDirect = None
        self._TagSpecification = None
        self._SecurityGroups = None
        self._DefaultBandWidthIn = None
        self._DisableWanIp = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ModuleName(self):
        """模块名称，如视频直播模块。限制：模块名称不得以空格开头，长度不得超过60个字符。
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName

    @property
    def DefaultBandWidth(self):
        """默认带宽，单位：Mbps。范围不得超过带宽上下限，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :rtype: int
        """
        return self._DefaultBandWidth

    @DefaultBandWidth.setter
    def DefaultBandWidth(self, DefaultBandWidth):
        self._DefaultBandWidth = DefaultBandWidth

    @property
    def DefaultImageId(self):
        """默认镜像。
        :rtype: str
        """
        return self._DefaultImageId

    @DefaultImageId.setter
    def DefaultImageId(self, DefaultImageId):
        self._DefaultImageId = DefaultImageId

    @property
    def InstanceType(self):
        """机型ID。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DefaultSystemDiskSize(self):
        """默认系统盘大小，单位：GB，默认大小为50GB。范围不得超过系统盘上下限制，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :rtype: int
        """
        return self._DefaultSystemDiskSize

    @DefaultSystemDiskSize.setter
    def DefaultSystemDiskSize(self, DefaultSystemDiskSize):
        self._DefaultSystemDiskSize = DefaultSystemDiskSize

    @property
    def DefaultDataDiskSize(self):
        """默认数据盘大小，单位：GB。范围不得超过数据盘范围大小，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :rtype: int
        """
        return self._DefaultDataDiskSize

    @DefaultDataDiskSize.setter
    def DefaultDataDiskSize(self, DefaultDataDiskSize):
        self._DefaultDataDiskSize = DefaultDataDiskSize

    @property
    def CloseIpDirect(self):
        """是否关闭IP直通。取值范围：
true：表示关闭IP直通
false：表示开通IP直通
        :rtype: bool
        """
        return self._CloseIpDirect

    @CloseIpDirect.setter
    def CloseIpDirect(self, CloseIpDirect):
        self._CloseIpDirect = CloseIpDirect

    @property
    def TagSpecification(self):
        """标签列表。
        :rtype: list of TagSpecification
        """
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def SecurityGroups(self):
        """模块默认安全组列表
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups

    @property
    def DefaultBandWidthIn(self):
        """默认入带宽，单位：Mbps。范围不得超过带宽上下限，详看[DescribeConfig](https://cloud.tencent.com/document/product/1108/42572)。
        :rtype: int
        """
        return self._DefaultBandWidthIn

    @DefaultBandWidthIn.setter
    def DefaultBandWidthIn(self, DefaultBandWidthIn):
        self._DefaultBandWidthIn = DefaultBandWidthIn

    @property
    def DisableWanIp(self):
        """是否禁止分配外网IP
        :rtype: bool
        """
        return self._DisableWanIp

    @DisableWanIp.setter
    def DisableWanIp(self, DisableWanIp):
        self._DisableWanIp = DisableWanIp

    @property
    def SystemDisk(self):
        """系统盘信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """数据盘信息。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        self._ModuleName = params.get("ModuleName")
        self._DefaultBandWidth = params.get("DefaultBandWidth")
        self._DefaultImageId = params.get("DefaultImageId")
        self._InstanceType = params.get("InstanceType")
        self._DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self._DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self._CloseIpDirect = params.get("CloseIpDirect")
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._SecurityGroups = params.get("SecurityGroups")
        self._DefaultBandWidthIn = params.get("DefaultBandWidthIn")
        self._DisableWanIp = params.get("DisableWanIp")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModuleResponse(AbstractModel):
    """CreateModule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID，创建模块成功后分配给该模块的ID。
        :type ModuleId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModuleId = None
        self._RequestId = None

    @property
    def ModuleId(self):
        """模块ID，创建模块成功后分配给该模块的ID。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

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
        self._ModuleId = params.get("ModuleId")
        self._RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param _NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。
        :type NetworkInterfaceName: str
        :param _SubnetId: 弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。
        :type SubnetId: str
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        :param _NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。
        :type NetworkInterfaceDescription: str
        :param _SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，内网IP地址个数总和不能超过配额数。
        :type SecondaryPrivateIpAddressCount: int
        :param _SecurityGroupIds: 指定绑定的安全组，例如：['sg-1dd51d']。
        :type SecurityGroupIds: list of str
        :param _PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param _Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self._VpcId = None
        self._NetworkInterfaceName = None
        self._SubnetId = None
        self._EcmRegion = None
        self._NetworkInterfaceDescription = None
        self._SecondaryPrivateIpAddressCount = None
        self._SecurityGroupIds = None
        self._PrivateIpAddresses = None
        self._Tags = None

    @property
    def VpcId(self):
        """VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def NetworkInterfaceName(self):
        """弹性网卡名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._NetworkInterfaceName

    @NetworkInterfaceName.setter
    def NetworkInterfaceName(self, NetworkInterfaceName):
        self._NetworkInterfaceName = NetworkInterfaceName

    @property
    def SubnetId(self):
        """弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceDescription(self):
        """弹性网卡描述，可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._NetworkInterfaceDescription

    @NetworkInterfaceDescription.setter
    def NetworkInterfaceDescription(self, NetworkInterfaceDescription):
        self._NetworkInterfaceDescription = NetworkInterfaceDescription

    @property
    def SecondaryPrivateIpAddressCount(self):
        """新申请的内网IP地址个数，内网IP地址个数总和不能超过配额数。
        :rtype: int
        """
        return self._SecondaryPrivateIpAddressCount

    @SecondaryPrivateIpAddressCount.setter
    def SecondaryPrivateIpAddressCount(self, SecondaryPrivateIpAddressCount):
        self._SecondaryPrivateIpAddressCount = SecondaryPrivateIpAddressCount

    @property
    def SecurityGroupIds(self):
        """指定绑定的安全组，例如：['sg-1dd51d']。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def PrivateIpAddresses(self):
        """指定的内网IP信息，单次最多指定10个。
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Tags(self):
        """指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._NetworkInterfaceName = params.get("NetworkInterfaceName")
        self._SubnetId = params.get("SubnetId")
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self._SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
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
        


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterface: 弹性网卡实例。
        :type NetworkInterface: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetworkInterface = None
        self._RequestId = None

    @property
    def NetworkInterface(self):
        """弹性网卡实例。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`
        """
        return self._NetworkInterface

    @NetworkInterface.setter
    def NetworkInterface(self, NetworkInterface):
        self._NetworkInterface = NetworkInterface

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
        if params.get("NetworkInterface") is not None:
            self._NetworkInterface = NetworkInterface()
            self._NetworkInterface._deserialize(params.get("NetworkInterface"))
        self._RequestId = params.get("RequestId")


class CreateRouteTableRequest(AbstractModel):
    """CreateRouteTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param _RouteTableName: 路由表名称，最大长度不能超过60个字节。
        :type RouteTableName: str
        :param _EcmRegion: ecm地域
        :type EcmRegion: str
        """
        self._VpcId = None
        self._RouteTableName = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def RouteTableName(self):
        """路由表名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def EcmRegion(self):
        """ecm地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._RouteTableName = params.get("RouteTableName")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTable: 路由表对象
        :type RouteTable: :class:`tencentcloud.ecm.v20190719.models.RouteTable`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RouteTable = None
        self._RequestId = None

    @property
    def RouteTable(self):
        """路由表对象
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RouteTable`
        """
        return self._RouteTable

    @RouteTable.setter
    def RouteTable(self, RouteTable):
        self._RouteTable = RouteTable

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
        if params.get("RouteTable") is not None:
            self._RouteTable = RouteTable()
            self._RouteTable._deserialize(params.get("RouteTable"))
        self._RequestId = params.get("RequestId")


class CreateRoutesRequest(AbstractModel):
    """CreateRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID。
        :type RouteTableId: str
        :param _Routes: 要创建的路由策略对象。
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """路由表实例ID。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def Routes(self):
        """要创建的路由策略对象。
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 新增的实例个数。
        :type TotalCount: int
        :param _RouteTableSet: 路由表对象。
        :type RouteTableSet: list of RouteTable
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteTableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """新增的实例个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteTableSet(self):
        """路由表对象。
        :rtype: list of RouteTable
        """
        return self._RouteTableSet

    @RouteTableSet.setter
    def RouteTableSet(self, RouteTableSet):
        self._RouteTableSet = RouteTableSet

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
        if params.get("RouteTableSet") is not None:
            self._RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self._RouteTableSet.append(obj)
        self._RequestId = params.get("RequestId")


class CreateSecurityGroupPoliciesRequest(AbstractModel):
    """CreateSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: 安全组规则集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """安全组规则集合。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies返回参数结构体

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


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 安全组名称，可任意命名，但不得超过60个字符。
        :type GroupName: str
        :param _GroupDescription: 安全组备注，最多100个字符。
        :type GroupDescription: str
        :param _Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        """
        self._GroupName = None
        self._GroupDescription = None
        self._Tags = None

    @property
    def GroupName(self):
        """安全组名称，可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupDescription(self):
        """安全组备注，最多100个字符。
        :rtype: str
        """
        return self._GroupDescription

    @GroupDescription.setter
    def GroupDescription(self, GroupDescription):
        self._GroupDescription = GroupDescription

    @property
    def Tags(self):
        """指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._GroupDescription = params.get("GroupDescription")
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
        


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroup: 安全组对象。
        :type SecurityGroup: :class:`tencentcloud.ecm.v20190719.models.SecurityGroup`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroup = None
        self._RequestId = None

    @property
    def SecurityGroup(self):
        """安全组对象。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroup`
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

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
        if params.get("SecurityGroup") is not None:
            self._SecurityGroup = SecurityGroup()
            self._SecurityGroup._deserialize(params.get("SecurityGroup"))
        self._RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param _SubnetName: 子网名称，最大长度不能超过60个字节。
        :type SubnetName: str
        :param _CidrBlock: 子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。
        :type CidrBlock: str
        :param _Zone: 子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。
        :type Zone: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        :param _IPv6CidrBlock: IPv6 CIDR
        :type IPv6CidrBlock: str
        """
        self._VpcId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._Zone = None
        self._EcmRegion = None
        self._Tags = None
        self._IPv6CidrBlock = None

    @property
    def VpcId(self):
        """待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetName(self):
        """子网名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        """子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Zone(self):
        """子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Tags(self):
        """指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IPv6CidrBlock(self):
        """IPv6 CIDR
        :rtype: str
        """
        return self._IPv6CidrBlock

    @IPv6CidrBlock.setter
    def IPv6CidrBlock(self, IPv6CidrBlock):
        self._IPv6CidrBlock = IPv6CidrBlock


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._Zone = params.get("Zone")
        self._EcmRegion = params.get("EcmRegion")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IPv6CidrBlock = params.get("IPv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Subnet: 子网对象。
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Subnet = None
        self._RequestId = None

    @property
    def Subnet(self):
        """子网对象。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

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
        if params.get("Subnet") is not None:
            self._Subnet = Subnet()
            self._Subnet._deserialize(params.get("Subnet"))
        self._RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcName: vpc名称，最大长度不能超过60个字节。
        :type VpcName: str
        :param _CidrBlock: vpc的cidr，只能为10.*.0.0/16，172.[16-31].0.0/16，192.168.0.0/16这三个内网网段内。
        :type CidrBlock: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _EnableMulticast: 是否开启组播。true: 开启, false: 不开启。暂不支持
        :type EnableMulticast: str
        :param _DnsServers: DNS地址，最多支持4个，暂不支持
        :type DnsServers: list of str
        :param _DomainName: 域名，暂不支持
        :type DomainName: str
        :param _Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :type Tags: list of Tag
        :param _Description: 描述信息
        :type Description: str
        :param _ISPTypes: 网络运营商类型 取值范围:'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
        :type ISPTypes: list of ISPTypeItem
        """
        self._VpcName = None
        self._CidrBlock = None
        self._EcmRegion = None
        self._EnableMulticast = None
        self._DnsServers = None
        self._DomainName = None
        self._Tags = None
        self._Description = None
        self._ISPTypes = None

    @property
    def VpcName(self):
        """vpc名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def CidrBlock(self):
        """vpc的cidr，只能为10.*.0.0/16，172.[16-31].0.0/16，192.168.0.0/16这三个内网网段内。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def EnableMulticast(self):
        """是否开启组播。true: 开启, false: 不开启。暂不支持
        :rtype: str
        """
        return self._EnableMulticast

    @EnableMulticast.setter
    def EnableMulticast(self, EnableMulticast):
        self._EnableMulticast = EnableMulticast

    @property
    def DnsServers(self):
        """DNS地址，最多支持4个，暂不支持
        :rtype: list of str
        """
        return self._DnsServers

    @DnsServers.setter
    def DnsServers(self, DnsServers):
        self._DnsServers = DnsServers

    @property
    def DomainName(self):
        """域名，暂不支持
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Tags(self):
        """指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        """描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ISPTypes(self):
        """网络运营商类型 取值范围:'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
        :rtype: list of ISPTypeItem
        """
        return self._ISPTypes

    @ISPTypes.setter
    def ISPTypes(self, ISPTypes):
        self._ISPTypes = ISPTypes


    def _deserialize(self, params):
        self._VpcName = params.get("VpcName")
        self._CidrBlock = params.get("CidrBlock")
        self._EcmRegion = params.get("EcmRegion")
        self._EnableMulticast = params.get("EnableMulticast")
        self._DnsServers = params.get("DnsServers")
        self._DomainName = params.get("DomainName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        if params.get("ISPTypes") is not None:
            self._ISPTypes = []
            for item in params.get("ISPTypes"):
                obj = ISPTypeItem()
                obj._deserialize(item)
                self._ISPTypes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Vpc: Vpc对象。
        :type Vpc: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Vpc = None
        self._RequestId = None

    @property
    def Vpc(self):
        """Vpc对象。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`
        """
        return self._Vpc

    @Vpc.setter
    def Vpc(self, Vpc):
        self._Vpc = Vpc

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
        if params.get("Vpc") is not None:
            self._Vpc = VpcInfo()
            self._Vpc._deserialize(params.get("Vpc"))
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskSize: 数据盘大小。单位GB。
        :type DiskSize: int
        :param _DiskType: 数据盘类型，取值范围：
- LOCAL_BASIC：本地硬盘
- CLOUD_PREMIUM：高性能云硬盘

默认取值： LOCAL_BASIC。
        :type DiskType: str
        """
        self._DiskSize = None
        self._DiskType = None

    @property
    def DiskSize(self):
        """数据盘大小。单位GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        """数据盘类型，取值范围：
- LOCAL_BASIC：本地硬盘
- CLOUD_PREMIUM：高性能云硬盘

默认取值： LOCAL_BASIC。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HaVipId: HAVIP唯一ID，形如：havip-9o233uri。
        :type HaVipId: str
        """
        self._HaVipId = None

    @property
    def HaVipId(self):
        """HAVIP唯一ID，形如：havip-9o233uri。
        :rtype: str
        """
        return self._HaVipId

    @HaVipId.setter
    def HaVipId(self, HaVipId):
        self._HaVipId = HaVipId


    def _deserialize(self, params):
        self._HaVipId = params.get("HaVipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip返回参数结构体

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


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageIDSet: 镜像ID列表。
        :type ImageIDSet: list of str
        """
        self._ImageIDSet = None

    @property
    def ImageIDSet(self):
        """镜像ID列表。
        :rtype: list of str
        """
        return self._ImageIDSet

    @ImageIDSet.setter
    def ImageIDSet(self, ImageIDSet):
        self._ImageIDSet = ImageIDSet


    def _deserialize(self, params):
        self._ImageIDSet = params.get("ImageIDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage返回参数结构体

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


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerId: 要删除的监听器 ID
        :type ListenerId: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """要删除的监听器 ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener返回参数结构体

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


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerIds: 指定删除的监听器ID数组，若不填则删除负载均衡的所有监听器
        :type ListenerIds: list of str
        """
        self._LoadBalancerId = None
        self._ListenerIds = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        """指定删除的监听器ID数组，若不填则删除负载均衡的所有监听器
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners返回参数结构体

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


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 要删除的负载均衡实例 ID数组，数组大小最大支持20
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        """要删除的负载均衡实例 ID数组，数组大小最大支持20
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回参数结构体

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


class DeleteModuleRequest(AbstractModel):
    """DeleteModule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID。如：em-qn46snq8
        :type ModuleId: str
        """
        self._ModuleId = None

    @property
    def ModuleId(self):
        """模块ID。如：em-qn46snq8
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModuleResponse(AbstractModel):
    """DeleteModule返回参数结构体

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


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface返回参数结构体

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


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c
        :type RouteTableId: str
        """
        self._RouteTableId = None

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-azd4dt1c
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable返回参数结构体

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


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param _Routes: 路由策略对象。
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """路由表唯一ID。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def Routes(self):
        """路由策略对象。
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes返回参数结构体

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


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: 安全组规则集合。一个请求中只能删除单个方向的一条或多条规则。支持指定索引（PolicyIndex） 匹配删除和安全组规则匹配删除两种方式，一个请求中只能使用一种匹配方式。
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """安全组规则集合。一个请求中只能删除单个方向的一条或多条规则。支持指定索引（PolicyIndex） 匹配删除和安全组规则匹配删除两种方式，一个请求中只能使用一种匹配方式。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies返回参数结构体

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


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        """
        self._SecurityGroupId = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup返回参数结构体

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


class DeleteSnapshotsRequest(AbstractModel):
    """DeleteSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 要删除的快照ID列表，可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :type SnapshotIds: list of str
        :param _DeleteBindImages: 是否强制删除快照关联的镜像
        :type DeleteBindImages: bool
        """
        self._SnapshotIds = None
        self._DeleteBindImages = None

    @property
    def SnapshotIds(self):
        """要删除的快照ID列表，可通过[DescribeSnapshots](/document/product/362/15647)查询。
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def DeleteBindImages(self):
        """是否强制删除快照关联的镜像
        :rtype: bool
        """
        return self._DeleteBindImages

    @DeleteBindImages.setter
    def DeleteBindImages(self, DeleteBindImages):
        self._DeleteBindImages = DeleteBindImages


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        self._DeleteBindImages = params.get("DeleteBindImages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSnapshotsResponse(AbstractModel):
    """DeleteSnapshots返回参数结构体

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


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。
        :type SubnetId: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self._SubnetId = None
        self._EcmRegion = None

    @property
    def SubnetId(self):
        """子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回参数结构体

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


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self._VpcId = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc返回参数结构体

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


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self._EcmRegion = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaSet: 账户 EIP 配额信息。
        :type QuotaSet: list of EipQuota
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QuotaSet = None
        self._RequestId = None

    @property
    def QuotaSet(self):
        """账户 EIP 配额信息。
        :rtype: list of EipQuota
        """
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

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
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = EipQuota()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressIds: 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：eip-11112222。参数不支持同时指定AddressIds和Filters。
        :type AddressIds: list of str
        :param _Filters: 每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定AddressIds和Filters。详细的过滤条件如下：
address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。
address-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。
address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。
address-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。取值范围：详见EIP状态列表。
instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。
private-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。
network-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。
is-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._EcmRegion = None
        self._AddressIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressIds(self):
        """标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：eip-11112222。参数不支持同时指定AddressIds和Filters。
        :rtype: list of str
        """
        return self._AddressIds

    @AddressIds.setter
    def AddressIds(self, AddressIds):
        self._AddressIds = AddressIds

    @property
    def Filters(self):
        """每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定AddressIds和Filters。详细的过滤条件如下：
address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。
address-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。
address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。
address-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。取值范围：详见EIP状态列表。
instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。
private-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。
network-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。
is-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressIds = params.get("AddressIds")
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
        


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的 EIP 数量。
        :type TotalCount: int
        :param _AddressSet: EIP 详细信息列表。
        :type AddressSet: list of Address
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AddressSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的 EIP 数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AddressSet(self):
        """EIP 详细信息列表。
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

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
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBaseOverviewRequest(AbstractModel):
    """DescribeBaseOverview请求参数结构体

    """


class DescribeBaseOverviewResponse(AbstractModel):
    """DescribeBaseOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleNum: 模块数量，单位：个
        :type ModuleNum: int
        :param _NodeNum: 节点数量，单位：个
        :type NodeNum: int
        :param _VcpuNum: cpu核数，单位：个
        :type VcpuNum: int
        :param _MemoryNum: 内存大小，单位：G
        :type MemoryNum: int
        :param _StorageNum: 硬盘大小，单位：G
        :type StorageNum: int
        :param _NetworkNum: 昨日网络峰值,单位：M
        :type NetworkNum: int
        :param _InstanceNum: 实例数量，单位：台
        :type InstanceNum: int
        :param _RunningNum: 运行中数量，单位：台
        :type RunningNum: int
        :param _IsolationNum: 安全隔离数量，单位：台
        :type IsolationNum: int
        :param _ExpiredNum: 过期实例数量，单位：台
        :type ExpiredNum: int
        :param _WillExpireNum: 即将过期实例数量，单位：台
        :type WillExpireNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModuleNum = None
        self._NodeNum = None
        self._VcpuNum = None
        self._MemoryNum = None
        self._StorageNum = None
        self._NetworkNum = None
        self._InstanceNum = None
        self._RunningNum = None
        self._IsolationNum = None
        self._ExpiredNum = None
        self._WillExpireNum = None
        self._RequestId = None

    @property
    def ModuleNum(self):
        """模块数量，单位：个
        :rtype: int
        """
        return self._ModuleNum

    @ModuleNum.setter
    def ModuleNum(self, ModuleNum):
        self._ModuleNum = ModuleNum

    @property
    def NodeNum(self):
        """节点数量，单位：个
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def VcpuNum(self):
        """cpu核数，单位：个
        :rtype: int
        """
        return self._VcpuNum

    @VcpuNum.setter
    def VcpuNum(self, VcpuNum):
        self._VcpuNum = VcpuNum

    @property
    def MemoryNum(self):
        """内存大小，单位：G
        :rtype: int
        """
        return self._MemoryNum

    @MemoryNum.setter
    def MemoryNum(self, MemoryNum):
        self._MemoryNum = MemoryNum

    @property
    def StorageNum(self):
        """硬盘大小，单位：G
        :rtype: int
        """
        return self._StorageNum

    @StorageNum.setter
    def StorageNum(self, StorageNum):
        self._StorageNum = StorageNum

    @property
    def NetworkNum(self):
        """昨日网络峰值,单位：M
        :rtype: int
        """
        return self._NetworkNum

    @NetworkNum.setter
    def NetworkNum(self, NetworkNum):
        self._NetworkNum = NetworkNum

    @property
    def InstanceNum(self):
        """实例数量，单位：台
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum

    @property
    def RunningNum(self):
        """运行中数量，单位：台
        :rtype: int
        """
        return self._RunningNum

    @RunningNum.setter
    def RunningNum(self, RunningNum):
        self._RunningNum = RunningNum

    @property
    def IsolationNum(self):
        """安全隔离数量，单位：台
        :rtype: int
        """
        return self._IsolationNum

    @IsolationNum.setter
    def IsolationNum(self, IsolationNum):
        self._IsolationNum = IsolationNum

    @property
    def ExpiredNum(self):
        """过期实例数量，单位：台
        :rtype: int
        """
        return self._ExpiredNum

    @ExpiredNum.setter
    def ExpiredNum(self, ExpiredNum):
        self._ExpiredNum = ExpiredNum

    @property
    def WillExpireNum(self):
        """即将过期实例数量，单位：台
        :rtype: int
        """
        return self._WillExpireNum

    @WillExpireNum.setter
    def WillExpireNum(self, WillExpireNum):
        self._WillExpireNum = WillExpireNum

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
        self._ModuleNum = params.get("ModuleNum")
        self._NodeNum = params.get("NodeNum")
        self._VcpuNum = params.get("VcpuNum")
        self._MemoryNum = params.get("MemoryNum")
        self._StorageNum = params.get("StorageNum")
        self._NetworkNum = params.get("NetworkNum")
        self._InstanceNum = params.get("InstanceNum")
        self._RunningNum = params.get("RunningNum")
        self._IsolationNum = params.get("IsolationNum")
        self._ExpiredNum = params.get("ExpiredNum")
        self._WillExpireNum = params.get("WillExpireNum")
        self._RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkStorageRange: 网络带宽硬盘大小的范围信息。
        :type NetworkStorageRange: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        :param _ImageWhiteSet: 镜像操作系统白名单。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageWhiteSet: list of str
        :param _InstanceNetworkLimitConfigs: 网络限额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNetworkLimitConfigs: list of InstanceNetworkLimitConfig
        :param _ImageLimits: 镜像限额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageLimits: :class:`tencentcloud.ecm.v20190719.models.ImageLimitConfig`
        :param _DefaultIPDirect: 默认是否IP直通，用于模块创建，虚机购买等具有直通参数场景时的默认参数。
        :type DefaultIPDirect: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NetworkStorageRange = None
        self._ImageWhiteSet = None
        self._InstanceNetworkLimitConfigs = None
        self._ImageLimits = None
        self._DefaultIPDirect = None
        self._RequestId = None

    @property
    def NetworkStorageRange(self):
        """网络带宽硬盘大小的范围信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`
        """
        return self._NetworkStorageRange

    @NetworkStorageRange.setter
    def NetworkStorageRange(self, NetworkStorageRange):
        self._NetworkStorageRange = NetworkStorageRange

    @property
    def ImageWhiteSet(self):
        """镜像操作系统白名单。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ImageWhiteSet

    @ImageWhiteSet.setter
    def ImageWhiteSet(self, ImageWhiteSet):
        self._ImageWhiteSet = ImageWhiteSet

    @property
    def InstanceNetworkLimitConfigs(self):
        """网络限额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNetworkLimitConfig
        """
        return self._InstanceNetworkLimitConfigs

    @InstanceNetworkLimitConfigs.setter
    def InstanceNetworkLimitConfigs(self, InstanceNetworkLimitConfigs):
        self._InstanceNetworkLimitConfigs = InstanceNetworkLimitConfigs

    @property
    def ImageLimits(self):
        """镜像限额信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImageLimitConfig`
        """
        return self._ImageLimits

    @ImageLimits.setter
    def ImageLimits(self, ImageLimits):
        self._ImageLimits = ImageLimits

    @property
    def DefaultIPDirect(self):
        """默认是否IP直通，用于模块创建，虚机购买等具有直通参数场景时的默认参数。
        :rtype: bool
        """
        return self._DefaultIPDirect

    @DefaultIPDirect.setter
    def DefaultIPDirect(self, DefaultIPDirect):
        self._DefaultIPDirect = DefaultIPDirect

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
        if params.get("NetworkStorageRange") is not None:
            self._NetworkStorageRange = NetworkStorageRange()
            self._NetworkStorageRange._deserialize(params.get("NetworkStorageRange"))
        self._ImageWhiteSet = params.get("ImageWhiteSet")
        if params.get("InstanceNetworkLimitConfigs") is not None:
            self._InstanceNetworkLimitConfigs = []
            for item in params.get("InstanceNetworkLimitConfigs"):
                obj = InstanceNetworkLimitConfig()
                obj._deserialize(item)
                self._InstanceNetworkLimitConfigs.append(obj)
        if params.get("ImageLimits") is not None:
            self._ImageLimits = ImageLimitConfig()
            self._ImageLimits._deserialize(params.get("ImageLimits"))
        self._DefaultIPDirect = params.get("DefaultIPDirect")
        self._RequestId = params.get("RequestId")


class DescribeCustomImageTaskRequest(AbstractModel):
    """DescribeCustomImageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 支持key,value查询
task-id: 异步任务ID
image-id: 镜像ID
image-name: 镜像名称
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """支持key,value查询
task-id: 异步任务ID
image-id: 镜像ID
image-name: 镜像名称
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeCustomImageTaskResponse(AbstractModel):
    """DescribeCustomImageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageTaskSet: 导入任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageTaskSet: list of ImageTask
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageTaskSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ImageTaskSet(self):
        """导入任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ImageTask
        """
        return self._ImageTaskSet

    @ImageTaskSet.setter
    def ImageTaskSet(self, ImageTaskSet):
        self._ImageTaskSet = ImageTaskSet

    @property
    def TotalCount(self):
        """总数
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
        if params.get("ImageTaskSet") is not None:
            self._ImageTaskSet = []
            for item in params.get("ImageTaskSet"):
                obj = ImageTask()
                obj._deserialize(item)
                self._ImageTaskSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDefaultSubnetRequest(AbstractModel):
    """DescribeDefaultSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM地域
        :type EcmRegion: str
        :param _Zone: ECM可用区
        :type Zone: str
        """
        self._EcmRegion = None
        self._Zone = None

    @property
    def EcmRegion(self):
        """ECM地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Zone(self):
        """ECM可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultSubnetResponse(AbstractModel):
    """DescribeDefaultSubnet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Subnet: 默认子网信息，若无子网，则为空数据。
        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Subnet = None
        self._RequestId = None

    @property
    def Subnet(self):
        """默认子网信息，若无子网，则为空数据。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Subnet`
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

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
        if params.get("Subnet") is not None:
            self._Subnet = Subnet()
            self._Subnet._deserialize(params.get("Subnet"))
        self._RequestId = params.get("RequestId")


class DescribeDisksRequest(AbstractModel):
    """DescribeDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。参数不支持同时指定`DiskIds`和`Filters`。<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按云盘类型过滤。 (SYSTEM_DISK：表示系统盘 | DATA_DISK：表示数据盘)<br><li>disk-charge-type - Array of String - 是否必填：否 -（过滤条件）按照云硬盘计费模式过滤。 (PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费。)<br><li>portable - Array of String - 是否必填：否 -（过滤条件）按是否为弹性云盘过滤。 (TRUE：表示弹性云盘 | FALSE：表示非弹性云盘。)<br><li>project-id - Array of Integer - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id - Array of String - 是否必填：否 -（过滤条件）按照云硬盘ID过滤。云盘ID形如：`disk-11112222`。<br><li>disk-name - Array of String - 是否必填：否 -（过滤条件）按照云盘名称过滤。<br><li>disk-type - Array of String - 是否必填：否 -（过滤条件）按照云盘介质类型过滤。(CLOUD_BASIC：表示普通云硬盘 | CLOUD_PREMIUM：表示高性能云硬盘。| CLOUD_SSD：表示SSD云硬盘 | CLOUD_HSSD：表示增强型SSD云硬盘。| CLOUD_TSSD：表示极速型云硬盘。)<br><li>disk-state - Array of String - 是否必填：否 -（过滤条件）按照云盘状态过滤。(UNATTACHED：未挂载 | ATTACHING：挂载中 | ATTACHED：已挂载 | DETACHING：解挂中 | EXPANDING：扩容中 | ROLLBACKING：回滚中 | TORECYCLE：待回收。)<br><li>instance-id - Array of String - 是否必填：否 -（过滤条件）按照云盘挂载的云主机实例ID过滤。可根据此参数查询挂载在指定云主机下的云硬盘。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>instance-ip-address - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载云主机的内网或外网IP过滤。<br><li>instance-name - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载的实例名称过滤。<br><li>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。<br><li>tag-value - Array of String - 是否必填：否 -（过滤条件）照标签值进行过滤。<br><li>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _OrderField: 云盘列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据云盘的创建时间排序<br><li>DEADLINE：依据云盘的到期时间排序<br>默认按云盘创建时间排序。
        :type OrderField: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param _ReturnBindAutoSnapshotPolicy: 云盘详情中是否需要返回云盘绑定的定期快照策略ID，TRUE表示需要返回，FALSE表示不返回。
        :type ReturnBindAutoSnapshotPolicy: bool
        :param _DiskIds: 按照一个或者多个云硬盘ID查询。云硬盘ID形如：`disk-11112222`，此参数的具体格式可参考API[简介](/document/product/362/15633)的ids.N一节）。参数不支持同时指定`DiskIds`和`Filters`。
        :type DiskIds: list of str
        :param _Order: 输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        """
        self._Filters = None
        self._Limit = None
        self._OrderField = None
        self._Offset = None
        self._ReturnBindAutoSnapshotPolicy = None
        self._DiskIds = None
        self._Order = None

    @property
    def Filters(self):
        """过滤条件。参数不支持同时指定`DiskIds`和`Filters`。<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按云盘类型过滤。 (SYSTEM_DISK：表示系统盘 | DATA_DISK：表示数据盘)<br><li>disk-charge-type - Array of String - 是否必填：否 -（过滤条件）按照云硬盘计费模式过滤。 (PREPAID：表示预付费，即包年包月 | POSTPAID_BY_HOUR：表示后付费，即按量计费。)<br><li>portable - Array of String - 是否必填：否 -（过滤条件）按是否为弹性云盘过滤。 (TRUE：表示弹性云盘 | FALSE：表示非弹性云盘。)<br><li>project-id - Array of Integer - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id - Array of String - 是否必填：否 -（过滤条件）按照云硬盘ID过滤。云盘ID形如：`disk-11112222`。<br><li>disk-name - Array of String - 是否必填：否 -（过滤条件）按照云盘名称过滤。<br><li>disk-type - Array of String - 是否必填：否 -（过滤条件）按照云盘介质类型过滤。(CLOUD_BASIC：表示普通云硬盘 | CLOUD_PREMIUM：表示高性能云硬盘。| CLOUD_SSD：表示SSD云硬盘 | CLOUD_HSSD：表示增强型SSD云硬盘。| CLOUD_TSSD：表示极速型云硬盘。)<br><li>disk-state - Array of String - 是否必填：否 -（过滤条件）按照云盘状态过滤。(UNATTACHED：未挂载 | ATTACHING：挂载中 | ATTACHED：已挂载 | DETACHING：解挂中 | EXPANDING：扩容中 | ROLLBACKING：回滚中 | TORECYCLE：待回收。)<br><li>instance-id - Array of String - 是否必填：否 -（过滤条件）按照云盘挂载的云主机实例ID过滤。可根据此参数查询挂载在指定云主机下的云硬盘。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>instance-ip-address - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载云主机的内网或外网IP过滤。<br><li>instance-name - Array of String - 是否必填：否 -（过滤条件）按云盘所挂载的实例名称过滤。<br><li>tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键进行过滤。<br><li>tag-value - Array of String - 是否必填：否 -（过滤条件）照标签值进行过滤。<br><li>tag:tag-key - Array of String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        """云盘列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据云盘的创建时间排序<br><li>DEADLINE：依据云盘的到期时间排序<br>默认按云盘创建时间排序。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ReturnBindAutoSnapshotPolicy(self):
        """云盘详情中是否需要返回云盘绑定的定期快照策略ID，TRUE表示需要返回，FALSE表示不返回。
        :rtype: bool
        """
        return self._ReturnBindAutoSnapshotPolicy

    @ReturnBindAutoSnapshotPolicy.setter
    def ReturnBindAutoSnapshotPolicy(self, ReturnBindAutoSnapshotPolicy):
        self._ReturnBindAutoSnapshotPolicy = ReturnBindAutoSnapshotPolicy

    @property
    def DiskIds(self):
        """按照一个或者多个云硬盘ID查询。云硬盘ID形如：`disk-11112222`，此参数的具体格式可参考API[简介](/document/product/362/15633)的ids.N一节）。参数不支持同时指定`DiskIds`和`Filters`。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def Order(self):
        """输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._ReturnBindAutoSnapshotPolicy = params.get("ReturnBindAutoSnapshotPolicy")
        self._DiskIds = params.get("DiskIds")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDisksResponse(AbstractModel):
    """DescribeDisks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的云硬盘数量。
        :type TotalCount: int
        :param _DiskSet: 云硬盘的详细信息列表。
        :type DiskSet: list of Disk
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DiskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的云硬盘数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DiskSet(self):
        """云硬盘的详细信息列表。
        :rtype: list of Disk
        """
        return self._DiskSet

    @DiskSet.setter
    def DiskSet(self, DiskSet):
        self._DiskSet = DiskSet

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
        if params.get("DiskSet") is not None:
            self._DiskSet = []
            for item in params.get("DiskSet"):
                obj = Disk()
                obj._deserialize(item)
                self._DiskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HaVipIds: HAVIP数组，HAVIP唯一ID，形如：havip-9o233uri。
        :type HaVipIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定HaVipIds和Filters。
havip-id - String - HAVIP唯一ID，形如：havip-9o233uri。
havip-name - String - HAVIP名称。
vpc-id - String - HAVIP所在私有网络ID。
subnet-id - String - HAVIP所在子网ID。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认值是0。
        :type Offset: int
        :param _Limit: 返回数量，默认值是20，最大是100。
        :type Limit: int
        :param _EcmRegion: Ecm 区域，不填代表全部区域。
        :type EcmRegion: str
        """
        self._HaVipIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None

    @property
    def HaVipIds(self):
        """HAVIP数组，HAVIP唯一ID，形如：havip-9o233uri。
        :rtype: list of str
        """
        return self._HaVipIds

    @HaVipIds.setter
    def HaVipIds(self, HaVipIds):
        self._HaVipIds = HaVipIds

    @property
    def Filters(self):
        """过滤条件，参数不支持同时指定HaVipIds和Filters。
havip-id - String - HAVIP唯一ID，形如：havip-9o233uri。
havip-name - String - HAVIP名称。
vpc-id - String - HAVIP所在私有网络ID。
subnet-id - String - HAVIP所在子网ID。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认值是0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认值是20，最大是100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """Ecm 区域，不填代表全部区域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._HaVipIds = params.get("HaVipIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param _HaVipSet: HAVIP对象数组。
        :type HaVipSet: list of HaVip
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HaVipSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的对象数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HaVipSet(self):
        """HAVIP对象数组。
        :rtype: list of HaVip
        """
        return self._HaVipSet

    @HaVipSet.setter
    def HaVipSet(self, HaVipSet):
        self._HaVipSet = HaVipSet

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
        if params.get("HaVipSet") is not None:
            self._HaVipSet = []
            for item in params.get("HaVipSet"):
                obj = HaVip()
                obj._deserialize(item)
                self._HaVipSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，每次请求的Filters的上限为10，详细的过滤条件如下：
image-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤
image-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：
PRIVATE_IMAGE: 私有镜像 (本账户创建的镜像) 
PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)
instance-type -String - 是否必填: 否 - (过滤条件) 按机型过滤支持的镜像
image-name - String - 是否必填：否 - (过滤条件) 按镜像的名称模糊匹配，只能提供一个值
image-os - String - 是否必填：否 - (过滤条件) 按镜像系统的名称模糊匹配，只能提供一个值
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """过滤条件，每次请求的Filters的上限为10，详细的过滤条件如下：
image-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤
image-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：
PRIVATE_IMAGE: 私有镜像 (本账户创建的镜像) 
PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)
instance-type -String - 是否必填: 否 - (过滤条件) 按机型过滤支持的镜像
image-name - String - 是否必填：否 - (过滤条件) 按镜像的名称模糊匹配，只能提供一个值
image-os - String - 是否必填：否 - (过滤条件) 按镜像系统的名称模糊匹配，只能提供一个值
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
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
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 镜像总数
        :type TotalCount: int
        :param _ImageSet: 镜像数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSet: list of Image
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ImageSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """镜像总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ImageSet(self):
        """镜像数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Image
        """
        return self._ImageSet

    @ImageSet.setter
    def ImageSet(self, ImageSet):
        self._ImageSet = ImageSet

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
        if params.get("ImageSet") is not None:
            self._ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self._ImageSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs请求参数结构体

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImportImageOsListSupported: 支持的导入镜像的操作系统类型
        :type ImportImageOsListSupported: :class:`tencentcloud.ecm.v20190719.models.ImageOsList`
        :param _ImportImageOsVersionSet: 支持的导入镜像的操作系统版本
        :type ImportImageOsVersionSet: list of OsVersion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImportImageOsListSupported = None
        self._ImportImageOsVersionSet = None
        self._RequestId = None

    @property
    def ImportImageOsListSupported(self):
        """支持的导入镜像的操作系统类型
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImageOsList`
        """
        return self._ImportImageOsListSupported

    @ImportImageOsListSupported.setter
    def ImportImageOsListSupported(self, ImportImageOsListSupported):
        self._ImportImageOsListSupported = ImportImageOsListSupported

    @property
    def ImportImageOsVersionSet(self):
        """支持的导入镜像的操作系统版本
        :rtype: list of OsVersion
        """
        return self._ImportImageOsVersionSet

    @ImportImageOsVersionSet.setter
    def ImportImageOsVersionSet(self, ImportImageOsVersionSet):
        self._ImportImageOsVersionSet = ImportImageOsVersionSet

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
        if params.get("ImportImageOsListSupported") is not None:
            self._ImportImageOsListSupported = ImageOsList()
            self._ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self._ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self._ImportImageOsVersionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigRequest(AbstractModel):
    """DescribeInstanceTypeConfig请求参数结构体

    """


class DescribeInstanceTypeConfigResponse(AbstractModel):
    """DescribeInstanceTypeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _InstanceTypeConfigSet: 机型配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceTypeConfigSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceTypeConfigSet(self):
        """机型配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceTypeConfig
        """
        return self._InstanceTypeConfigSet

    @InstanceTypeConfigSet.setter
    def InstanceTypeConfigSet(self, InstanceTypeConfigSet):
        self._InstanceTypeConfigSet = InstanceTypeConfigSet

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
        if params.get("InstanceTypeConfigSet") is not None:
            self._InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self._InstanceTypeConfigSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 一个操作的实例ID。可通过DescribeInstances API返回值中的InstanceId获取。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """一个操作的实例ID。可通过DescribeInstances API返回值中的InstanceId获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceVncUrl: 实例的管理终端地址。
        :type InstanceVncUrl: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceVncUrl = None
        self._RequestId = None

    @property
    def InstanceVncUrl(self):
        """实例的管理终端地址。
        :rtype: str
        """
        return self._InstanceVncUrl

    @InstanceVncUrl.setter
    def InstanceVncUrl(self, InstanceVncUrl):
        self._InstanceVncUrl = InstanceVncUrl

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
        self._InstanceVncUrl = params.get("InstanceVncUrl")
        self._RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 无
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """无
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceOperatorSet: 实例对应的禁止操作
        :type InstanceOperatorSet: list of InstanceOperator
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceOperatorSet = None
        self._RequestId = None

    @property
    def InstanceOperatorSet(self):
        """实例对应的禁止操作
        :rtype: list of InstanceOperator
        """
        return self._InstanceOperatorSet

    @InstanceOperatorSet.setter
    def InstanceOperatorSet(self, InstanceOperatorSet):
        self._InstanceOperatorSet = InstanceOperatorSet

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
        if params.get("InstanceOperatorSet") is not None:
            self._InstanceOperatorSet = []
            for item in params.get("InstanceOperatorSet"):
                obj = InstanceOperator()
                obj._deserialize(item)
                self._InstanceOperatorSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。
zone      String      是否必填：否     （过滤条件）按照可用区英文标识符过滤。
zone-name      String      是否必填：否     （过滤条件）按照可用区中文名过滤,支持模糊匹配。
module-id      String      是否必填：否     （过滤条件）按照模块ID过滤。
instance-id      String      是否必填：否      （过滤条件）按照实例ID过滤。
instance-name      String      是否必填：否      （过滤条件）按照实例名称过滤,支持模糊匹配。
ip-address      String      是否必填：否      （过滤条件）按照实例的内网/公网IP过滤。
instance-uuid   string 是否必填：否 （过滤条件）按照uuid过滤实例列表。
instance-state  string  是否必填：否 （过滤条件）按照实例状态更新实例列表。
internet-service-provider      String      是否必填：否      （过滤条件）按照实例公网IP所属的运营商进行过滤。
tag-key      String      是否必填：否      （过滤条件）按照标签键进行过滤。
tag:tag-key      String      是否必填：否      （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
instance-family      String      是否必填：否      （过滤条件）按照机型family过滤。
module-name      String      是否必填：否      （过滤条件）按照模块名称过滤,支持模糊匹配。
image-id      String      是否必填：否      （过滤条件）按照实例的镜像ID过滤。
vpc-id String      是否必填：否      （过滤条件）按照实例的vpc id过滤。
subnet-id String      是否必填：否      （过滤条件）按照实例的subnet id过滤。

若不传Filters参数则表示查询所有相关的实例信息。
单次请求的Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20(如果查询结果数目大于等于20)，最大值为100。
        :type Limit: int
        :param _OrderByField: 指定排序字段。目前支持的可选值如下
timestamp 按实例创建时间排序。
注意：目前仅支持按创建时间排序，后续可能会有扩展。
如果不传，默认按实例创建时间排序
        :type OrderByField: str
        :param _OrderDirection: 指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序
        :type OrderDirection: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderByField = None
        self._OrderDirection = None

    @property
    def Filters(self):
        """过滤条件。
zone      String      是否必填：否     （过滤条件）按照可用区英文标识符过滤。
zone-name      String      是否必填：否     （过滤条件）按照可用区中文名过滤,支持模糊匹配。
module-id      String      是否必填：否     （过滤条件）按照模块ID过滤。
instance-id      String      是否必填：否      （过滤条件）按照实例ID过滤。
instance-name      String      是否必填：否      （过滤条件）按照实例名称过滤,支持模糊匹配。
ip-address      String      是否必填：否      （过滤条件）按照实例的内网/公网IP过滤。
instance-uuid   string 是否必填：否 （过滤条件）按照uuid过滤实例列表。
instance-state  string  是否必填：否 （过滤条件）按照实例状态更新实例列表。
internet-service-provider      String      是否必填：否      （过滤条件）按照实例公网IP所属的运营商进行过滤。
tag-key      String      是否必填：否      （过滤条件）按照标签键进行过滤。
tag:tag-key      String      是否必填：否      （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
instance-family      String      是否必填：否      （过滤条件）按照机型family过滤。
module-name      String      是否必填：否      （过滤条件）按照模块名称过滤,支持模糊匹配。
image-id      String      是否必填：否      （过滤条件）按照实例的镜像ID过滤。
vpc-id String      是否必填：否      （过滤条件）按照实例的vpc id过滤。
subnet-id String      是否必填：否      （过滤条件）按照实例的subnet id过滤。

若不传Filters参数则表示查询所有相关的实例信息。
单次请求的Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        """返回数量，默认为20(如果查询结果数目大于等于20)，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByField(self):
        """指定排序字段。目前支持的可选值如下
timestamp 按实例创建时间排序。
注意：目前仅支持按创建时间排序，后续可能会有扩展。
如果不传，默认按实例创建时间排序
        :rtype: str
        """
        return self._OrderByField

    @OrderByField.setter
    def OrderByField(self, OrderByField):
        self._OrderByField = OrderByField

    @property
    def OrderDirection(self):
        """指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序
        :rtype: int
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByField = params.get("OrderByField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 返回的实例相关信息列表的长度。
        :type TotalCount: int
        :param _InstanceSet: 返回的实例相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of Instance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """返回的实例相关信息列表的长度。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        """返回的实例相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

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
                obj = Instance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerIds: 要查询的负载均衡监听器 ID数组
        :type ListenerIds: list of str
        :param _Protocol: 要查询的监听器协议类型，取值 TCP | UDP
        :type Protocol: str
        :param _Port: 要查询的监听器的端口
        :type Port: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        """要查询的负载均衡监听器 ID数组
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        """要查询的监听器协议类型，取值 TCP | UDP
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """要查询的监听器的端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listeners: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of Listener
        :param _TotalCount: 总的监听器个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listeners = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listeners(self):
        """监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Listener
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def TotalCount(self):
        """总的监听器个数
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
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalanceTaskStatusRequest(AbstractModel):
    """DescribeLoadBalanceTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 请求ID，即接口返回的 RequestId 参数
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """请求ID，即接口返回的 RequestId 参数
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
        


class DescribeLoadBalanceTaskStatusResponse(AbstractModel):
    """DescribeLoadBalanceTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务的当前状态。 0：成功，1：失败，2：进行中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        """任务的当前状态。 0：成功，1：失败，2：进行中。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
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
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: 区域。如果不传则默认查询所有区域。
        :type EcmRegion: str
        :param _LoadBalancerIds: 负载均衡实例 ID。
        :type LoadBalancerIds: list of str
        :param _LoadBalancerName: 负载均衡实例的名称。
        :type LoadBalancerName: str
        :param _LoadBalancerVips: 负载均衡实例的 VIP 地址，支持多个。
        :type LoadBalancerVips: list of str
        :param _BackendPrivateIps: 负载均衡绑定的后端服务的内网 IP。
        :type BackendPrivateIps: list of str
        :param _Offset: 数据偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回负载均衡实例的数量，默认为20，最大值为100。
        :type Limit: int
        :param _WithBackend: 负载均衡是否绑定后端服务，0：没有绑定后端服务，1：绑定后端服务，-1：查询全部。 
如果不传则默认查询全部。
        :type WithBackend: int
        :param _VpcId: 负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx。
        :type VpcId: str
        :param _Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。详细的过滤条件如下：
tag-key - String - 是否必填：否 - （过滤条件）按照标签的键过滤。
        :type Filters: list of Filter
        :param _SecurityGroup: 安全组。
        :type SecurityGroup: str
        """
        self._EcmRegion = None
        self._LoadBalancerIds = None
        self._LoadBalancerName = None
        self._LoadBalancerVips = None
        self._BackendPrivateIps = None
        self._Offset = None
        self._Limit = None
        self._WithBackend = None
        self._VpcId = None
        self._Filters = None
        self._SecurityGroup = None

    @property
    def EcmRegion(self):
        """区域。如果不传则默认查询所有区域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def LoadBalancerIds(self):
        """负载均衡实例 ID。
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def LoadBalancerName(self):
        """负载均衡实例的名称。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerVips(self):
        """负载均衡实例的 VIP 地址，支持多个。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def BackendPrivateIps(self):
        """负载均衡绑定的后端服务的内网 IP。
        :rtype: list of str
        """
        return self._BackendPrivateIps

    @BackendPrivateIps.setter
    def BackendPrivateIps(self, BackendPrivateIps):
        self._BackendPrivateIps = BackendPrivateIps

    @property
    def Offset(self):
        """数据偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回负载均衡实例的数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def WithBackend(self):
        """负载均衡是否绑定后端服务，0：没有绑定后端服务，1：绑定后端服务，-1：查询全部。 
如果不传则默认查询全部。
        :rtype: int
        """
        return self._WithBackend

    @WithBackend.setter
    def WithBackend(self, WithBackend):
        self._WithBackend = WithBackend

    @property
    def VpcId(self):
        """负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Filters(self):
        """每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。详细的过滤条件如下：
tag-key - String - 是否必填：否 - （过滤条件）按照标签的键过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SecurityGroup(self):
        """安全组。
        :rtype: str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._BackendPrivateIps = params.get("BackendPrivateIps")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._WithBackend = params.get("WithBackend")
        self._VpcId = params.get("VpcId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _LoadBalancerSet: 返回的负载均衡实例数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerSet: list of LoadBalancer
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._LoadBalancerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def LoadBalancerSet(self):
        """返回的负载均衡实例数组。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LoadBalancer
        """
        return self._LoadBalancerSet

    @LoadBalancerSet.setter
    def LoadBalancerSet(self, LoadBalancerSet):
        self._LoadBalancerSet = LoadBalancerSet

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
        if params.get("LoadBalancerSet") is not None:
            self._LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeModuleDetailRequest(AbstractModel):
    """DescribeModuleDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID，如em-qn46snq8。
        :type ModuleId: str
        """
        self._ModuleId = None

    @property
    def ModuleId(self):
        """模块ID，如em-qn46snq8。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleDetailResponse(AbstractModel):
    """DescribeModuleDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Module: 模块的详细信息，详细见数据结构中的ModuleInfo。
注意：此字段可能返回 null，表示取不到有效值。
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        :param _ModuleCounter: 模块的统计信息，详细见数据结构中的ModuleCounterInfo。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleCounter: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Module = None
        self._ModuleCounter = None
        self._RequestId = None

    @property
    def Module(self):
        """模块的详细信息，详细见数据结构中的ModuleInfo。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ModuleCounter(self):
        """模块的统计信息，详细见数据结构中的ModuleCounterInfo。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`
        """
        return self._ModuleCounter

    @ModuleCounter.setter
    def ModuleCounter(self, ModuleCounter):
        self._ModuleCounter = ModuleCounter

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
        if params.get("Module") is not None:
            self._Module = Module()
            self._Module._deserialize(params.get("Module"))
        if params.get("ModuleCounter") is not None:
            self._ModuleCounter = ModuleCounter()
            self._ModuleCounter._deserialize(params.get("ModuleCounter"))
        self._RequestId = params.get("RequestId")


class DescribeModuleRequest(AbstractModel):
    """DescribeModule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。
module-name - string - 是否必填：否 - （过滤条件）按照模块名称过滤。
module-id - string - 是否必填：否 - （过滤条件）按照模块ID过滤。
image-id      String      是否必填：否      （过滤条件）按照镜像ID过滤。
instance-family      String      是否必填：否      （过滤条件）按照机型family过滤。
security-group-id - string 是否必填：否 - （过滤条件）按照模块绑定的安全组id过滤。
每次请求的Filters的上限为10，Filter.Values的上限为5。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        :param _OrderByField: 指定排序字段。目前支持的可选值如下
instance-num 按实例数量排序。
node-num 按节点数量排序。
timestamp 按实例创建时间排序。
如果不传，默认按实例创建时间排序
        :type OrderByField: str
        :param _OrderDirection: 指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序
        :type OrderDirection: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderByField = None
        self._OrderDirection = None

    @property
    def Filters(self):
        """过滤条件。
module-name - string - 是否必填：否 - （过滤条件）按照模块名称过滤。
module-id - string - 是否必填：否 - （过滤条件）按照模块ID过滤。
image-id      String      是否必填：否      （过滤条件）按照镜像ID过滤。
instance-family      String      是否必填：否      （过滤条件）按照机型family过滤。
security-group-id - string 是否必填：否 - （过滤条件）按照模块绑定的安全组id过滤。
每次请求的Filters的上限为10，Filter.Values的上限为5。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderByField(self):
        """指定排序字段。目前支持的可选值如下
instance-num 按实例数量排序。
node-num 按节点数量排序。
timestamp 按实例创建时间排序。
如果不传，默认按实例创建时间排序
        :rtype: str
        """
        return self._OrderByField

    @OrderByField.setter
    def OrderByField(self, OrderByField):
        self._OrderByField = OrderByField

    @property
    def OrderDirection(self):
        """指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序
        :rtype: int
        """
        return self._OrderDirection

    @OrderDirection.setter
    def OrderDirection(self, OrderDirection):
        self._OrderDirection = OrderDirection


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderByField = params.get("OrderByField")
        self._OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleResponse(AbstractModel):
    """DescribeModule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的模块数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ModuleItemSet: 模块详情信息的列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModuleItemSet: list of ModuleItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ModuleItemSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的模块数量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ModuleItemSet(self):
        """模块详情信息的列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ModuleItem
        """
        return self._ModuleItemSet

    @ModuleItemSet.setter
    def ModuleItemSet(self, ModuleItemSet):
        self._ModuleItemSet = ModuleItemSet

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
        if params.get("ModuleItemSet") is not None:
            self._ModuleItemSet = []
            for item in params.get("ModuleItemSet"):
                obj = ModuleItem()
                obj._deserialize(item)
                self._ModuleItemSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMonthPeakNetworkRequest(AbstractModel):
    """DescribeMonthPeakNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 月份时间(xxxx-xx) 如2021-03,默认取当前时间的上一个月份
        :type Month: str
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._Month = None
        self._Filters = None

    @property
    def Month(self):
        """月份时间(xxxx-xx) 如2021-03,默认取当前时间的上一个月份
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Filters(self):
        """过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Month = params.get("Month")
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
        


class DescribeMonthPeakNetworkResponse(AbstractModel):
    """DescribeMonthPeakNetwork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MonthNetWorkData: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type MonthNetWorkData: list of MonthNetwork
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MonthNetWorkData = None
        self._RequestId = None

    @property
    def MonthNetWorkData(self):
        """无
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MonthNetwork
        """
        return self._MonthNetWorkData

    @MonthNetWorkData.setter
    def MonthNetWorkData(self, MonthNetWorkData):
        self._MonthNetWorkData = MonthNetWorkData

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
        if params.get("MonthNetWorkData") is not None:
            self._MonthNetWorkData = []
            for item in params.get("MonthNetWorkData"):
                obj = MonthNetwork()
                obj._deserialize(item)
                self._MonthNetWorkData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceIds: 弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。
        :type NetworkInterfaceIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。
network-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。
attachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ein-3nqpdn3i。
groups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。
network-interface-name - String - （过滤条件）网卡实例名称。
network-interface-description - String - （过滤条件）网卡实例描述。
address-ip - String - （过滤条件）内网IPv4地址。
tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
is-primary - Boolean - 是否必填：否 - （过滤条件）按照是否主网卡进行过滤。值为true时，仅过滤主网卡；值为false时，仅过滤辅助网卡；次过滤参数为提供时，同时过滤主网卡和辅助网卡。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        """
        self._NetworkInterfaceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceIds(self):
        """弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。
        :rtype: list of str
        """
        return self._NetworkInterfaceIds

    @NetworkInterfaceIds.setter
    def NetworkInterfaceIds(self, NetworkInterfaceIds):
        self._NetworkInterfaceIds = NetworkInterfaceIds

    @property
    def Filters(self):
        """过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。
network-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。
attachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ein-3nqpdn3i。
groups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。
network-interface-name - String - （过滤条件）网卡实例名称。
network-interface-description - String - （过滤条件）网卡实例描述。
address-ip - String - （过滤条件）内网IPv4地址。
tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
is-primary - Boolean - 是否必填：否 - （过滤条件）按照是否主网卡进行过滤。值为true时，仅过滤主网卡；值为false时，仅过滤辅助网卡；次过滤参数为提供时，同时过滤主网卡和辅助网卡。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _NetworkInterfaceSet: 实例详细信息列表。
        :type NetworkInterfaceSet: list of NetworkInterface
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NetworkInterfaceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NetworkInterfaceSet(self):
        """实例详细信息列表。
        :rtype: list of NetworkInterface
        """
        return self._NetworkInterfaceSet

    @NetworkInterfaceSet.setter
    def NetworkInterfaceSet(self, NetworkInterfaceSet):
        self._NetworkInterfaceSet = NetworkInterfaceSet

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
        if params.get("NetworkInterfaceSet") is not None:
            self._NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self._NetworkInterfaceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNodeRequest(AbstractModel):
    """DescribeNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，name取值为： InstanceFamily-实例系列
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """过滤条件，name取值为： InstanceFamily-实例系列
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeNodeResponse(AbstractModel):
    """DescribeNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeSet: 节点详细信息的列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of Node
        :param _TotalCount: 所有的节点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodeSet(self):
        """节点详细信息的列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Node
        """
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

    @property
    def TotalCount(self):
        """所有的节点数量。
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
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = Node()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePackingQuotaGroupRequest(AbstractModel):
    """DescribePackingQuotaGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件，name取值为：Zone-可用区， InstanceType-实例类型，DataDiskSize - 数据盘大小
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        """过滤条件，name取值为：Zone-可用区， InstanceType-实例类型，DataDiskSize - 数据盘大小
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribePackingQuotaGroupResponse(AbstractModel):
    """DescribePackingQuotaGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PackingQuotaSet: 装箱配额组
        :type PackingQuotaSet: list of PackingQuotaGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PackingQuotaSet = None
        self._RequestId = None

    @property
    def PackingQuotaSet(self):
        """装箱配额组
        :rtype: list of PackingQuotaGroup
        """
        return self._PackingQuotaSet

    @PackingQuotaSet.setter
    def PackingQuotaSet(self, PackingQuotaSet):
        self._PackingQuotaSet = PackingQuotaSet

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
        if params.get("PackingQuotaSet") is not None:
            self._PackingQuotaSet = []
            for item in params.get("PackingQuotaSet"):
                obj = PackingQuotaGroup()
                obj._deserialize(item)
                self._PackingQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePeakBaseOverviewRequest(AbstractModel):
    """DescribePeakBaseOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期，不应与当前日期间隔超过90天。
        :type StartTime: str
        :param _EndTime: 结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天，不应与当前日期间隔超过90天。当开始与结束间隔不超过30天时返回1小时粒度的数据，否则返回3小时粒度的数据。
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期，不应与当前日期间隔超过90天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天，不应与当前日期间隔超过90天。当开始与结束间隔不超过30天时返回1小时粒度的数据，否则返回3小时粒度的数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakBaseOverviewResponse(AbstractModel):
    """DescribePeakBaseOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PeakFamilyInfoSet: 基础峰值列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakFamilyInfoSet: list of PeakFamilyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PeakFamilyInfoSet = None
        self._RequestId = None

    @property
    def PeakFamilyInfoSet(self):
        """基础峰值列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PeakFamilyInfo
        """
        return self._PeakFamilyInfoSet

    @PeakFamilyInfoSet.setter
    def PeakFamilyInfoSet(self, PeakFamilyInfoSet):
        self._PeakFamilyInfoSet = PeakFamilyInfoSet

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
        if params.get("PeakFamilyInfoSet") is not None:
            self._PeakFamilyInfoSet = []
            for item in params.get("PeakFamilyInfoSet"):
                obj = PeakFamilyInfo()
                obj._deserialize(item)
                self._PeakFamilyInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePeakNetworkOverviewRequest(AbstractModel):
    """DescribePeakNetworkOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期，不应与当前日期间隔超过30天。
        :type StartTime: str
        :param _EndTime: 结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天，不应与当前日期间隔超过30天。当开始与结束间隔不超过1天时会返回1分钟粒度的数据，不超过7天时返回5分钟粒度的数据，否则返回1小时粒度的数据。
        :type EndTime: str
        :param _Filters: 过滤条件。

region    String      是否必填：否     （过滤条件）按照region过滤，不支持模糊匹配。注意 region 填上需要查询ecm region才能返回数据。
area       String      是否必填：否     （过滤条件）按照大区过滤，不支持模糊匹配。大区包括：china-central、china-east等等，可以通过DescribeNode获得所有大区；也可使用ALL_REGION表示所有地区。
isp         String      是否必填：否     （过滤条件）按照运营商过滤大区流量，运营商包括CTCC、CUCC和CMCC。只和area同时使用，且一次只能指定一种运营商。

region和area只应填写一个。
        :type Filters: list of Filter
        :param _Period: 统计周期，单位秒。取值60/300。
        :type Period: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Period = None

    @property
    def StartTime(self):
        """开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期，不应与当前日期间隔超过30天。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天，不应与当前日期间隔超过30天。当开始与结束间隔不超过1天时会返回1分钟粒度的数据，不超过7天时返回5分钟粒度的数据，否则返回1小时粒度的数据。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        """过滤条件。

region    String      是否必填：否     （过滤条件）按照region过滤，不支持模糊匹配。注意 region 填上需要查询ecm region才能返回数据。
area       String      是否必填：否     （过滤条件）按照大区过滤，不支持模糊匹配。大区包括：china-central、china-east等等，可以通过DescribeNode获得所有大区；也可使用ALL_REGION表示所有地区。
isp         String      是否必填：否     （过滤条件）按照运营商过滤大区流量，运营商包括CTCC、CUCC和CMCC。只和area同时使用，且一次只能指定一种运营商。

region和area只应填写一个。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Period(self):
        """统计周期，单位秒。取值60/300。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakNetworkOverviewResponse(AbstractModel):
    """DescribePeakNetworkOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PeakNetworkRegionSet: 网络峰值数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakNetworkRegionSet: list of PeakNetworkRegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PeakNetworkRegionSet = None
        self._RequestId = None

    @property
    def PeakNetworkRegionSet(self):
        """网络峰值数组。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PeakNetworkRegionInfo
        """
        return self._PeakNetworkRegionSet

    @PeakNetworkRegionSet.setter
    def PeakNetworkRegionSet(self, PeakNetworkRegionSet):
        self._PeakNetworkRegionSet = PeakNetworkRegionSet

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
        if params.get("PeakNetworkRegionSet") is not None:
            self._PeakNetworkRegionSet = []
            for item in params.get("PeakNetworkRegionSet"):
                obj = PeakNetworkRegionInfo()
                obj._deserialize(item)
                self._PeakNetworkRegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePriceRunInstanceRequest(AbstractModel):
    """DescribePriceRunInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例的机型信息
        :type InstanceType: str
        :param _SystemDisk: 系统盘信息
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _InstanceCount: 实例个数
        :type InstanceCount: int
        :param _DataDisk: 数据盘信息
        :type DataDisk: list of DataDisk
        :param _InstanceChargeType: 实例计费类型。其中：
0，按资源维度后付费，计算当日用量峰值，例如CPU，内存，硬盘等，仅适用于非GNR系列机型；
1，按小时后付费，单价：xx元/实例/小时，仅适用于GNR机型，如需开通该计费方式请提工单申请；
2，按月后付费，单价：xx元/实例/月，仅适用于GNR机型；
该字段不填时，非GNR机型会默认选择0；GNR机型默认选择2。
        :type InstanceChargeType: int
        """
        self._InstanceType = None
        self._SystemDisk = None
        self._InstanceCount = None
        self._DataDisk = None
        self._InstanceChargeType = None

    @property
    def InstanceType(self):
        """实例的机型信息
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        """系统盘信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceCount(self):
        """实例个数
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def DataDisk(self):
        """数据盘信息
        :rtype: list of DataDisk
        """
        return self._DataDisk

    @DataDisk.setter
    def DataDisk(self, DataDisk):
        self._DataDisk = DataDisk

    @property
    def InstanceChargeType(self):
        """实例计费类型。其中：
0，按资源维度后付费，计算当日用量峰值，例如CPU，内存，硬盘等，仅适用于非GNR系列机型；
1，按小时后付费，单价：xx元/实例/小时，仅适用于GNR机型，如需开通该计费方式请提工单申请；
2，按月后付费，单价：xx元/实例/月，仅适用于GNR机型；
该字段不填时，非GNR机型会默认选择0；GNR机型默认选择2。
        :rtype: int
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceCount = params.get("InstanceCount")
        if params.get("DataDisk") is not None:
            self._DataDisk = []
            for item in params.get("DataDisk"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisk.append(obj)
        self._InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePriceRunInstanceResponse(AbstractModel):
    """DescribePriceRunInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格信息
        :type InstancePrice: :class:`tencentcloud.ecm.v20190719.models.InstancesPrice`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstancePrice = None
        self._RequestId = None

    @property
    def InstancePrice(self):
        """实例价格信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstancesPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

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
        if params.get("InstancePrice") is not None:
            self._InstancePrice = InstancesPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        self._RequestId = params.get("RequestId")


class DescribeRegionIpv6AddressesRequest(AbstractModel):
    """DescribeRegionIpv6Addresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域，为空时返回所有地域的IPv6地址。
        :type EcmRegion: str
        :param _Filters: 详细的过滤条件如下：
address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的 ID 过滤。
address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。
network-interface-id - String - 是否必填：否 - （过滤条件）按照弹性网卡的唯一ID过滤。
instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 所绑定的实例 ID 过滤。
vpc-id - String - 是否必填：否 - （过滤条件）按照 EIP 所在 VPC 的 ID 进行过滤。
address-isp - String - 是否必填：否 - （过滤条件）按照 EIP 的运营商进行过滤。
address-status  - String - 是否必填：否 - （过滤条件）按照 EIP  的状态信息进行过滤。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :type Limit: int
        """
        self._EcmRegion = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def EcmRegion(self):
        """ECM 地域，为空时返回所有地域的IPv6地址。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Filters(self):
        """详细的过滤条件如下：
address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的 ID 过滤。
address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。
network-interface-id - String - 是否必填：否 - （过滤条件）按照弹性网卡的唯一ID过滤。
instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 所绑定的实例 ID 过滤。
vpc-id - String - 是否必填：否 - （过滤条件）按照 EIP 所在 VPC 的 ID 进行过滤。
address-isp - String - 是否必填：否 - （过滤条件）按照 EIP 的运营商进行过滤。
address-status  - String - 是否必填：否 - （过滤条件）按照 EIP  的状态信息进行过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
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
        


class DescribeRegionIpv6AddressesResponse(AbstractModel):
    """DescribeRegionIpv6Addresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的 IPV6 数量。
        :type TotalCount: int
        :param _AddressSet: IPV6 详细信息列表。
        :type AddressSet: list of Address
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AddressSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的 IPV6 数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AddressSet(self):
        """IPV6 详细信息列表。
        :rtype: list of Address
        """
        return self._AddressSet

    @AddressSet.setter
    def AddressSet(self, AddressSet):
        self._AddressSet = AddressSet

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
        if params.get("AddressSet") is not None:
            self._AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self._AddressSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteConflictsRequest(AbstractModel):
    """DescribeRouteConflicts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param _DestinationCidrBlocks: 要检查的与之冲突的目的端列表
        :type DestinationCidrBlocks: list of str
        """
        self._RouteTableId = None
        self._DestinationCidrBlocks = None

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-azd4dt1c。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def DestinationCidrBlocks(self):
        """要检查的与之冲突的目的端列表
        :rtype: list of str
        """
        return self._DestinationCidrBlocks

    @DestinationCidrBlocks.setter
    def DestinationCidrBlocks(self, DestinationCidrBlocks):
        self._DestinationCidrBlocks = DestinationCidrBlocks


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._DestinationCidrBlocks = params.get("DestinationCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteConflictsResponse(AbstractModel):
    """DescribeRouteConflicts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteConflictSet: 路由策略冲突列表
        :type RouteConflictSet: list of RouteConflict
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RouteConflictSet = None
        self._RequestId = None

    @property
    def RouteConflictSet(self):
        """路由策略冲突列表
        :rtype: list of RouteConflict
        """
        return self._RouteConflictSet

    @RouteConflictSet.setter
    def RouteConflictSet(self, RouteConflictSet):
        self._RouteConflictSet = RouteConflictSet

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
        if params.get("RouteConflictSet") is not None:
            self._RouteConflictSet = []
            for item in params.get("RouteConflictSet"):
                obj = RouteConflict()
                obj._deserialize(item)
                self._RouteConflictSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableIds: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
route-table-name - String - （过滤条件）路由表名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
association.main - String - （过滤条件）是否主路由表。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 限数
        :type Limit: int
        :param _EcmRegion: ECM 地域，传空或不传表示所有区域
        :type EcmRegion: str
        """
        self._RouteTableIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None

    @property
    def RouteTableIds(self):
        """路由表实例ID，例如：rtb-azd4dt1c。
        :rtype: list of str
        """
        return self._RouteTableIds

    @RouteTableIds.setter
    def RouteTableIds(self, RouteTableIds):
        self._RouteTableIds = RouteTableIds

    @property
    def Filters(self):
        """过滤条件，参数不支持同时指定RouteTableIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
route-table-name - String - （过滤条件）路由表名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
association.main - String - （过滤条件）是否主路由表。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """限数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """ECM 地域，传空或不传表示所有区域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._RouteTableIds = params.get("RouteTableIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量
        :type TotalCount: int
        :param _RouteTableSet: 路由表列表
        :type RouteTableSet: list of RouteTable
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RouteTableSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的实例数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RouteTableSet(self):
        """路由表列表
        :rtype: list of RouteTable
        """
        return self._RouteTableSet

    @RouteTableSet.setter
    def RouteTableSet(self, RouteTableSet):
        self._RouteTableSet = RouteTableSet

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
        if params.get("RouteTableSet") is not None:
            self._RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self._RouteTableSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupAssociationStatisticsRequest(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 安全实例ID，例如esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。
        :type SecurityGroupIds: list of str
        """
        self._SecurityGroupIds = None

    @property
    def SecurityGroupIds(self):
        """安全实例ID，例如esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupAssociationStatisticsSet: 安全组关联实例统计。
        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupAssociationStatisticsSet = None
        self._RequestId = None

    @property
    def SecurityGroupAssociationStatisticsSet(self):
        """安全组关联实例统计。
        :rtype: list of SecurityGroupAssociationStatistics
        """
        return self._SecurityGroupAssociationStatisticsSet

    @SecurityGroupAssociationStatisticsSet.setter
    def SecurityGroupAssociationStatisticsSet(self, SecurityGroupAssociationStatisticsSet):
        self._SecurityGroupAssociationStatisticsSet = SecurityGroupAssociationStatisticsSet

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
        if params.get("SecurityGroupAssociationStatisticsSet") is not None:
            self._SecurityGroupAssociationStatisticsSet = []
            for item in params.get("SecurityGroupAssociationStatisticsSet"):
                obj = SecurityGroupAssociationStatistics()
                obj._deserialize(item)
                self._SecurityGroupAssociationStatisticsSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupLimitsRequest(AbstractModel):
    """DescribeSecurityGroupLimits请求参数结构体

    """


class DescribeSecurityGroupLimitsResponse(AbstractModel):
    """DescribeSecurityGroupLimits返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupLimitSet: 用户安全组配额限制。
        :type SecurityGroupLimitSet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupLimitSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupLimitSet = None
        self._RequestId = None

    @property
    def SecurityGroupLimitSet(self):
        """用户安全组配额限制。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupLimitSet`
        """
        return self._SecurityGroupLimitSet

    @SecurityGroupLimitSet.setter
    def SecurityGroupLimitSet(self, SecurityGroupLimitSet):
        self._SecurityGroupLimitSet = SecurityGroupLimitSet

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
        if params.get("SecurityGroupLimitSet") is not None:
            self._SecurityGroupLimitSet = SecurityGroupLimitSet()
            self._SecurityGroupLimitSet._deserialize(params.get("SecurityGroupLimitSet"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如：esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。
        :type SecurityGroupId: str
        """
        self._SecurityGroupId = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如：esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupPolicySet: 安全组规则集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityGroupPolicySet = None
        self._RequestId = None

    @property
    def SecurityGroupPolicySet(self):
        """安全组规则集合。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet

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
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 安全组实例ID，例如：esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。每次请求的实例的上限为100。参数不支持同时指定SecurityGroupIds和Filters。
        :type SecurityGroupIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定SecurityGroupIds和Filters。
security-group-id - String - （过滤条件）安全组ID。
security-group-name - String - （过滤条件）安全组名称。
tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._SecurityGroupIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SecurityGroupIds(self):
        """安全组实例ID，例如：esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。每次请求的实例的上限为100。参数不支持同时指定SecurityGroupIds和Filters。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Filters(self):
        """过滤条件，参数不支持同时指定SecurityGroupIds和Filters。
security-group-id - String - （过滤条件）安全组ID。
security-group-name - String - （过滤条件）安全组名称。
tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
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
        


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _SecurityGroupSet: 安全组对象。
        :type SecurityGroupSet: list of SecurityGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecurityGroupSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecurityGroupSet(self):
        """安全组对象。
        :rtype: list of SecurityGroup
        """
        return self._SecurityGroupSet

    @SecurityGroupSet.setter
    def SecurityGroupSet(self, SecurityGroupSet):
        self._SecurityGroupSet = SecurityGroupSet

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
        if params.get("SecurityGroupSet") is not None:
            self._SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self._SecurityGroupSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSnapshotsRequest(AbstractModel):
    """DescribeSnapshots请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SnapshotIds: 要查询快照的ID列表。参数不支持同时指定`SnapshotIds`和`Filters`。
        :type SnapshotIds: list of str
        :param _Filters: 过滤条件。参数不支持同时指定`SnapshotIds`和`Filters`。<br><li>snapshot-id - Array of String - 是否必填：否 -（过滤条件）按照快照的ID过滤。快照ID形如：`snap-11112222`。<br><li>snapshot-name - Array of String - 是否必填：否 -（过滤条件）按照快照名称过滤。<br><li>snapshot-state - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤。 (NORMAL：正常 | CREATING：创建中 | ROLLBACKING：回滚中。)<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按创建快照的云盘类型过滤。 (SYSTEM_DISK：代表系统盘 | DATA_DISK：代表数据盘。)<br><li>project-id  - Array of String - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id  - Array of String - 是否必填：否 -（过滤条件）按照创建快照的云硬盘ID过滤。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>encrypt - Array of String - 是否必填：否 -（过滤条件）按是否加密盘快照过滤。 (TRUE：表示加密盘快照 | FALSE：表示非加密盘快照。)
<li>snapshot-type- Array of String - 是否必填：否 -（过滤条件）根据snapshot-type指定的快照类型查询对应的快照。
(SHARED_SNAPSHOT：表示共享过来的快照 | PRIVATE_SNAPSHOT：表示自己私有快照。)
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :type Limit: int
        :param _OrderField: 快照列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据快照的创建时间排序<br>默认按创建时间排序。
        :type OrderField: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :type Offset: int
        :param _Order: 输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :type Order: str
        """
        self._SnapshotIds = None
        self._Filters = None
        self._Limit = None
        self._OrderField = None
        self._Offset = None
        self._Order = None

    @property
    def SnapshotIds(self):
        """要查询快照的ID列表。参数不支持同时指定`SnapshotIds`和`Filters`。
        :rtype: list of str
        """
        return self._SnapshotIds

    @SnapshotIds.setter
    def SnapshotIds(self, SnapshotIds):
        self._SnapshotIds = SnapshotIds

    @property
    def Filters(self):
        """过滤条件。参数不支持同时指定`SnapshotIds`和`Filters`。<br><li>snapshot-id - Array of String - 是否必填：否 -（过滤条件）按照快照的ID过滤。快照ID形如：`snap-11112222`。<br><li>snapshot-name - Array of String - 是否必填：否 -（过滤条件）按照快照名称过滤。<br><li>snapshot-state - Array of String - 是否必填：否 -（过滤条件）按照快照状态过滤。 (NORMAL：正常 | CREATING：创建中 | ROLLBACKING：回滚中。)<br><li>disk-usage - Array of String - 是否必填：否 -（过滤条件）按创建快照的云盘类型过滤。 (SYSTEM_DISK：代表系统盘 | DATA_DISK：代表数据盘。)<br><li>project-id  - Array of String - 是否必填：否 -（过滤条件）按云硬盘所属项目ID过滤。<br><li>disk-id  - Array of String - 是否必填：否 -（过滤条件）按照创建快照的云硬盘ID过滤。<br><li>zone - Array of String - 是否必填：否 -（过滤条件）按照[可用区](/document/product/213/15753#ZoneInfo)过滤。<br><li>encrypt - Array of String - 是否必填：否 -（过滤条件）按是否加密盘快照过滤。 (TRUE：表示加密盘快照 | FALSE：表示非加密盘快照。)
<li>snapshot-type- Array of String - 是否必填：否 -（过滤条件）根据snapshot-type指定的快照类型查询对应的快照。
(SHARED_SNAPSHOT：表示共享过来的快照 | PRIVATE_SNAPSHOT：表示自己私有快照。)
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](/document/product/362/15633)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        """快照列表排序的依据字段。取值范围：<br><li>CREATE_TIME：依据快照的创建时间排序<br>默认按创建时间排序。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Offset(self):
        """偏移量，默认为0。关于`Offset`的更进一步介绍请参考API[简介](/document/product/362/15633)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        """输出云盘列表的排列顺序。取值范围：<br><li>ASC：升序排列<br><li>DESC：降序排列。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._SnapshotIds = params.get("SnapshotIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSnapshotsResponse(AbstractModel):
    """DescribeSnapshots返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 快照的数量。
        :type TotalCount: int
        :param _SnapshotSet: 快照的详情列表。
        :type SnapshotSet: list of Snapshot
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SnapshotSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """快照的数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SnapshotSet(self):
        """快照的详情列表。
        :rtype: list of Snapshot
        """
        return self._SnapshotSet

    @SnapshotSet.setter
    def SnapshotSet(self, SnapshotSet):
        self._SnapshotSet = SnapshotSet

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
        if params.get("SnapshotSet") is not None:
            self._SnapshotSet = []
            for item in params.get("SnapshotSet"):
                obj = Snapshot()
                obj._deserialize(item)
                self._SnapshotSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetIds: 子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
subnet-id - String - Subnet实例名称。
subnet-name - String - 子网名称。只支持单值的模糊查询。
cidr-block - String - 子网网段，形如: 192.168.1.0 。只支持单值的模糊查询。
vpc-id - String - VPC实例ID，形如：vpc-f49l6u0z。
vpc-cidr-block  - String - vpc网段，形如: 192.168.1.0 。只支持单值的模糊查询。
region - String - ECM地域
zone - String - 可用区。
tag-key - String -是否必填：否- 按照标签键进行过滤。
ipv6-cidr-block- String - 是否必填：否 - 按照IPv6 CIDR进行过滤。
isp-type - String - 是否必填：否 - 按照运营商类型( 如CMCC，CUCC， CTCC)进行过滤。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: str
        :param _Limit: 返回数量
        :type Limit: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _Sort: 排序方式：time时间倒序, default按照网络规划排序
        :type Sort: str
        """
        self._SubnetIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None
        self._Sort = None

    @property
    def SubnetIds(self):
        """子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def Filters(self):
        """过滤条件，参数不支持同时指定SubnetIds和Filters。
subnet-id - String - Subnet实例名称。
subnet-name - String - 子网名称。只支持单值的模糊查询。
cidr-block - String - 子网网段，形如: 192.168.1.0 。只支持单值的模糊查询。
vpc-id - String - VPC实例ID，形如：vpc-f49l6u0z。
vpc-cidr-block  - String - vpc网段，形如: 192.168.1.0 。只支持单值的模糊查询。
region - String - ECM地域
zone - String - 可用区。
tag-key - String -是否必填：否- 按照标签键进行过滤。
ipv6-cidr-block- String - 是否必填：否 - 按照IPv6 CIDR进行过滤。
isp-type - String - 是否必填：否 - 按照运营商类型( 如CMCC，CUCC， CTCC)进行过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量
        :rtype: str
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量
        :rtype: str
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Sort(self):
        """排序方式：time时间倒序, default按照网络规划排序
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param _SubnetSet: 子网对象。
        :type SubnetSet: list of Subnet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SubnetSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的实例数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SubnetSet(self):
        """子网对象。
        :rtype: list of Subnet
        """
        return self._SubnetSet

    @SubnetSet.setter
    def SubnetSet(self, SubnetSet):
        self._SubnetSet = SubnetSet

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
        if params.get("SubnetSet") is not None:
            self._SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self._SubnetSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 要查询的负载均衡实例 ID列表
        :type LoadBalancerIds: list of str
        """
        self._LoadBalancerIds = None

    @property
    def LoadBalancerIds(self):
        """要查询的负载均衡实例 ID列表
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: 负载均衡实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancers: list of LoadBalancerHealth
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        """负载均衡实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LoadBalancerHealth
        """
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

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
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerIds: 监听器 ID列表
        :type ListenerIds: list of str
        :param _Protocol: 监听器协议类型
        :type Protocol: int
        :param _Port: 监听器端口
        :type Port: int
        """
        self._LoadBalancerId = None
        self._ListenerIds = None
        self._Protocol = None
        self._Port = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerIds(self):
        """监听器 ID列表
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def Protocol(self):
        """监听器协议类型
        :rtype: int
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """监听器端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerIds = params.get("ListenerIds")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listeners: 监听器后端绑定的机器信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerBackend
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listeners = None
        self._RequestId = None

    @property
    def Listeners(self):
        """监听器后端绑定的机器信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ListenerBackend
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

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
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        """
        self._EcmRegion = None
        self._TaskId = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def TaskId(self):
        """异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务ID。
        :type TaskId: str
        :param _Result: 执行结果，包括"SUCCESS", "FAILED", "RUNNING"
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._Result = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Result(self):
        """执行结果，包括"SUCCESS", "FAILED", "RUNNING"
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
        self._TaskId = params.get("TaskId")
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskSet: 任务描述
        :type TaskSet: list of TaskInput
        """
        self._TaskSet = None

    @property
    def TaskSet(self):
        """任务描述
        :rtype: list of TaskInput
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskInput()
                obj._deserialize(item)
                self._TaskSet.append(obj)
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
        :param _TaskSet: 任务描述
        :type TaskSet: list of TaskOutput
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskSet = None
        self._RequestId = None

    @property
    def TaskSet(self):
        """任务描述
        :rtype: list of TaskOutput
        """
        return self._TaskSet

    @TaskSet.setter
    def TaskSet(self, TaskSet):
        self._TaskSet = TaskSet

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
        if params.get("TaskSet") is not None:
            self._TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskOutput()
                obj._deserialize(item)
                self._TaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcIds: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。
        :type VpcIds: list of str
        :param _Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
vpc-name - String - VPC实例名称，只支持单值的模糊查询。
vpc-id - String - VPC实例ID形如：vpc-f49l6u0z。
cidr-block - String - vpc的cidr，只支持单值的模糊查询。
region - String - vpc的region。
tag-key - String -是否必填：否- 按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - 按照标签键值对进行过滤。
ipv6-cidr-block - String - 是否必填：否 - 按照IPv6 CIDR block进行过滤。
isp-type - String - 是否必填：否 - 按照运营商（如CMCC, CUCC, CTCC）进行过滤。
        :type Filters: list of Filter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 返回数量
        :type Limit: int
        :param _EcmRegion: 地域
        :type EcmRegion: str
        :param _Sort: 排序方式：time时间倒序, default按照网络规划排序
        :type Sort: str
        """
        self._VpcIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._EcmRegion = None
        self._Sort = None

    @property
    def VpcIds(self):
        """VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。
        :rtype: list of str
        """
        return self._VpcIds

    @VpcIds.setter
    def VpcIds(self, VpcIds):
        self._VpcIds = VpcIds

    @property
    def Filters(self):
        """过滤条件，参数不支持同时指定VpcIds和Filters。
vpc-name - String - VPC实例名称，只支持单值的模糊查询。
vpc-id - String - VPC实例ID形如：vpc-f49l6u0z。
cidr-block - String - vpc的cidr，只支持单值的模糊查询。
region - String - vpc的region。
tag-key - String -是否必填：否- 按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - 按照标签键值对进行过滤。
ipv6-cidr-block - String - 是否必填：否 - 按照IPv6 CIDR block进行过滤。
isp-type - String - 是否必填：否 - 按照运营商（如CMCC, CUCC, CTCC）进行过滤。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EcmRegion(self):
        """地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Sort(self):
        """排序方式：time时间倒序, default按照网络规划排序
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._EcmRegion = params.get("EcmRegion")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param _VpcSet: 私有网络对象。
        :type VpcSet: list of VpcInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的对象数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSet(self):
        """私有网络对象。
        :rtype: list of VpcInfo
        """
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

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
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DetachDisksRequest(AbstractModel):
    """DetachDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 将要卸载的云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询，单次请求最多可卸载10块弹性云盘。
        :type DiskIds: list of str
        :param _InstanceId: 对于非共享型云盘，会忽略该参数；对于共享型云盘，该参数表示要从哪个CVM实例上卸载云盘。
        :type InstanceId: str
        """
        self._DiskIds = None
        self._InstanceId = None

    @property
    def DiskIds(self):
        """将要卸载的云硬盘ID， 通过[DescribeDisks](/document/product/362/16315)接口查询，单次请求最多可卸载10块弹性云盘。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds

    @property
    def InstanceId(self):
        """对于非共享型云盘，会忽略该参数；对于共享型云盘，该参数表示要从哪个CVM实例上卸载云盘。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachDisksResponse(AbstractModel):
    """DetachDisks返回参数结构体

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


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _InstanceId: 实例ID。形如：ein-hcs7jkg4
        :type InstanceId: str
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._InstanceId = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def InstanceId(self):
        """实例ID。形如：ein-hcs7jkg4
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._InstanceId = params.get("InstanceId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface返回参数结构体

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


class DisableRoutesRequest(AbstractModel):
    """DisableRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param _RouteIds: 路由策略ID。
        :type RouteIds: list of int non-negative
        """
        self._RouteTableId = None
        self._RouteIds = None

    @property
    def RouteTableId(self):
        """路由表唯一ID。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteIds(self):
        """路由策略ID。
        :rtype: list of int non-negative
        """
        return self._RouteIds

    @RouteIds.setter
    def RouteIds(self, RouteIds):
        self._RouteIds = RouteIds


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRoutesResponse(AbstractModel):
    """DisableRoutes返回参数结构体

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


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :type AddressId: str
        :param _ReallocateNormalPublicIp: 表示解绑 EIP 之后是否分配普通公网 IP。取值范围：
TRUE：表示解绑 EIP 之后分配普通公网 IP。
FALSE：表示解绑 EIP 之后不分配普通公网 IP。
默认取值：FALSE。

只有满足以下条件时才能指定该参数：
只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。
解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 DescribeAddressQuota 接口获取。
        :type ReallocateNormalPublicIp: bool
        """
        self._EcmRegion = None
        self._AddressId = None
        self._ReallocateNormalPublicIp = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressId(self):
        """标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def ReallocateNormalPublicIp(self):
        """表示解绑 EIP 之后是否分配普通公网 IP。取值范围：
TRUE：表示解绑 EIP 之后分配普通公网 IP。
FALSE：表示解绑 EIP 之后不分配普通公网 IP。
默认取值：FALSE。

只有满足以下条件时才能指定该参数：
只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。
解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 DescribeAddressQuota 接口获取。
        :rtype: bool
        """
        return self._ReallocateNormalPublicIp

    @ReallocateNormalPublicIp.setter
    def ReallocateNormalPublicIp(self, ReallocateNormalPublicIp):
        self._ReallocateNormalPublicIp = ReallocateNormalPublicIp


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressId = params.get("AddressId")
        self._ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
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


class DisassociateInstancesKeyPairsRequest(AbstractModel):
    """DisassociateInstancesKeyPairs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 可以通过以下方式获取可用的实例ID：
通过登录控制台查询实例ID。
通过调用接口 DescribeInstances ，取返回信息中的 InstanceId 获取实例ID。
        :type InstanceIds: list of str
        :param _KeyIds: 密钥对ID列表，每次请求批量密钥对的上限为100。密钥对ID形如：skey-11112222。

可以通过以下方式获取可用的密钥ID：
通过登录控制台查询密钥ID。
通过调用接口 DescribeKeyPairs ，取返回信息中的 KeyId 获取密钥对ID。
        :type KeyIds: list of str
        :param _ForceStop: 是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再解绑密钥。取值范围：
TRUE：表示在正常关机失败后进行强制关机。
FALSE：表示在正常关机失败后不进行强制关机。

默认取值：FALSE。
        :type ForceStop: bool
        """
        self._InstanceIds = None
        self._KeyIds = None
        self._ForceStop = None

    @property
    def InstanceIds(self):
        """可以通过以下方式获取可用的实例ID：
通过登录控制台查询实例ID。
通过调用接口 DescribeInstances ，取返回信息中的 InstanceId 获取实例ID。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def KeyIds(self):
        """密钥对ID列表，每次请求批量密钥对的上限为100。密钥对ID形如：skey-11112222。

可以通过以下方式获取可用的密钥ID：
通过登录控制台查询密钥ID。
通过调用接口 DescribeKeyPairs ，取返回信息中的 KeyId 获取密钥对ID。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def ForceStop(self):
        """是否对运行中的实例选择强制关机。建议对运行中的实例先手动关机，然后再解绑密钥。取值范围：
TRUE：表示在正常关机失败后进行强制关机。
FALSE：表示在正常关机失败后不进行强制关机。

默认取值：FALSE。
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._KeyIds = params.get("KeyIds")
        self._ForceStop = params.get("ForceStop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateInstancesKeyPairsResponse(AbstractModel):
    """DisassociateInstancesKeyPairs返回参数结构体

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


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIds: 要解绑的安全组ID，类似esg-efil73jd，只支持解绑单个安全组。
        :type SecurityGroupIds: list of str
        :param _InstanceIds: 被解绑的实例ID，类似ein-lesecurk，支持指定多个实例 。
        :type InstanceIds: list of str
        """
        self._SecurityGroupIds = None
        self._InstanceIds = None

    @property
    def SecurityGroupIds(self):
        """要解绑的安全组ID，类似esg-efil73jd，只支持解绑单个安全组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def InstanceIds(self):
        """被解绑的实例ID，类似ein-lesecurk，支持指定多个实例 。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

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


class Disk(AbstractModel):
    """描述了云硬盘的详细信息

    """

    def __init__(self):
        r"""
        :param _DeleteWithInstance: 云盘是否与挂载的实例一起销毁。<br><li>true:销毁实例时会同时销毁云盘，只支持按小时后付费云盘。<br><li>false：销毁实例时不销毁云盘。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeleteWithInstance: bool
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: str
        :param _DiskType: 硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :type DiskType: str
        :param _DiskState: 云盘状态。取值范围：<br><li>UNATTACHED：未挂载<br><li>ATTACHING：挂载中<br><li>ATTACHED：已挂载<br><li>DETACHING：解挂中<br><li>EXPANDING：扩容中<br><li>ROLLBACKING：回滚中<br><li>TORECYCLE：待回收<br><li>DUMPING：拷贝硬盘中。
        :type DiskState: str
        :param _SnapshotCount: 云盘拥有的快照总数。
        :type SnapshotCount: int
        :param _AutoRenewFlagError: 云盘已挂载到子机，且子机与云盘都是包年包月。<br><li>true：子机设置了自动续费标识，但云盘未设置<br><li>false：云盘自动续费标识正常。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlagError: bool
        :param _Rollbacking: 云盘是否处于快照回滚状态。取值范围：<br><li>false:表示不处于快照回滚状态<br><li>true:表示处于快照回滚状态。
        :type Rollbacking: bool
        :param _InstanceIdList: 对于非共享型云盘，该参数为空数组。对于共享型云盘，则表示该云盘当前被挂载到的CVM实例InstanceId
        :type InstanceIdList: list of str
        :param _Encrypt: 云盘是否为加密盘。取值范围：<br><li>false:表示非加密盘<br><li>true:表示加密盘。
        :type Encrypt: bool
        :param _DiskName: 云硬盘名称。
        :type DiskName: str
        :param _BackupDisk: 云硬盘因欠费销毁或者到期销毁时， 是否使用快照备份数据的标识。true表示销毁时创建快照进行数据备份。false表示直接销毁，不进行数据备份。
        :type BackupDisk: bool
        :param _Tags: 与云盘绑定的标签，云盘未绑定标签则取值为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _InstanceId: 云硬盘挂载的云主机ID。
        :type InstanceId: str
        :param _AutoSnapshotPolicyIds: 云盘关联的定期快照ID。只有在调用DescribeDisks接口时，入参ReturnBindAutoSnapshotPolicy取值为TRUE才会返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoSnapshotPolicyIds: list of str
        :param _ThroughputPerformance: 云硬盘额外性能值，单位MB/s。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        :param _Migrating: 云盘是否处于类型变更中。取值范围：<br><li>false:表示云盘不处于类型变更中<br><li>true:表示云盘已发起类型变更，正处于迁移中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Migrating: bool
        :param _DiskId: 云硬盘ID。
        :type DiskId: str
        :param _SnapshotSize: 云盘拥有的快照总容量，单位为MB。
        :type SnapshotSize: int
        :param _Placement: 云硬盘所在的位置。
        :type Placement: :class:`tencentcloud.ecm.v20190719.models.Placement`
        :param _IsReturnable: 判断预付费的云盘是否支持主动退还。<br><li>true:支持主动退还<br><li>false:不支持主动退还。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsReturnable: bool
        :param _Attached: 云盘是否挂载到云主机上。取值范围：<br><li>false:表示未挂载<br><li>true:表示已挂载。
        :type Attached: bool
        :param _DiskSize: 云硬盘大小，单位GB。
        :type DiskSize: int
        :param _MigratePercent: 云盘类型变更的迁移进度，取值0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :type MigratePercent: int
        :param _DiskUsage: 云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param _DiskChargeType: 付费模式。取值范围：<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：后付费，即按量计费。
        :type DiskChargeType: str
        :param _Portable: 是否为弹性云盘，false表示非弹性云盘，true表示弹性云盘。
        :type Portable: bool
        :param _SnapshotAbility: 云盘是否具备创建快照的能力。取值范围：<br><li>false表示不具备<br><li>true表示具备。
        :type SnapshotAbility: bool
        :param _DeadlineError: 在云盘已挂载到实例，且实例与云盘都是包年包月的条件下，此字段才有意义。<br><li>true:云盘到期时间早于实例。<br><li>false：云盘到期时间晚于实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeadlineError: bool
        :param _RollbackPercent: 云盘快照回滚的进度。
        :type RollbackPercent: int
        :param _DifferDaysOfDeadline: 当前时间距离盘到期的天数（仅对预付费盘有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :type DifferDaysOfDeadline: int
        :param _ReturnFailCode: 预付费云盘在不支持主动退还的情况下，该参数表明不支持主动退还的具体原因。取值范围：<br><li>1：云硬盘已经退还<br><li>2：云硬盘已过期<br><li>3：云盘不支持退还<br><li>8：超过可退还数量的限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnFailCode: int
        :param _Shareable: 云盘是否为共享型云盘。
        :type Shareable: bool
        :param _CreateTime: 云硬盘的创建时间。
        :type CreateTime: str
        :param _DeadlineTime: 云硬盘的到期时间。
        :type DeadlineTime: str
        :param _AttachMode: 云盘的挂载类型。取值范围：<br><li>PF: PF挂载<br><li>VF: VF挂载
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachMode: str
        """
        self._DeleteWithInstance = None
        self._RenewFlag = None
        self._DiskType = None
        self._DiskState = None
        self._SnapshotCount = None
        self._AutoRenewFlagError = None
        self._Rollbacking = None
        self._InstanceIdList = None
        self._Encrypt = None
        self._DiskName = None
        self._BackupDisk = None
        self._Tags = None
        self._InstanceId = None
        self._AutoSnapshotPolicyIds = None
        self._ThroughputPerformance = None
        self._Migrating = None
        self._DiskId = None
        self._SnapshotSize = None
        self._Placement = None
        self._IsReturnable = None
        self._Attached = None
        self._DiskSize = None
        self._MigratePercent = None
        self._DiskUsage = None
        self._DiskChargeType = None
        self._Portable = None
        self._SnapshotAbility = None
        self._DeadlineError = None
        self._RollbackPercent = None
        self._DifferDaysOfDeadline = None
        self._ReturnFailCode = None
        self._Shareable = None
        self._CreateTime = None
        self._DeadlineTime = None
        self._AttachMode = None

    @property
    def DeleteWithInstance(self):
        """云盘是否与挂载的实例一起销毁。<br><li>true:销毁实例时会同时销毁云盘，只支持按小时后付费云盘。<br><li>false：销毁实例时不销毁云盘。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def RenewFlag(self):
        """自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def DiskType(self):
        """硬盘介质类型。取值范围：<br><li>CLOUD_BASIC：表示普通云硬盘<br><li>CLOUD_PREMIUM：表示高性能云硬盘<br><li>CLOUD_SSD：表示SSD云硬盘<br><li>CLOUD_HSSD：表示增强型SSD云硬盘<br><li>CLOUD_TSSD：表示极速型SSD云硬盘。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskState(self):
        """云盘状态。取值范围：<br><li>UNATTACHED：未挂载<br><li>ATTACHING：挂载中<br><li>ATTACHED：已挂载<br><li>DETACHING：解挂中<br><li>EXPANDING：扩容中<br><li>ROLLBACKING：回滚中<br><li>TORECYCLE：待回收<br><li>DUMPING：拷贝硬盘中。
        :rtype: str
        """
        return self._DiskState

    @DiskState.setter
    def DiskState(self, DiskState):
        self._DiskState = DiskState

    @property
    def SnapshotCount(self):
        """云盘拥有的快照总数。
        :rtype: int
        """
        return self._SnapshotCount

    @SnapshotCount.setter
    def SnapshotCount(self, SnapshotCount):
        self._SnapshotCount = SnapshotCount

    @property
    def AutoRenewFlagError(self):
        """云盘已挂载到子机，且子机与云盘都是包年包月。<br><li>true：子机设置了自动续费标识，但云盘未设置<br><li>false：云盘自动续费标识正常。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoRenewFlagError

    @AutoRenewFlagError.setter
    def AutoRenewFlagError(self, AutoRenewFlagError):
        self._AutoRenewFlagError = AutoRenewFlagError

    @property
    def Rollbacking(self):
        """云盘是否处于快照回滚状态。取值范围：<br><li>false:表示不处于快照回滚状态<br><li>true:表示处于快照回滚状态。
        :rtype: bool
        """
        return self._Rollbacking

    @Rollbacking.setter
    def Rollbacking(self, Rollbacking):
        self._Rollbacking = Rollbacking

    @property
    def InstanceIdList(self):
        """对于非共享型云盘，该参数为空数组。对于共享型云盘，则表示该云盘当前被挂载到的CVM实例InstanceId
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def Encrypt(self):
        """云盘是否为加密盘。取值范围：<br><li>false:表示非加密盘<br><li>true:表示加密盘。
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def DiskName(self):
        """云硬盘名称。
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName

    @property
    def BackupDisk(self):
        """云硬盘因欠费销毁或者到期销毁时， 是否使用快照备份数据的标识。true表示销毁时创建快照进行数据备份。false表示直接销毁，不进行数据备份。
        :rtype: bool
        """
        return self._BackupDisk

    @BackupDisk.setter
    def BackupDisk(self, BackupDisk):
        self._BackupDisk = BackupDisk

    @property
    def Tags(self):
        """与云盘绑定的标签，云盘未绑定标签则取值为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        """云硬盘挂载的云主机ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AutoSnapshotPolicyIds(self):
        """云盘关联的定期快照ID。只有在调用DescribeDisks接口时，入参ReturnBindAutoSnapshotPolicy取值为TRUE才会返回该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AutoSnapshotPolicyIds

    @AutoSnapshotPolicyIds.setter
    def AutoSnapshotPolicyIds(self, AutoSnapshotPolicyIds):
        self._AutoSnapshotPolicyIds = AutoSnapshotPolicyIds

    @property
    def ThroughputPerformance(self):
        """云硬盘额外性能值，单位MB/s。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance

    @property
    def Migrating(self):
        """云盘是否处于类型变更中。取值范围：<br><li>false:表示云盘不处于类型变更中<br><li>true:表示云盘已发起类型变更，正处于迁移中。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Migrating

    @Migrating.setter
    def Migrating(self, Migrating):
        self._Migrating = Migrating

    @property
    def DiskId(self):
        """云硬盘ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def SnapshotSize(self):
        """云盘拥有的快照总容量，单位为MB。
        :rtype: int
        """
        return self._SnapshotSize

    @SnapshotSize.setter
    def SnapshotSize(self, SnapshotSize):
        self._SnapshotSize = SnapshotSize

    @property
    def Placement(self):
        """云硬盘所在的位置。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def IsReturnable(self):
        """判断预付费的云盘是否支持主动退还。<br><li>true:支持主动退还<br><li>false:不支持主动退还。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsReturnable

    @IsReturnable.setter
    def IsReturnable(self, IsReturnable):
        self._IsReturnable = IsReturnable

    @property
    def Attached(self):
        """云盘是否挂载到云主机上。取值范围：<br><li>false:表示未挂载<br><li>true:表示已挂载。
        :rtype: bool
        """
        return self._Attached

    @Attached.setter
    def Attached(self, Attached):
        self._Attached = Attached

    @property
    def DiskSize(self):
        """云硬盘大小，单位GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def MigratePercent(self):
        """云盘类型变更的迁移进度，取值0到100。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MigratePercent

    @MigratePercent.setter
    def MigratePercent(self, MigratePercent):
        self._MigratePercent = MigratePercent

    @property
    def DiskUsage(self):
        """云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def DiskChargeType(self):
        """付费模式。取值范围：<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：后付费，即按量计费。
        :rtype: str
        """
        return self._DiskChargeType

    @DiskChargeType.setter
    def DiskChargeType(self, DiskChargeType):
        self._DiskChargeType = DiskChargeType

    @property
    def Portable(self):
        """是否为弹性云盘，false表示非弹性云盘，true表示弹性云盘。
        :rtype: bool
        """
        return self._Portable

    @Portable.setter
    def Portable(self, Portable):
        self._Portable = Portable

    @property
    def SnapshotAbility(self):
        """云盘是否具备创建快照的能力。取值范围：<br><li>false表示不具备<br><li>true表示具备。
        :rtype: bool
        """
        return self._SnapshotAbility

    @SnapshotAbility.setter
    def SnapshotAbility(self, SnapshotAbility):
        self._SnapshotAbility = SnapshotAbility

    @property
    def DeadlineError(self):
        """在云盘已挂载到实例，且实例与云盘都是包年包月的条件下，此字段才有意义。<br><li>true:云盘到期时间早于实例。<br><li>false：云盘到期时间晚于实例。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._DeadlineError

    @DeadlineError.setter
    def DeadlineError(self, DeadlineError):
        self._DeadlineError = DeadlineError

    @property
    def RollbackPercent(self):
        """云盘快照回滚的进度。
        :rtype: int
        """
        return self._RollbackPercent

    @RollbackPercent.setter
    def RollbackPercent(self, RollbackPercent):
        self._RollbackPercent = RollbackPercent

    @property
    def DifferDaysOfDeadline(self):
        """当前时间距离盘到期的天数（仅对预付费盘有意义）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DifferDaysOfDeadline

    @DifferDaysOfDeadline.setter
    def DifferDaysOfDeadline(self, DifferDaysOfDeadline):
        self._DifferDaysOfDeadline = DifferDaysOfDeadline

    @property
    def ReturnFailCode(self):
        """预付费云盘在不支持主动退还的情况下，该参数表明不支持主动退还的具体原因。取值范围：<br><li>1：云硬盘已经退还<br><li>2：云硬盘已过期<br><li>3：云盘不支持退还<br><li>8：超过可退还数量的限制。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReturnFailCode

    @ReturnFailCode.setter
    def ReturnFailCode(self, ReturnFailCode):
        self._ReturnFailCode = ReturnFailCode

    @property
    def Shareable(self):
        """云盘是否为共享型云盘。
        :rtype: bool
        """
        return self._Shareable

    @Shareable.setter
    def Shareable(self, Shareable):
        self._Shareable = Shareable

    @property
    def CreateTime(self):
        """云硬盘的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeadlineTime(self):
        """云硬盘的到期时间。
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def AttachMode(self):
        """云盘的挂载类型。取值范围：<br><li>PF: PF挂载<br><li>VF: VF挂载
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttachMode

    @AttachMode.setter
    def AttachMode(self, AttachMode):
        self._AttachMode = AttachMode


    def _deserialize(self, params):
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._RenewFlag = params.get("RenewFlag")
        self._DiskType = params.get("DiskType")
        self._DiskState = params.get("DiskState")
        self._SnapshotCount = params.get("SnapshotCount")
        self._AutoRenewFlagError = params.get("AutoRenewFlagError")
        self._Rollbacking = params.get("Rollbacking")
        self._InstanceIdList = params.get("InstanceIdList")
        self._Encrypt = params.get("Encrypt")
        self._DiskName = params.get("DiskName")
        self._BackupDisk = params.get("BackupDisk")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._AutoSnapshotPolicyIds = params.get("AutoSnapshotPolicyIds")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        self._Migrating = params.get("Migrating")
        self._DiskId = params.get("DiskId")
        self._SnapshotSize = params.get("SnapshotSize")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._IsReturnable = params.get("IsReturnable")
        self._Attached = params.get("Attached")
        self._DiskSize = params.get("DiskSize")
        self._MigratePercent = params.get("MigratePercent")
        self._DiskUsage = params.get("DiskUsage")
        self._DiskChargeType = params.get("DiskChargeType")
        self._Portable = params.get("Portable")
        self._SnapshotAbility = params.get("SnapshotAbility")
        self._DeadlineError = params.get("DeadlineError")
        self._RollbackPercent = params.get("RollbackPercent")
        self._DifferDaysOfDeadline = params.get("DifferDaysOfDeadline")
        self._ReturnFailCode = params.get("ReturnFailCode")
        self._Shareable = params.get("Shareable")
        self._CreateTime = params.get("CreateTime")
        self._DeadlineTime = params.get("DeadlineTime")
        self._AttachMode = params.get("AttachMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买云盘的时长，默认单位为月，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费。
        :type RenewFlag: str
        :param _CurInstanceDeadline: 需要将云盘的到期时间与挂载的子机对齐时，可传入该参数。该参数表示子机当前的到期时间，此时Period如果传入，则表示子机需要续费的时长，云盘会自动按对齐到子机续费后的到期时间续费，示例取值：2018-03-30 20:15:03。
        :type CurInstanceDeadline: str
        """
        self._Period = None
        self._RenewFlag = None
        self._CurInstanceDeadline = None

    @property
    def Period(self):
        """购买云盘的时长，默认单位为月，取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        """自动续费标识。取值范围：<br><li>NOTIFY_AND_AUTO_RENEW：通知过期且自动续费<br><li>NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费<br><br>默认取值：NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费。
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def CurInstanceDeadline(self):
        """需要将云盘的到期时间与挂载的子机对齐时，可传入该参数。该参数表示子机当前的到期时间，此时Period如果传入，则表示子机需要续费的时长，云盘会自动按对齐到子机续费后的到期时间续费，示例取值：2018-03-30 20:15:03。
        :rtype: str
        """
        return self._CurInstanceDeadline

    @CurInstanceDeadline.setter
    def CurInstanceDeadline(self, CurInstanceDeadline):
        self._CurInstanceDeadline = CurInstanceDeadline


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._CurInstanceDeadline = params.get("CurInstanceDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiskInfo(AbstractModel):
    """磁盘信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 磁盘类型：LOCAL_BASIC
        :type DiskType: str
        :param _DiskId: 磁盘ID
        :type DiskId: str
        :param _DiskSize: 磁盘大小（GB）
        :type DiskSize: int
        :param _DeleteWithInstance: 是否随实例删除。
        :type DeleteWithInstance: bool
        :param _SnapshotId: 快照ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None
        self._DeleteWithInstance = None
        self._SnapshotId = None

    @property
    def DiskType(self):
        """磁盘类型：LOCAL_BASIC
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """磁盘ID
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        """磁盘大小（GB）
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DeleteWithInstance(self):
        """是否随实例删除。
        :rtype: bool
        """
        return self._DeleteWithInstance

    @DeleteWithInstance.setter
    def DeleteWithInstance(self, DeleteWithInstance):
        self._DeleteWithInstance = DeleteWithInstance

    @property
    def SnapshotId(self):
        """快照ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        self._DeleteWithInstance = params.get("DeleteWithInstance")
        self._SnapshotId = params.get("SnapshotId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipQuota(AbstractModel):
    """描述EIP配额信息

    """

    def __init__(self):
        r"""
        :param _QuotaId: 配额名称，取值范围：
TOTAL_EIP_QUOTA：用户当前地域下EIP的配额数；
DAILY_EIP_APPLY：用户当前地域下今日申购次数；
DAILY_PUBLIC_IP_ASSIGN：用户当前地域下，重新分配公网 IP次数。
        :type QuotaId: str
        :param _QuotaCurrent: 当前数量
        :type QuotaCurrent: int
        :param _QuotaLimit: 配额数量
        :type QuotaLimit: int
        """
        self._QuotaId = None
        self._QuotaCurrent = None
        self._QuotaLimit = None

    @property
    def QuotaId(self):
        """配额名称，取值范围：
TOTAL_EIP_QUOTA：用户当前地域下EIP的配额数；
DAILY_EIP_APPLY：用户当前地域下今日申购次数；
DAILY_PUBLIC_IP_ASSIGN：用户当前地域下，重新分配公网 IP次数。
        :rtype: str
        """
        return self._QuotaId

    @QuotaId.setter
    def QuotaId(self, QuotaId):
        self._QuotaId = QuotaId

    @property
    def QuotaCurrent(self):
        """当前数量
        :rtype: int
        """
        return self._QuotaCurrent

    @QuotaCurrent.setter
    def QuotaCurrent(self, QuotaCurrent):
        self._QuotaCurrent = QuotaCurrent

    @property
    def QuotaLimit(self):
        """配额数量
        :rtype: int
        """
        return self._QuotaLimit

    @QuotaLimit.setter
    def QuotaLimit(self, QuotaLimit):
        self._QuotaLimit = QuotaLimit


    def _deserialize(self, params):
        self._QuotaId = params.get("QuotaId")
        self._QuotaCurrent = params.get("QuotaCurrent")
        self._QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param _RouteIds: 路由策略ID。
        :type RouteIds: list of int non-negative
        """
        self._RouteTableId = None
        self._RouteIds = None

    @property
    def RouteTableId(self):
        """路由表唯一ID。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteIds(self):
        """路由策略ID。
        :rtype: list of int non-negative
        """
        return self._RouteIds

    @RouteIds.setter
    def RouteIds(self, RouteIds):
        self._RouteIds = RouteIds


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesResponse(AbstractModel):
    """EnableRoutes返回参数结构体

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


class EnhancedService(AbstractModel):
    """增强服务

    """

    def __init__(self):
        r"""
        :param _SecurityService: 是否开启云镜服务。
        :type SecurityService: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        :param _MonitorService: 是否开启云监控服务。
        :type MonitorService: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        :param _EIPDirectService: 是否开通IP直通。若不指定该参数，则Linux镜像默认开通，windows镜像暂不支持IP直通。
        :type EIPDirectService: :class:`tencentcloud.ecm.v20190719.models.RunEIPDirectServiceEnabled`
        """
        self._SecurityService = None
        self._MonitorService = None
        self._EIPDirectService = None

    @property
    def SecurityService(self):
        """是否开启云镜服务。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`
        """
        return self._SecurityService

    @SecurityService.setter
    def SecurityService(self, SecurityService):
        self._SecurityService = SecurityService

    @property
    def MonitorService(self):
        """是否开启云监控服务。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`
        """
        return self._MonitorService

    @MonitorService.setter
    def MonitorService(self, MonitorService):
        self._MonitorService = MonitorService

    @property
    def EIPDirectService(self):
        """是否开通IP直通。若不指定该参数，则Linux镜像默认开通，windows镜像暂不支持IP直通。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunEIPDirectServiceEnabled`
        """
        return self._EIPDirectService

    @EIPDirectService.setter
    def EIPDirectService(self, EIPDirectService):
        self._EIPDirectService = EIPDirectService


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self._SecurityService = RunSecurityServiceEnabled()
            self._SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self._MonitorService = RunMonitorServiceEnabled()
            self._MonitorService._deserialize(params.get("MonitorService"))
        if params.get("EIPDirectService") is not None:
            self._EIPDirectService = RunEIPDirectServiceEnabled()
            self._EIPDirectService._deserialize(params.get("EIPDirectService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    """

    def __init__(self):
        r"""
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        :param _Name: 过滤键的名称。
        :type Name: str
        """
        self._Values = None
        self._Name = None

    @property
    def Values(self):
        """一个或者多个过滤值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Name(self):
        """过滤键的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Values = params.get("Values")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVip(AbstractModel):
    """HAVIP对象。

    """

    def __init__(self):
        r"""
        :param _HaVipId: HAVIP的ID，是HAVIP的唯一标识。
        :type HaVipId: str
        :param _HaVipName: HAVIP名称。
        :type HaVipName: str
        :param _Vip: 虚拟IP地址。
        :type Vip: str
        :param _VpcId: HAVIP所在私有网络ID。
        :type VpcId: str
        :param _SubnetId: HAVIP所在子网ID。
        :type SubnetId: str
        :param _NetworkInterfaceId: HAVIP关联弹性网卡ID。
        :type NetworkInterfaceId: str
        :param _InstanceId: 被绑定的实例ID。
        :type InstanceId: str
        :param _AddressIp: 绑定EIP。
        :type AddressIp: str
        :param _State: 状态：
AVAILABLE：运行中。
UNBIND：未绑定。
        :type State: str
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _Business: 使用havip的业务标识。
        :type Business: str
        """
        self._HaVipId = None
        self._HaVipName = None
        self._Vip = None
        self._VpcId = None
        self._SubnetId = None
        self._NetworkInterfaceId = None
        self._InstanceId = None
        self._AddressIp = None
        self._State = None
        self._CreatedTime = None
        self._Business = None

    @property
    def HaVipId(self):
        """HAVIP的ID，是HAVIP的唯一标识。
        :rtype: str
        """
        return self._HaVipId

    @HaVipId.setter
    def HaVipId(self, HaVipId):
        self._HaVipId = HaVipId

    @property
    def HaVipName(self):
        """HAVIP名称。
        :rtype: str
        """
        return self._HaVipName

    @HaVipName.setter
    def HaVipName(self, HaVipName):
        self._HaVipName = HaVipName

    @property
    def Vip(self):
        """虚拟IP地址。
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def VpcId(self):
        """HAVIP所在私有网络ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """HAVIP所在子网ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def NetworkInterfaceId(self):
        """HAVIP关联弹性网卡ID。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def InstanceId(self):
        """被绑定的实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AddressIp(self):
        """绑定EIP。
        :rtype: str
        """
        return self._AddressIp

    @AddressIp.setter
    def AddressIp(self, AddressIp):
        self._AddressIp = AddressIp

    @property
    def State(self):
        """状态：
AVAILABLE：运行中。
UNBIND：未绑定。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreatedTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Business(self):
        """使用havip的业务标识。
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._HaVipId = params.get("HaVipId")
        self._HaVipName = params.get("HaVipName")
        self._Vip = params.get("Vip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._InstanceId = params.get("InstanceId")
        self._AddressIp = params.get("AddressIp")
        self._State = params.get("State")
        self._CreatedTime = params.get("CreatedTime")
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheck(AbstractModel):
    """负载均衡健康检查

    """

    def __init__(self):
        r"""
        :param _HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthSwitch: int
        :param _TimeOut: 健康检查的响应超时时间，可选值：2~60，默认值：2，单位：秒。响应超时时间要小于检查间隔时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeOut: int
        :param _IntervalTime: 健康检查探测间隔时间，默认值：5，可选值：5~300，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntervalTime: int
        :param _HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthNum: int
        :param _UnHealthyNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发异常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnHealthyNum: int
        :param _CheckPort: 自定义探测相关参数。健康检查端口，默认为后端服务的端口，除非您希望指定特定端口，否则建议留空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPort: int
        :param _ContextType: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContextType: str
        :param _SendContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。
注意：此字段可能返回 null，表示取不到有效值。
        :type SendContext: str
        :param _RecvContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecvContext: str
        :param _CheckType: 自定义探测相关参数。健康检查使用的协议：TCP | CUSTOM（UDP监听器只支持CUSTOM；如果使用自定义健康检查功能，则必传）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckType: str
        """
        self._HealthSwitch = None
        self._TimeOut = None
        self._IntervalTime = None
        self._HealthNum = None
        self._UnHealthyNum = None
        self._CheckPort = None
        self._ContextType = None
        self._SendContext = None
        self._RecvContext = None
        self._CheckType = None

    @property
    def HealthSwitch(self):
        """是否开启健康检查：1（开启）、0（关闭）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HealthSwitch

    @HealthSwitch.setter
    def HealthSwitch(self, HealthSwitch):
        self._HealthSwitch = HealthSwitch

    @property
    def TimeOut(self):
        """健康检查的响应超时时间，可选值：2~60，默认值：2，单位：秒。响应超时时间要小于检查间隔时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TimeOut

    @TimeOut.setter
    def TimeOut(self, TimeOut):
        self._TimeOut = TimeOut

    @property
    def IntervalTime(self):
        """健康检查探测间隔时间，默认值：5，可选值：5~300，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IntervalTime

    @IntervalTime.setter
    def IntervalTime(self, IntervalTime):
        self._IntervalTime = IntervalTime

    @property
    def HealthNum(self):
        """健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HealthNum

    @HealthNum.setter
    def HealthNum(self, HealthNum):
        self._HealthNum = HealthNum

    @property
    def UnHealthyNum(self):
        """不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发异常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UnHealthyNum

    @UnHealthyNum.setter
    def UnHealthyNum(self, UnHealthyNum):
        self._UnHealthyNum = UnHealthyNum

    @property
    def CheckPort(self):
        """自定义探测相关参数。健康检查端口，默认为后端服务的端口，除非您希望指定特定端口，否则建议留空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CheckPort

    @CheckPort.setter
    def CheckPort(self, CheckPort):
        self._CheckPort = CheckPort

    @property
    def ContextType(self):
        """自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContextType

    @ContextType.setter
    def ContextType(self, ContextType):
        self._ContextType = ContextType

    @property
    def SendContext(self):
        """自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SendContext

    @SendContext.setter
    def SendContext(self, SendContext):
        self._SendContext = SendContext

    @property
    def RecvContext(self):
        """自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecvContext

    @RecvContext.setter
    def RecvContext(self, RecvContext):
        self._RecvContext = RecvContext

    @property
    def CheckType(self):
        """自定义探测相关参数。健康检查使用的协议：TCP | CUSTOM（UDP监听器只支持CUSTOM；如果使用自定义健康检查功能，则必传）。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CheckType

    @CheckType.setter
    def CheckType(self, CheckType):
        self._CheckType = CheckType


    def _deserialize(self, params):
        self._HealthSwitch = params.get("HealthSwitch")
        self._TimeOut = params.get("TimeOut")
        self._IntervalTime = params.get("IntervalTime")
        self._HealthNum = params.get("HealthNum")
        self._UnHealthyNum = params.get("UnHealthyNum")
        self._CheckPort = params.get("CheckPort")
        self._ContextType = params.get("ContextType")
        self._SendContext = params.get("SendContext")
        self._RecvContext = params.get("RecvContext")
        self._CheckType = params.get("CheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISP(AbstractModel):
    """运营商信息

    """

    def __init__(self):
        r"""
        :param _ISPId: 运营商ID
        :type ISPId: str
        :param _ISPName: 运营商名称
        :type ISPName: str
        """
        self._ISPId = None
        self._ISPName = None

    @property
    def ISPId(self):
        """运营商ID
        :rtype: str
        """
        return self._ISPId

    @ISPId.setter
    def ISPId(self, ISPId):
        self._ISPId = ISPId

    @property
    def ISPName(self):
        """运营商名称
        :rtype: str
        """
        return self._ISPName

    @ISPName.setter
    def ISPName(self, ISPName):
        self._ISPName = ISPName


    def _deserialize(self, params):
        self._ISPId = params.get("ISPId")
        self._ISPName = params.get("ISPName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISPCounter(AbstractModel):
    """运行商统计信息

    """

    def __init__(self):
        r"""
        :param _ProviderName: 运营商名称
        :type ProviderName: str
        :param _ProviderNodeNum: 节点数量
        :type ProviderNodeNum: int
        :param _ProvederInstanceNum: 实例数量
        :type ProvederInstanceNum: int
        :param _ZoneInstanceInfoSet: Zone实例信息结构体数组
        :type ZoneInstanceInfoSet: list of ZoneInstanceInfo
        :param _ProviderInstanceNum: 实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ProviderInstanceNum: int
        """
        self._ProviderName = None
        self._ProviderNodeNum = None
        self._ProvederInstanceNum = None
        self._ZoneInstanceInfoSet = None
        self._ProviderInstanceNum = None

    @property
    def ProviderName(self):
        """运营商名称
        :rtype: str
        """
        return self._ProviderName

    @ProviderName.setter
    def ProviderName(self, ProviderName):
        self._ProviderName = ProviderName

    @property
    def ProviderNodeNum(self):
        """节点数量
        :rtype: int
        """
        return self._ProviderNodeNum

    @ProviderNodeNum.setter
    def ProviderNodeNum(self, ProviderNodeNum):
        self._ProviderNodeNum = ProviderNodeNum

    @property
    def ProvederInstanceNum(self):
        warnings.warn("parameter `ProvederInstanceNum` is deprecated", DeprecationWarning) 

        """实例数量
        :rtype: int
        """
        return self._ProvederInstanceNum

    @ProvederInstanceNum.setter
    def ProvederInstanceNum(self, ProvederInstanceNum):
        warnings.warn("parameter `ProvederInstanceNum` is deprecated", DeprecationWarning) 

        self._ProvederInstanceNum = ProvederInstanceNum

    @property
    def ZoneInstanceInfoSet(self):
        """Zone实例信息结构体数组
        :rtype: list of ZoneInstanceInfo
        """
        return self._ZoneInstanceInfoSet

    @ZoneInstanceInfoSet.setter
    def ZoneInstanceInfoSet(self, ZoneInstanceInfoSet):
        self._ZoneInstanceInfoSet = ZoneInstanceInfoSet

    @property
    def ProviderInstanceNum(self):
        """实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProviderInstanceNum

    @ProviderInstanceNum.setter
    def ProviderInstanceNum(self, ProviderInstanceNum):
        self._ProviderInstanceNum = ProviderInstanceNum


    def _deserialize(self, params):
        self._ProviderName = params.get("ProviderName")
        self._ProviderNodeNum = params.get("ProviderNodeNum")
        self._ProvederInstanceNum = params.get("ProvederInstanceNum")
        if params.get("ZoneInstanceInfoSet") is not None:
            self._ZoneInstanceInfoSet = []
            for item in params.get("ZoneInstanceInfoSet"):
                obj = ZoneInstanceInfo()
                obj._deserialize(item)
                self._ZoneInstanceInfoSet.append(obj)
        self._ProviderInstanceNum = params.get("ProviderInstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISPIPv6CidrBlock(AbstractModel):
    """多运营商IPv6 Cidr Block

    """

    def __init__(self):
        r"""
        :param _IPv6CidrBlock: IPv6 CIdr Block。
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6CidrBlock: str
        :param _ISPType: 网络运营商类型 取值范围:'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
注意：此字段可能返回 null，表示取不到有效值。
        :type ISPType: str
        """
        self._IPv6CidrBlock = None
        self._ISPType = None

    @property
    def IPv6CidrBlock(self):
        """IPv6 CIdr Block。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IPv6CidrBlock

    @IPv6CidrBlock.setter
    def IPv6CidrBlock(self, IPv6CidrBlock):
        self._IPv6CidrBlock = IPv6CidrBlock

    @property
    def ISPType(self):
        """网络运营商类型 取值范围:'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ISPType

    @ISPType.setter
    def ISPType(self, ISPType):
        self._ISPType = ISPType


    def _deserialize(self, params):
        self._IPv6CidrBlock = params.get("IPv6CidrBlock")
        self._ISPType = params.get("ISPType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISPTypeItem(AbstractModel):
    """申请ipv6 cidr block的信息

    """

    def __init__(self):
        r"""
        :param _ISPType: IPv6 Cidr所属运营商类型，支持的类型有 'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调。作为入参数时为必选。
        :type ISPType: str
        :param _Count: 申请IPv6 Cidr Block的个数。作为入参数时为必选。
        :type Count: int
        """
        self._ISPType = None
        self._Count = None

    @property
    def ISPType(self):
        """IPv6 Cidr所属运营商类型，支持的类型有 'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调。作为入参数时为必选。
        :rtype: str
        """
        return self._ISPType

    @ISPType.setter
    def ISPType(self, ISPType):
        self._ISPType = ISPType

    @property
    def Count(self):
        """申请IPv6 Cidr Block的个数。作为入参数时为必选。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._ISPType = params.get("ISPType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _ImageState: 镜像状态
        :type ImageState: str
        :param _ImageType: 镜像类型
        :type ImageType: str
        :param _ImageOsName: 操作系统名称
        :type ImageOsName: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        :param _ImageCreateTime: 镜像导入时间
        :type ImageCreateTime: str
        :param _Architecture: 操作系统位数
        :type Architecture: str
        :param _OsType: 操作系统类型
        :type OsType: str
        :param _OsVersion: 操作系统版本
        :type OsVersion: str
        :param _Platform: 操作系统平台
        :type Platform: str
        :param _ImageOwner: 镜像所有者
        :type ImageOwner: int
        :param _ImageSize: 镜像大小。单位：GB
        :type ImageSize: int
        :param _SrcImage: 镜像来源信息
        :type SrcImage: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        :param _ImageSource: 镜像来源类型
        :type ImageSource: str
        :param _TaskId: 中间态和失败时候的任务ID
        :type TaskId: str
        :param _IsSupportCloudInit: 是否支持CloudInit
        :type IsSupportCloudInit: bool
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageState = None
        self._ImageType = None
        self._ImageOsName = None
        self._ImageDescription = None
        self._ImageCreateTime = None
        self._Architecture = None
        self._OsType = None
        self._OsVersion = None
        self._Platform = None
        self._ImageOwner = None
        self._ImageSize = None
        self._SrcImage = None
        self._ImageSource = None
        self._TaskId = None
        self._IsSupportCloudInit = None

    @property
    def ImageId(self):
        """镜像ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        """镜像名称
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageState(self):
        """镜像状态
        :rtype: str
        """
        return self._ImageState

    @ImageState.setter
    def ImageState(self, ImageState):
        self._ImageState = ImageState

    @property
    def ImageType(self):
        """镜像类型
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType

    @property
    def ImageOsName(self):
        """操作系统名称
        :rtype: str
        """
        return self._ImageOsName

    @ImageOsName.setter
    def ImageOsName(self, ImageOsName):
        self._ImageOsName = ImageOsName

    @property
    def ImageDescription(self):
        """镜像描述
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def ImageCreateTime(self):
        """镜像导入时间
        :rtype: str
        """
        return self._ImageCreateTime

    @ImageCreateTime.setter
    def ImageCreateTime(self, ImageCreateTime):
        self._ImageCreateTime = ImageCreateTime

    @property
    def Architecture(self):
        """操作系统位数
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def OsType(self):
        """操作系统类型
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsVersion(self):
        """操作系统版本
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def Platform(self):
        """操作系统平台
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ImageOwner(self):
        """镜像所有者
        :rtype: int
        """
        return self._ImageOwner

    @ImageOwner.setter
    def ImageOwner(self, ImageOwner):
        self._ImageOwner = ImageOwner

    @property
    def ImageSize(self):
        """镜像大小。单位：GB
        :rtype: int
        """
        return self._ImageSize

    @ImageSize.setter
    def ImageSize(self, ImageSize):
        self._ImageSize = ImageSize

    @property
    def SrcImage(self):
        """镜像来源信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SrcImage`
        """
        return self._SrcImage

    @SrcImage.setter
    def SrcImage(self, SrcImage):
        self._SrcImage = SrcImage

    @property
    def ImageSource(self):
        """镜像来源类型
        :rtype: str
        """
        return self._ImageSource

    @ImageSource.setter
    def ImageSource(self, ImageSource):
        self._ImageSource = ImageSource

    @property
    def TaskId(self):
        """中间态和失败时候的任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def IsSupportCloudInit(self):
        """是否支持CloudInit
        :rtype: bool
        """
        return self._IsSupportCloudInit

    @IsSupportCloudInit.setter
    def IsSupportCloudInit(self, IsSupportCloudInit):
        self._IsSupportCloudInit = IsSupportCloudInit


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageState = params.get("ImageState")
        self._ImageType = params.get("ImageType")
        self._ImageOsName = params.get("ImageOsName")
        self._ImageDescription = params.get("ImageDescription")
        self._ImageCreateTime = params.get("ImageCreateTime")
        self._Architecture = params.get("Architecture")
        self._OsType = params.get("OsType")
        self._OsVersion = params.get("OsVersion")
        self._Platform = params.get("Platform")
        self._ImageOwner = params.get("ImageOwner")
        self._ImageSize = params.get("ImageSize")
        if params.get("SrcImage") is not None:
            self._SrcImage = SrcImage()
            self._SrcImage._deserialize(params.get("SrcImage"))
        self._ImageSource = params.get("ImageSource")
        self._TaskId = params.get("TaskId")
        self._IsSupportCloudInit = params.get("IsSupportCloudInit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageLimitConfig(AbstractModel):
    """镜像限制配置

    """

    def __init__(self):
        r"""
        :param _MaxImageSize: 支持的最大镜像大小，包括可导入的自定义镜像大小，中心云镜像大小，单位为GB。
        :type MaxImageSize: int
        """
        self._MaxImageSize = None

    @property
    def MaxImageSize(self):
        """支持的最大镜像大小，包括可导入的自定义镜像大小，中心云镜像大小，单位为GB。
        :rtype: int
        """
        return self._MaxImageSize

    @MaxImageSize.setter
    def MaxImageSize(self, MaxImageSize):
        self._MaxImageSize = MaxImageSize


    def _deserialize(self, params):
        self._MaxImageSize = params.get("MaxImageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """支持的操作系统类型，根据windows和Linux分类。

    """

    def __init__(self):
        r"""
        :param _Windows: 支持的windows操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Windows: list of str
        :param _Linux: 支持的linux操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type Linux: list of str
        """
        self._Windows = None
        self._Linux = None

    @property
    def Windows(self):
        """支持的windows操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Windows

    @Windows.setter
    def Windows(self, Windows):
        self._Windows = Windows

    @property
    def Linux(self):
        """支持的linux操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Linux

    @Linux.setter
    def Linux(self, Linux):
        self._Linux = Linux


    def _deserialize(self, params):
        self._Windows = params.get("Windows")
        self._Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTask(AbstractModel):
    """镜像任务

    """

    def __init__(self):
        r"""
        :param _State: 镜像导入状态， PENDING, PROCESSING, SUCCESS, FAILED
        :type State: str
        :param _Message: 导入失败(FAILED)时， 说明失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._State = None
        self._Message = None
        self._ImageName = None
        self._CreateTime = None

    @property
    def State(self):
        """镜像导入状态， PENDING, PROCESSING, SUCCESS, FAILED
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Message(self):
        """导入失败(FAILED)时， 说明失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ImageName(self):
        """镜像名称
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._State = params.get("State")
        self._Message = params.get("Message")
        self._ImageName = params.get("ImageName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageUrl(AbstractModel):
    """镜像文件信息

    """

    def __init__(self):
        r"""
        :param _ImageFile: 镜像文件COS链接，如设置私有读写，需授权腾讯云ECM运营账号访问权限。
        :type ImageFile: str
        """
        self._ImageFile = None

    @property
    def ImageFile(self):
        """镜像文件COS链接，如设置私有读写，需授权腾讯云ECM运营账号访问权限。
        :rtype: str
        """
        return self._ImageFile

    @ImageFile.setter
    def ImageFile(self, ImageFile):
        self._ImageFile = ImageFile


    def _deserialize(self, params):
        self._ImageFile = params.get("ImageFile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportCustomImageRequest(AbstractModel):
    """ImportCustomImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _Architecture: 导入镜像的操作系统架构，x86_64 或 i386
        :type Architecture: str
        :param _OsType: 导入镜像的操作系统类型，通过DescribeImportImageOs获取
        :type OsType: str
        :param _OsVersion: 导入镜像的操作系统版本，通过DescribeImportImageOs获取
        :type OsVersion: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        :param _InitFlag: 镜像启动方式，cloudinit或nbd， 默认cloudinit
        :type InitFlag: str
        :param _ImageUrls: 镜像文件描述，多层镜像按顺序传入
        :type ImageUrls: list of ImageUrl
        """
        self._ImageName = None
        self._Architecture = None
        self._OsType = None
        self._OsVersion = None
        self._ImageDescription = None
        self._InitFlag = None
        self._ImageUrls = None

    @property
    def ImageName(self):
        """镜像名称
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def Architecture(self):
        """导入镜像的操作系统架构，x86_64 或 i386
        :rtype: str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture

    @property
    def OsType(self):
        """导入镜像的操作系统类型，通过DescribeImportImageOs获取
        :rtype: str
        """
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OsVersion(self):
        """导入镜像的操作系统版本，通过DescribeImportImageOs获取
        :rtype: str
        """
        return self._OsVersion

    @OsVersion.setter
    def OsVersion(self, OsVersion):
        self._OsVersion = OsVersion

    @property
    def ImageDescription(self):
        """镜像描述
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def InitFlag(self):
        """镜像启动方式，cloudinit或nbd， 默认cloudinit
        :rtype: str
        """
        return self._InitFlag

    @InitFlag.setter
    def InitFlag(self, InitFlag):
        self._InitFlag = InitFlag

    @property
    def ImageUrls(self):
        """镜像文件描述，多层镜像按顺序传入
        :rtype: list of ImageUrl
        """
        return self._ImageUrls

    @ImageUrls.setter
    def ImageUrls(self, ImageUrls):
        self._ImageUrls = ImageUrls


    def _deserialize(self, params):
        self._ImageName = params.get("ImageName")
        self._Architecture = params.get("Architecture")
        self._OsType = params.get("OsType")
        self._OsVersion = params.get("OsVersion")
        self._ImageDescription = params.get("ImageDescription")
        self._InitFlag = params.get("InitFlag")
        if params.get("ImageUrls") is not None:
            self._ImageUrls = []
            for item in params.get("ImageUrls"):
                obj = ImageUrl()
                obj._deserialize(item)
                self._ImageUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportCustomImageResponse(AbstractModel):
    """ImportCustomImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID
        :type ImageId: str
        :param _TaskId: 异步任务ID，可根据DescribeCustomImageTask查询任务信息
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImageId = None
        self._TaskId = None
        self._RequestId = None

    @property
    def ImageId(self):
        """镜像ID
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def TaskId(self):
        """异步任务ID，可根据DescribeCustomImageTask查询任务信息
        :rtype: int
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
        self._ImageId = params.get("ImageId")
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ImportImageRequest(AbstractModel):
    """ImportImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像的Id。
        :type ImageId: str
        :param _ImageDescription: 镜像的描述。
        :type ImageDescription: str
        :param _SourceRegion: 源地域
        :type SourceRegion: str
        """
        self._ImageId = None
        self._ImageDescription = None
        self._SourceRegion = None

    @property
    def ImageId(self):
        """镜像的Id。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageDescription(self):
        """镜像的描述。
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

    @property
    def SourceRegion(self):
        """源地域
        :rtype: str
        """
        return self._SourceRegion

    @SourceRegion.setter
    def SourceRegion(self, SourceRegion):
        self._SourceRegion = SourceRegion


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageDescription = params.get("ImageDescription")
        self._SourceRegion = params.get("SourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage返回参数结构体

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


class Instance(AbstractModel):
    """用于描述实例相关的信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _InstanceName: 实例名称，如ens-34241f3s。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _InstanceState: 实例状态。取值范围：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
STOPPED：表示关机
STARTING：表示开机中
STOPPING：表示关机中
REBOOTING：表示重启中
SHUTDOWN：表示停止待销毁
TERMINATING：表示销毁中。
        :type InstanceState: str
        :param _Image: 实例当前使用的镜像的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param _SimpleModule: 实例当前所属的模块简要信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SimpleModule: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        :param _Position: 实例所在的位置相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param _Internet: 实例的网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Internet: :class:`tencentcloud.ecm.v20190719.models.Internet`
        :param _InstanceTypeConfig: 实例的配置相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param _CreateTime: 实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _TagSet: 实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param _LatestOperation: 实例最后一次操作。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperation: str
        :param _LatestOperationState: 实例最后一次操作结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param _RestrictState: 实例业务状态。取值范围：
NORMAL：表示正常状态的实例
EXPIRED：表示过期的实例
PROTECTIVELY_ISOLATED：表示被安全隔离的实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type RestrictState: str
        :param _SystemDiskSize: 系统盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDiskSize: int
        :param _DataDiskSize: 数据盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDiskSize: int
        :param _UUID: 实例UUID
注意：此字段可能返回 null，表示取不到有效值。
        :type UUID: str
        :param _PayMode: 付费方式。
    0为后付费。
    1为预付费。
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param _ExpireTime: 过期时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _IsolatedTime: 隔离时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolatedTime: str
        :param _RenewFlag: 是否自动续费。
      0为不自动续费。
      1为自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _ExpireState: 过期状态。
    NORMAL 表示机器运行正常。
    WILL_EXPIRE 表示即将过期。
    EXPIRED 表示已过期。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireState: str
        :param _SystemDisk: 系统盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        :param _DataDisks: 数据盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DiskInfo
        :param _NewFlag: 新实例标志
注意：此字段可能返回 null，表示取不到有效值。
        :type NewFlag: int
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param _VirtualPrivateCloud: VPC属性
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.ecm.v20190719.models.VirtualPrivateCloud`
        :param _ISP: 实例运营商字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type ISP: str
        :param _PhysicalPosition: 物理位置信息。注意该字段目前为保留字段，均为空值。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalPosition: :class:`tencentcloud.ecm.v20190719.models.PhysicalPosition`
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceState = None
        self._Image = None
        self._SimpleModule = None
        self._Position = None
        self._Internet = None
        self._InstanceTypeConfig = None
        self._CreateTime = None
        self._TagSet = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._RestrictState = None
        self._SystemDiskSize = None
        self._DataDiskSize = None
        self._UUID = None
        self._PayMode = None
        self._ExpireTime = None
        self._IsolatedTime = None
        self._RenewFlag = None
        self._ExpireState = None
        self._SystemDisk = None
        self._DataDisks = None
        self._NewFlag = None
        self._SecurityGroupIds = None
        self._VirtualPrivateCloud = None
        self._ISP = None
        self._PhysicalPosition = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称，如ens-34241f3s。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceState(self):
        """实例状态。取值范围：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
STOPPED：表示关机
STARTING：表示开机中
STOPPING：表示关机中
REBOOTING：表示重启中
SHUTDOWN：表示停止待销毁
TERMINATING：表示销毁中。
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Image(self):
        """实例当前使用的镜像的信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Image`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def SimpleModule(self):
        """实例当前所属的模块简要信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`
        """
        return self._SimpleModule

    @SimpleModule.setter
    def SimpleModule(self, SimpleModule):
        self._SimpleModule = SimpleModule

    @property
    def Position(self):
        """实例所在的位置相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Position`
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Internet(self):
        """实例的网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Internet`
        """
        return self._Internet

    @Internet.setter
    def Internet(self, Internet):
        self._Internet = Internet

    @property
    def InstanceTypeConfig(self):
        """实例的配置相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        """
        return self._InstanceTypeConfig

    @InstanceTypeConfig.setter
    def InstanceTypeConfig(self, InstanceTypeConfig):
        self._InstanceTypeConfig = InstanceTypeConfig

    @property
    def CreateTime(self):
        """实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def TagSet(self):
        """实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def LatestOperation(self):
        """实例最后一次操作。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        """实例最后一次操作结果。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def RestrictState(self):
        """实例业务状态。取值范围：
NORMAL：表示正常状态的实例
EXPIRED：表示过期的实例
PROTECTIVELY_ISOLATED：表示被安全隔离的实例。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RestrictState

    @RestrictState.setter
    def RestrictState(self, RestrictState):
        self._RestrictState = RestrictState

    @property
    def SystemDiskSize(self):
        """系统盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def DataDiskSize(self):
        """数据盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def UUID(self):
        """实例UUID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UUID

    @UUID.setter
    def UUID(self, UUID):
        self._UUID = UUID

    @property
    def PayMode(self):
        """付费方式。
    0为后付费。
    1为预付费。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpireTime(self):
        """过期时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def IsolatedTime(self):
        """隔离时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IsolatedTime

    @IsolatedTime.setter
    def IsolatedTime(self, IsolatedTime):
        self._IsolatedTime = IsolatedTime

    @property
    def RenewFlag(self):
        """是否自动续费。
      0为不自动续费。
      1为自动续费。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpireState(self):
        """过期状态。
    NORMAL 表示机器运行正常。
    WILL_EXPIRE 表示即将过期。
    EXPIRED 表示已过期。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireState

    @ExpireState.setter
    def ExpireState(self, ExpireState):
        self._ExpireState = ExpireState

    @property
    def SystemDisk(self):
        """系统盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """数据盘信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DiskInfo
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def NewFlag(self):
        """新实例标志
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NewFlag

    @NewFlag.setter
    def NewFlag(self, NewFlag):
        self._NewFlag = NewFlag

    @property
    def SecurityGroupIds(self):
        """实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def VirtualPrivateCloud(self):
        """VPC属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.VirtualPrivateCloud`
        """
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ISP(self):
        """实例运营商字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def PhysicalPosition(self):
        """物理位置信息。注意该字段目前为保留字段，均为空值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PhysicalPosition`
        """
        return self._PhysicalPosition

    @PhysicalPosition.setter
    def PhysicalPosition(self, PhysicalPosition):
        self._PhysicalPosition = PhysicalPosition


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceState = params.get("InstanceState")
        if params.get("Image") is not None:
            self._Image = Image()
            self._Image._deserialize(params.get("Image"))
        if params.get("SimpleModule") is not None:
            self._SimpleModule = SimpleModule()
            self._SimpleModule._deserialize(params.get("SimpleModule"))
        if params.get("Position") is not None:
            self._Position = Position()
            self._Position._deserialize(params.get("Position"))
        if params.get("Internet") is not None:
            self._Internet = Internet()
            self._Internet._deserialize(params.get("Internet"))
        if params.get("InstanceTypeConfig") is not None:
            self._InstanceTypeConfig = InstanceTypeConfig()
            self._InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        self._CreateTime = params.get("CreateTime")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._RestrictState = params.get("RestrictState")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._DataDiskSize = params.get("DataDiskSize")
        self._UUID = params.get("UUID")
        self._PayMode = params.get("PayMode")
        self._ExpireTime = params.get("ExpireTime")
        self._IsolatedTime = params.get("IsolatedTime")
        self._RenewFlag = params.get("RenewFlag")
        self._ExpireState = params.get("ExpireState")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = DiskInfo()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskInfo()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._NewFlag = params.get("NewFlag")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ISP = params.get("ISP")
        if params.get("PhysicalPosition") is not None:
            self._PhysicalPosition = PhysicalPosition()
            self._PhysicalPosition._deserialize(params.get("PhysicalPosition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """机型族配置

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyName: 机型名称
        :type InstanceFamilyName: str
        :param _InstanceFamily: 机型ID
        :type InstanceFamily: str
        """
        self._InstanceFamilyName = None
        self._InstanceFamily = None

    @property
    def InstanceFamilyName(self):
        """机型名称
        :rtype: str
        """
        return self._InstanceFamilyName

    @InstanceFamilyName.setter
    def InstanceFamilyName(self, InstanceFamilyName):
        self._InstanceFamilyName = InstanceFamilyName

    @property
    def InstanceFamily(self):
        """机型ID
        :rtype: str
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily


    def _deserialize(self, params):
        self._InstanceFamilyName = params.get("InstanceFamilyName")
        self._InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyTypeConfig(AbstractModel):
    """实例系列类型配置

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyType: 实例机型系列类型Id
        :type InstanceFamilyType: str
        :param _InstanceFamilyTypeName: 实例机型系列类型名称
        :type InstanceFamilyTypeName: str
        """
        self._InstanceFamilyType = None
        self._InstanceFamilyTypeName = None

    @property
    def InstanceFamilyType(self):
        """实例机型系列类型Id
        :rtype: str
        """
        return self._InstanceFamilyType

    @InstanceFamilyType.setter
    def InstanceFamilyType(self, InstanceFamilyType):
        self._InstanceFamilyType = InstanceFamilyType

    @property
    def InstanceFamilyTypeName(self):
        """实例机型系列类型名称
        :rtype: str
        """
        return self._InstanceFamilyTypeName

    @InstanceFamilyTypeName.setter
    def InstanceFamilyTypeName(self, InstanceFamilyTypeName):
        self._InstanceFamilyTypeName = InstanceFamilyTypeName


    def _deserialize(self, params):
        self._InstanceFamilyType = params.get("InstanceFamilyType")
        self._InstanceFamilyTypeName = params.get("InstanceFamilyTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkInfo(AbstractModel):
    """实例网卡ip网络信息数组

    """

    def __init__(self):
        r"""
        :param _AddressInfoSet: 实例内外网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressInfoSet: list of AddressInfo
        :param _NetworkInterfaceId: 网卡ID。
        :type NetworkInterfaceId: str
        :param _NetworkInterfaceName: 网卡名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkInterfaceName: str
        :param _Primary: 主网卡属性。true为主网卡，false为辅助网卡。
        :type Primary: bool
        """
        self._AddressInfoSet = None
        self._NetworkInterfaceId = None
        self._NetworkInterfaceName = None
        self._Primary = None

    @property
    def AddressInfoSet(self):
        """实例内外网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AddressInfo
        """
        return self._AddressInfoSet

    @AddressInfoSet.setter
    def AddressInfoSet(self, AddressInfoSet):
        self._AddressInfoSet = AddressInfoSet

    @property
    def NetworkInterfaceId(self):
        """网卡ID。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def NetworkInterfaceName(self):
        """网卡名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NetworkInterfaceName

    @NetworkInterfaceName.setter
    def NetworkInterfaceName(self, NetworkInterfaceName):
        self._NetworkInterfaceName = NetworkInterfaceName

    @property
    def Primary(self):
        """主网卡属性。true为主网卡，false为辅助网卡。
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary


    def _deserialize(self, params):
        if params.get("AddressInfoSet") is not None:
            self._AddressInfoSet = []
            for item in params.get("AddressInfoSet"):
                obj = AddressInfo()
                obj._deserialize(item)
                self._AddressInfoSet.append(obj)
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._NetworkInterfaceName = params.get("NetworkInterfaceName")
        self._Primary = params.get("Primary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkLimitConfig(AbstractModel):
    """机器网络资源限制

    """

    def __init__(self):
        r"""
        :param _CpuNum: cpu核数
        :type CpuNum: int
        :param _NetworkInterfaceLimit: 网卡数量限制
        :type NetworkInterfaceLimit: int
        :param _InnerIpPerNetworkInterface: 每张网卡内网ip数量限制
        :type InnerIpPerNetworkInterface: int
        :param _PublicIpPerInstance: 每个实例的外网ip限制
        :type PublicIpPerInstance: int
        """
        self._CpuNum = None
        self._NetworkInterfaceLimit = None
        self._InnerIpPerNetworkInterface = None
        self._PublicIpPerInstance = None

    @property
    def CpuNum(self):
        """cpu核数
        :rtype: int
        """
        return self._CpuNum

    @CpuNum.setter
    def CpuNum(self, CpuNum):
        self._CpuNum = CpuNum

    @property
    def NetworkInterfaceLimit(self):
        """网卡数量限制
        :rtype: int
        """
        return self._NetworkInterfaceLimit

    @NetworkInterfaceLimit.setter
    def NetworkInterfaceLimit(self, NetworkInterfaceLimit):
        self._NetworkInterfaceLimit = NetworkInterfaceLimit

    @property
    def InnerIpPerNetworkInterface(self):
        """每张网卡内网ip数量限制
        :rtype: int
        """
        return self._InnerIpPerNetworkInterface

    @InnerIpPerNetworkInterface.setter
    def InnerIpPerNetworkInterface(self, InnerIpPerNetworkInterface):
        self._InnerIpPerNetworkInterface = InnerIpPerNetworkInterface

    @property
    def PublicIpPerInstance(self):
        """每个实例的外网ip限制
        :rtype: int
        """
        return self._PublicIpPerInstance

    @PublicIpPerInstance.setter
    def PublicIpPerInstance(self, PublicIpPerInstance):
        self._PublicIpPerInstance = PublicIpPerInstance


    def _deserialize(self, params):
        self._CpuNum = params.get("CpuNum")
        self._NetworkInterfaceLimit = params.get("NetworkInterfaceLimit")
        self._InnerIpPerNetworkInterface = params.get("InnerIpPerNetworkInterface")
        self._PublicIpPerInstance = params.get("PublicIpPerInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperator(AbstractModel):
    """实例可执行操作

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _DeniedActions: 实例禁止的操作
注意：此字段可能返回 null，表示取不到有效值。
        :type DeniedActions: list of OperatorAction
        """
        self._InstanceId = None
        self._DeniedActions = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeniedActions(self):
        """实例禁止的操作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OperatorAction
        """
        return self._DeniedActions

    @DeniedActions.setter
    def DeniedActions(self, DeniedActions):
        self._DeniedActions = DeniedActions


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self._DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = OperatorAction()
                obj._deserialize(item)
                self._DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePricesPartDetail(AbstractModel):
    """描述实例的价格相关

    """

    def __init__(self):
        r"""
        :param _CpuPrice: cpu的价格信息
        :type CpuPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        :param _MemPrice: 内存价格信息
        :type MemPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        :param _DisksPrice: 磁盘价格信息
        :type DisksPrice: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        self._CpuPrice = None
        self._MemPrice = None
        self._DisksPrice = None

    @property
    def CpuPrice(self):
        """cpu的价格信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        return self._CpuPrice

    @CpuPrice.setter
    def CpuPrice(self, CpuPrice):
        self._CpuPrice = CpuPrice

    @property
    def MemPrice(self):
        """内存价格信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        return self._MemPrice

    @MemPrice.setter
    def MemPrice(self, MemPrice):
        self._MemPrice = MemPrice

    @property
    def DisksPrice(self):
        """磁盘价格信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.PriceDetail`
        """
        return self._DisksPrice

    @DisksPrice.setter
    def DisksPrice(self, DisksPrice):
        self._DisksPrice = DisksPrice


    def _deserialize(self, params):
        if params.get("CpuPrice") is not None:
            self._CpuPrice = PriceDetail()
            self._CpuPrice._deserialize(params.get("CpuPrice"))
        if params.get("MemPrice") is not None:
            self._MemPrice = PriceDetail()
            self._MemPrice._deserialize(params.get("MemPrice"))
        if params.get("DisksPrice") is not None:
            self._DisksPrice = PriceDetail()
            self._DisksPrice._deserialize(params.get("DisksPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatistic(AbstractModel):
    """用于描述实例的统计信息

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例的类型
        :type InstanceType: str
        :param _InstanceCount: 实例的个数
        :type InstanceCount: int
        """
        self._InstanceType = None
        self._InstanceCount = None

    @property
    def InstanceType(self):
        """实例的类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCount(self):
        """实例的个数
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfig(AbstractModel):
    """机型配置

    """

    def __init__(self):
        r"""
        :param _InstanceFamilyConfig: 机型族配置信息
        :type InstanceFamilyConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        :param _InstanceType: 机型
        :type InstanceType: str
        :param _Vcpu: CPU核数
        :type Vcpu: int
        :param _Memory: 内存大小
        :type Memory: int
        :param _Frequency: 主频
        :type Frequency: str
        :param _CpuModelName: 处理器型号
        :type CpuModelName: str
        :param _InstanceFamilyTypeConfig: 机型族类别配置信息
        :type InstanceFamilyTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param _ExtInfo: 机型额外信息 是一个json字符串，如果存在则表示特殊机型，格式如下：{"dataDiskSize":3200,"systemDiskSize":60, "systemDiskSizeShow":"系统盘默认60G","dataDiskSizeShow":"本地NVMe SSD 硬盘3200 GB"}
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtInfo: str
        :param _Vgpu: GPU卡数
注意：此字段可能返回 null，表示取不到有效值。
        :type Vgpu: float
        :param _GpuModelName: GPU型号
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuModelName: str
        """
        self._InstanceFamilyConfig = None
        self._InstanceType = None
        self._Vcpu = None
        self._Memory = None
        self._Frequency = None
        self._CpuModelName = None
        self._InstanceFamilyTypeConfig = None
        self._ExtInfo = None
        self._Vgpu = None
        self._GpuModelName = None

    @property
    def InstanceFamilyConfig(self):
        """机型族配置信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`
        """
        return self._InstanceFamilyConfig

    @InstanceFamilyConfig.setter
    def InstanceFamilyConfig(self, InstanceFamilyConfig):
        self._InstanceFamilyConfig = InstanceFamilyConfig

    @property
    def InstanceType(self):
        """机型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Vcpu(self):
        """CPU核数
        :rtype: int
        """
        return self._Vcpu

    @Vcpu.setter
    def Vcpu(self, Vcpu):
        self._Vcpu = Vcpu

    @property
    def Memory(self):
        """内存大小
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Frequency(self):
        """主频
        :rtype: str
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def CpuModelName(self):
        """处理器型号
        :rtype: str
        """
        return self._CpuModelName

    @CpuModelName.setter
    def CpuModelName(self, CpuModelName):
        self._CpuModelName = CpuModelName

    @property
    def InstanceFamilyTypeConfig(self):
        """机型族类别配置信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        """
        return self._InstanceFamilyTypeConfig

    @InstanceFamilyTypeConfig.setter
    def InstanceFamilyTypeConfig(self, InstanceFamilyTypeConfig):
        self._InstanceFamilyTypeConfig = InstanceFamilyTypeConfig

    @property
    def ExtInfo(self):
        """机型额外信息 是一个json字符串，如果存在则表示特殊机型，格式如下：{"dataDiskSize":3200,"systemDiskSize":60, "systemDiskSizeShow":"系统盘默认60G","dataDiskSizeShow":"本地NVMe SSD 硬盘3200 GB"}
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExtInfo

    @ExtInfo.setter
    def ExtInfo(self, ExtInfo):
        self._ExtInfo = ExtInfo

    @property
    def Vgpu(self):
        """GPU卡数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Vgpu

    @Vgpu.setter
    def Vgpu(self, Vgpu):
        self._Vgpu = Vgpu

    @property
    def GpuModelName(self):
        """GPU型号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GpuModelName

    @GpuModelName.setter
    def GpuModelName(self, GpuModelName):
        self._GpuModelName = GpuModelName


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfig") is not None:
            self._InstanceFamilyConfig = InstanceFamilyConfig()
            self._InstanceFamilyConfig._deserialize(params.get("InstanceFamilyConfig"))
        self._InstanceType = params.get("InstanceType")
        self._Vcpu = params.get("Vcpu")
        self._Memory = params.get("Memory")
        self._Frequency = params.get("Frequency")
        self._CpuModelName = params.get("CpuModelName")
        if params.get("InstanceFamilyTypeConfig") is not None:
            self._InstanceFamilyTypeConfig = InstanceFamilyTypeConfig()
            self._InstanceFamilyTypeConfig._deserialize(params.get("InstanceFamilyTypeConfig"))
        self._ExtInfo = params.get("ExtInfo")
        self._Vgpu = params.get("Vgpu")
        self._GpuModelName = params.get("GpuModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancesPrice(AbstractModel):
    """实例价格信息

    """

    def __init__(self):
        r"""
        :param _InstancePricesPartDetail: 分部描述实例子维度的价格
        :type InstancePricesPartDetail: :class:`tencentcloud.ecm.v20190719.models.InstancePricesPartDetail`
        :param _Discount: 实例总价折扣
        :type Discount: int
        :param _DiscountPrice: 折扣后价格
        :type DiscountPrice: int
        :param _OriginalPrice: 折扣前价格，原始总价
        :type OriginalPrice: int
        """
        self._InstancePricesPartDetail = None
        self._Discount = None
        self._DiscountPrice = None
        self._OriginalPrice = None

    @property
    def InstancePricesPartDetail(self):
        """分部描述实例子维度的价格
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstancePricesPartDetail`
        """
        return self._InstancePricesPartDetail

    @InstancePricesPartDetail.setter
    def InstancePricesPartDetail(self, InstancePricesPartDetail):
        self._InstancePricesPartDetail = InstancePricesPartDetail

    @property
    def Discount(self):
        """实例总价折扣
        :rtype: int
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        """折扣后价格
        :rtype: int
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def OriginalPrice(self):
        """折扣前价格，原始总价
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice


    def _deserialize(self, params):
        if params.get("InstancePricesPartDetail") is not None:
            self._InstancePricesPartDetail = InstancePricesPartDetail()
            self._InstancePricesPartDetail._deserialize(params.get("InstancePricesPartDetail"))
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Internet(AbstractModel):
    """实例的网络相关信息。

    """

    def __init__(self):
        r"""
        :param _PrivateIPAddressSet: 实例的内网相关信息列表。顺序为主网卡在前，辅助网卡按绑定先后顺序排列。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIPAddressSet: list of PrivateIPAddressInfo
        :param _PublicIPAddressSet: 实例的公网相关信息列表。顺序为主网卡在前，辅助网卡按绑定先后顺序排列。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIPAddressSet: list of PublicIPAddressInfo
        :param _InstanceNetworkInfoSet: 实例网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceNetworkInfoSet: list of InstanceNetworkInfo
        """
        self._PrivateIPAddressSet = None
        self._PublicIPAddressSet = None
        self._InstanceNetworkInfoSet = None

    @property
    def PrivateIPAddressSet(self):
        """实例的内网相关信息列表。顺序为主网卡在前，辅助网卡按绑定先后顺序排列。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PrivateIPAddressInfo
        """
        return self._PrivateIPAddressSet

    @PrivateIPAddressSet.setter
    def PrivateIPAddressSet(self, PrivateIPAddressSet):
        self._PrivateIPAddressSet = PrivateIPAddressSet

    @property
    def PublicIPAddressSet(self):
        """实例的公网相关信息列表。顺序为主网卡在前，辅助网卡按绑定先后顺序排列。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PublicIPAddressInfo
        """
        return self._PublicIPAddressSet

    @PublicIPAddressSet.setter
    def PublicIPAddressSet(self, PublicIPAddressSet):
        self._PublicIPAddressSet = PublicIPAddressSet

    @property
    def InstanceNetworkInfoSet(self):
        """实例网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InstanceNetworkInfo
        """
        return self._InstanceNetworkInfoSet

    @InstanceNetworkInfoSet.setter
    def InstanceNetworkInfoSet(self, InstanceNetworkInfoSet):
        self._InstanceNetworkInfoSet = InstanceNetworkInfoSet


    def _deserialize(self, params):
        if params.get("PrivateIPAddressSet") is not None:
            self._PrivateIPAddressSet = []
            for item in params.get("PrivateIPAddressSet"):
                obj = PrivateIPAddressInfo()
                obj._deserialize(item)
                self._PrivateIPAddressSet.append(obj)
        if params.get("PublicIPAddressSet") is not None:
            self._PublicIPAddressSet = []
            for item in params.get("PublicIPAddressSet"):
                obj = PublicIPAddressInfo()
                obj._deserialize(item)
                self._PublicIPAddressSet.append(obj)
        if params.get("InstanceNetworkInfoSet") is not None:
            self._InstanceNetworkInfoSet = []
            for item in params.get("InstanceNetworkInfoSet"):
                obj = InstanceNetworkInfo()
                obj._deserialize(item)
                self._InstanceNetworkInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Address(AbstractModel):
    """IPv6地址信息。

    """

    def __init__(self):
        r"""
        :param _Address: IPv6地址，形如：3402:4e00:20:100:0:8cd9:2a67:71f3
        :type Address: str
        :param _Primary: 是否是主IP。
        :type Primary: bool
        :param _AddressId: EIP实例ID，形如：eip-hxlqja90。
        :type AddressId: str
        :param _Description: 描述信息。
        :type Description: str
        :param _IsWanIpBlocked: 公网IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param _State: IPv6地址状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的
        :type State: str
        """
        self._Address = None
        self._Primary = None
        self._AddressId = None
        self._Description = None
        self._IsWanIpBlocked = None
        self._State = None

    @property
    def Address(self):
        """IPv6地址，形如：3402:4e00:20:100:0:8cd9:2a67:71f3
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def Primary(self):
        """是否是主IP。
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def AddressId(self):
        """EIP实例ID，形如：eip-hxlqja90。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def Description(self):
        """描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsWanIpBlocked(self):
        """公网IP是否被封堵。
        :rtype: bool
        """
        return self._IsWanIpBlocked

    @IsWanIpBlocked.setter
    def IsWanIpBlocked(self, IsWanIpBlocked):
        self._IsWanIpBlocked = IsWanIpBlocked

    @property
    def State(self):
        """IPv6地址状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._Primary = params.get("Primary")
        self._AddressId = params.get("AddressId")
        self._Description = params.get("Description")
        self._IsWanIpBlocked = params.get("IsWanIpBlocked")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6SubnetCidrBlock(AbstractModel):
    """IPv6子网段对象。

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网实例`ID`。形如：`subnet-pxir56ns`。	
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Ipv6CidrBlock: `IPv6`子网段。形如：`3402:4e00:20:1001::/64`	
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6CidrBlock: str
        """
        self._SubnetId = None
        self._Ipv6CidrBlock = None

    @property
    def SubnetId(self):
        """子网实例`ID`。形如：`subnet-pxir56ns`。	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Ipv6CidrBlock(self):
        """`IPv6`子网段。形如：`3402:4e00:20:1001::/64`	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyPair(AbstractModel):
    """描述密钥对信息

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥对的ID，是密钥对的唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyId: str
        :param _KeyName: 密钥对名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyName: str
        :param _ProjectId: 密钥对所属的项目ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param _Description: 密钥对描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _PublicKey: 密钥对的纯文本公钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicKey: str
        :param _PrivateKey: 钥对的纯文本私钥。腾讯云不会保管私钥，请用户自行妥善保存。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param _AssociatedInstanceIds: 钥关联的实例ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociatedInstanceIds: list of str
        :param _CreatedTime: 创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self._KeyId = None
        self._KeyName = None
        self._ProjectId = None
        self._Description = None
        self._PublicKey = None
        self._PrivateKey = None
        self._AssociatedInstanceIds = None
        self._CreatedTime = None

    @property
    def KeyId(self):
        """密钥对的ID，是密钥对的唯一标识。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyName(self):
        """密钥对名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyName

    @KeyName.setter
    def KeyName(self, KeyName):
        self._KeyName = KeyName

    @property
    def ProjectId(self):
        """密钥对所属的项目ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """密钥对描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PublicKey(self):
        """密钥对的纯文本公钥。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        """钥对的纯文本私钥。腾讯云不会保管私钥，请用户自行妥善保存。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def AssociatedInstanceIds(self):
        """钥关联的实例ID列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._AssociatedInstanceIds

    @AssociatedInstanceIds.setter
    def AssociatedInstanceIds(self, AssociatedInstanceIds):
        self._AssociatedInstanceIds = AssociatedInstanceIds

    @property
    def CreatedTime(self):
        """创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeyName = params.get("KeyName")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._AssociatedInstanceIds = params.get("AssociatedInstanceIds")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """负载均衡监听器

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _Protocol: 监听器协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Port: 监听器端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _HealthCheck: 监听器的健康检查信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param _Scheduler: 请求的调度方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheduler: str
        :param _SessionExpireTime: 会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionExpireTime: int
        :param _ListenerName: 监听器的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _CreateTime: 监听器的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _SessionType: 监听器的会话类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionType: str
        :param _EndPort: 端口段结束端口
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPort: int
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._HealthCheck = None
        self._Scheduler = None
        self._SessionExpireTime = None
        self._ListenerName = None
        self._CreateTime = None
        self._SessionType = None
        self._EndPort = None

    @property
    def ListenerId(self):
        """负载均衡监听器 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        """监听器协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """监听器端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthCheck(self):
        """监听器的健康检查信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        """请求的调度方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler

    @property
    def SessionExpireTime(self):
        """会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def ListenerName(self):
        """监听器的名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def CreateTime(self):
        """监听器的创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SessionType(self):
        """监听器的会话类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionType

    @SessionType.setter
    def SessionType(self, SessionType):
        self._SessionType = SessionType

    @property
    def EndPort(self):
        """端口段结束端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        self._SessionExpireTime = params.get("SessionExpireTime")
        self._ListenerName = params.get("ListenerName")
        self._CreateTime = params.get("CreateTime")
        self._SessionType = params.get("SessionType")
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """监听器后端

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _Protocol: 监听器的协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Port: 监听器的端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Targets: 监听器上绑定的后端服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of Backend
        """
        self._ListenerId = None
        self._Protocol = None
        self._Port = None
        self._Targets = None

    @property
    def ListenerId(self):
        """监听器 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Protocol(self):
        """监听器的协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """监听器的端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Targets(self):
        """监听器上绑定的后端服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Backend
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """监听器健康状态

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _ListenerName: 监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _Protocol: 监听器的协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Port: 监听器的端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Rules: 监听器的转发规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of RuleHealth
        """
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._Port = None
        self._Rules = None

    @property
    def ListenerId(self):
        """监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        """监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        """监听器的协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """监听器的端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Rules(self):
        """监听器的转发规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RuleHealth
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """负载均衡实例信息

    """

    def __init__(self):
        r"""
        :param _Region: 区域。
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Position: 位置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`
        :param _LoadBalancerId: 负载均衡实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _LoadBalancerType: 负载均衡实例的网络类型：OPEN：公网属性
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _LoadBalancerVips: 负载均衡实例的 VIP 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerVips: list of str
        :param _Status: 负载均衡实例的状态，包括
 0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CreateTime: 负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _StatusTime: 负载均衡实例的上次状态转换时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusTime: str
        :param _VpcId: 私有网络的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Tags: 负载均衡实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _VipIsp: 负载均衡IP地址所属的ISP。
注意：此字段可能返回 null，表示取不到有效值。
        :type VipIsp: str
        :param _NetworkAttributes: 负载均衡实例的网络属性。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkAttributes: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param _SecureGroups: 安全组。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecureGroups: list of str
        :param _LoadBalancerPassToTarget: 后端机器是否放通来自ELB的流量。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerPassToTarget: bool
        :param _AddressIPv6: 负载均衡实例的IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPv6: str
        """
        self._Region = None
        self._Position = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerType = None
        self._LoadBalancerVips = None
        self._Status = None
        self._CreateTime = None
        self._StatusTime = None
        self._VpcId = None
        self._Tags = None
        self._VipIsp = None
        self._NetworkAttributes = None
        self._SecureGroups = None
        self._LoadBalancerPassToTarget = None
        self._AddressIPv6 = None

    @property
    def Region(self):
        """区域。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Position(self):
        """位置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Position`
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """负载均衡实例的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerType(self):
        """负载均衡实例的网络类型：OPEN：公网属性
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def LoadBalancerVips(self):
        """负载均衡实例的 VIP 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LoadBalancerVips

    @LoadBalancerVips.setter
    def LoadBalancerVips(self, LoadBalancerVips):
        self._LoadBalancerVips = LoadBalancerVips

    @property
    def Status(self):
        """负载均衡实例的状态，包括
 0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StatusTime(self):
        """负载均衡实例的上次状态转换时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusTime

    @StatusTime.setter
    def StatusTime(self, StatusTime):
        self._StatusTime = StatusTime

    @property
    def VpcId(self):
        """私有网络的 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Tags(self):
        """负载均衡实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VipIsp(self):
        """负载均衡IP地址所属的ISP。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VipIsp

    @VipIsp.setter
    def VipIsp(self, VipIsp):
        self._VipIsp = VipIsp

    @property
    def NetworkAttributes(self):
        """负载均衡实例的网络属性。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        """
        return self._NetworkAttributes

    @NetworkAttributes.setter
    def NetworkAttributes(self, NetworkAttributes):
        self._NetworkAttributes = NetworkAttributes

    @property
    def SecureGroups(self):
        """安全组。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SecureGroups

    @SecureGroups.setter
    def SecureGroups(self, SecureGroups):
        self._SecureGroups = SecureGroups

    @property
    def LoadBalancerPassToTarget(self):
        """后端机器是否放通来自ELB的流量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget

    @property
    def AddressIPv6(self):
        """负载均衡实例的IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddressIPv6

    @AddressIPv6.setter
    def AddressIPv6(self, AddressIPv6):
        self._AddressIPv6 = AddressIPv6


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("Position") is not None:
            self._Position = Position()
            self._Position._deserialize(params.get("Position"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._LoadBalancerVips = params.get("LoadBalancerVips")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._StatusTime = params.get("StatusTime")
        self._VpcId = params.get("VpcId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VipIsp = params.get("VipIsp")
        if params.get("NetworkAttributes") is not None:
            self._NetworkAttributes = LoadBalancerInternetAccessible()
            self._NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        self._SecureGroups = params.get("SecureGroups")
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        self._AddressIPv6 = params.get("AddressIPv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """负载均衡器健康状态

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _Listeners: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ListenerHealth
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """负载均衡实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        """监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ListenerHealth
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self._Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerInternetAccessible(AbstractModel):
    """负载均衡的带宽限制等信息。

    """

    def __init__(self):
        r"""
        :param _InternetMaxBandwidthOut: 最大出带宽，单位Mbps。默认值10
        :type InternetMaxBandwidthOut: int
        """
        self._InternetMaxBandwidthOut = None

    @property
    def InternetMaxBandwidthOut(self):
        """最大出带宽，单位Mbps。默认值10
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _SourceInstanceId: 弹性网卡当前绑定的ECM实例ID。形如：ein-r8hr2upy。
        :type SourceInstanceId: str
        :param _DestinationInstanceId: 待迁移的目的ECM实例ID。
        :type DestinationInstanceId: str
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._SourceInstanceId = None
        self._DestinationInstanceId = None

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def SourceInstanceId(self):
        """弹性网卡当前绑定的ECM实例ID。形如：ein-r8hr2upy。
        :rtype: str
        """
        return self._SourceInstanceId

    @SourceInstanceId.setter
    def SourceInstanceId(self, SourceInstanceId):
        self._SourceInstanceId = SourceInstanceId

    @property
    def DestinationInstanceId(self):
        """待迁移的目的ECM实例ID。
        :rtype: str
        """
        return self._DestinationInstanceId

    @DestinationInstanceId.setter
    def DestinationInstanceId(self, DestinationInstanceId):
        self._DestinationInstanceId = DestinationInstanceId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._SourceInstanceId = params.get("SourceInstanceId")
        self._DestinationInstanceId = params.get("DestinationInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface返回参数结构体

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


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        :param _SourceNetworkInterfaceId: 当前内网IP绑定的弹性网卡实例ID，例如：eni-11112222。
        :type SourceNetworkInterfaceId: str
        :param _DestinationNetworkInterfaceId: 待迁移的目的弹性网卡实例ID。
        :type DestinationNetworkInterfaceId: str
        :param _PrivateIpAddress: 迁移的内网IP地址，例如：10.0.0.6。
        :type PrivateIpAddress: str
        """
        self._EcmRegion = None
        self._SourceNetworkInterfaceId = None
        self._DestinationNetworkInterfaceId = None
        self._PrivateIpAddress = None

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def SourceNetworkInterfaceId(self):
        """当前内网IP绑定的弹性网卡实例ID，例如：eni-11112222。
        :rtype: str
        """
        return self._SourceNetworkInterfaceId

    @SourceNetworkInterfaceId.setter
    def SourceNetworkInterfaceId(self, SourceNetworkInterfaceId):
        self._SourceNetworkInterfaceId = SourceNetworkInterfaceId

    @property
    def DestinationNetworkInterfaceId(self):
        """待迁移的目的弹性网卡实例ID。
        :rtype: str
        """
        return self._DestinationNetworkInterfaceId

    @DestinationNetworkInterfaceId.setter
    def DestinationNetworkInterfaceId(self, DestinationNetworkInterfaceId):
        self._DestinationNetworkInterfaceId = DestinationNetworkInterfaceId

    @property
    def PrivateIpAddress(self):
        """迁移的内网IP地址，例如：10.0.0.6。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self._DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress返回参数结构体

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


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :type AddressId: str
        :param _AddressName: 修改后的 EIP 名称。长度上限为20个字符。
        :type AddressName: str
        :param _EipDirectConnection: 设定EIP是否直通，"TRUE"表示直通，"FALSE"表示非直通。注意该参数仅对EIP直通功能可见的用户可以设定。
        :type EipDirectConnection: str
        """
        self._EcmRegion = None
        self._AddressId = None
        self._AddressName = None
        self._EipDirectConnection = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressId(self):
        """标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressName(self):
        """修改后的 EIP 名称。长度上限为20个字符。
        :rtype: str
        """
        return self._AddressName

    @AddressName.setter
    def AddressName(self, AddressName):
        self._AddressName = AddressName

    @property
    def EipDirectConnection(self):
        """设定EIP是否直通，"TRUE"表示直通，"FALSE"表示非直通。注意该参数仅对EIP直通功能可见的用户可以设定。
        :rtype: str
        """
        return self._EipDirectConnection

    @EipDirectConnection.setter
    def EipDirectConnection(self, EipDirectConnection):
        self._EipDirectConnection = EipDirectConnection


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressId = params.get("AddressId")
        self._AddressName = params.get("AddressName")
        self._EipDirectConnection = params.get("EipDirectConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute返回参数结构体

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


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressIds: EIP唯一标识ID，形如'eip-xxxxxxx'
        :type AddressIds: list of str
        :param _InternetMaxBandwidthOut: 调整带宽目标值
        :type InternetMaxBandwidthOut: int
        """
        self._EcmRegion = None
        self._AddressIds = None
        self._InternetMaxBandwidthOut = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressIds(self):
        """EIP唯一标识ID，形如'eip-xxxxxxx'
        :rtype: list of str
        """
        return self._AddressIds

    @AddressIds.setter
    def AddressIds(self, AddressIds):
        self._AddressIds = AddressIds

    @property
    def InternetMaxBandwidthOut(self):
        """调整带宽目标值
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressIds = params.get("AddressIds")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务TaskId。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步任务TaskId。
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


class ModifyDefaultSubnetRequest(AbstractModel):
    """ModifyDefaultSubnet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM地域
        :type EcmRegion: str
        :param _Zone: ECM可用区
        :type Zone: str
        :param _VpcId: 私有网络ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._EcmRegion = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def EcmRegion(self):
        """ECM地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Zone(self):
        """ECM可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        """私有网络ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultSubnetResponse(AbstractModel):
    """ModifyDefaultSubnet返回参数结构体

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


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HaVipId: HAVIP唯一ID，形如：havip-9o233uri。
        :type HaVipId: str
        :param _HaVipName: HAVIP名称，可任意命名，但不得超过60个字符。
        :type HaVipName: str
        """
        self._HaVipId = None
        self._HaVipName = None

    @property
    def HaVipId(self):
        """HAVIP唯一ID，形如：havip-9o233uri。
        :rtype: str
        """
        return self._HaVipId

    @HaVipId.setter
    def HaVipId(self, HaVipId):
        self._HaVipId = HaVipId

    @property
    def HaVipName(self):
        """HAVIP名称，可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._HaVipName

    @HaVipName.setter
    def HaVipName(self, HaVipName):
        self._HaVipName = HaVipName


    def _deserialize(self, params):
        self._HaVipId = params.get("HaVipId")
        self._HaVipName = params.get("HaVipName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute返回参数结构体

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


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像ID，形如img-gvbnzy6f
        :type ImageId: str
        :param _ImageName: 设置新的镜像名称；必须满足下列限制：
不得超过20个字符。
- 镜像名称不能与已有镜像重复。
        :type ImageName: str
        :param _ImageDescription: 设置新的镜像描述；必须满足下列限制：
- 不得超过60个字符。
        :type ImageDescription: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageDescription = None

    @property
    def ImageId(self):
        """镜像ID，形如img-gvbnzy6f
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        """设置新的镜像名称；必须满足下列限制：
不得超过20个字符。
- 镜像名称不能与已有镜像重复。
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageDescription(self):
        """设置新的镜像描述；必须满足下列限制：
- 不得超过60个字符。
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute返回参数结构体

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


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待修改的实例ID列表。在单次请求的过程中，请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param _InstanceName: 修改成功后显示的实例名称，不得超过60个字符，不传则名称显示为空。
        :type InstanceName: str
        :param _SecurityGroups: 指定实例的安全组Id列表，子机将重新关联指定列表的安全组，原本关联的安全组会被解绑。限制不超过5个。
        :type SecurityGroups: list of str
        """
        self._InstanceIdSet = None
        self._InstanceName = None
        self._SecurityGroups = None

    @property
    def InstanceIdSet(self):
        """待修改的实例ID列表。在单次请求的过程中，请求实例数上限为100。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def InstanceName(self):
        """修改成功后显示的实例名称，不得超过60个字符，不传则名称显示为空。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SecurityGroups(self):
        """指定实例的安全组Id列表，子机将重新关联指定列表的安全组，原本关联的安全组会被解绑。限制不超过5个。
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._InstanceName = params.get("InstanceName")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回参数结构体

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


class ModifyIpv6AddressesAttributeRequest(AbstractModel):
    """ModifyIpv6AddressesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _NetworkInterfaceId: 弹性网卡实例ID，形如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _Ipv6Addresses: 指定的IPv6地址信息。
        :type Ipv6Addresses: list of Ipv6Address
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._Ipv6Addresses = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，形如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def Ipv6Addresses(self):
        """指定的IPv6地址信息。
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIpv6AddressesAttributeResponse(AbstractModel):
    """ModifyIpv6AddressesAttribute返回参数结构体

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


class ModifyIpv6AddressesBandwidthRequest(AbstractModel):
    """ModifyIpv6AddressesBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _InternetMaxBandwidthOut: 修改的目标带宽，单位Mbps
        :type InternetMaxBandwidthOut: int
        :param _Ipv6Addresses: IPV6地址。Ipv6Addresses和Ipv6AddressId必须且只能传一个
        :type Ipv6Addresses: list of Ipv6Address
        :param _Ipv6AddressIds: IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ipv6Addresses和Ipv6AddressId必须且只能传一个
        :type Ipv6AddressIds: list of str
        """
        self._EcmRegion = None
        self._InternetMaxBandwidthOut = None
        self._Ipv6Addresses = None
        self._Ipv6AddressIds = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def InternetMaxBandwidthOut(self):
        """修改的目标带宽，单位Mbps
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Ipv6Addresses(self):
        """IPV6地址。Ipv6Addresses和Ipv6AddressId必须且只能传一个
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses

    @property
    def Ipv6AddressIds(self):
        """IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ipv6Addresses和Ipv6AddressId必须且只能传一个
        :rtype: list of str
        """
        return self._Ipv6AddressIds

    @Ipv6AddressIds.setter
    def Ipv6AddressIds(self, Ipv6AddressIds):
        self._Ipv6AddressIds = Ipv6AddressIds


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        self._Ipv6AddressIds = params.get("Ipv6AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIpv6AddressesBandwidthResponse(AbstractModel):
    """ModifyIpv6AddressesBandwidth返回参数结构体

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


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param _ListenerName: 新的监听器名称
        :type ListenerName: str
        :param _SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :type SessionExpireTime: int
        :param _HealthCheck: 健康检查相关参数
        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        :param _Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :type Scheduler: str
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._ListenerName = None
        self._SessionExpireTime = None
        self._HealthCheck = None
        self._Scheduler = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """负载均衡监听器 ID
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
    def SessionExpireTime(self):
        """会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。
        :rtype: int
        """
        return self._SessionExpireTime

    @SessionExpireTime.setter
    def SessionExpireTime(self, SessionExpireTime):
        self._SessionExpireTime = SessionExpireTime

    @property
    def HealthCheck(self):
        """健康检查相关参数
        :rtype: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`
        """
        return self._HealthCheck

    @HealthCheck.setter
    def HealthCheck(self, HealthCheck):
        self._HealthCheck = HealthCheck

    @property
    def Scheduler(self):
        """监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。
        :rtype: str
        """
        return self._Scheduler

    @Scheduler.setter
    def Scheduler(self, Scheduler):
        self._Scheduler = Scheduler


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self._HealthCheck = HealthCheck()
            self._HealthCheck._deserialize(params.get("HealthCheck"))
        self._Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener返回参数结构体

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


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡的唯一ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例名称
        :type LoadBalancerName: str
        :param _InternetChargeInfo: 网络计费及带宽相关参数
        :type InternetChargeInfo: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        :param _LoadBalancerPassToTarget: Target是否放通来自ELB的流量。开启放通（true）：只验证ELB上的安全组；不开启放通（false）：需同时验证ELB和后端实例上的安全组。
        :type LoadBalancerPassToTarget: bool
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._InternetChargeInfo = None
        self._LoadBalancerPassToTarget = None

    @property
    def LoadBalancerId(self):
        """负载均衡的唯一ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        """负载均衡实例名称
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def InternetChargeInfo(self):
        """网络计费及带宽相关参数
        :rtype: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`
        """
        return self._InternetChargeInfo

    @InternetChargeInfo.setter
    def InternetChargeInfo(self, InternetChargeInfo):
        self._InternetChargeInfo = InternetChargeInfo

    @property
    def LoadBalancerPassToTarget(self):
        """Target是否放通来自ELB的流量。开启放通（true）：只验证ELB上的安全组；不开启放通（false）：需同时验证ELB和后端实例上的安全组。
        :rtype: bool
        """
        return self._LoadBalancerPassToTarget

    @LoadBalancerPassToTarget.setter
    def LoadBalancerPassToTarget(self, LoadBalancerPassToTarget):
        self._LoadBalancerPassToTarget = LoadBalancerPassToTarget


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("InternetChargeInfo") is not None:
            self._InternetChargeInfo = LoadBalancerInternetAccessible()
            self._InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self._LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回参数结构体

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


class ModifyModuleConfigRequest(AbstractModel):
    """ModifyModuleConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID。
        :type ModuleId: str
        :param _InstanceType: 机型ID。
        :type InstanceType: str
        :param _DefaultDataDiskSize: 默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。
        :type DefaultDataDiskSize: int
        :param _DefaultSystemDiskSize: 默认系统盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。
        :type DefaultSystemDiskSize: int
        :param _SystemDisk: 系统盘
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: 数据盘
        :type DataDisks: list of DataDisk
        """
        self._ModuleId = None
        self._InstanceType = None
        self._DefaultDataDiskSize = None
        self._DefaultSystemDiskSize = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ModuleId(self):
        """模块ID。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def InstanceType(self):
        """机型ID。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DefaultDataDiskSize(self):
        """默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。
        :rtype: int
        """
        return self._DefaultDataDiskSize

    @DefaultDataDiskSize.setter
    def DefaultDataDiskSize(self, DefaultDataDiskSize):
        self._DefaultDataDiskSize = DefaultDataDiskSize

    @property
    def DefaultSystemDiskSize(self):
        """默认系统盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。
        :rtype: int
        """
        return self._DefaultSystemDiskSize

    @DefaultSystemDiskSize.setter
    def DefaultSystemDiskSize(self, DefaultSystemDiskSize):
        self._DefaultSystemDiskSize = DefaultSystemDiskSize

    @property
    def SystemDisk(self):
        """系统盘
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """数据盘
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._InstanceType = params.get("InstanceType")
        self._DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self._DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleConfigResponse(AbstractModel):
    """ModifyModuleConfig返回参数结构体

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


class ModifyModuleDisableWanIpRequest(AbstractModel):
    """ModifyModuleDisableWanIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID
        :type ModuleId: str
        :param _DisableWanIp: 是否禁止分配外网ip,true：统一分配外网ip，false：禁止分配外网ip.
        :type DisableWanIp: bool
        """
        self._ModuleId = None
        self._DisableWanIp = None

    @property
    def ModuleId(self):
        """模块ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def DisableWanIp(self):
        """是否禁止分配外网ip,true：统一分配外网ip，false：禁止分配外网ip.
        :rtype: bool
        """
        return self._DisableWanIp

    @DisableWanIp.setter
    def DisableWanIp(self, DisableWanIp):
        self._DisableWanIp = DisableWanIp


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._DisableWanIp = params.get("DisableWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleDisableWanIpResponse(AbstractModel):
    """ModifyModuleDisableWanIp返回参数结构体

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


class ModifyModuleImageRequest(AbstractModel):
    """ModifyModuleImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DefaultImageId: 默认镜像ID
        :type DefaultImageId: str
        :param _ModuleId: 模块ID
        :type ModuleId: str
        """
        self._DefaultImageId = None
        self._ModuleId = None

    @property
    def DefaultImageId(self):
        """默认镜像ID
        :rtype: str
        """
        return self._DefaultImageId

    @DefaultImageId.setter
    def DefaultImageId(self, DefaultImageId):
        self._DefaultImageId = DefaultImageId

    @property
    def ModuleId(self):
        """模块ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._DefaultImageId = params.get("DefaultImageId")
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleImageResponse(AbstractModel):
    """ModifyModuleImage返回参数结构体

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


class ModifyModuleIpDirectRequest(AbstractModel):
    """ModifyModuleIpDirect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID。
        :type ModuleId: str
        :param _CloseIpDirect: 是否关闭IP直通。取值范围：
true：表示关闭IP直通
false：表示开通IP直通
        :type CloseIpDirect: bool
        """
        self._ModuleId = None
        self._CloseIpDirect = None

    @property
    def ModuleId(self):
        """模块ID。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def CloseIpDirect(self):
        """是否关闭IP直通。取值范围：
true：表示关闭IP直通
false：表示开通IP直通
        :rtype: bool
        """
        return self._CloseIpDirect

    @CloseIpDirect.setter
    def CloseIpDirect(self, CloseIpDirect):
        self._CloseIpDirect = CloseIpDirect


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._CloseIpDirect = params.get("CloseIpDirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleIpDirectResponse(AbstractModel):
    """ModifyModuleIpDirect返回参数结构体

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


class ModifyModuleNameRequest(AbstractModel):
    """ModifyModuleName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID。
        :type ModuleId: str
        :param _ModuleName: 模块名称。
        :type ModuleName: str
        """
        self._ModuleId = None
        self._ModuleName = None

    @property
    def ModuleId(self):
        """模块ID。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ModuleName(self):
        """模块名称。
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNameResponse(AbstractModel):
    """ModifyModuleName返回参数结构体

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


class ModifyModuleNetworkRequest(AbstractModel):
    """ModifyModuleNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块Id
        :type ModuleId: str
        :param _DefaultBandwidth: 默认出带宽上限
        :type DefaultBandwidth: int
        :param _DefaultBandwidthIn: 默认入带宽上限
        :type DefaultBandwidthIn: int
        """
        self._ModuleId = None
        self._DefaultBandwidth = None
        self._DefaultBandwidthIn = None

    @property
    def ModuleId(self):
        """模块Id
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def DefaultBandwidth(self):
        """默认出带宽上限
        :rtype: int
        """
        return self._DefaultBandwidth

    @DefaultBandwidth.setter
    def DefaultBandwidth(self, DefaultBandwidth):
        self._DefaultBandwidth = DefaultBandwidth

    @property
    def DefaultBandwidthIn(self):
        """默认入带宽上限
        :rtype: int
        """
        return self._DefaultBandwidthIn

    @DefaultBandwidthIn.setter
    def DefaultBandwidthIn(self, DefaultBandwidthIn):
        self._DefaultBandwidthIn = DefaultBandwidthIn


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._DefaultBandwidth = params.get("DefaultBandwidth")
        self._DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNetworkResponse(AbstractModel):
    """ModifyModuleNetwork返回参数结构体

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


class ModifyModuleSecurityGroupsRequest(AbstractModel):
    """ModifyModuleSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupIdSet: 安全组列表。不超过5个。
        :type SecurityGroupIdSet: list of str
        :param _ModuleId: 模块id。
        :type ModuleId: str
        """
        self._SecurityGroupIdSet = None
        self._ModuleId = None

    @property
    def SecurityGroupIdSet(self):
        """安全组列表。不超过5个。
        :rtype: list of str
        """
        return self._SecurityGroupIdSet

    @SecurityGroupIdSet.setter
    def SecurityGroupIdSet(self, SecurityGroupIdSet):
        self._SecurityGroupIdSet = SecurityGroupIdSet

    @property
    def ModuleId(self):
        """模块id。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId


    def _deserialize(self, params):
        self._SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self._ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleSecurityGroupsResponse(AbstractModel):
    """ModifyModuleSecurityGroups返回参数结构体

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


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _PrivateIpAddresses: 指定的内网IP信息。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param _EcmRegion: ECM 节点Region信息，形如ap-xian-ecm。
        :type EcmRegion: str
        """
        self._NetworkInterfaceId = None
        self._PrivateIpAddresses = None
        self._EcmRegion = None

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddresses(self):
        """指定的内网IP信息。
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def EcmRegion(self):
        """ECM 节点Region信息，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute返回参数结构体

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


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c
        :type RouteTableId: str
        :param _RouteTableName: 路由表名称
        :type RouteTableName: str
        """
        self._RouteTableId = None
        self._RouteTableName = None

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-azd4dt1c
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        """路由表名称
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute返回参数结构体

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


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param _GroupName: 安全组名称，可任意命名，但不得超过60个字符。
        :type GroupName: str
        :param _GroupDescription: 安全组备注，最多100个字符。
        :type GroupDescription: str
        """
        self._SecurityGroupId = None
        self._GroupName = None
        self._GroupDescription = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def GroupName(self):
        """安全组名称，可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupDescription(self):
        """安全组备注，最多100个字符。
        :rtype: str
        """
        return self._GroupDescription

    @GroupDescription.setter
    def GroupDescription(self, GroupDescription):
        self._GroupDescription = GroupDescription


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._GroupName = params.get("GroupName")
        self._GroupDescription = params.get("GroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute返回参数结构体

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


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: 安全组规则集合。 SecurityGroupPolicySet对象必须同时指定新的出（Egress）入（Ingress）站规则。 SecurityGroupPolicy对象不支持自定义索引（PolicyIndex）。
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        :param _SortPolicys: 排序安全组标识。值为True时，支持安全组排序；SortPolicys不存在或SortPolicys为False时，为修改安全组规则。
        :type SortPolicys: bool
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None
        self._SortPolicys = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """安全组规则集合。 SecurityGroupPolicySet对象必须同时指定新的出（Egress）入（Ingress）站规则。 SecurityGroupPolicy对象不支持自定义索引（PolicyIndex）。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet

    @property
    def SortPolicys(self):
        """排序安全组标识。值为True时，支持安全组排序；SortPolicys不存在或SortPolicys为False时，为修改安全组规则。
        :rtype: bool
        """
        return self._SortPolicys

    @SortPolicys.setter
    def SortPolicys(self, SortPolicys):
        self._SortPolicys = SortPolicys


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self._SortPolicys = params.get("SortPolicys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies返回参数结构体

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


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网实例ID。形如：subnet-pxir56ns。
        :type SubnetId: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _SubnetName: 子网名称，最大长度不能超过60个字节。
        :type SubnetName: str
        :param _EnableBroadcast: 子网是否开启广播。
        :type EnableBroadcast: str
        :param _Tags: 子网的标签键值
        :type Tags: list of Tag
        """
        self._SubnetId = None
        self._EcmRegion = None
        self._SubnetName = None
        self._EnableBroadcast = None
        self._Tags = None

    @property
    def SubnetId(self):
        """子网实例ID。形如：subnet-pxir56ns。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def SubnetName(self):
        """子网名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def EnableBroadcast(self):
        """子网是否开启广播。
        :rtype: str
        """
        return self._EnableBroadcast

    @EnableBroadcast.setter
    def EnableBroadcast(self, EnableBroadcast):
        self._EnableBroadcast = EnableBroadcast

    @property
    def Tags(self):
        """子网的标签键值
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._EcmRegion = params.get("EcmRegion")
        self._SubnetName = params.get("SubnetName")
        self._EnableBroadcast = params.get("EnableBroadcast")
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
        


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute返回参数结构体

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


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param _Targets: 要修改端口的后端服务列表
        :type Targets: list of Target
        :param _NewPort: 后端服务绑定到监听器或转发规则的新端口
        :type NewPort: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._NewPort = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """负载均衡监听器 ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        """要修改端口的后端服务列表
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def NewPort(self):
        """后端服务绑定到监听器或转发规则的新端口
        :rtype: int
        """
        return self._NewPort

    @NewPort.setter
    def NewPort(self, NewPort):
        self._NewPort = NewPort


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort返回参数结构体

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


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param _Targets: 要修改权重的后端服务列表
        :type Targets: list of Target
        :param _Weight: 后端服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。
        :type Weight: int
        """
        self._LoadBalancerId = None
        self._ListenerId = None
        self._Targets = None
        self._Weight = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ListenerId(self):
        """负载均衡监听器 ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        """要修改权重的后端服务列表
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def Weight(self):
        """后端服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight返回参数结构体

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


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。形如：vpc-f49l6u0z。
        :type VpcId: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _VpcName: 私有网络名称，可任意命名，但不得超过60个字符。
        :type VpcName: str
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _Description: 私有网络描述
        :type Description: str
        :param _DnsServers: DNS地址，最多支持4个，第1个默认为主，其余为备。	
        :type DnsServers: list of str
        :param _DomainName: 域名。
        :type DomainName: str
        """
        self._VpcId = None
        self._EcmRegion = None
        self._VpcName = None
        self._Tags = None
        self._Description = None
        self._DnsServers = None
        self._DomainName = None

    @property
    def VpcId(self):
        """VPC实例ID。形如：vpc-f49l6u0z。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def VpcName(self):
        """私有网络名称，可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Description(self):
        """私有网络描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DnsServers(self):
        """DNS地址，最多支持4个，第1个默认为主，其余为备。	
        :rtype: list of str
        """
        return self._DnsServers

    @DnsServers.setter
    def DnsServers(self, DnsServers):
        self._DnsServers = DnsServers

    @property
    def DomainName(self):
        """域名。
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._EcmRegion = params.get("EcmRegion")
        self._VpcName = params.get("VpcName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Description = params.get("Description")
        self._DnsServers = params.get("DnsServers")
        self._DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute返回参数结构体

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


class Module(AbstractModel):
    """模块信息

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块Id。
        :type ModuleId: str
        :param _ModuleName: 模块名称。
        :type ModuleName: str
        :param _ModuleState: 模块状态：
NORMAL：正常。
DELETING：删除中 
DELETEFAILED：删除失败。
        :type ModuleState: str
        :param _DefaultSystemDiskSize: 默认系统盘大小。
        :type DefaultSystemDiskSize: int
        :param _DefaultDataDiskSize: 默认数据盘大小。
        :type DefaultDataDiskSize: int
        :param _InstanceTypeConfig: 默认机型。
        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        :param _DefaultImage: 默认镜像。
        :type DefaultImage: :class:`tencentcloud.ecm.v20190719.models.Image`
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _DefaultBandwidth: 默认出带宽。
        :type DefaultBandwidth: int
        :param _TagSet: 标签集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param _CloseIpDirect: 是否关闭IP直通。
        :type CloseIpDirect: int
        :param _SecurityGroupIds: 默认安全组id列表。
        :type SecurityGroupIds: list of str
        :param _DefaultBandwidthIn: 默认入带宽。
        :type DefaultBandwidthIn: int
        :param _UserData: 自定义脚本数据
        :type UserData: str
        :param _SystemDisk: 系统盘信息。
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: 数据盘信息。
        :type DataDisks: list of DataDisk
        :param _DisableWanIp: 是否禁止外网ip
        :type DisableWanIp: int
        """
        self._ModuleId = None
        self._ModuleName = None
        self._ModuleState = None
        self._DefaultSystemDiskSize = None
        self._DefaultDataDiskSize = None
        self._InstanceTypeConfig = None
        self._DefaultImage = None
        self._CreateTime = None
        self._DefaultBandwidth = None
        self._TagSet = None
        self._CloseIpDirect = None
        self._SecurityGroupIds = None
        self._DefaultBandwidthIn = None
        self._UserData = None
        self._SystemDisk = None
        self._DataDisks = None
        self._DisableWanIp = None

    @property
    def ModuleId(self):
        """模块Id。
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ModuleName(self):
        """模块名称。
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName

    @property
    def ModuleState(self):
        """模块状态：
NORMAL：正常。
DELETING：删除中 
DELETEFAILED：删除失败。
        :rtype: str
        """
        return self._ModuleState

    @ModuleState.setter
    def ModuleState(self, ModuleState):
        self._ModuleState = ModuleState

    @property
    def DefaultSystemDiskSize(self):
        """默认系统盘大小。
        :rtype: int
        """
        return self._DefaultSystemDiskSize

    @DefaultSystemDiskSize.setter
    def DefaultSystemDiskSize(self, DefaultSystemDiskSize):
        self._DefaultSystemDiskSize = DefaultSystemDiskSize

    @property
    def DefaultDataDiskSize(self):
        """默认数据盘大小。
        :rtype: int
        """
        return self._DefaultDataDiskSize

    @DefaultDataDiskSize.setter
    def DefaultDataDiskSize(self, DefaultDataDiskSize):
        self._DefaultDataDiskSize = DefaultDataDiskSize

    @property
    def InstanceTypeConfig(self):
        """默认机型。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`
        """
        return self._InstanceTypeConfig

    @InstanceTypeConfig.setter
    def InstanceTypeConfig(self, InstanceTypeConfig):
        self._InstanceTypeConfig = InstanceTypeConfig

    @property
    def DefaultImage(self):
        """默认镜像。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Image`
        """
        return self._DefaultImage

    @DefaultImage.setter
    def DefaultImage(self, DefaultImage):
        self._DefaultImage = DefaultImage

    @property
    def CreateTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DefaultBandwidth(self):
        """默认出带宽。
        :rtype: int
        """
        return self._DefaultBandwidth

    @DefaultBandwidth.setter
    def DefaultBandwidth(self, DefaultBandwidth):
        self._DefaultBandwidth = DefaultBandwidth

    @property
    def TagSet(self):
        """标签集合。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def CloseIpDirect(self):
        """是否关闭IP直通。
        :rtype: int
        """
        return self._CloseIpDirect

    @CloseIpDirect.setter
    def CloseIpDirect(self, CloseIpDirect):
        self._CloseIpDirect = CloseIpDirect

    @property
    def SecurityGroupIds(self):
        """默认安全组id列表。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def DefaultBandwidthIn(self):
        """默认入带宽。
        :rtype: int
        """
        return self._DefaultBandwidthIn

    @DefaultBandwidthIn.setter
    def DefaultBandwidthIn(self, DefaultBandwidthIn):
        self._DefaultBandwidthIn = DefaultBandwidthIn

    @property
    def UserData(self):
        """自定义脚本数据
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def SystemDisk(self):
        """系统盘信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """数据盘信息。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def DisableWanIp(self):
        """是否禁止外网ip
        :rtype: int
        """
        return self._DisableWanIp

    @DisableWanIp.setter
    def DisableWanIp(self, DisableWanIp):
        self._DisableWanIp = DisableWanIp


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._ModuleName = params.get("ModuleName")
        self._ModuleState = params.get("ModuleState")
        self._DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self._DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        if params.get("InstanceTypeConfig") is not None:
            self._InstanceTypeConfig = InstanceTypeConfig()
            self._InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        if params.get("DefaultImage") is not None:
            self._DefaultImage = Image()
            self._DefaultImage._deserialize(params.get("DefaultImage"))
        self._CreateTime = params.get("CreateTime")
        self._DefaultBandwidth = params.get("DefaultBandwidth")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._CloseIpDirect = params.get("CloseIpDirect")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        self._UserData = params.get("UserData")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._DisableWanIp = params.get("DisableWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleCounter(AbstractModel):
    """节点统计数据

    """

    def __init__(self):
        r"""
        :param _ISPCounterSet: 运营商统计信息列表
        :type ISPCounterSet: list of ISPCounter
        :param _ProvinceNum: 省份数量
        :type ProvinceNum: int
        :param _CityNum: 城市数量
        :type CityNum: int
        :param _NodeNum: 节点数量
        :type NodeNum: int
        :param _InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self._ISPCounterSet = None
        self._ProvinceNum = None
        self._CityNum = None
        self._NodeNum = None
        self._InstanceNum = None

    @property
    def ISPCounterSet(self):
        """运营商统计信息列表
        :rtype: list of ISPCounter
        """
        return self._ISPCounterSet

    @ISPCounterSet.setter
    def ISPCounterSet(self, ISPCounterSet):
        self._ISPCounterSet = ISPCounterSet

    @property
    def ProvinceNum(self):
        """省份数量
        :rtype: int
        """
        return self._ProvinceNum

    @ProvinceNum.setter
    def ProvinceNum(self, ProvinceNum):
        self._ProvinceNum = ProvinceNum

    @property
    def CityNum(self):
        """城市数量
        :rtype: int
        """
        return self._CityNum

    @CityNum.setter
    def CityNum(self, CityNum):
        self._CityNum = CityNum

    @property
    def NodeNum(self):
        """节点数量
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def InstanceNum(self):
        """实例数量
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        if params.get("ISPCounterSet") is not None:
            self._ISPCounterSet = []
            for item in params.get("ISPCounterSet"):
                obj = ISPCounter()
                obj._deserialize(item)
                self._ISPCounterSet.append(obj)
        self._ProvinceNum = params.get("ProvinceNum")
        self._CityNum = params.get("CityNum")
        self._NodeNum = params.get("NodeNum")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleItem(AbstractModel):
    """模块列表Item信息

    """

    def __init__(self):
        r"""
        :param _NodeInstanceNum: 节点实例统计信息
        :type NodeInstanceNum: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        :param _Module: 模块信息
        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        self._NodeInstanceNum = None
        self._Module = None

    @property
    def NodeInstanceNum(self):
        """节点实例统计信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`
        """
        return self._NodeInstanceNum

    @NodeInstanceNum.setter
    def NodeInstanceNum(self, NodeInstanceNum):
        self._NodeInstanceNum = NodeInstanceNum

    @property
    def Module(self):
        """模块信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Module`
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        if params.get("NodeInstanceNum") is not None:
            self._NodeInstanceNum = NodeInstanceNum()
            self._NodeInstanceNum._deserialize(params.get("NodeInstanceNum"))
        if params.get("Module") is not None:
            self._Module = Module()
            self._Module._deserialize(params.get("Module"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonthNetwork(AbstractModel):
    """客户对应月份的带宽信息

    """

    def __init__(self):
        r"""
        :param _ZoneInfo: 节点zone信息
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param _Month: 带宽月份 示例"202103"
        :type Month: str
        :param _BandwidthPkgId: 带宽包id 格式如"bwp-xxxxxxxx"
        :type BandwidthPkgId: str
        :param _Isp: 运营商简称 取值范围"CUCC;CTCC;CMCC"
        :type Isp: str
        :param _TrafficMaxIn: 入网带宽包峰值,取值范围0.0-xxx.xxx
        :type TrafficMaxIn: float
        :param _TrafficMaxOut: 出网带宽包峰值,取值范围0.0-xxx.xxx
        :type TrafficMaxOut: float
        :param _FeeTraffic: 计费带宽,取值范围0.0-xxx.xxx
        :type FeeTraffic: float
        :param _StartTime: 月计费带宽起始时间 格式"yyyy-mm-dd HH:mm:ss"
        :type StartTime: str
        :param _EndTime: 月计费带宽结束时间 格式"yyyy-mm-dd HH:mm:ss"
        :type EndTime: str
        :param _EffectiveDays: 月计费带宽实际有效天数 整形必须大于等于0
        :type EffectiveDays: int
        :param _MonthDays: 指定月份的实际天数 实例 30
        :type MonthDays: int
        :param _EffectiveDaysRate: 有效天占比 保留小数点后四位0.2134
        :type EffectiveDaysRate: float
        :param _BandwidthPkgType: 计费带宽包类型 实例"Address","LoadBalance","AddressIpv6"
        :type BandwidthPkgType: str
        """
        self._ZoneInfo = None
        self._Month = None
        self._BandwidthPkgId = None
        self._Isp = None
        self._TrafficMaxIn = None
        self._TrafficMaxOut = None
        self._FeeTraffic = None
        self._StartTime = None
        self._EndTime = None
        self._EffectiveDays = None
        self._MonthDays = None
        self._EffectiveDaysRate = None
        self._BandwidthPkgType = None

    @property
    def ZoneInfo(self):
        """节点zone信息
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        """
        return self._ZoneInfo

    @ZoneInfo.setter
    def ZoneInfo(self, ZoneInfo):
        self._ZoneInfo = ZoneInfo

    @property
    def Month(self):
        """带宽月份 示例"202103"
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def BandwidthPkgId(self):
        """带宽包id 格式如"bwp-xxxxxxxx"
        :rtype: str
        """
        return self._BandwidthPkgId

    @BandwidthPkgId.setter
    def BandwidthPkgId(self, BandwidthPkgId):
        self._BandwidthPkgId = BandwidthPkgId

    @property
    def Isp(self):
        """运营商简称 取值范围"CUCC;CTCC;CMCC"
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def TrafficMaxIn(self):
        """入网带宽包峰值,取值范围0.0-xxx.xxx
        :rtype: float
        """
        return self._TrafficMaxIn

    @TrafficMaxIn.setter
    def TrafficMaxIn(self, TrafficMaxIn):
        self._TrafficMaxIn = TrafficMaxIn

    @property
    def TrafficMaxOut(self):
        """出网带宽包峰值,取值范围0.0-xxx.xxx
        :rtype: float
        """
        return self._TrafficMaxOut

    @TrafficMaxOut.setter
    def TrafficMaxOut(self, TrafficMaxOut):
        self._TrafficMaxOut = TrafficMaxOut

    @property
    def FeeTraffic(self):
        """计费带宽,取值范围0.0-xxx.xxx
        :rtype: float
        """
        return self._FeeTraffic

    @FeeTraffic.setter
    def FeeTraffic(self, FeeTraffic):
        self._FeeTraffic = FeeTraffic

    @property
    def StartTime(self):
        """月计费带宽起始时间 格式"yyyy-mm-dd HH:mm:ss"
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """月计费带宽结束时间 格式"yyyy-mm-dd HH:mm:ss"
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def EffectiveDays(self):
        """月计费带宽实际有效天数 整形必须大于等于0
        :rtype: int
        """
        return self._EffectiveDays

    @EffectiveDays.setter
    def EffectiveDays(self, EffectiveDays):
        self._EffectiveDays = EffectiveDays

    @property
    def MonthDays(self):
        """指定月份的实际天数 实例 30
        :rtype: int
        """
        return self._MonthDays

    @MonthDays.setter
    def MonthDays(self, MonthDays):
        self._MonthDays = MonthDays

    @property
    def EffectiveDaysRate(self):
        """有效天占比 保留小数点后四位0.2134
        :rtype: float
        """
        return self._EffectiveDaysRate

    @EffectiveDaysRate.setter
    def EffectiveDaysRate(self, EffectiveDaysRate):
        self._EffectiveDaysRate = EffectiveDaysRate

    @property
    def BandwidthPkgType(self):
        """计费带宽包类型 实例"Address","LoadBalance","AddressIpv6"
        :rtype: str
        """
        return self._BandwidthPkgType

    @BandwidthPkgType.setter
    def BandwidthPkgType(self, BandwidthPkgType):
        self._BandwidthPkgType = BandwidthPkgType


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self._ZoneInfo = ZoneInfo()
            self._ZoneInfo._deserialize(params.get("ZoneInfo"))
        self._Month = params.get("Month")
        self._BandwidthPkgId = params.get("BandwidthPkgId")
        self._Isp = params.get("Isp")
        self._TrafficMaxIn = params.get("TrafficMaxIn")
        self._TrafficMaxOut = params.get("TrafficMaxOut")
        self._FeeTraffic = params.get("FeeTraffic")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._EffectiveDays = params.get("EffectiveDays")
        self._MonthDays = params.get("MonthDays")
        self._EffectiveDaysRate = params.get("EffectiveDaysRate")
        self._BandwidthPkgType = params.get("BandwidthPkgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterface(AbstractModel):
    """弹性网卡

    """

    def __init__(self):
        r"""
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-f1xjkw1b。
        :type NetworkInterfaceId: str
        :param _NetworkInterfaceName: 弹性网卡名称。
        :type NetworkInterfaceName: str
        :param _NetworkInterfaceDescription: 弹性网卡描述。
        :type NetworkInterfaceDescription: str
        :param _SubnetId: 子网实例ID。
        :type SubnetId: str
        :param _VpcId: VPC实例ID。
        :type VpcId: str
        :param _GroupSet: 绑定的安全组。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupSet: list of str
        :param _Primary: 是否是主网卡。
        :type Primary: bool
        :param _MacAddress: MAC地址。
        :type MacAddress: str
        :param _State: 弹性网卡状态：
PENDING：创建中
AVAILABLE：可用的
ATTACHING：绑定中
DETACHING：解绑中
DELETING：删除中
        :type State: str
        :param _PrivateIpAddressSet: 内网IP信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param _Attachment: 绑定的云服务器对象。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Attachment: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`
        :param _Zone: 可用区。
        :type Zone: str
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _Ipv6AddressSet: IPv6地址列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6AddressSet: list of Ipv6Address
        :param _TagSet: 标签键值对。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param _EniType: 网卡类型。0 - 弹性网卡；1 - evm弹性网卡。
        :type EniType: int
        :param _EcmRegion: EcmRegion ecm区域
        :type EcmRegion: str
        :param _Business: 网卡绑定的子机类型：cvm，eks。
注意：此字段可能返回 null，表示取不到有效值。
        :type Business: str
        """
        self._NetworkInterfaceId = None
        self._NetworkInterfaceName = None
        self._NetworkInterfaceDescription = None
        self._SubnetId = None
        self._VpcId = None
        self._GroupSet = None
        self._Primary = None
        self._MacAddress = None
        self._State = None
        self._PrivateIpAddressSet = None
        self._Attachment = None
        self._Zone = None
        self._CreatedTime = None
        self._Ipv6AddressSet = None
        self._TagSet = None
        self._EniType = None
        self._EcmRegion = None
        self._Business = None

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-f1xjkw1b。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def NetworkInterfaceName(self):
        """弹性网卡名称。
        :rtype: str
        """
        return self._NetworkInterfaceName

    @NetworkInterfaceName.setter
    def NetworkInterfaceName(self, NetworkInterfaceName):
        self._NetworkInterfaceName = NetworkInterfaceName

    @property
    def NetworkInterfaceDescription(self):
        """弹性网卡描述。
        :rtype: str
        """
        return self._NetworkInterfaceDescription

    @NetworkInterfaceDescription.setter
    def NetworkInterfaceDescription(self, NetworkInterfaceDescription):
        self._NetworkInterfaceDescription = NetworkInterfaceDescription

    @property
    def SubnetId(self):
        """子网实例ID。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        """VPC实例ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def GroupSet(self):
        """绑定的安全组。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._GroupSet

    @GroupSet.setter
    def GroupSet(self, GroupSet):
        self._GroupSet = GroupSet

    @property
    def Primary(self):
        """是否是主网卡。
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def MacAddress(self):
        """MAC地址。
        :rtype: str
        """
        return self._MacAddress

    @MacAddress.setter
    def MacAddress(self, MacAddress):
        self._MacAddress = MacAddress

    @property
    def State(self):
        """弹性网卡状态：
PENDING：创建中
AVAILABLE：可用的
ATTACHING：绑定中
DETACHING：解绑中
DELETING：删除中
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def PrivateIpAddressSet(self):
        """内网IP信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddressSet

    @PrivateIpAddressSet.setter
    def PrivateIpAddressSet(self, PrivateIpAddressSet):
        self._PrivateIpAddressSet = PrivateIpAddressSet

    @property
    def Attachment(self):
        """绑定的云服务器对象。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`
        """
        return self._Attachment

    @Attachment.setter
    def Attachment(self, Attachment):
        self._Attachment = Attachment

    @property
    def Zone(self):
        """可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CreatedTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Ipv6AddressSet(self):
        """IPv6地址列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Ipv6Address
        """
        return self._Ipv6AddressSet

    @Ipv6AddressSet.setter
    def Ipv6AddressSet(self, Ipv6AddressSet):
        self._Ipv6AddressSet = Ipv6AddressSet

    @property
    def TagSet(self):
        """标签键值对。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def EniType(self):
        """网卡类型。0 - 弹性网卡；1 - evm弹性网卡。
        :rtype: int
        """
        return self._EniType

    @EniType.setter
    def EniType(self, EniType):
        self._EniType = EniType

    @property
    def EcmRegion(self):
        """EcmRegion ecm区域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Business(self):
        """网卡绑定的子机类型：cvm，eks。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business


    def _deserialize(self, params):
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        self._NetworkInterfaceName = params.get("NetworkInterfaceName")
        self._NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._GroupSet = params.get("GroupSet")
        self._Primary = params.get("Primary")
        self._MacAddress = params.get("MacAddress")
        self._State = params.get("State")
        if params.get("PrivateIpAddressSet") is not None:
            self._PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddressSet.append(obj)
        if params.get("Attachment") is not None:
            self._Attachment = NetworkInterfaceAttachment()
            self._Attachment._deserialize(params.get("Attachment"))
        self._Zone = params.get("Zone")
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Ipv6AddressSet") is not None:
            self._Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6AddressSet.append(obj)
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._EniType = params.get("EniType")
        self._EcmRegion = params.get("EcmRegion")
        self._Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterfaceAttachment(AbstractModel):
    """弹性网卡绑定关系

    """

    def __init__(self):
        r"""
        :param _InstanceId: 云主机实例ID。
        :type InstanceId: str
        :param _DeviceIndex: 网卡在云主机实例内的序号。
        :type DeviceIndex: int
        :param _InstanceAccountId: 云主机所有者账户信息。
        :type InstanceAccountId: str
        :param _AttachTime: 绑定时间。
        :type AttachTime: str
        """
        self._InstanceId = None
        self._DeviceIndex = None
        self._InstanceAccountId = None
        self._AttachTime = None

    @property
    def InstanceId(self):
        """云主机实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceIndex(self):
        """网卡在云主机实例内的序号。
        :rtype: int
        """
        return self._DeviceIndex

    @DeviceIndex.setter
    def DeviceIndex(self, DeviceIndex):
        self._DeviceIndex = DeviceIndex

    @property
    def InstanceAccountId(self):
        """云主机所有者账户信息。
        :rtype: str
        """
        return self._InstanceAccountId

    @InstanceAccountId.setter
    def InstanceAccountId(self, InstanceAccountId):
        self._InstanceAccountId = InstanceAccountId

    @property
    def AttachTime(self):
        """绑定时间。
        :rtype: str
        """
        return self._AttachTime

    @AttachTime.setter
    def AttachTime(self, AttachTime):
        self._AttachTime = AttachTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceIndex = params.get("DeviceIndex")
        self._InstanceAccountId = params.get("InstanceAccountId")
        self._AttachTime = params.get("AttachTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkStorageRange(AbstractModel):
    """网络硬盘上下限数据

    """

    def __init__(self):
        r"""
        :param _MaxBandwidth: 网络带宽上限
        :type MaxBandwidth: int
        :param _MaxSystemDiskSize: 数据盘上限
        :type MaxSystemDiskSize: int
        :param _MinBandwidth: 网络带宽下限
        :type MinBandwidth: int
        :param _MinSystemDiskSize: 数据盘下限
        :type MinSystemDiskSize: int
        :param _MaxDataDiskSize: 最大数据盘大小
        :type MaxDataDiskSize: int
        :param _MinDataDiskSize: 最小数据盘大小
        :type MinDataDiskSize: int
        :param _SuggestBandwidth: 建议带宽
        :type SuggestBandwidth: int
        :param _SuggestDataDiskSize: 建议硬盘大小
        :type SuggestDataDiskSize: int
        :param _SuggestSystemDiskSize: 建议系统盘大小
        :type SuggestSystemDiskSize: int
        :param _MaxVcpu: Cpu核数峰值
        :type MaxVcpu: int
        :param _MinVcpu: Cpu核最小值
        :type MinVcpu: int
        :param _MaxVcpuPerReq: 单次请求最大cpu核数
        :type MaxVcpuPerReq: int
        :param _PerBandwidth: 带宽步长
        :type PerBandwidth: int
        :param _PerDataDisk: 数据盘步长
        :type PerDataDisk: int
        :param _MaxModuleNum: 总模块数量
        :type MaxModuleNum: int
        :param _CBSSupported: 是否支持cbs
        :type CBSSupported: bool
        :param _DiskNumLimit: 磁盘数量限制
        :type DiskNumLimit: int
        """
        self._MaxBandwidth = None
        self._MaxSystemDiskSize = None
        self._MinBandwidth = None
        self._MinSystemDiskSize = None
        self._MaxDataDiskSize = None
        self._MinDataDiskSize = None
        self._SuggestBandwidth = None
        self._SuggestDataDiskSize = None
        self._SuggestSystemDiskSize = None
        self._MaxVcpu = None
        self._MinVcpu = None
        self._MaxVcpuPerReq = None
        self._PerBandwidth = None
        self._PerDataDisk = None
        self._MaxModuleNum = None
        self._CBSSupported = None
        self._DiskNumLimit = None

    @property
    def MaxBandwidth(self):
        """网络带宽上限
        :rtype: int
        """
        return self._MaxBandwidth

    @MaxBandwidth.setter
    def MaxBandwidth(self, MaxBandwidth):
        self._MaxBandwidth = MaxBandwidth

    @property
    def MaxSystemDiskSize(self):
        """数据盘上限
        :rtype: int
        """
        return self._MaxSystemDiskSize

    @MaxSystemDiskSize.setter
    def MaxSystemDiskSize(self, MaxSystemDiskSize):
        self._MaxSystemDiskSize = MaxSystemDiskSize

    @property
    def MinBandwidth(self):
        """网络带宽下限
        :rtype: int
        """
        return self._MinBandwidth

    @MinBandwidth.setter
    def MinBandwidth(self, MinBandwidth):
        self._MinBandwidth = MinBandwidth

    @property
    def MinSystemDiskSize(self):
        """数据盘下限
        :rtype: int
        """
        return self._MinSystemDiskSize

    @MinSystemDiskSize.setter
    def MinSystemDiskSize(self, MinSystemDiskSize):
        self._MinSystemDiskSize = MinSystemDiskSize

    @property
    def MaxDataDiskSize(self):
        """最大数据盘大小
        :rtype: int
        """
        return self._MaxDataDiskSize

    @MaxDataDiskSize.setter
    def MaxDataDiskSize(self, MaxDataDiskSize):
        self._MaxDataDiskSize = MaxDataDiskSize

    @property
    def MinDataDiskSize(self):
        """最小数据盘大小
        :rtype: int
        """
        return self._MinDataDiskSize

    @MinDataDiskSize.setter
    def MinDataDiskSize(self, MinDataDiskSize):
        self._MinDataDiskSize = MinDataDiskSize

    @property
    def SuggestBandwidth(self):
        """建议带宽
        :rtype: int
        """
        return self._SuggestBandwidth

    @SuggestBandwidth.setter
    def SuggestBandwidth(self, SuggestBandwidth):
        self._SuggestBandwidth = SuggestBandwidth

    @property
    def SuggestDataDiskSize(self):
        """建议硬盘大小
        :rtype: int
        """
        return self._SuggestDataDiskSize

    @SuggestDataDiskSize.setter
    def SuggestDataDiskSize(self, SuggestDataDiskSize):
        self._SuggestDataDiskSize = SuggestDataDiskSize

    @property
    def SuggestSystemDiskSize(self):
        """建议系统盘大小
        :rtype: int
        """
        return self._SuggestSystemDiskSize

    @SuggestSystemDiskSize.setter
    def SuggestSystemDiskSize(self, SuggestSystemDiskSize):
        self._SuggestSystemDiskSize = SuggestSystemDiskSize

    @property
    def MaxVcpu(self):
        """Cpu核数峰值
        :rtype: int
        """
        return self._MaxVcpu

    @MaxVcpu.setter
    def MaxVcpu(self, MaxVcpu):
        self._MaxVcpu = MaxVcpu

    @property
    def MinVcpu(self):
        """Cpu核最小值
        :rtype: int
        """
        return self._MinVcpu

    @MinVcpu.setter
    def MinVcpu(self, MinVcpu):
        self._MinVcpu = MinVcpu

    @property
    def MaxVcpuPerReq(self):
        """单次请求最大cpu核数
        :rtype: int
        """
        return self._MaxVcpuPerReq

    @MaxVcpuPerReq.setter
    def MaxVcpuPerReq(self, MaxVcpuPerReq):
        self._MaxVcpuPerReq = MaxVcpuPerReq

    @property
    def PerBandwidth(self):
        """带宽步长
        :rtype: int
        """
        return self._PerBandwidth

    @PerBandwidth.setter
    def PerBandwidth(self, PerBandwidth):
        self._PerBandwidth = PerBandwidth

    @property
    def PerDataDisk(self):
        """数据盘步长
        :rtype: int
        """
        return self._PerDataDisk

    @PerDataDisk.setter
    def PerDataDisk(self, PerDataDisk):
        self._PerDataDisk = PerDataDisk

    @property
    def MaxModuleNum(self):
        """总模块数量
        :rtype: int
        """
        return self._MaxModuleNum

    @MaxModuleNum.setter
    def MaxModuleNum(self, MaxModuleNum):
        self._MaxModuleNum = MaxModuleNum

    @property
    def CBSSupported(self):
        """是否支持cbs
        :rtype: bool
        """
        return self._CBSSupported

    @CBSSupported.setter
    def CBSSupported(self, CBSSupported):
        self._CBSSupported = CBSSupported

    @property
    def DiskNumLimit(self):
        """磁盘数量限制
        :rtype: int
        """
        return self._DiskNumLimit

    @DiskNumLimit.setter
    def DiskNumLimit(self, DiskNumLimit):
        self._DiskNumLimit = DiskNumLimit


    def _deserialize(self, params):
        self._MaxBandwidth = params.get("MaxBandwidth")
        self._MaxSystemDiskSize = params.get("MaxSystemDiskSize")
        self._MinBandwidth = params.get("MinBandwidth")
        self._MinSystemDiskSize = params.get("MinSystemDiskSize")
        self._MaxDataDiskSize = params.get("MaxDataDiskSize")
        self._MinDataDiskSize = params.get("MinDataDiskSize")
        self._SuggestBandwidth = params.get("SuggestBandwidth")
        self._SuggestDataDiskSize = params.get("SuggestDataDiskSize")
        self._SuggestSystemDiskSize = params.get("SuggestSystemDiskSize")
        self._MaxVcpu = params.get("MaxVcpu")
        self._MinVcpu = params.get("MinVcpu")
        self._MaxVcpuPerReq = params.get("MaxVcpuPerReq")
        self._PerBandwidth = params.get("PerBandwidth")
        self._PerDataDisk = params.get("PerDataDisk")
        self._MaxModuleNum = params.get("MaxModuleNum")
        self._CBSSupported = params.get("CBSSupported")
        self._DiskNumLimit = params.get("DiskNumLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Node(AbstractModel):
    """节点信息

    """

    def __init__(self):
        r"""
        :param _ZoneInfo: zone信息。
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param _Country: 国家信息。
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param _Area: 区域信息。
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param _Province: 省份信息。
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param _City: 城市信息。
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param _RegionInfo: Region信息。
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        :param _ISPSet: 运营商列表。
        :type ISPSet: list of ISP
        :param _ISPNum: 运营商数量。
        :type ISPNum: int
        :param _LBSupported: 节点是否支持LB
        :type LBSupported: bool
        """
        self._ZoneInfo = None
        self._Country = None
        self._Area = None
        self._Province = None
        self._City = None
        self._RegionInfo = None
        self._ISPSet = None
        self._ISPNum = None
        self._LBSupported = None

    @property
    def ZoneInfo(self):
        """zone信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        """
        return self._ZoneInfo

    @ZoneInfo.setter
    def ZoneInfo(self, ZoneInfo):
        self._ZoneInfo = ZoneInfo

    @property
    def Country(self):
        """国家信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Country`
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Area(self):
        """区域信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Area`
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Province(self):
        """省份信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Province`
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """城市信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.City`
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def RegionInfo(self):
        """Region信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        return self._RegionInfo

    @RegionInfo.setter
    def RegionInfo(self, RegionInfo):
        self._RegionInfo = RegionInfo

    @property
    def ISPSet(self):
        """运营商列表。
        :rtype: list of ISP
        """
        return self._ISPSet

    @ISPSet.setter
    def ISPSet(self, ISPSet):
        self._ISPSet = ISPSet

    @property
    def ISPNum(self):
        """运营商数量。
        :rtype: int
        """
        return self._ISPNum

    @ISPNum.setter
    def ISPNum(self, ISPNum):
        self._ISPNum = ISPNum

    @property
    def LBSupported(self):
        """节点是否支持LB
        :rtype: bool
        """
        return self._LBSupported

    @LBSupported.setter
    def LBSupported(self, LBSupported):
        self._LBSupported = LBSupported


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self._ZoneInfo = ZoneInfo()
            self._ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self._Country = Country()
            self._Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self._Area = Area()
            self._Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self._Province = Province()
            self._Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self._City = City()
            self._City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self._RegionInfo = RegionInfo()
            self._RegionInfo._deserialize(params.get("RegionInfo"))
        if params.get("ISPSet") is not None:
            self._ISPSet = []
            for item in params.get("ISPSet"):
                obj = ISP()
                obj._deserialize(item)
                self._ISPSet.append(obj)
        self._ISPNum = params.get("ISPNum")
        self._LBSupported = params.get("LBSupported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInstanceNum(AbstractModel):
    """节点实例数量信息

    """

    def __init__(self):
        r"""
        :param _NodeNum: 节点数量
        :type NodeNum: int
        :param _InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self._NodeNum = None
        self._InstanceNum = None

    @property
    def NodeNum(self):
        """节点数量
        :rtype: int
        """
        return self._NodeNum

    @NodeNum.setter
    def NodeNum(self, NodeNum):
        self._NodeNum = NodeNum

    @property
    def InstanceNum(self):
        """实例数量
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        self._NodeNum = params.get("NodeNum")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperatorAction(AbstractModel):
    """操作Action

    """

    def __init__(self):
        r"""
        :param _Action: 可执行操作
        :type Action: str
        :param _Code: 编码Code
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param _Message: 具体信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._Action = None
        self._Code = None
        self._Message = None

    @property
    def Action(self):
        """可执行操作
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Code(self):
        """编码Code
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """具体信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """操作系统支持的类型。

    """

    def __init__(self):
        r"""
        :param _OsName: 操作系统类型
        :type OsName: str
        :param _OsVersions: 支持的操作系统版本
注意：此字段可能返回 null，表示取不到有效值。
        :type OsVersions: list of str
        :param _Architecture: 支持的操作系统架构
注意：此字段可能返回 null，表示取不到有效值。
        :type Architecture: list of str
        """
        self._OsName = None
        self._OsVersions = None
        self._Architecture = None

    @property
    def OsName(self):
        """操作系统类型
        :rtype: str
        """
        return self._OsName

    @OsName.setter
    def OsName(self, OsName):
        self._OsName = OsName

    @property
    def OsVersions(self):
        """支持的操作系统版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._OsVersions

    @OsVersions.setter
    def OsVersions(self, OsVersions):
        self._OsVersions = OsVersions

    @property
    def Architecture(self):
        """支持的操作系统架构
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Architecture

    @Architecture.setter
    def Architecture(self, Architecture):
        self._Architecture = Architecture


    def _deserialize(self, params):
        self._OsName = params.get("OsName")
        self._OsVersions = params.get("OsVersions")
        self._Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackingQuotaGroup(AbstractModel):
    """一组相互关联的装箱配额，以实例类型的优先级排序，优先级高的在前

    """

    def __init__(self):
        r"""
        :param _Zone: 可用区
        :type Zone: str
        :param _ZoneId: 可用区id
        :type ZoneId: int
        :param _ISPId: ISP id
        :type ISPId: str
        :param _PackingQuotaInfos: 一组相互关联的装箱配额
        :type PackingQuotaInfos: list of PackingQuotaInfo
        """
        self._Zone = None
        self._ZoneId = None
        self._ISPId = None
        self._PackingQuotaInfos = None

    @property
    def Zone(self):
        """可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        """可用区id
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ISPId(self):
        """ISP id
        :rtype: str
        """
        return self._ISPId

    @ISPId.setter
    def ISPId(self, ISPId):
        self._ISPId = ISPId

    @property
    def PackingQuotaInfos(self):
        """一组相互关联的装箱配额
        :rtype: list of PackingQuotaInfo
        """
        return self._PackingQuotaInfos

    @PackingQuotaInfos.setter
    def PackingQuotaInfos(self, PackingQuotaInfos):
        self._PackingQuotaInfos = PackingQuotaInfos


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._ISPId = params.get("ISPId")
        if params.get("PackingQuotaInfos") is not None:
            self._PackingQuotaInfos = []
            for item in params.get("PackingQuotaInfos"):
                obj = PackingQuotaInfo()
                obj._deserialize(item)
                self._PackingQuotaInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackingQuotaInfo(AbstractModel):
    """一组相关联的装箱配额信息

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型
        :type InstanceType: str
        :param _PackingQuota: 装箱配额
        :type PackingQuota: int
        """
        self._InstanceType = None
        self._PackingQuota = None

    @property
    def InstanceType(self):
        """实例类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def PackingQuota(self):
        """装箱配额
        :rtype: int
        """
        return self._PackingQuota

    @PackingQuota.setter
    def PackingQuota(self, PackingQuota):
        self._PackingQuota = PackingQuota


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._PackingQuota = params.get("PackingQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakBase(AbstractModel):
    """峰值信息

    """

    def __init__(self):
        r"""
        :param _PeakCpuNum: CPU峰值
        :type PeakCpuNum: int
        :param _PeakMemoryNum: 内存峰值
        :type PeakMemoryNum: int
        :param _PeakStorageNum: 硬盘峰值
        :type PeakStorageNum: int
        :param _RecordTime: 记录时间
        :type RecordTime: str
        """
        self._PeakCpuNum = None
        self._PeakMemoryNum = None
        self._PeakStorageNum = None
        self._RecordTime = None

    @property
    def PeakCpuNum(self):
        """CPU峰值
        :rtype: int
        """
        return self._PeakCpuNum

    @PeakCpuNum.setter
    def PeakCpuNum(self, PeakCpuNum):
        self._PeakCpuNum = PeakCpuNum

    @property
    def PeakMemoryNum(self):
        """内存峰值
        :rtype: int
        """
        return self._PeakMemoryNum

    @PeakMemoryNum.setter
    def PeakMemoryNum(self, PeakMemoryNum):
        self._PeakMemoryNum = PeakMemoryNum

    @property
    def PeakStorageNum(self):
        """硬盘峰值
        :rtype: int
        """
        return self._PeakStorageNum

    @PeakStorageNum.setter
    def PeakStorageNum(self, PeakStorageNum):
        self._PeakStorageNum = PeakStorageNum

    @property
    def RecordTime(self):
        """记录时间
        :rtype: str
        """
        return self._RecordTime

    @RecordTime.setter
    def RecordTime(self, RecordTime):
        self._RecordTime = RecordTime


    def _deserialize(self, params):
        self._PeakCpuNum = params.get("PeakCpuNum")
        self._PeakMemoryNum = params.get("PeakMemoryNum")
        self._PeakStorageNum = params.get("PeakStorageNum")
        self._RecordTime = params.get("RecordTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakFamilyInfo(AbstractModel):
    """PeakFamilyInfo 按机型类别分类的cpu等数据的峰值信息

    """

    def __init__(self):
        r"""
        :param _InstanceFamily: 机型类别信息。
        :type InstanceFamily: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        :param _PeakBaseSet: 基础数据峰值信息。
        :type PeakBaseSet: list of PeakBase
        """
        self._InstanceFamily = None
        self._PeakBaseSet = None

    @property
    def InstanceFamily(self):
        """机型类别信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`
        """
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def PeakBaseSet(self):
        """基础数据峰值信息。
        :rtype: list of PeakBase
        """
        return self._PeakBaseSet

    @PeakBaseSet.setter
    def PeakBaseSet(self, PeakBaseSet):
        self._PeakBaseSet = PeakBaseSet


    def _deserialize(self, params):
        if params.get("InstanceFamily") is not None:
            self._InstanceFamily = InstanceFamilyTypeConfig()
            self._InstanceFamily._deserialize(params.get("InstanceFamily"))
        if params.get("PeakBaseSet") is not None:
            self._PeakBaseSet = []
            for item in params.get("PeakBaseSet"):
                obj = PeakBase()
                obj._deserialize(item)
                self._PeakBaseSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetwork(AbstractModel):
    """峰值网络数据

    """

    def __init__(self):
        r"""
        :param _RecordTime: 记录时间。
        :type RecordTime: str
        :param _PeakInNetwork: 入带宽数据。
        :type PeakInNetwork: str
        :param _PeakOutNetwork: 出带宽数据。
        :type PeakOutNetwork: str
        :param _ChargeNetwork: 计费带宽。单位bps
        :type ChargeNetwork: str
        """
        self._RecordTime = None
        self._PeakInNetwork = None
        self._PeakOutNetwork = None
        self._ChargeNetwork = None

    @property
    def RecordTime(self):
        """记录时间。
        :rtype: str
        """
        return self._RecordTime

    @RecordTime.setter
    def RecordTime(self, RecordTime):
        self._RecordTime = RecordTime

    @property
    def PeakInNetwork(self):
        """入带宽数据。
        :rtype: str
        """
        return self._PeakInNetwork

    @PeakInNetwork.setter
    def PeakInNetwork(self, PeakInNetwork):
        self._PeakInNetwork = PeakInNetwork

    @property
    def PeakOutNetwork(self):
        """出带宽数据。
        :rtype: str
        """
        return self._PeakOutNetwork

    @PeakOutNetwork.setter
    def PeakOutNetwork(self, PeakOutNetwork):
        self._PeakOutNetwork = PeakOutNetwork

    @property
    def ChargeNetwork(self):
        """计费带宽。单位bps
        :rtype: str
        """
        return self._ChargeNetwork

    @ChargeNetwork.setter
    def ChargeNetwork(self, ChargeNetwork):
        self._ChargeNetwork = ChargeNetwork


    def _deserialize(self, params):
        self._RecordTime = params.get("RecordTime")
        self._PeakInNetwork = params.get("PeakInNetwork")
        self._PeakOutNetwork = params.get("PeakOutNetwork")
        self._ChargeNetwork = params.get("ChargeNetwork")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetworkRegionInfo(AbstractModel):
    """region维度的网络峰值信息

    """

    def __init__(self):
        r"""
        :param _Region: region信息
        :type Region: str
        :param _PeakNetworkSet: 网络峰值集合
注意：此字段可能返回 null，表示取不到有效值。
        :type PeakNetworkSet: list of PeakNetwork
        """
        self._Region = None
        self._PeakNetworkSet = None

    @property
    def Region(self):
        """region信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PeakNetworkSet(self):
        """网络峰值集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PeakNetwork
        """
        return self._PeakNetworkSet

    @PeakNetworkSet.setter
    def PeakNetworkSet(self, PeakNetworkSet):
        self._PeakNetworkSet = PeakNetworkSet


    def _deserialize(self, params):
        self._Region = params.get("Region")
        if params.get("PeakNetworkSet") is not None:
            self._PeakNetworkSet = []
            for item in params.get("PeakNetworkSet"):
                obj = PeakNetwork()
                obj._deserialize(item)
                self._PeakNetworkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhysicalPosition(AbstractModel):
    """物理位置信息

    """

    def __init__(self):
        r"""
        :param _PosId: 机位
注意：此字段可能返回 null，表示取不到有效值。
        :type PosId: str
        :param _RackId: 机架
注意：此字段可能返回 null，表示取不到有效值。
        :type RackId: str
        :param _SwitchId: 交换机
注意：此字段可能返回 null，表示取不到有效值。
        :type SwitchId: str
        """
        self._PosId = None
        self._RackId = None
        self._SwitchId = None

    @property
    def PosId(self):
        """机位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PosId

    @PosId.setter
    def PosId(self, PosId):
        self._PosId = PosId

    @property
    def RackId(self):
        """机架
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RackId

    @RackId.setter
    def RackId(self, RackId):
        self._RackId = RackId

    @property
    def SwitchId(self):
        """交换机
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SwitchId

    @SwitchId.setter
    def SwitchId(self, SwitchId):
        self._SwitchId = SwitchId


    def _deserialize(self, params):
        self._PosId = params.get("PosId")
        self._RackId = params.get("RackId")
        self._SwitchId = params.get("SwitchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，以及所属的独享集群的ID和名字。

    """

    def __init__(self):
        r"""
        :param _Zone: 云硬盘所属的[可用区](/document/product/213/15753#ZoneInfo)。该参数也可以通过调用  [DescribeZones](/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param _CageId: 围笼Id。作为入参时，表示对指定的CageId的资源进行操作，可为空。 作为出参时，表示资源所属围笼ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CageId: str
        :param _ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param _CdcName: 独享集群名字。作为入参时，忽略。作为出参时，表示云硬盘所属的独享集群名，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcName: str
        :param _CdcId: 实例所属的独享集群ID。作为入参时，表示对指定的CdcId独享集群的资源进行操作，可为空。 作为出参时，表示资源所属的独享集群的ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type CdcId: str
        """
        self._Zone = None
        self._CageId = None
        self._ProjectId = None
        self._CdcName = None
        self._CdcId = None

    @property
    def Zone(self):
        """云硬盘所属的[可用区](/document/product/213/15753#ZoneInfo)。该参数也可以通过调用  [DescribeZones](/document/product/213/15707) 的返回值中的Zone字段来获取。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def CageId(self):
        """围笼Id。作为入参时，表示对指定的CageId的资源进行操作，可为空。 作为出参时，表示资源所属围笼ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CageId

    @CageId.setter
    def CageId(self, CageId):
        self._CageId = CageId

    @property
    def ProjectId(self):
        """实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CdcName(self):
        """独享集群名字。作为入参时，忽略。作为出参时，表示云硬盘所属的独享集群名，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CdcName

    @CdcName.setter
    def CdcName(self, CdcName):
        self._CdcName = CdcName

    @property
    def CdcId(self):
        """实例所属的独享集群ID。作为入参时，表示对指定的CdcId独享集群的资源进行操作，可为空。 作为出参时，表示资源所属的独享集群的ID，可为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CdcId

    @CdcId.setter
    def CdcId(self, CdcId):
        self._CdcId = CdcId


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._CageId = params.get("CageId")
        self._ProjectId = params.get("ProjectId")
        self._CdcName = params.get("CdcName")
        self._CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Position(AbstractModel):
    """描述实例的位置相关信息。

    """

    def __init__(self):
        r"""
        :param _ZoneInfo: 实例所在的Zone的信息。
        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        :param _Country: 实例所在的国家的信息。
        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`
        :param _Area: 实例所在的Area的信息。
        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`
        :param _Province: 实例所在的省份的信息。
        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`
        :param _City: 实例所在的城市的信息。
        :type City: :class:`tencentcloud.ecm.v20190719.models.City`
        :param _RegionInfo: 实例所在的Region的信息。
        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        :param _Ipv6Supported: 实例是否支持ipv6
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6Supported: bool
        """
        self._ZoneInfo = None
        self._Country = None
        self._Area = None
        self._Province = None
        self._City = None
        self._RegionInfo = None
        self._Ipv6Supported = None

    @property
    def ZoneInfo(self):
        """实例所在的Zone的信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`
        """
        return self._ZoneInfo

    @ZoneInfo.setter
    def ZoneInfo(self, ZoneInfo):
        self._ZoneInfo = ZoneInfo

    @property
    def Country(self):
        """实例所在的国家的信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Country`
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Area(self):
        """实例所在的Area的信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Area`
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Province(self):
        """实例所在的省份的信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Province`
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def City(self):
        """实例所在的城市的信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.City`
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def RegionInfo(self):
        """实例所在的Region的信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`
        """
        return self._RegionInfo

    @RegionInfo.setter
    def RegionInfo(self, RegionInfo):
        self._RegionInfo = RegionInfo

    @property
    def Ipv6Supported(self):
        """实例是否支持ipv6
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Ipv6Supported

    @Ipv6Supported.setter
    def Ipv6Supported(self, Ipv6Supported):
        self._Ipv6Supported = Ipv6Supported


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self._ZoneInfo = ZoneInfo()
            self._ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self._Country = Country()
            self._Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self._Area = Area()
            self._Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self._Province = Province()
            self._Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self._City = City()
            self._City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self._RegionInfo = RegionInfo()
            self._RegionInfo._deserialize(params.get("RegionInfo"))
        self._Ipv6Supported = params.get("Ipv6Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceDetail(AbstractModel):
    """描述cpu,内存等维度的价格

    """

    def __init__(self):
        r"""
        :param _Discount: 表示折扣，20 表示20%，打2折
        :type Discount: int
        :param _DiscountPrice: 打折后价格，单位分
        :type DiscountPrice: int
        :param _OriginalPrice: 折扣前价格，单位分
        :type OriginalPrice: int
        """
        self._Discount = None
        self._DiscountPrice = None
        self._OriginalPrice = None

    @property
    def Discount(self):
        """表示折扣，20 表示20%，打2折
        :rtype: int
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def DiscountPrice(self):
        """打折后价格，单位分
        :rtype: int
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice

    @property
    def OriginalPrice(self):
        """折扣前价格，单位分
        :rtype: int
        """
        return self._OriginalPrice

    @OriginalPrice.setter
    def OriginalPrice(self, OriginalPrice):
        self._OriginalPrice = OriginalPrice


    def _deserialize(self, params):
        self._Discount = params.get("Discount")
        self._DiscountPrice = params.get("DiscountPrice")
        self._OriginalPrice = params.get("OriginalPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIPAddressInfo(AbstractModel):
    """实例的内网ip相关信息。

    """

    def __init__(self):
        r"""
        :param _PrivateIPAddress: 实例的内网ip。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIPAddress: str
        """
        self._PrivateIPAddress = None

    @property
    def PrivateIPAddress(self):
        """实例的内网ip。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateIPAddress

    @PrivateIPAddress.setter
    def PrivateIPAddress(self, PrivateIPAddress):
        self._PrivateIPAddress = PrivateIPAddress


    def _deserialize(self, params):
        self._PrivateIPAddress = params.get("PrivateIPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIpAddressSpecification(AbstractModel):
    """内网IP信息

    """

    def __init__(self):
        r"""
        :param _PrivateIpAddress: 内网IP地址。
        :type PrivateIpAddress: str
        :param _Primary: 是否是主IP。
        :type Primary: bool
        :param _PublicIpAddress: 公网IP地址。
        :type PublicIpAddress: str
        :param _AddressId: EIP实例ID，例如：eip-11112222。
        :type AddressId: str
        :param _Description: 内网IP描述信息。
        :type Description: str
        :param _IsWanIpBlocked: 公网IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param _State: IP状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的
        :type State: str
        """
        self._PrivateIpAddress = None
        self._Primary = None
        self._PublicIpAddress = None
        self._AddressId = None
        self._Description = None
        self._IsWanIpBlocked = None
        self._State = None

    @property
    def PrivateIpAddress(self):
        """内网IP地址。
        :rtype: str
        """
        return self._PrivateIpAddress

    @PrivateIpAddress.setter
    def PrivateIpAddress(self, PrivateIpAddress):
        self._PrivateIpAddress = PrivateIpAddress

    @property
    def Primary(self):
        """是否是主IP。
        :rtype: bool
        """
        return self._Primary

    @Primary.setter
    def Primary(self, Primary):
        self._Primary = Primary

    @property
    def PublicIpAddress(self):
        """公网IP地址。
        :rtype: str
        """
        return self._PublicIpAddress

    @PublicIpAddress.setter
    def PublicIpAddress(self, PublicIpAddress):
        self._PublicIpAddress = PublicIpAddress

    @property
    def AddressId(self):
        """EIP实例ID，例如：eip-11112222。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def Description(self):
        """内网IP描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsWanIpBlocked(self):
        """公网IP是否被封堵。
        :rtype: bool
        """
        return self._IsWanIpBlocked

    @IsWanIpBlocked.setter
    def IsWanIpBlocked(self, IsWanIpBlocked):
        self._IsWanIpBlocked = IsWanIpBlocked

    @property
    def State(self):
        """IP状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State


    def _deserialize(self, params):
        self._PrivateIpAddress = params.get("PrivateIpAddress")
        self._Primary = params.get("Primary")
        self._PublicIpAddress = params.get("PublicIpAddress")
        self._AddressId = params.get("AddressId")
        self._Description = params.get("Description")
        self._IsWanIpBlocked = params.get("IsWanIpBlocked")
        self._State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Province(AbstractModel):
    """省份信息

    """

    def __init__(self):
        r"""
        :param _ProvinceId: 省份Id
        :type ProvinceId: str
        :param _ProvinceName: 省份名称
        :type ProvinceName: str
        """
        self._ProvinceId = None
        self._ProvinceName = None

    @property
    def ProvinceId(self):
        """省份Id
        :rtype: str
        """
        return self._ProvinceId

    @ProvinceId.setter
    def ProvinceId(self, ProvinceId):
        self._ProvinceId = ProvinceId

    @property
    def ProvinceName(self):
        """省份名称
        :rtype: str
        """
        return self._ProvinceName

    @ProvinceName.setter
    def ProvinceName(self, ProvinceName):
        self._ProvinceName = ProvinceName


    def _deserialize(self, params):
        self._ProvinceId = params.get("ProvinceId")
        self._ProvinceName = params.get("ProvinceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIPAddressInfo(AbstractModel):
    """实例的公网ip相关信息。

    """

    def __init__(self):
        r"""
        :param _ChargeMode: 计费模式。
        :type ChargeMode: str
        :param _PublicIPAddress: 实例的公网ip。
        :type PublicIPAddress: str
        :param _ISP: 实例的公网ip所属的运营商。
        :type ISP: :class:`tencentcloud.ecm.v20190719.models.ISP`
        :param _MaxBandwidthOut: 实例的最大出带宽上限，单位为Mbps。
        :type MaxBandwidthOut: int
        :param _MaxBandwidthIn: 实例的最大入带宽上限，单位为Mbps。
        :type MaxBandwidthIn: int
        """
        self._ChargeMode = None
        self._PublicIPAddress = None
        self._ISP = None
        self._MaxBandwidthOut = None
        self._MaxBandwidthIn = None

    @property
    def ChargeMode(self):
        """计费模式。
        :rtype: str
        """
        return self._ChargeMode

    @ChargeMode.setter
    def ChargeMode(self, ChargeMode):
        self._ChargeMode = ChargeMode

    @property
    def PublicIPAddress(self):
        """实例的公网ip。
        :rtype: str
        """
        return self._PublicIPAddress

    @PublicIPAddress.setter
    def PublicIPAddress(self, PublicIPAddress):
        self._PublicIPAddress = PublicIPAddress

    @property
    def ISP(self):
        """实例的公网ip所属的运营商。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ISP`
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def MaxBandwidthOut(self):
        """实例的最大出带宽上限，单位为Mbps。
        :rtype: int
        """
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def MaxBandwidthIn(self):
        """实例的最大入带宽上限，单位为Mbps。
        :rtype: int
        """
        return self._MaxBandwidthIn

    @MaxBandwidthIn.setter
    def MaxBandwidthIn(self, MaxBandwidthIn):
        self._MaxBandwidthIn = MaxBandwidthIn


    def _deserialize(self, params):
        self._ChargeMode = params.get("ChargeMode")
        self._PublicIPAddress = params.get("PublicIPAddress")
        if params.get("ISP") is not None:
            self._ISP = ISP()
            self._ISP._deserialize(params.get("ISP"))
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryVpcTaskResultRequest(AbstractModel):
    """QueryVpcTaskResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 无
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """无
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
        


class QueryVpcTaskResultResponse(AbstractModel):
    """QueryVpcTaskResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 执行结果，包括"SUCCESS", "FAILED", "RUNNING"
        :type Status: str
        :param _Output: 异步任务执行输出。
        :type Output: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Output = None
        self._RequestId = None

    @property
    def Status(self):
        """执行结果，包括"SUCCESS", "FAILED", "RUNNING"
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Output(self):
        """异步任务执行输出。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

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
        self._Output = params.get("Output")
        self._RequestId = params.get("RequestId")


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待重启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param _ForceReboot: 是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启；
FALSE：表示在正常重启失败后不进行强制重启；
默认取值：FALSE。
        :type ForceReboot: bool
        :param _StopType: 关机类型。取值范围：
SOFT：表示软关机
HARD：表示硬关机
SOFT_FIRST：表示优先软关机，失败再执行硬关机

默认取值：SOFT。
        :type StopType: str
        """
        self._InstanceIdSet = None
        self._ForceReboot = None
        self._StopType = None

    @property
    def InstanceIdSet(self):
        """待重启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ForceReboot(self):
        """是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启；
FALSE：表示在正常重启失败后不进行强制重启；
默认取值：FALSE。
        :rtype: bool
        """
        return self._ForceReboot

    @ForceReboot.setter
    def ForceReboot(self, ForceReboot):
        self._ForceReboot = ForceReboot

    @property
    def StopType(self):
        """关机类型。取值范围：
SOFT：表示软关机
HARD：表示硬关机
SOFT_FIRST：表示优先软关机，失败再执行硬关机

默认取值：SOFT。
        :rtype: str
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ForceReboot = params.get("ForceReboot")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回参数结构体

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


class RegionInfo(AbstractModel):
    """Region和RegionName

    """

    def __init__(self):
        r"""
        :param _Region: Region
        :type Region: str
        :param _RegionName: Region名称
        :type RegionName: str
        :param _RegionId: RegionID
        :type RegionId: int
        """
        self._Region = None
        self._RegionName = None
        self._RegionId = None

    @property
    def Region(self):
        """Region
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """Region名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionId(self):
        """RegionID
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _AddressIds: 标识 EIP 的唯一 ID 列表。
        :type AddressIds: list of str
        """
        self._EcmRegion = None
        self._AddressIds = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def AddressIds(self):
        """标识 EIP 的唯一 ID 列表。
        :rtype: list of str
        """
        return self._AddressIds

    @AddressIds.setter
    def AddressIds(self, AddressIds):
        self._AddressIds = AddressIds


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._AddressIds = params.get("AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。
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


class ReleaseIpv6AddressesBandwidthRequest(AbstractModel):
    """ReleaseIpv6AddressesBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域。
        :type EcmRegion: str
        :param _Ipv6Addresses: IPV6地址。Ipv6Addresses和Ipv6AddressIds必须且只能传一个。
        :type Ipv6Addresses: list of str
        :param _Ipv6AddressIds: IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ipv6Addresses和Ipv6AddressIds必须且只能传一个。
        :type Ipv6AddressIds: list of str
        """
        self._EcmRegion = None
        self._Ipv6Addresses = None
        self._Ipv6AddressIds = None

    @property
    def EcmRegion(self):
        """ECM 地域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def Ipv6Addresses(self):
        """IPV6地址。Ipv6Addresses和Ipv6AddressIds必须且只能传一个。
        :rtype: list of str
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses

    @property
    def Ipv6AddressIds(self):
        """IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ipv6Addresses和Ipv6AddressIds必须且只能传一个。
        :rtype: list of str
        """
        return self._Ipv6AddressIds

    @Ipv6AddressIds.setter
    def Ipv6AddressIds(self, Ipv6AddressIds):
        self._Ipv6AddressIds = Ipv6AddressIds


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._Ipv6Addresses = params.get("Ipv6Addresses")
        self._Ipv6AddressIds = params.get("Ipv6AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIpv6AddressesBandwidthResponse(AbstractModel):
    """ReleaseIpv6AddressesBandwidth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 异步任务TaskId。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """异步任务TaskId。
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


class ReleaseIpv6AddressesRequest(AbstractModel):
    """ReleaseIpv6Addresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        :param _NetworkInterfaceId: 弹性网卡实例ID，形如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param _Ipv6Addresses: 指定的IPv6地址列表，单次最多指定10个。
        :type Ipv6Addresses: list of Ipv6Address
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._Ipv6Addresses = None

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，形如：eni-m6dyj72l。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def Ipv6Addresses(self):
        """指定的IPv6地址列表，单次最多指定10个。
        :rtype: list of Ipv6Address
        """
        return self._Ipv6Addresses

    @Ipv6Addresses.setter
    def Ipv6Addresses(self, Ipv6Addresses):
        self._Ipv6Addresses = Ipv6Addresses


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self._Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self._Ipv6Addresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIpv6AddressesResponse(AbstractModel):
    """ReleaseIpv6Addresses返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID，可以通过DescribeTaskResult查询任务状态
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID，可以通过DescribeTaskResult查询任务状态
        :rtype: int
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


class RemovePrivateIpAddressesRequest(AbstractModel):
    """RemovePrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EcmRegion: ECM 地域，形如ap-xian-ecm。
        :type EcmRegion: str
        :param _NetworkInterfaceId: 弹性网卡实例ID，例如：eni-11112222。
        :type NetworkInterfaceId: str
        :param _PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self._EcmRegion = None
        self._NetworkInterfaceId = None
        self._PrivateIpAddresses = None

    @property
    def EcmRegion(self):
        """ECM 地域，形如ap-xian-ecm。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion

    @property
    def NetworkInterfaceId(self):
        """弹性网卡实例ID，例如：eni-11112222。
        :rtype: str
        """
        return self._NetworkInterfaceId

    @NetworkInterfaceId.setter
    def NetworkInterfaceId(self, NetworkInterfaceId):
        self._NetworkInterfaceId = NetworkInterfaceId

    @property
    def PrivateIpAddresses(self):
        """指定的内网IP信息，单次最多指定10个。
        :rtype: list of PrivateIpAddressSpecification
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses


    def _deserialize(self, params):
        self._EcmRegion = params.get("EcmRegion")
        self._NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self._PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self._PrivateIpAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePrivateIpAddressesResponse(AbstractModel):
    """RemovePrivateIpAddresses返回参数结构体

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


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网实例ID，例如：subnet-3x5lf5q0。可通过DescribeSubnets接口查询。
        :type SubnetId: str
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param _EcmRegion: ECM 地域
        :type EcmRegion: str
        """
        self._SubnetId = None
        self._RouteTableId = None
        self._EcmRegion = None

    @property
    def SubnetId(self):
        """子网实例ID，例如：subnet-3x5lf5q0。可通过DescribeSubnets接口查询。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-azd4dt1c。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def EcmRegion(self):
        """ECM 地域
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._RouteTableId = params.get("RouteTableId")
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation返回参数结构体

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


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID。
        :type RouteTableId: str
        :param _Routes: 路由策略对象。
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """路由表实例ID。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def Routes(self):
        """路由策略对象。
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes返回参数结构体

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


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取
        :type SecurityGroupId: str
        :param _SecurityGroupPolicySet: 安全组规则集合对象。
        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        self._SecurityGroupId = None
        self._SecurityGroupPolicySet = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupPolicySet(self):
        """安全组规则集合对象。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`
        """
        return self._SecurityGroupPolicySet

    @SecurityGroupPolicySet.setter
    def SecurityGroupPolicySet(self, SecurityGroupPolicySet):
        self._SecurityGroupPolicySet = SecurityGroupPolicySet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self._SecurityGroupPolicySet = SecurityGroupPolicySet()
            self._SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy返回参数结构体

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


class ResetInstancesMaxBandwidthRequest(AbstractModel):
    """ResetInstancesMaxBandwidth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待重置带宽上限的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param _MaxBandwidthOut: 修改后的最大出带宽上限。
        :type MaxBandwidthOut: int
        :param _MaxBandwidthIn: 修改后的最大入带宽上限。
        :type MaxBandwidthIn: int
        """
        self._InstanceIdSet = None
        self._MaxBandwidthOut = None
        self._MaxBandwidthIn = None

    @property
    def InstanceIdSet(self):
        """待重置带宽上限的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def MaxBandwidthOut(self):
        """修改后的最大出带宽上限。
        :rtype: int
        """
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def MaxBandwidthIn(self):
        """修改后的最大入带宽上限。
        :rtype: int
        """
        return self._MaxBandwidthIn

    @MaxBandwidthIn.setter
    def MaxBandwidthIn(self, MaxBandwidthIn):
        self._MaxBandwidthIn = MaxBandwidthIn


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesMaxBandwidthResponse(AbstractModel):
    """ResetInstancesMaxBandwidth返回参数结构体

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


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待重置密码的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param _Password: 新密码，Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。
Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。
如果实例即包含Linux实例又包含Windows实例，则密码复杂度限制按照Windows实例的限制。
        :type Password: str
        :param _ForceStop: 是否强制关机，默认为false。
        :type ForceStop: bool
        :param _UserName: 待重置密码的实例的用户名，不得超过64个字符。若未指定用户名，则对于Linux而言，默认重置root用户的密码，对于Windows而言，默认重置administrator的密码。
        :type UserName: str
        """
        self._InstanceIdSet = None
        self._Password = None
        self._ForceStop = None
        self._UserName = None

    @property
    def InstanceIdSet(self):
        """待重置密码的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def Password(self):
        """新密码，Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。
Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。
如果实例即包含Linux实例又包含Windows实例，则密码复杂度限制按照Windows实例的限制。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def ForceStop(self):
        """是否强制关机，默认为false。
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def UserName(self):
        """待重置密码的实例的用户名，不得超过64个字符。若未指定用户名，则对于Linux而言，默认重置root用户的密码，对于Windows而言，默认重置administrator的密码。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._Password = params.get("Password")
        self._ForceStop = params.get("ForceStop")
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword返回参数结构体

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


class ResetInstancesRequest(AbstractModel):
    """ResetInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待重装的实例ID列表。
        :type InstanceIdSet: list of str
        :param _ImageId: 重装使用的镜像ID，若未指定，则使用各个实例当前的镜像进行重装。
        :type ImageId: str
        :param _Password: 密码设置，若未指定，则后续将以站内信的形式通知密码。
        :type Password: str
        :param _EnhancedService: 是否开启腾讯云可观测平台和主机安全服务，未指定时默认开启。
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param _KeepData: 是否保留数据盘数据，取值"true"/"false"。默认为"true"
        :type KeepData: str
        :param _KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：
TRUE：表示保持镜像的登录设置
FALSE：表示不保持镜像的登录设置

默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        """
        self._InstanceIdSet = None
        self._ImageId = None
        self._Password = None
        self._EnhancedService = None
        self._KeepData = None
        self._KeepImageLogin = None

    @property
    def InstanceIdSet(self):
        """待重装的实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ImageId(self):
        """重装使用的镜像ID，若未指定，则使用各个实例当前的镜像进行重装。
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def Password(self):
        """密码设置，若未指定，则后续将以站内信的形式通知密码。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def EnhancedService(self):
        """是否开启腾讯云可观测平台和主机安全服务，未指定时默认开启。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def KeepData(self):
        """是否保留数据盘数据，取值"true"/"false"。默认为"true"
        :rtype: str
        """
        return self._KeepData

    @KeepData.setter
    def KeepData(self, KeepData):
        self._KeepData = KeepData

    @property
    def KeepImageLogin(self):
        """保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：
TRUE：表示保持镜像的登录设置
FALSE：表示不保持镜像的登录设置

默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ImageId = params.get("ImageId")
        self._Password = params.get("Password")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        self._KeepData = params.get("KeepData")
        self._KeepImageLogin = params.get("KeepImageLogin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesResponse(AbstractModel):
    """ResetInstances返回参数结构体

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


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param _RouteTableName: 路由表名称，最大长度不能超过60个字节。
        :type RouteTableName: str
        :param _Routes: 路由策略。
        :type Routes: list of Route
        """
        self._RouteTableId = None
        self._RouteTableName = None
        self._Routes = None

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-azd4dt1c。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        """路由表名称，最大长度不能超过60个字节。
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def Routes(self):
        """路由策略。
        :rtype: list of Route
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self._Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes返回参数结构体

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


class Route(AbstractModel):
    """路由策略

    """

    def __init__(self):
        r"""
        :param _DestinationCidrBlock: 目的IPv4网段
        :type DestinationCidrBlock: str
        :param _GatewayType: 下一跳类型
NORMAL_CVM：普通云服务器；
        :type GatewayType: str
        :param _GatewayId: 下一跳地址
这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址
当 GatewayType 为 EIP 时，GatewayId 固定值 '0'
        :type GatewayId: str
        :param _RouteItemId: 路由策略唯一ID
        :type RouteItemId: str
        :param _RouteDescription: 路由策略描述
        :type RouteDescription: str
        :param _Enabled: 是否启用
        :type Enabled: bool
        :param _RouteType: 路由类型，目前我们支持的类型有：
USER：用户路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和操作 USER 类型的路由。
        :type RouteType: str
        :param _RouteId: 路由策略ID。IPv4路由策略ID是有意义的值，IPv6路由策略是无意义的值0。后续建议完全使用字符串唯一ID `RouteItemId`操作路由策略
        :type RouteId: int
        :param _RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        """
        self._DestinationCidrBlock = None
        self._GatewayType = None
        self._GatewayId = None
        self._RouteItemId = None
        self._RouteDescription = None
        self._Enabled = None
        self._RouteType = None
        self._RouteId = None
        self._RouteTableId = None

    @property
    def DestinationCidrBlock(self):
        """目的IPv4网段
        :rtype: str
        """
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def GatewayType(self):
        """下一跳类型
NORMAL_CVM：普通云服务器；
        :rtype: str
        """
        return self._GatewayType

    @GatewayType.setter
    def GatewayType(self, GatewayType):
        self._GatewayType = GatewayType

    @property
    def GatewayId(self):
        """下一跳地址
这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址
当 GatewayType 为 EIP 时，GatewayId 固定值 '0'
        :rtype: str
        """
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def RouteItemId(self):
        """路由策略唯一ID
        :rtype: str
        """
        return self._RouteItemId

    @RouteItemId.setter
    def RouteItemId(self, RouteItemId):
        self._RouteItemId = RouteItemId

    @property
    def RouteDescription(self):
        """路由策略描述
        :rtype: str
        """
        return self._RouteDescription

    @RouteDescription.setter
    def RouteDescription(self, RouteDescription):
        self._RouteDescription = RouteDescription

    @property
    def Enabled(self):
        """是否启用
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def RouteType(self):
        """路由类型，目前我们支持的类型有：
USER：用户路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和操作 USER 类型的路由。
        :rtype: str
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def RouteId(self):
        """路由策略ID。IPv4路由策略ID是有意义的值，IPv6路由策略是无意义的值0。后续建议完全使用字符串唯一ID `RouteItemId`操作路由策略
        :rtype: int
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-azd4dt1c。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId


    def _deserialize(self, params):
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        self._GatewayType = params.get("GatewayType")
        self._GatewayId = params.get("GatewayId")
        self._RouteItemId = params.get("RouteItemId")
        self._RouteDescription = params.get("RouteDescription")
        self._Enabled = params.get("Enabled")
        self._RouteType = params.get("RouteType")
        self._RouteId = params.get("RouteId")
        self._RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteConflict(AbstractModel):
    """路由冲突对象

    """

    def __init__(self):
        r"""
        :param _RouteTableId: 路由表实例ID
        :type RouteTableId: str
        :param _DestinationCidrBlock: 要检查的与之冲突的目的端
        :type DestinationCidrBlock: str
        :param _ConflictSet: 冲突的路由策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ConflictSet: list of Route
        """
        self._RouteTableId = None
        self._DestinationCidrBlock = None
        self._ConflictSet = None

    @property
    def RouteTableId(self):
        """路由表实例ID
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def DestinationCidrBlock(self):
        """要检查的与之冲突的目的端
        :rtype: str
        """
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def ConflictSet(self):
        """冲突的路由策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Route
        """
        return self._ConflictSet

    @ConflictSet.setter
    def ConflictSet(self, ConflictSet):
        self._ConflictSet = ConflictSet


    def _deserialize(self, params):
        self._RouteTableId = params.get("RouteTableId")
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        if params.get("ConflictSet") is not None:
            self._ConflictSet = []
            for item in params.get("ConflictSet"):
                obj = Route()
                obj._deserialize(item)
                self._ConflictSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTable(AbstractModel):
    """路由表

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID
        :type VpcId: str
        :param _RouteTableId: 路由表实例ID
        :type RouteTableId: str
        :param _RouteTableName: 路由表名称
        :type RouteTableName: str
        :param _AssociationSet: 路由表关联关系
注意：此字段可能返回 null，表示取不到有效值。
        :type AssociationSet: list of RouteTableAssociation
        :param _RouteSet: IPv4路由策略集合
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteSet: list of Route
        :param _Main: 是否默认路由表
        :type Main: bool
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        """
        self._VpcId = None
        self._RouteTableId = None
        self._RouteTableName = None
        self._AssociationSet = None
        self._RouteSet = None
        self._Main = None
        self._CreatedTime = None

    @property
    def VpcId(self):
        """VPC实例ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def RouteTableId(self):
        """路由表实例ID
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def RouteTableName(self):
        """路由表名称
        :rtype: str
        """
        return self._RouteTableName

    @RouteTableName.setter
    def RouteTableName(self, RouteTableName):
        self._RouteTableName = RouteTableName

    @property
    def AssociationSet(self):
        """路由表关联关系
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RouteTableAssociation
        """
        return self._AssociationSet

    @AssociationSet.setter
    def AssociationSet(self, AssociationSet):
        self._AssociationSet = AssociationSet

    @property
    def RouteSet(self):
        """IPv4路由策略集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Route
        """
        return self._RouteSet

    @RouteSet.setter
    def RouteSet(self, RouteSet):
        self._RouteSet = RouteSet

    @property
    def Main(self):
        """是否默认路由表
        :rtype: bool
        """
        return self._Main

    @Main.setter
    def Main(self, Main):
        self._Main = Main

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._RouteTableId = params.get("RouteTableId")
        self._RouteTableName = params.get("RouteTableName")
        if params.get("AssociationSet") is not None:
            self._AssociationSet = []
            for item in params.get("AssociationSet"):
                obj = RouteTableAssociation()
                obj._deserialize(item)
                self._AssociationSet.append(obj)
        if params.get("RouteSet") is not None:
            self._RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self._RouteSet.append(obj)
        self._Main = params.get("Main")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableAssociation(AbstractModel):
    """路由表关联关系

    """

    def __init__(self):
        r"""
        :param _SubnetId: 子网实例ID
        :type SubnetId: str
        :param _RouteTableId: 路由表实例ID
        :type RouteTableId: str
        """
        self._SubnetId = None
        self._RouteTableId = None

    @property
    def SubnetId(self):
        """子网实例ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def RouteTableId(self):
        """路由表实例ID
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealth(AbstractModel):
    """转发规则及健康状态列表

    """

    def __init__(self):
        r"""
        :param _Targets: 本规则上绑定的后端的健康检查状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of TargetHealth
        """
        self._Targets = None

    @property
    def Targets(self):
        """本规则上绑定的后端的健康检查状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TargetHealth
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunEIPDirectServiceEnabled(AbstractModel):
    """IP直通相关的信息

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开通IP直通。取值范围：
TRUE：表示开通IP直通
FALSE：表示不开通IP直通
默认取值：TRUE。
windows镜像目前不支持IP直通。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """是否开通IP直通。取值范围：
TRUE：表示开通IP直通
FALSE：表示不开通IP直通
默认取值：TRUE。
windows镜像目前不支持IP直通。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneInstanceCountISPSet: 需要创建实例的可用区及创建数目及运营商的列表。在单次请求的过程中，单个region下的请求创建实例数上限为100
        :type ZoneInstanceCountISPSet: list of ZoneInstanceCountISP
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：
Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]中的特殊符。Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /]中的特殊符号。
        :type Password: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。
1.如果未传该参数或者传的值为0，则使用模块下的默认值。
2.如果未传该参数或者传的值为0且未指定模块，则使用InternetMaxBandwidthIn的值
        :type InternetMaxBandwidthOut: int
        :param _ModuleId: 模块ID。如果未传该参数，则必须传ImageId，InstanceType，DataDiskSize，InternetMaxBandwidthOut参数
        :type ModuleId: str
        :param _ImageId: 镜像ID。如果未传该参数或者传的值为空，则使用模块下的默认值
        :type ImageId: str
        :param _InstanceName: 实例显示名称。
不指定实例显示名称则默认显示‘未命名’。
购买多台实例，如果指定模式串{R:x}，表示生成数字[x, x+n-1]，其中n表示购买实例的数量，例如server\_{R:3}，购买1台时，实例显示名称为server\_3；购买2台时，实例显示名称分别为server\_3，server\_4。
支持指定多个模式串{R:x}。
购买多台实例，如果不指定模式串，则在实例显示名称添加后缀1、2...n，其中n表示购买实例的数量，例如server_，购买2台时，实例显示名称分别为server\_1，server\_2。
如果购买的实例属于不同的地域或运营商，则上述规则在每个地域和运营商内独立计数。
最多支持60个字符（包含模式串）。
        :type InstanceName: str
        :param _HostName: 主机名称
点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。
Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。
其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。
        :type HostName: str
        :param _ClientToken: 用于保证请求幂等性的字符串。目前为保留参数，请勿使用。
        :type ClientToken: str
        :param _EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、腾讯云可观测平台等服务。若不指定该参数，则默认公共镜像开启腾讯云可观测平台、云安全服务
        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        :param _TagSpecification: 标签列表
        :type TagSpecification: list of TagSpecification
        :param _UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB
        :type UserData: str
        :param _InstanceType: 机型。如果未传该参数或者传的值为空，则使用模块下的默认值
        :type InstanceType: str
        :param _DataDiskSize: 数据盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值
        :type DataDiskSize: int
        :param _SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _SystemDiskSize: 系统盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值
        :type SystemDiskSize: int
        :param _InternetMaxBandwidthIn: 公网入带宽上限，单位：Mbps。
1.如果未传该参数或者传的值为0，则使用对应模块的默认值。
2.如果未传该参数或者传的值为0且未指定模块，则使用InternetMaxBandwidthOut
        :type InternetMaxBandwidthIn: int
        :param _InstanceChargeType: 实例计费类型。其中：
0，按资源维度后付费，计算当日用量峰值，例如CPU，内存，硬盘等，仅适用于非GNR系列机型；
1，按小时后付费，单价：xx元/实例/小时，仅适用于GNR机型，如需开通该计费方式请提工单申请；
2，按月后付费，单价：xx元/实例/月，仅适用于GNR机型；
该字段不填时，非GNR机型会默认选择0；GNR机型默认选择2。
        :type InstanceChargeType: int
        :param _KeyIds: 密钥对。
        :type KeyIds: list of str
        :param _KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：
TRUE：表示保持镜像的登录设置
FALSE：表示不保持镜像的登录设置

默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        :param _SystemDisk: 系统盘信息。
        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        :param _DataDisks: 数据盘信息。
        :type DataDisks: list of DataDisk
        """
        self._ZoneInstanceCountISPSet = None
        self._Password = None
        self._InternetMaxBandwidthOut = None
        self._ModuleId = None
        self._ImageId = None
        self._InstanceName = None
        self._HostName = None
        self._ClientToken = None
        self._EnhancedService = None
        self._TagSpecification = None
        self._UserData = None
        self._InstanceType = None
        self._DataDiskSize = None
        self._SecurityGroupIds = None
        self._SystemDiskSize = None
        self._InternetMaxBandwidthIn = None
        self._InstanceChargeType = None
        self._KeyIds = None
        self._KeepImageLogin = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def ZoneInstanceCountISPSet(self):
        """需要创建实例的可用区及创建数目及运营商的列表。在单次请求的过程中，单个region下的请求创建实例数上限为100
        :rtype: list of ZoneInstanceCountISP
        """
        return self._ZoneInstanceCountISPSet

    @ZoneInstanceCountISPSet.setter
    def ZoneInstanceCountISPSet(self, ZoneInstanceCountISPSet):
        self._ZoneInstanceCountISPSet = ZoneInstanceCountISPSet

    @property
    def Password(self):
        """实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：
Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]中的特殊符。Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /]中的特殊符号。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def InternetMaxBandwidthOut(self):
        """公网出带宽上限，单位：Mbps。
1.如果未传该参数或者传的值为0，则使用模块下的默认值。
2.如果未传该参数或者传的值为0且未指定模块，则使用InternetMaxBandwidthIn的值
        :rtype: int
        """
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def ModuleId(self):
        """模块ID。如果未传该参数，则必须传ImageId，InstanceType，DataDiskSize，InternetMaxBandwidthOut参数
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ImageId(self):
        """镜像ID。如果未传该参数或者传的值为空，则使用模块下的默认值
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InstanceName(self):
        """实例显示名称。
不指定实例显示名称则默认显示‘未命名’。
购买多台实例，如果指定模式串{R:x}，表示生成数字[x, x+n-1]，其中n表示购买实例的数量，例如server\_{R:3}，购买1台时，实例显示名称为server\_3；购买2台时，实例显示名称分别为server\_3，server\_4。
支持指定多个模式串{R:x}。
购买多台实例，如果不指定模式串，则在实例显示名称添加后缀1、2...n，其中n表示购买实例的数量，例如server_，购买2台时，实例显示名称分别为server\_1，server\_2。
如果购买的实例属于不同的地域或运营商，则上述规则在每个地域和运营商内独立计数。
最多支持60个字符（包含模式串）。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def HostName(self):
        """主机名称
点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。
Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。
其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def ClientToken(self):
        """用于保证请求幂等性的字符串。目前为保留参数，请勿使用。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def EnhancedService(self):
        """增强服务。通过该参数可以指定是否开启云安全、腾讯云可观测平台等服务。若不指定该参数，则默认公共镜像开启腾讯云可观测平台、云安全服务
        :rtype: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`
        """
        return self._EnhancedService

    @EnhancedService.setter
    def EnhancedService(self, EnhancedService):
        self._EnhancedService = EnhancedService

    @property
    def TagSpecification(self):
        """标签列表
        :rtype: list of TagSpecification
        """
        return self._TagSpecification

    @TagSpecification.setter
    def TagSpecification(self, TagSpecification):
        self._TagSpecification = TagSpecification

    @property
    def UserData(self):
        """提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB
        :rtype: str
        """
        return self._UserData

    @UserData.setter
    def UserData(self, UserData):
        self._UserData = UserData

    @property
    def InstanceType(self):
        """机型。如果未传该参数或者传的值为空，则使用模块下的默认值
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def DataDiskSize(self):
        """数据盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值
        :rtype: int
        """
        return self._DataDiskSize

    @DataDiskSize.setter
    def DataDiskSize(self, DataDiskSize):
        self._DataDiskSize = DataDiskSize

    @property
    def SecurityGroupIds(self):
        """实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def SystemDiskSize(self):
        """系统盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值
        :rtype: int
        """
        return self._SystemDiskSize

    @SystemDiskSize.setter
    def SystemDiskSize(self, SystemDiskSize):
        self._SystemDiskSize = SystemDiskSize

    @property
    def InternetMaxBandwidthIn(self):
        """公网入带宽上限，单位：Mbps。
1.如果未传该参数或者传的值为0，则使用对应模块的默认值。
2.如果未传该参数或者传的值为0且未指定模块，则使用InternetMaxBandwidthOut
        :rtype: int
        """
        return self._InternetMaxBandwidthIn

    @InternetMaxBandwidthIn.setter
    def InternetMaxBandwidthIn(self, InternetMaxBandwidthIn):
        self._InternetMaxBandwidthIn = InternetMaxBandwidthIn

    @property
    def InstanceChargeType(self):
        """实例计费类型。其中：
0，按资源维度后付费，计算当日用量峰值，例如CPU，内存，硬盘等，仅适用于非GNR系列机型；
1，按小时后付费，单价：xx元/实例/小时，仅适用于GNR机型，如需开通该计费方式请提工单申请；
2，按月后付费，单价：xx元/实例/月，仅适用于GNR机型；
该字段不填时，非GNR机型会默认选择0；GNR机型默认选择2。
        :rtype: int
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def KeyIds(self):
        """密钥对。
        :rtype: list of str
        """
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def KeepImageLogin(self):
        """保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：
TRUE：表示保持镜像的登录设置
FALSE：表示不保持镜像的登录设置

默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeepImageLogin

    @KeepImageLogin.setter
    def KeepImageLogin(self, KeepImageLogin):
        self._KeepImageLogin = KeepImageLogin

    @property
    def SystemDisk(self):
        """系统盘信息。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        """数据盘信息。
        :rtype: list of DataDisk
        """
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        if params.get("ZoneInstanceCountISPSet") is not None:
            self._ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ZoneInstanceCountISP()
                obj._deserialize(item)
                self._ZoneInstanceCountISPSet.append(obj)
        self._Password = params.get("Password")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._ModuleId = params.get("ModuleId")
        self._ImageId = params.get("ImageId")
        self._InstanceName = params.get("InstanceName")
        self._HostName = params.get("HostName")
        self._ClientToken = params.get("ClientToken")
        if params.get("EnhancedService") is not None:
            self._EnhancedService = EnhancedService()
            self._EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("TagSpecification") is not None:
            self._TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._TagSpecification.append(obj)
        self._UserData = params.get("UserData")
        self._InstanceType = params.get("InstanceType")
        self._DataDiskSize = params.get("DataDiskSize")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._SystemDiskSize = params.get("SystemDiskSize")
        self._InternetMaxBandwidthIn = params.get("InternetMaxBandwidthIn")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._KeyIds = params.get("KeyIds")
        self._KeepImageLogin = params.get("KeepImageLogin")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 创建中的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        """创建中的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

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
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """云监控服务

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启。
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        """是否开启。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """云镜服务；

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启。
        :type Enabled: bool
        :param _Version: 云镜版本：0 基础版，1 专业版。目前仅支持基础版
        :type Version: int
        """
        self._Enabled = None
        self._Version = None

    @property
    def Enabled(self):
        """是否开启。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Version(self):
        """云镜版本：0 基础版，1 专业版。目前仅支持基础版
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组对象

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID，例如：esg-ohuuioma。
        :type SecurityGroupId: str
        :param _SecurityGroupName: 安全组名称，可任意命名，但不得超过60个字符。
        :type SecurityGroupName: str
        :param _SecurityGroupDesc: 安全组备注，最多100个字符。
        :type SecurityGroupDesc: str
        :param _IsDefault: 是否是默认安全组，默认安全组不支持删除。
        :type IsDefault: bool
        :param _CreatedTime: 安全组创建时间。
        :type CreatedTime: str
        :param _TagSet: 标签键值对。
        :type TagSet: list of Tag
        """
        self._SecurityGroupId = None
        self._SecurityGroupName = None
        self._SecurityGroupDesc = None
        self._IsDefault = None
        self._CreatedTime = None
        self._TagSet = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如：esg-ohuuioma。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def SecurityGroupName(self):
        """安全组名称，可任意命名，但不得超过60个字符。
        :rtype: str
        """
        return self._SecurityGroupName

    @SecurityGroupName.setter
    def SecurityGroupName(self, SecurityGroupName):
        self._SecurityGroupName = SecurityGroupName

    @property
    def SecurityGroupDesc(self):
        """安全组备注，最多100个字符。
        :rtype: str
        """
        return self._SecurityGroupDesc

    @SecurityGroupDesc.setter
    def SecurityGroupDesc(self, SecurityGroupDesc):
        self._SecurityGroupDesc = SecurityGroupDesc

    @property
    def IsDefault(self):
        """是否是默认安全组，默认安全组不支持删除。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def CreatedTime(self):
        """安全组创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def TagSet(self):
        """标签键值对。
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._SecurityGroupName = params.get("SecurityGroupName")
        self._SecurityGroupDesc = params.get("SecurityGroupDesc")
        self._IsDefault = params.get("IsDefault")
        self._CreatedTime = params.get("CreatedTime")
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
        


class SecurityGroupAssociationStatistics(AbstractModel):
    """安全组关联的资源统计

    """

    def __init__(self):
        r"""
        :param _SecurityGroupId: 安全组实例ID。
        :type SecurityGroupId: str
        :param _ECM: ECM实例数。
        :type ECM: int
        :param _Module: ECM模块数。
        :type Module: int
        :param _ENI: 弹性网卡实例数。
        :type ENI: int
        :param _SG: 被安全组引用数。
        :type SG: int
        :param _CLB: 负载均衡实例数。
        :type CLB: int
        :param _InstanceStatistics: 全量实例的绑定统计。
        :type InstanceStatistics: list of InstanceStatistic
        :param _TotalCount: 所有资源的总计数（不包含被安全组引用数）。
        :type TotalCount: int
        """
        self._SecurityGroupId = None
        self._ECM = None
        self._Module = None
        self._ENI = None
        self._SG = None
        self._CLB = None
        self._InstanceStatistics = None
        self._TotalCount = None

    @property
    def SecurityGroupId(self):
        """安全组实例ID。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def ECM(self):
        """ECM实例数。
        :rtype: int
        """
        return self._ECM

    @ECM.setter
    def ECM(self, ECM):
        self._ECM = ECM

    @property
    def Module(self):
        """ECM模块数。
        :rtype: int
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def ENI(self):
        """弹性网卡实例数。
        :rtype: int
        """
        return self._ENI

    @ENI.setter
    def ENI(self, ENI):
        self._ENI = ENI

    @property
    def SG(self):
        """被安全组引用数。
        :rtype: int
        """
        return self._SG

    @SG.setter
    def SG(self, SG):
        self._SG = SG

    @property
    def CLB(self):
        """负载均衡实例数。
        :rtype: int
        """
        return self._CLB

    @CLB.setter
    def CLB(self, CLB):
        self._CLB = CLB

    @property
    def InstanceStatistics(self):
        """全量实例的绑定统计。
        :rtype: list of InstanceStatistic
        """
        return self._InstanceStatistics

    @InstanceStatistics.setter
    def InstanceStatistics(self, InstanceStatistics):
        self._InstanceStatistics = InstanceStatistics

    @property
    def TotalCount(self):
        """所有资源的总计数（不包含被安全组引用数）。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._SecurityGroupId = params.get("SecurityGroupId")
        self._ECM = params.get("ECM")
        self._Module = params.get("Module")
        self._ENI = params.get("ENI")
        self._SG = params.get("SG")
        self._CLB = params.get("CLB")
        if params.get("InstanceStatistics") is not None:
            self._InstanceStatistics = []
            for item in params.get("InstanceStatistics"):
                obj = InstanceStatistic()
                obj._deserialize(item)
                self._InstanceStatistics.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupLimitSet(AbstractModel):
    """用户安全组配额限制

    """

    def __init__(self):
        r"""
        :param _SecurityGroupLimit: 可创建安全组总数
        :type SecurityGroupLimit: int
        :param _SecurityGroupPolicyLimit: 安全组下的最大规则数
        :type SecurityGroupPolicyLimit: int
        :param _ReferedSecurityGroupLimit: 安全组下嵌套安全组规则数
        :type ReferedSecurityGroupLimit: int
        :param _SecurityGroupInstanceLimit: 单安全组关联实例数
        :type SecurityGroupInstanceLimit: int
        :param _InstanceSecurityGroupLimit: 实例关联安全组数
        :type InstanceSecurityGroupLimit: int
        :param _SecurityGroupModuleLimit: 单安全组关联的模块数
        :type SecurityGroupModuleLimit: int
        :param _ModuleSecurityGroupLimit: 模块关联的安全组数
        :type ModuleSecurityGroupLimit: int
        """
        self._SecurityGroupLimit = None
        self._SecurityGroupPolicyLimit = None
        self._ReferedSecurityGroupLimit = None
        self._SecurityGroupInstanceLimit = None
        self._InstanceSecurityGroupLimit = None
        self._SecurityGroupModuleLimit = None
        self._ModuleSecurityGroupLimit = None

    @property
    def SecurityGroupLimit(self):
        """可创建安全组总数
        :rtype: int
        """
        return self._SecurityGroupLimit

    @SecurityGroupLimit.setter
    def SecurityGroupLimit(self, SecurityGroupLimit):
        self._SecurityGroupLimit = SecurityGroupLimit

    @property
    def SecurityGroupPolicyLimit(self):
        """安全组下的最大规则数
        :rtype: int
        """
        return self._SecurityGroupPolicyLimit

    @SecurityGroupPolicyLimit.setter
    def SecurityGroupPolicyLimit(self, SecurityGroupPolicyLimit):
        self._SecurityGroupPolicyLimit = SecurityGroupPolicyLimit

    @property
    def ReferedSecurityGroupLimit(self):
        """安全组下嵌套安全组规则数
        :rtype: int
        """
        return self._ReferedSecurityGroupLimit

    @ReferedSecurityGroupLimit.setter
    def ReferedSecurityGroupLimit(self, ReferedSecurityGroupLimit):
        self._ReferedSecurityGroupLimit = ReferedSecurityGroupLimit

    @property
    def SecurityGroupInstanceLimit(self):
        """单安全组关联实例数
        :rtype: int
        """
        return self._SecurityGroupInstanceLimit

    @SecurityGroupInstanceLimit.setter
    def SecurityGroupInstanceLimit(self, SecurityGroupInstanceLimit):
        self._SecurityGroupInstanceLimit = SecurityGroupInstanceLimit

    @property
    def InstanceSecurityGroupLimit(self):
        """实例关联安全组数
        :rtype: int
        """
        return self._InstanceSecurityGroupLimit

    @InstanceSecurityGroupLimit.setter
    def InstanceSecurityGroupLimit(self, InstanceSecurityGroupLimit):
        self._InstanceSecurityGroupLimit = InstanceSecurityGroupLimit

    @property
    def SecurityGroupModuleLimit(self):
        """单安全组关联的模块数
        :rtype: int
        """
        return self._SecurityGroupModuleLimit

    @SecurityGroupModuleLimit.setter
    def SecurityGroupModuleLimit(self, SecurityGroupModuleLimit):
        self._SecurityGroupModuleLimit = SecurityGroupModuleLimit

    @property
    def ModuleSecurityGroupLimit(self):
        """模块关联的安全组数
        :rtype: int
        """
        return self._ModuleSecurityGroupLimit

    @ModuleSecurityGroupLimit.setter
    def ModuleSecurityGroupLimit(self, ModuleSecurityGroupLimit):
        self._ModuleSecurityGroupLimit = ModuleSecurityGroupLimit


    def _deserialize(self, params):
        self._SecurityGroupLimit = params.get("SecurityGroupLimit")
        self._SecurityGroupPolicyLimit = params.get("SecurityGroupPolicyLimit")
        self._ReferedSecurityGroupLimit = params.get("ReferedSecurityGroupLimit")
        self._SecurityGroupInstanceLimit = params.get("SecurityGroupInstanceLimit")
        self._InstanceSecurityGroupLimit = params.get("InstanceSecurityGroupLimit")
        self._SecurityGroupModuleLimit = params.get("SecurityGroupModuleLimit")
        self._ModuleSecurityGroupLimit = params.get("ModuleSecurityGroupLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    """安全组规则对象

    """

    def __init__(self):
        r"""
        :param _PolicyIndex: 安全组规则索引号
        :type PolicyIndex: int
        :param _Protocol: 协议, 取值: TCP,UDP, ICMP。
        :type Protocol: str
        :param _Port: 端口(all, 离散port, range)。
        :type Port: str
        :param _ServiceTemplate: 协议端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。
        :type ServiceTemplate: :class:`tencentcloud.ecm.v20190719.models.ServiceTemplateSpecification`
        :param _CidrBlock: 网段或IP(互斥)。
        :type CidrBlock: str
        :param _SecurityGroupId: 安全组实例ID，例如：esg-ohuuioma。
        :type SecurityGroupId: str
        :param _AddressTemplate: IP地址ID或者ID地址组ID。
        :type AddressTemplate: :class:`tencentcloud.ecm.v20190719.models.AddressTemplateSpecification`
        :param _Action: ACCEPT 或 DROP。
        :type Action: str
        :param _PolicyDescription: 安全组规则描述。
        :type PolicyDescription: str
        :param _ModifyTime: 修改时间，例如 2020-07-22 19：27：23
        :type ModifyTime: str
        :param _Ipv6CidrBlock: 网段或IPv6(互斥)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6CidrBlock: str
        """
        self._PolicyIndex = None
        self._Protocol = None
        self._Port = None
        self._ServiceTemplate = None
        self._CidrBlock = None
        self._SecurityGroupId = None
        self._AddressTemplate = None
        self._Action = None
        self._PolicyDescription = None
        self._ModifyTime = None
        self._Ipv6CidrBlock = None

    @property
    def PolicyIndex(self):
        """安全组规则索引号
        :rtype: int
        """
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def Protocol(self):
        """协议, 取值: TCP,UDP, ICMP。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """端口(all, 离散port, range)。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceTemplate(self):
        """协议端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ServiceTemplateSpecification`
        """
        return self._ServiceTemplate

    @ServiceTemplate.setter
    def ServiceTemplate(self, ServiceTemplate):
        self._ServiceTemplate = ServiceTemplate

    @property
    def CidrBlock(self):
        """网段或IP(互斥)。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def SecurityGroupId(self):
        """安全组实例ID，例如：esg-ohuuioma。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def AddressTemplate(self):
        """IP地址ID或者ID地址组ID。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AddressTemplateSpecification`
        """
        return self._AddressTemplate

    @AddressTemplate.setter
    def AddressTemplate(self, AddressTemplate):
        self._AddressTemplate = AddressTemplate

    @property
    def Action(self):
        """ACCEPT 或 DROP。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PolicyDescription(self):
        """安全组规则描述。
        :rtype: str
        """
        return self._PolicyDescription

    @PolicyDescription.setter
    def PolicyDescription(self, PolicyDescription):
        self._PolicyDescription = PolicyDescription

    @property
    def ModifyTime(self):
        """修改时间，例如 2020-07-22 19：27：23
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Ipv6CidrBlock(self):
        """网段或IPv6(互斥)。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock


    def _deserialize(self, params):
        self._PolicyIndex = params.get("PolicyIndex")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self._ServiceTemplate = ServiceTemplateSpecification()
            self._ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self._CidrBlock = params.get("CidrBlock")
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self._AddressTemplate = AddressTemplateSpecification()
            self._AddressTemplate._deserialize(params.get("AddressTemplate"))
        self._Action = params.get("Action")
        self._PolicyDescription = params.get("PolicyDescription")
        self._ModifyTime = params.get("ModifyTime")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicySet(AbstractModel):
    """安全组规则集合

    """

    def __init__(self):
        r"""
        :param _Version: 安全组规则当前版本。用户每次更新安全规则版本会自动加1，防止更新的路由规则已过期，不填不考虑冲突。
        :type Version: str
        :param _Egress: 出站规则。其中出站规则和入站规则必须选一个。
        :type Egress: list of SecurityGroupPolicy
        :param _Ingress: 入站规则。其中出站规则和入站规则必须选一个。
        :type Ingress: list of SecurityGroupPolicy
        """
        self._Version = None
        self._Egress = None
        self._Ingress = None

    @property
    def Version(self):
        """安全组规则当前版本。用户每次更新安全规则版本会自动加1，防止更新的路由规则已过期，不填不考虑冲突。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Egress(self):
        """出站规则。其中出站规则和入站规则必须选一个。
        :rtype: list of SecurityGroupPolicy
        """
        return self._Egress

    @Egress.setter
    def Egress(self, Egress):
        self._Egress = Egress

    @property
    def Ingress(self):
        """入站规则。其中出站规则和入站规则必须选一个。
        :rtype: list of SecurityGroupPolicy
        """
        return self._Ingress

    @Ingress.setter
    def Ingress(self, Ingress):
        self._Ingress = Ingress


    def _deserialize(self, params):
        self._Version = params.get("Version")
        if params.get("Egress") is not None:
            self._Egress = []
            for item in params.get("Egress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._Egress.append(obj)
        if params.get("Ingress") is not None:
            self._Ingress = []
            for item in params.get("Ingress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self._Ingress.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateSpecification(AbstractModel):
    """协议端口模板

    """

    def __init__(self):
        r"""
        :param _ServiceId: 协议端口ID，例如：eppm-f5n1f8da。
        :type ServiceId: str
        :param _ServiceGroupId: 协议端口组ID，例如：eppmg-f5n1f8da。
        :type ServiceGroupId: str
        """
        self._ServiceId = None
        self._ServiceGroupId = None

    @property
    def ServiceId(self):
        """协议端口ID，例如：eppm-f5n1f8da。
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceGroupId(self):
        """协议端口组ID，例如：eppmg-f5n1f8da。
        :rtype: str
        """
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param _SecurityGroups: 安全组ID构成的数组，一个负载均衡实例最多可绑定5个安全组，如果要解绑所有安全组，可不传此参数，或传入空数组
        :type SecurityGroups: list of str
        """
        self._LoadBalancerId = None
        self._SecurityGroups = None

    @property
    def LoadBalancerId(self):
        """负载均衡实例 ID
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SecurityGroups(self):
        """安全组ID构成的数组，一个负载均衡实例最多可绑定5个安全组，如果要解绑所有安全组，可不传此参数，或传入空数组
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups返回参数结构体

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


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 负载均衡实例ID数组
        :type LoadBalancerIds: list of str
        :param _SecurityGroup: 安全组ID，如 esg-12345678
        :type SecurityGroup: str
        :param _OperationType: ADD 绑定安全组；
DEL 解绑安全组
        :type OperationType: str
        """
        self._LoadBalancerIds = None
        self._SecurityGroup = None
        self._OperationType = None

    @property
    def LoadBalancerIds(self):
        """负载均衡实例ID数组
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def SecurityGroup(self):
        """安全组ID，如 esg-12345678
        :rtype: str
        """
        return self._SecurityGroup

    @SecurityGroup.setter
    def SecurityGroup(self, SecurityGroup):
        self._SecurityGroup = SecurityGroup

    @property
    def OperationType(self):
        """ADD 绑定安全组；
DEL 解绑安全组
        :rtype: str
        """
        return self._OperationType

    @OperationType.setter
    def OperationType(self, OperationType):
        self._OperationType = OperationType


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._SecurityGroup = params.get("SecurityGroup")
        self._OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers返回参数结构体

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


class SimpleModule(AbstractModel):
    """Module的简要信息

    """

    def __init__(self):
        r"""
        :param _ModuleId: 模块ID
        :type ModuleId: str
        :param _ModuleName: 模块名称
        :type ModuleName: str
        """
        self._ModuleId = None
        self._ModuleName = None

    @property
    def ModuleId(self):
        """模块ID
        :rtype: str
        """
        return self._ModuleId

    @ModuleId.setter
    def ModuleId(self, ModuleId):
        self._ModuleId = ModuleId

    @property
    def ModuleName(self):
        """模块名称
        :rtype: str
        """
        return self._ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName):
        self._ModuleName = ModuleName


    def _deserialize(self, params):
        self._ModuleId = params.get("ModuleId")
        self._ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Snapshot(AbstractModel):
    """描述了快照的详细信息

    """

    def __init__(self):
        r"""
        :param _Placement: 快照所在的位置。
        :type Placement: :class:`tencentcloud.ecm.v20190719.models.Placement`
        :param _CopyFromRemote: 是否为跨地域复制的快照。取值范围：<br><li>true：表示为跨地域复制的快照。<br><li>false:本地域的快照。
        :type CopyFromRemote: bool
        :param _IsPermanent: 是否为永久快照。取值范围：<br><li>true：永久快照<br><li>false：非永久快照。
        :type IsPermanent: bool
        :param _SnapshotName: 快照名称，用户自定义的快照别名。调用[ModifySnapshotAttribute](/document/product/362/15650)可修改此字段。
        :type SnapshotName: str
        :param _Percent: 快照创建进度百分比，快照创建成功后此字段恒为100。
        :type Percent: int
        :param _Images: 快照关联的镜像列表。
        :type Images: list of Image
        :param _ShareReference: 快照当前被共享数。
        :type ShareReference: int
        :param _SnapshotType: 快照类型，目前该项取值可以为PRIVATE_SNAPSHOT或者SHARED_SNAPSHOT
        :type SnapshotType: str
        :param _DiskSize: 创建此快照的云硬盘大小，单位GB。
        :type DiskSize: int
        :param _DiskId: 创建此快照的云硬盘ID。
        :type DiskId: str
        :param _CopyingToRegions: 快照正在跨地域复制的目的地域，默认取值为[]。
        :type CopyingToRegions: list of str
        :param _SnapshotId: 快照ID。
        :type SnapshotId: str
        :param _DiskUsage: 创建此快照的云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :type DiskUsage: str
        :param _Encrypt: 是否为加密盘创建的快照。取值范围：<br><li>true：该快照为加密盘创建的<br><li>false:非加密盘创建的快照。
        :type Encrypt: bool
        :param _CreateTime: 快照的创建时间。
        :type CreateTime: str
        :param _ImageCount: 快照关联的镜像个数。
        :type ImageCount: int
        :param _SnapshotState: 快照的状态。取值范围：<br><li>NORMAL：正常<br><li>CREATING：创建中<br><li>ROLLBACKING：回滚中<br><li>COPYING_FROM_REMOTE：跨地域复制中<br><li>CHECKING_COPIED：复制校验中<br><li>TORECYCLE：待回收。
        :type SnapshotState: str
        :param _DeadlineTime: 快照的到期时间。
        :type DeadlineTime: str
        :param _TimeStartShare: 快照开始共享的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeStartShare: str
        """
        self._Placement = None
        self._CopyFromRemote = None
        self._IsPermanent = None
        self._SnapshotName = None
        self._Percent = None
        self._Images = None
        self._ShareReference = None
        self._SnapshotType = None
        self._DiskSize = None
        self._DiskId = None
        self._CopyingToRegions = None
        self._SnapshotId = None
        self._DiskUsage = None
        self._Encrypt = None
        self._CreateTime = None
        self._ImageCount = None
        self._SnapshotState = None
        self._DeadlineTime = None
        self._TimeStartShare = None

    @property
    def Placement(self):
        """快照所在的位置。
        :rtype: :class:`tencentcloud.ecm.v20190719.models.Placement`
        """
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CopyFromRemote(self):
        """是否为跨地域复制的快照。取值范围：<br><li>true：表示为跨地域复制的快照。<br><li>false:本地域的快照。
        :rtype: bool
        """
        return self._CopyFromRemote

    @CopyFromRemote.setter
    def CopyFromRemote(self, CopyFromRemote):
        self._CopyFromRemote = CopyFromRemote

    @property
    def IsPermanent(self):
        """是否为永久快照。取值范围：<br><li>true：永久快照<br><li>false：非永久快照。
        :rtype: bool
        """
        return self._IsPermanent

    @IsPermanent.setter
    def IsPermanent(self, IsPermanent):
        self._IsPermanent = IsPermanent

    @property
    def SnapshotName(self):
        """快照名称，用户自定义的快照别名。调用[ModifySnapshotAttribute](/document/product/362/15650)可修改此字段。
        :rtype: str
        """
        return self._SnapshotName

    @SnapshotName.setter
    def SnapshotName(self, SnapshotName):
        self._SnapshotName = SnapshotName

    @property
    def Percent(self):
        """快照创建进度百分比，快照创建成功后此字段恒为100。
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def Images(self):
        """快照关联的镜像列表。
        :rtype: list of Image
        """
        return self._Images

    @Images.setter
    def Images(self, Images):
        self._Images = Images

    @property
    def ShareReference(self):
        """快照当前被共享数。
        :rtype: int
        """
        return self._ShareReference

    @ShareReference.setter
    def ShareReference(self, ShareReference):
        self._ShareReference = ShareReference

    @property
    def SnapshotType(self):
        """快照类型，目前该项取值可以为PRIVATE_SNAPSHOT或者SHARED_SNAPSHOT
        :rtype: str
        """
        return self._SnapshotType

    @SnapshotType.setter
    def SnapshotType(self, SnapshotType):
        self._SnapshotType = SnapshotType

    @property
    def DiskSize(self):
        """创建此快照的云硬盘大小，单位GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskId(self):
        """创建此快照的云硬盘ID。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def CopyingToRegions(self):
        """快照正在跨地域复制的目的地域，默认取值为[]。
        :rtype: list of str
        """
        return self._CopyingToRegions

    @CopyingToRegions.setter
    def CopyingToRegions(self, CopyingToRegions):
        self._CopyingToRegions = CopyingToRegions

    @property
    def SnapshotId(self):
        """快照ID。
        :rtype: str
        """
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def DiskUsage(self):
        """创建此快照的云硬盘类型。取值范围：<br><li>SYSTEM_DISK：系统盘<br><li>DATA_DISK：数据盘。
        :rtype: str
        """
        return self._DiskUsage

    @DiskUsage.setter
    def DiskUsage(self, DiskUsage):
        self._DiskUsage = DiskUsage

    @property
    def Encrypt(self):
        """是否为加密盘创建的快照。取值范围：<br><li>true：该快照为加密盘创建的<br><li>false:非加密盘创建的快照。
        :rtype: bool
        """
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def CreateTime(self):
        """快照的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ImageCount(self):
        """快照关联的镜像个数。
        :rtype: int
        """
        return self._ImageCount

    @ImageCount.setter
    def ImageCount(self, ImageCount):
        self._ImageCount = ImageCount

    @property
    def SnapshotState(self):
        """快照的状态。取值范围：<br><li>NORMAL：正常<br><li>CREATING：创建中<br><li>ROLLBACKING：回滚中<br><li>COPYING_FROM_REMOTE：跨地域复制中<br><li>CHECKING_COPIED：复制校验中<br><li>TORECYCLE：待回收。
        :rtype: str
        """
        return self._SnapshotState

    @SnapshotState.setter
    def SnapshotState(self, SnapshotState):
        self._SnapshotState = SnapshotState

    @property
    def DeadlineTime(self):
        """快照的到期时间。
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def TimeStartShare(self):
        """快照开始共享的时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeStartShare

    @TimeStartShare.setter
    def TimeStartShare(self, TimeStartShare):
        self._TimeStartShare = TimeStartShare


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CopyFromRemote = params.get("CopyFromRemote")
        self._IsPermanent = params.get("IsPermanent")
        self._SnapshotName = params.get("SnapshotName")
        self._Percent = params.get("Percent")
        if params.get("Images") is not None:
            self._Images = []
            for item in params.get("Images"):
                obj = Image()
                obj._deserialize(item)
                self._Images.append(obj)
        self._ShareReference = params.get("ShareReference")
        self._SnapshotType = params.get("SnapshotType")
        self._DiskSize = params.get("DiskSize")
        self._DiskId = params.get("DiskId")
        self._CopyingToRegions = params.get("CopyingToRegions")
        self._SnapshotId = params.get("SnapshotId")
        self._DiskUsage = params.get("DiskUsage")
        self._Encrypt = params.get("Encrypt")
        self._CreateTime = params.get("CreateTime")
        self._ImageCount = params.get("ImageCount")
        self._SnapshotState = params.get("SnapshotState")
        self._DeadlineTime = params.get("DeadlineTime")
        self._TimeStartShare = params.get("TimeStartShare")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrcImage(AbstractModel):
    """镜像来源信息

    """

    def __init__(self):
        r"""
        :param _ImageId: 镜像id
        :type ImageId: str
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _ImageOsName: 系统名称
        :type ImageOsName: str
        :param _ImageDescription: 镜像描述
        :type ImageDescription: str
        :param _Region: 区域
        :type Region: str
        :param _RegionID: 区域ID
        :type RegionID: int
        :param _RegionName: 区域名称
        :type RegionName: str
        :param _InstanceName: 来源实例名称
        :type InstanceName: str
        :param _InstanceId: 来源实例ID
        :type InstanceId: str
        :param _ImageType: 来源镜像类型
        :type ImageType: str
        """
        self._ImageId = None
        self._ImageName = None
        self._ImageOsName = None
        self._ImageDescription = None
        self._Region = None
        self._RegionID = None
        self._RegionName = None
        self._InstanceName = None
        self._InstanceId = None
        self._ImageType = None

    @property
    def ImageId(self):
        """镜像id
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        """镜像名称
        :rtype: str
        """
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def ImageOsName(self):
        """系统名称
        :rtype: str
        """
        return self._ImageOsName

    @ImageOsName.setter
    def ImageOsName(self, ImageOsName):
        self._ImageOsName = ImageOsName

    @property
    def ImageDescription(self):
        """镜像描述
        :rtype: str
        """
        return self._ImageDescription

    @ImageDescription.setter
    def ImageDescription(self, ImageDescription):
        self._ImageDescription = ImageDescription

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
    def RegionID(self):
        """区域ID
        :rtype: int
        """
        return self._RegionID

    @RegionID.setter
    def RegionID(self, RegionID):
        self._RegionID = RegionID

    @property
    def RegionName(self):
        """区域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def InstanceName(self):
        """来源实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceId(self):
        """来源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ImageType(self):
        """来源镜像类型
        :rtype: str
        """
        return self._ImageType

    @ImageType.setter
    def ImageType(self, ImageType):
        self._ImageType = ImageType


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._ImageOsName = params.get("ImageOsName")
        self._ImageDescription = params.get("ImageDescription")
        self._Region = params.get("Region")
        self._RegionID = params.get("RegionID")
        self._RegionName = params.get("RegionName")
        self._InstanceName = params.get("InstanceName")
        self._InstanceId = params.get("InstanceId")
        self._ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待开启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        """
        self._InstanceIdSet = None

    @property
    def InstanceIdSet(self):
        """待开启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances返回参数结构体

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


class StopInstancesRequest(AbstractModel):
    """StopInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 需要关机的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :type InstanceIdSet: list of str
        :param _ForceStop: 是否在正常关闭失败后选择强制关闭实例，默认为false，即否。
        :type ForceStop: bool
        :param _StopType: 实例的关闭模式。取值范围：
SOFT_FIRST：表示在正常关闭失败后进行强制关闭;
HARD：直接强制关闭;
SOFT：仅软关机；
默认为SOFT。
        :type StopType: str
        """
        self._InstanceIdSet = None
        self._ForceStop = None
        self._StopType = None

    @property
    def InstanceIdSet(self):
        """需要关机的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def ForceStop(self):
        """是否在正常关闭失败后选择强制关闭实例，默认为false，即否。
        :rtype: bool
        """
        return self._ForceStop

    @ForceStop.setter
    def ForceStop(self, ForceStop):
        self._ForceStop = ForceStop

    @property
    def StopType(self):
        """实例的关闭模式。取值范围：
SOFT_FIRST：表示在正常关闭失败后进行强制关闭;
HARD：直接强制关闭;
SOFT：仅软关机；
默认为SOFT。
        :rtype: str
        """
        return self._StopType

    @StopType.setter
    def StopType(self, StopType):
        self._StopType = StopType


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._ForceStop = params.get("ForceStop")
        self._StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances返回参数结构体

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


class Subnet(AbstractModel):
    """子网对象

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC实例ID。
        :type VpcId: str
        :param _SubnetId: 子网实例ID，例如：subnet-bthucmmy。
        :type SubnetId: str
        :param _SubnetName: 子网名称。
        :type SubnetName: str
        :param _CidrBlock: 子网的 IPv4 CIDR。
        :type CidrBlock: str
        :param _IsDefault: 是否默认子网。
        :type IsDefault: bool
        :param _EnableBroadcast: 是否开启广播。
        :type EnableBroadcast: bool
        :param _RouteTableId: 路由表实例ID，例如：rtb-l2h8d7c2。
        :type RouteTableId: str
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _AvailableIpAddressCount: 可用IP数。
        :type AvailableIpAddressCount: int
        :param _Ipv6CidrBlock: 子网的 IPv6 CIDR。
        :type Ipv6CidrBlock: str
        :param _NetworkAclId: 关联ACLID
        :type NetworkAclId: str
        :param _IsRemoteVpcSnat: 是否为 SNAT 地址池子网。
        :type IsRemoteVpcSnat: bool
        :param _TagSet: 标签键值对。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param _Zone: 所在区域
        :type Zone: str
        :param _ZoneName: 可用区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneName: str
        :param _InstanceCount: 实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param _VpcCidrBlock: VPC的 IPv4 CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param _VpcIpv6CidrBlock: VPC的 IPv6 CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcIpv6CidrBlock: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _ISPType: 运营商类型。'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
注意：此字段可能返回 null，表示取不到有效值。
        :type ISPType: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._SubnetName = None
        self._CidrBlock = None
        self._IsDefault = None
        self._EnableBroadcast = None
        self._RouteTableId = None
        self._CreatedTime = None
        self._AvailableIpAddressCount = None
        self._Ipv6CidrBlock = None
        self._NetworkAclId = None
        self._IsRemoteVpcSnat = None
        self._TagSet = None
        self._Zone = None
        self._ZoneName = None
        self._InstanceCount = None
        self._VpcCidrBlock = None
        self._VpcIpv6CidrBlock = None
        self._Region = None
        self._ISPType = None

    @property
    def VpcId(self):
        """VPC实例ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网实例ID，例如：subnet-bthucmmy。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def SubnetName(self):
        """子网名称。
        :rtype: str
        """
        return self._SubnetName

    @SubnetName.setter
    def SubnetName(self, SubnetName):
        self._SubnetName = SubnetName

    @property
    def CidrBlock(self):
        """子网的 IPv4 CIDR。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def IsDefault(self):
        """是否默认子网。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def EnableBroadcast(self):
        """是否开启广播。
        :rtype: bool
        """
        return self._EnableBroadcast

    @EnableBroadcast.setter
    def EnableBroadcast(self, EnableBroadcast):
        self._EnableBroadcast = EnableBroadcast

    @property
    def RouteTableId(self):
        """路由表实例ID，例如：rtb-l2h8d7c2。
        :rtype: str
        """
        return self._RouteTableId

    @RouteTableId.setter
    def RouteTableId(self, RouteTableId):
        self._RouteTableId = RouteTableId

    @property
    def CreatedTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def AvailableIpAddressCount(self):
        """可用IP数。
        :rtype: int
        """
        return self._AvailableIpAddressCount

    @AvailableIpAddressCount.setter
    def AvailableIpAddressCount(self, AvailableIpAddressCount):
        self._AvailableIpAddressCount = AvailableIpAddressCount

    @property
    def Ipv6CidrBlock(self):
        """子网的 IPv6 CIDR。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def NetworkAclId(self):
        """关联ACLID
        :rtype: str
        """
        return self._NetworkAclId

    @NetworkAclId.setter
    def NetworkAclId(self, NetworkAclId):
        self._NetworkAclId = NetworkAclId

    @property
    def IsRemoteVpcSnat(self):
        """是否为 SNAT 地址池子网。
        :rtype: bool
        """
        return self._IsRemoteVpcSnat

    @IsRemoteVpcSnat.setter
    def IsRemoteVpcSnat(self, IsRemoteVpcSnat):
        self._IsRemoteVpcSnat = IsRemoteVpcSnat

    @property
    def TagSet(self):
        """标签键值对。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def Zone(self):
        """所在区域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneName(self):
        """可用区名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceCount(self):
        """实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def VpcCidrBlock(self):
        """VPC的 IPv4 CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcCidrBlock

    @VpcCidrBlock.setter
    def VpcCidrBlock(self, VpcCidrBlock):
        self._VpcCidrBlock = VpcCidrBlock

    @property
    def VpcIpv6CidrBlock(self):
        """VPC的 IPv6 CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcIpv6CidrBlock

    @VpcIpv6CidrBlock.setter
    def VpcIpv6CidrBlock(self, VpcIpv6CidrBlock):
        self._VpcIpv6CidrBlock = VpcIpv6CidrBlock

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
    def ISPType(self):
        """运营商类型。'CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ISPType

    @ISPType.setter
    def ISPType(self, ISPType):
        self._ISPType = ISPType


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._SubnetName = params.get("SubnetName")
        self._CidrBlock = params.get("CidrBlock")
        self._IsDefault = params.get("IsDefault")
        self._EnableBroadcast = params.get("EnableBroadcast")
        self._RouteTableId = params.get("RouteTableId")
        self._CreatedTime = params.get("CreatedTime")
        self._AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._NetworkAclId = params.get("NetworkAclId")
        self._IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._Zone = params.get("Zone")
        self._ZoneName = params.get("ZoneName")
        self._InstanceCount = params.get("InstanceCount")
        self._VpcCidrBlock = params.get("VpcCidrBlock")
        self._VpcIpv6CidrBlock = params.get("VpcIpv6CidrBlock")
        self._Region = params.get("Region")
        self._ISPType = params.get("ISPType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    """用于描述系统盘。

    """

    def __init__(self):
        r"""
        :param _DiskType: 硬盘类型。取值范围：
- LOCAL_BASIC：本地硬盘；
- CLOUD_PREMIUM：高性能云硬盘；
默认取值：CLOUD_BASIC。
        :type DiskType: str
        :param _DiskId: 硬盘ID。此参数暂不可用。
        :type DiskId: str
        :param _DiskSize: 硬盘容量大小。单位GB。
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskId = None
        self._DiskSize = None

    @property
    def DiskType(self):
        """硬盘类型。取值范围：
- LOCAL_BASIC：本地硬盘；
- CLOUD_PREMIUM：高性能云硬盘；
默认取值：CLOUD_BASIC。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskId(self):
        """硬盘ID。此参数暂不可用。
        :rtype: str
        """
        return self._DiskId

    @DiskId.setter
    def DiskId(self, DiskId):
        self._DiskId = DiskId

    @property
    def DiskSize(self):
        """硬盘容量大小。单位GB。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskId = params.get("DiskId")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        r"""
        :param _Key: 标签健。
        :type Key: str
        :param _Value: 标签值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """标签健。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值。
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
        


class TagInfo(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键。
        :type TagKey: str
        :param _TagValue: 标签的值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签的键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签的值。
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
        


class TagSpecification(AbstractModel):
    """资源类型的Tag

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型，目前仅支持"instance"、"module"
        :type ResourceType: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        """资源类型，目前仅支持"instance"、"module"
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
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
        


class Target(AbstractModel):
    """负责均衡后端目标

    """

    def __init__(self):
        r"""
        :param _Port: 后端服务的监听端口
        :type Port: int
        :param _InstanceId: 子机ID
        :type InstanceId: str
        :param _Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        :param _EniIp: 绑定弹性网卡时需要传入此参数，代表弹性网卡的IP，弹性网卡必须先绑定至子机，然后才能绑定到负载均衡实例。注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。
        :type EniIp: str
        """
        self._Port = None
        self._InstanceId = None
        self._Weight = None
        self._EniIp = None

    @property
    def Port(self):
        """后端服务的监听端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def InstanceId(self):
        """子机ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Weight(self):
        """后端服务的转发权重，取值范围：[0, 100]，默认为 10。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def EniIp(self):
        """绑定弹性网卡时需要传入此参数，代表弹性网卡的IP，弹性网卡必须先绑定至子机，然后才能绑定到负载均衡实例。注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._InstanceId = params.get("InstanceId")
        self._Weight = params.get("Weight")
        self._EniIp = params.get("EniIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealth(AbstractModel):
    """后端的健康检查状态

    """

    def __init__(self):
        r"""
        :param _IP: Target的内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param _Port: Target绑定的端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _HealthStatus: 当前健康状态，true：健康，false：不健康（包括尚未开始探测、探测中、状态异常等几种状态）。只有处于健康状态（且权重大于0），负载均衡才会向其转发流量。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatus: bool
        :param _TargetId: Target的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetId: str
        :param _HealthStatusDetail: 当前健康状态的详细信息。如：Alive、Dead、Unknown、Close。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知，Close为未配置健康检查。
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatusDetail: str
        """
        self._IP = None
        self._Port = None
        self._HealthStatus = None
        self._TargetId = None
        self._HealthStatusDetail = None

    @property
    def IP(self):
        """Target的内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Port(self):
        """Target绑定的端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def HealthStatus(self):
        """当前健康状态，true：健康，false：不健康（包括尚未开始探测、探测中、状态异常等几种状态）。只有处于健康状态（且权重大于0），负载均衡才会向其转发流量。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def TargetId(self):
        """Target的实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def HealthStatusDetail(self):
        """当前健康状态的详细信息。如：Alive、Dead、Unknown、Close。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知，Close为未配置健康检查。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HealthStatusDetail

    @HealthStatusDetail.setter
    def HealthStatusDetail(self, HealthStatusDetail):
        self._HealthStatusDetail = HealthStatusDetail


    def _deserialize(self, params):
        self._IP = params.get("IP")
        self._Port = params.get("Port")
        self._HealthStatus = params.get("HealthStatus")
        self._TargetId = params.get("TargetId")
        self._HealthStatusDetail = params.get("HealthStatusDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetsWeightRule(AbstractModel):
    """目标和权重的描述信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 负载均衡监听器 ID
        :type ListenerId: str
        :param _Targets: 要修改权重的后端机器列表
        :type Targets: list of Target
        :param _Weight: 后端服务新的转发权重，取值范围：0~100。
        :type Weight: int
        """
        self._ListenerId = None
        self._Targets = None
        self._Weight = None

    @property
    def ListenerId(self):
        """负载均衡监听器 ID
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Targets(self):
        """要修改权重的后端机器列表
        :rtype: list of Target
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def Weight(self):
        """后端服务新的转发权重，取值范围：0~100。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """任务查询

    """

    def __init__(self):
        r"""
        :param _Operation: 操作名，即API名称，比如：CreateImage
        :type Operation: str
        :param _TaskId: 任务id
        :type TaskId: str
        """
        self._Operation = None
        self._TaskId = None

    @property
    def Operation(self):
        """操作名，即API名称，比如：CreateImage
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutput(AbstractModel):
    """任务查询出参

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务id
        :type TaskId: str
        :param _Message: 状态描述
        :type Message: str
        :param _Status: 状态值，SUCCESS/FAILED/OPERATING
        :type Status: str
        :param _AddTime: 任务提交时间
        :type AddTime: str
        :param _EndTime: 任务结束时间
        :type EndTime: str
        :param _Operation: 操作名
        :type Operation: str
        """
        self._TaskId = None
        self._Message = None
        self._Status = None
        self._AddTime = None
        self._EndTime = None
        self._Operation = None

    @property
    def TaskId(self):
        """任务id
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Message(self):
        """状态描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Status(self):
        """状态值，SUCCESS/FAILED/OPERATING
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AddTime(self):
        """任务提交时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def EndTime(self):
        """任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Operation(self):
        """操作名
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Message = params.get("Message")
        self._Status = params.get("Status")
        self._AddTime = params.get("AddTime")
        self._EndTime = params.get("EndTime")
        self._Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksRequest(AbstractModel):
    """TerminateDisks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DiskIds: 需退还的云盘ID列表。
        :type DiskIds: list of str
        """
        self._DiskIds = None

    @property
    def DiskIds(self):
        """需退还的云盘ID列表。
        :rtype: list of str
        """
        return self._DiskIds

    @DiskIds.setter
    def DiskIds(self, DiskIds):
        self._DiskIds = DiskIds


    def _deserialize(self, params):
        self._DiskIds = params.get("DiskIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateDisksResponse(AbstractModel):
    """TerminateDisks返回参数结构体

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


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 待销毁的实例ID列表。
        :type InstanceIdSet: list of str
        :param _TerminateDelay: 是否定时销毁，默认为否。
        :type TerminateDelay: bool
        :param _TerminateTime: 定时销毁的时间，格式形如："2019-08-05 12:01:30"，若非定时销毁，则此参数被忽略。
        :type TerminateTime: str
        :param _AssociatedResourceDestroy: 是否关联删除已绑定的弹性网卡和弹性IP，默认为true。
当为true时，一并删除弹性网卡和弹性IP；
当为false时，只销毁主机，保留弹性网卡和弹性IP。
        :type AssociatedResourceDestroy: bool
        """
        self._InstanceIdSet = None
        self._TerminateDelay = None
        self._TerminateTime = None
        self._AssociatedResourceDestroy = None

    @property
    def InstanceIdSet(self):
        """待销毁的实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def TerminateDelay(self):
        """是否定时销毁，默认为否。
        :rtype: bool
        """
        return self._TerminateDelay

    @TerminateDelay.setter
    def TerminateDelay(self, TerminateDelay):
        self._TerminateDelay = TerminateDelay

    @property
    def TerminateTime(self):
        """定时销毁的时间，格式形如："2019-08-05 12:01:30"，若非定时销毁，则此参数被忽略。
        :rtype: str
        """
        return self._TerminateTime

    @TerminateTime.setter
    def TerminateTime(self, TerminateTime):
        self._TerminateTime = TerminateTime

    @property
    def AssociatedResourceDestroy(self):
        """是否关联删除已绑定的弹性网卡和弹性IP，默认为true。
当为true时，一并删除弹性网卡和弹性IP；
当为false时，只销毁主机，保留弹性网卡和弹性IP。
        :rtype: bool
        """
        return self._AssociatedResourceDestroy

    @AssociatedResourceDestroy.setter
    def AssociatedResourceDestroy(self, AssociatedResourceDestroy):
        self._AssociatedResourceDestroy = AssociatedResourceDestroy


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._TerminateDelay = params.get("TerminateDelay")
        self._TerminateTime = params.get("TerminateTime")
        self._AssociatedResourceDestroy = params.get("AssociatedResourceDestroy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回参数结构体

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


class UnassignIpv6SubnetCidrBlockRequest(AbstractModel):
    """UnassignIpv6SubnetCidrBlock请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VpcId: 子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。	
        :type VpcId: str
        :param _Ipv6SubnetCidrBlocks: `IPv6` 子网段列表。	
        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock
        :param _EcmRegion: ECM地域。
        :type EcmRegion: str
        """
        self._VpcId = None
        self._Ipv6SubnetCidrBlocks = None
        self._EcmRegion = None

    @property
    def VpcId(self):
        """子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。	
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Ipv6SubnetCidrBlocks(self):
        """`IPv6` 子网段列表。	
        :rtype: list of Ipv6SubnetCidrBlock
        """
        return self._Ipv6SubnetCidrBlocks

    @Ipv6SubnetCidrBlocks.setter
    def Ipv6SubnetCidrBlocks(self, Ipv6SubnetCidrBlocks):
        self._Ipv6SubnetCidrBlocks = Ipv6SubnetCidrBlocks

    @property
    def EcmRegion(self):
        """ECM地域。
        :rtype: str
        """
        return self._EcmRegion

    @EcmRegion.setter
    def EcmRegion(self, EcmRegion):
        self._EcmRegion = EcmRegion


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self._Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self._Ipv6SubnetCidrBlocks.append(obj)
        self._EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignIpv6SubnetCidrBlockResponse(AbstractModel):
    """UnassignIpv6SubnetCidrBlock返回参数结构体

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


class VirtualPrivateCloud(AbstractModel):
    """私有网络相关信息配置。

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID，形如vpc-xxx。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如subnet-xxx。
        :type SubnetId: str
        :param _AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：
TRUE：表示用作公网网关
FALSE：表示不用作公网网关

默认取值：FALSE。
        :type AsVpcGateway: bool
        :param _PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: 为弹性网卡指定随机生成的 IPv6 地址数量。
        :type Ipv6AddressCount: int
        :param _Ipv6SubnetIds: runInstances接口创建三网ipv6地址使用
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6SubnetIds: list of str
        """
        self._VpcId = None
        self._SubnetId = None
        self._AsVpcGateway = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None
        self._Ipv6SubnetIds = None

    @property
    def VpcId(self):
        """私有网络ID，形如vpc-xxx。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """私有网络子网ID，形如subnet-xxx。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def AsVpcGateway(self):
        """是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：
TRUE：表示用作公网网关
FALSE：表示不用作公网网关

默认取值：FALSE。
        :rtype: bool
        """
        return self._AsVpcGateway

    @AsVpcGateway.setter
    def AsVpcGateway(self, AsVpcGateway):
        self._AsVpcGateway = AsVpcGateway

    @property
    def PrivateIpAddresses(self):
        """私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        """为弹性网卡指定随机生成的 IPv6 地址数量。
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def Ipv6SubnetIds(self):
        """runInstances接口创建三网ipv6地址使用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Ipv6SubnetIds

    @Ipv6SubnetIds.setter
    def Ipv6SubnetIds(self, Ipv6SubnetIds):
        self._Ipv6SubnetIds = Ipv6SubnetIds


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._AsVpcGateway = params.get("AsVpcGateway")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._Ipv6SubnetIds = params.get("Ipv6SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """私有网络(VPC) 对象。

    """

    def __init__(self):
        r"""
        :param _VpcName: VPC名称。
        :type VpcName: str
        :param _VpcId: VPC实例ID，例如：vpc-azd4dt1c。
        :type VpcId: str
        :param _CidrBlock: VPC的IPv4 CIDR。
        :type CidrBlock: str
        :param _IsDefault: 是否默认VPC。
        :type IsDefault: bool
        :param _EnableMulticast: 是否开启组播。
        :type EnableMulticast: bool
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _DnsServerSet: DNS列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DnsServerSet: list of str
        :param _DomainName: DHCP域名选项值。
        :type DomainName: str
        :param _DhcpOptionsId: DHCP选项集ID。
        :type DhcpOptionsId: str
        :param _EnableDhcp: 是否开启DHCP。
        :type EnableDhcp: bool
        :param _Ipv6CidrBlock: VPC的IPv6 CIDR。
        :type Ipv6CidrBlock: str
        :param _TagSet: 标签键值对
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param _AssistantCidrSet: 辅助CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type AssistantCidrSet: list of AssistantCidr
        :param _Region: 地域
        :type Region: str
        :param _Description: 描述
        :type Description: str
        :param _RegionName: 地域中文名
        :type RegionName: str
        :param _SubnetCount: 包含子网数量
        :type SubnetCount: int
        :param _InstanceCount: 包含实例数量
        :type InstanceCount: int
        :param _Ipv6ISP: ipv6运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6ISP: str
        :param _Ipv6CidrBlockSet: 多运营商IPv6 Cidr Block。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6CidrBlockSet: list of ISPIPv6CidrBlock
        """
        self._VpcName = None
        self._VpcId = None
        self._CidrBlock = None
        self._IsDefault = None
        self._EnableMulticast = None
        self._CreatedTime = None
        self._DnsServerSet = None
        self._DomainName = None
        self._DhcpOptionsId = None
        self._EnableDhcp = None
        self._Ipv6CidrBlock = None
        self._TagSet = None
        self._AssistantCidrSet = None
        self._Region = None
        self._Description = None
        self._RegionName = None
        self._SubnetCount = None
        self._InstanceCount = None
        self._Ipv6ISP = None
        self._Ipv6CidrBlockSet = None

    @property
    def VpcName(self):
        """VPC名称。
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def VpcId(self):
        """VPC实例ID，例如：vpc-azd4dt1c。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def CidrBlock(self):
        """VPC的IPv4 CIDR。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def IsDefault(self):
        """是否默认VPC。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def EnableMulticast(self):
        """是否开启组播。
        :rtype: bool
        """
        return self._EnableMulticast

    @EnableMulticast.setter
    def EnableMulticast(self, EnableMulticast):
        self._EnableMulticast = EnableMulticast

    @property
    def CreatedTime(self):
        """创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DnsServerSet(self):
        """DNS列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._DnsServerSet

    @DnsServerSet.setter
    def DnsServerSet(self, DnsServerSet):
        self._DnsServerSet = DnsServerSet

    @property
    def DomainName(self):
        """DHCP域名选项值。
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DhcpOptionsId(self):
        """DHCP选项集ID。
        :rtype: str
        """
        return self._DhcpOptionsId

    @DhcpOptionsId.setter
    def DhcpOptionsId(self, DhcpOptionsId):
        self._DhcpOptionsId = DhcpOptionsId

    @property
    def EnableDhcp(self):
        """是否开启DHCP。
        :rtype: bool
        """
        return self._EnableDhcp

    @EnableDhcp.setter
    def EnableDhcp(self, EnableDhcp):
        self._EnableDhcp = EnableDhcp

    @property
    def Ipv6CidrBlock(self):
        """VPC的IPv6 CIDR。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def TagSet(self):
        """标签键值对
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AssistantCidrSet(self):
        """辅助CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AssistantCidr
        """
        return self._AssistantCidrSet

    @AssistantCidrSet.setter
    def AssistantCidrSet(self, AssistantCidrSet):
        self._AssistantCidrSet = AssistantCidrSet

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Description(self):
        """描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RegionName(self):
        """地域中文名
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def SubnetCount(self):
        """包含子网数量
        :rtype: int
        """
        return self._SubnetCount

    @SubnetCount.setter
    def SubnetCount(self, SubnetCount):
        self._SubnetCount = SubnetCount

    @property
    def InstanceCount(self):
        """包含实例数量
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def Ipv6ISP(self):
        """ipv6运营商
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ipv6ISP

    @Ipv6ISP.setter
    def Ipv6ISP(self, Ipv6ISP):
        self._Ipv6ISP = Ipv6ISP

    @property
    def Ipv6CidrBlockSet(self):
        """多运营商IPv6 Cidr Block。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ISPIPv6CidrBlock
        """
        return self._Ipv6CidrBlockSet

    @Ipv6CidrBlockSet.setter
    def Ipv6CidrBlockSet(self, Ipv6CidrBlockSet):
        self._Ipv6CidrBlockSet = Ipv6CidrBlockSet


    def _deserialize(self, params):
        self._VpcName = params.get("VpcName")
        self._VpcId = params.get("VpcId")
        self._CidrBlock = params.get("CidrBlock")
        self._IsDefault = params.get("IsDefault")
        self._EnableMulticast = params.get("EnableMulticast")
        self._CreatedTime = params.get("CreatedTime")
        self._DnsServerSet = params.get("DnsServerSet")
        self._DomainName = params.get("DomainName")
        self._DhcpOptionsId = params.get("DhcpOptionsId")
        self._EnableDhcp = params.get("EnableDhcp")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("AssistantCidrSet") is not None:
            self._AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self._AssistantCidrSet.append(obj)
        self._Region = params.get("Region")
        self._Description = params.get("Description")
        self._RegionName = params.get("RegionName")
        self._SubnetCount = params.get("SubnetCount")
        self._InstanceCount = params.get("InstanceCount")
        self._Ipv6ISP = params.get("Ipv6ISP")
        if params.get("Ipv6CidrBlockSet") is not None:
            self._Ipv6CidrBlockSet = []
            for item in params.get("Ipv6CidrBlockSet"):
                obj = ISPIPv6CidrBlock()
                obj._deserialize(item)
                self._Ipv6CidrBlockSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Zone信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: ZoneId
        :type ZoneId: int
        :param _ZoneName: ZoneName
        :type ZoneName: str
        :param _Zone: Zone
        :type Zone: str
        """
        self._ZoneId = None
        self._ZoneName = None
        self._Zone = None

    @property
    def ZoneId(self):
        """ZoneId
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        """ZoneName
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def Zone(self):
        """Zone
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceCountISP(AbstractModel):
    """实例可用区及对应的实例创建数目及运营商的组合；

    """

    def __init__(self):
        r"""
        :param _Zone: 创建实例的可用区。
        :type Zone: str
        :param _InstanceCount: 在当前可用区创建的实例数目。
        :type InstanceCount: int
        :param _ISP: 运营商如下：
CTCC：中国电信
CUCC：中国联通
CMCC：中国移动
CMCC;CUCC;CTCC：三网；三网需要开通白名单，请直接联系腾讯云客服。
        :type ISP: str
        :param _VpcId: 指定私有网络编号，SubnetId与VpcId必须同时指定或不指定
        :type VpcId: str
        :param _SubnetId: 指定子网编号，SubnetId与VpcId必须同时指定或不指定
        :type SubnetId: str
        :param _PrivateIpAddresses: 指定主网卡内网IP。条件：SubnetId与VpcId必须同时指定，并且IP数量与InstanceCount相同，多IP主机副网卡内网IP在相同子网内通过DHCP获取。
        :type PrivateIpAddresses: list of str
        :param _Ipv6AddressCount: 为弹性网卡指定随机生成的IPv6地址数量，单网情况下是1，单网需要ISP 只能为单网运营商，三网情况3
        :type Ipv6AddressCount: int
        :param _Ipv6SubnetIds: 指定创建三网ipv6地址，使用的subnet数组，只创建ipv4不创建ipv6和单网ipv6子网依然使用SubnetId字段；
该数组必须且仅支持传入三个不同的子网，并且这三个子网各自分配了电信、联通、移动三个运营商的其中一个IPV6 CIDR网段
        :type Ipv6SubnetIds: list of str
        """
        self._Zone = None
        self._InstanceCount = None
        self._ISP = None
        self._VpcId = None
        self._SubnetId = None
        self._PrivateIpAddresses = None
        self._Ipv6AddressCount = None
        self._Ipv6SubnetIds = None

    @property
    def Zone(self):
        """创建实例的可用区。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceCount(self):
        """在当前可用区创建的实例数目。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ISP(self):
        """运营商如下：
CTCC：中国电信
CUCC：中国联通
CMCC：中国移动
CMCC;CUCC;CTCC：三网；三网需要开通白名单，请直接联系腾讯云客服。
        :rtype: str
        """
        return self._ISP

    @ISP.setter
    def ISP(self, ISP):
        self._ISP = ISP

    @property
    def VpcId(self):
        """指定私有网络编号，SubnetId与VpcId必须同时指定或不指定
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """指定子网编号，SubnetId与VpcId必须同时指定或不指定
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def PrivateIpAddresses(self):
        """指定主网卡内网IP。条件：SubnetId与VpcId必须同时指定，并且IP数量与InstanceCount相同，多IP主机副网卡内网IP在相同子网内通过DHCP获取。
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def Ipv6AddressCount(self):
        """为弹性网卡指定随机生成的IPv6地址数量，单网情况下是1，单网需要ISP 只能为单网运营商，三网情况3
        :rtype: int
        """
        return self._Ipv6AddressCount

    @Ipv6AddressCount.setter
    def Ipv6AddressCount(self, Ipv6AddressCount):
        self._Ipv6AddressCount = Ipv6AddressCount

    @property
    def Ipv6SubnetIds(self):
        """指定创建三网ipv6地址，使用的subnet数组，只创建ipv4不创建ipv6和单网ipv6子网依然使用SubnetId字段；
该数组必须且仅支持传入三个不同的子网，并且这三个子网各自分配了电信、联通、移动三个运营商的其中一个IPV6 CIDR网段
        :rtype: list of str
        """
        return self._Ipv6SubnetIds

    @Ipv6SubnetIds.setter
    def Ipv6SubnetIds(self, Ipv6SubnetIds):
        self._Ipv6SubnetIds = Ipv6SubnetIds


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        self._InstanceCount = params.get("InstanceCount")
        self._ISP = params.get("ISP")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._Ipv6AddressCount = params.get("Ipv6AddressCount")
        self._Ipv6SubnetIds = params.get("Ipv6SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceInfo(AbstractModel):
    """Zone的实例信息

    """

    def __init__(self):
        r"""
        :param _ZoneName: Zone名称
        :type ZoneName: str
        :param _InstanceNum: 实例数量
        :type InstanceNum: int
        """
        self._ZoneName = None
        self._InstanceNum = None

    @property
    def ZoneName(self):
        """Zone名称
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def InstanceNum(self):
        """实例数量
        :rtype: int
        """
        return self._InstanceNum

    @InstanceNum.setter
    def InstanceNum(self, InstanceNum):
        self._InstanceNum = InstanceNum


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        self._InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        