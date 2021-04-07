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

from tencentcloud.common.abstract_model import AbstractModel


class AcceptDirectConnectTunnelRequest(AbstractModel):
    """AcceptDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 物理专线拥有者接受共享专用通道申请
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class AcceptDirectConnectTunnelResponse(AbstractModel):
    """AcceptDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccessPoint(AbstractModel):
    """接入点信息。

    """

    def __init__(self):
        """
        :param AccessPointName: 接入点的名称。
        :type AccessPointName: str
        :param AccessPointId: 接入点唯一ID。
        :type AccessPointId: str
        :param State: 接入点的状态。可用，不可用。
        :type State: str
        :param Location: 接入点的位置。
        :type Location: str
        :param LineOperator: 接入点支持的运营商列表。
        :type LineOperator: list of str
        :param RegionId: 接入点管理的大区ID。
        :type RegionId: str
        :param AvailablePortType: 接入点可用的端口类型列表。1000BASE-T代表千兆电口，1000BASE-LX代表千兆单模光口10km，1000BASE-ZX代表千兆单模光口80km,10GBASE-LR代表万兆单模光口10km,10GBASE-ZR代表万兆单模光口80km,10GBASE-LH代表万兆单模光口40km,100GBASE-LR4代表100G单模光口10km
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailablePortType: list of str
        :param Coordinate: 接入点经纬度
注意：此字段可能返回 null，表示取不到有效值。
        :type Coordinate: :class:`tencentcloud.dc.v20180410.models.Coordinate`
        :param City: 接入点所在城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        :param Area: 接入点地域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
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


class ApplyInternetAddressRequest(AbstractModel):
    """ApplyInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param MaskLen: CIDR地址掩码长度
        :type MaskLen: int
        :param AddrType: 0:BGP类型地址
1：中国电信
2：中国移动
3：中国联通
        :type AddrType: int
        :param AddrProto: 0：IPv4
1:IPv6
        :type AddrProto: int
        """
        self.MaskLen = None
        self.AddrType = None
        self.AddrProto = None


    def _deserialize(self, params):
        self.MaskLen = params.get("MaskLen")
        self.AddrType = params.get("AddrType")
        self.AddrProto = params.get("AddrProto")


class ApplyInternetAddressResponse(AbstractModel):
    """ApplyInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 互联网公网地址ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param ProbeFailedTimes: 健康检查次数
        :type ProbeFailedTimes: int
        :param Interval: 健康检查间隔
        :type Interval: int
        """
        self.ProbeFailedTimes = None
        self.Interval = None


    def _deserialize(self, params):
        self.ProbeFailedTimes = params.get("ProbeFailedTimes")
        self.Interval = params.get("Interval")


class BGPStatus(AbstractModel):
    """bgp状态信息

    """

    def __init__(self):
        """
        :param TencentAddressBgpState: 腾讯侧主互联IP BGP状态
        :type TencentAddressBgpState: str
        :param TencentBackupAddressBgpState: 腾讯侧备互联IP BGP状态
        :type TencentBackupAddressBgpState: str
        """
        self.TencentAddressBgpState = None
        self.TencentBackupAddressBgpState = None


    def _deserialize(self, params):
        self.TencentAddressBgpState = params.get("TencentAddressBgpState")
        self.TencentBackupAddressBgpState = params.get("TencentBackupAddressBgpState")


class BgpPeer(AbstractModel):
    """bgp参数，包括Asn，AuthKey

    """

    def __init__(self):
        """
        :param Asn: 用户侧，BGP Asn
        :type Asn: int
        :param AuthKey: 用户侧BGP密钥
        :type AuthKey: str
        """
        self.Asn = None
        self.AuthKey = None


    def _deserialize(self, params):
        self.Asn = params.get("Asn")
        self.AuthKey = params.get("AuthKey")


class Coordinate(AbstractModel):
    """坐标，经维度描述

    """

    def __init__(self):
        """
        :param Lat: 纬度
        :type Lat: float
        :param Lng: 经度
        :type Lng: float
        """
        self.Lat = None
        self.Lng = None


    def _deserialize(self, params):
        self.Lat = params.get("Lat")
        self.Lng = params.get("Lng")


class CreateDirectConnectRequest(AbstractModel):
    """CreateDirectConnect请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectName: 物理专线的名称。
        :type DirectConnectName: str
        :param AccessPointId: 物理专线所在的接入点。
您可以通过调用 DescribeAccessPoints接口获取地域ID。所选择的接入点必须存在且处于可接入的状态。
        :type AccessPointId: str
        :param LineOperator: 提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。
        :type LineOperator: str
        :param PortType: 物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）。
        :type PortType: str
        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
        :type CircuitCode: str
        :param Location: 本地数据中心的地理位置。
        :type Location: str
        :param Bandwidth: 物理专线接入接口带宽，单位为Mbps，默认值为1000，取值范围为 [2, 10240]。
        :type Bandwidth: int
        :param RedundantDirectConnectId: 冗余物理专线的ID。
        :type RedundantDirectConnectId: str
        :param Vlan: 物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
        :type Vlan: int
        :param TencentAddress: 物理专线调试腾讯侧互联 IP。默认自动分配。
        :type TencentAddress: str
        :param CustomerAddress: 物理专线调试用户侧互联 IP。默认自动分配。
        :type CustomerAddress: str
        :param CustomerName: 物理专线申请者姓名。默认从账户体系获取。
        :type CustomerName: str
        :param CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
        :type CustomerContactMail: str
        :param CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
        :type CustomerContactNumber: str
        :param FaultReportContactPerson: 报障联系人。
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: 报障联系电话。
        :type FaultReportContactNumber: str
        :param SignLaw: 物理专线申请者是否签署了用户使用协议。默认已签署
        :type SignLaw: bool
        """
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


class CreateDirectConnectResponse(AbstractModel):
    """CreateDirectConnect返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectIdSet: 物理专线的ID。
        :type DirectConnectIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DirectConnectId: 专线 ID，例如：dc-kd7d06of
        :type DirectConnectId: str
        :param DirectConnectTunnelName: 专用通道名称
        :type DirectConnectTunnelName: str
        :param DirectConnectOwnerAccount: 物理专线 owner，缺省为当前客户（物理专线 owner）
共享专线时这里需要填写共享专线的开发商账号 ID
        :type DirectConnectOwnerAccount: str
        :param NetworkType: 网络类型，分别为VPC、BMVPC，CCN，默认是VPC
VPC：私有网络
BMVPC：黑石网络
CCN：云联网
        :type NetworkType: str
        :param NetworkRegion: 网络地域
        :type NetworkRegion: str
        :param VpcId: 私有网络统一 ID 或者黑石网络统一 ID
        :type VpcId: str
        :param DirectConnectGatewayId: 专线网关 ID，例如 dcg-d545ddf
        :type DirectConnectGatewayId: str
        :param Bandwidth: 专线带宽，单位：Mbps
默认是物理专线带宽值
        :type Bandwidth: int
        :param RouteType: BGP ：BGP路由
STATIC：静态
默认为 BGP 路由
        :type RouteType: str
        :param BgpPeer: BgpPeer，用户侧bgp信息，包括Asn和AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 静态路由，用户IDC的网段地址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param Vlan: vlan，范围：0 ~ 3000
0：不开启子接口
默认值是非0
        :type Vlan: int
        :param TencentAddress: TencentAddress，腾讯侧互联 IP
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress，用户侧互联 IP
        :type CustomerAddress: str
        :param TencentBackupAddress: TencentBackupAddress，腾讯侧备用互联 IP
        :type TencentBackupAddress: str
        :param CloudAttachId: 高速上云服务ID
        :type CloudAttachId: str
        """
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


class CreateDirectConnectTunnelResponse(AbstractModel):
    """CreateDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelIdSet: 专用通道ID
        :type DirectConnectTunnelIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DirectConnectId: 物理专线的ID。
        :type DirectConnectId: str
        """
        self.DirectConnectId = None


    def _deserialize(self, params):
        self.DirectConnectId = params.get("DirectConnectId")


class DeleteDirectConnectResponse(AbstractModel):
    """DeleteDirectConnect返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectTunnelRequest(AbstractModel):
    """DeleteDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class DeleteDirectConnectTunnelResponse(AbstractModel):
    """DeleteDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessPointsRequest(AbstractModel):
    """DescribeAccessPoints请求参数结构体

    """

    def __init__(self):
        """
        :param RegionId: 接入点所在的地域。使用DescribeRegions查询

您可以通过调用 DescribeRegions接口获取地域ID。
        :type RegionId: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self.RegionId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAccessPointsResponse(AbstractModel):
    """DescribeAccessPoints返回参数结构体

    """

    def __init__(self):
        """
        :param AccessPointSet: 接入点信息。
        :type AccessPointSet: list of AccessPoint
        :param TotalCount: 符合接入点数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class DescribeDirectConnectTunnelExtraResponse(AbstractModel):
    """DescribeDirectConnectTunnelExtra返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelExtra: 专用通道扩展信息
        :type DirectConnectTunnelExtra: :class:`tencentcloud.dc.v20180410.models.DirectConnectTunnelExtra`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
<li>direct-connect-id, 物理专线实例ID，如，dc-abcdefgh。</li>
        :type Filters: list of Filter
        :param DirectConnectTunnelIds: 专用通道 ID数组
        :type DirectConnectTunnelIds: list of str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        """
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


class DescribeDirectConnectTunnelsResponse(AbstractModel):
    """DescribeDirectConnectTunnels返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelSet: 专用通道列表
        :type DirectConnectTunnelSet: list of DirectConnectTunnel
        :param TotalCount: 符合专用通道数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Filters: 过滤条件:
        :type Filters: list of Filter
        :param DirectConnectIds: 物理专线 ID数组
        :type DirectConnectIds: list of str
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        """
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


class DescribeDirectConnectsResponse(AbstractModel):
    """DescribeDirectConnects返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectSet: 物理专线列表。
        :type DirectConnectSet: list of DirectConnect
        :param TotalCount: 符合物理专线列表数量。
        :type TotalCount: int
        :param AllSignLaw: 用户名下物理专线是否都签署了用户协议
注意：此字段可能返回 null，表示取不到有效值。
        :type AllSignLaw: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6PrefixLen: int
        :param Ipv4BgpQuota: BGP类型IPv4互联网地址配额
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv4BgpQuota: int
        :param Ipv4OtherQuota: 非BGP类型IPv4互联网地址配额
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv4OtherQuota: int
        :param Ipv4BgpNum: BGP类型IPv4互联网地址已使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv4BgpNum: int
        :param Ipv4OtherNum: 非BGP类型互联网地址已使用数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv4OtherNum: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值100
        :type Limit: int
        :param Filters: 过滤条件：
<li>AddrType, 地址类型。0：BGP 1; 1: 电信， 2：移动， 3：联通</li>
<li>AddrProto地址类型。0：IPv4 1:IPv6</li>
<li>Status 地址状态。 0：使用中， 1：已停用， 2：已退还</li>
<li>Subnet 互联网公网地址，数组</li>
<InstanceIds>互联网公网地址ID，数组</li>
        :type Filters: list of Filter
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
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeInternetAddressResponse(AbstractModel):
    """DescribeInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 互联网公网地址数量
        :type TotalCount: int
        :param Subnets: 互联网公网地址列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Subnets: list of InternetAddressDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param TotalCount: 互联网公网地址统计信息数量
        :type TotalCount: int
        :param InternetAddressStatistics: 互联网公网地址统计信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAddressStatistics: list of InternetAddressStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param Filters: 过滤条件：
route-type：路由类型，取值：BGP/STATIC
route-subnet：路由cidr，取值如：192.68.1.0/24
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        """
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


class DescribePublicDirectConnectTunnelRoutesResponse(AbstractModel):
    """DescribePublicDirectConnectTunnelRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param Routes: 互联网通道路由列表
        :type Routes: list of DirectConnectTunnelRoute
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param DirectConnectId: 物理专线ID。
        :type DirectConnectId: str
        :param DirectConnectName: 物理专线的名称。
        :type DirectConnectName: str
        :param AccessPointId: 物理专线的接入点ID。
        :type AccessPointId: str
        :param State: 物理专线的状态。
申请中：PENDING 
申请驳回：REJECTED   
待付款：TOPAY 
已付款：PAID 
建设中：ALLOCATED   
已开通：AVAILABLE  
删除中 ：DELETING
已删除：DELETED 。
        :type State: str
        :param CreatedTime: 物理专线创建时间。
        :type CreatedTime: str
        :param EnabledTime: 物理专线的开通时间。
        :type EnabledTime: str
        :param LineOperator: 提供接入物理专线的运营商。ChinaTelecom：中国电信， ChinaMobile：中国移动，ChinaUnicom：中国联通， In-houseWiring：楼内线，ChinaOther：中国其他， InternationalOperator：境外其他。
        :type LineOperator: str
        :param Location: 本地数据中心的地理位置。
        :type Location: str
        :param Bandwidth: 物理专线接入接口带宽，单位为Mbps。
        :type Bandwidth: int
        :param PortType: 用户侧物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）
        :type PortType: str
        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type CircuitCode: str
        :param RedundantDirectConnectId: 冗余物理专线的ID。
        :type RedundantDirectConnectId: str
        :param Vlan: 物理专线调试VLAN。默认开启VLAN，自动分配VLAN。
注意：此字段可能返回 null，表示取不到有效值。
        :type Vlan: int
        :param TencentAddress: 物理专线调试腾讯侧互联IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type TencentAddress: str
        :param CustomerAddress: 物理专线调试用户侧互联IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerAddress: str
        :param CustomerName: 物理专线申请者姓名。默认从账户体系获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerName: str
        :param CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerContactMail: str
        :param CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerContactNumber: str
        :param ExpiredTime: 物理专线的过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param ChargeType: 物理专线计费类型。 NON_RECURRING_CHARGE：一次性接入费用；PREPAID_BY_YEAR：按年预付费。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param FaultReportContactPerson: 报障联系人。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: 报障联系电话。
注意：此字段可能返回 null，表示取不到有效值。
        :type FaultReportContactNumber: str
        :param TagSet: 标签键值对
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of Tag
        :param AccessPointType: 物理专线的接入点类型。
        :type AccessPointType: str
        :param IdcCity: IDC所在城市
注意：此字段可能返回 null，表示取不到有效值。
        :type IdcCity: str
        :param ChargeState: 计费状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeState: str
        :param StartTime: 物理专线开通时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param SignLaw: 物理专线是否已签署用户协议
注意：此字段可能返回 null，表示取不到有效值。
        :type SignLaw: bool
        """
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


class DirectConnectTunnel(AbstractModel):
    """专用通道信息列表

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param DirectConnectId: 物理专线ID
        :type DirectConnectId: str
        :param State: 专用通道状态
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
        :param DirectConnectOwnerAccount: 物理专线的拥有者，开发商账号 ID
        :type DirectConnectOwnerAccount: str
        :param OwnerAccount: 专用通道的拥有者，开发商账号 ID
        :type OwnerAccount: str
        :param NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :type NetworkType: str
        :param NetworkRegion: VPC地域对应的网络名，如ap-guangzhou
        :type NetworkRegion: str
        :param VpcId: 私有网络统一 ID 或者黑石网络统一 ID
        :type VpcId: str
        :param DirectConnectGatewayId: 专线网关 ID
        :type DirectConnectGatewayId: str
        :param RouteType: BGP ：BGP路由 STATIC：静态 默认为 BGP 路由
        :type RouteType: str
        :param BgpPeer: 用户侧BGP，Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 用户侧网段地址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param Vlan: 专用通道的Vlan
        :type Vlan: int
        :param TencentAddress: TencentAddress，腾讯侧互联 IP
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress，用户侧互联 IP
        :type CustomerAddress: str
        :param DirectConnectTunnelName: 专用通道名称
        :type DirectConnectTunnelName: str
        :param CreatedTime: 专用通道创建时间
        :type CreatedTime: str
        :param Bandwidth: 专用通道带宽值
        :type Bandwidth: int
        :param TagSet: 专用通道标签值
        :type TagSet: list of Tag
        :param NetDetectId: 关联的网络自定义探测ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NetDetectId: str
        :param EnableBGPCommunity: BGP community开关
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableBGPCommunity: bool
        :param NatType: 是否为Nat通道
注意：此字段可能返回 null，表示取不到有效值。
        :type NatType: int
        :param VpcRegion: VPC地域简码，如gz、cd
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcRegion: str
        :param BfdEnable: 是否开启BFD
注意：此字段可能返回 null，表示取不到有效值。
        :type BfdEnable: int
        :param AccessPointType: 专用通道接入点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessPointType: str
        :param DirectConnectGatewayName: 专线网关名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DirectConnectGatewayName: str
        :param VpcName: VPC名称
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        :param TencentBackupAddress: TencentBackupAddress，腾讯侧备用互联 IP
注意：此字段可能返回 null，表示取不到有效值。
        :type TencentBackupAddress: str
        :param SignLaw: 专用通道关联的物理专线是否签署了用户协议
注意：此字段可能返回 null，表示取不到有效值。
        :type SignLaw: bool
        :param CloudAttachId: 高速上云服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudAttachId: str
        """
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


class DirectConnectTunnelExtra(AbstractModel):
    """专用通道扩展信息

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param DirectConnectId: 物理专线ID
        :type DirectConnectId: str
        :param State: 专用通道状态
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
        :param DirectConnectOwnerAccount: 物理专线的拥有者，开发商账号 ID
        :type DirectConnectOwnerAccount: str
        :param OwnerAccount: 专用通道的拥有者，开发商账号 ID
        :type OwnerAccount: str
        :param NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :type NetworkType: str
        :param NetworkRegion: VPC地域对应的网络名，如ap-guangzhou
        :type NetworkRegion: str
        :param VpcId: 私有网络统一 ID 或者黑石网络统一 ID
        :type VpcId: str
        :param DirectConnectGatewayId: 专线网关 ID
        :type DirectConnectGatewayId: str
        :param RouteType: BGP ：BGP路由 STATIC：静态 默认为 BGP 路由
        :type RouteType: str
        :param BgpPeer: 用户侧BGP，Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 用户侧网段地址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param PublicAddresses: 互联网通道公网网段地址
        :type PublicAddresses: list of RouteFilterPrefix
        :param Vlan: 专用通道的Vlan
        :type Vlan: int
        :param TencentAddress: 腾讯侧互联 IP
        :type TencentAddress: str
        :param TencentBackupAddress: 腾讯侧备用互联IP
        :type TencentBackupAddress: str
        :param CustomerAddress: 用户侧互联 IP
        :type CustomerAddress: str
        :param DirectConnectTunnelName: 专用通道名称
        :type DirectConnectTunnelName: str
        :param CreatedTime: 专用通道创建时间
        :type CreatedTime: str
        :param Bandwidth: 专用通道带宽值
        :type Bandwidth: int
        :param NetDetectId: 关联的网络自定义探测ID
        :type NetDetectId: str
        :param EnableBGPCommunity: BGP community开关
        :type EnableBGPCommunity: bool
        :param NatType: 是否为Nat通道
        :type NatType: int
        :param VpcRegion: VPC地域简码，如gz、cd
        :type VpcRegion: str
        :param BfdEnable: 是否开启BFD
        :type BfdEnable: int
        :param NqaEnable: 是否开启NQA
        :type NqaEnable: int
        :param AccessPointType: 专用通道接入点类型
        :type AccessPointType: str
        :param DirectConnectGatewayName: 专线网关名称
        :type DirectConnectGatewayName: str
        :param VpcName: VPC名称
        :type VpcName: str
        :param SignLaw: 专用通道关联的物理专线是否签署了用户协议
        :type SignLaw: bool
        :param BfdInfo: BFD配置信息
        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        :param NqaInfo: NQA配置信息
        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        :param BgpStatus: BGP状态
        :type BgpStatus: :class:`tencentcloud.dc.v20180410.models.BGPStatus`
        :param IPv6Enable: 是否开启IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type IPv6Enable: int
        :param TencentIPv6Address: 腾讯侧互联IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type TencentIPv6Address: str
        :param TencentBackupIPv6Address: 腾讯侧备用互联IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type TencentBackupIPv6Address: str
        :param BgpIPv6Status: BGPv6状态
注意：此字段可能返回 null，表示取不到有效值。
        :type BgpIPv6Status: :class:`tencentcloud.dc.v20180410.models.BGPStatus`
        :param CustomerIPv6Address: 用户侧互联IPv6地址
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomerIPv6Address: str
        """
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


class DirectConnectTunnelRoute(AbstractModel):
    """专线通道路由

    """

    def __init__(self):
        """
        :param RouteId: 专用通道路由ID
        :type RouteId: str
        :param DestinationCidrBlock: 网段CIDR
        :type DestinationCidrBlock: str
        :param RouteType: 路由类型：BGP/STATIC路由
        :type RouteType: str
        :param Status: ENABLE：路由启用，DISABLE：路由禁用
        :type Status: str
        :param ASPath: ASPath信息
        :type ASPath: list of str
        :param NextHop: 路由下一跳IP
        :type NextHop: str
        """
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


class DisableInternetAddressRequest(AbstractModel):
    """DisableInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 公网互联网地址ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DisableInternetAddressResponse(AbstractModel):
    """DisableInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableInternetAddressRequest(AbstractModel):
    """EnableInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 互联网公网地址ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class EnableInternetAddressResponse(AbstractModel):
    """EnableInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """用于条件过滤查询

    """

    def __init__(self):
        """
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class InternetAddressDetail(AbstractModel):
    """互联网地址详细信息

    """

    def __init__(self):
        """
        :param InstanceId: 互联网地址ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Subnet: 互联网网络地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Subnet: str
        :param MaskLen: 网络地址掩码长度
注意：此字段可能返回 null，表示取不到有效值。
        :type MaskLen: int
        :param AddrType: 0:BGP
1:电信
2:移动
3:联通
注意：此字段可能返回 null，表示取不到有效值。
        :type AddrType: int
        :param Status: 0:使用中
1:已停用
2:已退还
        :type Status: int
        :param ApplyTime: 申请时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplyTime: str
        :param StopTime: 停用时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StopTime: str
        :param ReleaseTime: 退还时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param AppId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param AddrProto: 0:IPv4 1:IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type AddrProto: int
        :param ReserveTime: 释放状态的IP地址保留的天数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReserveTime: int
        """
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


class InternetAddressStatistics(AbstractModel):
    """互联网公网地址统计

    """

    def __init__(self):
        """
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param SubnetNum: 互联网公网地址数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetNum: int
        """
        self.Region = None
        self.SubnetNum = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.SubnetNum = params.get("SubnetNum")


class ModifyDirectConnectAttributeRequest(AbstractModel):
    """ModifyDirectConnectAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectId: 物理专线的ID。
        :type DirectConnectId: str
        :param DirectConnectName: 物理专线名称。
        :type DirectConnectName: str
        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
        :type CircuitCode: str
        :param Vlan: 物理专线调试VLAN。
        :type Vlan: int
        :param TencentAddress: 物理专线调试腾讯侧互联 IP。
        :type TencentAddress: str
        :param CustomerAddress: 物理专线调试用户侧互联 IP。
        :type CustomerAddress: str
        :param CustomerName: 物理专线申请者姓名。默认从账户体系获取。
        :type CustomerName: str
        :param CustomerContactMail: 物理专线申请者联系邮箱。默认从账户体系获取。
        :type CustomerContactMail: str
        :param CustomerContactNumber: 物理专线申请者联系号码。默认从账户体系获取。
        :type CustomerContactNumber: str
        :param FaultReportContactPerson: 报障联系人。
        :type FaultReportContactPerson: str
        :param FaultReportContactNumber: 报障联系电话。
        :type FaultReportContactNumber: str
        :param SignLaw: 物理专线申请者补签用户使用协议
        :type SignLaw: bool
        :param Bandwidth: 物理专线带宽
        :type Bandwidth: int
        """
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


class ModifyDirectConnectAttributeResponse(AbstractModel):
    """ModifyDirectConnectAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelAttributeRequest(AbstractModel):
    """ModifyDirectConnectTunnelAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param DirectConnectTunnelName: 专用通道名称
        :type DirectConnectTunnelName: str
        :param BgpPeer: 用户侧BGP，包括Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 用户侧网段地址
        :type RouteFilterPrefixes: list of RouteFilterPrefix
        :param TencentAddress: 腾讯侧互联IP
        :type TencentAddress: str
        :param CustomerAddress: 用户侧互联IP
        :type CustomerAddress: str
        :param Bandwidth: 专用通道带宽值，单位为M。
        :type Bandwidth: int
        :param TencentBackupAddress: 腾讯侧备用互联IP
        :type TencentBackupAddress: str
        """
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


class ModifyDirectConnectTunnelAttributeResponse(AbstractModel):
    """ModifyDirectConnectTunnelAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectTunnelExtraRequest(AbstractModel):
    """ModifyDirectConnectTunnelExtra请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专用通道ID
        :type DirectConnectTunnelId: str
        :param Vlan: 专用通道的Vlan
        :type Vlan: int
        :param BgpPeer: 用户侧BGP，Asn，AuthKey
        :type BgpPeer: :class:`tencentcloud.dc.v20180410.models.BgpPeer`
        :param RouteFilterPrefixes: 用户侧过滤网段地址
        :type RouteFilterPrefixes: :class:`tencentcloud.dc.v20180410.models.RouteFilterPrefix`
        :param TencentAddress: 腾讯侧互联IP
        :type TencentAddress: str
        :param TencentBackupAddress: 腾讯侧备用互联IP
        :type TencentBackupAddress: str
        :param CustomerAddress: 用户侧互联IP
        :type CustomerAddress: str
        :param Bandwidth: 专用通道带宽值
        :type Bandwidth: int
        :param EnableBGPCommunity: BGP community开关
        :type EnableBGPCommunity: bool
        :param BfdEnable: 是否开启BFD
        :type BfdEnable: int
        :param NqaEnable: 是否开启NQA
        :type NqaEnable: int
        :param BfdInfo: BFD配置信息
        :type BfdInfo: :class:`tencentcloud.dc.v20180410.models.BFDInfo`
        :param NqaInfo: NQA配置信息
        :type NqaInfo: :class:`tencentcloud.dc.v20180410.models.NQAInfo`
        :param IPv6Enable: 0：停用IPv6
1: 启用IPv6
        :type IPv6Enable: int
        :param CustomerIDCRoutes: 去往用户侧的路由信息
        :type CustomerIDCRoutes: list of RouteFilterPrefix
        """
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


class ModifyDirectConnectTunnelExtraResponse(AbstractModel):
    """ModifyDirectConnectTunnelExtra返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NQAInfo(AbstractModel):
    """nqa配置信息

    """

    def __init__(self):
        """
        :param ProbeFailedTimes: 健康检查次数
        :type ProbeFailedTimes: int
        :param Interval: 健康检查间隔
        :type Interval: int
        :param DestinationIp: 健康检查地址
        :type DestinationIp: str
        """
        self.ProbeFailedTimes = None
        self.Interval = None
        self.DestinationIp = None


    def _deserialize(self, params):
        self.ProbeFailedTimes = params.get("ProbeFailedTimes")
        self.Interval = params.get("Interval")
        self.DestinationIp = params.get("DestinationIp")


class RejectDirectConnectTunnelRequest(AbstractModel):
    """RejectDirectConnectTunnel请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 无
        :type DirectConnectTunnelId: str
        """
        self.DirectConnectTunnelId = None


    def _deserialize(self, params):
        self.DirectConnectTunnelId = params.get("DirectConnectTunnelId")


class RejectDirectConnectTunnelResponse(AbstractModel):
    """RejectDirectConnectTunnel返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseInternetAddressRequest(AbstractModel):
    """ReleaseInternetAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 公网互联网地址ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class ReleaseInternetAddressResponse(AbstractModel):
    """ReleaseInternetAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RouteFilterPrefix(AbstractModel):
    """用户侧网段地址

    """

    def __init__(self):
        """
        :param Cidr: 用户侧网段地址
        :type Cidr: str
        """
        self.Cidr = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        """
        :param Key: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")