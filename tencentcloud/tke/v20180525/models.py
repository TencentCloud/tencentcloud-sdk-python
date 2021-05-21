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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AcquireClusterAdminRoleRequest(AbstractModel):
    """AcquireClusterAdminRole请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AcquireClusterAdminRoleResponse(AbstractModel):
    """AcquireClusterAdminRole返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 实例列表，不支持竞价实例
        :type InstanceIds: list of str
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息(默认值)
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param HostName: 重装系统时，可以指定修改实例的HostName(集群为HostName模式时，此参数必传，规则名称除不支持大写字符外与[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口HostName一致)
        :type HostName: str
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）
        :type SecurityGroupIds: list of str
        :param NodePool: 节点池选项
        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePoolOption`
        :param SkipValidateOptions: 校验规则相关选项，可配置跳过某些校验规则。目前支持GlobalRouteCIDRCheck（跳过GlobalRouter的相关校验），VpcCniCIDRCheck（跳过VpcCni相关校验）
        :type SkipValidateOptions: list of str
        :param InstanceAdvancedSettingsOverrides: 参数InstanceAdvancedSettingsOverride数组用于定制化地配置各台instance，与InstanceIds顺序对应。当传入InstanceAdvancedSettingsOverrides数组时，将覆盖默认参数InstanceAdvancedSettings；当没有传入参数InstanceAdvancedSettingsOverrides时，InstanceAdvancedSettings参数对每台instance生效。

参数InstanceAdvancedSettingsOverride数组的长度应与InstanceIds数组一致；当长度大于InstanceIds数组长度时将报错；当长度小于InstanceIds数组时，没有对应配置的instace将使用默认配置。
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.HostName = None
        self.SecurityGroupIds = None
        self.NodePool = None
        self.SkipValidateOptions = None
        self.InstanceAdvancedSettingsOverrides = None


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
        self.HostName = params.get("HostName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("NodePool") is not None:
            self.NodePool = NodePoolOption()
            self.NodePool._deserialize(params.get("NodePool"))
        self.SkipValidateOptions = params.get("SkipValidateOptions")
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self.InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self.InstanceAdvancedSettingsOverrides.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param FailedInstanceIds: 失败的节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInstanceIds: list of str
        :param SuccInstanceIds: 成功的节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccInstanceIds: list of str
        :param TimeoutInstanceIds: 超时未返回出来节点的ID(可能失败，也可能成功)
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutInstanceIds: list of str
        :param FailedReasons: 失败的节点的失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReasons: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedInstanceIds = None
        self.SuccInstanceIds = None
        self.TimeoutInstanceIds = None
        self.FailedReasons = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.TimeoutInstanceIds = params.get("TimeoutInstanceIds")
        self.FailedReasons = params.get("FailedReasons")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddNodeToNodePoolRequest(AbstractModel):
    """AddNodeToNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param InstanceIds: 节点id
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddNodeToNodePoolResponse(AbstractModel):
    """AddNodeToNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AutoScalingGroupRange(AbstractModel):
    """集群关联的伸缩组最大实例数最小值实例数

    """

    def __init__(self):
        """
        :param MinSize: 伸缩组最小实例数
        :type MinSize: int
        :param MaxSize: 伸缩组最大实例数
        :type MaxSize: int
        """
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AutoscalingAdded(AbstractModel):
    """自动扩所容的节点

    """

    def __init__(self):
        """
        :param Joining: 正在加入中的节点数量
        :type Joining: int
        :param Initializing: 初始化中的节点数量
        :type Initializing: int
        :param Normal: 正常的节点数量
        :type Normal: int
        :param Total: 节点总数
        :type Total: int
        """
        self.Joining = None
        self.Initializing = None
        self.Normal = None
        self.Total = None


    def _deserialize(self, params):
        self.Joining = params.get("Joining")
        self.Initializing = params.get("Initializing")
        self.Normal = params.get("Normal")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CheckInstancesUpgradeAbleRequest(AbstractModel):
    """CheckInstancesUpgradeAble请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 节点列表，空为全部节点
        :type InstanceIds: list of str
        :param UpgradeType: 升级类型
        :type UpgradeType: str
        :param Offset: 分页Offset
        :type Offset: int
        :param Limit: 分页Limit
        :type Limit: int
        :param Filter: 过滤
        :type Filter: list of Filter
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.UpgradeType = None
        self.Offset = None
        self.Limit = None
        self.Filter = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.UpgradeType = params.get("UpgradeType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CheckInstancesUpgradeAbleResponse(AbstractModel):
    """CheckInstancesUpgradeAble返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterVersion: 集群master当前小版本
        :type ClusterVersion: str
        :param LatestVersion: 集群master对应的大版本目前最新小版本
        :type LatestVersion: str
        :param UpgradeAbleInstances: 可升级节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeAbleInstances: list of UpgradeAbleInstancesItem
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterVersion = None
        self.LatestVersion = None
        self.UpgradeAbleInstances = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterVersion = params.get("ClusterVersion")
        self.LatestVersion = params.get("LatestVersion")
        if params.get("UpgradeAbleInstances") is not None:
            self.UpgradeAbleInstances = []
            for item in params.get("UpgradeAbleInstances"):
                obj = UpgradeAbleInstancesItem()
                obj._deserialize(item)
                self.UpgradeAbleInstances.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param TagSpecification: 标签描述列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: list of TagSpecification
        :param ClusterStatus: 集群状态 (Running 运行中  Creating 创建中 Abnormal 异常  )
        :type ClusterStatus: str
        :param Property: 集群属性(包括集群不同属性的MAP，属性字段包括NodeNameType (lan-ip模式和hostname 模式，默认无lan-ip模式))
注意：此字段可能返回 null，表示取不到有效值。
        :type Property: str
        :param ClusterMaterNodeNum: 集群当前master数量
        :type ClusterMaterNodeNum: int
        :param ImageId: 集群使用镜像id
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param OsCustomizeType: OsCustomizeType 系统定制类型
注意：此字段可能返回 null，表示取不到有效值。
        :type OsCustomizeType: str
        :param ContainerRuntime: 集群运行环境docker或container
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerRuntime: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param DeletionProtection: 删除保护开关
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionProtection: bool
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
        self.TagSpecification = None
        self.ClusterStatus = None
        self.Property = None
        self.ClusterMaterNodeNum = None
        self.ImageId = None
        self.OsCustomizeType = None
        self.ContainerRuntime = None
        self.CreatedTime = None
        self.DeletionProtection = None


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
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.ClusterStatus = params.get("ClusterStatus")
        self.Property = params.get("Property")
        self.ClusterMaterNodeNum = params.get("ClusterMaterNodeNum")
        self.ImageId = params.get("ImageId")
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.CreatedTime = params.get("CreatedTime")
        self.DeletionProtection = params.get("DeletionProtection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param NodeNameType: 集群中节点NodeName类型（包括 hostname,lan-ip两种形式，默认为lan-ip。如果开启了hostname模式，创建节点时需要设置HostName参数，并且InstanceName需要和HostName一致）
        :type NodeNameType: str
        :param ExtraArgs: 集群自定义参数
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param NetworkType: 集群网络类型（包括GR(全局路由)和VPC-CNI两种模式，默认为GR。
        :type NetworkType: str
        :param IsNonStaticIpMode: 集群VPC-CNI模式是否为非固定IP，默认: FALSE 固定IP。
        :type IsNonStaticIpMode: bool
        :param DeletionProtection: 是否启用集群删除保护
        :type DeletionProtection: bool
        :param KubeProxyMode: 集群的网络代理模型，目前tke集群支持的网络代理模式有三种：iptables,ipvs,ipvs-bpf，此参数仅在使用ipvs-bpf模式时使用，三种网络模式的参数设置关系如下：
iptables模式：IPVS和KubeProxyMode都不设置
ipvs模式: 设置IPVS为true, KubeProxyMode不设置
ipvs-bpf模式: 设置KubeProxyMode为kube-proxy-bpf
使用ipvs-bpf的网络模式需要满足以下条件：
1. 集群版本必须为1.14及以上；
2. 系统镜像必须是: Tencent Linux 2.4；
        :type KubeProxyMode: str
        :param AuditEnabled: 是否开启审计开关
        :type AuditEnabled: bool
        :param AuditLogsetId: 审计日志上传到的logset日志集
        :type AuditLogsetId: str
        :param AuditLogTopicId: 审计日志上传到的topic
        :type AuditLogTopicId: str
        :param VpcCniType: 区分单网卡多IP模式和独立网卡模式
        :type VpcCniType: str
        :param RuntimeVersion: 运行时版本
        :type RuntimeVersion: str
        :param EnableCustomizedPodCIDR: 是否开节点podCIDR大小的自定义模式
        :type EnableCustomizedPodCIDR: bool
        :param BasePodNumber: 自定义模式下的基础pod数量
        :type BasePodNumber: int
        """
        self.IPVS = None
        self.AsEnabled = None
        self.ContainerRuntime = None
        self.NodeNameType = None
        self.ExtraArgs = None
        self.NetworkType = None
        self.IsNonStaticIpMode = None
        self.DeletionProtection = None
        self.KubeProxyMode = None
        self.AuditEnabled = None
        self.AuditLogsetId = None
        self.AuditLogTopicId = None
        self.VpcCniType = None
        self.RuntimeVersion = None
        self.EnableCustomizedPodCIDR = None
        self.BasePodNumber = None


    def _deserialize(self, params):
        self.IPVS = params.get("IPVS")
        self.AsEnabled = params.get("AsEnabled")
        self.ContainerRuntime = params.get("ContainerRuntime")
        self.NodeNameType = params.get("NodeNameType")
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = ClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.NetworkType = params.get("NetworkType")
        self.IsNonStaticIpMode = params.get("IsNonStaticIpMode")
        self.DeletionProtection = params.get("DeletionProtection")
        self.KubeProxyMode = params.get("KubeProxyMode")
        self.AuditEnabled = params.get("AuditEnabled")
        self.AuditLogsetId = params.get("AuditLogsetId")
        self.AuditLogTopicId = params.get("AuditLogTopicId")
        self.VpcCniType = params.get("VpcCniType")
        self.RuntimeVersion = params.get("RuntimeVersion")
        self.EnableCustomizedPodCIDR = params.get("EnableCustomizedPodCIDR")
        self.BasePodNumber = params.get("BasePodNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterAsGroup(AbstractModel):
    """集群关联的伸缩组信息

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param Status: 伸缩组状态(开启 enabled 开启中 enabling 关闭 disabled 关闭中 disabling 更新中 updating 删除中 deleting 开启缩容中 scaleDownEnabling 关闭缩容中 scaleDownDisabling)
        :type Status: str
        :param IsUnschedulable: 节点是否设置成不可调度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsUnschedulable: bool
        :param Labels: 伸缩组的label列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        """
        self.AutoScalingGroupId = None
        self.Status = None
        self.IsUnschedulable = None
        self.Labels = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.Status = params.get("Status")
        self.IsUnschedulable = params.get("IsUnschedulable")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterAsGroupAttribute(AbstractModel):
    """集群伸缩组属性

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param AutoScalingGroupEnabled: 是否开启
        :type AutoScalingGroupEnabled: bool
        :param AutoScalingGroupRange: 伸缩组最大最小实例数
        :type AutoScalingGroupRange: :class:`tencentcloud.tke.v20180525.models.AutoScalingGroupRange`
        """
        self.AutoScalingGroupId = None
        self.AutoScalingGroupEnabled = None
        self.AutoScalingGroupRange = None


    def _deserialize(self, params):
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.AutoScalingGroupEnabled = params.get("AutoScalingGroupEnabled")
        if params.get("AutoScalingGroupRange") is not None:
            self.AutoScalingGroupRange = AutoScalingGroupRange()
            self.AutoScalingGroupRange._deserialize(params.get("AutoScalingGroupRange"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterAsGroupOption(AbstractModel):
    """集群弹性伸缩配置

    """

    def __init__(self):
        """
        :param IsScaleDownEnabled: 是否开启缩容
注意：此字段可能返回 null，表示取不到有效值。
        :type IsScaleDownEnabled: bool
        :param Expander: 多伸缩组情况下扩容选择算法(random 随机选择，most-pods 最多类型的Pod least-waste 最少的资源浪费，默认为random)
注意：此字段可能返回 null，表示取不到有效值。
        :type Expander: str
        :param MaxEmptyBulkDelete: 最大并发缩容数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxEmptyBulkDelete: int
        :param ScaleDownDelay: 集群扩容后多少分钟开始判断缩容（默认为10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleDownDelay: int
        :param ScaleDownUnneededTime: 节点连续空闲多少分钟后被缩容（默认为 10分钟）
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleDownUnneededTime: int
        :param ScaleDownUtilizationThreshold: 节点资源使用量低于多少(百分比)时认为空闲(默认: 50(百分比))
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleDownUtilizationThreshold: int
        :param SkipNodesWithLocalStorage: 含有本地存储Pod的节点是否不缩容(默认： FALSE)
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipNodesWithLocalStorage: bool
        :param SkipNodesWithSystemPods: 含有kube-system namespace下非DaemonSet管理的Pod的节点是否不缩容 (默认： FALSE)
注意：此字段可能返回 null，表示取不到有效值。
        :type SkipNodesWithSystemPods: bool
        :param IgnoreDaemonSetsUtilization: 计算资源使用量时是否默认忽略DaemonSet的实例(默认值: False，不忽略)
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreDaemonSetsUtilization: bool
        :param OkTotalUnreadyCount: CA做健康性判断的个数，默认3，即超过OkTotalUnreadyCount个数后，CA会进行健康性判断。
注意：此字段可能返回 null，表示取不到有效值。
        :type OkTotalUnreadyCount: int
        :param MaxTotalUnreadyPercentage: 未就绪节点的最大百分比，此后CA会停止操作
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTotalUnreadyPercentage: int
        :param ScaleDownUnreadyTime: 表示未准备就绪的节点在有资格进行缩减之前应该停留多长时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleDownUnreadyTime: int
        :param UnregisteredNodeRemovalTime: CA删除未在Kubernetes中注册的节点之前等待的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UnregisteredNodeRemovalTime: int
        """
        self.IsScaleDownEnabled = None
        self.Expander = None
        self.MaxEmptyBulkDelete = None
        self.ScaleDownDelay = None
        self.ScaleDownUnneededTime = None
        self.ScaleDownUtilizationThreshold = None
        self.SkipNodesWithLocalStorage = None
        self.SkipNodesWithSystemPods = None
        self.IgnoreDaemonSetsUtilization = None
        self.OkTotalUnreadyCount = None
        self.MaxTotalUnreadyPercentage = None
        self.ScaleDownUnreadyTime = None
        self.UnregisteredNodeRemovalTime = None


    def _deserialize(self, params):
        self.IsScaleDownEnabled = params.get("IsScaleDownEnabled")
        self.Expander = params.get("Expander")
        self.MaxEmptyBulkDelete = params.get("MaxEmptyBulkDelete")
        self.ScaleDownDelay = params.get("ScaleDownDelay")
        self.ScaleDownUnneededTime = params.get("ScaleDownUnneededTime")
        self.ScaleDownUtilizationThreshold = params.get("ScaleDownUtilizationThreshold")
        self.SkipNodesWithLocalStorage = params.get("SkipNodesWithLocalStorage")
        self.SkipNodesWithSystemPods = params.get("SkipNodesWithSystemPods")
        self.IgnoreDaemonSetsUtilization = params.get("IgnoreDaemonSetsUtilization")
        self.OkTotalUnreadyCount = params.get("OkTotalUnreadyCount")
        self.MaxTotalUnreadyPercentage = params.get("MaxTotalUnreadyPercentage")
        self.ScaleDownUnreadyTime = params.get("ScaleDownUnreadyTime")
        self.UnregisteredNodeRemovalTime = params.get("UnregisteredNodeRemovalTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到集群实例。
        :type TagSpecification: list of TagSpecification
        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
        :type OsCustomizeType: str
        :param NeedWorkSecurityGroup: 是否开启节点的默认安全组(默认: 否，Aphla特性)
        :type NeedWorkSecurityGroup: bool
        """
        self.ClusterOs = None
        self.ClusterVersion = None
        self.ClusterName = None
        self.ClusterDescription = None
        self.VpcId = None
        self.ProjectId = None
        self.TagSpecification = None
        self.OsCustomizeType = None
        self.NeedWorkSecurityGroup = None


    def _deserialize(self, params):
        self.ClusterOs = params.get("ClusterOs")
        self.ClusterVersion = params.get("ClusterVersion")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDescription = params.get("ClusterDescription")
        self.VpcId = params.get("VpcId")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.NeedWorkSecurityGroup = params.get("NeedWorkSecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterCIDRSettings(AbstractModel):
    """集群容器网络相关参数

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用于分配集群容器和服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突。且网段范围必须在内网网段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 冲突错误, 默认不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量。取值范围4～256。不为2的幂值时会向上取最接近的2的幂值。
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service数量。取值范围32～32768，不为2的幂值时会向上取最接近的2的幂值。
        :type MaxClusterServiceNum: int
        :param ServiceCIDR: 用于分配集群服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突。且网段范围必须在内网网段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。
        :type ServiceCIDR: str
        :param EniSubnetIds: VPC-CNI网络模式下，弹性网卡的子网Id。
        :type EniSubnetIds: list of str
        :param ClaimExpiredSeconds: VPC-CNI网络模式下，弹性网卡IP的回收时间，取值范围[300,15768000)
        :type ClaimExpiredSeconds: int
        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.ServiceCIDR = None
        self.EniSubnetIds = None
        self.ClaimExpiredSeconds = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.EniSubnetIds = params.get("EniSubnetIds")
        self.ClaimExpiredSeconds = params.get("ClaimExpiredSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterCredential(AbstractModel):
    """接入k8s 的认证信息

    """

    def __init__(self):
        """
        :param CACert: CA 根证书
        :type CACert: str
        :param Token: 认证用的Token
        :type Token: str
        """
        self.CACert = None
        self.Token = None


    def _deserialize(self, params):
        self.CACert = params.get("CACert")
        self.Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterExtraArgs(AbstractModel):
    """集群master自定义参数

    """

    def __init__(self):
        """
        :param KubeAPIServer: kube-apiserver自定义参数，参数格式为["k1=v1", "k1=v2"]， 例如["max-requests-inflight=500","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeAPIServer: list of str
        :param KubeControllerManager: kube-controller-manager自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeControllerManager: list of str
        :param KubeScheduler: kube-scheduler自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeScheduler: list of str
        :param Etcd: etcd自定义参数，只支持独立集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Etcd: list of str
        """
        self.KubeAPIServer = None
        self.KubeControllerManager = None
        self.KubeScheduler = None
        self.Etcd = None


    def _deserialize(self, params):
        self.KubeAPIServer = params.get("KubeAPIServer")
        self.KubeControllerManager = params.get("KubeControllerManager")
        self.KubeScheduler = params.get("KubeScheduler")
        self.Etcd = params.get("Etcd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterInternalLB(AbstractModel):
    """弹性容器集群内网访问LB信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启内网访问LB
        :type Enabled: bool
        :param SubnetId: 内网访问LB关联的子网Id
        :type SubnetId: str
        """
        self.Enabled = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterPublicLB(AbstractModel):
    """弹性容器集群公网访问负载均衡信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启公网访问LB
        :type Enabled: bool
        :param AllowFromCidrs: 允许访问的来源CIDR列表
        :type AllowFromCidrs: list of str
        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)
        :type SecurityPolicies: list of str
        """
        self.Enabled = None
        self.AllowFromCidrs = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.AllowFromCidrs = params.get("AllowFromCidrs")
        self.SecurityPolicies = params.get("SecurityPolicies")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClusterVersion(AbstractModel):
    """集群版本信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Versions: 集群主版本号列表，例如1.18.4
        :type Versions: list of str
        """
        self.ClusterId = None
        self.Versions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Versions = params.get("Versions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CommonName(AbstractModel):
    """账户UIN与客户端证书CommonName的映射

    """

    def __init__(self):
        """
        :param SubaccountUin: 子账户UIN
        :type SubaccountUin: str
        :param CN: 子账户客户端证书中的CommonName字段
        :type CN: str
        """
        self.SubaccountUin = None
        self.CN = None


    def _deserialize(self, params):
        self.SubaccountUin = params.get("SubaccountUin")
        self.CN = params.get("CN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterAsGroupRequest(AbstractModel):
    """CreateClusterAsGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AutoScalingGroupPara: 伸缩组创建透传参数，json化字符串格式，详见[伸缩组创建实例](https://cloud.tencent.com/document/api/377/20440)接口。LaunchConfigurationId由LaunchConfigurePara参数创建，不支持填写
        :type AutoScalingGroupPara: str
        :param LaunchConfigurePara: 启动配置创建透传参数，json化字符串格式，详见[创建启动配置](https://cloud.tencent.com/document/api/377/20447)接口。另外ImageId参数由于集群维度已经有的ImageId信息，这个字段不需要填写。UserData字段设置通过UserScript设置，这个字段不需要填写。
        :type LaunchConfigurePara: str
        :param InstanceAdvancedSettings: 节点高级配置信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param Labels: 节点Label数组
        :type Labels: list of Label
        """
        self.ClusterId = None
        self.AutoScalingGroupPara = None
        self.LaunchConfigurePara = None
        self.InstanceAdvancedSettings = None
        self.Labels = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupPara = params.get("AutoScalingGroupPara")
        self.LaunchConfigurePara = params.get("LaunchConfigurePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterAsGroupResponse(AbstractModel):
    """CreateClusterAsGroup返回参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 启动配置ID
        :type LaunchConfigurationId: str
        :param AutoScalingGroupId: 伸缩组ID
        :type AutoScalingGroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LaunchConfigurationId = None
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SubnetId: 集群端口所在的子网ID  (仅在开启非外网访问时需要填，必须为集群所在VPC内的子网)
        :type SubnetId: str
        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.SubnetId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetId = params.get("SubnetId")
        self.IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterEndpointResponse(AbstractModel):
    """CreateClusterEndpoint返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterEndpointVipRequest(AbstractModel):
    """CreateClusterEndpointVip请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)
        :type SecurityPolicies: list of str
        """
        self.ClusterId = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip返回参数结构体

    """

    def __init__(self):
        """
        :param RequestFlowId: 请求任务的FlowId
        :type RequestFlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestFlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestFlowId = params.get("RequestFlowId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段
        :type ClusterId: str
        :param RunInstancePara: CVM创建透传参数，json化字符串格式，如需要保证扩展集群节点请求幂等性需要在此参数添加ClientToken字段，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。
        :type RunInstancePara: str
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param SkipValidateOptions: 校验规则相关选项，可配置跳过某些校验规则。目前支持GlobalRouteCIDRCheck（跳过GlobalRouter的相关校验），VpcCniCIDRCheck（跳过VpcCni相关校验）
        :type SkipValidateOptions: list of str
        """
        self.ClusterId = None
        self.RunInstancePara = None
        self.InstanceAdvancedSettings = None
        self.SkipValidateOptions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RunInstancePara = params.get("RunInstancePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.SkipValidateOptions = params.get("SkipValidateOptions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterNodePoolFromExistingAsgRequest(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AutoscalingGroupId: 伸缩组ID
        :type AutoscalingGroupId: str
        """
        self.ClusterId = None
        self.AutoscalingGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterNodePoolFromExistingAsgResponse(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg返回参数结构体

    """

    def __init__(self):
        """
        :param NodePoolId: 节点池ID
        :type NodePoolId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodePoolId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterNodePoolRequest(AbstractModel):
    """CreateClusterNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: cluster id
        :type ClusterId: str
        :param AutoScalingGroupPara: AutoScalingGroupPara AS组参数
        :type AutoScalingGroupPara: str
        :param LaunchConfigurePara: LaunchConfigurePara 运行参数
        :type LaunchConfigurePara: str
        :param InstanceAdvancedSettings: InstanceAdvancedSettings 示例参数
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnableAutoscale: 是否启用自动伸缩
        :type EnableAutoscale: bool
        :param Name: 节点池名称
        :type Name: str
        :param Labels: Labels标签
        :type Labels: list of Label
        :param Taints: Taints互斥
        :type Taints: list of Taint
        :param NodePoolOs: 节点池os
        :type NodePoolOs: str
        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
        :type OsCustomizeType: str
        """
        self.ClusterId = None
        self.AutoScalingGroupPara = None
        self.LaunchConfigurePara = None
        self.InstanceAdvancedSettings = None
        self.EnableAutoscale = None
        self.Name = None
        self.Labels = None
        self.Taints = None
        self.NodePoolOs = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupPara = params.get("AutoScalingGroupPara")
        self.LaunchConfigurePara = params.get("LaunchConfigurePara")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.EnableAutoscale = params.get("EnableAutoscale")
        self.Name = params.get("Name")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        self.NodePoolOs = params.get("NodePoolOs")
        self.OsCustomizeType = params.get("OsCustomizeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterNodePoolResponse(AbstractModel):
    """CreateClusterNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodePoolId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: 集群容器网络配置信息
        :type ClusterCIDRSettings: :class:`tencentcloud.tke.v20180525.models.ClusterCIDRSettings`
        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。
        :type ClusterType: str
        :param RunInstancesForNode: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。总机型(包括地域)数量不超过10个，相同机型(地域)购买多台机器可以通过设置参数中RunInstances中InstanceCount来实现。
        :type RunInstancesForNode: list of RunInstancesForNode
        :param ClusterBasicSettings: 集群的基本配置信息
        :type ClusterBasicSettings: :class:`tencentcloud.tke.v20180525.models.ClusterBasicSettings`
        :param ClusterAdvancedSettings: 集群高级配置信息
        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.ClusterAdvancedSettings`
        :param InstanceAdvancedSettings: 节点高级配置信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param ExistedInstancesForNode: 已存在实例的配置信息。所有实例必须在同一个VPC中，最大数量不超过100。
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        :param InstanceDataDiskMountSettings: CVM类型和其对应的数据盘挂载配置信息
        :type InstanceDataDiskMountSettings: list of InstanceDataDiskMountSetting
        :param ExtensionAddons: 需要安装的扩展组件信息
        :type ExtensionAddons: list of ExtensionAddon
        """
        self.ClusterCIDRSettings = None
        self.ClusterType = None
        self.RunInstancesForNode = None
        self.ClusterBasicSettings = None
        self.ClusterAdvancedSettings = None
        self.InstanceAdvancedSettings = None
        self.ExistedInstancesForNode = None
        self.InstanceDataDiskMountSettings = None
        self.ExtensionAddons = None


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
        if params.get("InstanceDataDiskMountSettings") is not None:
            self.InstanceDataDiskMountSettings = []
            for item in params.get("InstanceDataDiskMountSettings"):
                obj = InstanceDataDiskMountSetting()
                obj._deserialize(item)
                self.InstanceDataDiskMountSettings.append(obj)
        if params.get("ExtensionAddons") is not None:
            self.ExtensionAddons = []
            for item in params.get("ExtensionAddons"):
                obj = ExtensionAddon()
                obj._deserialize(item)
                self.ExtensionAddons.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateEKSClusterRequest(AbstractModel):
    """CreateEKSCluster请求参数结构体

    """

    def __init__(self):
        """
        :param K8SVersion: k8s版本号。可为1.14.4, 1.12.8。
        :type K8SVersion: str
        :param VpcId: vpc 的Id
        :type VpcId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param SubnetIds: 子网Id 列表
        :type SubnetIds: list of str
        :param ClusterDesc: 集群描述信息
        :type ClusterDesc: str
        :param ServiceSubnetId: Serivce 所在子网Id
        :type ServiceSubnetId: str
        :param DnsServers: 集群自定义的Dns服务器信息
        :type DnsServers: list of DnsServerConf
        :param ExtraParam: 扩展参数。须是map[string]string 的json 格式。
        :type ExtraParam: str
        :param EnableVpcCoreDNS: 是否在用户集群内开启Dns。默认为true
        :type EnableVpcCoreDNS: bool
        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到集群实例。
        :type TagSpecification: list of TagSpecification
        """
        self.K8SVersion = None
        self.VpcId = None
        self.ClusterName = None
        self.SubnetIds = None
        self.ClusterDesc = None
        self.ServiceSubnetId = None
        self.DnsServers = None
        self.ExtraParam = None
        self.EnableVpcCoreDNS = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.K8SVersion = params.get("K8SVersion")
        self.VpcId = params.get("VpcId")
        self.ClusterName = params.get("ClusterName")
        self.SubnetIds = params.get("SubnetIds")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ServiceSubnetId = params.get("ServiceSubnetId")
        if params.get("DnsServers") is not None:
            self.DnsServers = []
            for item in params.get("DnsServers"):
                obj = DnsServerConf()
                obj._deserialize(item)
                self.DnsServers.append(obj)
        self.ExtraParam = params.get("ExtraParam")
        self.EnableVpcCoreDNS = params.get("EnableVpcCoreDNS")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateEKSClusterResponse(AbstractModel):
    """CreateEKSCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 弹性集群Id
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePrometheusDashboardRequest(AbstractModel):
    """CreatePrometheusDashboard请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param DashboardName: 面板组名称
        :type DashboardName: str
        :param Contents: 面板列表
每一项是一个grafana dashboard的json定义
        :type Contents: list of str
        """
        self.InstanceId = None
        self.DashboardName = None
        self.Contents = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DashboardName = params.get("DashboardName")
        self.Contents = params.get("Contents")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePrometheusDashboardResponse(AbstractModel):
    """CreatePrometheusDashboard返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePrometheusTemplateRequest(AbstractModel):
    """CreatePrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Template: 模板设置
        :type Template: :class:`tencentcloud.tke.v20180525.models.PrometheusTemplate`
        """
        self.Template = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = PrometheusTemplate()
            self.Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreatePrometheusTemplateResponse(AbstractModel):
    """CreatePrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id
        :type TemplateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DataDisk(AbstractModel):
    """描述了k8s节点数据盘相关配置与信息。

    """

    def __init__(self):
        """
        :param DiskType: 云盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param FileSystem: 文件系统(ext3/ext4/xfs)
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystem: str
        :param DiskSize: 云盘大小(G）
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param AutoFormatAndMount: 是否自动化格式盘并挂载
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoFormatAndMount: bool
        :param MountTarget: 挂载目录
注意：此字段可能返回 null，表示取不到有效值。
        :type MountTarget: str
        """
        self.DiskType = None
        self.FileSystem = None
        self.DiskSize = None
        self.AutoFormatAndMount = None
        self.MountTarget = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.FileSystem = params.get("FileSystem")
        self.DiskSize = params.get("DiskSize")
        self.AutoFormatAndMount = params.get("AutoFormatAndMount")
        self.MountTarget = params.get("MountTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID，通过[DescribeClusters](https://cloud.tencent.com/document/api/457/31862)接口获取。
        :type ClusterId: str
        :param AutoScalingGroupIds: 集群伸缩组ID的列表
        :type AutoScalingGroupIds: list of str
        :param KeepInstance: 是否保留伸缩组中的节点(默认值： false(不保留))
        :type KeepInstance: bool
        """
        self.ClusterId = None
        self.AutoScalingGroupIds = None
        self.KeepInstance = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self.KeepInstance = params.get("KeepInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterEndpointRequest(AbstractModel):
    """DeleteClusterEndpoint请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterEndpointVipRequest(AbstractModel):
    """DeleteClusterEndpointVip请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param ForceDelete: 是否强制删除(当节点在初始化时，可以指定参数为TRUE)
        :type ForceDelete: bool
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.InstanceDeleteMode = None
        self.ForceDelete = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        self.ForceDelete = params.get("ForceDelete")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param SuccInstanceIds: 删除成功的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccInstanceIds: list of str
        :param FailedInstanceIds: 删除失败的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInstanceIds: list of str
        :param NotFoundInstanceIds: 未匹配到的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NotFoundInstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccInstanceIds = None
        self.FailedInstanceIds = None
        self.NotFoundInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.NotFoundInstanceIds = params.get("NotFoundInstanceIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterNodePoolRequest(AbstractModel):
    """DeleteClusterNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 节点池对应的 ClusterId
        :type ClusterId: str
        :param NodePoolIds: 需要删除的节点池 Id 列表
        :type NodePoolIds: list of str
        :param KeepInstance: 删除节点池时是否保留节点池内节点(节点仍然会被移出集群，但对应的实例不会被销毁)
        :type KeepInstance: bool
        """
        self.ClusterId = None
        self.NodePoolIds = None
        self.KeepInstance = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolIds = params.get("NodePoolIds")
        self.KeepInstance = params.get("KeepInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterNodePoolResponse(AbstractModel):
    """DeleteClusterNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceDeleteMode: 集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）
        :type InstanceDeleteMode: str
        :param ResourceDeleteOptions: 集群删除时资源的删除策略，目前支持CBS（默认保留CBS）
        :type ResourceDeleteOptions: list of ResourceDeleteOption
        """
        self.ClusterId = None
        self.InstanceDeleteMode = None
        self.ResourceDeleteOptions = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        if params.get("ResourceDeleteOptions") is not None:
            self.ResourceDeleteOptions = []
            for item in params.get("ResourceDeleteOptions"):
                obj = ResourceDeleteOption()
                obj._deserialize(item)
                self.ResourceDeleteOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteEKSClusterRequest(AbstractModel):
    """DeleteEKSCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 弹性集群Id
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteEKSClusterResponse(AbstractModel):
    """DeleteEKSCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePrometheusTemplateRequest(AbstractModel):
    """DeletePrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板id
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePrometheusTemplateResponse(AbstractModel):
    """DeletePrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePrometheusTemplateSyncRequest(AbstractModel):
    """DeletePrometheusTemplateSync请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板id
        :type TemplateId: str
        :param Targets: 取消同步的对象列表
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self.TemplateId = None
        self.Targets = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeletePrometheusTemplateSyncResponse(AbstractModel):
    """DeletePrometheusTemplateSync返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAvailableClusterVersionRequest(AbstractModel):
    """DescribeAvailableClusterVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 Id
        :type ClusterId: str
        :param ClusterIds: 集群 Id 列表
        :type ClusterIds: list of str
        """
        self.ClusterId = None
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeAvailableClusterVersionResponse(AbstractModel):
    """DescribeAvailableClusterVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Versions: 可升级的集群版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of str
        :param Clusters: 集群信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Clusters: list of ClusterVersion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Versions = None
        self.Clusters = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Versions = params.get("Versions")
        if params.get("Clusters") is not None:
            self.Clusters = []
            for item in params.get("Clusters"):
                obj = ClusterVersion()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterAsGroupOption: 集群弹性伸缩属性
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterAsGroupOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterAsGroupOption") is not None:
            self.ClusterAsGroupOption = ClusterAsGroupOption()
            self.ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterAsGroupsRequest(AbstractModel):
    """DescribeClusterAsGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AutoScalingGroupIds: 伸缩组ID列表，如果为空，表示拉取集群关联的所有伸缩组。
        :type AutoScalingGroupIds: list of str
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ClusterId = None
        self.AutoScalingGroupIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AutoScalingGroupIds = params.get("AutoScalingGroupIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群关联的伸缩组总数
        :type TotalCount: int
        :param ClusterAsGroupSet: 集群关联的伸缩组列表
        :type ClusterAsGroupSet: list of ClusterAsGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterAsGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterAsGroupSet") is not None:
            self.ClusterAsGroupSet = []
            for item in params.get("ClusterAsGroupSet"):
                obj = ClusterAsGroup()
                obj._deserialize(item)
                self.ClusterAsGroupSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterCommonNamesRequest(AbstractModel):
    """DescribeClusterCommonNames请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SubaccountUins: 子账户列表，不可超出最大值50
        :type SubaccountUins: list of str
        :param RoleIds: 角色ID列表，不可超出最大值50
        :type RoleIds: list of str
        """
        self.ClusterId = None
        self.SubaccountUins = None
        self.RoleIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubaccountUins = params.get("SubaccountUins")
        self.RoleIds = params.get("RoleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterCommonNamesResponse(AbstractModel):
    """DescribeClusterCommonNames返回参数结构体

    """

    def __init__(self):
        """
        :param CommonNames: 子账户Uin与其客户端证书的CN字段映射
        :type CommonNames: list of CommonName
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CommonNames = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CommonNames") is not None:
            self.CommonNames = []
            for item in params.get("CommonNames"):
                obj = CommonName()
                obj._deserialize(item)
                self.CommonNames.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterEndpointStatusRequest(AbstractModel):
    """DescribeClusterEndpointStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）
        :type IsExtranet: bool
        """
        self.ClusterId = None
        self.IsExtranet = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 查询集群访问端口状态（Created 开启成功，Creating 开启中，NotFound 未开启）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrorMsg: 开启访问入口失败信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 端口操作状态 (Creating 创建中  CreateFailed 创建失败 Created 创建完成 Deleting 删除中 DeletedFailed 删除失败 Deleted 已删除 NotFound 未发现操作 )
        :type Status: str
        :param ErrorMsg: 操作失败的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param InstanceIds: 需要获取的节点实例Id列表。如果为空，表示拉取集群下所有节点实例。
        :type InstanceIds: list of str
        :param InstanceRole: 节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER。默认为WORKER类型。
        :type InstanceRole: str
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceRole = params.get("InstanceRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterKubeconfigRequest(AbstractModel):
    """DescribeClusterKubeconfig请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterKubeconfigResponse(AbstractModel):
    """DescribeClusterKubeconfig返回参数结构体

    """

    def __init__(self):
        """
        :param Kubeconfig: 子账户kubeconfig文件，可用于直接访问集群kube-apiserver
        :type Kubeconfig: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Kubeconfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Kubeconfig = params.get("Kubeconfig")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterNodePoolDetailRequest(AbstractModel):
    """DescribeClusterNodePoolDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        """
        self.ClusterId = None
        self.NodePoolId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterNodePoolDetailResponse(AbstractModel):
    """DescribeClusterNodePoolDetail返回参数结构体

    """

    def __init__(self):
        """
        :param NodePool: 节点池详情
        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePool`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodePool = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodePool") is not None:
            self.NodePool = NodePool()
            self.NodePool._deserialize(params.get("NodePool"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterNodePoolsRequest(AbstractModel):
    """DescribeClusterNodePools请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: ClusterId（集群id）
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterNodePoolsResponse(AbstractModel):
    """DescribeClusterNodePools返回参数结构体

    """

    def __init__(self):
        """
        :param NodePoolSet: NodePools（节点池列表）
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolSet: list of NodePool
        :param TotalCount: 资源总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodePoolSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodePoolSet") is not None:
            self.NodePoolSet = []
            for item in params.get("NodePoolSet"):
                obj = NodePool()
                obj._deserialize(item)
                self.NodePoolSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeClusterRoutesRequest(AbstractModel):
    """DescribeClusterRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param Filters: 过滤条件,当前只支持按照单个条件GatewayIP进行过滤（可选）
        :type Filters: list of Filter
        """
        self.RouteTableName = None
        self.Filters = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityPolicy: list of str
        :param Kubeconfig: 集群Kubeconfig文件
注意：此字段可能返回 null，表示取不到有效值。
        :type Kubeconfig: str
        :param JnsGwEndpoint: 集群JnsGw的访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type JnsGwEndpoint: str
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
        self.Kubeconfig = None
        self.JnsGwEndpoint = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        self.CertificationAuthority = params.get("CertificationAuthority")
        self.ClusterExternalEndpoint = params.get("ClusterExternalEndpoint")
        self.Domain = params.get("Domain")
        self.PgwEndpoint = params.get("PgwEndpoint")
        self.SecurityPolicy = params.get("SecurityPolicy")
        self.Kubeconfig = params.get("Kubeconfig")
        self.JnsGwEndpoint = params.get("JnsGwEndpoint")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param Limit: 最大输出条数，默认20，最大为100
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEKSClusterCredentialRequest(AbstractModel):
    """DescribeEKSClusterCredential请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEKSClusterCredentialResponse(AbstractModel):
    """DescribeEKSClusterCredential返回参数结构体

    """

    def __init__(self):
        """
        :param Addresses: 集群的接入地址信息
        :type Addresses: list of IPAddress
        :param Credential: 集群的认证信息
        :type Credential: :class:`tencentcloud.tke.v20180525.models.ClusterCredential`
        :param PublicLB: 集群的公网访问信息
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.ClusterPublicLB`
        :param InternalLB: 集群的内网访问信息
        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.ClusterInternalLB`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Addresses = None
        self.Credential = None
        self.PublicLB = None
        self.InternalLB = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Addresses") is not None:
            self.Addresses = []
            for item in params.get("Addresses"):
                obj = IPAddress()
                obj._deserialize(item)
                self.Addresses.append(obj)
        if params.get("Credential") is not None:
            self.Credential = ClusterCredential()
            self.Credential._deserialize(params.get("Credential"))
        if params.get("PublicLB") is not None:
            self.PublicLB = ClusterPublicLB()
            self.PublicLB._deserialize(params.get("PublicLB"))
        if params.get("InternalLB") is not None:
            self.InternalLB = ClusterInternalLB()
            self.InternalLB._deserialize(params.get("InternalLB"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEKSClustersRequest(AbstractModel):
    """DescribeEKSClusters请求参数结构体

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEKSClustersResponse(AbstractModel):
    """DescribeEKSClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群总个数
        :type TotalCount: int
        :param Clusters: 集群信息列表
        :type Clusters: list of EksCluster
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
                obj = EksCluster()
                obj._deserialize(item)
                self.Clusters.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEnableVpcCniProgressRequest(AbstractModel):
    """DescribeEnableVpcCniProgress请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 开启vpc-cni的集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEnableVpcCniProgressResponse(AbstractModel):
    """DescribeEnableVpcCniProgress返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务进度的描述：Running/Succeed/Failed
        :type Status: str
        :param ErrorMessage: 当任务进度为Failed时，对任务状态的进一步描述，例如IPAMD组件安装失败
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写查询集群列表 接口中返回的 ClusterId 字段（仅通过ClusterId获取需要过滤条件中的VPCID。节点状态比较时会使用该地域下所有集群中的节点进行比较。参数不支持同时指定InstanceIds和ClusterId。
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
        :param IpAddresses: 根据多个实例IP进行过滤
        :type IpAddresses: list of str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Filters = None
        self.VagueIpAddress = None
        self.VagueInstanceName = None
        self.Offset = None
        self.Limit = None
        self.IpAddresses = None


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
        self.IpAddresses = params.get("IpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 镜像数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ImageInstanceSet: 镜像信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageInstanceSet: list of ImageInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageInstanceSet") is not None:
            self.ImageInstanceSet = []
            for item in params.get("ImageInstanceSet"):
                obj = ImageInstance()
                obj._deserialize(item)
                self.ImageInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAgentInstancesRequest(AbstractModel):
    """DescribePrometheusAgentInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
可以是tke, eks, edge的集群id
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAgentInstancesResponse(AbstractModel):
    """DescribePrometheusAgentInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Instances: 关联该集群的实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Instances: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Instances = params.get("Instances")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAgentsRequest(AbstractModel):
    """DescribePrometheusAgents请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Offset: 用于分页
        :type Offset: int
        :param Limit: 用于分页
        :type Limit: int
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAgentsResponse(AbstractModel):
    """DescribePrometheusAgents返回参数结构体

    """

    def __init__(self):
        """
        :param Agents: 被关联集群信息
        :type Agents: list of PrometheusAgentOverview
        :param Total: 被关联集群总量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Agents = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Agents") is not None:
            self.Agents = []
            for item in params.get("Agents"):
                obj = PrometheusAgentOverview()
                obj._deserialize(item)
                self.Agents.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAlertHistoryRequest(AbstractModel):
    """DescribePrometheusAlertHistory请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param RuleName: 告警名称
        :type RuleName: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Labels: label集合
        :type Labels: str
        :param Offset: 分片
        :type Offset: int
        :param Limit: 分片
        :type Limit: int
        """
        self.InstanceId = None
        self.RuleName = None
        self.StartTime = None
        self.EndTime = None
        self.Labels = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RuleName = params.get("RuleName")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Labels = params.get("Labels")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAlertHistoryResponse(AbstractModel):
    """DescribePrometheusAlertHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Items: 告警历史
        :type Items: list of PrometheusAlertHistoryItem
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = PrometheusAlertHistoryItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAlertRuleRequest(AbstractModel):
    """DescribePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Offset: 分页
        :type Offset: int
        :param Limit: 分页
        :type Limit: int
        :param Filters: 过滤
支持ID，Name
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusAlertRuleResponse(AbstractModel):
    """DescribePrometheusAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param AlertRules: 告警详情
        :type AlertRules: list of PrometheusAlertRuleDetail
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AlertRules = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AlertRules") is not None:
            self.AlertRules = []
            for item in params.get("AlertRules"):
                obj = PrometheusAlertRuleDetail()
                obj._deserialize(item)
                self.AlertRules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusOverviewsRequest(AbstractModel):
    """DescribePrometheusOverviews请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 用于分页
        :type Offset: int
        :param Limit: 用于分页
        :type Limit: int
        :param Filters: 过滤实例，目前支持：
ID: 通过实例ID来过滤 
Name: 通过实例名称来过滤
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusOverviewsResponse(AbstractModel):
    """DescribePrometheusOverviews返回参数结构体

    """

    def __init__(self):
        """
        :param Instances: 实例列表
        :type Instances: list of PrometheusInstanceOverview
        :param Total: 实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = PrometheusInstanceOverview()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusTargetsRequest(AbstractModel):
    """DescribePrometheusTargets请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param ClusterType: 集群类型
        :type ClusterType: str
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Filters: 过滤条件，当前支持
Name=state
Value=up, down, unknown
        :type Filters: list of Filter
        """
        self.InstanceId = None
        self.ClusterType = None
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ClusterType = params.get("ClusterType")
        self.ClusterId = params.get("ClusterId")
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusTargetsResponse(AbstractModel):
    """DescribePrometheusTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Jobs: 所有Job的targets信息
        :type Jobs: list of PrometheusJobTargets
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Jobs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Jobs") is not None:
            self.Jobs = []
            for item in params.get("Jobs"):
                obj = PrometheusJobTargets()
                obj._deserialize(item)
                self.Jobs.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusTemplateSyncRequest(AbstractModel):
    """DescribePrometheusTemplateSync请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusTemplateSyncResponse(AbstractModel):
    """DescribePrometheusTemplateSync返回参数结构体

    """

    def __init__(self):
        """
        :param Targets: 同步目标详情
        :type Targets: list of PrometheusTemplateSyncTarget
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Targets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusTemplatesRequest(AbstractModel):
    """DescribePrometheusTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 模糊过滤条件，支持
Level 按模板级别过滤
Name 按名称过滤
Describe 按描述过滤
ID 按templateId过滤
        :type Filters: list of Filter
        :param Offset: 分页偏移
        :type Offset: int
        :param Limit: 总数限制
        :type Limit: int
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePrometheusTemplatesResponse(AbstractModel):
    """DescribePrometheusTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param Templates: 模板列表
        :type Templates: list of PrometheusTemplate
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = PrometheusTemplate()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 地域的数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RegionInstanceSet: 地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionInstanceSet: list of RegionInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RegionInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RegionInstanceSet") is not None:
            self.RegionInstanceSet = []
            for item in params.get("RegionInstanceSet"):
                obj = RegionInstance()
                obj._deserialize(item)
                self.RegionInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DnsServerConf(AbstractModel):
    """Eks 自定义域名服务器 配置

    """

    def __init__(self):
        """
        :param Domain: 域名。空字符串表示所有域名。
        :type Domain: str
        :param DnsServers: dns 服务器地址列表。地址格式 ip:port
        :type DnsServers: list of str
        """
        self.Domain = None
        self.DnsServers = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.DnsServers = params.get("DnsServers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EksCluster(AbstractModel):
    """弹性集群信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param VpcId: Vpc Id
        :type VpcId: str
        :param SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param K8SVersion: k8s 版本号
        :type K8SVersion: str
        :param Status: 集群状态(running运行中，initializing 初始化中，failed异常)
        :type Status: str
        :param ClusterDesc: 集群描述信息
        :type ClusterDesc: str
        :param CreatedTime: 集群创建时间
        :type CreatedTime: str
        :param ServiceSubnetId: Service 子网Id
        :type ServiceSubnetId: str
        :param DnsServers: 集群的自定义dns 服务器信息
        :type DnsServers: list of DnsServerConf
        :param NeedDeleteCbs: 将来删除集群时是否要删除cbs。默认为 FALSE
        :type NeedDeleteCbs: bool
        :param EnableVpcCoreDNS: 是否在用户集群内开启Dns。默认为TRUE
        :type EnableVpcCoreDNS: bool
        :param TagSpecification: 标签描述列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSpecification: list of TagSpecification
        """
        self.ClusterId = None
        self.ClusterName = None
        self.VpcId = None
        self.SubnetIds = None
        self.K8SVersion = None
        self.Status = None
        self.ClusterDesc = None
        self.CreatedTime = None
        self.ServiceSubnetId = None
        self.DnsServers = None
        self.NeedDeleteCbs = None
        self.EnableVpcCoreDNS = None
        self.TagSpecification = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")
        self.K8SVersion = params.get("K8SVersion")
        self.Status = params.get("Status")
        self.ClusterDesc = params.get("ClusterDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ServiceSubnetId = params.get("ServiceSubnetId")
        if params.get("DnsServers") is not None:
            self.DnsServers = []
            for item in params.get("DnsServers"):
                obj = DnsServerConf()
                obj._deserialize(item)
                self.DnsServers.append(obj)
        self.NeedDeleteCbs = params.get("NeedDeleteCbs")
        self.EnableVpcCoreDNS = params.get("EnableVpcCoreDNS")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableVpcCniNetworkTypeRequest(AbstractModel):
    """EnableVpcCniNetworkType请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param VpcCniType: 开启vpc-cni的模式，tke-route-eni开启的是策略路由模式，tke-direct-eni开启的是独立网卡模式
        :type VpcCniType: str
        :param EnableStaticIp: 是否开启固定IP模式
        :type EnableStaticIp: bool
        :param Subnets: 使用的容器子网
        :type Subnets: list of str
        :param ExpiredSeconds: 在固定IP模式下，Pod销毁后退还IP的时间，传参必须大于300；不传默认IP永不销毁。
        :type ExpiredSeconds: int
        """
        self.ClusterId = None
        self.VpcCniType = None
        self.EnableStaticIp = None
        self.Subnets = None
        self.ExpiredSeconds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.VpcCniType = params.get("VpcCniType")
        self.EnableStaticIp = params.get("EnableStaticIp")
        self.Subnets = params.get("Subnets")
        self.ExpiredSeconds = params.get("ExpiredSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableVpcCniNetworkTypeResponse(AbstractModel):
    """EnableVpcCniNetworkType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        :param CreatedTime: 创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
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
        :param AutoscalingGroupId: 伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupId: str
        :param InstanceChargeType: 实例计费模式。取值范围： PREPAID：表示预付费，即包年包月 POSTPAID_BY_HOUR：表示后付费，即按量计费 CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        """
        self.Usable = None
        self.UnusableReason = None
        self.AlreadyInCluster = None
        self.InstanceId = None
        self.InstanceName = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None
        self.CreatedTime = None
        self.CPU = None
        self.Memory = None
        self.OsName = None
        self.InstanceType = None
        self.AutoscalingGroupId = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.Usable = params.get("Usable")
        self.UnusableReason = params.get("UnusableReason")
        self.AlreadyInCluster = params.get("AlreadyInCluster")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.CreatedTime = params.get("CreatedTime")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.OsName = params.get("OsName")
        self.InstanceType = params.get("InstanceType")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExistedInstancesForNode(AbstractModel):
    """不同角色的已存在节点配置参数

    """

    def __init__(self):
        """
        :param NodeRole: 节点角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在创建 INDEPENDENT_CLUSTER 独立集群时需要指定。MASTER_ETCD节点数量为3～7，建议为奇数。MASTER_ETCD最小配置为4C8G。
        :type NodeRole: str
        :param ExistedInstancesPara: 已存在实例的重装参数
        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`
        :param InstanceAdvancedSettingsOverride: 节点高级设置，会覆盖集群级别设置的InstanceAdvancedSettings（当前只对节点自定义参数ExtraArgs生效）
        :type InstanceAdvancedSettingsOverride: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param DesiredPodNumbers: 自定义模式集群，可指定每个节点的pod数量
        :type DesiredPodNumbers: list of int
        """
        self.NodeRole = None
        self.ExistedInstancesPara = None
        self.InstanceAdvancedSettingsOverride = None
        self.DesiredPodNumbers = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        if params.get("ExistedInstancesPara") is not None:
            self.ExistedInstancesPara = ExistedInstancesPara()
            self.ExistedInstancesPara._deserialize(params.get("ExistedInstancesPara"))
        if params.get("InstanceAdvancedSettingsOverride") is not None:
            self.InstanceAdvancedSettingsOverride = InstanceAdvancedSettings()
            self.InstanceAdvancedSettingsOverride._deserialize(params.get("InstanceAdvancedSettingsOverride"))
        self.DesiredPodNumbers = params.get("DesiredPodNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param HostName: 重装系统时，可以指定修改实例的HostName(集群为HostName模式时，此参数必传，规则名称除不支持大写字符外与[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口HostName一致)
        :type HostName: str
        """
        self.InstanceIds = None
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.HostName = None


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
        self.HostName = params.get("HostName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ExtensionAddon(AbstractModel):
    """创建集群时，选择安装的扩展组件的信息

    """

    def __init__(self):
        """
        :param AddonName: 扩展组件名称
        :type AddonName: str
        :param AddonParam: 扩展组件信息(扩展组件资源对象的json字符串描述)
        :type AddonParam: str
        """
        self.AddonName = None
        self.AddonParam = None


    def _deserialize(self, params):
        self.AddonName = params.get("AddonName")
        self.AddonParam = params.get("AddonParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/15728)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
    ```
    Filters.0.Name=zone
    &Filters.0.Values.0=ap-guangzhou-1
    &Filters.1.Name=instance-charge-type
    &Filters.1.Values.0=PREPAID
    &Filters.1.Values.1=POSTPAID_BY_HOUR
    ```

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetUpgradeInstanceProgressRequest(AbstractModel):
    """GetUpgradeInstanceProgress请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Limit: 最多获取多少个节点的进度
        :type Limit: int
        :param Offset: 从第几个节点开始获取进度
        :type Offset: int
        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetUpgradeInstanceProgressResponse(AbstractModel):
    """GetUpgradeInstanceProgress返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 升级节点总数
        :type Total: int
        :param Done: 已升级节点总数
        :type Done: int
        :param LifeState: 升级任务生命周期
process 运行中
paused 已停止
pauing 正在停止
done  已完成
timeout 已超时
aborted 已取消
        :type LifeState: str
        :param Instances: 各节点升级进度详情
        :type Instances: list of InstanceUpgradeProgressItem
        :param ClusterStatus: 集群当前状态
        :type ClusterStatus: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradeClusterStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Done = None
        self.LifeState = None
        self.Instances = None
        self.ClusterStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Done = params.get("Done")
        self.LifeState = params.get("LifeState")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = InstanceUpgradeProgressItem()
                obj._deserialize(item)
                self.Instances.append(obj)
        if params.get("ClusterStatus") is not None:
            self.ClusterStatus = InstanceUpgradeClusterStatus()
            self.ClusterStatus._deserialize(params.get("ClusterStatus"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IPAddress(AbstractModel):
    """IP 地址

    """

    def __init__(self):
        """
        :param Type: Ip 地址的类型。可为 advertise, public 等
        :type Type: str
        :param Ip: Ip 地址
        :type Ip: str
        :param Port: 网络端口
        :type Port: int
        """
        self.Type = None
        self.Ip = None
        self.Port = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Ip = params.get("Ip")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImageInstance(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        """
        :param Alias: 镜像别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param OsName: 操作系统名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OsName: str
        :param ImageId: 镜像ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
注意：此字段可能返回 null，表示取不到有效值。
        :type OsCustomizeType: str
        """
        self.Alias = None
        self.OsName = None
        self.ImageId = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.OsName = params.get("OsName")
        self.ImageId = params.get("ImageId")
        self.OsCustomizeType = params.get("OsCustomizeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param DrainStatus: 实例是否封锁状态
注意：此字段可能返回 null，表示取不到有效值。
        :type DrainStatus: str
        :param InstanceAdvancedSettings: 节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param CreatedTime: 添加时间
        :type CreatedTime: str
        :param LanIP: 节点内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIP: str
        :param NodePoolId: 资源池ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolId: str
        :param AutoscalingGroupId: 自动伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupId: str
        """
        self.InstanceId = None
        self.InstanceRole = None
        self.FailedReason = None
        self.InstanceState = None
        self.DrainStatus = None
        self.InstanceAdvancedSettings = None
        self.CreatedTime = None
        self.LanIP = None
        self.NodePoolId = None
        self.AutoscalingGroupId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRole = params.get("InstanceRole")
        self.FailedReason = params.get("FailedReason")
        self.InstanceState = params.get("InstanceState")
        self.DrainStatus = params.get("DrainStatus")
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self.CreatedTime = params.get("CreatedTime")
        self.LanIP = params.get("LanIP")
        self.NodePoolId = params.get("NodePoolId")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相关配置与信息。

    """

    def __init__(self):
        """
        :param MountTarget: 数据盘挂载点, 默认不挂载数据盘. 已格式化的 ext3，ext4，xfs 文件系统的数据盘将直接挂载，其他文件系统或未格式化的数据盘将自动格式化为ext4 (tlinux系统格式化成xfs)并挂载，请注意备份数据! 无数据盘或有多块数据盘的云主机此设置不生效。
注意，注意，多盘场景请使用下方的DataDisks数据结构，设置对应的云盘类型、云盘大小、挂载路径、是否格式化等信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type MountTarget: str
        :param DockerGraphPath: dockerd --graph 指定值, 默认为 /var/lib/docker
注意：此字段可能返回 null，表示取不到有效值。
        :type DockerGraphPath: str
        :param UserScript: base64 编码的用户脚本, 此脚本会在 k8s 组件运行后执行, 需要用户保证脚本的可重入及重试逻辑, 脚本及其生成的日志文件可在节点的 /data/ccs_userscript/ 路径查看, 如果要求节点需要在进行初始化完成后才可加入调度, 可配合 unschedulable 参数使用, 在 userScript 最后初始化完成后, 添加 kubectl uncordon nodename --kubeconfig=/root/.kube/config 命令使节点加入调度
注意：此字段可能返回 null，表示取不到有效值。
        :type UserScript: str
        :param Unschedulable: 设置加入的节点是否参与调度，默认值为0，表示参与调度；非0表示不参与调度, 待节点初始化完成之后, 可执行kubectl uncordon nodename使node加入调度.
        :type Unschedulable: int
        :param Labels: 节点Label数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param DataDisks: 多盘数据盘挂载信息，同时请确保购买CVM的参数传递了购买多个数据盘的信息，如添加节点CreateClusterInstances API的RunInstancesPara下的DataDisks也设置了购买多个数据盘, 具体可以参考CreateClusterInstances接口的，添加集群节点(多块数据盘)样例；注意：此参数在调用接口AddExistedInstances时不起作用
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        :param ExtraArgs: 节点相关的自定义参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        :param DesiredPodNumber: 该节点属于podCIDR大小自定义模式时，可指定节点上运行的pod数量上限
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredPodNumber: int
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None
        self.Labels = None
        self.DataDisks = None
        self.ExtraArgs = None
        self.DesiredPodNumber = None


    def _deserialize(self, params):
        self.MountTarget = params.get("MountTarget")
        self.DockerGraphPath = params.get("DockerGraphPath")
        self.UserScript = params.get("UserScript")
        self.Unschedulable = params.get("Unschedulable")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = InstanceExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.DesiredPodNumber = params.get("DesiredPodNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceDataDiskMountSetting(AbstractModel):
    """CVM实例数据盘挂载配置

    """

    def __init__(self):
        """
        :param InstanceType: CVM实例类型
        :type InstanceType: str
        :param DataDisks: 数据盘挂载信息
        :type DataDisks: list of DataDisk
        :param Zone: CVM实例所属可用区
        :type Zone: str
        """
        self.InstanceType = None
        self.DataDisks = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceExtraArgs(AbstractModel):
    """节点自定义参数

    """

    def __init__(self):
        """
        :param Kubelet: kubelet自定义参数，参数格式为["k1=v1", "k1=v2"]， 例如["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
注意：此字段可能返回 null，表示取不到有效值。
        :type Kubelet: list of str
        """
        self.Kubelet = None


    def _deserialize(self, params):
        self.Kubelet = params.get("Kubelet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceUpgradeClusterStatus(AbstractModel):
    """节点升级过程中集群当前状态

    """

    def __init__(self):
        """
        :param PodTotal: pod总数
        :type PodTotal: int
        :param NotReadyPod: NotReady pod总数
        :type NotReadyPod: int
        """
        self.PodTotal = None
        self.NotReadyPod = None


    def _deserialize(self, params):
        self.PodTotal = params.get("PodTotal")
        self.NotReadyPod = params.get("NotReadyPod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceUpgradePreCheckResult(AbstractModel):
    """某个节点升级前检查结果

    """

    def __init__(self):
        """
        :param CheckPass: 检查是否通过
        :type CheckPass: bool
        :param Items: 检查项数组
        :type Items: list of InstanceUpgradePreCheckResultItem
        :param SinglePods: 本节点独立pod列表
        :type SinglePods: list of str
        """
        self.CheckPass = None
        self.Items = None
        self.SinglePods = None


    def _deserialize(self, params):
        self.CheckPass = params.get("CheckPass")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceUpgradePreCheckResultItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.SinglePods = params.get("SinglePods")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceUpgradePreCheckResultItem(AbstractModel):
    """节点升级检查项结果

    """

    def __init__(self):
        """
        :param Namespace: 工作负载的命名空间
        :type Namespace: str
        :param WorkLoadKind: 工作负载类型
        :type WorkLoadKind: str
        :param WorkLoadName: 工作负载名称
        :type WorkLoadName: str
        :param Before: 驱逐节点前工作负载running的pod数目
        :type Before: int
        :param After: 驱逐节点后工作负载running的pod数目
        :type After: int
        :param Pods: 工作负载在本节点上的pod列表
        :type Pods: list of str
        """
        self.Namespace = None
        self.WorkLoadKind = None
        self.WorkLoadName = None
        self.Before = None
        self.After = None
        self.Pods = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.WorkLoadKind = params.get("WorkLoadKind")
        self.WorkLoadName = params.get("WorkLoadName")
        self.Before = params.get("Before")
        self.After = params.get("After")
        self.Pods = params.get("Pods")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class InstanceUpgradeProgressItem(AbstractModel):
    """某个节点的升级进度

    """

    def __init__(self):
        """
        :param InstanceID: 节点instanceID
        :type InstanceID: str
        :param LifeState: 任务生命周期
process 运行中
paused 已停止
pauing 正在停止
done  已完成
timeout 已超时
aborted 已取消
pending 还未开始
        :type LifeState: str
        :param StartAt: 升级开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param EndAt: 升级结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndAt: str
        :param CheckResult: 升级前检查结果
        :type CheckResult: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradePreCheckResult`
        :param Detail: 升级步骤详情
        :type Detail: list of TaskStepInfo
        """
        self.InstanceID = None
        self.LifeState = None
        self.StartAt = None
        self.EndAt = None
        self.CheckResult = None
        self.Detail = None


    def _deserialize(self, params):
        self.InstanceID = params.get("InstanceID")
        self.LifeState = params.get("LifeState")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        if params.get("CheckResult") is not None:
            self.CheckResult = InstanceUpgradePreCheckResult()
            self.CheckResult._deserialize(params.get("CheckResult"))
        if params.get("Detail") is not None:
            self.Detail = []
            for item in params.get("Detail"):
                obj = TaskStepInfo()
                obj._deserialize(item)
                self.Detail.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Label(AbstractModel):
    """k8s中标签，一般以数组的方式存在

    """

    def __init__(self):
        """
        :param Name: map表中的Name
        :type Name: str
        :param Value: map表中的Value
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        """
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type Password: str
        :param KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口[DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699)获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ManuallyAdded(AbstractModel):
    """手动加入的节点

    """

    def __init__(self):
        """
        :param Joining: 加入中的节点数量
        :type Joining: int
        :param Initializing: 初始化中的节点数量
        :type Initializing: int
        :param Normal: 正常的节点数量
        :type Normal: int
        :param Total: 节点总数
        :type Total: int
        """
        self.Joining = None
        self.Initializing = None
        self.Normal = None
        self.Total = None


    def _deserialize(self, params):
        self.Joining = params.get("Joining")
        self.Initializing = params.get("Initializing")
        self.Normal = params.get("Normal")
        self.Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterAsGroupAttribute: 集群关联的伸缩组属性
        :type ClusterAsGroupAttribute: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupAttribute`
        """
        self.ClusterId = None
        self.ClusterAsGroupAttribute = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupAttribute") is not None:
            self.ClusterAsGroupAttribute = ClusterAsGroupAttribute()
            self.ClusterAsGroupAttribute._deserialize(params.get("ClusterAsGroupAttribute"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterAsGroupOptionAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterAsGroupOption: 集群弹性伸缩属性
        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`
        """
        self.ClusterId = None
        self.ClusterAsGroupOption = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ClusterAsGroupOption") is not None:
            self.ClusterAsGroupOption = ClusterAsGroupOption()
            self.ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterAsGroupOptionAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterAttributeRequest(AbstractModel):
    """ModifyClusterAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ProjectId: 集群所属项目
        :type ProjectId: int
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterDesc: 集群描述
        :type ClusterDesc: str
        """
        self.ClusterId = None
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterAttributeResponse(AbstractModel):
    """ModifyClusterAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 集群所属项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterDesc: 集群描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)
        :type SecurityPolicies: list of str
        """
        self.ClusterId = None
        self.SecurityPolicies = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SecurityPolicies = params.get("SecurityPolicies")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterNodePoolRequest(AbstractModel):
    """ModifyClusterNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NodePoolId: 节点池ID
        :type NodePoolId: str
        :param Name: 名称
        :type Name: str
        :param MaxNodesNum: 最大节点数
        :type MaxNodesNum: int
        :param MinNodesNum: 最小节点数
        :type MinNodesNum: int
        :param Labels: 标签
        :type Labels: list of Label
        :param Taints: 污点
        :type Taints: list of Taint
        :param EnableAutoscale: 是否开启伸缩
        :type EnableAutoscale: bool
        :param OsName: 操作系统名称
        :type OsName: str
        :param OsCustomizeType: 镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
        :type OsCustomizeType: str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.Name = None
        self.MaxNodesNum = None
        self.MinNodesNum = None
        self.Labels = None
        self.Taints = None
        self.EnableAutoscale = None
        self.OsName = None
        self.OsCustomizeType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.Name = params.get("Name")
        self.MaxNodesNum = params.get("MaxNodesNum")
        self.MinNodesNum = params.get("MinNodesNum")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        self.EnableAutoscale = params.get("EnableAutoscale")
        self.OsName = params.get("OsName")
        self.OsCustomizeType = params.get("OsCustomizeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyClusterNodePoolResponse(AbstractModel):
    """ModifyClusterNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyNodePoolDesiredCapacityAboutAsgRequest(AbstractModel):
    """ModifyNodePoolDesiredCapacityAboutAsg请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param DesiredCapacity: 节点池所关联的伸缩组的期望实例数
        :type DesiredCapacity: int
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.DesiredCapacity = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.DesiredCapacity = params.get("DesiredCapacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyNodePoolDesiredCapacityAboutAsgResponse(AbstractModel):
    """ModifyNodePoolDesiredCapacityAboutAsg返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPrometheusTemplateRequest(AbstractModel):
    """ModifyPrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param Template: 修改内容
        :type Template: :class:`tencentcloud.tke.v20180525.models.PrometheusTemplateModify`
        """
        self.TemplateId = None
        self.Template = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Template") is not None:
            self.Template = PrometheusTemplateModify()
            self.Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ModifyPrometheusTemplateResponse(AbstractModel):
    """ModifyPrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class NodeCountSummary(AbstractModel):
    """节点统计列表

    """

    def __init__(self):
        """
        :param ManuallyAdded: 手动管理的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ManuallyAdded: :class:`tencentcloud.tke.v20180525.models.ManuallyAdded`
        :param AutoscalingAdded: 自动管理的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingAdded: :class:`tencentcloud.tke.v20180525.models.AutoscalingAdded`
        """
        self.ManuallyAdded = None
        self.AutoscalingAdded = None


    def _deserialize(self, params):
        if params.get("ManuallyAdded") is not None:
            self.ManuallyAdded = ManuallyAdded()
            self.ManuallyAdded._deserialize(params.get("ManuallyAdded"))
        if params.get("AutoscalingAdded") is not None:
            self.AutoscalingAdded = AutoscalingAdded()
            self.AutoscalingAdded._deserialize(params.get("AutoscalingAdded"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class NodePool(AbstractModel):
    """节点池描述

    """

    def __init__(self):
        """
        :param NodePoolId: NodePoolId 资源池id
        :type NodePoolId: str
        :param Name: Name 资源池名称
        :type Name: str
        :param ClusterInstanceId: ClusterInstanceId 集群实例id
        :type ClusterInstanceId: str
        :param LifeState: LifeState 状态，当前节点池生命周期状态包括：creating，normal，updating，deleting，deleted
        :type LifeState: str
        :param LaunchConfigurationId: LaunchConfigurationId 配置
        :type LaunchConfigurationId: str
        :param AutoscalingGroupId: AutoscalingGroupId 分组id
        :type AutoscalingGroupId: str
        :param Labels: Labels 标签
        :type Labels: list of Label
        :param Taints: Taints 污点标记
        :type Taints: list of Taint
        :param NodeCountSummary: NodeCountSummary 节点列表
        :type NodeCountSummary: :class:`tencentcloud.tke.v20180525.models.NodeCountSummary`
        :param AutoscalingGroupStatus: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupStatus: str
        :param MaxNodesNum: 最大节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNodesNum: int
        :param MinNodesNum: 最小节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinNodesNum: int
        :param DesiredNodesNum: 期望的节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredNodesNum: int
        :param NodePoolOs: 节点池osName
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolOs: str
        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
注意：此字段可能返回 null，表示取不到有效值。
        :type OsCustomizeType: str
        :param ImageId: 镜像id
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param DesiredPodNum: 集群属于节点podCIDR大小自定义模式时，节点池需要带上pod数量属性
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredPodNum: int
        :param UserScript: 用户自定义脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type UserScript: str
        """
        self.NodePoolId = None
        self.Name = None
        self.ClusterInstanceId = None
        self.LifeState = None
        self.LaunchConfigurationId = None
        self.AutoscalingGroupId = None
        self.Labels = None
        self.Taints = None
        self.NodeCountSummary = None
        self.AutoscalingGroupStatus = None
        self.MaxNodesNum = None
        self.MinNodesNum = None
        self.DesiredNodesNum = None
        self.NodePoolOs = None
        self.OsCustomizeType = None
        self.ImageId = None
        self.DesiredPodNum = None
        self.UserScript = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.Name = params.get("Name")
        self.ClusterInstanceId = params.get("ClusterInstanceId")
        self.LifeState = params.get("LifeState")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoscalingGroupId = params.get("AutoscalingGroupId")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Taints") is not None:
            self.Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self.Taints.append(obj)
        if params.get("NodeCountSummary") is not None:
            self.NodeCountSummary = NodeCountSummary()
            self.NodeCountSummary._deserialize(params.get("NodeCountSummary"))
        self.AutoscalingGroupStatus = params.get("AutoscalingGroupStatus")
        self.MaxNodesNum = params.get("MaxNodesNum")
        self.MinNodesNum = params.get("MinNodesNum")
        self.DesiredNodesNum = params.get("DesiredNodesNum")
        self.NodePoolOs = params.get("NodePoolOs")
        self.OsCustomizeType = params.get("OsCustomizeType")
        self.ImageId = params.get("ImageId")
        self.DesiredPodNum = params.get("DesiredPodNum")
        self.UserScript = params.get("UserScript")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class NodePoolOption(AbstractModel):
    """加入存量节点时的节点池选项

    """

    def __init__(self):
        """
        :param AddToNodePool: 是否加入节点池
        :type AddToNodePool: bool
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param InheritConfigurationFromNodePool: 是否继承节点池相关配置
        :type InheritConfigurationFromNodePool: bool
        """
        self.AddToNodePool = None
        self.NodePoolId = None
        self.InheritConfigurationFromNodePool = None


    def _deserialize(self, params):
        self.AddToNodePool = params.get("AddToNodePool")
        self.NodePoolId = params.get("NodePoolId")
        self.InheritConfigurationFromNodePool = params.get("InheritConfigurationFromNodePool")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusAgentOverview(AbstractModel):
    """托管prometheus agent概览

    """

    def __init__(self):
        """
        :param ClusterType: 集群类型
        :type ClusterType: str
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Status: agent状态
normal = 正常
abnormal = 异常
        :type Status: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        """
        self.ClusterType = None
        self.ClusterId = None
        self.Status = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterType = params.get("ClusterType")
        self.ClusterId = params.get("ClusterId")
        self.Status = params.get("Status")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusAlertHistoryItem(AbstractModel):
    """prometheus告警历史

    """

    def __init__(self):
        """
        :param RuleName: 告警名称
        :type RuleName: str
        :param StartTime: 告警开始时间
        :type StartTime: str
        :param Content: 告警内容
        :type Content: str
        :param State: 告警状态
注意：此字段可能返回 null，表示取不到有效值。
        :type State: str
        :param RuleItem: 触发的规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleItem: str
        :param TopicId: 告警渠道的id
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param TopicName: 告警渠道的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        """
        self.RuleName = None
        self.StartTime = None
        self.Content = None
        self.State = None
        self.RuleItem = None
        self.TopicId = None
        self.TopicName = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        self.StartTime = params.get("StartTime")
        self.Content = params.get("Content")
        self.State = params.get("State")
        self.RuleItem = params.get("RuleItem")
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusAlertRule(AbstractModel):
    """Prometheus告警规则

    """

    def __init__(self):
        """
        :param Name: 规则名称
        :type Name: str
        :param Rule: prometheus语句
        :type Rule: str
        :param Labels: 额外标签
        :type Labels: list of Label
        :param Template: 告警发送模板
        :type Template: str
        :param For: 持续时间
        :type For: str
        :param Describe: 该条规则的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        """
        self.Name = None
        self.Rule = None
        self.Labels = None
        self.Template = None
        self.For = None
        self.Describe = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Rule = params.get("Rule")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.Template = params.get("Template")
        self.For = params.get("For")
        self.Describe = params.get("Describe")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusAlertRuleDetail(AbstractModel):
    """托管prometheus告警配置实例

    """

    def __init__(self):
        """
        :param Name: 规则名称
        :type Name: str
        :param Rules: 规则列表
        :type Rules: list of PrometheusAlertRule
        :param UpdatedAt: 最后修改时间
        :type UpdatedAt: str
        :param Notification: 告警渠道
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotification`
        :param Id: 告警 id
        :type Id: str
        :param TemplateId: 如果该告警来至模板下发，则TemplateId为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param Interval: 计算周期
注意：此字段可能返回 null，表示取不到有效值。
        :type Interval: str
        """
        self.Name = None
        self.Rules = None
        self.UpdatedAt = None
        self.Notification = None
        self.Id = None
        self.TemplateId = None
        self.Interval = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.UpdatedAt = params.get("UpdatedAt")
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotification()
            self.Notification._deserialize(params.get("Notification"))
        self.Id = params.get("Id")
        self.TemplateId = params.get("TemplateId")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusConfigItem(AbstractModel):
    """prometheus配置

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Config: 配置内容
        :type Config: str
        :param TemplateId: 用于出参，如果该配置来至模板，则为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        """
        self.Name = None
        self.Config = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Config = params.get("Config")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusInstanceOverview(AbstractModel):
    """托管prometheus实例概览

    """

    def __init__(self):
        """
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Name: 实例名称
        :type Name: str
        :param VpcId: 实例vpcId
        :type VpcId: str
        :param SubnetId: 实例子网Id
        :type SubnetId: str
        :param Status: 实例当前的状态
prepare_env = 初始化环境
install_suit = 安装组件
running = 运行中
        :type Status: str
        :param COSBucket: COS桶存储
        :type COSBucket: str
        """
        self.InstanceId = None
        self.Name = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.COSBucket = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.COSBucket = params.get("COSBucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusJobTargets(AbstractModel):
    """prometheus一个job的targets

    """

    def __init__(self):
        """
        :param Targets: 该Job的targets列表
        :type Targets: list of PrometheusTarget
        :param JobName: job的名称
        :type JobName: str
        :param Total: targets总数
        :type Total: int
        :param Up: 健康的target总数
        :type Up: int
        """
        self.Targets = None
        self.JobName = None
        self.Total = None
        self.Up = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.JobName = params.get("JobName")
        self.Total = params.get("Total")
        self.Up = params.get("Up")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusNotification(AbstractModel):
    """amp告警渠道配置

    """

    def __init__(self):
        """
        :param Enabled: 是否启用
        :type Enabled: bool
        :param RepeatInterval: 收敛时间
        :type RepeatInterval: str
        :param TimeRangeStart: 生效起始时间
        :type TimeRangeStart: str
        :param TimeRangeEnd: 生效结束时间
        :type TimeRangeEnd: str
        :param NotifyWay: 告警通知方式。目前有SMS、EMAIL、CALL、WECHAT方式。
分别代表：短信、邮件、电话、微信
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param ReceiverGroups: 告警接收组（用户组）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverGroups: list of int non-negative
        :param PhoneNotifyOrder: 电话告警顺序。
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNotifyOrder: list of int non-negative
        :param PhoneCircleTimes: 电话告警次数。
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleTimes: int
        :param PhoneInnerInterval: 电话告警轮内间隔。单位：秒
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneInnerInterval: int
        :param PhoneCircleInterval: 电话告警轮外间隔。单位：秒
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneCircleInterval: int
        :param PhoneArriveNotice: 电话告警触达通知
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneArriveNotice: bool
        :param Type: 通道类型，默认为amp，支持以下
amp
webhook
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param WebHook: 如果Type为webhook, 则该字段为必填项
注意：此字段可能返回 null，表示取不到有效值。
        :type WebHook: str
        """
        self.Enabled = None
        self.RepeatInterval = None
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.NotifyWay = None
        self.ReceiverGroups = None
        self.PhoneNotifyOrder = None
        self.PhoneCircleTimes = None
        self.PhoneInnerInterval = None
        self.PhoneCircleInterval = None
        self.PhoneArriveNotice = None
        self.Type = None
        self.WebHook = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.RepeatInterval = params.get("RepeatInterval")
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        self.NotifyWay = params.get("NotifyWay")
        self.ReceiverGroups = params.get("ReceiverGroups")
        self.PhoneNotifyOrder = params.get("PhoneNotifyOrder")
        self.PhoneCircleTimes = params.get("PhoneCircleTimes")
        self.PhoneInnerInterval = params.get("PhoneInnerInterval")
        self.PhoneCircleInterval = params.get("PhoneCircleInterval")
        self.PhoneArriveNotice = params.get("PhoneArriveNotice")
        self.Type = params.get("Type")
        self.WebHook = params.get("WebHook")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusTarget(AbstractModel):
    """prometheus一个抓取目标的信息

    """

    def __init__(self):
        """
        :param Url: 抓取目标的URL
        :type Url: str
        :param State: target当前状态,当前支持
up = 健康
down = 不健康
unknown = 未知
        :type State: str
        :param Labels: target的元label
        :type Labels: list of Label
        :param LastScrape: 上一次抓取的时间
        :type LastScrape: str
        :param ScrapeDuration: 上一次抓取的耗时，单位是s
        :type ScrapeDuration: float
        :param Error: 上一次抓取如果错误，该字段存储错误信息
        :type Error: str
        """
        self.Url = None
        self.State = None
        self.Labels = None
        self.LastScrape = None
        self.ScrapeDuration = None
        self.Error = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.State = params.get("State")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.LastScrape = params.get("LastScrape")
        self.ScrapeDuration = params.get("ScrapeDuration")
        self.Error = params.get("Error")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusTemplate(AbstractModel):
    """模板实例

    """

    def __init__(self):
        """
        :param Name: 模板名称
        :type Name: str
        :param Level: 模板维度，支持以下类型
instance 实例级别
cluster 集群级别
        :type Level: str
        :param Describe: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param AlertRules: 当Level为instance时有效，
模板中的告警配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRules: list of PrometheusAlertRule
        :param RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordRules: list of PrometheusConfigItem
        :param ServiceMonitors: 当Level为cluster时有效，
模板中的ServiceMonitor规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMonitors: list of PrometheusConfigItem
        :param PodMonitors: 当Level为cluster时有效，
模板中的PodMonitors规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodMonitors: list of PrometheusConfigItem
        :param RawJobs: 当Level为cluster时有效，
模板中的RawJobs规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RawJobs: list of PrometheusConfigItem
        :param TemplateId: 模板的ID, 用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param UpdateTime: 最近更新时间，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param Version: 当前版本，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param IsDefault: 是否系统提供的默认模板，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefault: bool
        :param AlertDetailRules: 当Level为instance时有效，
模板中的告警配置列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertDetailRules: list of PrometheusAlertRuleDetail
        """
        self.Name = None
        self.Level = None
        self.Describe = None
        self.AlertRules = None
        self.RecordRules = None
        self.ServiceMonitors = None
        self.PodMonitors = None
        self.RawJobs = None
        self.TemplateId = None
        self.UpdateTime = None
        self.Version = None
        self.IsDefault = None
        self.AlertDetailRules = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Describe = params.get("Describe")
        if params.get("AlertRules") is not None:
            self.AlertRules = []
            for item in params.get("AlertRules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self.AlertRules.append(obj)
        if params.get("RecordRules") is not None:
            self.RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RecordRules.append(obj)
        if params.get("ServiceMonitors") is not None:
            self.ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self.PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self.RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RawJobs.append(obj)
        self.TemplateId = params.get("TemplateId")
        self.UpdateTime = params.get("UpdateTime")
        self.Version = params.get("Version")
        self.IsDefault = params.get("IsDefault")
        if params.get("AlertDetailRules") is not None:
            self.AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertRuleDetail()
                obj._deserialize(item)
                self.AlertDetailRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusTemplateModify(AbstractModel):
    """云原生Prometheus模板可修改项

    """

    def __init__(self):
        """
        :param Name: 修改名称
        :type Name: str
        :param Describe: 修改描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param AlertRules: 修改内容，只有当模板类型是Alert时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRules: list of PrometheusAlertRule
        :param RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordRules: list of PrometheusConfigItem
        :param ServiceMonitors: 当Level为cluster时有效，
模板中的ServiceMonitor规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMonitors: list of PrometheusConfigItem
        :param PodMonitors: 当Level为cluster时有效，
模板中的PodMonitors规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodMonitors: list of PrometheusConfigItem
        :param RawJobs: 当Level为cluster时有效，
模板中的RawJobs规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RawJobs: list of PrometheusConfigItem
        :param AlertDetailRules: 修改内容，只有当模板类型是Alert时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertDetailRules: list of PrometheusAlertRuleDetail
        """
        self.Name = None
        self.Describe = None
        self.AlertRules = None
        self.RecordRules = None
        self.ServiceMonitors = None
        self.PodMonitors = None
        self.RawJobs = None
        self.AlertDetailRules = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Describe = params.get("Describe")
        if params.get("AlertRules") is not None:
            self.AlertRules = []
            for item in params.get("AlertRules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self.AlertRules.append(obj)
        if params.get("RecordRules") is not None:
            self.RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RecordRules.append(obj)
        if params.get("ServiceMonitors") is not None:
            self.ServiceMonitors = []
            for item in params.get("ServiceMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.ServiceMonitors.append(obj)
        if params.get("PodMonitors") is not None:
            self.PodMonitors = []
            for item in params.get("PodMonitors"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.PodMonitors.append(obj)
        if params.get("RawJobs") is not None:
            self.RawJobs = []
            for item in params.get("RawJobs"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RawJobs.append(obj)
        if params.get("AlertDetailRules") is not None:
            self.AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertRuleDetail()
                obj._deserialize(item)
                self.AlertDetailRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PrometheusTemplateSyncTarget(AbstractModel):
    """云原生Prometheus模板同步目标

    """

    def __init__(self):
        """
        :param Region: 目标所在地域
        :type Region: str
        :param InstanceId: 目标实例
        :type InstanceId: str
        :param ClusterId: 集群id，只有当采集模板的Level为cluster的时候需要
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param SyncTime: 最后一次同步时间， 用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncTime: str
        :param Version: 当前使用的模板版本，用于出参
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param ClusterType: 集群类型，只有当采集模板的Level为cluster的时候需要
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param InstanceName: 用于出参，实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param ClusterName: 用于出参，集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        """
        self.Region = None
        self.InstanceId = None
        self.ClusterId = None
        self.SyncTime = None
        self.Version = None
        self.ClusterType = None
        self.InstanceName = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.InstanceId = params.get("InstanceId")
        self.ClusterId = params.get("ClusterId")
        self.SyncTime = params.get("SyncTime")
        self.Version = params.get("Version")
        self.ClusterType = params.get("ClusterType")
        self.InstanceName = params.get("InstanceName")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegionInstance(AbstractModel):
    """地域属性信息

    """

    def __init__(self):
        """
        :param RegionName: 地域名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionName: str
        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionId: int
        :param Status: 地域状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param FeatureGates: 地域特性开关(按照JSON的形式返回所有属性)
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureGates: str
        :param Alias: 地域简称
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Remark: 地域白名单
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.RegionName = None
        self.RegionId = None
        self.Status = None
        self.FeatureGates = None
        self.Alias = None
        self.Remark = None


    def _deserialize(self, params):
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        self.Status = params.get("Status")
        self.FeatureGates = params.get("FeatureGates")
        self.Alias = params.get("Alias")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RemoveNodeFromNodePoolRequest(AbstractModel):
    """RemoveNodeFromNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param InstanceIds: 节点id列表
        :type InstanceIds: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RemoveNodeFromNodePoolResponse(AbstractModel):
    """RemoveNodeFromNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceDeleteOption(AbstractModel):
    """资源删除选项

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型，例如CBS
        :type ResourceType: str
        :param DeleteMode: 集群删除时资源的删除模式：terminate（销毁），retain （保留）
        :type DeleteMode: str
        """
        self.ResourceType = None
        self.DeleteMode = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.DeleteMode = params.get("DeleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RunInstancesForNode(AbstractModel):
    """不同角色的节点配置参数

    """

    def __init__(self):
        """
        :param NodeRole: 节点角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在创建 INDEPENDENT_CLUSTER 独立集群时需要指定。MASTER_ETCD节点数量为3～7，建议为奇数。MASTER_ETCD节点最小配置为4C8G。
        :type NodeRole: str
        :param RunInstancesPara: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口，传入公共参数外的其他参数即可，其中ImageId会替换为TKE集群OS对应的镜像。
        :type RunInstancesPara: list of str
        :param InstanceAdvancedSettingsOverrides: 节点高级设置，该参数会覆盖集群级别设置的InstanceAdvancedSettings，和上边的RunInstancesPara按照顺序一一对应（当前只对节点自定义参数ExtraArgs生效）。
        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings
        """
        self.NodeRole = None
        self.RunInstancesPara = None
        self.InstanceAdvancedSettingsOverrides = None


    def _deserialize(self, params):
        self.NodeRole = params.get("NodeRole")
        self.RunInstancesPara = params.get("RunInstancesPara")
        if params.get("InstanceAdvancedSettingsOverrides") is not None:
            self.InstanceAdvancedSettingsOverrides = []
            for item in params.get("InstanceAdvancedSettingsOverrides"):
                obj = InstanceAdvancedSettings()
                obj._deserialize(item)
                self.InstanceAdvancedSettingsOverrides.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetNodePoolNodeProtectionRequest(AbstractModel):
    """SetNodePoolNodeProtection请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param InstanceIds: 节点id
        :type InstanceIds: list of str
        :param ProtectedFromScaleIn: 节点是否需要移出保护
        :type ProtectedFromScaleIn: bool
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceIds = None
        self.ProtectedFromScaleIn = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceIds = params.get("InstanceIds")
        self.ProtectedFromScaleIn = params.get("ProtectedFromScaleIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SetNodePoolNodeProtectionResponse(AbstractModel):
    """SetNodePoolNodeProtection返回参数结构体

    """

    def __init__(self):
        """
        :param SucceedInstanceIds: 成功设置的节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type SucceedInstanceIds: list of str
        :param FailedInstanceIds: 没有成功设置的节点id
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedInstanceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SucceedInstanceIds = None
        self.FailedInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucceedInstanceIds = params.get("SucceedInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SyncPrometheusTemplateRequest(AbstractModel):
    """SyncPrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 实例id
        :type TemplateId: str
        :param Targets: 同步目标
        :type Targets: list of PrometheusTemplateSyncTarget
        """
        self.TemplateId = None
        self.Targets = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = PrometheusTemplateSyncTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SyncPrometheusTemplateResponse(AbstractModel):
    """SyncPrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """标签绑定的资源类型，当前支持类型："cluster"

    """

    def __init__(self):
        """
        :param Key: 标签键
        :type Key: str
        :param Value: 标签值
        :type Value: str
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TagSpecification(AbstractModel):
    """标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云主机实例。

    """

    def __init__(self):
        """
        :param ResourceType: 标签绑定的资源类型，当前支持类型："cluster"
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param Tags: 标签对列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Taint(AbstractModel):
    """kubernetes Taint

    """

    def __init__(self):
        """
        :param Key: Key
        :type Key: str
        :param Value: Value
        :type Value: str
        :param Effect: Effect
        :type Effect: str
        """
        self.Key = None
        self.Value = None
        self.Effect = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Effect = params.get("Effect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TaskStepInfo(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        """
        :param Step: 步骤名称
        :type Step: str
        :param LifeState: 生命周期
pending : 步骤未开始
running: 步骤执行中
success: 步骤成功完成
failed: 步骤失败
        :type LifeState: str
        :param StartAt: 步骤开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param EndAt: 步骤结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndAt: str
        :param FailedMsg: 若步骤生命周期为failed,则此字段显示错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedMsg: str
        """
        self.Step = None
        self.LifeState = None
        self.StartAt = None
        self.EndAt = None
        self.FailedMsg = None


    def _deserialize(self, params):
        self.Step = params.get("Step")
        self.LifeState = params.get("LifeState")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        self.FailedMsg = params.get("FailedMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateClusterVersionRequest(AbstractModel):
    """UpdateClusterVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 Id
        :type ClusterId: str
        :param DstVersion: 需要升级到的版本
        :type DstVersion: str
        :param ExtraArgs: 集群自定义参数
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        :param MaxNotReadyPercent: 可容忍的最大不可用pod数目
        :type MaxNotReadyPercent: float
        :param SkipPreCheck: 是否跳过预检查阶段
        :type SkipPreCheck: bool
        """
        self.ClusterId = None
        self.DstVersion = None
        self.ExtraArgs = None
        self.MaxNotReadyPercent = None
        self.SkipPreCheck = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.DstVersion = params.get("DstVersion")
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = ClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        self.MaxNotReadyPercent = params.get("MaxNotReadyPercent")
        self.SkipPreCheck = params.get("SkipPreCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateClusterVersionResponse(AbstractModel):
    """UpdateClusterVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateEKSClusterRequest(AbstractModel):
    """UpdateEKSCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 弹性集群Id
        :type ClusterId: str
        :param ClusterName: 弹性集群名称
        :type ClusterName: str
        :param ClusterDesc: 弹性集群描述信息
        :type ClusterDesc: str
        :param SubnetIds: 子网Id 列表
        :type SubnetIds: list of str
        :param PublicLB: 弹性容器集群公网访问LB信息
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.ClusterPublicLB`
        :param InternalLB: 弹性容器集群内网访问LB信息
        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.ClusterInternalLB`
        :param ServiceSubnetId: Service 子网Id
        :type ServiceSubnetId: str
        :param DnsServers: 集群自定义的dns 服务器信息
        :type DnsServers: list of DnsServerConf
        :param ClearDnsServer: 是否清空自定义dns 服务器设置。为1 表示 是。其他表示 否。
        :type ClearDnsServer: str
        :param NeedDeleteCbs: 将来删除集群时是否要删除cbs。默认为 FALSE
        :type NeedDeleteCbs: bool
        """
        self.ClusterId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.SubnetIds = None
        self.PublicLB = None
        self.InternalLB = None
        self.ServiceSubnetId = None
        self.DnsServers = None
        self.ClearDnsServer = None
        self.NeedDeleteCbs = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.SubnetIds = params.get("SubnetIds")
        if params.get("PublicLB") is not None:
            self.PublicLB = ClusterPublicLB()
            self.PublicLB._deserialize(params.get("PublicLB"))
        if params.get("InternalLB") is not None:
            self.InternalLB = ClusterInternalLB()
            self.InternalLB._deserialize(params.get("InternalLB"))
        self.ServiceSubnetId = params.get("ServiceSubnetId")
        if params.get("DnsServers") is not None:
            self.DnsServers = []
            for item in params.get("DnsServers"):
                obj = DnsServerConf()
                obj._deserialize(item)
                self.DnsServers.append(obj)
        self.ClearDnsServer = params.get("ClearDnsServer")
        self.NeedDeleteCbs = params.get("NeedDeleteCbs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateEKSClusterResponse(AbstractModel):
    """UpdateEKSCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeAbleInstancesItem(AbstractModel):
    """可升级节点信息

    """

    def __init__(self):
        """
        :param InstanceId: 节点Id
        :type InstanceId: str
        :param Version: 节点的当前版本
        :type Version: str
        :param LatestVersion: 当前版本的最新小版本
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestVersion: str
        """
        self.InstanceId = None
        self.Version = None
        self.LatestVersion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Version = params.get("Version")
        self.LatestVersion = params.get("LatestVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeClusterInstancesRequest(AbstractModel):
    """UpgradeClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Operation: create 表示开始一次升级任务
pause 表示停止任务
resume表示继续任务
abort表示终止任务
        :type Operation: str
        :param UpgradeType: 升级类型，只有Operation是create需要设置
reset 大版本重装升级
hot 小版本热升级
major 大版本原地升级
        :type UpgradeType: str
        :param InstanceIds: 需要升级的节点列表
        :type InstanceIds: list of str
        :param ResetParam: 当节点重新加入集群时候所使用的参数，参考添加已有节点接口
        :type ResetParam: :class:`tencentcloud.tke.v20180525.models.UpgradeNodeResetParam`
        :param SkipPreCheck: 是否忽略节点升级前检查
        :type SkipPreCheck: bool
        :param MaxNotReadyPercent: 最大可容忍的不可用Pod比例
        :type MaxNotReadyPercent: float
        """
        self.ClusterId = None
        self.Operation = None
        self.UpgradeType = None
        self.InstanceIds = None
        self.ResetParam = None
        self.SkipPreCheck = None
        self.MaxNotReadyPercent = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Operation = params.get("Operation")
        self.UpgradeType = params.get("UpgradeType")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("ResetParam") is not None:
            self.ResetParam = UpgradeNodeResetParam()
            self.ResetParam._deserialize(params.get("ResetParam"))
        self.SkipPreCheck = params.get("SkipPreCheck")
        self.MaxNotReadyPercent = params.get("MaxNotReadyPercent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeClusterInstancesResponse(AbstractModel):
    """UpgradeClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpgradeNodeResetParam(AbstractModel):
    """节点升级重装参数

    """

    def __init__(self):
        """
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`
        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）
        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）
        :type SecurityGroupIds: list of str
        """
        self.InstanceAdvancedSettings = None
        self.EnhancedService = None
        self.LoginSettings = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        