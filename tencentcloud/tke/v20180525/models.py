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


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 实例列表
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）
        :type SecurityGroupIds: list of str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param FailedInstanceIds: 失败的节点ID
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: 成功的节点ID
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: 超时未返回出来节点的ID(可能失败，也可能成功)
        :type TimeoutInstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self.RequestId = params.get("RequestId")


class Cluster(AbstractModel):
    """集群信息结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterDescription: 集群描述
        :type ClusterDescription: str
        :param ClusterVersion: 集群版本（默认值为1.10.5）
        :type ClusterVersion: str
        :param ClusterOs: 集群系统。centos7.2x86_64 或者 ubuntu16.04.1 LTSx86_64，默认取值为ubuntu16.04.1 LTSx86_64
        :type ClusterOs: str
        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。
        :type ClusterType: str
        :param ClusterNetworkSettings: 集群网络相关参数
        :type ClusterNetworkSettings: :class:`tencentcloud.tke.v20180525.models.ClusterNetworkSettings`
        :param ClusterNodeNum: 集群当前node数量
        :type ClusterNodeNum: int
        :param ProjectId: 集群所属的项目ID
        :type ProjectId: int
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.ClusterVersion = None
        self.ClusterOs = None
        self.ClusterType = None
        self.ClusterNetworkSettings = None
        self.ClusterNodeNum = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterType = params.get("ClusterType")
        if params.get("ClusterNetworkSettings") is not None:
            self.ClusterNetworkSettings = ClusterNetworkSettings()
            self.ClusterNetworkSettings._deserialize(params.get("ClusterNetworkSettings"))
        self.ClusterNodeNum = params.get("ClusterNodeNum")
        self.ProjectId = params.get("ProjectId")


class ClusterAdvancedSettings(AbstractModel):
    """集群高级配置

    """

    def __init__(self):
        """
        :param IPVS: 是否启用IPVS
        :type IPVS: bool
        :param AsEnabled: 是否启用集群节点自动扩缩容(创建集群流程不支持开启此功能)
        :type AsEnabled: bool
        :param ContainerRuntime: 集群使用的runtime类型，包括"docker"和"containerd"两种类型，默认为"docker"
        :type ContainerRuntime: str
        """
        self.IPVS = None
        self.AsEnabled = None
        self.ContainerRuntime = None


    def _deserialize(self, params):
        self.IPVS = params.get("IPVS")
        self.AsEnabled = params.get("AsEnabled")
        self.ContainerRuntime = params.get("ContainerRuntime")


class ClusterBasicSettings(AbstractModel):
    """描述集群的基本配置信息

    """

    def __init__(self):
        """
        :param ClusterOs: 集群系统。centos7.2x86_64 或者 ubuntu16.04.1 LTSx86_64，默认取值为ubuntu16.04.1 LTSx86_64
        :type ClusterOs: str
        :param ClusterVersion: 集群版本,默认值为1.10.5
        :type ClusterVersion: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterDescription: 集群描述
        :type ClusterDescription: str
        :param VpcId: 私有网络ID，形如vpc-xxx。创建托管空集群时必传。
        :type VpcId: str
        :param ProjectId: 集群内新增资源所属项目ID。
        :type ProjectId: int
        """
        self.ClusterOs = None
        self.ClusterVersion = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.VpcId = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")


class ClusterCIDRSettings(AbstractModel):
    """集群容器网络相关参数

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用于分配集群容器和服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 冲突错误, 默认不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service数量
        :type MaxClusterServiceNum: int
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")


class ClusterNetworkSettings(AbstractModel):
    """集群网络相关的参数

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用于分配集群容器和服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 冲突错误, 默认不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量(默认为256)
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service数量(默认为256)
        :type MaxClusterServiceNum: int
        :param Ipvs: 是否启用IPVS(默认不开启)
        :type Ipvs: bool
        :param VpcId: 集群的VPCID（如果创建空集群，为必传值，否则自动设置为和集群的节点保持一致）
        :type VpcId: str
        :param Cni: 网络插件是否启用CNI(默认开启)
        :type Cni: bool
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.Ipvs = None
        self.VpcId = None
        self.Cni = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.Ipvs = params.get("Ipvs")
        self.VpcId = params.get("VpcId")
        self.Cni = params.get("Cni")


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段
        :type ClusterId: str
        :param RunInstancePara: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。
        :type RunInstancePara: str
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        """
        self.ClusterId = None
        self.RunInstancePara = None
        self.InstanceAdvancedSettings = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RunInstancePara = params.get("RunInstancePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 节点实例ID
        :type InstanceIdSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: 集群容器网络配置信息
        :type ClusterCIDRSettings: :class:`tencentcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。
        :type ClusterType: str
        :param RunInstancesForNode: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。
        :type RunInstancesForNode: list of RunInstancesForNode
        :param ClusterBasicSettings: 集群的基本配置信息
        :type ClusterBasicSettings: :class:`tencentcloud.tke.v20180525.models.ClusterBasicSettings`
        :param ClusterAdvancedSettings: 集群高级配置信息
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.ClusterAdvancedSettings`
        :param InstanceAdvancedSettings: 节点高级配置信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param ExistedInstancesForNode: 已存在实例的配置信息
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        """
        self.ClusterCIDRSettings = None
        self.ClusterType = None
        self.RunInstancesForNode = None
        self.ClusterBasicSettings = None
        self.ClusterAdvancedSettings = None
        self.InstanceAdvancedSettings = None
        self.ExistedInstancesForNode = None


    def _deserialize(self, params):
        if params.get("ClusterCIDRSettings") is not None:
            self.ClusterCIDRSettings = ClusterCIDRSettings()
            self.ClusterCIDRSettings._deserialize(params.get("ClusterCIDRSettings"))
        self.ClusterType = params.get("ClusterType")
        if params.get("RunInstancesForNode") is not None:
            self.RunInstancesForNode = []
            for item in params.get("RunInstancesForNode"):
                obj = RunInstancesForNode()
                obj._deserialize(item)
                self.RunInstancesForNode.append(obj)
        if params.get("ClusterBasicSettings") is not None:
            self.ClusterBasicSettings = ClusterBasicSettings()
            self.ClusterBasicSettings._deserialize(params.get("ClusterBasicSettings"))
        if params.get("ClusterAdvancedSettings") is not None:
            self.ClusterAdvancedSettings = ClusterAdvancedSettings()
            self.ClusterAdvancedSettings._deserialize(params.get("ClusterAdvancedSettings"))
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("ExistedInstancesForNode") is not None:
            self.ExistedInstancesForNode = []
            for item in params.get("ExistedInstancesForNode"):
                obj = ExistedInstancesForNode()
                obj._deserialize(item)
                self.ExistedInstancesForNode.append(obj)


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreateClusterRouteRequest(AbstractModel):
    """CreateClusterRoute请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param DestinationCidrBlock: 目的端CIDR。
        :type DestinationCidrBlock: str
        :param GatewayIp: 下一跳地址。
        :type GatewayIp: str
        """
        self.RouteTableName = None
        self.DestinationCidrBlock = None
        self.GatewayIp = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayIp = params.get("GatewayIp")


class CreateClusterRouteResponse(AbstractModel):
    """CreateClusterRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterRouteTableRequest(AbstractModel):
    """CreateClusterRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称
        :type RouteTableName: str
        :param RouteTableCidrBlock: 路由表CIDR
        :type RouteTableCidrBlock: str
        :param VpcId: 路由表绑定的VPC
        :type VpcId: str
        :param IgnoreClusterCidrConflict: 是否忽略CIDR冲突
        :type IgnoreClusterCidrConflict: int
        """
        self.RouteTableName = None
        self.RouteTableCidrBlock = None
        self.VpcId = None
        self.IgnoreClusterCidrConflict = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")
        self.IgnoreClusterCidrConflict = params.get("IgnoreClusterCidrConflict")


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 主机InstanceId列表
        :type InstanceIds: list of str
        :param InstanceDeleteMode: 集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）
        :type InstanceDeleteMode: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceDeleteMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceDeleteMode: 集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）
        :type InstanceDeleteMode: str
        """
        self.ClusterId = None
        self.InstanceDeleteMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteRequest(AbstractModel):
    """DeleteClusterRoute请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param GatewayIp: 下一跳地址。
        :type GatewayIp: str
        :param DestinationCidrBlock: 目的端CIDR。
        :type DestinationCidrBlock: str
        """
        self.RouteTableName = None
        self.GatewayIp = None
        self.DestinationCidrBlock = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.GatewayIp = params.get("GatewayIp")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteTableRequest(AbstractModel):
    """DeleteClusterRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称
        :type RouteTableName: str
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20
        :type Limit: int
        :param InstanceIds: 需要获取的节点实例Id列表(默认为空，表示拉取集群下所有节点实例)
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群中实例总数
        :type TotalCount: int
        :param InstanceSet: 集群中实例列表
        :type InstanceSet: list of Instance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterRouteTablesRequest(AbstractModel):
    """DescribeClusterRouteTables请求参数结构体

    """


class DescribeClusterRouteTablesResponse(AbstractModel):
    """DescribeClusterRouteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RouteTableSet: 集群路由表对象。
        :type RouteTableSet: list of RouteTableInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTableInfo()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterRoutesRequest(AbstractModel):
    """DescribeClusterRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RouteSet: 集群路由对象。
        :type RouteSet: list of RouteInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = RouteInfo()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterSecurityRequest(AbstractModel):
    """DescribeClusterSecurity请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity返回参数结构体

    """

    def __init__(self):
        """
        :param UserName: 集群的账号名称
        :type UserName: str
        :param Password: 集群的访问密码
        :type Password: str
        :param CertificationAuthority: 集群访问CA证书
        :type CertificationAuthority: str
        :param ClusterExternalEndpoint: 集群访问的地址
        :type ClusterExternalEndpoint: str
        :param Domain: 集群访问的域名
        :type Domain: str
        :param PgwEndpoint: 集群Endpoint地址
        :type PgwEndpoint: str
        :param SecurityPolicy: 集群访问策略组
        :type SecurityPolicy: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserName = None
        self.Password = None
        self.CertificationAuthority = None
        self.ClusterExternalEndpoint = None
        self.Domain = None
        self.PgwEndpoint = None
        self.SecurityPolicy = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.CertificationAuthority = params.get("CertificationAuthority")
        self.ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self.Domain = params.get("Domain")
        self.PgwEndpoint = params.get("PgwEndpoint")
        self.SecurityPolicy = params.get("SecurityPolicy")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 集群ID列表(为空时，
表示获取账号下所有集群)
        :type ClusterIds: list of str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20
        :type Limit: int
        :param Filters: 过滤条件,当前只支持按照单个条件ClusterName进行过滤
        :type Filters: list of Filter
        """
        self.ClusterIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群总个数
        :type TotalCount: int
        :param Clusters: 集群信息列表
        :type Clusters: list of Cluster
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = Cluster()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写查询集群列表 接口中返回的 ClusterId 字段（仅通过ClusterId获取需要过滤条件中的VPCID，比较状态时会使用该地域下所有集群中的节点进行比较。参数不支持同时指定InstanceIds和ClusterId。
        :type ClusterId: str
        :param InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：ins-xxxxxxxx。（此参数的具体格式可参考API简介的id.N一节）。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param Filters: 过滤条件,字段和详见[CVM查询实例](https://cloud.tencent.com/document/api/213/15728)如果设置了ClusterId，会附加集群的VPCID作为查询字段，在此情况下如果在Filter中指定了"vpc-id"作为过滤字段，指定的VPCID必须与集群的VPCID相同。
        :type Filters: list of Filter
        :param VagueIpAddress: 实例IP进行过滤(同时支持内网IP和外网IP)
        :type VagueIpAddress: str
        :param VagueInstanceName: 实例名称进行过滤
        :type VagueInstanceName: str
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Filters = None
        self.VagueIpAddress = None
        self.VagueInstanceName = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.VagueIpAddress = params.get("VagueIpAddress")
        self.VagueInstanceName = params.get("VagueInstanceName")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ExistedInstanceSet: 已经存在的实例信息数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExistedInstanceSet: list of ExistedInstance
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ExistedInstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ExistedInstanceSet") is not None:
            self.ExistedInstanceSet = []
            for item in params.get("ExistedInstanceSet"):
                obj = ExistedInstance()
                obj._deserialize(item)
                self.ExistedInstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableCidrBlock: 路由表CIDR
        :type RouteTableCidrBlock: str
        :param VpcId: 路由表绑定的VPC
        :type VpcId: str
        """
        self.RouteTableCidrBlock = None
        self.VpcId = None


    def _deserialize(self, params):
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts返回参数结构体

    """

    def __init__(self):
        """
        :param HasConflict: 路由表是否冲突。
        :type HasConflict: bool
        :param RouteTableConflictSet: 路由表冲突列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteTableConflictSet: list of RouteTableConflict
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HasConflict = None
        self.RouteTableConflictSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.HasConflict = params.get("HasConflict")
        if params.get("RouteTableConflictSet") is not None:
            self.RouteTableConflictSet = []
            for item in params.get("RouteTableConflictSet"):
                obj = RouteTableConflict()
                obj._deserialize(item)
                self.RouteTableConflictSet.append(obj)
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        """
        :param SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.RunSecurityServiceEnabled`
        :param MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.RunMonitorServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))


class ExistedInstance(AbstractModel):
    """已经存在的实例信息

    """

    def __init__(self):
        """
        :param Usable: 实例是否支持加入集群(TRUE 可以加入 FALSE 不能加入)。
注意：此字段可能返回 null，表示取不到有效值。
        :type Usable: bool
        :param UnusableReason: 实例不支持加入的原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnusableReason: str
        :param AlreadyInCluster: 实例已经所在的集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AlreadyInCluster: str
        :param InstanceId: 实例ID形如：ins-xxxxxxxx。
        :type InstanceId: str
        :param InstanceName: 实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param PrivateIpAddresses: 实例主网卡的内网IP列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: 实例主网卡的公网IP列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param CreatedTime: 创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param InstanceChargeType: 实例计费模式。取值范围：
PREPAID：表示预付费，即包年包月
POSTPAID_BY_HOUR：表示后付费，即按量计费
CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param CPU: 实例的CPU核数，单位：核。
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: int
        :param Memory: 实例内存容量，单位：GB。
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param OsName: 操作系统名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param InstanceType: 实例机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        """
        self.Usable = None
        self.UnusableReason = None
        self.AlreadyInCluster = None
        self.InstanceId = None
        self.InstanceName = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.CreatedTime = None
        self.InstanceChargeType = None
        self.CPU = None
        self.Memory = None
        self.OsName = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Usable = params.get("Usable")
        self.UnusableReason = params.get("UnusableReason")
        self.AlreadyInCluster = params.get("AlreadyInCluster")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.CreatedTime = params.get("CreatedTime")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.OsName = params.get("OsName")
        self.InstanceType = params.get("InstanceType")


class ExistedInstancesForNode(AbstractModel):
    """不同角色的已存在节点配置参数

    """

    def __init__(self):
        """
        :param NodeRole: 节点角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在创建 INDEPENDENT_CLUSTER 独立集群时需要指定。
        :type NodeRole: str
        :param ExistedInstancesPara: 已存在实例的重装参数
        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))


class ExistedInstancesPara(AbstractModel):
    """已存在实例的重装参数

    """

    def __init__(self):
        """
        :param InstanceIds: 集群ID
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）
        :type SecurityGroupIds: list of str
        """
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Instance(AbstractModel):
    """集群的实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceRole: 节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER
        :type InstanceRole: str
        :param FailedReason: 实例异常(或者处于初始化中)的原因
        :type FailedReason: str
        :param InstanceState: 实例的状态（running 运行中，initializing 初始化中，failed 异常）
        :type InstanceState: str
        """
        self.InstanceId = None
        self.InstanceRole = None
        self.FailedReason = None
        self.InstanceState = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.FailedReason = params.get("FailedReason")
        self.InstanceState = params.get("InstanceState")


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相关配置与信息。

    """

    def __init__(self):
        """
        :param MountTarget: 数据盘挂载点, 默认不挂载数据盘. 已格式化的 ext3，ext4，xfs 文件系统的数据盘将直接挂载，其他文件系统或未格式化的数据盘将自动格式化为ext4 并挂载，请注意备份数据! 无数据盘或有多块数据盘的云主机此设置不生效。
        :type MountTarget: str
        :param DockerGraphPath: dockerd --graph 指定值, 默认为 /var/lib/docker
        :type DockerGraphPath: str
        :param UserScript: base64 编码的用户脚本, 此脚本会在 k8s 组件运行后执行, 需要用户保证脚本的可重入及重试逻辑, 脚本及其生成的日志文件可在节点的 /data/ccs_userscript/ 路径查看, 如果要求节点需要在进行初始化完成后才可加入调度, 可配合 unschedulable 参数使用, 在 userScript 最后初始化完成后, 添加 kubectl uncordon nodename --kubeconfig=/root/.kube/config 命令使节点加入调度
        :type UserScript: str
        :param Unschedulable: 设置加入的节点是否参与调度，默认值为0，表示参与调度；非0表示不参与调度, 待节点初始化完成之后, 可执行kubectl uncordon nodename使node加入调度.
        :type Unschedulable: int
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")
        self.UserScript = params.get("UserScript")
        self.Unschedulable = params.get("Unschedulable")


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        """
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class RouteInfo(AbstractModel):
    """集群路由对象

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param DestinationCidrBlock: 目的端CIDR。
        :type DestinationCidrBlock: str
        :param GatewayIp: 下一跳地址。
        :type GatewayIp: str
        """
        self.RouteTableName = None
        self.DestinationCidrBlock = None
        self.GatewayIp = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayIp = params.get("GatewayIp")


class RouteTableConflict(AbstractModel):
    """路由表冲突对象

    """

    def __init__(self):
        """
        :param RouteTableType: 路由表类型。
        :type RouteTableType: str
        :param RouteTableCidrBlock: 路由表CIDR。
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteTableCidrBlock: str
        :param RouteTableName: 路由表名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteTableName: str
        :param RouteTableId: 路由表ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteTableId: str
        """
        self.RouteTableType = None
        self.RouteTableCidrBlock = None
        self.RouteTableName = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableType = params.get("RouteTableType")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableId = params.get("RouteTableId")


class RouteTableInfo(AbstractModel):
    """集群路由表对象

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param RouteTableCidrBlock: 路由表CIDR。
        :type RouteTableCidrBlock: str
        :param VpcId: VPC实例ID。
        :type VpcId: str
        """
        self.RouteTableName = None
        self.RouteTableCidrBlock = None
        self.VpcId = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        self.RouteTableCidrBlock = params.get("RouteTableCidrBlock")
        self.VpcId = params.get("VpcId")


class RunInstancesForNode(AbstractModel):
    """不同角色的节点配置参数

    """

    def __init__(self):
        """
        :param NodeRole: 节点角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在创建 INDEPENDENT_CLUSTER 独立集群时需要指定。
        :type NodeRole: str
        :param RunInstancesPara: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口，传入公共参数外的其他参数即可，其中ImageId会替换为TKE集群OS对应的镜像。
        :type RunInstancesPara: list of str
        """
        self.NodeRole = None
        self.RunInstancesPara = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        self.RunInstancesPara = params.get("RunInstancesPara")


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启[云监控](/document/product/248)服务。取值范围：<br><li>TRUE：表示开启云监控服务<br><li>FALSE：表示不开启云监控服务<br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启[云安全](/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务<br><li>FALSE：表示不开启云安全服务<br><br>默认取值：TRUE。
        :type Enabled: bool
        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")