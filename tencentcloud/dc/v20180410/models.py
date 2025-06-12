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


class AcceptDirectConnectTunnelRequest(AbstractModel):
    """AcceptDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。可以通过[DescribeDirectConnectTunnels](https://cloud.tencent.com/document/product/216/19819)接口获取。
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。可以通过[DescribeDirectConnectTunnels](https://cloud.tencent.com/document/product/216/19819)接口获取。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel返回参数结构体

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


class AccessPoint(AbstractModel):
    """接入点信息。

    """

    def __init__(self):
        r"""
        :param _AccessPointName: 接入点的名称。
        :type AccessPointName: str
        :param _AccessPointId: 接入点唯一ID。
        :type AccessPointId: str
        :param _State: 接入点的状态。可用，不可用。
        :type State: str
        :param _Location: 接入点的位置。
        :type Location: str
        :param _LineOperator: 接入点支持的运营商列表。
        :type LineOperator: list of str
        :param _RegionId: 接入点管理的大区ID。
        :type RegionId: str
        :param _AvailablePortType: 接入点可用的端口类型列表。1000BASE-T代表千兆电口，1000BASE-LX代表千兆单模光口10km，1000BASE-ZX代表千兆单模光口80km,10GBASE-LR代表万兆单模光口10km,10GBASE-ZR代表万兆单模光口80km,10GBASE-LH代表万兆单模光口40km,100GBASE-LR4代表100G单模光口10km。
        :type AvailablePortType: list of str
        :param _Coordinate: 接入点经纬度。
        :type Coordinate: :class:`tencentcloud.dc.v20180410.models.Coordinate`
        :param _City: 接入点所在城市。
        :type City: str
        :param _Area: 接入点地域名称。
        :type Area: str
        :param _AccessPointType: 接入点类型。VXLAN/QCPL/QCAR
        :type AccessPointType: str
        :param _AvailablePortInfo: 端口规格信息。
        :type AvailablePortInfo: list of PortSpecification
        :param _Address: 接入点地址。
        :type Address: str
        :param _IsMacSec: 是否MACsec
        :type IsMacSec: bool
        """
        self._AccessPointName = None
        self._AccessPointId = None
        self._State = None
        self._Location = None
        self._LineOperator = None
        self._RegionId = None
        self._AvailablePortType = None
        self._Coordinate = None
        self._City = None
        self._Area = None
        self._AccessPointType = None
        self._AvailablePortInfo = None
        self._Address = None
        self._IsMacSec = None

    @property
    def AccessPointName(self):
        """接入点的名称。
        :rtype: str
        """
        return self._AccessPointName

    @AccessPointName.setter
    def AccessPointName(self, AccessPointName):
        self._AccessPointName = AccessPointName

    @property
    def AccessPointId(self):
        """接入点唯一ID。
        :rtype: str
        """
        return self._AccessPointId

    @AccessPointId.setter
    def AccessPointId(self, AccessPointId):
        self._AccessPointId = AccessPointId

    @property
    def State(self):
        """接入点的状态。可用，不可用。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Location(self):
        """接入点的位置。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def LineOperator(self):
        """接入点支持的运营商列表。
        :rtype: list of str
        """
        return self._LineOperator

    @LineOperator.setter
    def LineOperator(self, LineOperator):
        self._LineOperator = LineOperator

    @property
    def RegionId(self):
        """接入点管理的大区ID。
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def AvailablePortType(self):
        """接入点可用的端口类型列表。1000BASE-T代表千兆电口，1000BASE-LX代表千兆单模光口10km，1000BASE-ZX代表千兆单模光口80km,10GBASE-LR代表万兆单模光口10km,10GBASE-ZR代表万兆单模光口80km,10GBASE-LH代表万兆单模光口40km,100GBASE-LR4代表100G单模光口10km。
        :rtype: list of str
        """
        return self._AvailablePortType

    @AvailablePortType.setter
    def AvailablePortType(self, AvailablePortType):
        self._AvailablePortType = AvailablePortType

    @property
    def Coordinate(self):
        """接入点经纬度。
        :rtype: :class:`tencentcloud.dc.v20180410.models.Coordinate`
        """
        return self._Coordinate

    @Coordinate.setter
    def Coordinate(self, Coordinate):
        self._Coordinate = Coordinate

    @property
    def City(self):
        """接入点所在城市。
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Area(self):
        """接入点地域名称。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AccessPointType(self):
        """接入点类型。VXLAN/QCPL/QCAR
        :rtype: str
        """
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType

    @property
    def AvailablePortInfo(self):
        """端口规格信息。
        :rtype: list of PortSpecification
        """
        return self._AvailablePortInfo

    @AvailablePortInfo.setter
    def AvailablePortInfo(self, AvailablePortInfo):
        self._AvailablePortInfo = AvailablePortInfo

    @property
    def Address(self):
        """接入点地址。
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def IsMacSec(self):
        """是否MACsec
        :rtype: bool
        """
        return self._IsMacSec

    @IsMacSec.setter
    def IsMacSec(self, IsMacSec):
        self._IsMacSec = IsMacSec


    def _deserialize(self, params):
        self._AccessPointName = params.get("AccessPointName")
        self._AccessPointId = params.get("AccessPointId")
        self._State = params.get("State")
        self._Location = params.get("Location")
        self._LineOperator = params.get("LineOperator")
        self._RegionId = params.get("RegionId")
        self._AvailablePortType = params.get("AvailablePortType")
        if params.get("Coordinate") is not None:
            self._Coordinate = Coordinate()
            self._Coordinate._deserialize(params.get("Coordinate"))
        self._City = params.get("City")
        self._Area = params.get("Area")
        self._AccessPointType = params.get("AccessPointType")
        if params.get("AvailablePortInfo") is not None:
            self._AvailablePortInfo = []
            for item in params.get("AvailablePortInfo"):
                obj = PortSpecification()
                obj._deserialize(item)
                self._AvailablePortInfo.append(obj)
        self._Address = params.get("Address")
        self._IsMacSec = params.get("IsMacSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressRequest(AbstractModel):
    """ApplyInternetAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaskLen: CIDR地址掩码长度
        :type MaskLen: int
        :param _AddrType: 0:BGP类型地址
1：中国电信
2：中国移动
3：中国联通
        :type AddrType: int
        :param _AddrProto: 0：IPv4
1:IPv6
        :type AddrProto: int
        """
        self._MaskLen = None
        self._AddrType = None
        self._AddrProto = None

    @property
    def MaskLen(self):
        """CIDR地址掩码长度
        :rtype: int
        """
        return self._MaskLen

    @MaskLen.setter
    def MaskLen(self, MaskLen):
        self._MaskLen = MaskLen

    @property
    def AddrType(self):
        """0:BGP类型地址
1：中国电信
2：中国移动
3：中国联通
        :rtype: int
        """
        return self._AddrType

    @AddrType.setter
    def AddrType(self, AddrType):
        self._AddrType = AddrType

    @property
    def AddrProto(self):
        """0：IPv4
1:IPv6
        :rtype: int
        """
        return self._AddrProto

    @AddrProto.setter
    def AddrProto(self, AddrProto):
        self._AddrProto = AddrProto


    def _deserialize(self, params):
        self._MaskLen = params.get("MaskLen")
        self._AddrType = params.get("AddrType")
        self._AddrProto = params.get("AddrProto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressResponse(AbstractModel):
    """ApplyInternetAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 互联网公网地址ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """互联网公网地址ID
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


class BFDInfo(AbstractModel):
    """BFD配置信息

    """

    def __init__(self):
        r"""
        :param _ProbeFailedTimes: 健康检查次数
        :type ProbeFailedTimes: int
        :param _Interval: 健康检查间隔
        :type Interval: int
        """
        self._ProbeFailedTimes = None
        self._Interval = None

    @property
    def ProbeFailedTimes(self):
        """健康检查次数
        :rtype: int
        """
        return self._ProbeFailedTimes

    @ProbeFailedTimes.setter
    def ProbeFailedTimes(self, ProbeFailedTimes):
        self._ProbeFailedTimes = ProbeFailedTimes

    @property
    def Interval(self):
        """健康检查间隔
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._ProbeFailedTimes = params.get("ProbeFailedTimes")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPStatus(AbstractModel):
    """bgp状态信息

    """

    def __init__(self):
        r"""
        :param _TencentAddressBgpState: 腾讯侧主互联IP BGP状态
        :type TencentAddressBgpState: str
        :param _TencentBackupAddressBgpState: 腾讯侧备互联IP BGP状态
        :type TencentBackupAddressBgpState: str
        """
        self._TencentAddressBgpState = None
        self._TencentBackupAddressBgpState = None

    @property
    def TencentAddressBgpState(self):
        """腾讯侧主互联IP BGP状态
        :rtype: str
        """
        return self._TencentAddressBgpState

    @TencentAddressBgpState.setter
    def TencentAddressBgpState(self, TencentAddressBgpState):
        self._TencentAddressBgpState = TencentAddressBgpState

    @property
    def TencentBackupAddressBgpState(self):
        """腾讯侧备互联IP BGP状态
        :rtype: str
        """
        return self._TencentBackupAddressBgpState

    @TencentBackupAddressBgpState.setter
    def TencentBackupAddressBgpState(self, TencentBackupAddressBgpState):
        self._TencentBackupAddressBgpState = TencentBackupAddressBgpState


    def _deserialize(self, params):
        self._TencentAddressBgpState = params.get("TencentAddressBgpState")
        self._TencentBackupAddressBgpState = params.get("TencentBackupAddressBgpState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BgpPeer(AbstractModel):
    """bgp参数，包括CloudAsn，Asn，AuthKey

    """

    def __init__(self):
        r"""
        :param _CloudAsn: 腾讯侧BGP ASN
        :type CloudAsn: int
        :param _Asn: 用户侧BGP ASN
        :type Asn: int
        :param _AuthKey: 用户侧BGP密钥
        :type AuthKey: str
        """
        self._CloudAsn = None
        self._Asn = None
        self._AuthKey = None

    @property
    def CloudAsn(self):
        """腾讯侧BGP ASN
        :rtype: int
        """
        return self._CloudAsn

    @CloudAsn.setter
    def CloudAsn(self, CloudAsn):
        self._CloudAsn = CloudAsn

    @property
    def Asn(self):
        """用户侧BGP ASN
        :rtype: int
        """
        return self._Asn

    @Asn.setter
    def Asn(self, Asn):
        self._Asn = Asn

    @property
    def AuthKey(self):
        """用户侧BGP密钥
        :rtype: str
        """
        return self._AuthKey

    @AuthKey.setter
    def AuthKey(self, AuthKey):
        self._AuthKey = AuthKey


    def _deserialize(self, params):
        self._CloudAsn = params.get("CloudAsn")
        self._Asn = params.get("Asn")
        self._AuthKey = params.get("AuthKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudAttachInfo(AbstractModel):
    """敏捷上云服务信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 敏捷上云实例id
        :type InstanceId: str
        :param _Name: 敏捷上云名称
        :type Name: str
        :param _IapId: 合作伙伴的AppId
        :type IapId: str
        :param _IdcAddress: 需要接入敏捷上云的IDC的地址
        :type IdcAddress: str
        :param _IdcType: 需要接入敏捷上云的IDC的互联网服务提供商类型
        :type IdcType: str
        :param _Bandwidth: 敏捷上云的带宽，单位为MB
        :type Bandwidth: int
        :param _Telephone: 联系电话
        :type Telephone: str
        :param _Status: 敏捷上云的状态
available：就绪状态
applying：申请，待审核状态
pendingpay：代付款状态
building：建设中状态
confirming：待确认状态
isolate: 隔离状态
stoped：终止状态
        :type Status: str
        :param _ApplyTime: 敏捷上云申请的时间
        :type ApplyTime: str
        :param _ReadyTime: 敏捷上云建设完成的时间
        :type ReadyTime: str
        :param _ExpireTime: 敏捷上云过期时间
        :type ExpireTime: str
        :param _Remarks: 备注信息
        :type Remarks: str
        :param _RegionStatus: 敏捷上云的地域状态。
same-region：同地域
cross-region：跨地域
        :type RegionStatus: str
        :param _AppId: 用户的AppId
        :type AppId: str
        :param _Uin: 用户的Uin
        :type Uin: str
        :param _CustomerAuthName: 用户注册名称
        :type CustomerAuthName: str
        :param _DirectConnectId: 物理专线实例ID
        :type DirectConnectId: str
        :param _CloudAttachServiceGatewaysSupport: 敏捷上云是否支持创建高速上云专线网关
        :type CloudAttachServiceGatewaysSupport: bool
        :param _BUpdateBandwidth: 敏捷上云服务是否处于升降配中
        :type BUpdateBandwidth: bool
        :param _ArRegion: 接入地域
        :type ArRegion: str
        """
        self._InstanceId = None
        self._Name = None
        self._IapId = None
        self._IdcAddress = None
        self._IdcType = None
        self._Bandwidth = None
        self._Telephone = None
        self._Status = None
        self._ApplyTime = None
        self._ReadyTime = None
        self._ExpireTime = None
        self._Remarks = None
        self._RegionStatus = None
        self._AppId = None
        self._Uin = None
        self._CustomerAuthName = None
        self._DirectConnectId = None
        self._CloudAttachServiceGatewaysSupport = None
        self._BUpdateBandwidth = None
        self._ArRegion = None

    @property
    def InstanceId(self):
        """敏捷上云实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """敏捷上云名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IapId(self):
        """合作伙伴的AppId
        :rtype: str
        """
        return self._IapId

    @IapId.setter
    def IapId(self, IapId):
        self._IapId = IapId

    @property
    def IdcAddress(self):
        """需要接入敏捷上云的IDC的地址
        :rtype: str
        """
        return self._IdcAddress

    @IdcAddress.setter
    def IdcAddress(self, IdcAddress):
        self._IdcAddress = IdcAddress

    @property
    def IdcType(self):
        """需要接入敏捷上云的IDC的互联网服务提供商类型
        :rtype: str
        """
        return self._IdcType

    @IdcType.setter
    def IdcType(self, IdcType):
        self._IdcType = IdcType

    @property
    def Bandwidth(self):
        """敏捷上云的带宽，单位为MB
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Telephone(self):
        """联系电话
        :rtype: str
        """
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone

    @property
    def Status(self):
        """敏捷上云的状态
available：就绪状态
applying：申请，待审核状态
pendingpay：代付款状态
building：建设中状态
confirming：待确认状态
isolate: 隔离状态
stoped：终止状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApplyTime(self):
        """敏捷上云申请的时间
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def ReadyTime(self):
        """敏捷上云建设完成的时间
        :rtype: str
        """
        return self._ReadyTime

    @ReadyTime.setter
    def ReadyTime(self, ReadyTime):
        self._ReadyTime = ReadyTime

    @property
    def ExpireTime(self):
        """敏捷上云过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Remarks(self):
        """备注信息
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def RegionStatus(self):
        """敏捷上云的地域状态。
same-region：同地域
cross-region：跨地域
        :rtype: str
        """
        return self._RegionStatus

    @RegionStatus.setter
    def RegionStatus(self, RegionStatus):
        self._RegionStatus = RegionStatus

    @property
    def AppId(self):
        """用户的AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        """用户的Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def CustomerAuthName(self):
        """用户注册名称
        :rtype: str
        """
        return self._CustomerAuthName

    @CustomerAuthName.setter
    def CustomerAuthName(self, CustomerAuthName):
        self._CustomerAuthName = CustomerAuthName

    @property
    def DirectConnectId(self):
        """物理专线实例ID
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def CloudAttachServiceGatewaysSupport(self):
        """敏捷上云是否支持创建高速上云专线网关
        :rtype: bool
        """
        return self._CloudAttachServiceGatewaysSupport

    @CloudAttachServiceGatewaysSupport.setter
    def CloudAttachServiceGatewaysSupport(self, CloudAttachServiceGatewaysSupport):
        self._CloudAttachServiceGatewaysSupport = CloudAttachServiceGatewaysSupport

    @property
    def BUpdateBandwidth(self):
        """敏捷上云服务是否处于升降配中
        :rtype: bool
        """
        return self._BUpdateBandwidth

    @BUpdateBandwidth.setter
    def BUpdateBandwidth(self, BUpdateBandwidth):
        self._BUpdateBandwidth = BUpdateBandwidth

    @property
    def ArRegion(self):
        """接入地域
        :rtype: str
        """
        return self._ArRegion

    @ArRegion.setter
    def ArRegion(self, ArRegion):
        self._ArRegion = ArRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._IapId = params.get("IapId")
        self._IdcAddress = params.get("IdcAddress")
        self._IdcType = params.get("IdcType")
        self._Bandwidth = params.get("Bandwidth")
        self._Telephone = params.get("Telephone")
        self._Status = params.get("Status")
        self._ApplyTime = params.get("ApplyTime")
        self._ReadyTime = params.get("ReadyTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Remarks = params.get("Remarks")
        self._RegionStatus = params.get("RegionStatus")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._CustomerAuthName = params.get("CustomerAuthName")
        self._DirectConnectId = params.get("DirectConnectId")
        self._CloudAttachServiceGatewaysSupport = params.get("CloudAttachServiceGatewaysSupport")
        self._BUpdateBandwidth = params.get("BUpdateBandwidth")
        self._ArRegion = params.get("ArRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标，经维度描述

    """

    def __init__(self):
        r"""
        :param _Lat: 纬度
        :type Lat: float
        :param _Lng: 经度
        :type Lng: float
        """
        self._Lat = None
        self._Lng = None

    @property
    def Lat(self):
        """纬度
        :rtype: float
        """
        return self._Lat

    @Lat.setter
    def Lat(self, Lat):
        self._Lat = Lat

    @property
    def Lng(self):
        """经度
        :rtype: float
        """
        return self._Lng

    @Lng.setter
    def Lng(self, Lng):
        self._Lng = Lng


    def _deserialize(self, params):
        self._Lat = params.get("Lat")
        self._Lng = params.get("Lng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCasInput(AbstractModel):
    """创建敏捷上云入参

    """

    def __init__(self):
        r"""
        :param _Name: 敏捷上云名称
        :type Name: str
        :param _IdcAddress: 需要接入敏捷上云的IDC的地址
        :type IdcAddress: str
        :param _IdcType: 需要接入敏捷上云的IDC的互联网服务提供商类型
        :type IdcType: str
        :param _Bandwidth: 敏捷上云的带宽，单位为MB
        :type Bandwidth: int
        :param _Telephone: 联系电话
        :type Telephone: str
        :param _Remarks: 备注信息
        :type Remarks: str
        :param _ArRegion: 接入地域
        :type ArRegion: str
        """
        self._Name = None
        self._IdcAddress = None
        self._IdcType = None
        self._Bandwidth = None
        self._Telephone = None
        self._Remarks = None
        self._ArRegion = None

    @property
    def Name(self):
        """敏捷上云名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdcAddress(self):
        """需要接入敏捷上云的IDC的地址
        :rtype: str
        """
        return self._IdcAddress

    @IdcAddress.setter
    def IdcAddress(self, IdcAddress):
        self._IdcAddress = IdcAddress

    @property
    def IdcType(self):
        """需要接入敏捷上云的IDC的互联网服务提供商类型
        :rtype: str
        """
        return self._IdcType

    @IdcType.setter
    def IdcType(self, IdcType):
        self._IdcType = IdcType

    @property
    def Bandwidth(self):
        """敏捷上云的带宽，单位为MB
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Telephone(self):
        """联系电话
        :rtype: str
        """
        return self._Telephone

    @Telephone.setter
    def Telephone(self, Telephone):
        self._Telephone = Telephone

    @property
    def Remarks(self):
        """备注信息
        :rtype: str
        """
        return self._Remarks

    @Remarks.setter
    def Remarks(self, Remarks):
        self._Remarks = Remarks

    @property
    def ArRegion(self):
        """接入地域
        :rtype: str
        """
        return self._ArRegion

    @ArRegion.setter
    def ArRegion(self, ArRegion):
        self._ArRegion = ArRegion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IdcAddress = params.get("IdcAddress")
        self._IdcType = params.get("IdcType")
        self._Bandwidth = params.get("Bandwidth")
        self._Telephone = params.get("Telephone")
        self._Remarks = params.get("Remarks")
        self._ArRegion = params.get("ArRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudAttachServiceRequest(AbstractModel):
    """CreateCloudAttachService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建敏捷上云入参
        :type Data: :class:`tencentcloud.dc.v20180410.models.CreateCasInput`
        """
        self._Data = None

    @property
    def Data(self):
        """创建敏捷上云入参
        :rtype: :class:`tencentcloud.dc.v20180410.models.CreateCasInput`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CreateCasInput()
            self._Data._deserialize(params.get("Data"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudAttachServiceResponse(AbstractModel):
    """CreateCloudAttachService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudAttach: 敏捷上云服务详情
        :type CloudAttach: :class:`tencentcloud.dc.v20180410.models.CloudAttachInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CloudAttach = None
        self._RequestId = None

    @property
    def CloudAttach(self):
        """敏捷上云服务详情
        :rtype: :class:`tencentcloud.dc.v20180410.models.CloudAttachInfo`
        """
        return self._CloudAttach

    @CloudAttach.setter
    def CloudAttach(self, CloudAttach):
        self._CloudAttach = CloudAttach

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CloudAttach") is not None:
            self._CloudAttach = CloudAttachInfo()
            self._CloudAttach._deserialize(params.get("CloudAttach"))
        self._RequestId = params.get("RequestId")


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectName: 物理专线的名称。
        :type DirectConnectName: str
        :param _AccessPointId: 物理专线所在的接入点。
您可以通过调用[DescribeAccessPoints](https://cloud.tencent.com/document/product/216/34827)接口获取接入点ID。
        :type AccessPointId: str
        :param _LineOperator: 提供接入物理专线的运营商。
ChinaTelecom：中国电信； 
ChinaMobile：中国移动；
ChinaUnicom：中国联通；
 In-houseWiring：楼内线；
ChinaOther：中国其他；
 InternationalOperator：境外其他。
        :type LineOperator: str
        :param _PortType: 物理专线接入端口类型，取值：
100Base-T：百兆电口；
1000Base-T（默认值）：千兆电口；
1000Base-LX：千兆单模光口（10千米）；
10GBase-T：万兆电口；
10GBase-LR（默认值）：万兆单模光口（10千米）。
        :type PortType: str
        :param _CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
        :type CircuitCode: str
        :param _Location: 本地数据中心的地理位置。
        :type Location: str
        :param _Bandwidth: 物理专线接入接口带宽，单位为Mbps，默认值为1000，取值范围为 [2, 10240]。
        :type Bandwidth: int
        :param _RedundantDirectConnectId: 冗余物理专线的ID。
        :type RedundantDirectConnectId: str
        :param _Vlan: 物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
        :type Vlan: int
        :param _TencentAddress: 物理专线调试腾讯侧互联 IP。默认自动分配。
        :type TencentAddress: str
        :param _CustomerAddress: 物理专线调试用户侧互联 IP。默认自动分配。
        :type CustomerAddress: str
        :param _CustomerName: 物理专线申请者姓名。默认从账户体系获取。
        :type CustomerName: str
        :param _CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
        :type CustomerContactMail: str
        :param _CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
        :type CustomerContactNumber: str
        :param _FaultReportContactPerson: 报障联系人。
        :type FaultReportContactPerson: str
        :param _FaultReportContactNumber: 报障联系电话。
        :type FaultReportContactNumber: str
        :param _SignLaw: 物理专线申请者是否签署了用户使用协议。默认已签署。
        :type SignLaw: bool
        :param _Tags: 标签键值对
        :type Tags: list of Tag
        :param _IsMacSec: 是否MACsec需求
        :type IsMacSec: bool
        """
        self._DirectConnectName = None
        self._AccessPointId = None
        self._LineOperator = None
        self._PortType = None
        self._CircuitCode = None
        self._Location = None
        self._Bandwidth = None
        self._RedundantDirectConnectId = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._CustomerName = None
        self._CustomerContactMail = None
        self._CustomerContactNumber = None
        self._FaultReportContactPerson = None
        self._FaultReportContactNumber = None
        self._SignLaw = None
        self._Tags = None
        self._IsMacSec = None

    @property
    def DirectConnectName(self):
        """物理专线的名称。
        :rtype: str
        """
        return self._DirectConnectName

    @DirectConnectName.setter
    def DirectConnectName(self, DirectConnectName):
        self._DirectConnectName = DirectConnectName

    @property
    def AccessPointId(self):
        """物理专线所在的接入点。
您可以通过调用[DescribeAccessPoints](https://cloud.tencent.com/document/product/216/34827)接口获取接入点ID。
        :rtype: str
        """
        return self._AccessPointId

    @AccessPointId.setter
    def AccessPointId(self, AccessPointId):
        self._AccessPointId = AccessPointId

    @property
    def LineOperator(self):
        """提供接入物理专线的运营商。
ChinaTelecom：中国电信； 
ChinaMobile：中国移动；
ChinaUnicom：中国联通；
 In-houseWiring：楼内线；
ChinaOther：中国其他；
 InternationalOperator：境外其他。
        :rtype: str
        """
        return self._LineOperator

    @LineOperator.setter
    def LineOperator(self, LineOperator):
        self._LineOperator = LineOperator

    @property
    def PortType(self):
        """物理专线接入端口类型，取值：
100Base-T：百兆电口；
1000Base-T（默认值）：千兆电口；
1000Base-LX：千兆单模光口（10千米）；
10GBase-T：万兆电口；
10GBase-LR（默认值）：万兆单模光口（10千米）。
        :rtype: str
        """
        return self._PortType

    @PortType.setter
    def PortType(self, PortType):
        self._PortType = PortType

    @property
    def CircuitCode(self):
        """运营商或者服务商为物理专线提供的电路编码。
        :rtype: str
        """
        return self._CircuitCode

    @CircuitCode.setter
    def CircuitCode(self, CircuitCode):
        self._CircuitCode = CircuitCode

    @property
    def Location(self):
        """本地数据中心的地理位置。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Bandwidth(self):
        """物理专线接入接口带宽，单位为Mbps，默认值为1000，取值范围为 [2, 10240]。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def RedundantDirectConnectId(self):
        """冗余物理专线的ID。
        :rtype: str
        """
        return self._RedundantDirectConnectId

    @RedundantDirectConnectId.setter
    def RedundantDirectConnectId(self, RedundantDirectConnectId):
        self._RedundantDirectConnectId = RedundantDirectConnectId

    @property
    def Vlan(self):
        """物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        """物理专线调试腾讯侧互联 IP。默认自动分配。
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        """物理专线调试用户侧互联 IP。默认自动分配。
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def CustomerName(self):
        """物理专线申请者姓名。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerContactMail(self):
        """物理专线申请者联系邮箱。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerContactMail

    @CustomerContactMail.setter
    def CustomerContactMail(self, CustomerContactMail):
        self._CustomerContactMail = CustomerContactMail

    @property
    def CustomerContactNumber(self):
        """物理专线申请者联系号码。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerContactNumber

    @CustomerContactNumber.setter
    def CustomerContactNumber(self, CustomerContactNumber):
        self._CustomerContactNumber = CustomerContactNumber

    @property
    def FaultReportContactPerson(self):
        """报障联系人。
        :rtype: str
        """
        return self._FaultReportContactPerson

    @FaultReportContactPerson.setter
    def FaultReportContactPerson(self, FaultReportContactPerson):
        self._FaultReportContactPerson = FaultReportContactPerson

    @property
    def FaultReportContactNumber(self):
        """报障联系电话。
        :rtype: str
        """
        return self._FaultReportContactNumber

    @FaultReportContactNumber.setter
    def FaultReportContactNumber(self, FaultReportContactNumber):
        self._FaultReportContactNumber = FaultReportContactNumber

    @property
    def SignLaw(self):
        """物理专线申请者是否签署了用户使用协议。默认已签署。
        :rtype: bool
        """
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def Tags(self):
        """标签键值对
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsMacSec(self):
        """是否MACsec需求
        :rtype: bool
        """
        return self._IsMacSec

    @IsMacSec.setter
    def IsMacSec(self, IsMacSec):
        self._IsMacSec = IsMacSec


    def _deserialize(self, params):
        self._DirectConnectName = params.get("DirectConnectName")
        self._AccessPointId = params.get("AccessPointId")
        self._LineOperator = params.get("LineOperator")
        self._PortType = params.get("PortType")
        self._CircuitCode = params.get("CircuitCode")
        self._Location = params.get("Location")
        self._Bandwidth = params.get("Bandwidth")
        self._RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._CustomerName = params.get("CustomerName")
        self._CustomerContactMail = params.get("CustomerContactMail")
        self._CustomerContactNumber = params.get("CustomerContactNumber")
        self._FaultReportContactPerson = params.get("FaultReportContactPerson")
        self._FaultReportContactNumber = params.get("FaultReportContactNumber")
        self._SignLaw = params.get("SignLaw")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsMacSec = params.get("IsMacSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectIdSet: 物理专线的ID。
        :type DirectConnectIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DirectConnectIdSet = None
        self._RequestId = None

    @property
    def DirectConnectIdSet(self):
        """物理专线的ID。
        :rtype: list of str
        """
        return self._DirectConnectIdSet

    @DirectConnectIdSet.setter
    def DirectConnectIdSet(self, DirectConnectIdSet):
        self._DirectConnectIdSet = DirectConnectIdSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DirectConnectIdSet = params.get("DirectConnectIdSet")
        self._RequestId = params.get("RequestId")


class CreateDirectConnectTunnelRequest(AbstractModel):
    """CreateDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: 物理专线ID，例如：dc-kd7d06of。
        :type DirectConnectId: str
        :param _DirectConnectTunnelName: 专用通道名称。
        :type DirectConnectTunnelName: str
        :param _DirectConnectOwnerAccount: 物理专线owner，缺省为当前客户（物理专线 owner）
共享专线时这里需要填写共享专线的开发商账号 ID。
        :type DirectConnectOwnerAccount: str
        :param _NetworkType: 网络类型，枚举：VPC、CCN、NAT；默认为VPC。VPC：私有网络；CCN：云联网；NAT：NAT网络）。
        :type NetworkType: str
        :param _NetworkRegion: 网络地域。
        :type NetworkRegion: str
        :param _VpcId: 私有网络统一ID，在NetworkType为VPC时必填，且与专线网关所属的VPCID一致；NetworkType为其它组网类型时可不填，内部会统一处理。
        :type VpcId: str
        :param _DirectConnectGatewayId: 专线网关ID，例如 dcg-d545ddf。
        :type DirectConnectGatewayId: str
        :param _Bandwidth: 专线带宽，单位：Mbps；默认是物理专线带宽值。
        :type Bandwidth: int
        :param _RouteType: 路由类型，枚举：BGP、STATIC；默认为BGP 。（BGP ：BGP路由；STATIC：静态）。
        :type RouteType: str
        :param _BgpPeer: BgpPeer，用户侧bgp信息，包括Asn和AuthKey。
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: 静态路由，用户IDC的网段地址。
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _Vlan: vlan，范围：0 ~ 3000。
0：不开启子接口，默认值是非0。
        :type Vlan: int
        :param _TencentAddress: TencentAddress，腾讯侧互联 IP。
        :type TencentAddress: str
        :param _CustomerAddress: CustomerAddress，用户侧互联 IP。
        :type CustomerAddress: str
        :param _TencentBackupAddress: TencentBackupAddress，腾讯侧备用互联 IP。
        :type TencentBackupAddress: str
        :param _CloudAttachId: 高速上云服务ID。
        :type CloudAttachId: str
        :param _BfdEnable: 是否开启BFD。
        :type BfdEnable: int
        :param _NqaEnable: 是否开启NQA。
        :type NqaEnable: int
        :param _BfdInfo: BFD配置信息。
        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        :param _NqaInfo: NQA配置信息。
        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        :param _Tags: 标签键值对
        :type Tags: list of Tag
        """
        self._DirectConnectId = None
        self._DirectConnectTunnelName = None
        self._DirectConnectOwnerAccount = None
        self._NetworkType = None
        self._NetworkRegion = None
        self._VpcId = None
        self._DirectConnectGatewayId = None
        self._Bandwidth = None
        self._RouteType = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._TencentBackupAddress = None
        self._CloudAttachId = None
        self._BfdEnable = None
        self._NqaEnable = None
        self._BfdInfo = None
        self._NqaInfo = None
        self._Tags = None

    @property
    def DirectConnectId(self):
        """物理专线ID，例如：dc-kd7d06of。
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def DirectConnectTunnelName(self):
        """专用通道名称。
        :rtype: str
        """
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def DirectConnectOwnerAccount(self):
        """物理专线owner，缺省为当前客户（物理专线 owner）
共享专线时这里需要填写共享专线的开发商账号 ID。
        :rtype: str
        """
        return self._DirectConnectOwnerAccount

    @DirectConnectOwnerAccount.setter
    def DirectConnectOwnerAccount(self, DirectConnectOwnerAccount):
        self._DirectConnectOwnerAccount = DirectConnectOwnerAccount

    @property
    def NetworkType(self):
        """网络类型，枚举：VPC、CCN、NAT；默认为VPC。VPC：私有网络；CCN：云联网；NAT：NAT网络）。
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def NetworkRegion(self):
        """网络地域。
        :rtype: str
        """
        return self._NetworkRegion

    @NetworkRegion.setter
    def NetworkRegion(self, NetworkRegion):
        self._NetworkRegion = NetworkRegion

    @property
    def VpcId(self):
        """私有网络统一ID，在NetworkType为VPC时必填，且与专线网关所属的VPCID一致；NetworkType为其它组网类型时可不填，内部会统一处理。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DirectConnectGatewayId(self):
        """专线网关ID，例如 dcg-d545ddf。
        :rtype: str
        """
        return self._DirectConnectGatewayId

    @DirectConnectGatewayId.setter
    def DirectConnectGatewayId(self, DirectConnectGatewayId):
        self._DirectConnectGatewayId = DirectConnectGatewayId

    @property
    def Bandwidth(self):
        """专线带宽，单位：Mbps；默认是物理专线带宽值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def RouteType(self):
        """路由类型，枚举：BGP、STATIC；默认为BGP 。（BGP ：BGP路由；STATIC：静态）。
        :rtype: str
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def BgpPeer(self):
        """BgpPeer，用户侧bgp信息，包括Asn和AuthKey。
        :rtype: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        """
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        """静态路由，用户IDC的网段地址。
        :rtype: list of RouteFilterPrefix
        """
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def Vlan(self):
        """vlan，范围：0 ~ 3000。
0：不开启子接口，默认值是非0。
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        """TencentAddress，腾讯侧互联 IP。
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        """CustomerAddress，用户侧互联 IP。
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def TencentBackupAddress(self):
        """TencentBackupAddress，腾讯侧备用互联 IP。
        :rtype: str
        """
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress

    @property
    def CloudAttachId(self):
        """高速上云服务ID。
        :rtype: str
        """
        return self._CloudAttachId

    @CloudAttachId.setter
    def CloudAttachId(self, CloudAttachId):
        self._CloudAttachId = CloudAttachId

    @property
    def BfdEnable(self):
        """是否开启BFD。
        :rtype: int
        """
        return self._BfdEnable

    @BfdEnable.setter
    def BfdEnable(self, BfdEnable):
        self._BfdEnable = BfdEnable

    @property
    def NqaEnable(self):
        """是否开启NQA。
        :rtype: int
        """
        return self._NqaEnable

    @NqaEnable.setter
    def NqaEnable(self, NqaEnable):
        self._NqaEnable = NqaEnable

    @property
    def BfdInfo(self):
        """BFD配置信息。
        :rtype: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        """
        return self._BfdInfo

    @BfdInfo.setter
    def BfdInfo(self, BfdInfo):
        self._BfdInfo = BfdInfo

    @property
    def NqaInfo(self):
        """NQA配置信息。
        :rtype: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        """
        return self._NqaInfo

    @NqaInfo.setter
    def NqaInfo(self, NqaInfo):
        self._NqaInfo = NqaInfo

    @property
    def Tags(self):
        """标签键值对
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self._DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self._NetworkType = params.get("NetworkType")
        self._NetworkRegion = params.get("NetworkRegion")
        self._VpcId = params.get("VpcId")
        self._DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self._Bandwidth = params.get("Bandwidth")
        self._RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        self._CloudAttachId = params.get("CloudAttachId")
        self._BfdEnable = params.get("BfdEnable")
        self._NqaEnable = params.get("NqaEnable")
        if params.get("BfdInfo") is not None:
            self._BfdInfo = BFDInfo()
            self._BfdInfo._deserialize(params.get("BfdInfo"))
        if params.get("NqaInfo") is not None:
            self._NqaInfo = NQAInfo()
            self._NqaInfo._deserialize(params.get("NqaInfo"))
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
        


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelIdSet: 专用通道ID。
        :type DirectConnectTunnelIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DirectConnectTunnelIdSet = None
        self._RequestId = None

    @property
    def DirectConnectTunnelIdSet(self):
        """专用通道ID。
        :rtype: list of str
        """
        return self._DirectConnectTunnelIdSet

    @DirectConnectTunnelIdSet.setter
    def DirectConnectTunnelIdSet(self, DirectConnectTunnelIdSet):
        self._DirectConnectTunnelIdSet = DirectConnectTunnelIdSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DirectConnectTunnelIdSet = params.get("DirectConnectTunnelIdSet")
        self._RequestId = params.get("RequestId")


class DeleteDirectConnectRequest(AbstractModel):
    """DeleteDirectConnect请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: 物理专线的ID。
        :type DirectConnectId: str
        """
        self._DirectConnectId = None

    @property
    def DirectConnectId(self):
        """物理专线的ID。
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect返回参数结构体

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


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel返回参数结构体

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


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionId: 接入点所在的地域。你可以通过调用[DescribeRegions](https://cloud.tencent.com/document/product/1596/77930)接口获取地域ID。
        :type RegionId: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Filters: 过滤参数，支持：access-point-id、isp
        :type Filters: list of Filter
        """
        self._RegionId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def RegionId(self):
        """接入点所在的地域。你可以通过调用[DescribeRegions](https://cloud.tencent.com/document/product/1596/77930)接口获取地域ID。
        :rtype: str
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

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
        """过滤参数，支持：access-point-id、isp
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
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
        


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessPointSet: 接入点信息。
        :type AccessPointSet: list of AccessPoint
        :param _TotalCount: 接入点总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccessPointSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AccessPointSet(self):
        """接入点信息。
        :rtype: list of AccessPoint
        """
        return self._AccessPointSet

    @AccessPointSet.setter
    def AccessPointSet(self, AccessPointSet):
        self._AccessPointSet = AccessPointSet

    @property
    def TotalCount(self):
        """接入点总数量。
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
        if params.get("AccessPointSet") is not None:
            self._AccessPointSet = []
            for item in params.get("AccessPointSet"):
                obj = AccessPoint()
                obj._deserialize(item)
                self._AccessPointSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelExtraRequest(AbstractModel):
    """DescribeDirectConnectTunnelExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectTunnelExtraResponse(AbstractModel):
    """DescribeDirectConnectTunnelExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelExtra: 专用通道扩展信息。
        :type DirectConnectTunnelExtra: :class:`tencentcloud.dc.v20180410.models.DirectConnectTunnelExtra`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DirectConnectTunnelExtra = None
        self._RequestId = None

    @property
    def DirectConnectTunnelExtra(self):
        """专用通道扩展信息。
        :rtype: :class:`tencentcloud.dc.v20180410.models.DirectConnectTunnelExtra`
        """
        return self._DirectConnectTunnelExtra

    @DirectConnectTunnelExtra.setter
    def DirectConnectTunnelExtra(self, DirectConnectTunnelExtra):
        self._DirectConnectTunnelExtra = DirectConnectTunnelExtra

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DirectConnectTunnelExtra") is not None:
            self._DirectConnectTunnelExtra = DirectConnectTunnelExtra()
            self._DirectConnectTunnelExtra._deserialize(params.get("DirectConnectTunnelExtra"))
        self._RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelsRequest(AbstractModel):
    """DescribeDirectConnectTunnels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件:
参数不支持同时指定DirectConnectTunnelIds和Filters。
direct-connect-tunnel-name, 专用通道名称。
direct-connect-tunnel-id, 专用通道实例ID，如：dcx-abcdefgh。
direct-connect-id, 物理专线实例ID，如：dc-abcdefgh。
        :type Filters: list of Filter
        :param _DirectConnectTunnelIds: 专用通道ID数组。
        :type DirectConnectTunnelIds: list of str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._Filters = None
        self._DirectConnectTunnelIds = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """过滤条件:
参数不支持同时指定DirectConnectTunnelIds和Filters。
direct-connect-tunnel-name, 专用通道名称。
direct-connect-tunnel-id, 专用通道实例ID，如：dcx-abcdefgh。
direct-connect-id, 物理专线实例ID，如：dc-abcdefgh。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DirectConnectTunnelIds(self):
        """专用通道ID数组。
        :rtype: list of str
        """
        return self._DirectConnectTunnelIds

    @DirectConnectTunnelIds.setter
    def DirectConnectTunnelIds(self, DirectConnectTunnelIds):
        self._DirectConnectTunnelIds = DirectConnectTunnelIds

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DirectConnectTunnelIds = params.get("DirectConnectTunnelIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelSet: 专用通道列表。
        :type DirectConnectTunnelSet: list of DirectConnectTunnel
        :param _TotalCount: 专用通道总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DirectConnectTunnelSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DirectConnectTunnelSet(self):
        """专用通道列表。
        :rtype: list of DirectConnectTunnel
        """
        return self._DirectConnectTunnelSet

    @DirectConnectTunnelSet.setter
    def DirectConnectTunnelSet(self, DirectConnectTunnelSet):
        self._DirectConnectTunnelSet = DirectConnectTunnelSet

    @property
    def TotalCount(self):
        """专用通道总数量。
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
        if params.get("DirectConnectTunnelSet") is not None:
            self._DirectConnectTunnelSet = []
            for item in params.get("DirectConnectTunnelSet"):
                obj = DirectConnectTunnel()
                obj._deserialize(item)
                self._DirectConnectTunnelSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDirectConnectsRequest(AbstractModel):
    """DescribeDirectConnects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件。direct-connect-id：物理专线ID，states：物理专线状态（AVAILABLE-就绪，PENDING-申请中，REJECTED-申请被拒绝，PENDINGPAY-待付款，PAID-付款完成，BUILDING-建设中，STOPED-建设终止，DELETED-删除完成）。
        :type Filters: list of Filter
        :param _DirectConnectIds: 物理专线 ID数组。
        :type DirectConnectIds: list of str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._Filters = None
        self._DirectConnectIds = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        """过滤条件。direct-connect-id：物理专线ID，states：物理专线状态（AVAILABLE-就绪，PENDING-申请中，REJECTED-申请被拒绝，PENDINGPAY-待付款，PAID-付款完成，BUILDING-建设中，STOPED-建设终止，DELETED-删除完成）。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def DirectConnectIds(self):
        """物理专线 ID数组。
        :rtype: list of str
        """
        return self._DirectConnectIds

    @DirectConnectIds.setter
    def DirectConnectIds(self, DirectConnectIds):
        self._DirectConnectIds = DirectConnectIds

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
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._DirectConnectIds = params.get("DirectConnectIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectSet: 物理专线列表。
        :type DirectConnectSet: list of DirectConnect
        :param _TotalCount: 符合物理专线列表数量。
        :type TotalCount: int
        :param _AllSignLaw: 用户名下物理专线是否都签署了用户协议。
        :type AllSignLaw: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DirectConnectSet = None
        self._TotalCount = None
        self._AllSignLaw = None
        self._RequestId = None

    @property
    def DirectConnectSet(self):
        """物理专线列表。
        :rtype: list of DirectConnect
        """
        return self._DirectConnectSet

    @DirectConnectSet.setter
    def DirectConnectSet(self, DirectConnectSet):
        self._DirectConnectSet = DirectConnectSet

    @property
    def TotalCount(self):
        """符合物理专线列表数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AllSignLaw(self):
        """用户名下物理专线是否都签署了用户协议。
        :rtype: bool
        """
        return self._AllSignLaw

    @AllSignLaw.setter
    def AllSignLaw(self, AllSignLaw):
        self._AllSignLaw = AllSignLaw

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DirectConnectSet") is not None:
            self._DirectConnectSet = []
            for item in params.get("DirectConnectSet"):
                obj = DirectConnect()
                obj._deserialize(item)
                self._DirectConnectSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AllSignLaw = params.get("AllSignLaw")
        self._RequestId = params.get("RequestId")


class DescribeInternetAddressQuotaRequest(AbstractModel):
    """DescribeInternetAddressQuota请求参数结构体

    """


class DescribeInternetAddressQuotaResponse(AbstractModel):
    """DescribeInternetAddressQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ipv6PrefixLen: IPv6互联网公网允许的最小前缀长度
        :type Ipv6PrefixLen: int
        :param _Ipv4BgpQuota: BGP类型IPv4互联网地址配额
        :type Ipv4BgpQuota: int
        :param _Ipv4OtherQuota: 非BGP类型IPv4互联网地址配额
        :type Ipv4OtherQuota: int
        :param _Ipv4BgpNum: BGP类型IPv4互联网地址已使用数量
        :type Ipv4BgpNum: int
        :param _Ipv4OtherNum: 非BGP类型互联网地址已使用数量
        :type Ipv4OtherNum: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ipv6PrefixLen = None
        self._Ipv4BgpQuota = None
        self._Ipv4OtherQuota = None
        self._Ipv4BgpNum = None
        self._Ipv4OtherNum = None
        self._RequestId = None

    @property
    def Ipv6PrefixLen(self):
        """IPv6互联网公网允许的最小前缀长度
        :rtype: int
        """
        return self._Ipv6PrefixLen

    @Ipv6PrefixLen.setter
    def Ipv6PrefixLen(self, Ipv6PrefixLen):
        self._Ipv6PrefixLen = Ipv6PrefixLen

    @property
    def Ipv4BgpQuota(self):
        """BGP类型IPv4互联网地址配额
        :rtype: int
        """
        return self._Ipv4BgpQuota

    @Ipv4BgpQuota.setter
    def Ipv4BgpQuota(self, Ipv4BgpQuota):
        self._Ipv4BgpQuota = Ipv4BgpQuota

    @property
    def Ipv4OtherQuota(self):
        """非BGP类型IPv4互联网地址配额
        :rtype: int
        """
        return self._Ipv4OtherQuota

    @Ipv4OtherQuota.setter
    def Ipv4OtherQuota(self, Ipv4OtherQuota):
        self._Ipv4OtherQuota = Ipv4OtherQuota

    @property
    def Ipv4BgpNum(self):
        """BGP类型IPv4互联网地址已使用数量
        :rtype: int
        """
        return self._Ipv4BgpNum

    @Ipv4BgpNum.setter
    def Ipv4BgpNum(self, Ipv4BgpNum):
        self._Ipv4BgpNum = Ipv4BgpNum

    @property
    def Ipv4OtherNum(self):
        """非BGP类型互联网地址已使用数量
        :rtype: int
        """
        return self._Ipv4OtherNum

    @Ipv4OtherNum.setter
    def Ipv4OtherNum(self, Ipv4OtherNum):
        self._Ipv4OtherNum = Ipv4OtherNum

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Ipv6PrefixLen = params.get("Ipv6PrefixLen")
        self._Ipv4BgpQuota = params.get("Ipv4BgpQuota")
        self._Ipv4OtherQuota = params.get("Ipv4OtherQuota")
        self._Ipv4BgpNum = params.get("Ipv4BgpNum")
        self._Ipv4OtherNum = params.get("Ipv4OtherNum")
        self._RequestId = params.get("RequestId")


class DescribeInternetAddressRequest(AbstractModel):
    """DescribeInternetAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值100
        :type Limit: int
        :param _Filters: 过滤条件： <li>AddrType，地址类型。0：BGP 1；1: 电信；2：移动；3：联通</li> <li>AddrProto，地址类型。0：IPv4；1:IPv6</li> <li>Status，地址状态。 0：使用中；1：已停用； 2：已退还</li> <li>Subnet，互联网公网地址。数组</li> <li>InstanceIds，互联网公网地址ID。数组</li>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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
        """返回数量，默认为20，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """过滤条件： <li>AddrType，地址类型。0：BGP 1；1: 电信；2：移动；3：联通</li> <li>AddrProto，地址类型。0：IPv4；1:IPv6</li> <li>Status，地址状态。 0：使用中；1：已停用； 2：已退还</li> <li>Subnet，互联网公网地址。数组</li> <li>InstanceIds，互联网公网地址ID。数组</li>
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
        


class DescribeInternetAddressResponse(AbstractModel):
    """DescribeInternetAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 互联网公网地址数量
        :type TotalCount: int
        :param _Subnets: 互联网公网地址列表
        :type Subnets: list of InternetAddressDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Subnets = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """互联网公网地址数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Subnets(self):
        """互联网公网地址列表
        :rtype: list of InternetAddressDetail
        """
        return self._Subnets

    @Subnets.setter
    def Subnets(self, Subnets):
        self._Subnets = Subnets

    @property
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
        if params.get("Subnets") is not None:
            self._Subnets = []
            for item in params.get("Subnets"):
                obj = InternetAddressDetail()
                obj._deserialize(item)
                self._Subnets.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInternetAddressStatisticsRequest(AbstractModel):
    """DescribeInternetAddressStatistics请求参数结构体

    """


class DescribeInternetAddressStatisticsResponse(AbstractModel):
    """DescribeInternetAddressStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 互联网公网地址统计信息数量
        :type TotalCount: int
        :param _InternetAddressStatistics: 互联网公网地址统计信息列表
        :type InternetAddressStatistics: list of InternetAddressStatistics
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InternetAddressStatistics = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """互联网公网地址统计信息数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InternetAddressStatistics(self):
        """互联网公网地址统计信息列表
        :rtype: list of InternetAddressStatistics
        """
        return self._InternetAddressStatistics

    @InternetAddressStatistics.setter
    def InternetAddressStatistics(self, InternetAddressStatistics):
        self._InternetAddressStatistics = InternetAddressStatistics

    @property
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
        if params.get("InternetAddressStatistics") is not None:
            self._InternetAddressStatistics = []
            for item in params.get("InternetAddressStatistics"):
                obj = InternetAddressStatistics()
                obj._deserialize(item)
                self._InternetAddressStatistics.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePublicDirectConnectTunnelRoutesRequest(AbstractModel):
    """DescribePublicDirectConnectTunnelRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。
        :type DirectConnectTunnelId: str
        :param _Filters: 过滤条件：
route-type：路由类型，取值：BGP/STATIC；
route-subnet：路由cidr，取值如：192.68.1.0/24。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._DirectConnectTunnelId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def Filters(self):
        """过滤条件：
route-type：路由类型，取值：BGP/STATIC；
route-subnet：路由cidr，取值如：192.68.1.0/24。
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
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
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
        


class DescribePublicDirectConnectTunnelRoutesResponse(AbstractModel):
    """DescribePublicDirectConnectTunnelRoutes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Routes: 互联网通道路由列表。
        :type Routes: list of DirectConnectTunnelRoute
        :param _TotalCount: 路由总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Routes = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Routes(self):
        """互联网通道路由列表。
        :rtype: list of DirectConnectTunnelRoute
        """
        return self._Routes

    @Routes.setter
    def Routes(self, Routes):
        self._Routes = Routes

    @property
    def TotalCount(self):
        """路由总数量。
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
        if params.get("Routes") is not None:
            self._Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectTunnelRoute()
                obj._deserialize(item)
                self._Routes.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DirectConnect(AbstractModel):
    """物理专线信息列表

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: 物理专线ID。
        :type DirectConnectId: str
        :param _DirectConnectName: 物理专线的名称。
        :type DirectConnectName: str
        :param _AccessPointId: 物理专线的接入点ID。
        :type AccessPointId: str
        :param _State: 物理专线的状态。
申请中：PENDING 
申请驳回：REJECTED   
待付款：TOPAY 
已付款：PAID 
建设中：ALLOCATED   
已开通：AVAILABLE  
删除中 ：DELETING
已删除：DELETED 。
        :type State: str
        :param _CreatedTime: 物理专线创建时间。
        :type CreatedTime: str
        :param _EnabledTime: 物理专线的开通时间。
        :type EnabledTime: str
        :param _LineOperator: 提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。
        :type LineOperator: str
        :param _Location: 本地数据中心的地理位置。
        :type Location: str
        :param _Bandwidth: 物理专线接入接口带宽，单位为Mbps。
        :type Bandwidth: int
        :param _PortType: 用户侧物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）
        :type PortType: str
        :param _CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
        :type CircuitCode: str
        :param _RedundantDirectConnectId: 冗余物理专线的ID。
        :type RedundantDirectConnectId: str
        :param _Vlan: 物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
        :type Vlan: int
        :param _TencentAddress: 物理专线调试腾讯侧互联IP。
        :type TencentAddress: str
        :param _CustomerAddress: 物理专线调试用户侧互联IP。
        :type CustomerAddress: str
        :param _CustomerName: 物理专线申请者姓名。默认从账户体系获取。
        :type CustomerName: str
        :param _CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
        :type CustomerContactMail: str
        :param _CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
        :type CustomerContactNumber: str
        :param _ExpiredTime: 物理专线的过期时间。
        :type ExpiredTime: str
        :param _ChargeType: 物理专线计费类型。 NON_RECURRING_CHARGE：一次性接入费用；PREPAID_BY_YEAR：按年预付费。
        :type ChargeType: str
        :param _FaultReportContactPerson: 报障联系人。
        :type FaultReportContactPerson: str
        :param _FaultReportContactNumber: 报障联系电话。
        :type FaultReportContactNumber: str
        :param _TagSet: 标签键值对
        :type TagSet: list of Tag
        :param _AccessPointType: 物理专线的接入点类型。
        :type AccessPointType: str
        :param _IdcCity: IDC所在城市
        :type IdcCity: str
        :param _ChargeState: 计费状态
        :type ChargeState: str
        :param _StartTime: 物理专线开通时间
        :type StartTime: str
        :param _SignLaw: 物理专线是否已签署用户协议
        :type SignLaw: bool
        :param _LocalZone: 物理专线是否为LocalZone
        :type LocalZone: bool
        :param _VlanZeroDirectConnectTunnelCount: 该物理专线下vlan 0的专用通道数量
        :type VlanZeroDirectConnectTunnelCount: int
        :param _OtherVlanDirectConnectTunnelCount: 该物理专线下非vlan 0的专用通道数量
        :type OtherVlanDirectConnectTunnelCount: int
        :param _MinBandwidth: 物理专线最小带宽
        :type MinBandwidth: int
        :param _Construct: 建设模式
        :type Construct: int
        :param _AccessPointName: 物理专线的接入点名称
        :type AccessPointName: str
        :param _IsThreeArch: 是否三层架构
        :type IsThreeArch: bool
        :param _IsMacSec: 是否MACsec
        :type IsMacSec: bool
        :param _PortSpecification: 端口规格(Mbps)
        :type PortSpecification: int
        """
        self._DirectConnectId = None
        self._DirectConnectName = None
        self._AccessPointId = None
        self._State = None
        self._CreatedTime = None
        self._EnabledTime = None
        self._LineOperator = None
        self._Location = None
        self._Bandwidth = None
        self._PortType = None
        self._CircuitCode = None
        self._RedundantDirectConnectId = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._CustomerName = None
        self._CustomerContactMail = None
        self._CustomerContactNumber = None
        self._ExpiredTime = None
        self._ChargeType = None
        self._FaultReportContactPerson = None
        self._FaultReportContactNumber = None
        self._TagSet = None
        self._AccessPointType = None
        self._IdcCity = None
        self._ChargeState = None
        self._StartTime = None
        self._SignLaw = None
        self._LocalZone = None
        self._VlanZeroDirectConnectTunnelCount = None
        self._OtherVlanDirectConnectTunnelCount = None
        self._MinBandwidth = None
        self._Construct = None
        self._AccessPointName = None
        self._IsThreeArch = None
        self._IsMacSec = None
        self._PortSpecification = None

    @property
    def DirectConnectId(self):
        """物理专线ID。
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def DirectConnectName(self):
        """物理专线的名称。
        :rtype: str
        """
        return self._DirectConnectName

    @DirectConnectName.setter
    def DirectConnectName(self, DirectConnectName):
        self._DirectConnectName = DirectConnectName

    @property
    def AccessPointId(self):
        """物理专线的接入点ID。
        :rtype: str
        """
        return self._AccessPointId

    @AccessPointId.setter
    def AccessPointId(self, AccessPointId):
        self._AccessPointId = AccessPointId

    @property
    def State(self):
        """物理专线的状态。
申请中：PENDING 
申请驳回：REJECTED   
待付款：TOPAY 
已付款：PAID 
建设中：ALLOCATED   
已开通：AVAILABLE  
删除中 ：DELETING
已删除：DELETED 。
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def CreatedTime(self):
        """物理专线创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def EnabledTime(self):
        """物理专线的开通时间。
        :rtype: str
        """
        return self._EnabledTime

    @EnabledTime.setter
    def EnabledTime(self, EnabledTime):
        self._EnabledTime = EnabledTime

    @property
    def LineOperator(self):
        """提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。
        :rtype: str
        """
        return self._LineOperator

    @LineOperator.setter
    def LineOperator(self, LineOperator):
        self._LineOperator = LineOperator

    @property
    def Location(self):
        """本地数据中心的地理位置。
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def Bandwidth(self):
        """物理专线接入接口带宽，单位为Mbps。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def PortType(self):
        """用户侧物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）
        :rtype: str
        """
        return self._PortType

    @PortType.setter
    def PortType(self, PortType):
        self._PortType = PortType

    @property
    def CircuitCode(self):
        """运营商或者服务商为物理专线提供的电路编码。
        :rtype: str
        """
        return self._CircuitCode

    @CircuitCode.setter
    def CircuitCode(self, CircuitCode):
        self._CircuitCode = CircuitCode

    @property
    def RedundantDirectConnectId(self):
        """冗余物理专线的ID。
        :rtype: str
        """
        return self._RedundantDirectConnectId

    @RedundantDirectConnectId.setter
    def RedundantDirectConnectId(self, RedundantDirectConnectId):
        self._RedundantDirectConnectId = RedundantDirectConnectId

    @property
    def Vlan(self):
        """物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        """物理专线调试腾讯侧互联IP。
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        """物理专线调试用户侧互联IP。
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def CustomerName(self):
        """物理专线申请者姓名。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerContactMail(self):
        """物理专线申请者联系邮箱。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerContactMail

    @CustomerContactMail.setter
    def CustomerContactMail(self, CustomerContactMail):
        self._CustomerContactMail = CustomerContactMail

    @property
    def CustomerContactNumber(self):
        """物理专线申请者联系号码。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerContactNumber

    @CustomerContactNumber.setter
    def CustomerContactNumber(self, CustomerContactNumber):
        self._CustomerContactNumber = CustomerContactNumber

    @property
    def ExpiredTime(self):
        """物理专线的过期时间。
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def ChargeType(self):
        """物理专线计费类型。 NON_RECURRING_CHARGE：一次性接入费用；PREPAID_BY_YEAR：按年预付费。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def FaultReportContactPerson(self):
        """报障联系人。
        :rtype: str
        """
        return self._FaultReportContactPerson

    @FaultReportContactPerson.setter
    def FaultReportContactPerson(self, FaultReportContactPerson):
        self._FaultReportContactPerson = FaultReportContactPerson

    @property
    def FaultReportContactNumber(self):
        """报障联系电话。
        :rtype: str
        """
        return self._FaultReportContactNumber

    @FaultReportContactNumber.setter
    def FaultReportContactNumber(self, FaultReportContactNumber):
        self._FaultReportContactNumber = FaultReportContactNumber

    @property
    def TagSet(self):
        """标签键值对
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def AccessPointType(self):
        """物理专线的接入点类型。
        :rtype: str
        """
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType

    @property
    def IdcCity(self):
        """IDC所在城市
        :rtype: str
        """
        return self._IdcCity

    @IdcCity.setter
    def IdcCity(self, IdcCity):
        self._IdcCity = IdcCity

    @property
    def ChargeState(self):
        """计费状态
        :rtype: str
        """
        return self._ChargeState

    @ChargeState.setter
    def ChargeState(self, ChargeState):
        self._ChargeState = ChargeState

    @property
    def StartTime(self):
        """物理专线开通时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def SignLaw(self):
        """物理专线是否已签署用户协议
        :rtype: bool
        """
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def LocalZone(self):
        """物理专线是否为LocalZone
        :rtype: bool
        """
        return self._LocalZone

    @LocalZone.setter
    def LocalZone(self, LocalZone):
        self._LocalZone = LocalZone

    @property
    def VlanZeroDirectConnectTunnelCount(self):
        """该物理专线下vlan 0的专用通道数量
        :rtype: int
        """
        return self._VlanZeroDirectConnectTunnelCount

    @VlanZeroDirectConnectTunnelCount.setter
    def VlanZeroDirectConnectTunnelCount(self, VlanZeroDirectConnectTunnelCount):
        self._VlanZeroDirectConnectTunnelCount = VlanZeroDirectConnectTunnelCount

    @property
    def OtherVlanDirectConnectTunnelCount(self):
        """该物理专线下非vlan 0的专用通道数量
        :rtype: int
        """
        return self._OtherVlanDirectConnectTunnelCount

    @OtherVlanDirectConnectTunnelCount.setter
    def OtherVlanDirectConnectTunnelCount(self, OtherVlanDirectConnectTunnelCount):
        self._OtherVlanDirectConnectTunnelCount = OtherVlanDirectConnectTunnelCount

    @property
    def MinBandwidth(self):
        """物理专线最小带宽
        :rtype: int
        """
        return self._MinBandwidth

    @MinBandwidth.setter
    def MinBandwidth(self, MinBandwidth):
        self._MinBandwidth = MinBandwidth

    @property
    def Construct(self):
        """建设模式
        :rtype: int
        """
        return self._Construct

    @Construct.setter
    def Construct(self, Construct):
        self._Construct = Construct

    @property
    def AccessPointName(self):
        """物理专线的接入点名称
        :rtype: str
        """
        return self._AccessPointName

    @AccessPointName.setter
    def AccessPointName(self, AccessPointName):
        self._AccessPointName = AccessPointName

    @property
    def IsThreeArch(self):
        """是否三层架构
        :rtype: bool
        """
        return self._IsThreeArch

    @IsThreeArch.setter
    def IsThreeArch(self, IsThreeArch):
        self._IsThreeArch = IsThreeArch

    @property
    def IsMacSec(self):
        """是否MACsec
        :rtype: bool
        """
        return self._IsMacSec

    @IsMacSec.setter
    def IsMacSec(self, IsMacSec):
        self._IsMacSec = IsMacSec

    @property
    def PortSpecification(self):
        """端口规格(Mbps)
        :rtype: int
        """
        return self._PortSpecification

    @PortSpecification.setter
    def PortSpecification(self, PortSpecification):
        self._PortSpecification = PortSpecification


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        self._DirectConnectName = params.get("DirectConnectName")
        self._AccessPointId = params.get("AccessPointId")
        self._State = params.get("State")
        self._CreatedTime = params.get("CreatedTime")
        self._EnabledTime = params.get("EnabledTime")
        self._LineOperator = params.get("LineOperator")
        self._Location = params.get("Location")
        self._Bandwidth = params.get("Bandwidth")
        self._PortType = params.get("PortType")
        self._CircuitCode = params.get("CircuitCode")
        self._RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._CustomerName = params.get("CustomerName")
        self._CustomerContactMail = params.get("CustomerContactMail")
        self._CustomerContactNumber = params.get("CustomerContactNumber")
        self._ExpiredTime = params.get("ExpiredTime")
        self._ChargeType = params.get("ChargeType")
        self._FaultReportContactPerson = params.get("FaultReportContactPerson")
        self._FaultReportContactNumber = params.get("FaultReportContactNumber")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._AccessPointType = params.get("AccessPointType")
        self._IdcCity = params.get("IdcCity")
        self._ChargeState = params.get("ChargeState")
        self._StartTime = params.get("StartTime")
        self._SignLaw = params.get("SignLaw")
        self._LocalZone = params.get("LocalZone")
        self._VlanZeroDirectConnectTunnelCount = params.get("VlanZeroDirectConnectTunnelCount")
        self._OtherVlanDirectConnectTunnelCount = params.get("OtherVlanDirectConnectTunnelCount")
        self._MinBandwidth = params.get("MinBandwidth")
        self._Construct = params.get("Construct")
        self._AccessPointName = params.get("AccessPointName")
        self._IsThreeArch = params.get("IsThreeArch")
        self._IsMacSec = params.get("IsMacSec")
        self._PortSpecification = params.get("PortSpecification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnel(AbstractModel):
    """专用通道信息列表

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param _DirectConnectId: 物理专线ID
        :type DirectConnectId: str
        :param _State: 专用通道状态
AVAILABLE:就绪或者已连接
PENDING:申请中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒绝
        :type State: str
        :param _DirectConnectOwnerAccount: 物理专线的拥有者，开发商账号 ID
        :type DirectConnectOwnerAccount: str
        :param _OwnerAccount: 专用通道的拥有者，开发商账号 ID
        :type OwnerAccount: str
        :param _NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :type NetworkType: str
        :param _NetworkRegion: VPC地域对应的网络名，如ap-guangzhou
        :type NetworkRegion: str
        :param _VpcId: 私有网络统一 ID 或者黑石网络统一 ID
        :type VpcId: str
        :param _DirectConnectGatewayId: 专线网关 ID
        :type DirectConnectGatewayId: str
        :param _RouteType: BGP ：BGP路由 STATIC：静态 默认为 BGP 路由
        :type RouteType: str
        :param _BgpPeer: 用户侧BGP，包括： CloudAsn，Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: 用户侧网段地址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _Vlan: 专用通道的Vlan
        :type Vlan: int
        :param _TencentAddress: TencentAddress，腾讯侧互联 IP
        :type TencentAddress: str
        :param _CustomerAddress: CustomerAddress，用户侧互联 IP
        :type CustomerAddress: str
        :param _DirectConnectTunnelName: 专用通道名称
        :type DirectConnectTunnelName: str
        :param _CreatedTime: 专用通道创建时间
        :type CreatedTime: str
        :param _Bandwidth: 专用通道带宽值
        :type Bandwidth: int
        :param _TagSet: 专用通道标签值
        :type TagSet: list of Tag
        :param _NetDetectId: 关联的网络自定义探测ID
        :type NetDetectId: str
        :param _EnableBGPCommunity: BGP community开关
        :type EnableBGPCommunity: bool
        :param _NatType: 是否为Nat通道
        :type NatType: int
        :param _VpcRegion: VPC地域简码，如gz、cd
        :type VpcRegion: str
        :param _BfdEnable: 是否开启BFD
        :type BfdEnable: int
        :param _AccessPointType: 专用通道接入点类型
        :type AccessPointType: str
        :param _DirectConnectGatewayName: 专线网关名称
        :type DirectConnectGatewayName: str
        :param _VpcName: VPC名称
        :type VpcName: str
        :param _TencentBackupAddress: TencentBackupAddress，腾讯侧备用互联 IP
        :type TencentBackupAddress: str
        :param _SignLaw: 专用通道关联的物理专线是否签署了用户协议
        :type SignLaw: bool
        :param _CloudAttachId: 高速上云服务ID
        :type CloudAttachId: str
        :param _ShareOrNot: 是否共享通道
        :type ShareOrNot: int
        """
        self._DirectConnectTunnelId = None
        self._DirectConnectId = None
        self._State = None
        self._DirectConnectOwnerAccount = None
        self._OwnerAccount = None
        self._NetworkType = None
        self._NetworkRegion = None
        self._VpcId = None
        self._DirectConnectGatewayId = None
        self._RouteType = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._DirectConnectTunnelName = None
        self._CreatedTime = None
        self._Bandwidth = None
        self._TagSet = None
        self._NetDetectId = None
        self._EnableBGPCommunity = None
        self._NatType = None
        self._VpcRegion = None
        self._BfdEnable = None
        self._AccessPointType = None
        self._DirectConnectGatewayName = None
        self._VpcName = None
        self._TencentBackupAddress = None
        self._SignLaw = None
        self._CloudAttachId = None
        self._ShareOrNot = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def DirectConnectId(self):
        """物理专线ID
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def State(self):
        """专用通道状态
AVAILABLE:就绪或者已连接
PENDING:申请中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒绝
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DirectConnectOwnerAccount(self):
        """物理专线的拥有者，开发商账号 ID
        :rtype: str
        """
        return self._DirectConnectOwnerAccount

    @DirectConnectOwnerAccount.setter
    def DirectConnectOwnerAccount(self, DirectConnectOwnerAccount):
        self._DirectConnectOwnerAccount = DirectConnectOwnerAccount

    @property
    def OwnerAccount(self):
        """专用通道的拥有者，开发商账号 ID
        :rtype: str
        """
        return self._OwnerAccount

    @OwnerAccount.setter
    def OwnerAccount(self, OwnerAccount):
        self._OwnerAccount = OwnerAccount

    @property
    def NetworkType(self):
        """网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def NetworkRegion(self):
        """VPC地域对应的网络名，如ap-guangzhou
        :rtype: str
        """
        return self._NetworkRegion

    @NetworkRegion.setter
    def NetworkRegion(self, NetworkRegion):
        self._NetworkRegion = NetworkRegion

    @property
    def VpcId(self):
        """私有网络统一 ID 或者黑石网络统一 ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DirectConnectGatewayId(self):
        """专线网关 ID
        :rtype: str
        """
        return self._DirectConnectGatewayId

    @DirectConnectGatewayId.setter
    def DirectConnectGatewayId(self, DirectConnectGatewayId):
        self._DirectConnectGatewayId = DirectConnectGatewayId

    @property
    def RouteType(self):
        """BGP ：BGP路由 STATIC：静态 默认为 BGP 路由
        :rtype: str
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def BgpPeer(self):
        """用户侧BGP，包括： CloudAsn，Asn，AuthKey
        :rtype: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        """
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        """用户侧网段地址
        :rtype: list of RouteFilterPrefix
        """
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def Vlan(self):
        """专用通道的Vlan
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        """TencentAddress，腾讯侧互联 IP
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        """CustomerAddress，用户侧互联 IP
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def DirectConnectTunnelName(self):
        """专用通道名称
        :rtype: str
        """
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def CreatedTime(self):
        """专用通道创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Bandwidth(self):
        """专用通道带宽值
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def TagSet(self):
        """专用通道标签值
        :rtype: list of Tag
        """
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def NetDetectId(self):
        """关联的网络自定义探测ID
        :rtype: str
        """
        return self._NetDetectId

    @NetDetectId.setter
    def NetDetectId(self, NetDetectId):
        self._NetDetectId = NetDetectId

    @property
    def EnableBGPCommunity(self):
        """BGP community开关
        :rtype: bool
        """
        return self._EnableBGPCommunity

    @EnableBGPCommunity.setter
    def EnableBGPCommunity(self, EnableBGPCommunity):
        self._EnableBGPCommunity = EnableBGPCommunity

    @property
    def NatType(self):
        """是否为Nat通道
        :rtype: int
        """
        return self._NatType

    @NatType.setter
    def NatType(self, NatType):
        self._NatType = NatType

    @property
    def VpcRegion(self):
        """VPC地域简码，如gz、cd
        :rtype: str
        """
        return self._VpcRegion

    @VpcRegion.setter
    def VpcRegion(self, VpcRegion):
        self._VpcRegion = VpcRegion

    @property
    def BfdEnable(self):
        """是否开启BFD
        :rtype: int
        """
        return self._BfdEnable

    @BfdEnable.setter
    def BfdEnable(self, BfdEnable):
        self._BfdEnable = BfdEnable

    @property
    def AccessPointType(self):
        """专用通道接入点类型
        :rtype: str
        """
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType

    @property
    def DirectConnectGatewayName(self):
        """专线网关名称
        :rtype: str
        """
        return self._DirectConnectGatewayName

    @DirectConnectGatewayName.setter
    def DirectConnectGatewayName(self, DirectConnectGatewayName):
        self._DirectConnectGatewayName = DirectConnectGatewayName

    @property
    def VpcName(self):
        """VPC名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def TencentBackupAddress(self):
        """TencentBackupAddress，腾讯侧备用互联 IP
        :rtype: str
        """
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress

    @property
    def SignLaw(self):
        """专用通道关联的物理专线是否签署了用户协议
        :rtype: bool
        """
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def CloudAttachId(self):
        """高速上云服务ID
        :rtype: str
        """
        return self._CloudAttachId

    @CloudAttachId.setter
    def CloudAttachId(self, CloudAttachId):
        self._CloudAttachId = CloudAttachId

    @property
    def ShareOrNot(self):
        """是否共享通道
        :rtype: int
        """
        return self._ShareOrNot

    @ShareOrNot.setter
    def ShareOrNot(self, ShareOrNot):
        self._ShareOrNot = ShareOrNot


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self._DirectConnectId = params.get("DirectConnectId")
        self._State = params.get("State")
        self._DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self._OwnerAccount = params.get("OwnerAccount")
        self._NetworkType = params.get("NetworkType")
        self._NetworkRegion = params.get("NetworkRegion")
        self._VpcId = params.get("VpcId")
        self._DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self._RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self._CreatedTime = params.get("CreatedTime")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self._TagSet.append(obj)
        self._NetDetectId = params.get("NetDetectId")
        self._EnableBGPCommunity = params.get("EnableBGPCommunity")
        self._NatType = params.get("NatType")
        self._VpcRegion = params.get("VpcRegion")
        self._BfdEnable = params.get("BfdEnable")
        self._AccessPointType = params.get("AccessPointType")
        self._DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self._VpcName = params.get("VpcName")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        self._SignLaw = params.get("SignLaw")
        self._CloudAttachId = params.get("CloudAttachId")
        self._ShareOrNot = params.get("ShareOrNot")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnelExtra(AbstractModel):
    """专用通道扩展信息

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param _DirectConnectId: 物理专线ID
        :type DirectConnectId: str
        :param _State: 专用通道状态
AVAILABLE:就绪或者已连接
PENDING:申请中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒绝
        :type State: str
        :param _DirectConnectOwnerAccount: 物理专线的拥有者，开发商账号 ID
        :type DirectConnectOwnerAccount: str
        :param _OwnerAccount: 专用通道的拥有者，开发商账号 ID
        :type OwnerAccount: str
        :param _NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :type NetworkType: str
        :param _NetworkRegion: VPC地域对应的网络名，如ap-guangzhou
        :type NetworkRegion: str
        :param _VpcId: 私有网络统一 ID 或者黑石网络统一 ID
        :type VpcId: str
        :param _DirectConnectGatewayId: 专线网关 ID
        :type DirectConnectGatewayId: str
        :param _RouteType: BGP ：BGP路由 STATIC：静态 默认为 BGP 路由
        :type RouteType: str
        :param _BgpPeer: 用户侧BGP，Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: 用户侧网段地址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _PublicAddresses: 互联网通道公网网段地址
        :type PublicAddresses: list of RouteFilterPrefix
        :param _Vlan: 专用通道的Vlan
        :type Vlan: int
        :param _TencentAddress: 腾讯侧互联 IP
        :type TencentAddress: str
        :param _TencentBackupAddress: 腾讯侧备用互联IP
        :type TencentBackupAddress: str
        :param _CustomerAddress: 用户侧互联 IP
        :type CustomerAddress: str
        :param _DirectConnectTunnelName: 专用通道名称
        :type DirectConnectTunnelName: str
        :param _CreatedTime: 专用通道创建时间
        :type CreatedTime: str
        :param _Bandwidth: 专用通道带宽值
        :type Bandwidth: int
        :param _NetDetectId: 关联的网络自定义探测ID
        :type NetDetectId: str
        :param _EnableBGPCommunity: BGP community开关
        :type EnableBGPCommunity: bool
        :param _NatType: 是否为Nat通道
        :type NatType: int
        :param _VpcRegion: VPC地域简码，如gz、cd
        :type VpcRegion: str
        :param _BfdEnable: 是否开启BFD
        :type BfdEnable: int
        :param _NqaEnable: 是否开启NQA
        :type NqaEnable: int
        :param _AccessPointType: 专用通道接入点类型
        :type AccessPointType: str
        :param _DirectConnectGatewayName: 专线网关名称
        :type DirectConnectGatewayName: str
        :param _VpcName: VPC名称
        :type VpcName: str
        :param _SignLaw: 专用通道关联的物理专线是否签署了用户协议
        :type SignLaw: bool
        :param _BfdInfo: BFD配置信息
        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        :param _NqaInfo: NQA配置信息
        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        :param _BgpStatus: BGP状态
        :type BgpStatus: :class:`tencentcloud.dc.v20180410.models.BGPStatus`
        :param _IPv6Enable: 是否开启IPv6
        :type IPv6Enable: int
        :param _TencentIPv6Address: 腾讯侧互联IPv6地址
        :type TencentIPv6Address: str
        :param _TencentBackupIPv6Address: 腾讯侧备用互联IPv6地址
        :type TencentBackupIPv6Address: str
        :param _BgpIPv6Status: BGPv6状态
        :type BgpIPv6Status: :class:`tencentcloud.dc.v20180410.models.BGPStatus`
        :param _CustomerIPv6Address: 用户侧互联IPv6地址
        :type CustomerIPv6Address: str
        :param _JumboEnable: 专用通道是否支持巨帧。1 支持，0 不支持
        :type JumboEnable: int
        :param _HighPrecisionBFDEnable: 专用通道是否支持高精度BFD。1支持，0不支持
        :type HighPrecisionBFDEnable: int
        """
        self._DirectConnectTunnelId = None
        self._DirectConnectId = None
        self._State = None
        self._DirectConnectOwnerAccount = None
        self._OwnerAccount = None
        self._NetworkType = None
        self._NetworkRegion = None
        self._VpcId = None
        self._DirectConnectGatewayId = None
        self._RouteType = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._PublicAddresses = None
        self._Vlan = None
        self._TencentAddress = None
        self._TencentBackupAddress = None
        self._CustomerAddress = None
        self._DirectConnectTunnelName = None
        self._CreatedTime = None
        self._Bandwidth = None
        self._NetDetectId = None
        self._EnableBGPCommunity = None
        self._NatType = None
        self._VpcRegion = None
        self._BfdEnable = None
        self._NqaEnable = None
        self._AccessPointType = None
        self._DirectConnectGatewayName = None
        self._VpcName = None
        self._SignLaw = None
        self._BfdInfo = None
        self._NqaInfo = None
        self._BgpStatus = None
        self._IPv6Enable = None
        self._TencentIPv6Address = None
        self._TencentBackupIPv6Address = None
        self._BgpIPv6Status = None
        self._CustomerIPv6Address = None
        self._JumboEnable = None
        self._HighPrecisionBFDEnable = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def DirectConnectId(self):
        """物理专线ID
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def State(self):
        """专用通道状态
AVAILABLE:就绪或者已连接
PENDING:申请中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒绝
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def DirectConnectOwnerAccount(self):
        """物理专线的拥有者，开发商账号 ID
        :rtype: str
        """
        return self._DirectConnectOwnerAccount

    @DirectConnectOwnerAccount.setter
    def DirectConnectOwnerAccount(self, DirectConnectOwnerAccount):
        self._DirectConnectOwnerAccount = DirectConnectOwnerAccount

    @property
    def OwnerAccount(self):
        """专用通道的拥有者，开发商账号 ID
        :rtype: str
        """
        return self._OwnerAccount

    @OwnerAccount.setter
    def OwnerAccount(self, OwnerAccount):
        self._OwnerAccount = OwnerAccount

    @property
    def NetworkType(self):
        """网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :rtype: str
        """
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def NetworkRegion(self):
        """VPC地域对应的网络名，如ap-guangzhou
        :rtype: str
        """
        return self._NetworkRegion

    @NetworkRegion.setter
    def NetworkRegion(self, NetworkRegion):
        self._NetworkRegion = NetworkRegion

    @property
    def VpcId(self):
        """私有网络统一 ID 或者黑石网络统一 ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DirectConnectGatewayId(self):
        """专线网关 ID
        :rtype: str
        """
        return self._DirectConnectGatewayId

    @DirectConnectGatewayId.setter
    def DirectConnectGatewayId(self, DirectConnectGatewayId):
        self._DirectConnectGatewayId = DirectConnectGatewayId

    @property
    def RouteType(self):
        """BGP ：BGP路由 STATIC：静态 默认为 BGP 路由
        :rtype: str
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def BgpPeer(self):
        """用户侧BGP，Asn，AuthKey
        :rtype: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        """
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        """用户侧网段地址
        :rtype: list of RouteFilterPrefix
        """
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def PublicAddresses(self):
        """互联网通道公网网段地址
        :rtype: list of RouteFilterPrefix
        """
        return self._PublicAddresses

    @PublicAddresses.setter
    def PublicAddresses(self, PublicAddresses):
        self._PublicAddresses = PublicAddresses

    @property
    def Vlan(self):
        """专用通道的Vlan
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        """腾讯侧互联 IP
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def TencentBackupAddress(self):
        """腾讯侧备用互联IP
        :rtype: str
        """
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress

    @property
    def CustomerAddress(self):
        """用户侧互联 IP
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def DirectConnectTunnelName(self):
        """专用通道名称
        :rtype: str
        """
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def CreatedTime(self):
        """专用通道创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Bandwidth(self):
        """专用通道带宽值
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def NetDetectId(self):
        """关联的网络自定义探测ID
        :rtype: str
        """
        return self._NetDetectId

    @NetDetectId.setter
    def NetDetectId(self, NetDetectId):
        self._NetDetectId = NetDetectId

    @property
    def EnableBGPCommunity(self):
        """BGP community开关
        :rtype: bool
        """
        return self._EnableBGPCommunity

    @EnableBGPCommunity.setter
    def EnableBGPCommunity(self, EnableBGPCommunity):
        self._EnableBGPCommunity = EnableBGPCommunity

    @property
    def NatType(self):
        """是否为Nat通道
        :rtype: int
        """
        return self._NatType

    @NatType.setter
    def NatType(self, NatType):
        self._NatType = NatType

    @property
    def VpcRegion(self):
        """VPC地域简码，如gz、cd
        :rtype: str
        """
        return self._VpcRegion

    @VpcRegion.setter
    def VpcRegion(self, VpcRegion):
        self._VpcRegion = VpcRegion

    @property
    def BfdEnable(self):
        """是否开启BFD
        :rtype: int
        """
        return self._BfdEnable

    @BfdEnable.setter
    def BfdEnable(self, BfdEnable):
        self._BfdEnable = BfdEnable

    @property
    def NqaEnable(self):
        """是否开启NQA
        :rtype: int
        """
        return self._NqaEnable

    @NqaEnable.setter
    def NqaEnable(self, NqaEnable):
        self._NqaEnable = NqaEnable

    @property
    def AccessPointType(self):
        """专用通道接入点类型
        :rtype: str
        """
        return self._AccessPointType

    @AccessPointType.setter
    def AccessPointType(self, AccessPointType):
        self._AccessPointType = AccessPointType

    @property
    def DirectConnectGatewayName(self):
        """专线网关名称
        :rtype: str
        """
        return self._DirectConnectGatewayName

    @DirectConnectGatewayName.setter
    def DirectConnectGatewayName(self, DirectConnectGatewayName):
        self._DirectConnectGatewayName = DirectConnectGatewayName

    @property
    def VpcName(self):
        """VPC名称
        :rtype: str
        """
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName

    @property
    def SignLaw(self):
        """专用通道关联的物理专线是否签署了用户协议
        :rtype: bool
        """
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def BfdInfo(self):
        """BFD配置信息
        :rtype: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        """
        return self._BfdInfo

    @BfdInfo.setter
    def BfdInfo(self, BfdInfo):
        self._BfdInfo = BfdInfo

    @property
    def NqaInfo(self):
        """NQA配置信息
        :rtype: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        """
        return self._NqaInfo

    @NqaInfo.setter
    def NqaInfo(self, NqaInfo):
        self._NqaInfo = NqaInfo

    @property
    def BgpStatus(self):
        """BGP状态
        :rtype: :class:`tencentcloud.dc.v20180410.models.BGPStatus`
        """
        return self._BgpStatus

    @BgpStatus.setter
    def BgpStatus(self, BgpStatus):
        self._BgpStatus = BgpStatus

    @property
    def IPv6Enable(self):
        """是否开启IPv6
        :rtype: int
        """
        return self._IPv6Enable

    @IPv6Enable.setter
    def IPv6Enable(self, IPv6Enable):
        self._IPv6Enable = IPv6Enable

    @property
    def TencentIPv6Address(self):
        """腾讯侧互联IPv6地址
        :rtype: str
        """
        return self._TencentIPv6Address

    @TencentIPv6Address.setter
    def TencentIPv6Address(self, TencentIPv6Address):
        self._TencentIPv6Address = TencentIPv6Address

    @property
    def TencentBackupIPv6Address(self):
        """腾讯侧备用互联IPv6地址
        :rtype: str
        """
        return self._TencentBackupIPv6Address

    @TencentBackupIPv6Address.setter
    def TencentBackupIPv6Address(self, TencentBackupIPv6Address):
        self._TencentBackupIPv6Address = TencentBackupIPv6Address

    @property
    def BgpIPv6Status(self):
        """BGPv6状态
        :rtype: :class:`tencentcloud.dc.v20180410.models.BGPStatus`
        """
        return self._BgpIPv6Status

    @BgpIPv6Status.setter
    def BgpIPv6Status(self, BgpIPv6Status):
        self._BgpIPv6Status = BgpIPv6Status

    @property
    def CustomerIPv6Address(self):
        """用户侧互联IPv6地址
        :rtype: str
        """
        return self._CustomerIPv6Address

    @CustomerIPv6Address.setter
    def CustomerIPv6Address(self, CustomerIPv6Address):
        self._CustomerIPv6Address = CustomerIPv6Address

    @property
    def JumboEnable(self):
        """专用通道是否支持巨帧。1 支持，0 不支持
        :rtype: int
        """
        return self._JumboEnable

    @JumboEnable.setter
    def JumboEnable(self, JumboEnable):
        self._JumboEnable = JumboEnable

    @property
    def HighPrecisionBFDEnable(self):
        """专用通道是否支持高精度BFD。1支持，0不支持
        :rtype: int
        """
        return self._HighPrecisionBFDEnable

    @HighPrecisionBFDEnable.setter
    def HighPrecisionBFDEnable(self, HighPrecisionBFDEnable):
        self._HighPrecisionBFDEnable = HighPrecisionBFDEnable


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self._DirectConnectId = params.get("DirectConnectId")
        self._State = params.get("State")
        self._DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self._OwnerAccount = params.get("OwnerAccount")
        self._NetworkType = params.get("NetworkType")
        self._NetworkRegion = params.get("NetworkRegion")
        self._VpcId = params.get("VpcId")
        self._DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self._RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        if params.get("PublicAddresses") is not None:
            self._PublicAddresses = []
            for item in params.get("PublicAddresses"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._PublicAddresses.append(obj)
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self._CreatedTime = params.get("CreatedTime")
        self._Bandwidth = params.get("Bandwidth")
        self._NetDetectId = params.get("NetDetectId")
        self._EnableBGPCommunity = params.get("EnableBGPCommunity")
        self._NatType = params.get("NatType")
        self._VpcRegion = params.get("VpcRegion")
        self._BfdEnable = params.get("BfdEnable")
        self._NqaEnable = params.get("NqaEnable")
        self._AccessPointType = params.get("AccessPointType")
        self._DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self._VpcName = params.get("VpcName")
        self._SignLaw = params.get("SignLaw")
        if params.get("BfdInfo") is not None:
            self._BfdInfo = BFDInfo()
            self._BfdInfo._deserialize(params.get("BfdInfo"))
        if params.get("NqaInfo") is not None:
            self._NqaInfo = NQAInfo()
            self._NqaInfo._deserialize(params.get("NqaInfo"))
        if params.get("BgpStatus") is not None:
            self._BgpStatus = BGPStatus()
            self._BgpStatus._deserialize(params.get("BgpStatus"))
        self._IPv6Enable = params.get("IPv6Enable")
        self._TencentIPv6Address = params.get("TencentIPv6Address")
        self._TencentBackupIPv6Address = params.get("TencentBackupIPv6Address")
        if params.get("BgpIPv6Status") is not None:
            self._BgpIPv6Status = BGPStatus()
            self._BgpIPv6Status._deserialize(params.get("BgpIPv6Status"))
        self._CustomerIPv6Address = params.get("CustomerIPv6Address")
        self._JumboEnable = params.get("JumboEnable")
        self._HighPrecisionBFDEnable = params.get("HighPrecisionBFDEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnelRoute(AbstractModel):
    """专用通道路由

    """

    def __init__(self):
        r"""
        :param _RouteId: 专用通道路由ID
        :type RouteId: str
        :param _DestinationCidrBlock: 网段CIDR
        :type DestinationCidrBlock: str
        :param _RouteType: 路由类型：BGP/STATIC路由
        :type RouteType: str
        :param _Status: ENABLE：路由启用，DISABLE：路由禁用
        :type Status: str
        :param _ASPath: ASPath信息
        :type ASPath: list of str
        :param _NextHop: 路由下一跳IP
        :type NextHop: str
        :param _UpdateTime: 路由更新时间
        :type UpdateTime: str
        :param _ApplyOnTunnelEnable: 是否配置在通道上
        :type ApplyOnTunnelEnable: bool
        """
        self._RouteId = None
        self._DestinationCidrBlock = None
        self._RouteType = None
        self._Status = None
        self._ASPath = None
        self._NextHop = None
        self._UpdateTime = None
        self._ApplyOnTunnelEnable = None

    @property
    def RouteId(self):
        """专用通道路由ID
        :rtype: str
        """
        return self._RouteId

    @RouteId.setter
    def RouteId(self, RouteId):
        self._RouteId = RouteId

    @property
    def DestinationCidrBlock(self):
        """网段CIDR
        :rtype: str
        """
        return self._DestinationCidrBlock

    @DestinationCidrBlock.setter
    def DestinationCidrBlock(self, DestinationCidrBlock):
        self._DestinationCidrBlock = DestinationCidrBlock

    @property
    def RouteType(self):
        """路由类型：BGP/STATIC路由
        :rtype: str
        """
        return self._RouteType

    @RouteType.setter
    def RouteType(self, RouteType):
        self._RouteType = RouteType

    @property
    def Status(self):
        """ENABLE：路由启用，DISABLE：路由禁用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ASPath(self):
        """ASPath信息
        :rtype: list of str
        """
        return self._ASPath

    @ASPath.setter
    def ASPath(self, ASPath):
        self._ASPath = ASPath

    @property
    def NextHop(self):
        """路由下一跳IP
        :rtype: str
        """
        return self._NextHop

    @NextHop.setter
    def NextHop(self, NextHop):
        self._NextHop = NextHop

    @property
    def UpdateTime(self):
        """路由更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ApplyOnTunnelEnable(self):
        """是否配置在通道上
        :rtype: bool
        """
        return self._ApplyOnTunnelEnable

    @ApplyOnTunnelEnable.setter
    def ApplyOnTunnelEnable(self, ApplyOnTunnelEnable):
        self._ApplyOnTunnelEnable = ApplyOnTunnelEnable


    def _deserialize(self, params):
        self._RouteId = params.get("RouteId")
        self._DestinationCidrBlock = params.get("DestinationCidrBlock")
        self._RouteType = params.get("RouteType")
        self._Status = params.get("Status")
        self._ASPath = params.get("ASPath")
        self._NextHop = params.get("NextHop")
        self._UpdateTime = params.get("UpdateTime")
        self._ApplyOnTunnelEnable = params.get("ApplyOnTunnelEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInternetAddressRequest(AbstractModel):
    """DisableInternetAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 公网互联网地址ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """公网互联网地址ID
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
        


class DisableInternetAddressResponse(AbstractModel):
    """DisableInternetAddress返回参数结构体

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


class EnableInternetAddressRequest(AbstractModel):
    """EnableInternetAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 互联网公网地址ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """互联网公网地址ID
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
        


class EnableInternetAddressResponse(AbstractModel):
    """EnableInternetAddress返回参数结构体

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
    """用于条件过滤查询

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
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
        


class InternetAddressDetail(AbstractModel):
    """互联网地址详细信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 互联网地址ID
        :type InstanceId: str
        :param _Subnet: 互联网网络地址
        :type Subnet: str
        :param _MaskLen: 网络地址掩码长度
        :type MaskLen: int
        :param _AddrType: 0:BGP
1:电信
2:移动
3:联通
        :type AddrType: int
        :param _Status: 0:使用中
1:已停用
2:已退还
        :type Status: int
        :param _ApplyTime: 申请时间
        :type ApplyTime: str
        :param _StopTime: 停用时间
        :type StopTime: str
        :param _ReleaseTime: 退还时间
        :type ReleaseTime: str
        :param _Region: 地域信息
        :type Region: str
        :param _AppId: 用户ID
        :type AppId: int
        :param _AddrProto: 0:IPv4 1:IPv6
        :type AddrProto: int
        :param _ReserveTime: 释放状态的IP地址保留的天数
        :type ReserveTime: int
        """
        self._InstanceId = None
        self._Subnet = None
        self._MaskLen = None
        self._AddrType = None
        self._Status = None
        self._ApplyTime = None
        self._StopTime = None
        self._ReleaseTime = None
        self._Region = None
        self._AppId = None
        self._AddrProto = None
        self._ReserveTime = None

    @property
    def InstanceId(self):
        """互联网地址ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Subnet(self):
        """互联网网络地址
        :rtype: str
        """
        return self._Subnet

    @Subnet.setter
    def Subnet(self, Subnet):
        self._Subnet = Subnet

    @property
    def MaskLen(self):
        """网络地址掩码长度
        :rtype: int
        """
        return self._MaskLen

    @MaskLen.setter
    def MaskLen(self, MaskLen):
        self._MaskLen = MaskLen

    @property
    def AddrType(self):
        """0:BGP
1:电信
2:移动
3:联通
        :rtype: int
        """
        return self._AddrType

    @AddrType.setter
    def AddrType(self, AddrType):
        self._AddrType = AddrType

    @property
    def Status(self):
        """0:使用中
1:已停用
2:已退还
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApplyTime(self):
        """申请时间
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def StopTime(self):
        """停用时间
        :rtype: str
        """
        return self._StopTime

    @StopTime.setter
    def StopTime(self, StopTime):
        self._StopTime = StopTime

    @property
    def ReleaseTime(self):
        """退还时间
        :rtype: str
        """
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def Region(self):
        """地域信息
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def AppId(self):
        """用户ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AddrProto(self):
        """0:IPv4 1:IPv6
        :rtype: int
        """
        return self._AddrProto

    @AddrProto.setter
    def AddrProto(self, AddrProto):
        self._AddrProto = AddrProto

    @property
    def ReserveTime(self):
        """释放状态的IP地址保留的天数
        :rtype: int
        """
        return self._ReserveTime

    @ReserveTime.setter
    def ReserveTime(self, ReserveTime):
        self._ReserveTime = ReserveTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Subnet = params.get("Subnet")
        self._MaskLen = params.get("MaskLen")
        self._AddrType = params.get("AddrType")
        self._Status = params.get("Status")
        self._ApplyTime = params.get("ApplyTime")
        self._StopTime = params.get("StopTime")
        self._ReleaseTime = params.get("ReleaseTime")
        self._Region = params.get("Region")
        self._AppId = params.get("AppId")
        self._AddrProto = params.get("AddrProto")
        self._ReserveTime = params.get("ReserveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAddressStatistics(AbstractModel):
    """互联网公网地址统计

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _SubnetNum: 互联网公网地址数量
        :type SubnetNum: int
        """
        self._Region = None
        self._SubnetNum = None

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
    def SubnetNum(self):
        """互联网公网地址数量
        :rtype: int
        """
        return self._SubnetNum

    @SubnetNum.setter
    def SubnetNum(self, SubnetNum):
        self._SubnetNum = SubnetNum


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._SubnetNum = params.get("SubnetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectId: 物理专线ID。
        :type DirectConnectId: str
        :param _DirectConnectName: 物理专线名称。
        :type DirectConnectName: str
        :param _CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
        :type CircuitCode: str
        :param _Vlan: 物理专线调试VLAN。
        :type Vlan: int
        :param _TencentAddress: 物理专线调试腾讯侧互联 IP。
        :type TencentAddress: str
        :param _CustomerAddress: 物理专线调试用户侧互联 IP。
        :type CustomerAddress: str
        :param _CustomerName: 物理专线申请者姓名。默认从账户体系获取。
        :type CustomerName: str
        :param _CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
        :type CustomerContactMail: str
        :param _CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
        :type CustomerContactNumber: str
        :param _FaultReportContactPerson: 报障联系人。
        :type FaultReportContactPerson: str
        :param _FaultReportContactNumber: 报障联系电话。
        :type FaultReportContactNumber: str
        :param _SignLaw: 物理专线申请者补签用户使用协议。
        :type SignLaw: bool
        :param _Bandwidth: 物理专线带宽。
        :type Bandwidth: int
        """
        self._DirectConnectId = None
        self._DirectConnectName = None
        self._CircuitCode = None
        self._Vlan = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._CustomerName = None
        self._CustomerContactMail = None
        self._CustomerContactNumber = None
        self._FaultReportContactPerson = None
        self._FaultReportContactNumber = None
        self._SignLaw = None
        self._Bandwidth = None

    @property
    def DirectConnectId(self):
        """物理专线ID。
        :rtype: str
        """
        return self._DirectConnectId

    @DirectConnectId.setter
    def DirectConnectId(self, DirectConnectId):
        self._DirectConnectId = DirectConnectId

    @property
    def DirectConnectName(self):
        """物理专线名称。
        :rtype: str
        """
        return self._DirectConnectName

    @DirectConnectName.setter
    def DirectConnectName(self, DirectConnectName):
        self._DirectConnectName = DirectConnectName

    @property
    def CircuitCode(self):
        """运营商或者服务商为物理专线提供的电路编码。
        :rtype: str
        """
        return self._CircuitCode

    @CircuitCode.setter
    def CircuitCode(self, CircuitCode):
        self._CircuitCode = CircuitCode

    @property
    def Vlan(self):
        """物理专线调试VLAN。
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def TencentAddress(self):
        """物理专线调试腾讯侧互联 IP。
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        """物理专线调试用户侧互联 IP。
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def CustomerName(self):
        """物理专线申请者姓名。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerName

    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self._CustomerName = CustomerName

    @property
    def CustomerContactMail(self):
        """物理专线申请者联系邮箱。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerContactMail

    @CustomerContactMail.setter
    def CustomerContactMail(self, CustomerContactMail):
        self._CustomerContactMail = CustomerContactMail

    @property
    def CustomerContactNumber(self):
        """物理专线申请者联系号码。默认从账户体系获取。
        :rtype: str
        """
        return self._CustomerContactNumber

    @CustomerContactNumber.setter
    def CustomerContactNumber(self, CustomerContactNumber):
        self._CustomerContactNumber = CustomerContactNumber

    @property
    def FaultReportContactPerson(self):
        """报障联系人。
        :rtype: str
        """
        return self._FaultReportContactPerson

    @FaultReportContactPerson.setter
    def FaultReportContactPerson(self, FaultReportContactPerson):
        self._FaultReportContactPerson = FaultReportContactPerson

    @property
    def FaultReportContactNumber(self):
        """报障联系电话。
        :rtype: str
        """
        return self._FaultReportContactNumber

    @FaultReportContactNumber.setter
    def FaultReportContactNumber(self, FaultReportContactNumber):
        self._FaultReportContactNumber = FaultReportContactNumber

    @property
    def SignLaw(self):
        """物理专线申请者补签用户使用协议。
        :rtype: bool
        """
        return self._SignLaw

    @SignLaw.setter
    def SignLaw(self, SignLaw):
        self._SignLaw = SignLaw

    @property
    def Bandwidth(self):
        """物理专线带宽。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth


    def _deserialize(self, params):
        self._DirectConnectId = params.get("DirectConnectId")
        self._DirectConnectName = params.get("DirectConnectName")
        self._CircuitCode = params.get("CircuitCode")
        self._Vlan = params.get("Vlan")
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._CustomerName = params.get("CustomerName")
        self._CustomerContactMail = params.get("CustomerContactMail")
        self._CustomerContactNumber = params.get("CustomerContactNumber")
        self._FaultReportContactPerson = params.get("FaultReportContactPerson")
        self._FaultReportContactNumber = params.get("FaultReportContactNumber")
        self._SignLaw = params.get("SignLaw")
        self._Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute返回参数结构体

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


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。
        :type DirectConnectTunnelId: str
        :param _DirectConnectTunnelName: 专用通道名称。
        :type DirectConnectTunnelName: str
        :param _BgpPeer: 用户侧BGP，包括Asn，AuthKey。
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: 用户侧网段地址。
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param _TencentAddress: 腾讯侧互联IP。
        :type TencentAddress: str
        :param _CustomerAddress: 用户侧互联IP。
        :type CustomerAddress: str
        :param _Bandwidth: 专用通道带宽值，单位为M。
        :type Bandwidth: int
        :param _TencentBackupAddress: 腾讯侧备用互联IP。
        :type TencentBackupAddress: str
        """
        self._DirectConnectTunnelId = None
        self._DirectConnectTunnelName = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._TencentAddress = None
        self._CustomerAddress = None
        self._Bandwidth = None
        self._TencentBackupAddress = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def DirectConnectTunnelName(self):
        """专用通道名称。
        :rtype: str
        """
        return self._DirectConnectTunnelName

    @DirectConnectTunnelName.setter
    def DirectConnectTunnelName(self, DirectConnectTunnelName):
        self._DirectConnectTunnelName = DirectConnectTunnelName

    @property
    def BgpPeer(self):
        """用户侧BGP，包括Asn，AuthKey。
        :rtype: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        """
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        """用户侧网段地址。
        :rtype: list of RouteFilterPrefix
        """
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def TencentAddress(self):
        """腾讯侧互联IP。
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def CustomerAddress(self):
        """用户侧互联IP。
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def Bandwidth(self):
        """专用通道带宽值，单位为M。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def TencentBackupAddress(self):
        """腾讯侧备用互联IP。
        :rtype: str
        """
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self._DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._RouteFilterPrefixes.append(obj)
        self._TencentAddress = params.get("TencentAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._Bandwidth = params.get("Bandwidth")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute返回参数结构体

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


class ModifyDirectConnectTunnelExtraRequest(AbstractModel):
    """ModifyDirectConnectTunnelExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。
        :type DirectConnectTunnelId: str
        :param _Vlan: 专用通道的Vlan。
        :type Vlan: int
        :param _BgpPeer: Bgp参数，包括Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param _RouteFilterPrefixes: 用户侧过滤网段地址。
        :type RouteFilterPrefixes: :class:`tencentcloud.dc.v20180410.models.RouteFilterPrefix`
        :param _TencentAddress: 腾讯侧互联IP。
        :type TencentAddress: str
        :param _TencentBackupAddress: 腾讯侧备用互联IP。
        :type TencentBackupAddress: str
        :param _CustomerAddress: 用户侧互联IP。
        :type CustomerAddress: str
        :param _Bandwidth: 专用通道带宽值。
        :type Bandwidth: int
        :param _EnableBGPCommunity: BGP community开关。
        :type EnableBGPCommunity: bool
        :param _BfdEnable: 是否开启BFD。
        :type BfdEnable: int
        :param _NqaEnable: 是否开启NQA。
        :type NqaEnable: int
        :param _BfdInfo: BFD配置信息。
        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        :param _NqaInfo: NQA配置信息。
        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        :param _IPv6Enable: IPV6使能。0：停用IPv6；1: 启用IPv6。
        :type IPv6Enable: int
        :param _CustomerIDCRoutes: 去往用户侧的路由信息。
        :type CustomerIDCRoutes: list of RouteFilterPrefix
        :param _JumboEnable: 是否开启巨帧。1：开启；0：不开启。
        :type JumboEnable: int
        :param _TencentIPv6Address: 腾讯侧互联IPv6。
        :type TencentIPv6Address: str
        :param _TencentBackupIPv6Address: 腾讯侧备用互联IPv6。
        :type TencentBackupIPv6Address: str
        :param _CustomerIPv6Address: 用户侧互联IPv6。
        :type CustomerIPv6Address: str
        """
        self._DirectConnectTunnelId = None
        self._Vlan = None
        self._BgpPeer = None
        self._RouteFilterPrefixes = None
        self._TencentAddress = None
        self._TencentBackupAddress = None
        self._CustomerAddress = None
        self._Bandwidth = None
        self._EnableBGPCommunity = None
        self._BfdEnable = None
        self._NqaEnable = None
        self._BfdInfo = None
        self._NqaInfo = None
        self._IPv6Enable = None
        self._CustomerIDCRoutes = None
        self._JumboEnable = None
        self._TencentIPv6Address = None
        self._TencentBackupIPv6Address = None
        self._CustomerIPv6Address = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId

    @property
    def Vlan(self):
        """专用通道的Vlan。
        :rtype: int
        """
        return self._Vlan

    @Vlan.setter
    def Vlan(self, Vlan):
        self._Vlan = Vlan

    @property
    def BgpPeer(self):
        """Bgp参数，包括Asn，AuthKey
        :rtype: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        """
        return self._BgpPeer

    @BgpPeer.setter
    def BgpPeer(self, BgpPeer):
        self._BgpPeer = BgpPeer

    @property
    def RouteFilterPrefixes(self):
        """用户侧过滤网段地址。
        :rtype: :class:`tencentcloud.dc.v20180410.models.RouteFilterPrefix`
        """
        return self._RouteFilterPrefixes

    @RouteFilterPrefixes.setter
    def RouteFilterPrefixes(self, RouteFilterPrefixes):
        self._RouteFilterPrefixes = RouteFilterPrefixes

    @property
    def TencentAddress(self):
        """腾讯侧互联IP。
        :rtype: str
        """
        return self._TencentAddress

    @TencentAddress.setter
    def TencentAddress(self, TencentAddress):
        self._TencentAddress = TencentAddress

    @property
    def TencentBackupAddress(self):
        """腾讯侧备用互联IP。
        :rtype: str
        """
        return self._TencentBackupAddress

    @TencentBackupAddress.setter
    def TencentBackupAddress(self, TencentBackupAddress):
        self._TencentBackupAddress = TencentBackupAddress

    @property
    def CustomerAddress(self):
        """用户侧互联IP。
        :rtype: str
        """
        return self._CustomerAddress

    @CustomerAddress.setter
    def CustomerAddress(self, CustomerAddress):
        self._CustomerAddress = CustomerAddress

    @property
    def Bandwidth(self):
        """专用通道带宽值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def EnableBGPCommunity(self):
        """BGP community开关。
        :rtype: bool
        """
        return self._EnableBGPCommunity

    @EnableBGPCommunity.setter
    def EnableBGPCommunity(self, EnableBGPCommunity):
        self._EnableBGPCommunity = EnableBGPCommunity

    @property
    def BfdEnable(self):
        """是否开启BFD。
        :rtype: int
        """
        return self._BfdEnable

    @BfdEnable.setter
    def BfdEnable(self, BfdEnable):
        self._BfdEnable = BfdEnable

    @property
    def NqaEnable(self):
        """是否开启NQA。
        :rtype: int
        """
        return self._NqaEnable

    @NqaEnable.setter
    def NqaEnable(self, NqaEnable):
        self._NqaEnable = NqaEnable

    @property
    def BfdInfo(self):
        """BFD配置信息。
        :rtype: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        """
        return self._BfdInfo

    @BfdInfo.setter
    def BfdInfo(self, BfdInfo):
        self._BfdInfo = BfdInfo

    @property
    def NqaInfo(self):
        """NQA配置信息。
        :rtype: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        """
        return self._NqaInfo

    @NqaInfo.setter
    def NqaInfo(self, NqaInfo):
        self._NqaInfo = NqaInfo

    @property
    def IPv6Enable(self):
        """IPV6使能。0：停用IPv6；1: 启用IPv6。
        :rtype: int
        """
        return self._IPv6Enable

    @IPv6Enable.setter
    def IPv6Enable(self, IPv6Enable):
        self._IPv6Enable = IPv6Enable

    @property
    def CustomerIDCRoutes(self):
        """去往用户侧的路由信息。
        :rtype: list of RouteFilterPrefix
        """
        return self._CustomerIDCRoutes

    @CustomerIDCRoutes.setter
    def CustomerIDCRoutes(self, CustomerIDCRoutes):
        self._CustomerIDCRoutes = CustomerIDCRoutes

    @property
    def JumboEnable(self):
        """是否开启巨帧。1：开启；0：不开启。
        :rtype: int
        """
        return self._JumboEnable

    @JumboEnable.setter
    def JumboEnable(self, JumboEnable):
        self._JumboEnable = JumboEnable

    @property
    def TencentIPv6Address(self):
        """腾讯侧互联IPv6。
        :rtype: str
        """
        return self._TencentIPv6Address

    @TencentIPv6Address.setter
    def TencentIPv6Address(self, TencentIPv6Address):
        self._TencentIPv6Address = TencentIPv6Address

    @property
    def TencentBackupIPv6Address(self):
        """腾讯侧备用互联IPv6。
        :rtype: str
        """
        return self._TencentBackupIPv6Address

    @TencentBackupIPv6Address.setter
    def TencentBackupIPv6Address(self, TencentBackupIPv6Address):
        self._TencentBackupIPv6Address = TencentBackupIPv6Address

    @property
    def CustomerIPv6Address(self):
        """用户侧互联IPv6。
        :rtype: str
        """
        return self._CustomerIPv6Address

    @CustomerIPv6Address.setter
    def CustomerIPv6Address(self, CustomerIPv6Address):
        self._CustomerIPv6Address = CustomerIPv6Address


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self._Vlan = params.get("Vlan")
        if params.get("BgpPeer") is not None:
            self._BgpPeer = BgpPeer()
            self._BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self._RouteFilterPrefixes = RouteFilterPrefix()
            self._RouteFilterPrefixes._deserialize(params.get("RouteFilterPrefixes"))
        self._TencentAddress = params.get("TencentAddress")
        self._TencentBackupAddress = params.get("TencentBackupAddress")
        self._CustomerAddress = params.get("CustomerAddress")
        self._Bandwidth = params.get("Bandwidth")
        self._EnableBGPCommunity = params.get("EnableBGPCommunity")
        self._BfdEnable = params.get("BfdEnable")
        self._NqaEnable = params.get("NqaEnable")
        if params.get("BfdInfo") is not None:
            self._BfdInfo = BFDInfo()
            self._BfdInfo._deserialize(params.get("BfdInfo"))
        if params.get("NqaInfo") is not None:
            self._NqaInfo = NQAInfo()
            self._NqaInfo._deserialize(params.get("NqaInfo"))
        self._IPv6Enable = params.get("IPv6Enable")
        if params.get("CustomerIDCRoutes") is not None:
            self._CustomerIDCRoutes = []
            for item in params.get("CustomerIDCRoutes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self._CustomerIDCRoutes.append(obj)
        self._JumboEnable = params.get("JumboEnable")
        self._TencentIPv6Address = params.get("TencentIPv6Address")
        self._TencentBackupIPv6Address = params.get("TencentBackupIPv6Address")
        self._CustomerIPv6Address = params.get("CustomerIPv6Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectTunnelExtraResponse(AbstractModel):
    """ModifyDirectConnectTunnelExtra返回参数结构体

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


class NQAInfo(AbstractModel):
    """nqa配置信息

    """

    def __init__(self):
        r"""
        :param _ProbeFailedTimes: 健康检查次数
        :type ProbeFailedTimes: int
        :param _Interval: 健康检查间隔
        :type Interval: int
        :param _DestinationIp: 健康检查地址
        :type DestinationIp: str
        """
        self._ProbeFailedTimes = None
        self._Interval = None
        self._DestinationIp = None

    @property
    def ProbeFailedTimes(self):
        """健康检查次数
        :rtype: int
        """
        return self._ProbeFailedTimes

    @ProbeFailedTimes.setter
    def ProbeFailedTimes(self, ProbeFailedTimes):
        self._ProbeFailedTimes = ProbeFailedTimes

    @property
    def Interval(self):
        """健康检查间隔
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def DestinationIp(self):
        """健康检查地址
        :rtype: str
        """
        return self._DestinationIp

    @DestinationIp.setter
    def DestinationIp(self, DestinationIp):
        self._DestinationIp = DestinationIp


    def _deserialize(self, params):
        self._ProbeFailedTimes = params.get("ProbeFailedTimes")
        self._Interval = params.get("Interval")
        self._DestinationIp = params.get("DestinationIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortSpecification(AbstractModel):
    """端口规格

    """

    def __init__(self):
        r"""
        :param _InternationalName: 端口名称
        :type InternationalName: str
        :param _Specification: 端口规格（M）
        :type Specification: int
        :param _PortType: 端口类型：T-电口，X-光口
        :type PortType: str
        """
        self._InternationalName = None
        self._Specification = None
        self._PortType = None

    @property
    def InternationalName(self):
        """端口名称
        :rtype: str
        """
        return self._InternationalName

    @InternationalName.setter
    def InternationalName(self, InternationalName):
        self._InternationalName = InternationalName

    @property
    def Specification(self):
        """端口规格（M）
        :rtype: int
        """
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def PortType(self):
        """端口类型：T-电口，X-光口
        :rtype: str
        """
        return self._PortType

    @PortType.setter
    def PortType(self, PortType):
        self._PortType = PortType


    def _deserialize(self, params):
        self._InternationalName = params.get("InternationalName")
        self._Specification = params.get("Specification")
        self._PortType = params.get("PortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DirectConnectTunnelId: 专用通道ID。
        :type DirectConnectTunnelId: str
        """
        self._DirectConnectTunnelId = None

    @property
    def DirectConnectTunnelId(self):
        """专用通道ID。
        :rtype: str
        """
        return self._DirectConnectTunnelId

    @DirectConnectTunnelId.setter
    def DirectConnectTunnelId(self, DirectConnectTunnelId):
        self._DirectConnectTunnelId = DirectConnectTunnelId


    def _deserialize(self, params):
        self._DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel返回参数结构体

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


class ReleaseInternetAddressRequest(AbstractModel):
    """ReleaseInternetAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 公网互联网地址ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """公网互联网地址ID
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
        


class ReleaseInternetAddressResponse(AbstractModel):
    """ReleaseInternetAddress返回参数结构体

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


class RouteFilterPrefix(AbstractModel):
    """用户侧网段地址

    """

    def __init__(self):
        r"""
        :param _Cidr: 用户侧网段地址
        :type Cidr: str
        """
        self._Cidr = None

    @property
    def Cidr(self):
        """用户侧网段地址
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr


    def _deserialize(self, params):
        self._Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

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
        """标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值
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
        