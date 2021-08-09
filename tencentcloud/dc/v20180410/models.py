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
        """
        :param DirectConnectTunnelId: 物理专线拥有者接受共享专用通道申请\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccessPoint(AbstractModel):
    """接入点信息。

    """

    def __init__(self):
        """
        :param AccessPointName: 接入点的名称。\n        :type AccessPointName: str\n        :param AccessPointId: 接入点唯一ID。\n        :type AccessPointId: str\n        :param State: 接入点的状态。可用，不可用。\n        :type State: str\n        :param Location: 接入点的位置。\n        :type Location: str\n        :param LineOperator: 接入点支持的运营商列表。\n        :type LineOperator: list of str\n        :param RegionId: 接入点管理的大区ID。\n        :type RegionId: str\n        :param AvailablePortType: 接入点可用的端口类型列表。1000BASE-T代表千兆电口，1000BASE-LX代表千兆单模光口10km，1000BASE-ZX代表千兆单模光口80km,10GBASE-LR代表万兆单模光口10km,10GBASE-ZR代表万兆单模光口80km,10GBASE-LH代表万兆单模光口40km,100GBASE-LR4代表100G单模光口10km
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailablePortType: list of str\n        :param Coordinate: 接入点经纬度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Coordinate: :class:`tencentcloud.dc.v20180410.models.Coordinate`\n        :param City: 接入点所在城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        :param Area: 接入点地域名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Area: str\n        """
        self.AccessPointName = None
        self.AccessPointId = None
        self.State = None
        self.Location = None
        self.LineOperator = None
        self.RegionId = None
        self.AvailablePortType = None
        self.Coordinate = None
        self.City = None
        self.Area = None


    def _deserialize(self, params):
        self.AccessPointName = params.get("AccessPointName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.Location = params.get("Location")
        self.LineOperator = params.get("LineOperator")
        self.RegionId = params.get("RegionId")
        self.AvailablePortType = params.get("AvailablePortType")
        if params.get("Coordinate") is not None:
            self.Coordinate = Coordinate()
            self.Coordinate._deserialize(params.get("Coordinate"))
        self.City = params.get("City")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressRequest(AbstractModel):
    """ApplyInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param MaskLen: CIDR地址掩码长度\n        :type MaskLen: int\n        :param AddrType: 0:BGP类型地址
1：中国电信
2：中国移动
3：中国联通\n        :type AddrType: int\n        :param AddrProto: 0：IPv4
1:IPv6\n        :type AddrProto: int\n        """
        self.MaskLen = None
        self.AddrType = None
        self.AddrProto = None


    def _deserialize(self, params):
        self.MaskLen = params.get("MaskLen")
        self.AddrType = params.get("AddrType")
        self.AddrProto = params.get("AddrProto")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyInternetAddressResponse(AbstractModel):
    """ApplyInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 互联网公网地址ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class BFDInfo(AbstractModel):
    """BFD配置信息

    """

    def __init__(self):
        """
        :param ProbeFailedTimes: 健康检查次数\n        :type ProbeFailedTimes: int\n        :param Interval: 健康检查间隔\n        :type Interval: int\n        """
        self.ProbeFailedTimes = None
        self.Interval = None


    def _deserialize(self, params):
        self.ProbeFailedTimes = params.get("ProbeFailedTimes")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPStatus(AbstractModel):
    """bgp状态信息

    """

    def __init__(self):
        """
        :param TencentAddressBgpState: 腾讯侧主互联IP BGP状态\n        :type TencentAddressBgpState: str\n        :param TencentBackupAddressBgpState: 腾讯侧备互联IP BGP状态\n        :type TencentBackupAddressBgpState: str\n        """
        self.TencentAddressBgpState = None
        self.TencentBackupAddressBgpState = None


    def _deserialize(self, params):
        self.TencentAddressBgpState = params.get("TencentAddressBgpState")
        self.TencentBackupAddressBgpState = params.get("TencentBackupAddressBgpState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BgpPeer(AbstractModel):
    """bgp参数，包括Asn，AuthKey

    """

    def __init__(self):
        """
        :param Asn: 用户侧，BGP Asn\n        :type Asn: int\n        :param AuthKey: 用户侧BGP密钥\n        :type AuthKey: str\n        """
        self.Asn = None
        self.AuthKey = None


    def _deserialize(self, params):
        self.Asn = params.get("Asn")
        self.AuthKey = params.get("AuthKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Coordinate(AbstractModel):
    """坐标，经维度描述

    """

    def __init__(self):
        """
        :param Lat: 纬度\n        :type Lat: float\n        :param Lng: 经度\n        :type Lng: float\n        """
        self.Lat = None
        self.Lng = None


    def _deserialize(self, params):
        self.Lat = params.get("Lat")
        self.Lng = params.get("Lng")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectName: 物理专线的名称。\n        :type DirectConnectName: str\n        :param AccessPointId: 物理专线所在的接入点。
您可以通过调用 DescribeAccessPoints接口获取地域ID。所选择的接入点必须存在且处于可接入的状态。\n        :type AccessPointId: str\n        :param LineOperator: 提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。\n        :type LineOperator: str\n        :param PortType: 物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）。\n        :type PortType: str\n        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。\n        :type CircuitCode: str\n        :param Location: 本地数据中心的地理位置。\n        :type Location: str\n        :param Bandwidth: 物理专线接入接口带宽，单位为Mbps，默认值为1000，取值范围为 [2, 10240]。\n        :type Bandwidth: int\n        :param RedundantDirectConnectId: 冗余物理专线的ID。\n        :type RedundantDirectConnectId: str\n        :param Vlan: 物理专线调试VLAN。默认开启VLAN，自动分配VLAN。\n        :type Vlan: int\n        :param TencentAddress: 物理专线调试腾讯侧互联 IP。默认自动分配。\n        :type TencentAddress: str\n        :param CustomerAddress: 物理专线调试用户侧互联 IP。默认自动分配。\n        :type CustomerAddress: str\n        :param CustomerName: 物理专线申请者姓名。默认从账户体系获取。\n        :type CustomerName: str\n        :param CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。\n        :type CustomerContactMail: str\n        :param CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。\n        :type CustomerContactNumber: str\n        :param FaultReportContactPerson: 报障联系人。\n        :type FaultReportContactPerson: str\n        :param FaultReportContactNumber: 报障联系电话。\n        :type FaultReportContactNumber: str\n        :param SignLaw: 物理专线申请者是否签署了用户使用协议。默认已签署\n        :type SignLaw: bool\n        """
        self.DirectConnectName = None
        self.AccessPointId = None
        self.LineOperator = None
        self.PortType = None
        self.CircuitCode = None
        self.Location = None
        self.Bandwidth = None
        self.RedundantDirectConnectId = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.SignLaw = None


    def _deserialize(self, params):
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.LineOperator = params.get("LineOperator")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
        self.Location = params.get("Location")
        self.Bandwidth = params.get("Bandwidth")
        self.RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        self.SignLaw = params.get("SignLaw")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectIdSet: 物理专线的ID。\n        :type DirectConnectIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DirectConnectIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DirectConnectIdSet = params.get("DirectConnectIdSet")
        self.RequestId = params.get("RequestId")


class CreateDirectConnectTunnelRequest(AbstractModel):
    """CreateDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectId: 专线 ID，例如：dc-kd7d06of\n        :type DirectConnectId: str\n        :param DirectConnectTunnelName: 专用通道名称\n        :type DirectConnectTunnelName: str\n        :param DirectConnectOwnerAccount: 物理专线 owner，缺省为当前客户（物理专线 owner）
共享专线时这里需要填写共享专线的开发商账号 ID\n        :type DirectConnectOwnerAccount: str\n        :param NetworkType: 网络类型，分别为VPC、BMVPC，CCN，默认是VPC
VPC：私有网络
BMVPC：黑石网络
CCN：云联网\n        :type NetworkType: str\n        :param NetworkRegion: 网络地域\n        :type NetworkRegion: str\n        :param VpcId: 私有网络统一 ID 或者黑石网络统一 ID\n        :type VpcId: str\n        :param DirectConnectGatewayId: 专线网关 ID，例如 dcg-d545ddf\n        :type DirectConnectGatewayId: str\n        :param Bandwidth: 专线带宽，单位：Mbps
默认是物理专线带宽值\n        :type Bandwidth: int\n        :param RouteType: BGP ：BGP路由
STATIC：静态
默认为 BGP 路由\n        :type RouteType: str\n        :param BgpPeer: BgpPeer，用户侧bgp信息，包括Asn和AuthKey\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: 静态路由，用户IDC的网段地址\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param Vlan: vlan，范围：0 ~ 3000
0：不开启子接口
默认值是非0\n        :type Vlan: int\n        :param TencentAddress: TencentAddress，腾讯侧互联 IP\n        :type TencentAddress: str\n        :param CustomerAddress: CustomerAddress，用户侧互联 IP\n        :type CustomerAddress: str\n        :param TencentBackupAddress: TencentBackupAddress，腾讯侧备用互联 IP\n        :type TencentBackupAddress: str\n        :param CloudAttachId: 高速上云服务ID\n        :type CloudAttachId: str\n        """
        self.DirectConnectId = None
        self.DirectConnectTunnelName = None
        self.DirectConnectOwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.Bandwidth = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.TencentBackupAddress = None
        self.CloudAttachId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        self.CloudAttachId = params.get("CloudAttachId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelIdSet: 专用通道ID\n        :type DirectConnectTunnelIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DirectConnectTunnelIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelIdSet = params.get("DirectConnectTunnelIdSet")
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectRequest(AbstractModel):
    """DeleteDirectConnect请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理专线的ID。\n        :type DirectConnectId: str\n        """
        self.DirectConnectId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints请求参数结构体

    """

    def __init__(self):
        """
        :param RegionId: 接入点所在的地域。使用DescribeRegions查询

您可以通过调用 DescribeRegions接口获取地域ID。\n        :type RegionId: str\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.RegionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints返回参数结构体

    """

    def __init__(self):
        """
        :param AccessPointSet: 接入点信息。\n        :type AccessPointSet: list of AccessPoint\n        :param TotalCount: 符合接入点数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AccessPointSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessPointSet") is not None:
            self.AccessPointSet = []
            for item in params.get("AccessPointSet"):
                obj = AccessPoint()
                obj._deserialize(item)
                self.AccessPointSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelExtraRequest(AbstractModel):
    """DescribeDirectConnectTunnelExtra请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectTunnelExtraResponse(AbstractModel):
    """DescribeDirectConnectTunnelExtra返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelExtra: 专用通道扩展信息\n        :type DirectConnectTunnelExtra: :class:`tencentcloud.dc.v20180410.models.DirectConnectTunnelExtra`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DirectConnectTunnelExtra = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectTunnelExtra") is not None:
            self.DirectConnectTunnelExtra = DirectConnectTunnelExtra()
            self.DirectConnectTunnelExtra._deserialize(params.get("DirectConnectTunnelExtra"))
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectTunnelsRequest(AbstractModel):
    """DescribeDirectConnectTunnels请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件:
参数不支持同时指定DirectConnectTunnelIds和Filters。
<li> direct-connect-tunnel-name, 专用通道名称。</li>
<li> direct-connect-tunnel-id, 专用通道实例ID，如dcx-abcdefgh。</li>
<li>direct-connect-id, 物理专线实例ID，如，dc-abcdefgh。</li>\n        :type Filters: list of Filter\n        :param DirectConnectTunnelIds: 专用通道 ID数组\n        :type DirectConnectTunnelIds: list of str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100\n        :type Limit: int\n        """
        self.Filters = None
        self.DirectConnectTunnelIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DirectConnectTunnelIds = params.get("DirectConnectTunnelIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelSet: 专用通道列表\n        :type DirectConnectTunnelSet: list of DirectConnectTunnel\n        :param TotalCount: 符合专用通道数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DirectConnectTunnelSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectTunnelSet") is not None:
            self.DirectConnectTunnelSet = []
            for item in params.get("DirectConnectTunnelSet"):
                obj = DirectConnectTunnel()
                obj._deserialize(item)
                self.DirectConnectTunnelSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectsRequest(AbstractModel):
    """DescribeDirectConnects请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件:\n        :type Filters: list of Filter\n        :param DirectConnectIds: 物理专线 ID数组\n        :type DirectConnectIds: list of str\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100\n        :type Limit: int\n        """
        self.Filters = None
        self.DirectConnectIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DirectConnectIds = params.get("DirectConnectIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectSet: 物理专线列表。\n        :type DirectConnectSet: list of DirectConnect\n        :param TotalCount: 符合物理专线列表数量。\n        :type TotalCount: int\n        :param AllSignLaw: 用户名下物理专线是否都签署了用户协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type AllSignLaw: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DirectConnectSet = None
        self.TotalCount = None
        self.AllSignLaw = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectSet") is not None:
            self.DirectConnectSet = []
            for item in params.get("DirectConnectSet"):
                obj = DirectConnect()
                obj._deserialize(item)
                self.DirectConnectSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.AllSignLaw = params.get("AllSignLaw")
        self.RequestId = params.get("RequestId")


class DescribeInternetAddressQuotaRequest(AbstractModel):
    """DescribeInternetAddressQuota请求参数结构体

    """


class DescribeInternetAddressQuotaResponse(AbstractModel):
    """DescribeInternetAddressQuota返回参数结构体

    """

    def __init__(self):
        """
        :param Ipv6PrefixLen: IPv6互联网公网允许的最小前缀长度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6PrefixLen: int\n        :param Ipv4BgpQuota: BGP类型IPv4互联网地址配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv4BgpQuota: int\n        :param Ipv4OtherQuota: 非BGP类型IPv4互联网地址配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv4OtherQuota: int\n        :param Ipv4BgpNum: BGP类型IPv4互联网地址已使用数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv4BgpNum: int\n        :param Ipv4OtherNum: 非BGP类型互联网地址已使用数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv4OtherNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ipv6PrefixLen = None
        self.Ipv4BgpQuota = None
        self.Ipv4OtherQuota = None
        self.Ipv4BgpNum = None
        self.Ipv4OtherNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ipv6PrefixLen = params.get("Ipv6PrefixLen")
        self.Ipv4BgpQuota = params.get("Ipv4BgpQuota")
        self.Ipv4OtherQuota = params.get("Ipv4OtherQuota")
        self.Ipv4BgpNum = params.get("Ipv4BgpNum")
        self.Ipv4OtherNum = params.get("Ipv4OtherNum")
        self.RequestId = params.get("RequestId")


class DescribeInternetAddressRequest(AbstractModel):
    """DescribeInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值100\n        :type Limit: int\n        :param Filters: 过滤条件：
<li>AddrType, 地址类型。0：BGP 1; 1: 电信， 2：移动， 3：联通</li>
<li>AddrProto地址类型。0：IPv4 1:IPv6</li>
<li>Status 地址状态。 0：使用中， 1：已停用， 2：已退还</li>
<li>Subnet 互联网公网地址，数组</li>
<InstanceIds>互联网公网地址ID，数组</li>\n        :type Filters: list of Filter\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeInternetAddressResponse(AbstractModel):
    """DescribeInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 互联网公网地址数量\n        :type TotalCount: int\n        :param Subnets: 互联网公网地址列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Subnets: list of InternetAddressDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Subnets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Subnets") is not None:
            self.Subnets = []
            for item in params.get("Subnets"):
                obj = InternetAddressDetail()
                obj._deserialize(item)
                self.Subnets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInternetAddressStatisticsRequest(AbstractModel):
    """DescribeInternetAddressStatistics请求参数结构体

    """


class DescribeInternetAddressStatisticsResponse(AbstractModel):
    """DescribeInternetAddressStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 互联网公网地址统计信息数量\n        :type TotalCount: int\n        :param InternetAddressStatistics: 互联网公网地址统计信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type InternetAddressStatistics: list of InternetAddressStatistics\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InternetAddressStatistics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InternetAddressStatistics") is not None:
            self.InternetAddressStatistics = []
            for item in params.get("InternetAddressStatistics"):
                obj = InternetAddressStatistics()
                obj._deserialize(item)
                self.InternetAddressStatistics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePublicDirectConnectTunnelRoutesRequest(AbstractModel):
    """DescribePublicDirectConnectTunnelRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        :param Filters: 过滤条件：
route-type：路由类型，取值：BGP/STATIC
route-subnet：路由cidr，取值如：192.68.1.0/24\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100\n        :type Limit: int\n        """
        self.DirectConnectTunnelId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicDirectConnectTunnelRoutesResponse(AbstractModel):
    """DescribePublicDirectConnectTunnelRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param Routes: 互联网通道路由列表\n        :type Routes: list of DirectConnectTunnelRoute\n        :param TotalCount: 记录总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Routes = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectTunnelRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DirectConnect(AbstractModel):
    """物理专线信息列表

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理专线ID。\n        :type DirectConnectId: str\n        :param DirectConnectName: 物理专线的名称。\n        :type DirectConnectName: str\n        :param AccessPointId: 物理专线的接入点ID。\n        :type AccessPointId: str\n        :param State: 物理专线的状态。
申请中：PENDING 
申请驳回：REJECTED   
待付款：TOPAY 
已付款：PAID 
建设中：ALLOCATED   
已开通：AVAILABLE  
删除中 ：DELETING
已删除：DELETED 。\n        :type State: str\n        :param CreatedTime: 物理专线创建时间。\n        :type CreatedTime: str\n        :param EnabledTime: 物理专线的开通时间。\n        :type EnabledTime: str\n        :param LineOperator: 提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。\n        :type LineOperator: str\n        :param Location: 本地数据中心的地理位置。\n        :type Location: str\n        :param Bandwidth: 物理专线接入接口带宽，单位为Mbps。\n        :type Bandwidth: int\n        :param PortType: 用户侧物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）\n        :type PortType: str\n        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CircuitCode: str\n        :param RedundantDirectConnectId: 冗余物理专线的ID。\n        :type RedundantDirectConnectId: str\n        :param Vlan: 物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vlan: int\n        :param TencentAddress: 物理专线调试腾讯侧互联IP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TencentAddress: str\n        :param CustomerAddress: 物理专线调试用户侧互联IP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomerAddress: str\n        :param CustomerName: 物理专线申请者姓名。默认从账户体系获取。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomerName: str\n        :param CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomerContactMail: str\n        :param CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomerContactNumber: str\n        :param ExpiredTime: 物理专线的过期时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpiredTime: str\n        :param ChargeType: 物理专线计费类型。 NON_RECURRING_CHARGE：一次性接入费用；PREPAID_BY_YEAR：按年预付费。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChargeType: str\n        :param FaultReportContactPerson: 报障联系人。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FaultReportContactPerson: str\n        :param FaultReportContactNumber: 报障联系电话。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FaultReportContactNumber: str\n        :param TagSet: 标签键值对
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        :param AccessPointType: 物理专线的接入点类型。\n        :type AccessPointType: str\n        :param IdcCity: IDC所在城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type IdcCity: str\n        :param ChargeState: 计费状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type ChargeState: str\n        :param StartTime: 物理专线开通时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTime: str\n        :param SignLaw: 物理专线是否已签署用户协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type SignLaw: bool\n        :param LocalZone: 物理专线是否为LocalZone
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocalZone: bool\n        :param VlanZeroDirectConnectTunnelCount: 该物理专线下vlan 0的专用通道数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type VlanZeroDirectConnectTunnelCount: int\n        :param OtherVlanDirectConnectTunnelCount: 该物理专线下非vlan 0的专用通道数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type OtherVlanDirectConnectTunnelCount: int\n        :param MinBandwidth: 物理专线最小带宽
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinBandwidth: int\n        """
        self.DirectConnectId = None
        self.DirectConnectName = None
        self.AccessPointId = None
        self.State = None
        self.CreatedTime = None
        self.EnabledTime = None
        self.LineOperator = None
        self.Location = None
        self.Bandwidth = None
        self.PortType = None
        self.CircuitCode = None
        self.RedundantDirectConnectId = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.ExpiredTime = None
        self.ChargeType = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.TagSet = None
        self.AccessPointType = None
        self.IdcCity = None
        self.ChargeState = None
        self.StartTime = None
        self.SignLaw = None
        self.LocalZone = None
        self.VlanZeroDirectConnectTunnelCount = None
        self.OtherVlanDirectConnectTunnelCount = None
        self.MinBandwidth = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.EnabledTime = params.get("EnabledTime")
        self.LineOperator = params.get("LineOperator")
        self.Location = params.get("Location")
        self.Bandwidth = params.get("Bandwidth")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
        self.RedundantDirectConnectId = params.get("RedundantDirectConnectId")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.ExpiredTime = params.get("ExpiredTime")
        self.ChargeType = params.get("ChargeType")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.AccessPointType = params.get("AccessPointType")
        self.IdcCity = params.get("IdcCity")
        self.ChargeState = params.get("ChargeState")
        self.StartTime = params.get("StartTime")
        self.SignLaw = params.get("SignLaw")
        self.LocalZone = params.get("LocalZone")
        self.VlanZeroDirectConnectTunnelCount = params.get("VlanZeroDirectConnectTunnelCount")
        self.OtherVlanDirectConnectTunnelCount = params.get("OtherVlanDirectConnectTunnelCount")
        self.MinBandwidth = params.get("MinBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnel(AbstractModel):
    """专用通道信息列表

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        :param DirectConnectId: 物理专线ID\n        :type DirectConnectId: str\n        :param State: 专用通道状态
AVAILABLE:就绪或者已连接
PENDING:申请中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒绝\n        :type State: str\n        :param DirectConnectOwnerAccount: 物理专线的拥有者，开发商账号 ID\n        :type DirectConnectOwnerAccount: str\n        :param OwnerAccount: 专用通道的拥有者，开发商账号 ID\n        :type OwnerAccount: str\n        :param NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网\n        :type NetworkType: str\n        :param NetworkRegion: VPC地域对应的网络名，如ap-guangzhou\n        :type NetworkRegion: str\n        :param VpcId: 私有网络统一 ID 或者黑石网络统一 ID\n        :type VpcId: str\n        :param DirectConnectGatewayId: 专线网关 ID\n        :type DirectConnectGatewayId: str\n        :param RouteType: BGP ：BGP路由 STATIC：静态 默认为 BGP 路由\n        :type RouteType: str\n        :param BgpPeer: 用户侧BGP，Asn，AuthKey\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: 用户侧网段地址\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param Vlan: 专用通道的Vlan\n        :type Vlan: int\n        :param TencentAddress: TencentAddress，腾讯侧互联 IP\n        :type TencentAddress: str\n        :param CustomerAddress: CustomerAddress，用户侧互联 IP\n        :type CustomerAddress: str\n        :param DirectConnectTunnelName: 专用通道名称\n        :type DirectConnectTunnelName: str\n        :param CreatedTime: 专用通道创建时间\n        :type CreatedTime: str\n        :param Bandwidth: 专用通道带宽值\n        :type Bandwidth: int\n        :param TagSet: 专用通道标签值\n        :type TagSet: list of Tag\n        :param NetDetectId: 关联的网络自定义探测ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetDetectId: str\n        :param EnableBGPCommunity: BGP community开关
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableBGPCommunity: bool\n        :param NatType: 是否为Nat通道
注意：此字段可能返回 null，表示取不到有效值。\n        :type NatType: int\n        :param VpcRegion: VPC地域简码，如gz、cd
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcRegion: str\n        :param BfdEnable: 是否开启BFD
注意：此字段可能返回 null，表示取不到有效值。\n        :type BfdEnable: int\n        :param AccessPointType: 专用通道接入点类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessPointType: str\n        :param DirectConnectGatewayName: 专线网关名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type DirectConnectGatewayName: str\n        :param VpcName: VPC名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcName: str\n        :param TencentBackupAddress: TencentBackupAddress，腾讯侧备用互联 IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type TencentBackupAddress: str\n        :param SignLaw: 专用通道关联的物理专线是否签署了用户协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type SignLaw: bool\n        :param CloudAttachId: 高速上云服务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type CloudAttachId: str\n        """
        self.DirectConnectTunnelId = None
        self.DirectConnectId = None
        self.State = None
        self.DirectConnectOwnerAccount = None
        self.OwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.DirectConnectTunnelName = None
        self.CreatedTime = None
        self.Bandwidth = None
        self.TagSet = None
        self.NetDetectId = None
        self.EnableBGPCommunity = None
        self.NatType = None
        self.VpcRegion = None
        self.BfdEnable = None
        self.AccessPointType = None
        self.DirectConnectGatewayName = None
        self.VpcName = None
        self.TencentBackupAddress = None
        self.SignLaw = None
        self.CloudAttachId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectId = params.get("DirectConnectId")
        self.State = params.get("State")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.OwnerAccount = params.get("OwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.CreatedTime = params.get("CreatedTime")
        self.Bandwidth = params.get("Bandwidth")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.NetDetectId = params.get("NetDetectId")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.NatType = params.get("NatType")
        self.VpcRegion = params.get("VpcRegion")
        self.BfdEnable = params.get("BfdEnable")
        self.AccessPointType = params.get("AccessPointType")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcName = params.get("VpcName")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        self.SignLaw = params.get("SignLaw")
        self.CloudAttachId = params.get("CloudAttachId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnelExtra(AbstractModel):
    """专用通道扩展信息

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        :param DirectConnectId: 物理专线ID\n        :type DirectConnectId: str\n        :param State: 专用通道状态
AVAILABLE:就绪或者已连接
PENDING:申请中
ALLOCATING:配置中
ALLOCATED:配置完成
ALTERING:修改中
DELETING:删除中
DELETED:删除完成
COMFIRMING:待接受
REJECTED:拒绝\n        :type State: str\n        :param DirectConnectOwnerAccount: 物理专线的拥有者，开发商账号 ID\n        :type DirectConnectOwnerAccount: str\n        :param OwnerAccount: 专用通道的拥有者，开发商账号 ID\n        :type OwnerAccount: str\n        :param NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网\n        :type NetworkType: str\n        :param NetworkRegion: VPC地域对应的网络名，如ap-guangzhou\n        :type NetworkRegion: str\n        :param VpcId: 私有网络统一 ID 或者黑石网络统一 ID\n        :type VpcId: str\n        :param DirectConnectGatewayId: 专线网关 ID\n        :type DirectConnectGatewayId: str\n        :param RouteType: BGP ：BGP路由 STATIC：静态 默认为 BGP 路由\n        :type RouteType: str\n        :param BgpPeer: 用户侧BGP，Asn，AuthKey\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: 用户侧网段地址\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param PublicAddresses: 互联网通道公网网段地址\n        :type PublicAddresses: list of RouteFilterPrefix\n        :param Vlan: 专用通道的Vlan\n        :type Vlan: int\n        :param TencentAddress: 腾讯侧互联 IP\n        :type TencentAddress: str\n        :param TencentBackupAddress: 腾讯侧备用互联IP\n        :type TencentBackupAddress: str\n        :param CustomerAddress: 用户侧互联 IP\n        :type CustomerAddress: str\n        :param DirectConnectTunnelName: 专用通道名称\n        :type DirectConnectTunnelName: str\n        :param CreatedTime: 专用通道创建时间\n        :type CreatedTime: str\n        :param Bandwidth: 专用通道带宽值\n        :type Bandwidth: int\n        :param NetDetectId: 关联的网络自定义探测ID\n        :type NetDetectId: str\n        :param EnableBGPCommunity: BGP community开关\n        :type EnableBGPCommunity: bool\n        :param NatType: 是否为Nat通道\n        :type NatType: int\n        :param VpcRegion: VPC地域简码，如gz、cd\n        :type VpcRegion: str\n        :param BfdEnable: 是否开启BFD\n        :type BfdEnable: int\n        :param NqaEnable: 是否开启NQA\n        :type NqaEnable: int\n        :param AccessPointType: 专用通道接入点类型\n        :type AccessPointType: str\n        :param DirectConnectGatewayName: 专线网关名称\n        :type DirectConnectGatewayName: str\n        :param VpcName: VPC名称\n        :type VpcName: str\n        :param SignLaw: 专用通道关联的物理专线是否签署了用户协议\n        :type SignLaw: bool\n        :param BfdInfo: BFD配置信息\n        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`\n        :param NqaInfo: NQA配置信息\n        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`\n        :param BgpStatus: BGP状态\n        :type BgpStatus: :class:`tencentcloud.dc.v20180410.models.BGPStatus`\n        :param IPv6Enable: 是否开启IPv6
注意：此字段可能返回 null，表示取不到有效值。\n        :type IPv6Enable: int\n        :param TencentIPv6Address: 腾讯侧互联IPv6地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type TencentIPv6Address: str\n        :param TencentBackupIPv6Address: 腾讯侧备用互联IPv6地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type TencentBackupIPv6Address: str\n        :param BgpIPv6Status: BGPv6状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type BgpIPv6Status: :class:`tencentcloud.dc.v20180410.models.BGPStatus`\n        :param CustomerIPv6Address: 用户侧互联IPv6地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type CustomerIPv6Address: str\n        :param JumboEnable: 专用通道是否支持巨帧。1 支持，0 不支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type JumboEnable: int\n        """
        self.DirectConnectTunnelId = None
        self.DirectConnectId = None
        self.State = None
        self.DirectConnectOwnerAccount = None
        self.OwnerAccount = None
        self.NetworkType = None
        self.NetworkRegion = None
        self.VpcId = None
        self.DirectConnectGatewayId = None
        self.RouteType = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.PublicAddresses = None
        self.Vlan = None
        self.TencentAddress = None
        self.TencentBackupAddress = None
        self.CustomerAddress = None
        self.DirectConnectTunnelName = None
        self.CreatedTime = None
        self.Bandwidth = None
        self.NetDetectId = None
        self.EnableBGPCommunity = None
        self.NatType = None
        self.VpcRegion = None
        self.BfdEnable = None
        self.NqaEnable = None
        self.AccessPointType = None
        self.DirectConnectGatewayName = None
        self.VpcName = None
        self.SignLaw = None
        self.BfdInfo = None
        self.NqaInfo = None
        self.BgpStatus = None
        self.IPv6Enable = None
        self.TencentIPv6Address = None
        self.TencentBackupIPv6Address = None
        self.BgpIPv6Status = None
        self.CustomerIPv6Address = None
        self.JumboEnable = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectId = params.get("DirectConnectId")
        self.State = params.get("State")
        self.DirectConnectOwnerAccount = params.get("DirectConnectOwnerAccount")
        self.OwnerAccount = params.get("OwnerAccount")
        self.NetworkType = params.get("NetworkType")
        self.NetworkRegion = params.get("NetworkRegion")
        self.VpcId = params.get("VpcId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteType = params.get("RouteType")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        if params.get("PublicAddresses") is not None:
            self.PublicAddresses = []
            for item in params.get("PublicAddresses"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.PublicAddresses.append(obj)
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        self.CreatedTime = params.get("CreatedTime")
        self.Bandwidth = params.get("Bandwidth")
        self.NetDetectId = params.get("NetDetectId")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.NatType = params.get("NatType")
        self.VpcRegion = params.get("VpcRegion")
        self.BfdEnable = params.get("BfdEnable")
        self.NqaEnable = params.get("NqaEnable")
        self.AccessPointType = params.get("AccessPointType")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcName = params.get("VpcName")
        self.SignLaw = params.get("SignLaw")
        if params.get("BfdInfo") is not None:
            self.BfdInfo = BFDInfo()
            self.BfdInfo._deserialize(params.get("BfdInfo"))
        if params.get("NqaInfo") is not None:
            self.NqaInfo = NQAInfo()
            self.NqaInfo._deserialize(params.get("NqaInfo"))
        if params.get("BgpStatus") is not None:
            self.BgpStatus = BGPStatus()
            self.BgpStatus._deserialize(params.get("BgpStatus"))
        self.IPv6Enable = params.get("IPv6Enable")
        self.TencentIPv6Address = params.get("TencentIPv6Address")
        self.TencentBackupIPv6Address = params.get("TencentBackupIPv6Address")
        if params.get("BgpIPv6Status") is not None:
            self.BgpIPv6Status = BGPStatus()
            self.BgpIPv6Status._deserialize(params.get("BgpIPv6Status"))
        self.CustomerIPv6Address = params.get("CustomerIPv6Address")
        self.JumboEnable = params.get("JumboEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectTunnelRoute(AbstractModel):
    """专用通道路由

    """

    def __init__(self):
        """
        :param RouteId: 专用通道路由ID\n        :type RouteId: str\n        :param DestinationCidrBlock: 网段CIDR\n        :type DestinationCidrBlock: str\n        :param RouteType: 路由类型：BGP/STATIC路由\n        :type RouteType: str\n        :param Status: ENABLE：路由启用，DISABLE：路由禁用\n        :type Status: str\n        :param ASPath: ASPath信息\n        :type ASPath: list of str\n        :param NextHop: 路由下一跳IP\n        :type NextHop: str\n        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.RouteType = None
        self.Status = None
        self.ASPath = None
        self.NextHop = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.RouteType = params.get("RouteType")
        self.Status = params.get("Status")
        self.ASPath = params.get("ASPath")
        self.NextHop = params.get("NextHop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInternetAddressRequest(AbstractModel):
    """DisableInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 公网互联网地址ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInternetAddressResponse(AbstractModel):
    """DisableInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableInternetAddressRequest(AbstractModel):
    """EnableInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 互联网公网地址ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableInternetAddressResponse(AbstractModel):
    """EnableInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """用于条件过滤查询

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。\n        :type Name: str\n        :param Values: 字段的过滤值。\n        :type Values: list of str\n        """
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
        


class InternetAddressDetail(AbstractModel):
    """互联网地址详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 互联网地址ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param Subnet: 互联网网络地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Subnet: str\n        :param MaskLen: 网络地址掩码长度
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaskLen: int\n        :param AddrType: 0:BGP
1:电信
2:移动
3:联通
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddrType: int\n        :param Status: 0:使用中
1:已停用
2:已退还\n        :type Status: int\n        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApplyTime: str\n        :param StopTime: 停用时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StopTime: str\n        :param ReleaseTime: 退还时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseTime: str\n        :param Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type AppId: int\n        :param AddrProto: 0:IPv4 1:IPv6
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddrProto: int\n        :param ReserveTime: 释放状态的IP地址保留的天数
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReserveTime: int\n        """
        self.InstanceId = None
        self.Subnet = None
        self.MaskLen = None
        self.AddrType = None
        self.Status = None
        self.ApplyTime = None
        self.StopTime = None
        self.ReleaseTime = None
        self.Region = None
        self.AppId = None
        self.AddrProto = None
        self.ReserveTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Subnet = params.get("Subnet")
        self.MaskLen = params.get("MaskLen")
        self.AddrType = params.get("AddrType")
        self.Status = params.get("Status")
        self.ApplyTime = params.get("ApplyTime")
        self.StopTime = params.get("StopTime")
        self.ReleaseTime = params.get("ReleaseTime")
        self.Region = params.get("Region")
        self.AppId = params.get("AppId")
        self.AddrProto = params.get("AddrProto")
        self.ReserveTime = params.get("ReserveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAddressStatistics(AbstractModel):
    """互联网公网地址统计

    """

    def __init__(self):
        """
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param SubnetNum: 互联网公网地址数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetNum: int\n        """
        self.Region = None
        self.SubnetNum = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.SubnetNum = params.get("SubnetNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理专线的ID。\n        :type DirectConnectId: str\n        :param DirectConnectName: 物理专线名称。\n        :type DirectConnectName: str\n        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。\n        :type CircuitCode: str\n        :param Vlan: 物理专线调试VLAN。\n        :type Vlan: int\n        :param TencentAddress: 物理专线调试腾讯侧互联 IP。\n        :type TencentAddress: str\n        :param CustomerAddress: 物理专线调试用户侧互联 IP。\n        :type CustomerAddress: str\n        :param CustomerName: 物理专线申请者姓名。默认从账户体系获取。\n        :type CustomerName: str\n        :param CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。\n        :type CustomerContactMail: str\n        :param CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。\n        :type CustomerContactNumber: str\n        :param FaultReportContactPerson: 报障联系人。\n        :type FaultReportContactPerson: str\n        :param FaultReportContactNumber: 报障联系电话。\n        :type FaultReportContactNumber: str\n        :param SignLaw: 物理专线申请者补签用户使用协议\n        :type SignLaw: bool\n        :param Bandwidth: 物理专线带宽\n        :type Bandwidth: int\n        """
        self.DirectConnectId = None
        self.DirectConnectName = None
        self.CircuitCode = None
        self.Vlan = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.CustomerName = None
        self.CustomerContactMail = None
        self.CustomerContactNumber = None
        self.FaultReportContactPerson = None
        self.FaultReportContactNumber = None
        self.SignLaw = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")
        self.DirectConnectName = params.get("DirectConnectName")
        self.CircuitCode = params.get("CircuitCode")
        self.Vlan = params.get("Vlan")
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.CustomerName = params.get("CustomerName")
        self.CustomerContactMail = params.get("CustomerContactMail")
        self.CustomerContactNumber = params.get("CustomerContactNumber")
        self.FaultReportContactPerson = params.get("FaultReportContactPerson")
        self.FaultReportContactNumber = params.get("FaultReportContactNumber")
        self.SignLaw = params.get("SignLaw")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        :param DirectConnectTunnelName: 专用通道名称\n        :type DirectConnectTunnelName: str\n        :param BgpPeer: 用户侧BGP，包括Asn，AuthKey\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: 用户侧网段地址\n        :type RouteFilterPrefixes: list of RouteFilterPrefix\n        :param TencentAddress: 腾讯侧互联IP\n        :type TencentAddress: str\n        :param CustomerAddress: 用户侧互联IP\n        :type CustomerAddress: str\n        :param Bandwidth: 专用通道带宽值，单位为M。\n        :type Bandwidth: int\n        :param TencentBackupAddress: 腾讯侧备用互联IP\n        :type TencentBackupAddress: str\n        """
        self.DirectConnectTunnelId = None
        self.DirectConnectTunnelName = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.Bandwidth = None
        self.TencentBackupAddress = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.DirectConnectTunnelName = params.get("DirectConnectTunnelName")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = []
            for item in params.get("RouteFilterPrefixes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.RouteFilterPrefixes.append(obj)
        self.TencentAddress = params.get("TencentAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelExtraRequest(AbstractModel):
    """ModifyDirectConnectTunnelExtra请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID\n        :type DirectConnectTunnelId: str\n        :param Vlan: 专用通道的Vlan\n        :type Vlan: int\n        :param BgpPeer: 用户侧BGP，Asn，AuthKey\n        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`\n        :param RouteFilterPrefixes: 用户侧过滤网段地址\n        :type RouteFilterPrefixes: :class:`tencentcloud.dc.v20180410.models.RouteFilterPrefix`\n        :param TencentAddress: 腾讯侧互联IP\n        :type TencentAddress: str\n        :param TencentBackupAddress: 腾讯侧备用互联IP\n        :type TencentBackupAddress: str\n        :param CustomerAddress: 用户侧互联IP\n        :type CustomerAddress: str\n        :param Bandwidth: 专用通道带宽值\n        :type Bandwidth: int\n        :param EnableBGPCommunity: BGP community开关\n        :type EnableBGPCommunity: bool\n        :param BfdEnable: 是否开启BFD\n        :type BfdEnable: int\n        :param NqaEnable: 是否开启NQA\n        :type NqaEnable: int\n        :param BfdInfo: BFD配置信息\n        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`\n        :param NqaInfo: NQA配置信息\n        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`\n        :param IPv6Enable: 0：停用IPv6
1: 启用IPv6\n        :type IPv6Enable: int\n        :param CustomerIDCRoutes: 去往用户侧的路由信息\n        :type CustomerIDCRoutes: list of RouteFilterPrefix\n        :param JumboEnable: 是否开启巨帧
1：开启
0：不开启\n        :type JumboEnable: int\n        """
        self.DirectConnectTunnelId = None
        self.Vlan = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.TencentAddress = None
        self.TencentBackupAddress = None
        self.CustomerAddress = None
        self.Bandwidth = None
        self.EnableBGPCommunity = None
        self.BfdEnable = None
        self.NqaEnable = None
        self.BfdInfo = None
        self.NqaInfo = None
        self.IPv6Enable = None
        self.CustomerIDCRoutes = None
        self.JumboEnable = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        self.Vlan = params.get("Vlan")
        if params.get("BgpPeer") is not None:
            self.BgpPeer = BgpPeer()
            self.BgpPeer._deserialize(params.get("BgpPeer"))
        if params.get("RouteFilterPrefixes") is not None:
            self.RouteFilterPrefixes = RouteFilterPrefix()
            self.RouteFilterPrefixes._deserialize(params.get("RouteFilterPrefixes"))
        self.TencentAddress = params.get("TencentAddress")
        self.TencentBackupAddress = params.get("TencentBackupAddress")
        self.CustomerAddress = params.get("CustomerAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.BfdEnable = params.get("BfdEnable")
        self.NqaEnable = params.get("NqaEnable")
        if params.get("BfdInfo") is not None:
            self.BfdInfo = BFDInfo()
            self.BfdInfo._deserialize(params.get("BfdInfo"))
        if params.get("NqaInfo") is not None:
            self.NqaInfo = NQAInfo()
            self.NqaInfo._deserialize(params.get("NqaInfo"))
        self.IPv6Enable = params.get("IPv6Enable")
        if params.get("CustomerIDCRoutes") is not None:
            self.CustomerIDCRoutes = []
            for item in params.get("CustomerIDCRoutes"):
                obj = RouteFilterPrefix()
                obj._deserialize(item)
                self.CustomerIDCRoutes.append(obj)
        self.JumboEnable = params.get("JumboEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectTunnelExtraResponse(AbstractModel):
    """ModifyDirectConnectTunnelExtra返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NQAInfo(AbstractModel):
    """nqa配置信息

    """

    def __init__(self):
        """
        :param ProbeFailedTimes: 健康检查次数\n        :type ProbeFailedTimes: int\n        :param Interval: 健康检查间隔\n        :type Interval: int\n        :param DestinationIp: 健康检查地址\n        :type DestinationIp: str\n        """
        self.ProbeFailedTimes = None
        self.Interval = None
        self.DestinationIp = None


    def _deserialize(self, params):
        self.ProbeFailedTimes = params.get("ProbeFailedTimes")
        self.Interval = params.get("Interval")
        self.DestinationIp = params.get("DestinationIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 无\n        :type DirectConnectTunnelId: str\n        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseInternetAddressRequest(AbstractModel):
    """ReleaseInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 公网互联网地址ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseInternetAddressResponse(AbstractModel):
    """ReleaseInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RouteFilterPrefix(AbstractModel):
    """用户侧网段地址

    """

    def __init__(self):
        """
        :param Cidr: 用户侧网段地址\n        :type Cidr: str\n        """
        self.Cidr = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        """
        :param Key: 标签键
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        