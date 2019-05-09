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
        """
        self.AccessPointName = None
        self.AccessPointId = None
        self.State = None
        self.Location = None
        self.LineOperator = None
        self.RegionId = None


    def _deserialize(self, params):
        self.AccessPointName = params.get("AccessPointName")
        self.AccessPointId = params.get("AccessPointId")
        self.State = params.get("State")
        self.Location = params.get("Location")
        self.LineOperator = params.get("LineOperator")
        self.RegionId = params.get("RegionId")


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
        :param Location: 本地数据中心的地理位置。
        :type Location: str
        :param PortType: 物理专线接入端口类型,取值：100Base-T：百兆电口,1000Base-T（默认值）：千兆电口,1000Base-LX：千兆单模光口（10千米）,10GBase-T：万兆电口10GBase-LR：万兆单模光口（10千米），默认值，千兆单模光口（10千米）。
        :type PortType: str
        :param CircuitCode: 运营商或者服务商为物理专线提供的电路编码。
        :type CircuitCode: str
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
        """
        self.DirectConnectName = None
        self.AccessPointId = None
        self.LineOperator = None
        self.Location = None
        self.PortType = None
        self.CircuitCode = None
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


    def _deserialize(self, params):
        self.DirectConnectName = params.get("DirectConnectName")
        self.AccessPointId = params.get("AccessPointId")
        self.LineOperator = params.get("LineOperator")
        self.Location = params.get("Location")
        self.PortType = params.get("PortType")
        self.CircuitCode = params.get("CircuitCode")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectSet") is not None:
            self.DirectConnectSet = []
            for item in params.get("DirectConnectSet"):
                obj = DirectConnect()
                obj._deserialize(item)
                self.DirectConnectSet.append(obj)
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


class DirectConnectTunnel(AbstractModel):
    """专线通道信息列表

    """

    def __init__(self):
        """
        :param DirectConnectTunnelId: 专线通道ID
        :type DirectConnectTunnelId: str
        :param DirectConnectId: 物理专线ID
        :type DirectConnectId: str
        :param State: 专线通道状态
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
        :param OwnerAccount: 专线通道的拥有者，开发商账号 ID
        :type OwnerAccount: str
        :param NetworkType: 网络类型，分别为VPC、BMVPC、CCN
 VPC：私有网络 ，BMVPC：黑石网络，CCN：云联网
        :type NetworkType: str
        :param NetworkRegion: VPC地域
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
        :param Vlan: 专线通道的Vlan
        :type Vlan: int
        :param TencentAddress: TencentAddress，腾讯侧互联 IP
        :type TencentAddress: str
        :param CustomerAddress: CustomerAddress，用户侧互联 IP
        :type CustomerAddress: str
        :param DirectConnectTunnelName: 专线通道名称
        :type DirectConnectTunnelName: str
        :param CreatedTime: 专线通道创建时间
        :type CreatedTime: str
        :param Bandwidth: 专线通道带宽值
        :type Bandwidth: int
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
        """
        self.DirectConnectTunnelId = None
        self.DirectConnectTunnelName = None
        self.BgpPeer = None
        self.RouteFilterPrefixes = None
        self.TencentAddress = None
        self.CustomerAddress = None
        self.Bandwidth = None


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