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


class APM(AbstractModel):
    """腾讯云应用性能管理服务参数

    """

    def __init__(self):
        r"""
        :param Enable: 是否启用
        :type Enable: bool
        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param InstanceId: APM 实例，如果创建时传入的参数为空，则表示自动创建 APM 实例。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        """
        self.Enable = None
        self.Region = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessLogConfig(AbstractModel):
    """AccessLog 配置

    """

    def __init__(self):
        r"""
        :param Enable: 是否启用
        :type Enable: bool
        :param Template: 采用的模板，可选值：istio（默认）、trace
        :type Template: str
        :param SelectedRange: 选中的范围
        :type SelectedRange: :class:`tencentcloud.tcm.v20210413.models.SelectedRange`
        :param CLS: 腾讯云日志服务相关参数
        :type CLS: :class:`tencentcloud.tcm.v20210413.models.CLS`
        :param Encoding: 编码格式，可选值：TEXT、JSON
        :type Encoding: str
        :param Format: 日志格式
        :type Format: str
        :param Address: GRPC第三方服务器地址
        :type Address: str
        :param EnableServer: 是否启用GRPC第三方服务器
        :type EnableServer: bool
        :param EnableStdout: 是否启用标准输出
        :type EnableStdout: bool
        """
        self.Enable = None
        self.Template = None
        self.SelectedRange = None
        self.CLS = None
        self.Encoding = None
        self.Format = None
        self.Address = None
        self.EnableServer = None
        self.EnableStdout = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.Template = params.get("Template")
        if params.get("SelectedRange") is not None:
            self.SelectedRange = SelectedRange()
            self.SelectedRange._deserialize(params.get("SelectedRange"))
        if params.get("CLS") is not None:
            self.CLS = CLS()
            self.CLS._deserialize(params.get("CLS"))
        self.Encoding = params.get("Encoding")
        self.Format = params.get("Format")
        self.Address = params.get("Address")
        self.EnableServer = params.get("EnableServer")
        self.EnableStdout = params.get("EnableStdout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActiveOperation(AbstractModel):
    """正在执行的异步操作

    """

    def __init__(self):
        r"""
        :param OperationId: 操作Id
        :type OperationId: str
        :param Type: 操作类型，取值范围：
- LINK_CLUSTERS: 关联集群
- RELINK_CLUSTERS: 重新关联集群
- UNLINK_CLUSTERS: 解关联集群
- INSTALL_MESH: 安装网格
        :type Type: str
        """
        self.OperationId = None
        self.Type = None


    def _deserialize(self, params):
        self.OperationId = params.get("OperationId")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoInjectionNamespaceState(AbstractModel):
    """描述某一网格在特定命名空间下的自动注入状态

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名称
        :type Namespace: str
        :param State: 注入状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        """
        self.Namespace = None
        self.State = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CLS(AbstractModel):
    """腾讯云日志服务相关参数

    """

    def __init__(self):
        r"""
        :param Enable: 是否启用
        :type Enable: bool
        :param LogSet: 日志集
        :type LogSet: str
        :param Topic: 日志主题
        :type Topic: str
        :param NeedDelete: 是否删除
        :type NeedDelete: bool
        """
        self.Enable = None
        self.LogSet = None
        self.Topic = None
        self.NeedDelete = None


    def _deserialize(self, params):
        self.Enable = params.get("Enable")
        self.LogSet = params.get("LogSet")
        self.Topic = params.get("Topic")
        self.NeedDelete = params.get("NeedDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cluster(AbstractModel):
    """Mesh集群信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param Region: 地域
        :type Region: str
        :param Role: 集群角色，取值范围：
- MASTER：控制面所在的主集群
- REMOTE：主集群管理的远端集群
        :type Role: str
        :param VpcId: 私有网络Id
        :type VpcId: str
        :param SubnetId: 子网Id
        :type SubnetId: str
        :param DisplayName: 名称，只读
        :type DisplayName: str
        :param State: 状态，只读
        :type State: str
        :param LinkedTime: 关联时间，只读
        :type LinkedTime: str
        :param Config: 集群配置
        :type Config: :class:`tencentcloud.tcm.v20210413.models.ClusterConfig`
        :param Status: 详细状态，只读
        :type Status: :class:`tencentcloud.tcm.v20210413.models.ClusterStatus`
        :param Type: 类型，取值范围：
- TKE
- EKS
        :type Type: str
        :param HostedNamespaces: 集群关联的 Namespace 列表
        :type HostedNamespaces: list of str
        """
        self.ClusterId = None
        self.Region = None
        self.Role = None
        self.VpcId = None
        self.SubnetId = None
        self.DisplayName = None
        self.State = None
        self.LinkedTime = None
        self.Config = None
        self.Status = None
        self.Type = None
        self.HostedNamespaces = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Region = params.get("Region")
        self.Role = params.get("Role")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DisplayName = params.get("DisplayName")
        self.State = params.get("State")
        self.LinkedTime = params.get("LinkedTime")
        if params.get("Config") is not None:
            self.Config = ClusterConfig()
            self.Config._deserialize(params.get("Config"))
        if params.get("Status") is not None:
            self.Status = ClusterStatus()
            self.Status._deserialize(params.get("Status"))
        self.Type = params.get("Type")
        self.HostedNamespaces = params.get("HostedNamespaces")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterConfig(AbstractModel):
    """集群配置

    """

    def __init__(self):
        r"""
        :param AutoInjectionNamespaceList: 自动注入SideCar的NameSpace
        :type AutoInjectionNamespaceList: list of str
        :param IngressGatewayList: Ingress配置列表
        :type IngressGatewayList: list of IngressGateway
        :param EgressGatewayList: Egress配置列表
        :type EgressGatewayList: list of EgressGateway
        :param Istiod: Istiod配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Istiod: :class:`tencentcloud.tcm.v20210413.models.IstiodConfig`
        :param DeployConfig: 部署配置
        :type DeployConfig: :class:`tencentcloud.tcm.v20210413.models.DeployConfig`
        :param AutoInjectionNamespaceStateList: 自动注入命名空间状态列表
        :type AutoInjectionNamespaceStateList: list of AutoInjectionNamespaceState
        """
        self.AutoInjectionNamespaceList = None
        self.IngressGatewayList = None
        self.EgressGatewayList = None
        self.Istiod = None
        self.DeployConfig = None
        self.AutoInjectionNamespaceStateList = None


    def _deserialize(self, params):
        self.AutoInjectionNamespaceList = params.get("AutoInjectionNamespaceList")
        if params.get("IngressGatewayList") is not None:
            self.IngressGatewayList = []
            for item in params.get("IngressGatewayList"):
                obj = IngressGateway()
                obj._deserialize(item)
                self.IngressGatewayList.append(obj)
        if params.get("EgressGatewayList") is not None:
            self.EgressGatewayList = []
            for item in params.get("EgressGatewayList"):
                obj = EgressGateway()
                obj._deserialize(item)
                self.EgressGatewayList.append(obj)
        if params.get("Istiod") is not None:
            self.Istiod = IstiodConfig()
            self.Istiod._deserialize(params.get("Istiod"))
        if params.get("DeployConfig") is not None:
            self.DeployConfig = DeployConfig()
            self.DeployConfig._deserialize(params.get("DeployConfig"))
        if params.get("AutoInjectionNamespaceStateList") is not None:
            self.AutoInjectionNamespaceStateList = []
            for item in params.get("AutoInjectionNamespaceStateList"):
                obj = AutoInjectionNamespaceState()
                obj._deserialize(item)
                self.AutoInjectionNamespaceStateList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterStatus(AbstractModel):
    """集群状态

    """

    def __init__(self):
        r"""
        :param LinkState: 关联状态，取值范围：
- LINKING: 关联中
- LINKED: 已关联
- UNLINKING: 解关联中
- LINK_FAILED: 关联失败
- UNLINK_FAILED: 解关联失败
        :type LinkState: str
        :param LinkErrorDetail: 关联错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type LinkErrorDetail: str
        """
        self.LinkState = None
        self.LinkErrorDetail = None


    def _deserialize(self, params):
        self.LinkState = params.get("LinkState")
        self.LinkErrorDetail = params.get("LinkErrorDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CrossRegionConfig(AbstractModel):
    """负载均衡跨域设置

    """


class CustomPromConfig(AbstractModel):
    """第三方 Prometheus 配置参数

    """

    def __init__(self):
        r"""
        :param Url: Prometheus 访问地址
        :type Url: str
        :param AuthType: 认证方式
        :type AuthType: str
        :param IsPublicAddr: 是否公网地址，缺省为 false
        :type IsPublicAddr: bool
        :param VpcId: 虚拟网络id
        :type VpcId: str
        :param Username: Prometheus 用户名（用于 basic 认证方式）
        :type Username: str
        :param Password: Prometheus 密码（用于 basic 认证方式）
        :type Password: str
        """
        self.Url = None
        self.AuthType = None
        self.IsPublicAddr = None
        self.VpcId = None
        self.Username = None
        self.Password = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.AuthType = params.get("AuthType")
        self.IsPublicAddr = params.get("IsPublicAddr")
        self.VpcId = params.get("VpcId")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployConfig(AbstractModel):
    """部署配置

    """

    def __init__(self):
        r"""
        :param NodeSelectType: 部署类型，取值范围：
- SPECIFIC：专有模式
- AUTO：普通模式
        :type NodeSelectType: str
        :param Nodes: 指定的节点
        :type Nodes: list of str
        """
        self.NodeSelectType = None
        self.Nodes = None


    def _deserialize(self, params):
        self.NodeSelectType = params.get("NodeSelectType")
        self.Nodes = params.get("Nodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMeshListRequest(AbstractModel):
    """DescribeMeshList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Limit: 分页限制
        :type Limit: int
        :param Offset: 分页偏移
        :type Offset: int
        """
        self.Filters = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMeshListResponse(AbstractModel):
    """DescribeMeshList返回参数结构体

    """

    def __init__(self):
        r"""
        :param MeshList: 查询到的网格信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MeshList: list of Mesh
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MeshList = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MeshList") is not None:
            self.MeshList = []
            for item in params.get("MeshList"):
                obj = Mesh()
                obj._deserialize(item)
                self.MeshList.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeMeshRequest(AbstractModel):
    """DescribeMesh请求参数结构体

    """

    def __init__(self):
        r"""
        :param MeshId: 需要查询的网格 Id
        :type MeshId: str
        """
        self.MeshId = None


    def _deserialize(self, params):
        self.MeshId = params.get("MeshId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMeshResponse(AbstractModel):
    """DescribeMesh返回参数结构体

    """

    def __init__(self):
        r"""
        :param Mesh: Mesh详细信息
        :type Mesh: :class:`tencentcloud.tcm.v20210413.models.Mesh`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Mesh = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Mesh") is not None:
            self.Mesh = Mesh()
            self.Mesh._deserialize(params.get("Mesh"))
        self.RequestId = params.get("RequestId")


class EgressGateway(AbstractModel):
    """Egress配置

    """

    def __init__(self):
        r"""
        :param Name: Egress名称
        :type Name: str
        :param Namespace: 所在的Namespace
        :type Namespace: str
        :param Workload: 工作负载配置
        :type Workload: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        """
        self.Name = None
        self.Namespace = None
        self.Workload = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        if params.get("Workload") is not None:
            self.Workload = WorkloadConfig()
            self.Workload._deserialize(params.get("Workload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensiveCluster(AbstractModel):
    """内网独占集群配置

    """

    def __init__(self):
        r"""
        :param ClusterId: Cluster ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        """
        self.ClusterId = None
        self.Zone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensiveClusters(AbstractModel):
    """内网独占集群配置列表

    """

    def __init__(self):
        r"""
        :param L4Clusters: 4层集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :type L4Clusters: list of ExtensiveCluster
        :param L7Clusters: 7层集群配置
注意：此字段可能返回 null，表示取不到有效值。
        :type L7Clusters: list of ExtensiveCluster
        """
        self.L4Clusters = None
        self.L7Clusters = None


    def _deserialize(self, params):
        if params.get("L4Clusters") is not None:
            self.L4Clusters = []
            for item in params.get("L4Clusters"):
                obj = ExtensiveCluster()
                obj._deserialize(item)
                self.L4Clusters.append(obj)
        if params.get("L7Clusters") is not None:
            self.L7Clusters = []
            for item in params.get("L7Clusters"):
                obj = ExtensiveCluster()
                obj._deserialize(item)
                self.L7Clusters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """键值对过滤器，用于条件过滤查询。例如过滤ID、名称等

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrafanaInfo(AbstractModel):
    """Grafana信息

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启
        :type Enabled: bool
        :param InternalURL: 内网地址
        :type InternalURL: str
        :param PublicURL: 公网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicURL: str
        :param PublicFailedReason: 公网失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicFailedReason: str
        :param PublicFailedMessage: 公网失败详细信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicFailedMessage: str
        """
        self.Enabled = None
        self.InternalURL = None
        self.PublicURL = None
        self.PublicFailedReason = None
        self.PublicFailedMessage = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.InternalURL = params.get("InternalURL")
        self.PublicURL = params.get("PublicURL")
        self.PublicFailedReason = params.get("PublicFailedReason")
        self.PublicFailedMessage = params.get("PublicFailedMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscalerSpec(AbstractModel):
    """HPA 配置

    """

    def __init__(self):
        r"""
        :param MinReplicas: 最小副本数
        :type MinReplicas: int
        :param MaxReplicas: 最大副本数
        :type MaxReplicas: int
        :param Metrics: 用于计算副本数的指标
        :type Metrics: list of MetricSpec
        """
        self.MinReplicas = None
        self.MaxReplicas = None
        self.Metrics = None


    def _deserialize(self, params):
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = MetricSpec()
                obj._deserialize(item)
                self.Metrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressGateway(AbstractModel):
    """IngressGateway 实例信息

    """

    def __init__(self):
        r"""
        :param Name: IngressGateway 实例名字
        :type Name: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param ClusterId: 集群 ID
        :type ClusterId: str
        :param Service: Service 配置
        :type Service: :class:`tencentcloud.tcm.v20210413.models.Service`
        :param Workload: Workload 配置
        :type Workload: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        :param LoadBalancer: 负载均衡配置，自动创建 CLB 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancer: :class:`tencentcloud.tcm.v20210413.models.LoadBalancer`
        :param Status: IngressGateway 状态信息，只读
        :type Status: :class:`tencentcloud.tcm.v20210413.models.IngressGatewayStatus`
        :param LoadBalancerId: 负载均衡实例ID，使用已有 CLB 时返回
        :type LoadBalancerId: str
        """
        self.Name = None
        self.Namespace = None
        self.ClusterId = None
        self.Service = None
        self.Workload = None
        self.LoadBalancer = None
        self.Status = None
        self.LoadBalancerId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.ClusterId = params.get("ClusterId")
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        if params.get("Workload") is not None:
            self.Workload = WorkloadConfig()
            self.Workload._deserialize(params.get("Workload"))
        if params.get("LoadBalancer") is not None:
            self.LoadBalancer = LoadBalancer()
            self.LoadBalancer._deserialize(params.get("LoadBalancer"))
        if params.get("Status") is not None:
            self.Status = IngressGatewayStatus()
            self.Status._deserialize(params.get("Status"))
        self.LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IngressGatewayStatus(AbstractModel):
    """IngressGateway状态

    """

    def __init__(self):
        r"""
        :param LoadBalancer: 负载均衡实例状态
        :type LoadBalancer: :class:`tencentcloud.tcm.v20210413.models.LoadBalancerStatus`
        """
        self.LoadBalancer = None


    def _deserialize(self, params):
        if params.get("LoadBalancer") is not None:
            self.LoadBalancer = LoadBalancerStatus()
            self.LoadBalancer._deserialize(params.get("LoadBalancer"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InjectConfig(AbstractModel):
    """自动注入配置

    """

    def __init__(self):
        r"""
        :param ExcludeIPRanges: 不需要进行代理的 ip 地址范围
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeIPRanges: list of str
        :param HoldApplicationUntilProxyStarts: 是否等待sidecar启动
注意：此字段可能返回 null，表示取不到有效值。
        :type HoldApplicationUntilProxyStarts: bool
        :param HoldProxyUntilApplicationEnds: 是否允许sidecar等待
注意：此字段可能返回 null，表示取不到有效值。
        :type HoldProxyUntilApplicationEnds: bool
        """
        self.ExcludeIPRanges = None
        self.HoldApplicationUntilProxyStarts = None
        self.HoldProxyUntilApplicationEnds = None


    def _deserialize(self, params):
        self.ExcludeIPRanges = params.get("ExcludeIPRanges")
        self.HoldApplicationUntilProxyStarts = params.get("HoldApplicationUntilProxyStarts")
        self.HoldProxyUntilApplicationEnds = params.get("HoldProxyUntilApplicationEnds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IstioConfig(AbstractModel):
    """Istio配置

    """

    def __init__(self):
        r"""
        :param OutboundTrafficPolicy: 外部流量策略
        :type OutboundTrafficPolicy: str
        :param Tracing: 调用链配置（Deprecated，请使用 MeshConfig.Tracing 进行配置）
        :type Tracing: :class:`tencentcloud.tcm.v20210413.models.TracingConfig`
        :param DisablePolicyChecks: 禁用策略检查功能
注意：此字段可能返回 null，表示取不到有效值。
        :type DisablePolicyChecks: bool
        :param EnablePilotHTTP: 支持HTTP1.0协议
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePilotHTTP: bool
        :param DisableHTTPRetry: 禁用HTTP重试策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DisableHTTPRetry: bool
        :param SmartDNS: SmartDNS策略
注意：此字段可能返回 null，表示取不到有效值。
        :type SmartDNS: :class:`tencentcloud.tcm.v20210413.models.SmartDNSConfig`
        """
        self.OutboundTrafficPolicy = None
        self.Tracing = None
        self.DisablePolicyChecks = None
        self.EnablePilotHTTP = None
        self.DisableHTTPRetry = None
        self.SmartDNS = None


    def _deserialize(self, params):
        self.OutboundTrafficPolicy = params.get("OutboundTrafficPolicy")
        if params.get("Tracing") is not None:
            self.Tracing = TracingConfig()
            self.Tracing._deserialize(params.get("Tracing"))
        self.DisablePolicyChecks = params.get("DisablePolicyChecks")
        self.EnablePilotHTTP = params.get("EnablePilotHTTP")
        self.DisableHTTPRetry = params.get("DisableHTTPRetry")
        if params.get("SmartDNS") is not None:
            self.SmartDNS = SmartDNSConfig()
            self.SmartDNS._deserialize(params.get("SmartDNS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IstiodConfig(AbstractModel):
    """Istiod配置

    """

    def __init__(self):
        r"""
        :param Workload: 工作负载配置
        :type Workload: :class:`tencentcloud.tcm.v20210413.models.WorkloadConfig`
        """
        self.Workload = None


    def _deserialize(self, params):
        if params.get("Workload") is not None:
            self.Workload = WorkloadConfig()
            self.Workload._deserialize(params.get("Workload"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """负载均衡配置

    """

    def __init__(self):
        r"""
        :param LoadBalancerType: 负载均衡实例的网络类型：
OPEN：公网属性， INTERNAL：内网属性。
只读。
        :type LoadBalancerType: str
        :param SubnetId: 负载均衡实例所在的子网（仅对内网VPC型LB有意义），只读。
        :type SubnetId: str
        :param InternetChargeType: TRAFFIC_POSTPAID_BY_HOUR 按流量按小时后计费 ; BANDWIDTH_POSTPAID_BY_HOUR 按带宽按小时后计费;只读。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 最大出带宽，单位Mbps，仅对公网属性的LB生效，默认值 10
        :type InternetMaxBandwidthOut: int
        :param ZoneID: 可用区 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneID: str
        :param VipIsp: 运营商类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VipIsp: str
        :param TgwGroupName: TGW Group 名
注意：此字段可能返回 null，表示取不到有效值。
        :type TgwGroupName: str
        :param AddressIPVersion: IP 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIPVersion: str
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param ExtensiveClusters: 内网独占集群配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensiveClusters: :class:`tencentcloud.tcm.v20210413.models.ExtensiveClusters`
        :param CrossRegionConfig: 负载均衡跨地域配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CrossRegionConfig: :class:`tencentcloud.tcm.v20210413.models.CrossRegionConfig`
        """
        self.LoadBalancerType = None
        self.SubnetId = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.ZoneID = None
        self.VipIsp = None
        self.TgwGroupName = None
        self.AddressIPVersion = None
        self.Tags = None
        self.ExtensiveClusters = None
        self.CrossRegionConfig = None


    def _deserialize(self, params):
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.SubnetId = params.get("SubnetId")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ZoneID = params.get("ZoneID")
        self.VipIsp = params.get("VipIsp")
        self.TgwGroupName = params.get("TgwGroupName")
        self.AddressIPVersion = params.get("AddressIPVersion")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("ExtensiveClusters") is not None:
            self.ExtensiveClusters = ExtensiveClusters()
            self.ExtensiveClusters._deserialize(params.get("ExtensiveClusters"))
        if params.get("CrossRegionConfig") is not None:
            self.CrossRegionConfig = CrossRegionConfig()
            self.CrossRegionConfig._deserialize(params.get("CrossRegionConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerStatus(AbstractModel):
    """负载均衡状态信息

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: 负载均衡实例 ID
        :type LoadBalancerId: str
        :param LoadBalancerName: 负载均衡实例名字
        :type LoadBalancerName: str
        :param LoadBalancerVip: 负载均衡实例 VIP
        :type LoadBalancerVip: str
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerVip = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVip = params.get("LoadBalancerVip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Mesh(AbstractModel):
    """Mesh信息

    """

    def __init__(self):
        r"""
        :param MeshId: Mesh实例Id
        :type MeshId: str
        :param DisplayName: Mesh名称
        :type DisplayName: str
        :param Type: Mesh类型，取值范围：
- STANDALONE：独立网格
- HOSTED：托管网格
        :type Type: str
        :param Region: 地域
        :type Region: str
        :param Version: 版本
        :type Version: str
        :param State: Mesh状态，取值范围：
- PENDING：等待中
- CREATING：创建中
- RUNNING：运行中
- ABNORMAL：异常
- UPGRADING：升级中
- CANARY_UPGRADED：升级灰度完成
- ROLLBACKING：升级回滚
- DELETING：删除中
- CREATE_FAILED：安装失败
- DELETE_FAILED：删除失败
- UPGRADE_FAILED：升级失败
- ROLLBACK_FAILED：回滚失败
        :type State: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param UpdatedTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        :param ClusterList: 集群列表
        :type ClusterList: list of Cluster
        :param Config: Mesh配置
        :type Config: :class:`tencentcloud.tcm.v20210413.models.MeshConfig`
        :param Status: Mesh详细状态
        :type Status: :class:`tencentcloud.tcm.v20210413.models.MeshStatus`
        """
        self.MeshId = None
        self.DisplayName = None
        self.Type = None
        self.Region = None
        self.Version = None
        self.State = None
        self.CreatedTime = None
        self.UpdatedTime = None
        self.ClusterList = None
        self.Config = None
        self.Status = None


    def _deserialize(self, params):
        self.MeshId = params.get("MeshId")
        self.DisplayName = params.get("DisplayName")
        self.Type = params.get("Type")
        self.Region = params.get("Region")
        self.Version = params.get("Version")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.UpdatedTime = params.get("UpdatedTime")
        if params.get("ClusterList") is not None:
            self.ClusterList = []
            for item in params.get("ClusterList"):
                obj = Cluster()
                obj._deserialize(item)
                self.ClusterList.append(obj)
        if params.get("Config") is not None:
            self.Config = MeshConfig()
            self.Config._deserialize(params.get("Config"))
        if params.get("Status") is not None:
            self.Status = MeshStatus()
            self.Status._deserialize(params.get("Status"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MeshConfig(AbstractModel):
    """网格配置项

    """

    def __init__(self):
        r"""
        :param Istio: Istio配置
        :type Istio: :class:`tencentcloud.tcm.v20210413.models.IstioConfig`
        :param AccessLog: AccessLog配置
        :type AccessLog: :class:`tencentcloud.tcm.v20210413.models.AccessLogConfig`
        :param Prometheus: Prometheus配置
        :type Prometheus: :class:`tencentcloud.tcm.v20210413.models.PrometheusConfig`
        :param Inject: 自动注入配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Inject: :class:`tencentcloud.tcm.v20210413.models.InjectConfig`
        :param Tracing: 调用跟踪配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tracing: :class:`tencentcloud.tcm.v20210413.models.TracingConfig`
        :param SidecarResources: Sidecar自定义资源
注意：此字段可能返回 null，表示取不到有效值。
        :type SidecarResources: :class:`tencentcloud.tcm.v20210413.models.ResourceRequirements`
        """
        self.Istio = None
        self.AccessLog = None
        self.Prometheus = None
        self.Inject = None
        self.Tracing = None
        self.SidecarResources = None


    def _deserialize(self, params):
        if params.get("Istio") is not None:
            self.Istio = IstioConfig()
            self.Istio._deserialize(params.get("Istio"))
        if params.get("AccessLog") is not None:
            self.AccessLog = AccessLogConfig()
            self.AccessLog._deserialize(params.get("AccessLog"))
        if params.get("Prometheus") is not None:
            self.Prometheus = PrometheusConfig()
            self.Prometheus._deserialize(params.get("Prometheus"))
        if params.get("Inject") is not None:
            self.Inject = InjectConfig()
            self.Inject._deserialize(params.get("Inject"))
        if params.get("Tracing") is not None:
            self.Tracing = TracingConfig()
            self.Tracing._deserialize(params.get("Tracing"))
        if params.get("SidecarResources") is not None:
            self.SidecarResources = ResourceRequirements()
            self.SidecarResources._deserialize(params.get("SidecarResources"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MeshStatus(AbstractModel):
    """Mesh当前状态

    """

    def __init__(self):
        r"""
        :param ServiceCount: 服务数量
        :type ServiceCount: int
        :param CanaryVersion: 灰度升级的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CanaryVersion: str
        :param Prometheus: 已废弃
注意：此字段可能返回 null，表示取不到有效值。
        :type Prometheus: list of PrometheusStatus
        :param StateMessage: 状态附带信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StateMessage: str
        :param ActiveOperationList: 正在执行的异步操作
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveOperationList: list of ActiveOperation
        :param TPS: 获取TPS信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TPS: :class:`tencentcloud.tcm.v20210413.models.PrometheusStatus`
        """
        self.ServiceCount = None
        self.CanaryVersion = None
        self.Prometheus = None
        self.StateMessage = None
        self.ActiveOperationList = None
        self.TPS = None


    def _deserialize(self, params):
        self.ServiceCount = params.get("ServiceCount")
        self.CanaryVersion = params.get("CanaryVersion")
        if params.get("Prometheus") is not None:
            self.Prometheus = []
            for item in params.get("Prometheus"):
                obj = PrometheusStatus()
                obj._deserialize(item)
                self.Prometheus.append(obj)
        self.StateMessage = params.get("StateMessage")
        if params.get("ActiveOperationList") is not None:
            self.ActiveOperationList = []
            for item in params.get("ActiveOperationList"):
                obj = ActiveOperation()
                obj._deserialize(item)
                self.ActiveOperationList.append(obj)
        if params.get("TPS") is not None:
            self.TPS = PrometheusStatus()
            self.TPS._deserialize(params.get("TPS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricSpec(AbstractModel):
    """MetricSpec 描述如何通过指定指标进行自动扩缩容

    """

    def __init__(self):
        r"""
        :param Type: 指标来源类型，支持 Pods/Resource
        :type Type: str
        :param Pods: 使用自定义指标扩进行自动扩缩容
        :type Pods: :class:`tencentcloud.tcm.v20210413.models.PodsMetricSource`
        :param Resource: 使用资源指标扩进行自动扩缩容
        :type Resource: :class:`tencentcloud.tcm.v20210413.models.ResourceMetricSource`
        """
        self.Type = None
        self.Pods = None
        self.Resource = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        if params.get("Pods") is not None:
            self.Pods = PodsMetricSource()
            self.Pods._deserialize(params.get("Pods"))
        if params.get("Resource") is not None:
            self.Resource = ResourceMetricSource()
            self.Resource._deserialize(params.get("Resource"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodsMetricSource(AbstractModel):
    """PodsMetricSource 定义了如何根据特定指标进行扩缩容

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名
        :type MetricName: str
        :param TargetAverageValue: 目标值
        :type TargetAverageValue: str
        """
        self.MetricName = None
        self.TargetAverageValue = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        self.TargetAverageValue = params.get("TargetAverageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfig(AbstractModel):
    """Prometheus 配置

    """

    def __init__(self):
        r"""
        :param VpcId: 虚拟网络Id
        :type VpcId: str
        :param SubnetId: 子网Id
        :type SubnetId: str
        :param Region: 地域
        :type Region: str
        :param InstanceId: 关联已存在实例Id，不填则默认创建
        :type InstanceId: str
        :param CustomProm: 第三方 Prometheus
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomProm: :class:`tencentcloud.tcm.v20210413.models.CustomPromConfig`
        """
        self.VpcId = None
        self.SubnetId = None
        self.Region = None
        self.InstanceId = None
        self.CustomProm = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        if params.get("CustomProm") is not None:
            self.CustomProm = CustomPromConfig()
            self.CustomProm._deserialize(params.get("CustomProm"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusStatus(AbstractModel):
    """Prometheus状态信息

    """

    def __init__(self):
        r"""
        :param PrometheusId: Prometheus Id
        :type PrometheusId: str
        :param DisplayName: 展示名称
        :type DisplayName: str
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param VpcId: 虚拟网络Id
        :type VpcId: str
        :param State: 状态
        :type State: str
        :param Region: 地区
        :type Region: str
        :param Grafana: Grafana信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Grafana: :class:`tencentcloud.tcm.v20210413.models.GrafanaInfo`
        :param Type: Prometheus 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self.PrometheusId = None
        self.DisplayName = None
        self.InstanceId = None
        self.VpcId = None
        self.State = None
        self.Region = None
        self.Grafana = None
        self.Type = None


    def _deserialize(self, params):
        self.PrometheusId = params.get("PrometheusId")
        self.DisplayName = params.get("DisplayName")
        self.InstanceId = params.get("InstanceId")
        self.VpcId = params.get("VpcId")
        self.State = params.get("State")
        self.Region = params.get("Region")
        if params.get("Grafana") is not None:
            self.Grafana = GrafanaInfo()
            self.Grafana._deserialize(params.get("Grafana"))
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Resource(AbstractModel):
    """Resource 定义了资源类型和数量

    """

    def __init__(self):
        r"""
        :param Name: 资源类型 cpu/memory
        :type Name: str
        :param Quantity: 资源数量
        :type Quantity: str
        """
        self.Name = None
        self.Quantity = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Quantity = params.get("Quantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceMetricSource(AbstractModel):
    """ResourceMetricSource 定义了如何根据已知类型的资源指标进行扩缩容

    """

    def __init__(self):
        r"""
        :param Name: 资源名称 cpu/memory
        :type Name: str
        :param TargetAverageUtilization: 目标平均利用率
        :type TargetAverageUtilization: int
        :param TargetAverageValue: 目标平均值
        :type TargetAverageValue: str
        """
        self.Name = None
        self.TargetAverageUtilization = None
        self.TargetAverageValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.TargetAverageUtilization = params.get("TargetAverageUtilization")
        self.TargetAverageValue = params.get("TargetAverageValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceRequirements(AbstractModel):
    """ResourceRequirements 描述了计算资源需求。

    """

    def __init__(self):
        r"""
        :param Limits: Limits 描述了允许的最大计算资源量。
        :type Limits: list of Resource
        :param Requests: Requests 描述所需的最小计算资源量。
        :type Requests: list of Resource
        """
        self.Limits = None
        self.Requests = None


    def _deserialize(self, params):
        if params.get("Limits") is not None:
            self.Limits = []
            for item in params.get("Limits"):
                obj = Resource()
                obj._deserialize(item)
                self.Limits.append(obj)
        if params.get("Requests") is not None:
            self.Requests = []
            for item in params.get("Requests"):
                obj = Resource()
                obj._deserialize(item)
                self.Requests.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedItems(AbstractModel):
    """选中的项目

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间
        :type Namespace: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ItemName: 选中项目名字
        :type ItemName: str
        :param Gateways: ingress gw的名称列表
        :type Gateways: list of str
        """
        self.Namespace = None
        self.ClusterName = None
        self.ItemName = None
        self.Gateways = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.ClusterName = params.get("ClusterName")
        self.ItemName = params.get("ItemName")
        self.Gateways = params.get("Gateways")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SelectedRange(AbstractModel):
    """被选中的范围

    """

    def __init__(self):
        r"""
        :param Items: 选中的项目详细内容
        :type Items: list of SelectedItems
        :param All: 是否全选
        :type All: bool
        """
        self.Items = None
        self.All = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = SelectedItems()
                obj._deserialize(item)
                self.Items.append(obj)
        self.All = params.get("All")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """Service信息

    """

    def __init__(self):
        r"""
        :param Type: ClusterIP/NodePort/LoadBalancer
        :type Type: str
        :param CLBDirectAccess: 是否开启LB直通Pod
        :type CLBDirectAccess: bool
        :param ExternalTrafficPolicy: 服务是否希望将外部流量路由到节点本地或集群范围的端点。 有两个可用选项：Cluster（默认）和 Local。Cluster 隐藏了客户端源 IP，可能导致第二跳到另一个节点；Local 保留客户端源 IP 并避免 LoadBalancer 和 NodePort 类型服务的第二跳。
        :type ExternalTrafficPolicy: str
        """
        self.Type = None
        self.CLBDirectAccess = None
        self.ExternalTrafficPolicy = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.CLBDirectAccess = params.get("CLBDirectAccess")
        self.ExternalTrafficPolicy = params.get("ExternalTrafficPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SmartDNSConfig(AbstractModel):
    """智能DNS配置

    """

    def __init__(self):
        r"""
        :param IstioMetaDNSCapture: 开启DNS代理
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioMetaDNSCapture: bool
        :param IstioMetaDNSAutoAllocate: 开启自动地址分配
注意：此字段可能返回 null，表示取不到有效值。
        :type IstioMetaDNSAutoAllocate: bool
        """
        self.IstioMetaDNSCapture = None
        self.IstioMetaDNSAutoAllocate = None


    def _deserialize(self, params):
        self.IstioMetaDNSCapture = params.get("IstioMetaDNSCapture")
        self.IstioMetaDNSAutoAllocate = params.get("IstioMetaDNSAutoAllocate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param Key: 标签键
        :type Key: str
        :param Value: 标签值
        :type Value: str
        :param Passthrough: 是否透传给其他关联产品
        :type Passthrough: bool
        """
        self.Key = None
        self.Value = None
        self.Passthrough = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Passthrough = params.get("Passthrough")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TracingConfig(AbstractModel):
    """调用链配置

    """

    def __init__(self):
        r"""
        :param Sampling: 调用链采样率，百分比
        :type Sampling: float
        :param Enable: 是否启用调用跟踪
        :type Enable: bool
        :param APM: 腾讯云 APM 服务相关参数
        :type APM: :class:`tencentcloud.tcm.v20210413.models.APM`
        :param Zipkin: 启动第三方服务器的地址
        :type Zipkin: :class:`tencentcloud.tcm.v20210413.models.TracingZipkin`
        """
        self.Sampling = None
        self.Enable = None
        self.APM = None
        self.Zipkin = None


    def _deserialize(self, params):
        self.Sampling = params.get("Sampling")
        self.Enable = params.get("Enable")
        if params.get("APM") is not None:
            self.APM = APM()
            self.APM._deserialize(params.get("APM"))
        if params.get("Zipkin") is not None:
            self.Zipkin = TracingZipkin()
            self.Zipkin._deserialize(params.get("Zipkin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TracingZipkin(AbstractModel):
    """调用追踪的Zipkin设置

    """

    def __init__(self):
        r"""
        :param Address: Zipkin调用地址
        :type Address: str
        """
        self.Address = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkloadConfig(AbstractModel):
    """工作负载配置

    """

    def __init__(self):
        r"""
        :param Replicas: 工作副本数
        :type Replicas: int
        :param Resources: 资源配置
        :type Resources: :class:`tencentcloud.tcm.v20210413.models.ResourceRequirements`
        :param HorizontalPodAutoscaler: HPA策略
        :type HorizontalPodAutoscaler: :class:`tencentcloud.tcm.v20210413.models.HorizontalPodAutoscalerSpec`
        :param SelectedNodeList: 部署到指定节点
        :type SelectedNodeList: list of str
        :param DeployMode: 组件的部署模式，取值说明：
IN_GENERAL_NODE：常规节点
IN_EKLET：eklet 节点
IN_SHARED_NODE_POOL：共享节电池
IN_EXCLUSIVE_NODE_POOL：独占节点池
        :type DeployMode: str
        """
        self.Replicas = None
        self.Resources = None
        self.HorizontalPodAutoscaler = None
        self.SelectedNodeList = None
        self.DeployMode = None


    def _deserialize(self, params):
        self.Replicas = params.get("Replicas")
        if params.get("Resources") is not None:
            self.Resources = ResourceRequirements()
            self.Resources._deserialize(params.get("Resources"))
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscalerSpec()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self.SelectedNodeList = params.get("SelectedNodeList")
        self.DeployMode = params.get("DeployMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        