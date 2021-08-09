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


class AcquireClusterAdminRoleRequest(AbstractModel):
    """AcquireClusterAdminRole请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcquireClusterAdminRoleResponse(AbstractModel):
    """AcquireClusterAdminRole返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddClusterCIDRRequest(AbstractModel):
    """AddClusterCIDR请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterCIDRs: 增加的ClusterCIDR\n        :type ClusterCIDRs: list of str\n        :param IgnoreClusterCIDRConflict: 是否忽略ClusterCIDR与VPC路由表的冲突\n        :type IgnoreClusterCIDRConflict: bool\n        """
        self.ClusterId = None
        self.ClusterCIDRs = None
        self.IgnoreClusterCIDRConflict = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterCIDRs = params.get("ClusterCIDRs")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterCIDRResponse(AbstractModel):
    """AddClusterCIDR返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIds: 实例列表，不支持竞价实例\n        :type InstanceIds: list of str\n        :param InstanceAdvancedSettings: 实例额外需要设置参数信息(默认值)\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。\n        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`\n        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）\n        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`\n        :param HostName: 重装系统时，可以指定修改实例的HostName(集群为HostName模式时，此参数必传，规则名称除不支持大写字符外与[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口HostName一致)\n        :type HostName: str\n        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）\n        :type SecurityGroupIds: list of str\n        :param NodePool: 节点池选项\n        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePoolOption`\n        :param SkipValidateOptions: 校验规则相关选项，可配置跳过某些校验规则。目前支持GlobalRouteCIDRCheck（跳过GlobalRouter的相关校验），VpcCniCIDRCheck（跳过VpcCni相关校验）\n        :type SkipValidateOptions: list of str\n        :param InstanceAdvancedSettingsOverrides: 参数InstanceAdvancedSettingsOverride数组用于定制化地配置各台instance，与InstanceIds顺序对应。当传入InstanceAdvancedSettingsOverrides数组时，将覆盖默认参数InstanceAdvancedSettings；当没有传入参数InstanceAdvancedSettingsOverrides时，InstanceAdvancedSettings参数对每台instance生效。

参数InstanceAdvancedSettingsOverride数组的长度应与InstanceIds数组一致；当长度大于InstanceIds数组长度时将报错；当长度小于InstanceIds数组时，没有对应配置的instace将使用默认配置。\n        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param FailedInstanceIds: 失败的节点ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedInstanceIds: list of str\n        :param SuccInstanceIds: 成功的节点ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccInstanceIds: list of str\n        :param TimeoutInstanceIds: 超时未返回出来节点的ID(可能失败，也可能成功)
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeoutInstanceIds: list of str\n        :param FailedReasons: 失败的节点的失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedReasons: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class AddNodeToNodePoolRequest(AbstractModel):
    """AddNodeToNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        :param InstanceIds: 节点id\n        :type InstanceIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodeToNodePoolResponse(AbstractModel):
    """AddNodeToNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddVpcCniSubnetsRequest(AbstractModel):
    """AddVpcCniSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param SubnetIds: 为集群容器网络增加的子网列表\n        :type SubnetIds: list of str\n        :param VpcId: 集群所属的VPC的ID\n        :type VpcId: str\n        """
        self.ClusterId = None
        self.SubnetIds = None
        self.VpcId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetIds = params.get("SubnetIds")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddVpcCniSubnetsResponse(AbstractModel):
    """AddVpcCniSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AutoScalingGroupRange(AbstractModel):
    """集群关联的伸缩组最大实例数最小值实例数

    """

    def __init__(self):
        """
        :param MinSize: 伸缩组最小实例数\n        :type MinSize: int\n        :param MaxSize: 伸缩组最大实例数\n        :type MaxSize: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoscalingAdded(AbstractModel):
    """自动扩所容的节点

    """

    def __init__(self):
        """
        :param Joining: 正在加入中的节点数量\n        :type Joining: int\n        :param Initializing: 初始化中的节点数量\n        :type Initializing: int\n        :param Normal: 正常的节点数量\n        :type Normal: int\n        :param Total: 节点总数\n        :type Total: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstancesUpgradeAbleRequest(AbstractModel):
    """CheckInstancesUpgradeAble请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIds: 节点列表，空为全部节点\n        :type InstanceIds: list of str\n        :param UpgradeType: 升级类型\n        :type UpgradeType: str\n        :param Offset: 分页Offset\n        :type Offset: int\n        :param Limit: 分页Limit\n        :type Limit: int\n        :param Filter: 过滤\n        :type Filter: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstancesUpgradeAbleResponse(AbstractModel):
    """CheckInstancesUpgradeAble返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterVersion: 集群master当前小版本\n        :type ClusterVersion: str\n        :param LatestVersion: 集群master对应的大版本目前最新小版本\n        :type LatestVersion: str\n        :param UpgradeAbleInstances: 可升级节点列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpgradeAbleInstances: list of UpgradeAbleInstancesItem\n        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class Cluster(AbstractModel):
    """集群信息结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param ClusterDescription: 集群描述\n        :type ClusterDescription: str\n        :param ClusterVersion: 集群版本（默认值为1.10.5）\n        :type ClusterVersion: str\n        :param ClusterOs: 集群系统。centos7.2x86_64 或者 ubuntu16.04.1 LTSx86_64，默认取值为ubuntu16.04.1 LTSx86_64\n        :type ClusterOs: str\n        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。\n        :type ClusterType: str\n        :param ClusterNetworkSettings: 集群网络相关参数\n        :type ClusterNetworkSettings: :class:`tencentcloud.tke.v20180525.models.ClusterNetworkSettings`\n        :param ClusterNodeNum: 集群当前node数量\n        :type ClusterNodeNum: int\n        :param ProjectId: 集群所属的项目ID\n        :type ProjectId: int\n        :param TagSpecification: 标签描述列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSpecification: list of TagSpecification\n        :param ClusterStatus: 集群状态 (Running 运行中  Creating 创建中 Abnormal 异常  )\n        :type ClusterStatus: str\n        :param Property: 集群属性(包括集群不同属性的MAP，属性字段包括NodeNameType (lan-ip模式和hostname 模式，默认无lan-ip模式))
注意：此字段可能返回 null，表示取不到有效值。\n        :type Property: str\n        :param ClusterMaterNodeNum: 集群当前master数量\n        :type ClusterMaterNodeNum: int\n        :param ImageId: 集群使用镜像id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageId: str\n        :param OsCustomizeType: OsCustomizeType 系统定制类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type OsCustomizeType: str\n        :param ContainerRuntime: 集群运行环境docker或container
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContainerRuntime: str\n        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param DeletionProtection: 删除保护开关
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeletionProtection: bool\n        :param EnableExternalNode: 集群是否开启第三方节点支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableExternalNode: bool\n        """
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
        self.EnableExternalNode = None


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
        self.EnableExternalNode = params.get("EnableExternalNode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAdvancedSettings(AbstractModel):
    """集群高级配置

    """

    def __init__(self):
        """
        :param IPVS: 是否启用IPVS\n        :type IPVS: bool\n        :param AsEnabled: 是否启用集群节点自动扩缩容(创建集群流程不支持开启此功能)\n        :type AsEnabled: bool\n        :param ContainerRuntime: 集群使用的runtime类型，包括"docker"和"containerd"两种类型，默认为"docker"\n        :type ContainerRuntime: str\n        :param NodeNameType: 集群中节点NodeName类型（包括 hostname,lan-ip两种形式，默认为lan-ip。如果开启了hostname模式，创建节点时需要设置HostName参数，并且InstanceName需要和HostName一致）\n        :type NodeNameType: str\n        :param ExtraArgs: 集群自定义参数\n        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`\n        :param NetworkType: 集群网络类型（包括GR(全局路由)和VPC-CNI两种模式，默认为GR。\n        :type NetworkType: str\n        :param IsNonStaticIpMode: 集群VPC-CNI模式是否为非固定IP，默认: FALSE 固定IP。\n        :type IsNonStaticIpMode: bool\n        :param DeletionProtection: 是否启用集群删除保护\n        :type DeletionProtection: bool\n        :param KubeProxyMode: 集群的网络代理模型，目前tke集群支持的网络代理模式有三种：iptables,ipvs,ipvs-bpf，此参数仅在使用ipvs-bpf模式时使用，三种网络模式的参数设置关系如下：
iptables模式：IPVS和KubeProxyMode都不设置
ipvs模式: 设置IPVS为true, KubeProxyMode不设置
ipvs-bpf模式: 设置KubeProxyMode为kube-proxy-bpf
使用ipvs-bpf的网络模式需要满足以下条件：
1. 集群版本必须为1.14及以上；
2. 系统镜像必须是: Tencent Linux 2.4；\n        :type KubeProxyMode: str\n        :param AuditEnabled: 是否开启审计开关\n        :type AuditEnabled: bool\n        :param AuditLogsetId: 审计日志上传到的logset日志集\n        :type AuditLogsetId: str\n        :param AuditLogTopicId: 审计日志上传到的topic\n        :type AuditLogTopicId: str\n        :param VpcCniType: 区分单网卡多IP模式和独立网卡模式\n        :type VpcCniType: str\n        :param RuntimeVersion: 运行时版本\n        :type RuntimeVersion: str\n        :param EnableCustomizedPodCIDR: 是否开节点podCIDR大小的自定义模式\n        :type EnableCustomizedPodCIDR: bool\n        :param BasePodNumber: 自定义模式下的基础pod数量\n        :type BasePodNumber: int\n        :param CiliumMode: 启用 CiliumMode 的模式，空值表示不启用，“clusterIP” 表示启用 Cilium 支持 ClusterIP\n        :type CiliumMode: str\n        """
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
        self.CiliumMode = None


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
        self.CiliumMode = params.get("CiliumMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroup(AbstractModel):
    """集群关联的伸缩组信息

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID\n        :type AutoScalingGroupId: str\n        :param Status: 伸缩组状态(开启 enabled 开启中 enabling 关闭 disabled 关闭中 disabling 更新中 updating 删除中 deleting 开启缩容中 scaleDownEnabling 关闭缩容中 scaleDownDisabling)\n        :type Status: str\n        :param IsUnschedulable: 节点是否设置成不可调度
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsUnschedulable: bool\n        :param Labels: 伸缩组的label列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Labels: list of Label\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupAttribute(AbstractModel):
    """集群伸缩组属性

    """

    def __init__(self):
        """
        :param AutoScalingGroupId: 伸缩组ID\n        :type AutoScalingGroupId: str\n        :param AutoScalingGroupEnabled: 是否开启\n        :type AutoScalingGroupEnabled: bool\n        :param AutoScalingGroupRange: 伸缩组最大最小实例数\n        :type AutoScalingGroupRange: :class:`tencentcloud.tke.v20180525.models.AutoScalingGroupRange`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupOption(AbstractModel):
    """集群弹性伸缩配置

    """

    def __init__(self):
        """
        :param IsScaleDownEnabled: 是否开启缩容
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsScaleDownEnabled: bool\n        :param Expander: 多伸缩组情况下扩容选择算法(random 随机选择，most-pods 最多类型的Pod least-waste 最少的资源浪费，默认为random)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Expander: str\n        :param MaxEmptyBulkDelete: 最大并发缩容数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxEmptyBulkDelete: int\n        :param ScaleDownDelay: 集群扩容后多少分钟开始判断缩容（默认为10分钟）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScaleDownDelay: int\n        :param ScaleDownUnneededTime: 节点连续空闲多少分钟后被缩容（默认为 10分钟）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScaleDownUnneededTime: int\n        :param ScaleDownUtilizationThreshold: 节点资源使用量低于多少(百分比)时认为空闲(默认: 50(百分比))
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScaleDownUtilizationThreshold: int\n        :param SkipNodesWithLocalStorage: 含有本地存储Pod的节点是否不缩容(默认： FALSE)
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkipNodesWithLocalStorage: bool\n        :param SkipNodesWithSystemPods: 含有kube-system namespace下非DaemonSet管理的Pod的节点是否不缩容 (默认： FALSE)
注意：此字段可能返回 null，表示取不到有效值。\n        :type SkipNodesWithSystemPods: bool\n        :param IgnoreDaemonSetsUtilization: 计算资源使用量时是否默认忽略DaemonSet的实例(默认值: False，不忽略)
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreDaemonSetsUtilization: bool\n        :param OkTotalUnreadyCount: CA做健康性判断的个数，默认3，即超过OkTotalUnreadyCount个数后，CA会进行健康性判断。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OkTotalUnreadyCount: int\n        :param MaxTotalUnreadyPercentage: 未就绪节点的最大百分比，此后CA会停止操作
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxTotalUnreadyPercentage: int\n        :param ScaleDownUnreadyTime: 表示未准备就绪的节点在有资格进行缩减之前应该停留多长时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScaleDownUnreadyTime: int\n        :param UnregisteredNodeRemovalTime: CA删除未在Kubernetes中注册的节点之前等待的时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnregisteredNodeRemovalTime: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterBasicSettings(AbstractModel):
    """描述集群的基本配置信息

    """

    def __init__(self):
        """
        :param ClusterOs: 集群系统。centos7.2x86_64 或者 ubuntu16.04.1 LTSx86_64，默认取值为ubuntu16.04.1 LTSx86_64\n        :type ClusterOs: str\n        :param ClusterVersion: 集群版本,默认值为1.10.5\n        :type ClusterVersion: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param ClusterDescription: 集群描述\n        :type ClusterDescription: str\n        :param VpcId: 私有网络ID，形如vpc-xxx。创建托管空集群时必传。\n        :type VpcId: str\n        :param ProjectId: 集群内新增资源所属项目ID。\n        :type ProjectId: int\n        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到集群实例。\n        :type TagSpecification: list of TagSpecification\n        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)\n        :type OsCustomizeType: str\n        :param NeedWorkSecurityGroup: 是否开启节点的默认安全组(默认: 否，Aphla特性)\n        :type NeedWorkSecurityGroup: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCIDRSettings(AbstractModel):
    """集群容器网络相关参数

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用于分配集群容器和服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突。且网段范围必须在内网网段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。\n        :type ClusterCIDR: str\n        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 冲突错误, 默认不忽略\n        :type IgnoreClusterCIDRConflict: bool\n        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量。取值范围4～256。不为2的幂值时会向上取最接近的2的幂值。\n        :type MaxNodePodNum: int\n        :param MaxClusterServiceNum: 集群最大的service数量。取值范围32～32768，不为2的幂值时会向上取最接近的2的幂值。\n        :type MaxClusterServiceNum: int\n        :param ServiceCIDR: 用于分配集群服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突。且网段范围必须在内网网段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。\n        :type ServiceCIDR: str\n        :param EniSubnetIds: VPC-CNI网络模式下，弹性网卡的子网Id。\n        :type EniSubnetIds: list of str\n        :param ClaimExpiredSeconds: VPC-CNI网络模式下，弹性网卡IP的回收时间，取值范围[300,15768000)\n        :type ClaimExpiredSeconds: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCredential(AbstractModel):
    """接入k8s 的认证信息

    """

    def __init__(self):
        """
        :param CACert: CA 根证书\n        :type CACert: str\n        :param Token: 认证用的Token\n        :type Token: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExtraArgs(AbstractModel):
    """集群master自定义参数

    """

    def __init__(self):
        """
        :param KubeAPIServer: kube-apiserver自定义参数，参数格式为["k1=v1", "k1=v2"]， 例如["max-requests-inflight=500","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
注意：此字段可能返回 null，表示取不到有效值。\n        :type KubeAPIServer: list of str\n        :param KubeControllerManager: kube-controller-manager自定义参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type KubeControllerManager: list of str\n        :param KubeScheduler: kube-scheduler自定义参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type KubeScheduler: list of str\n        :param Etcd: etcd自定义参数，只支持独立集群
注意：此字段可能返回 null，表示取不到有效值。\n        :type Etcd: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInternalLB(AbstractModel):
    """弹性容器集群内网访问LB信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启内网访问LB\n        :type Enabled: bool\n        :param SubnetId: 内网访问LB关联的子网Id\n        :type SubnetId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterNetworkSettings(AbstractModel):
    """集群网络相关的参数

    """

    def __init__(self):
        """
        :param ClusterCIDR: 用于分配集群容器和服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突\n        :type ClusterCIDR: str\n        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 冲突错误, 默认不忽略\n        :type IgnoreClusterCIDRConflict: bool\n        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量(默认为256)\n        :type MaxNodePodNum: int\n        :param MaxClusterServiceNum: 集群最大的service数量(默认为256)\n        :type MaxClusterServiceNum: int\n        :param Ipvs: 是否启用IPVS(默认不开启)\n        :type Ipvs: bool\n        :param VpcId: 集群的VPCID（如果创建空集群，为必传值，否则自动设置为和集群的节点保持一致）\n        :type VpcId: str\n        :param Cni: 网络插件是否启用CNI(默认开启)\n        :type Cni: bool\n        :param KubeProxyMode: service的网络模式，当前参数只适用于ipvs+bpf模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type KubeProxyMode: str\n        :param ServiceCIDR: 用于分配service的IP range，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceCIDR: str\n        :param Subnets: 集群关联的容器子网
注意：此字段可能返回 null，表示取不到有效值。\n        :type Subnets: list of str\n        """
        self.ClusterCIDR = None
        self.IgnoreClusterCIDRConflict = None
        self.MaxNodePodNum = None
        self.MaxClusterServiceNum = None
        self.Ipvs = None
        self.VpcId = None
        self.Cni = None
        self.KubeProxyMode = None
        self.ServiceCIDR = None
        self.Subnets = None


    def _deserialize(self, params):
        self.ClusterCIDR = params.get("ClusterCIDR")
        self.IgnoreClusterCIDRConflict = params.get("IgnoreClusterCIDRConflict")
        self.MaxNodePodNum = params.get("MaxNodePodNum")
        self.MaxClusterServiceNum = params.get("MaxClusterServiceNum")
        self.Ipvs = params.get("Ipvs")
        self.VpcId = params.get("VpcId")
        self.Cni = params.get("Cni")
        self.KubeProxyMode = params.get("KubeProxyMode")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.Subnets = params.get("Subnets")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterPublicLB(AbstractModel):
    """弹性容器集群公网访问负载均衡信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启公网访问LB\n        :type Enabled: bool\n        :param AllowFromCidrs: 允许访问的来源CIDR列表\n        :type AllowFromCidrs: list of str\n        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)\n        :type SecurityPolicies: list of str\n        :param ExtraParam: 外网访问相关的扩展参数，格式为json\n        :type ExtraParam: str\n        """
        self.Enabled = None
        self.AllowFromCidrs = None
        self.SecurityPolicies = None
        self.ExtraParam = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.AllowFromCidrs = params.get("AllowFromCidrs")
        self.SecurityPolicies = params.get("SecurityPolicies")
        self.ExtraParam = params.get("ExtraParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterVersion(AbstractModel):
    """集群版本信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Versions: 集群主版本号列表，例如1.18.4\n        :type Versions: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonName(AbstractModel):
    """账户UIN与客户端证书CommonName的映射

    """

    def __init__(self):
        """
        :param SubaccountUin: 子账户UIN\n        :type SubaccountUin: str\n        :param CN: 子账户客户端证书中的CommonName字段\n        :type CN: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ControllerStatus(AbstractModel):
    """集群中控制器的状态描述

    """

    def __init__(self):
        """
        :param Name: 控制器的名字\n        :type Name: str\n        :param Enabled: 控制器是否开启\n        :type Enabled: bool\n        """
        self.Name = None
        self.Enabled = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterAsGroupRequest(AbstractModel):
    """CreateClusterAsGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param AutoScalingGroupPara: 伸缩组创建透传参数，json化字符串格式，详见[伸缩组创建实例](https://cloud.tencent.com/document/api/377/20440)接口。LaunchConfigurationId由LaunchConfigurePara参数创建，不支持填写\n        :type AutoScalingGroupPara: str\n        :param LaunchConfigurePara: 启动配置创建透传参数，json化字符串格式，详见[创建启动配置](https://cloud.tencent.com/document/api/377/20447)接口。另外ImageId参数由于集群维度已经有的ImageId信息，这个字段不需要填写。UserData字段设置通过UserScript设置，这个字段不需要填写。\n        :type LaunchConfigurePara: str\n        :param InstanceAdvancedSettings: 节点高级配置信息\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param Labels: 节点Label数组\n        :type Labels: list of Label\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterAsGroupResponse(AbstractModel):
    """CreateClusterAsGroup返回参数结构体

    """

    def __init__(self):
        """
        :param LaunchConfigurationId: 启动配置ID\n        :type LaunchConfigurationId: str\n        :param AutoScalingGroupId: 伸缩组ID\n        :type AutoScalingGroupId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LaunchConfigurationId = None
        self.AutoScalingGroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param SubnetId: 集群端口所在的子网ID  (仅在开启非外网访问时需要填，必须为集群所在VPC内的子网)\n        :type SubnetId: str\n        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）\n        :type IsExtranet: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointResponse(AbstractModel):
    """CreateClusterEndpoint返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointVipRequest(AbstractModel):
    """CreateClusterEndpointVip请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)\n        :type SecurityPolicies: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip返回参数结构体

    """

    def __init__(self):
        """
        :param RequestFlowId: 请求任务的FlowId\n        :type RequestFlowId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestFlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestFlowId = params.get("RequestFlowId")
        self.RequestId = params.get("RequestId")


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段\n        :type ClusterId: str\n        :param RunInstancePara: CVM创建透传参数，json化字符串格式，如需要保证扩展集群节点请求幂等性需要在此参数添加ClientToken字段，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。\n        :type RunInstancePara: str\n        :param InstanceAdvancedSettings: 实例额外需要设置参数信息\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param SkipValidateOptions: 校验规则相关选项，可配置跳过某些校验规则。目前支持GlobalRouteCIDRCheck（跳过GlobalRouter的相关校验），VpcCniCIDRCheck（跳过VpcCni相关校验）\n        :type SkipValidateOptions: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 节点实例ID\n        :type InstanceIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class CreateClusterNodePoolFromExistingAsgRequest(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param AutoscalingGroupId: 伸缩组ID\n        :type AutoscalingGroupId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterNodePoolFromExistingAsgResponse(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg返回参数结构体

    """

    def __init__(self):
        """
        :param NodePoolId: 节点池ID\n        :type NodePoolId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NodePoolId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.RequestId = params.get("RequestId")


class CreateClusterNodePoolRequest(AbstractModel):
    """CreateClusterNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: cluster id\n        :type ClusterId: str\n        :param AutoScalingGroupPara: AutoScalingGroupPara AS组参数\n        :type AutoScalingGroupPara: str\n        :param LaunchConfigurePara: LaunchConfigurePara 运行参数\n        :type LaunchConfigurePara: str\n        :param InstanceAdvancedSettings: InstanceAdvancedSettings 示例参数\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param EnableAutoscale: 是否启用自动伸缩\n        :type EnableAutoscale: bool\n        :param Name: 节点池名称\n        :type Name: str\n        :param Labels: Labels标签\n        :type Labels: list of Label\n        :param Taints: Taints互斥\n        :type Taints: list of Taint\n        :param NodePoolOs: 节点池os\n        :type NodePoolOs: str\n        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)\n        :type OsCustomizeType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterNodePoolResponse(AbstractModel):
    """CreateClusterNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NodePoolId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NodePoolId = params.get("NodePoolId")
        self.RequestId = params.get("RequestId")


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterCIDRSettings: 集群容器网络配置信息\n        :type ClusterCIDRSettings: :class:`tencentcloud.tke.v20180525.models.ClusterCIDRSettings`\n        :param ClusterType: 集群类型，托管集群：MANAGED_CLUSTER，独立集群：INDEPENDENT_CLUSTER。\n        :type ClusterType: str\n        :param RunInstancesForNode: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口。总机型(包括地域)数量不超过10个，相同机型(地域)购买多台机器可以通过设置参数中RunInstances中InstanceCount来实现。\n        :type RunInstancesForNode: list of RunInstancesForNode\n        :param ClusterBasicSettings: 集群的基本配置信息\n        :type ClusterBasicSettings: :class:`tencentcloud.tke.v20180525.models.ClusterBasicSettings`\n        :param ClusterAdvancedSettings: 集群高级配置信息\n        :type ClusterAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.ClusterAdvancedSettings`\n        :param InstanceAdvancedSettings: 节点高级配置信息\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param ExistedInstancesForNode: 已存在实例的配置信息。所有实例必须在同一个VPC中，最大数量不超过100。\n        :type ExistedInstancesForNode: list of ExistedInstancesForNode\n        :param InstanceDataDiskMountSettings: CVM类型和其对应的数据盘挂载配置信息\n        :type InstanceDataDiskMountSettings: list of InstanceDataDiskMountSetting\n        :param ExtensionAddons: 需要安装的扩展组件信息\n        :type ExtensionAddons: list of ExtensionAddon\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        :param DestinationCidrBlock: 目的端CIDR。\n        :type DestinationCidrBlock: str\n        :param GatewayIp: 下一跳地址。\n        :type GatewayIp: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRouteResponse(AbstractModel):
    """CreateClusterRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterRouteTableRequest(AbstractModel):
    """CreateClusterRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称\n        :type RouteTableName: str\n        :param RouteTableCidrBlock: 路由表CIDR\n        :type RouteTableCidrBlock: str\n        :param VpcId: 路由表绑定的VPC\n        :type VpcId: str\n        :param IgnoreClusterCidrConflict: 是否忽略CIDR冲突\n        :type IgnoreClusterCidrConflict: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEKSClusterRequest(AbstractModel):
    """CreateEKSCluster请求参数结构体

    """

    def __init__(self):
        """
        :param K8SVersion: k8s版本号。可为1.14.4, 1.12.8。\n        :type K8SVersion: str\n        :param VpcId: vpc 的Id\n        :type VpcId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param SubnetIds: 子网Id 列表\n        :type SubnetIds: list of str\n        :param ClusterDesc: 集群描述信息\n        :type ClusterDesc: str\n        :param ServiceSubnetId: Serivce 所在子网Id\n        :type ServiceSubnetId: str\n        :param DnsServers: 集群自定义的Dns服务器信息\n        :type DnsServers: list of DnsServerConf\n        :param ExtraParam: 扩展参数。须是map[string]string 的json 格式。\n        :type ExtraParam: str\n        :param EnableVpcCoreDNS: 是否在用户集群内开启Dns。默认为true\n        :type EnableVpcCoreDNS: bool\n        :param TagSpecification: 标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到集群实例。\n        :type TagSpecification: list of TagSpecification\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEKSClusterResponse(AbstractModel):
    """CreateEKSCluster返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 弹性集群Id\n        :type ClusterId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class CreatePrometheusAlertRuleRequest(AbstractModel):
    """CreatePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param AlertRule: 告警配置\n        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`\n        """
        self.InstanceId = None
        self.AlertRule = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self.AlertRule = PrometheusAlertRuleDetail()
            self.AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertRuleResponse(AbstractModel):
    """CreatePrometheusAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param Id: 告警id\n        :type Id: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreatePrometheusDashboardRequest(AbstractModel):
    """CreatePrometheusDashboard请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param DashboardName: 面板组名称\n        :type DashboardName: str\n        :param Contents: 面板列表
每一项是一个grafana dashboard的json定义\n        :type Contents: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusDashboardResponse(AbstractModel):
    """CreatePrometheusDashboard返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePrometheusTemplateRequest(AbstractModel):
    """CreatePrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param Template: 模板设置\n        :type Template: :class:`tencentcloud.tke.v20180525.models.PrometheusTemplate`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusTemplateResponse(AbstractModel):
    """CreatePrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id\n        :type TemplateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了k8s节点数据盘相关配置与信息。

    """

    def __init__(self):
        """
        :param DiskType: 云盘类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskType: str\n        :param FileSystem: 文件系统(ext3/ext4/xfs)
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileSystem: str\n        :param DiskSize: 云盘大小(G）
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskSize: int\n        :param AutoFormatAndMount: 是否自动化格式盘并挂载
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoFormatAndMount: bool\n        :param MountTarget: 挂载目录
注意：此字段可能返回 null，表示取不到有效值。\n        :type MountTarget: str\n        :param DiskPartition: 挂载设备名或分区名
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiskPartition: str\n        """
        self.DiskType = None
        self.FileSystem = None
        self.DiskSize = None
        self.AutoFormatAndMount = None
        self.MountTarget = None
        self.DiskPartition = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.FileSystem = params.get("FileSystem")
        self.DiskSize = params.get("DiskSize")
        self.AutoFormatAndMount = params.get("AutoFormatAndMount")
        self.MountTarget = params.get("MountTarget")
        self.DiskPartition = params.get("DiskPartition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterAsGroupsRequest(AbstractModel):
    """DeleteClusterAsGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID，通过[DescribeClusters](https://cloud.tencent.com/document/api/457/31862)接口获取。\n        :type ClusterId: str\n        :param AutoScalingGroupIds: 集群伸缩组ID的列表\n        :type AutoScalingGroupIds: list of str\n        :param KeepInstance: 是否保留伸缩组中的节点(默认值： false(不保留))\n        :type KeepInstance: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointRequest(AbstractModel):
    """DeleteClusterEndpoint请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）\n        :type IsExtranet: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointVipRequest(AbstractModel):
    """DeleteClusterEndpointVip请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterInstancesRequest(AbstractModel):
    """DeleteClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceIds: 主机InstanceId列表\n        :type InstanceIds: list of str\n        :param InstanceDeleteMode: 集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）\n        :type InstanceDeleteMode: str\n        :param ForceDelete: 是否强制删除(当节点在初始化时，可以指定参数为TRUE)\n        :type ForceDelete: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param SuccInstanceIds: 删除成功的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccInstanceIds: list of str\n        :param FailedInstanceIds: 删除失败的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedInstanceIds: list of str\n        :param NotFoundInstanceIds: 未匹配到的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotFoundInstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccInstanceIds = None
        self.FailedInstanceIds = None
        self.NotFoundInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccInstanceIds = params.get("SuccInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.NotFoundInstanceIds = params.get("NotFoundInstanceIds")
        self.RequestId = params.get("RequestId")


class DeleteClusterNodePoolRequest(AbstractModel):
    """DeleteClusterNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 节点池对应的 ClusterId\n        :type ClusterId: str\n        :param NodePoolIds: 需要删除的节点池 Id 列表\n        :type NodePoolIds: list of str\n        :param KeepInstance: 删除节点池时是否保留节点池内节点(节点仍然会被移出集群，但对应的实例不会被销毁)\n        :type KeepInstance: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterNodePoolResponse(AbstractModel):
    """DeleteClusterNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param InstanceDeleteMode: 集群实例删除时的策略：terminate（销毁实例，仅支持按量计费云主机实例） retain （仅移除，保留实例）\n        :type InstanceDeleteMode: str\n        :param ResourceDeleteOptions: 集群删除时资源的删除策略，目前支持CBS（默认保留CBS）\n        :type ResourceDeleteOptions: list of ResourceDeleteOption\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteRequest(AbstractModel):
    """DeleteClusterRoute请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        :param GatewayIp: 下一跳地址。\n        :type GatewayIp: str\n        :param DestinationCidrBlock: 目的端CIDR。\n        :type DestinationCidrBlock: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterRouteTableRequest(AbstractModel):
    """DeleteClusterRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称\n        :type RouteTableName: str\n        """
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEKSClusterRequest(AbstractModel):
    """DeleteEKSCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 弹性集群Id\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEKSClusterResponse(AbstractModel):
    """DeleteEKSCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusAlertRuleRequest(AbstractModel):
    """DeletePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param AlertIds: 告警规则id列表\n        :type AlertIds: list of str\n        """
        self.InstanceId = None
        self.AlertIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AlertIds = params.get("AlertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertRuleResponse(AbstractModel):
    """DeletePrometheusAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTemplateRequest(AbstractModel):
    """DeletePrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板id\n        :type TemplateId: str\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTemplateResponse(AbstractModel):
    """DeletePrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTemplateSyncRequest(AbstractModel):
    """DeletePrometheusTemplateSync请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板id\n        :type TemplateId: str\n        :param Targets: 取消同步的对象列表\n        :type Targets: list of PrometheusTemplateSyncTarget\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTemplateSyncResponse(AbstractModel):
    """DeletePrometheusTemplateSync返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAvailableClusterVersionRequest(AbstractModel):
    """DescribeAvailableClusterVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 Id\n        :type ClusterId: str\n        :param ClusterIds: 集群 Id 列表\n        :type ClusterIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableClusterVersionResponse(AbstractModel):
    """DescribeAvailableClusterVersion返回参数结构体

    """

    def __init__(self):
        """
        :param Versions: 可升级的集群版本号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Versions: list of str\n        :param Clusters: 集群信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Clusters: list of ClusterVersion\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption返回参数结构体

    """

    def __init__(self):
        """
        :param ClusterAsGroupOption: 集群弹性伸缩属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ClusterAsGroupOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterAsGroupOption") is not None:
            self.ClusterAsGroupOption = ClusterAsGroupOption()
            self.ClusterAsGroupOption._deserialize(params.get("ClusterAsGroupOption"))
        self.RequestId = params.get("RequestId")


class DescribeClusterAsGroupsRequest(AbstractModel):
    """DescribeClusterAsGroups请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param AutoScalingGroupIds: 伸缩组ID列表，如果为空，表示拉取集群关联的所有伸缩组。\n        :type AutoScalingGroupIds: list of str\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群关联的伸缩组总数\n        :type TotalCount: int\n        :param ClusterAsGroupSet: 集群关联的伸缩组列表\n        :type ClusterAsGroupSet: list of ClusterAsGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClusterCommonNamesRequest(AbstractModel):
    """DescribeClusterCommonNames请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param SubaccountUins: 子账户列表，不可超出最大值50\n        :type SubaccountUins: list of str\n        :param RoleIds: 角色ID列表，不可超出最大值50\n        :type RoleIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterCommonNamesResponse(AbstractModel):
    """DescribeClusterCommonNames返回参数结构体

    """

    def __init__(self):
        """
        :param CommonNames: 子账户Uin与其客户端证书的CN字段映射\n        :type CommonNames: list of CommonName\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClusterControllersRequest(AbstractModel):
    """DescribeClusterControllers请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterControllersResponse(AbstractModel):
    """DescribeClusterControllers返回参数结构体

    """

    def __init__(self):
        """
        :param ControllerStatusSet: 描述集群中各个控制器的状态\n        :type ControllerStatusSet: list of ControllerStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ControllerStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ControllerStatusSet") is not None:
            self.ControllerStatusSet = []
            for item in params.get("ControllerStatusSet"):
                obj = ControllerStatus()
                obj._deserialize(item)
                self.ControllerStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointStatusRequest(AbstractModel):
    """DescribeClusterEndpointStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）\n        :type IsExtranet: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 查询集群访问端口状态（Created 开启成功，Creating 开启中，NotFound 未开启）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param ErrorMsg: 开启访问入口失败信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 端口操作状态 (Creating 创建中  CreateFailed 创建失败 Created 创建完成 Deleting 删除中 DeletedFailed 删除失败 Deleted 已删除 NotFound 未发现操作 )\n        :type Status: str\n        :param ErrorMsg: 操作失败的原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.ErrorMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        :param InstanceIds: 需要获取的节点实例Id列表。如果为空，表示拉取集群下所有节点实例。\n        :type InstanceIds: list of str\n        :param InstanceRole: 节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER。默认为WORKER类型。\n        :type InstanceRole: str\n        :param Filters: 过滤条件列表；Name的可选值为nodepool-id、nodepool-instance-type；Name为nodepool-id表示根据节点池id过滤机器，Value的值为具体的节点池id，Name为nodepool-instance-type表示节点加入节点池的方式，Value的值为MANUALLY_ADDED（手动加入节点池）、AUTOSCALING_ADDED（伸缩组扩容方式加入节点池）、ALL（手动加入节点池 和 伸缩组扩容方式加入节点池）\n        :type Filters: list of Filter\n        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None
        self.InstanceIds = None
        self.InstanceRole = None
        self.Filters = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceIds = params.get("InstanceIds")
        self.InstanceRole = params.get("InstanceRole")
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
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群中实例总数\n        :type TotalCount: int\n        :param InstanceSet: 集群中实例列表\n        :type InstanceSet: list of Instance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClusterKubeconfigRequest(AbstractModel):
    """DescribeClusterKubeconfig请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterKubeconfigResponse(AbstractModel):
    """DescribeClusterKubeconfig返回参数结构体

    """

    def __init__(self):
        """
        :param Kubeconfig: 子账户kubeconfig文件，可用于直接访问集群kube-apiserver\n        :type Kubeconfig: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Kubeconfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Kubeconfig = params.get("Kubeconfig")
        self.RequestId = params.get("RequestId")


class DescribeClusterNodePoolDetailRequest(AbstractModel):
    """DescribeClusterNodePoolDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodePoolDetailResponse(AbstractModel):
    """DescribeClusterNodePoolDetail返回参数结构体

    """

    def __init__(self):
        """
        :param NodePool: 节点池详情\n        :type NodePool: :class:`tencentcloud.tke.v20180525.models.NodePool`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NodePool = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodePool") is not None:
            self.NodePool = NodePool()
            self.NodePool._deserialize(params.get("NodePool"))
        self.RequestId = params.get("RequestId")


class DescribeClusterNodePoolsRequest(AbstractModel):
    """DescribeClusterNodePools请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: ClusterId（集群id）\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodePoolsResponse(AbstractModel):
    """DescribeClusterNodePools返回参数结构体

    """

    def __init__(self):
        """
        :param NodePoolSet: NodePools（节点池列表）
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodePoolSet: list of NodePool\n        :param TotalCount: 资源总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClusterRouteTablesRequest(AbstractModel):
    """DescribeClusterRouteTables请求参数结构体

    """


class DescribeClusterRouteTablesResponse(AbstractModel):
    """DescribeClusterRouteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RouteTableSet: 集群路由表对象。\n        :type RouteTableSet: list of RouteTableInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        :param Filters: 过滤条件,当前只支持按照单个条件GatewayIP进行过滤（可选）\n        :type Filters: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RouteSet: 集群路由对象。\n        :type RouteSet: list of RouteInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ClusterId: 集群 ID，请填写 查询集群列表 接口中返回的 clusterId 字段\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity返回参数结构体

    """

    def __init__(self):
        """
        :param UserName: 集群的账号名称\n        :type UserName: str\n        :param Password: 集群的访问密码\n        :type Password: str\n        :param CertificationAuthority: 集群访问CA证书\n        :type CertificationAuthority: str\n        :param ClusterExternalEndpoint: 集群访问的地址\n        :type ClusterExternalEndpoint: str\n        :param Domain: 集群访问的域名\n        :type Domain: str\n        :param PgwEndpoint: 集群Endpoint地址\n        :type PgwEndpoint: str\n        :param SecurityPolicy: 集群访问策略组
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityPolicy: list of str\n        :param Kubeconfig: 集群Kubeconfig文件
注意：此字段可能返回 null，表示取不到有效值。\n        :type Kubeconfig: str\n        :param JnsGwEndpoint: 集群JnsGw的访问地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type JnsGwEndpoint: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 集群ID列表(为空时，
表示获取账号下所有集群)\n        :type ClusterIds: list of str\n        :param Offset: 偏移量,默认0\n        :type Offset: int\n        :param Limit: 最大输出条数，默认20，最大为100\n        :type Limit: int\n        :param Filters: 过滤条件,当前只支持按照单个条件ClusterName进行过滤\n        :type Filters: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群总个数\n        :type TotalCount: int\n        :param Clusters: 集群信息列表\n        :type Clusters: list of Cluster\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeEKSClusterCredentialRequest(AbstractModel):
    """DescribeEKSClusterCredential请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEKSClusterCredentialResponse(AbstractModel):
    """DescribeEKSClusterCredential返回参数结构体

    """

    def __init__(self):
        """
        :param Addresses: 集群的接入地址信息\n        :type Addresses: list of IPAddress\n        :param Credential: 集群的认证信息\n        :type Credential: :class:`tencentcloud.tke.v20180525.models.ClusterCredential`\n        :param PublicLB: 集群的公网访问信息\n        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.ClusterPublicLB`\n        :param InternalLB: 集群的内网访问信息\n        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.ClusterInternalLB`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeEKSClustersRequest(AbstractModel):
    """DescribeEKSClusters请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterIds: 集群ID列表(为空时，
表示获取账号下所有集群)\n        :type ClusterIds: list of str\n        :param Offset: 偏移量,默认0\n        :type Offset: int\n        :param Limit: 最大输出条数，默认20\n        :type Limit: int\n        :param Filters: 过滤条件,当前只支持按照单个条件ClusterName进行过滤\n        :type Filters: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEKSClustersResponse(AbstractModel):
    """DescribeEKSClusters返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 集群总个数\n        :type TotalCount: int\n        :param Clusters: 集群信息列表\n        :type Clusters: list of EksCluster\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeEnableVpcCniProgressRequest(AbstractModel):
    """DescribeEnableVpcCniProgress请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 开启vpc-cni的集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnableVpcCniProgressResponse(AbstractModel):
    """DescribeEnableVpcCniProgress返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务进度的描述：Running/Succeed/Failed\n        :type Status: str\n        :param ErrorMessage: 当任务进度为Failed时，对任务状态的进一步描述，例如IPAMD组件安装失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorMessage: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.ErrorMessage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ErrorMessage = params.get("ErrorMessage")
        self.RequestId = params.get("RequestId")


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 ID，请填写查询集群列表 接口中返回的 ClusterId 字段（仅通过ClusterId获取需要过滤条件中的VPCID。节点状态比较时会使用该地域下所有集群中的节点进行比较。参数不支持同时指定InstanceIds和ClusterId。\n        :type ClusterId: str\n        :param InstanceIds: 按照一个或者多个实例ID查询。实例ID形如：ins-xxxxxxxx。（此参数的具体格式可参考API简介的id.N一节）。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。\n        :type InstanceIds: list of str\n        :param Filters: 过滤条件,字段和详见[CVM查询实例](https://cloud.tencent.com/document/api/213/15728)如果设置了ClusterId，会附加集群的VPCID作为查询字段，在此情况下如果在Filter中指定了"vpc-id"作为过滤字段，指定的VPCID必须与集群的VPCID相同。\n        :type Filters: list of Filter\n        :param VagueIpAddress: 实例IP进行过滤(同时支持内网IP和外网IP)\n        :type VagueIpAddress: str\n        :param VagueInstanceName: 实例名称进行过滤\n        :type VagueInstanceName: str\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。\n        :type Limit: int\n        :param IpAddresses: 根据多个实例IP进行过滤\n        :type IpAddresses: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param ExistedInstanceSet: 已经存在的实例信息数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExistedInstanceSet: list of ExistedInstance\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 镜像数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ImageInstanceSet: 镜像信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageInstanceSet: list of ImageInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusAgentInstancesRequest(AbstractModel):
    """DescribePrometheusAgentInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id
可以是tke, eks, edge的集群id\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentInstancesResponse(AbstractModel):
    """DescribePrometheusAgentInstances返回参数结构体

    """

    def __init__(self):
        """
        :param Instances: 关联该集群的实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Instances: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Instances = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Instances = params.get("Instances")
        self.RequestId = params.get("RequestId")


class DescribePrometheusAgentsRequest(AbstractModel):
    """DescribePrometheusAgents请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param Offset: 用于分页\n        :type Offset: int\n        :param Limit: 用于分页\n        :type Limit: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentsResponse(AbstractModel):
    """DescribePrometheusAgents返回参数结构体

    """

    def __init__(self):
        """
        :param Agents: 被关联集群信息\n        :type Agents: list of PrometheusAgentOverview\n        :param Total: 被关联集群总量\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusAlertHistoryRequest(AbstractModel):
    """DescribePrometheusAlertHistory请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param RuleName: 告警名称\n        :type RuleName: str\n        :param StartTime: 开始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Labels: label集合\n        :type Labels: str\n        :param Offset: 分片\n        :type Offset: int\n        :param Limit: 分片\n        :type Limit: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertHistoryResponse(AbstractModel):
    """DescribePrometheusAlertHistory返回参数结构体

    """

    def __init__(self):
        """
        :param Items: 告警历史\n        :type Items: list of PrometheusAlertHistoryItem\n        :param Total: 总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusAlertRuleRequest(AbstractModel):
    """DescribePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param Offset: 分页\n        :type Offset: int\n        :param Limit: 分页\n        :type Limit: int\n        :param Filters: 过滤
支持ID，Name\n        :type Filters: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertRuleResponse(AbstractModel):
    """DescribePrometheusAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param AlertRules: 告警详情\n        :type AlertRules: list of PrometheusAlertRuleDetail\n        :param Total: 总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusInstanceRequest(AbstractModel):
    """DescribePrometheusInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstanceResponse(AbstractModel):
    """DescribePrometheusInstance返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param Name: 实例名称\n        :type Name: str\n        :param VpcId: 私有网络id\n        :type VpcId: str\n        :param SubnetId: 子网id\n        :type SubnetId: str\n        :param COSBucket: cos桶名称\n        :type COSBucket: str\n        :param QueryAddress: 数据查询地址\n        :type QueryAddress: str\n        :param Grafana: 实例中grafana相关的信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Grafana: :class:`tencentcloud.tke.v20180525.models.PrometheusGrafanaInfo`\n        :param AlertManagerUrl: 用户自定义alertmanager
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlertManagerUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceId = None
        self.Name = None
        self.VpcId = None
        self.SubnetId = None
        self.COSBucket = None
        self.QueryAddress = None
        self.Grafana = None
        self.AlertManagerUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.COSBucket = params.get("COSBucket")
        self.QueryAddress = params.get("QueryAddress")
        if params.get("Grafana") is not None:
            self.Grafana = PrometheusGrafanaInfo()
            self.Grafana._deserialize(params.get("Grafana"))
        self.AlertManagerUrl = params.get("AlertManagerUrl")
        self.RequestId = params.get("RequestId")


class DescribePrometheusOverviewsRequest(AbstractModel):
    """DescribePrometheusOverviews请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 用于分页\n        :type Offset: int\n        :param Limit: 用于分页\n        :type Limit: int\n        :param Filters: 过滤实例，目前支持：
ID: 通过实例ID来过滤 
Name: 通过实例名称来过滤\n        :type Filters: list of Filter\n        """
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
        


class DescribePrometheusOverviewsResponse(AbstractModel):
    """DescribePrometheusOverviews返回参数结构体

    """

    def __init__(self):
        """
        :param Instances: 实例列表\n        :type Instances: list of PrometheusInstanceOverview\n        :param Total: 实例总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusTargetsRequest(AbstractModel):
    """DescribePrometheusTargets请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param ClusterType: 集群类型\n        :type ClusterType: str\n        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param Filters: 过滤条件，当前支持
Name=state
Value=up, down, unknown\n        :type Filters: list of Filter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTargetsResponse(AbstractModel):
    """DescribePrometheusTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Jobs: 所有Job的targets信息\n        :type Jobs: list of PrometheusJobTargets\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusTemplateSyncRequest(AbstractModel):
    """DescribePrometheusTemplateSync请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID\n        :type TemplateId: str\n        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTemplateSyncResponse(AbstractModel):
    """DescribePrometheusTemplateSync返回参数结构体

    """

    def __init__(self):
        """
        :param Targets: 同步目标详情\n        :type Targets: list of PrometheusTemplateSyncTarget\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePrometheusTemplatesRequest(AbstractModel):
    """DescribePrometheusTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 模糊过滤条件，支持
Level 按模板级别过滤
Name 按名称过滤
Describe 按描述过滤
ID 按templateId过滤\n        :type Filters: list of Filter\n        :param Offset: 分页偏移\n        :type Offset: int\n        :param Limit: 总数限制\n        :type Limit: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTemplatesResponse(AbstractModel):
    """DescribePrometheusTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param Templates: 模板列表\n        :type Templates: list of PrometheusTemplate\n        :param Total: 总数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 地域的数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RegionInstanceSet: 地域列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionInstanceSet: list of RegionInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableCidrBlock: 路由表CIDR\n        :type RouteTableCidrBlock: str\n        :param VpcId: 路由表绑定的VPC\n        :type VpcId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts返回参数结构体

    """

    def __init__(self):
        """
        :param HasConflict: 路由表是否冲突。\n        :type HasConflict: bool\n        :param RouteTableConflictSet: 路由表冲突列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableConflictSet: list of RouteTableConflict\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeVersionsRequest(AbstractModel):
    """DescribeVersions请求参数结构体

    """


class DescribeVersionsResponse(AbstractModel):
    """DescribeVersions返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 版本数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param VersionInstanceSet: 版本列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionInstanceSet: list of VersionInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.VersionInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionInstanceSet") is not None:
            self.VersionInstanceSet = []
            for item in params.get("VersionInstanceSet"):
                obj = VersionInstance()
                obj._deserialize(item)
                self.VersionInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcCniPodLimitsRequest(AbstractModel):
    """DescribeVpcCniPodLimits请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 查询的机型所在可用区，如：ap-guangzhou-3，默认为空，即不按可用区过滤信息\n        :type Zone: str\n        :param InstanceFamily: 查询的实例机型系列信息，如：S5，默认为空，即不按机型系列过滤信息\n        :type InstanceFamily: str\n        :param InstanceType: 查询的实例机型信息，如：S5.LARGE8，默认为空，即不按机型过滤信息\n        :type InstanceType: str\n        """
        self.Zone = None
        self.InstanceFamily = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcCniPodLimitsResponse(AbstractModel):
    """DescribeVpcCniPodLimits返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 机型数据数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param PodLimitsInstanceSet: 机型信息及其可支持的最大VPC-CNI模式Pod数量信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodLimitsInstanceSet: list of PodLimitsInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.PodLimitsInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PodLimitsInstanceSet") is not None:
            self.PodLimitsInstanceSet = []
            for item in params.get("PodLimitsInstanceSet"):
                obj = PodLimitsInstance()
                obj._deserialize(item)
                self.PodLimitsInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisableVpcCniNetworkTypeRequest(AbstractModel):
    """DisableVpcCniNetworkType请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableVpcCniNetworkTypeResponse(AbstractModel):
    """DisableVpcCniNetworkType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DnsServerConf(AbstractModel):
    """Eks 自定义域名服务器 配置

    """

    def __init__(self):
        """
        :param Domain: 域名。空字符串表示所有域名。\n        :type Domain: str\n        :param DnsServers: dns 服务器地址列表。地址格式 ip:port\n        :type DnsServers: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EksCluster(AbstractModel):
    """弹性集群信息

    """

    def __init__(self):
        """
        :param ClusterId: 集群Id\n        :type ClusterId: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param VpcId: Vpc Id\n        :type VpcId: str\n        :param SubnetIds: 子网列表\n        :type SubnetIds: list of str\n        :param K8SVersion: k8s 版本号\n        :type K8SVersion: str\n        :param Status: 集群状态(running运行中，initializing 初始化中，failed异常)\n        :type Status: str\n        :param ClusterDesc: 集群描述信息\n        :type ClusterDesc: str\n        :param CreatedTime: 集群创建时间\n        :type CreatedTime: str\n        :param ServiceSubnetId: Service 子网Id\n        :type ServiceSubnetId: str\n        :param DnsServers: 集群的自定义dns 服务器信息\n        :type DnsServers: list of DnsServerConf\n        :param NeedDeleteCbs: 将来删除集群时是否要删除cbs。默认为 FALSE\n        :type NeedDeleteCbs: bool\n        :param EnableVpcCoreDNS: 是否在用户集群内开启Dns。默认为TRUE\n        :type EnableVpcCoreDNS: bool\n        :param TagSpecification: 标签描述列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSpecification: list of TagSpecification\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcCniNetworkTypeRequest(AbstractModel):
    """EnableVpcCniNetworkType请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param VpcCniType: 开启vpc-cni的模式，tke-route-eni开启的是策略路由模式，tke-direct-eni开启的是独立网卡模式\n        :type VpcCniType: str\n        :param EnableStaticIp: 是否开启固定IP模式\n        :type EnableStaticIp: bool\n        :param Subnets: 使用的容器子网\n        :type Subnets: list of str\n        :param ExpiredSeconds: 在固定IP模式下，Pod销毁后退还IP的时间，传参必须大于300；不传默认IP永不销毁。\n        :type ExpiredSeconds: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcCniNetworkTypeResponse(AbstractModel):
    """EnableVpcCniNetworkType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        """
        :param SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。\n        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.RunSecurityServiceEnabled`\n        :param MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。\n        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.RunMonitorServiceEnabled`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstance(AbstractModel):
    """已经存在的实例信息

    """

    def __init__(self):
        """
        :param Usable: 实例是否支持加入集群(TRUE 可以加入 FALSE 不能加入)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Usable: bool\n        :param UnusableReason: 实例不支持加入的原因。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnusableReason: str\n        :param AlreadyInCluster: 实例已经所在的集群ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlreadyInCluster: str\n        :param InstanceId: 实例ID形如：ins-xxxxxxxx。\n        :type InstanceId: str\n        :param InstanceName: 实例名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param PrivateIpAddresses: 实例主网卡的内网IP列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIpAddresses: list of str\n        :param PublicIpAddresses: 实例主网卡的公网IP列表。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicIpAddresses: list of str\n        :param CreatedTime: 创建时间。按照ISO8601标准表示，并且使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param CPU: 实例的CPU核数，单位：核。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CPU: int\n        :param Memory: 实例内存容量，单位：GB。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Memory: int\n        :param OsName: 操作系统名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OsName: str\n        :param InstanceType: 实例机型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param AutoscalingGroupId: 伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoscalingGroupId: str\n        :param InstanceChargeType: 实例计费模式。取值范围： PREPAID：表示预付费，即包年包月 POSTPAID_BY_HOUR：表示后付费，即按量计费 CDHPAID：CDH付费，即只对CDH计费，不对CDH上的实例计费。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceChargeType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesForNode(AbstractModel):
    """不同角色的已存在节点配置参数

    """

    def __init__(self):
        """
        :param NodeRole: 节点角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在创建 INDEPENDENT_CLUSTER 独立集群时需要指定。MASTER_ETCD节点数量为3～7，建议为奇数。MASTER_ETCD最小配置为4C8G。\n        :type NodeRole: str\n        :param ExistedInstancesPara: 已存在实例的重装参数\n        :type ExistedInstancesPara: :class:`tencentcloud.tke.v20180525.models.ExistedInstancesPara`\n        :param InstanceAdvancedSettingsOverride: 节点高级设置，会覆盖集群级别设置的InstanceAdvancedSettings（当前只对节点自定义参数ExtraArgs生效）\n        :type InstanceAdvancedSettingsOverride: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param DesiredPodNumbers: 自定义模式集群，可指定每个节点的pod数量\n        :type DesiredPodNumbers: list of int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesPara(AbstractModel):
    """已存在实例的重装参数

    """

    def __init__(self):
        """
        :param InstanceIds: 集群ID\n        :type InstanceIds: list of str\n        :param InstanceAdvancedSettings: 实例额外需要设置参数信息\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。\n        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`\n        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）\n        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`\n        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。\n        :type SecurityGroupIds: list of str\n        :param HostName: 重装系统时，可以指定修改实例的HostName(集群为HostName模式时，此参数必传，规则名称除不支持大写字符外与[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口HostName一致)\n        :type HostName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionAddon(AbstractModel):
    """创建集群时，选择安装的扩展组件的信息

    """

    def __init__(self):
        """
        :param AddonName: 扩展组件名称\n        :type AddonName: str\n        :param AddonParam: 扩展组件信息(扩展组件资源对象的json字符串描述)\n        :type AddonParam: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        


class GetUpgradeInstanceProgressRequest(AbstractModel):
    """GetUpgradeInstanceProgress请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Limit: 最多获取多少个节点的进度\n        :type Limit: int\n        :param Offset: 从第几个节点开始获取进度\n        :type Offset: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUpgradeInstanceProgressResponse(AbstractModel):
    """GetUpgradeInstanceProgress返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 升级节点总数\n        :type Total: int\n        :param Done: 已升级节点总数\n        :type Done: int\n        :param LifeState: 升级任务生命周期
process 运行中
paused 已停止
pauing 正在停止
done  已完成
timeout 已超时
aborted 已取消\n        :type LifeState: str\n        :param Instances: 各节点升级进度详情\n        :type Instances: list of InstanceUpgradeProgressItem\n        :param ClusterStatus: 集群当前状态\n        :type ClusterStatus: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradeClusterStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class IPAddress(AbstractModel):
    """IP 地址

    """

    def __init__(self):
        """
        :param Type: Ip 地址的类型。可为 advertise, public 等\n        :type Type: str\n        :param Ip: Ip 地址\n        :type Ip: str\n        :param Port: 网络端口\n        :type Port: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInstance(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        """
        :param Alias: 镜像别名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        :param OsName: 操作系统名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type OsName: str\n        :param ImageId: 镜像ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageId: str\n        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
注意：此字段可能返回 null，表示取不到有效值。\n        :type OsCustomizeType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """集群的实例信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID\n        :type InstanceId: str\n        :param InstanceRole: 节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER\n        :type InstanceRole: str\n        :param FailedReason: 实例异常(或者处于初始化中)的原因\n        :type FailedReason: str\n        :param InstanceState: 实例的状态（running 运行中，initializing 初始化中，failed 异常）\n        :type InstanceState: str\n        :param DrainStatus: 实例是否封锁状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type DrainStatus: str\n        :param InstanceAdvancedSettings: 节点配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param CreatedTime: 添加时间\n        :type CreatedTime: str\n        :param LanIP: 节点内网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type LanIP: str\n        :param NodePoolId: 资源池ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodePoolId: str\n        :param AutoscalingGroupId: 自动伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoscalingGroupId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相关配置与信息。

    """

    def __init__(self):
        """
        :param MountTarget: 数据盘挂载点, 默认不挂载数据盘. 已格式化的 ext3，ext4，xfs 文件系统的数据盘将直接挂载，其他文件系统或未格式化的数据盘将自动格式化为ext4 (tlinux系统格式化成xfs)并挂载，请注意备份数据! 无数据盘或有多块数据盘的云主机此设置不生效。
注意，注意，多盘场景请使用下方的DataDisks数据结构，设置对应的云盘类型、云盘大小、挂载路径、是否格式化等信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MountTarget: str\n        :param DockerGraphPath: dockerd --graph 指定值, 默认为 /var/lib/docker
注意：此字段可能返回 null，表示取不到有效值。\n        :type DockerGraphPath: str\n        :param UserScript: base64 编码的用户脚本, 此脚本会在 k8s 组件运行后执行, 需要用户保证脚本的可重入及重试逻辑, 脚本及其生成的日志文件可在节点的 /data/ccs_userscript/ 路径查看, 如果要求节点需要在进行初始化完成后才可加入调度, 可配合 unschedulable 参数使用, 在 userScript 最后初始化完成后, 添加 kubectl uncordon nodename --kubeconfig=/root/.kube/config 命令使节点加入调度
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserScript: str\n        :param Unschedulable: 设置加入的节点是否参与调度，默认值为0，表示参与调度；非0表示不参与调度, 待节点初始化完成之后, 可执行kubectl uncordon nodename使node加入调度.\n        :type Unschedulable: int\n        :param Labels: 节点Label数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Labels: list of Label\n        :param DataDisks: 多盘数据盘挂载信息：新建节点时请确保购买CVM的参数传递了购买多个数据盘的信息，如CreateClusterInstances API的RunInstancesPara下的DataDisks也需要设置购买多个数据盘, 具体可以参考CreateClusterInstances接口的添加集群节点(多块数据盘)样例；添加已有节点时，请确保填写的分区信息在节点上真实存在
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataDisks: list of DataDisk\n        :param ExtraArgs: 节点相关的自定义参数信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`\n        :param DesiredPodNumber: 该节点属于podCIDR大小自定义模式时，可指定节点上运行的pod数量上限
注意：此字段可能返回 null，表示取不到有效值。\n        :type DesiredPodNumber: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDataDiskMountSetting(AbstractModel):
    """CVM实例数据盘挂载配置

    """

    def __init__(self):
        """
        :param InstanceType: CVM实例类型\n        :type InstanceType: str\n        :param DataDisks: 数据盘挂载信息\n        :type DataDisks: list of DataDisk\n        :param Zone: CVM实例所属可用区\n        :type Zone: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtraArgs(AbstractModel):
    """节点自定义参数

    """

    def __init__(self):
        """
        :param Kubelet: kubelet自定义参数，参数格式为["k1=v1", "k1=v2"]， 例如["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
注意：此字段可能返回 null，表示取不到有效值。\n        :type Kubelet: list of str\n        """
        self.Kubelet = None


    def _deserialize(self, params):
        self.Kubelet = params.get("Kubelet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeClusterStatus(AbstractModel):
    """节点升级过程中集群当前状态

    """

    def __init__(self):
        """
        :param PodTotal: pod总数\n        :type PodTotal: int\n        :param NotReadyPod: NotReady pod总数\n        :type NotReadyPod: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResult(AbstractModel):
    """某个节点升级前检查结果

    """

    def __init__(self):
        """
        :param CheckPass: 检查是否通过\n        :type CheckPass: bool\n        :param Items: 检查项数组\n        :type Items: list of InstanceUpgradePreCheckResultItem\n        :param SinglePods: 本节点独立pod列表\n        :type SinglePods: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResultItem(AbstractModel):
    """节点升级检查项结果

    """

    def __init__(self):
        """
        :param Namespace: 工作负载的命名空间\n        :type Namespace: str\n        :param WorkLoadKind: 工作负载类型\n        :type WorkLoadKind: str\n        :param WorkLoadName: 工作负载名称\n        :type WorkLoadName: str\n        :param Before: 驱逐节点前工作负载running的pod数目\n        :type Before: int\n        :param After: 驱逐节点后工作负载running的pod数目\n        :type After: int\n        :param Pods: 工作负载在本节点上的pod列表\n        :type Pods: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeProgressItem(AbstractModel):
    """某个节点的升级进度

    """

    def __init__(self):
        """
        :param InstanceID: 节点instanceID\n        :type InstanceID: str\n        :param LifeState: 任务生命周期
process 运行中
paused 已停止
pauing 正在停止
done  已完成
timeout 已超时
aborted 已取消
pending 还未开始\n        :type LifeState: str\n        :param StartAt: 升级开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartAt: str\n        :param EndAt: 升级结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndAt: str\n        :param CheckResult: 升级前检查结果\n        :type CheckResult: :class:`tencentcloud.tke.v20180525.models.InstanceUpgradePreCheckResult`\n        :param Detail: 升级步骤详情\n        :type Detail: list of TaskStepInfo\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s中标签，一般以数组的方式存在

    """

    def __init__(self):
        """
        :param Name: map表中的Name\n        :type Name: str\n        :param Value: map表中的Value\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        """
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Password: str\n        :param KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口[DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699)获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyIds: list of str\n        :param KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeepImageLogin: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManuallyAdded(AbstractModel):
    """手动加入的节点

    """

    def __init__(self):
        """
        :param Joining: 加入中的节点数量\n        :type Joining: int\n        :param Initializing: 初始化中的节点数量\n        :type Initializing: int\n        :param Normal: 正常的节点数量\n        :type Normal: int\n        :param Total: 节点总数\n        :type Total: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterAsGroupAttribute: 集群关联的伸缩组属性\n        :type ClusterAsGroupAttribute: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupAttribute`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAsGroupOptionAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ClusterAsGroupOption: 集群弹性伸缩属性\n        :type ClusterAsGroupOption: :class:`tencentcloud.tke.v20180525.models.ClusterAsGroupOption`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupOptionAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAttributeRequest(AbstractModel):
    """ModifyClusterAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param ProjectId: 集群所属项目\n        :type ProjectId: int\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        :param ClusterDesc: 集群描述\n        :type ClusterDesc: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAttributeResponse(AbstractModel):
    """ModifyClusterAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 集群所属项目
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: int\n        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        :param ClusterDesc: 集群描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterDesc: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.RequestId = params.get("RequestId")


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)\n        :type SecurityPolicies: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterNodePoolRequest(AbstractModel):
    """ModifyClusterNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param NodePoolId: 节点池ID\n        :type NodePoolId: str\n        :param Name: 名称\n        :type Name: str\n        :param MaxNodesNum: 最大节点数\n        :type MaxNodesNum: int\n        :param MinNodesNum: 最小节点数\n        :type MinNodesNum: int\n        :param Labels: 标签\n        :type Labels: list of Label\n        :param Taints: 污点\n        :type Taints: list of Taint\n        :param EnableAutoscale: 是否开启伸缩\n        :type EnableAutoscale: bool\n        :param OsName: 操作系统名称\n        :type OsName: str\n        :param OsCustomizeType: 镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)\n        :type OsCustomizeType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNodePoolResponse(AbstractModel):
    """ModifyClusterNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNodePoolDesiredCapacityAboutAsgRequest(AbstractModel):
    """ModifyNodePoolDesiredCapacityAboutAsg请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        :param DesiredCapacity: 节点池所关联的伸缩组的期望实例数\n        :type DesiredCapacity: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolDesiredCapacityAboutAsgResponse(AbstractModel):
    """ModifyNodePoolDesiredCapacityAboutAsg返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusAlertRuleRequest(AbstractModel):
    """ModifyPrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param AlertRule: 告警配置\n        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`\n        """
        self.InstanceId = None
        self.AlertRule = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self.AlertRule = PrometheusAlertRuleDetail()
            self.AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAlertRuleResponse(AbstractModel):
    """ModifyPrometheusAlertRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusTemplateRequest(AbstractModel):
    """ModifyPrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID\n        :type TemplateId: str\n        :param Template: 修改内容\n        :type Template: :class:`tencentcloud.tke.v20180525.models.PrometheusTemplateModify`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusTemplateResponse(AbstractModel):
    """ModifyPrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NodeCountSummary(AbstractModel):
    """节点统计列表

    """

    def __init__(self):
        """
        :param ManuallyAdded: 手动管理的节点
注意：此字段可能返回 null，表示取不到有效值。\n        :type ManuallyAdded: :class:`tencentcloud.tke.v20180525.models.ManuallyAdded`\n        :param AutoscalingAdded: 自动管理的节点
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoscalingAdded: :class:`tencentcloud.tke.v20180525.models.AutoscalingAdded`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePool(AbstractModel):
    """节点池描述

    """

    def __init__(self):
        """
        :param NodePoolId: NodePoolId 资源池id\n        :type NodePoolId: str\n        :param Name: Name 资源池名称\n        :type Name: str\n        :param ClusterInstanceId: ClusterInstanceId 集群实例id\n        :type ClusterInstanceId: str\n        :param LifeState: LifeState 状态，当前节点池生命周期状态包括：creating，normal，updating，deleting，deleted\n        :type LifeState: str\n        :param LaunchConfigurationId: LaunchConfigurationId 配置\n        :type LaunchConfigurationId: str\n        :param AutoscalingGroupId: AutoscalingGroupId 分组id\n        :type AutoscalingGroupId: str\n        :param Labels: Labels 标签\n        :type Labels: list of Label\n        :param Taints: Taints 污点标记\n        :type Taints: list of Taint\n        :param NodeCountSummary: NodeCountSummary 节点列表\n        :type NodeCountSummary: :class:`tencentcloud.tke.v20180525.models.NodeCountSummary`\n        :param AutoscalingGroupStatus: 状态信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type AutoscalingGroupStatus: str\n        :param MaxNodesNum: 最大节点数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxNodesNum: int\n        :param MinNodesNum: 最小节点数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinNodesNum: int\n        :param DesiredNodesNum: 期望的节点数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type DesiredNodesNum: int\n        :param NodePoolOs: 节点池osName
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodePoolOs: str\n        :param OsCustomizeType: 容器的镜像版本，"DOCKER_CUSTOMIZE"(容器定制版),"GENERAL"(普通版本，默认值)
注意：此字段可能返回 null，表示取不到有效值。\n        :type OsCustomizeType: str\n        :param ImageId: 镜像id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageId: str\n        :param DesiredPodNum: 集群属于节点podCIDR大小自定义模式时，节点池需要带上pod数量属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type DesiredPodNum: int\n        :param UserScript: 用户自定义脚本
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserScript: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePoolOption(AbstractModel):
    """加入存量节点时的节点池选项

    """

    def __init__(self):
        """
        :param AddToNodePool: 是否加入节点池\n        :type AddToNodePool: bool\n        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        :param InheritConfigurationFromNodePool: 是否继承节点池相关配置\n        :type InheritConfigurationFromNodePool: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsByType(AbstractModel):
    """某机型可支持的最大 VPC-CNI 模式的 Pod 数量

    """

    def __init__(self):
        """
        :param TKERouteENINonStaticIP: TKE共享网卡非固定IP模式可支持的Pod数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TKERouteENINonStaticIP: int\n        :param TKERouteENIStaticIP: TKE共享网卡固定IP模式可支持的Pod数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TKERouteENIStaticIP: int\n        :param TKEDirectENI: TKE独立网卡模式可支持的Pod数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TKEDirectENI: int\n        """
        self.TKERouteENINonStaticIP = None
        self.TKERouteENIStaticIP = None
        self.TKEDirectENI = None


    def _deserialize(self, params):
        self.TKERouteENINonStaticIP = params.get("TKERouteENINonStaticIP")
        self.TKERouteENIStaticIP = params.get("TKERouteENIStaticIP")
        self.TKEDirectENI = params.get("TKEDirectENI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsInstance(AbstractModel):
    """机型信息和其可支持的最大VPC-CNI模式Pod数量信息

    """

    def __init__(self):
        """
        :param Zone: 机型所在可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        :param InstanceFamily: 机型所属机型族
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceFamily: str\n        :param InstanceType: 实例机型名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceType: str\n        :param PodLimits: 机型可支持的最大VPC-CNI模式Pod数量信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodLimits: :class:`tencentcloud.tke.v20180525.models.PodLimitsByType`\n        """
        self.Zone = None
        self.InstanceFamily = None
        self.InstanceType = None
        self.PodLimits = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceFamily = params.get("InstanceFamily")
        self.InstanceType = params.get("InstanceType")
        if params.get("PodLimits") is not None:
            self.PodLimits = PodLimitsByType()
            self.PodLimits._deserialize(params.get("PodLimits"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAgentOverview(AbstractModel):
    """托管prometheus agent概览

    """

    def __init__(self):
        """
        :param ClusterType: 集群类型\n        :type ClusterType: str\n        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param Status: agent状态
normal = 正常
abnormal = 异常\n        :type Status: str\n        :param ClusterName: 集群名称\n        :type ClusterName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertHistoryItem(AbstractModel):
    """prometheus告警历史

    """

    def __init__(self):
        """
        :param RuleName: 告警名称\n        :type RuleName: str\n        :param StartTime: 告警开始时间\n        :type StartTime: str\n        :param Content: 告警内容\n        :type Content: str\n        :param State: 告警状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type State: str\n        :param RuleItem: 触发的规则名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleItem: str\n        :param TopicId: 告警渠道的id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicId: str\n        :param TopicName: 告警渠道的名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRule(AbstractModel):
    """Prometheus告警规则

    """

    def __init__(self):
        """
        :param Name: 规则名称\n        :type Name: str\n        :param Rule: prometheus语句\n        :type Rule: str\n        :param Labels: 额外标签\n        :type Labels: list of Label\n        :param Template: 告警发送模板\n        :type Template: str\n        :param For: 持续时间\n        :type For: str\n        :param Describe: 该条规则的描述信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Describe: str\n        :param Annotations: 参考prometheus rule中的annotations
注意：此字段可能返回 null，表示取不到有效值。\n        :type Annotations: list of Label\n        """
        self.Name = None
        self.Rule = None
        self.Labels = None
        self.Template = None
        self.For = None
        self.Describe = None
        self.Annotations = None


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
        if params.get("Annotations") is not None:
            self.Annotations = []
            for item in params.get("Annotations"):
                obj = Label()
                obj._deserialize(item)
                self.Annotations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertRuleDetail(AbstractModel):
    """托管prometheus告警配置实例

    """

    def __init__(self):
        """
        :param Name: 规则名称\n        :type Name: str\n        :param Rules: 规则列表\n        :type Rules: list of PrometheusAlertRule\n        :param UpdatedAt: 最后修改时间\n        :type UpdatedAt: str\n        :param Notification: 告警渠道\n        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotification`\n        :param Id: 告警 id\n        :type Id: str\n        :param TemplateId: 如果该告警来至模板下发，则TemplateId为模板id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TemplateId: str\n        :param Interval: 计算周期
注意：此字段可能返回 null，表示取不到有效值。\n        :type Interval: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfigItem(AbstractModel):
    """prometheus配置

    """

    def __init__(self):
        """
        :param Name: 名称\n        :type Name: str\n        :param Config: 配置内容\n        :type Config: str\n        :param TemplateId: 用于出参，如果该配置来至模板，则为模板id
注意：此字段可能返回 null，表示取不到有效值。\n        :type TemplateId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusGrafanaInfo(AbstractModel):
    """托管prometheus中grafana的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否启用\n        :type Enabled: bool\n        :param Domain: 域名，只有开启外网访问才有效果\n        :type Domain: str\n        :param Address: 内网地址，或者外网地址\n        :type Address: str\n        :param Internet: 是否开启了外网访问
close = 未开启外网访问
opening = 正在开启外网访问
open  = 已开启外网访问\n        :type Internet: str\n        :param AdminUser: grafana管理员用户名\n        :type AdminUser: str\n        """
        self.Enabled = None
        self.Domain = None
        self.Address = None
        self.Internet = None
        self.AdminUser = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Domain = params.get("Domain")
        self.Address = params.get("Address")
        self.Internet = params.get("Internet")
        self.AdminUser = params.get("AdminUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusInstanceOverview(AbstractModel):
    """托管prometheus实例概览

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param Name: 实例名称\n        :type Name: str\n        :param VpcId: 实例vpcId\n        :type VpcId: str\n        :param SubnetId: 实例子网Id\n        :type SubnetId: str\n        :param Status: 实例当前的状态
prepare_env = 初始化环境
install_suit = 安装组件
running = 运行中\n        :type Status: str\n        :param COSBucket: COS桶存储\n        :type COSBucket: str\n        :param GrafanaURL: grafana默认地址，如果开启外网访问得为域名，否则为内网地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type GrafanaURL: str\n        :param BoundTotal: 关联集群总数
注意：此字段可能返回 null，表示取不到有效值。\n        :type BoundTotal: int\n        :param BoundNormal: 运行正常的集群数
注意：此字段可能返回 null，表示取不到有效值。\n        :type BoundNormal: int\n        """
        self.InstanceId = None
        self.Name = None
        self.VpcId = None
        self.SubnetId = None
        self.Status = None
        self.COSBucket = None
        self.GrafanaURL = None
        self.BoundTotal = None
        self.BoundNormal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Name = params.get("Name")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Status = params.get("Status")
        self.COSBucket = params.get("COSBucket")
        self.GrafanaURL = params.get("GrafanaURL")
        self.BoundTotal = params.get("BoundTotal")
        self.BoundNormal = params.get("BoundNormal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusJobTargets(AbstractModel):
    """prometheus一个job的targets

    """

    def __init__(self):
        """
        :param Targets: 该Job的targets列表\n        :type Targets: list of PrometheusTarget\n        :param JobName: job的名称\n        :type JobName: str\n        :param Total: targets总数\n        :type Total: int\n        :param Up: 健康的target总数\n        :type Up: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotification(AbstractModel):
    """amp告警渠道配置

    """

    def __init__(self):
        """
        :param Enabled: 是否启用\n        :type Enabled: bool\n        :param RepeatInterval: 收敛时间\n        :type RepeatInterval: str\n        :param TimeRangeStart: 生效起始时间\n        :type TimeRangeStart: str\n        :param TimeRangeEnd: 生效结束时间\n        :type TimeRangeEnd: str\n        :param NotifyWay: 告警通知方式。目前有SMS、EMAIL、CALL、WECHAT方式。
分别代表：短信、邮件、电话、微信
注意：此字段可能返回 null，表示取不到有效值。\n        :type NotifyWay: list of str\n        :param ReceiverGroups: 告警接收组（用户组）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReceiverGroups: list of int non-negative\n        :param PhoneNotifyOrder: 电话告警顺序。
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneNotifyOrder: list of int non-negative\n        :param PhoneCircleTimes: 电话告警次数。
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneCircleTimes: int\n        :param PhoneInnerInterval: 电话告警轮内间隔。单位：秒
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneInnerInterval: int\n        :param PhoneCircleInterval: 电话告警轮外间隔。单位：秒
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneCircleInterval: int\n        :param PhoneArriveNotice: 电话告警触达通知
注：NotifyWay选择CALL，采用该参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneArriveNotice: bool\n        :param Type: 通道类型，默认为amp，支持以下
amp
webhook
注意：此字段可能返回 null，表示取不到有效值。\n        :type Type: str\n        :param WebHook: 如果Type为webhook, 则该字段为必填项
注意：此字段可能返回 null，表示取不到有效值。\n        :type WebHook: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTarget(AbstractModel):
    """prometheus一个抓取目标的信息

    """

    def __init__(self):
        """
        :param Url: 抓取目标的URL\n        :type Url: str\n        :param State: target当前状态,当前支持
up = 健康
down = 不健康
unknown = 未知\n        :type State: str\n        :param Labels: target的元label\n        :type Labels: list of Label\n        :param LastScrape: 上一次抓取的时间\n        :type LastScrape: str\n        :param ScrapeDuration: 上一次抓取的耗时，单位是s\n        :type ScrapeDuration: float\n        :param Error: 上一次抓取如果错误，该字段存储错误信息\n        :type Error: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplate(AbstractModel):
    """模板实例

    """

    def __init__(self):
        """
        :param Name: 模板名称\n        :type Name: str\n        :param Level: 模板维度，支持以下类型
instance 实例级别
cluster 集群级别\n        :type Level: str\n        :param Describe: 模板描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Describe: str\n        :param AlertRules: 当Level为instance时有效，
模板中的告警配置列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlertRules: list of PrometheusAlertRule\n        :param RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordRules: list of PrometheusConfigItem\n        :param ServiceMonitors: 当Level为cluster时有效，
模板中的ServiceMonitor规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceMonitors: list of PrometheusConfigItem\n        :param PodMonitors: 当Level为cluster时有效，
模板中的PodMonitors规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodMonitors: list of PrometheusConfigItem\n        :param RawJobs: 当Level为cluster时有效，
模板中的RawJobs规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RawJobs: list of PrometheusConfigItem\n        :param TemplateId: 模板的ID, 用于出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type TemplateId: str\n        :param UpdateTime: 最近更新时间，用于出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param Version: 当前版本，用于出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param IsDefault: 是否系统提供的默认模板，用于出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDefault: bool\n        :param AlertDetailRules: 当Level为instance时有效，
模板中的告警配置列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlertDetailRules: list of PrometheusAlertRuleDetail\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateModify(AbstractModel):
    """云原生Prometheus模板可修改项

    """

    def __init__(self):
        """
        :param Name: 修改名称\n        :type Name: str\n        :param Describe: 修改描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Describe: str\n        :param AlertRules: 修改内容，只有当模板类型是Alert时生效
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlertRules: list of PrometheusAlertRule\n        :param RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecordRules: list of PrometheusConfigItem\n        :param ServiceMonitors: 当Level为cluster时有效，
模板中的ServiceMonitor规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceMonitors: list of PrometheusConfigItem\n        :param PodMonitors: 当Level为cluster时有效，
模板中的PodMonitors规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type PodMonitors: list of PrometheusConfigItem\n        :param RawJobs: 当Level为cluster时有效，
模板中的RawJobs规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RawJobs: list of PrometheusConfigItem\n        :param AlertDetailRules: 修改内容，只有当模板类型是Alert时生效
注意：此字段可能返回 null，表示取不到有效值。\n        :type AlertDetailRules: list of PrometheusAlertRuleDetail\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateSyncTarget(AbstractModel):
    """云原生Prometheus模板同步目标

    """

    def __init__(self):
        """
        :param Region: 目标所在地域\n        :type Region: str\n        :param InstanceId: 目标实例\n        :type InstanceId: str\n        :param ClusterId: 集群id，只有当采集模板的Level为cluster的时候需要
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterId: str\n        :param SyncTime: 最后一次同步时间， 用于出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type SyncTime: str\n        :param Version: 当前使用的模板版本，用于出参
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param ClusterType: 集群类型，只有当采集模板的Level为cluster的时候需要
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterType: str\n        :param InstanceName: 用于出参，实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param ClusterName: 用于出参，集群名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClusterName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstance(AbstractModel):
    """地域属性信息

    """

    def __init__(self):
        """
        :param RegionName: 地域名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionName: str\n        :param RegionId: 地域ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionId: int\n        :param Status: 地域状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param FeatureGates: 地域特性开关(按照JSON的形式返回所有属性)
注意：此字段可能返回 null，表示取不到有效值。\n        :type FeatureGates: str\n        :param Alias: 地域简称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        :param Remark: 地域白名单
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolRequest(AbstractModel):
    """RemoveNodeFromNodePool请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        :param InstanceIds: 节点id列表，一次最多支持100台\n        :type InstanceIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolResponse(AbstractModel):
    """RemoveNodeFromNodePool返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceDeleteOption(AbstractModel):
    """资源删除选项

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型，例如CBS\n        :type ResourceType: str\n        :param DeleteMode: 集群删除时资源的删除模式：terminate（销毁），retain （保留）\n        :type DeleteMode: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteInfo(AbstractModel):
    """集群路由对象

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        :param DestinationCidrBlock: 目的端CIDR。\n        :type DestinationCidrBlock: str\n        :param GatewayIp: 下一跳地址。\n        :type GatewayIp: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableConflict(AbstractModel):
    """路由表冲突对象

    """

    def __init__(self):
        """
        :param RouteTableType: 路由表类型。\n        :type RouteTableType: str\n        :param RouteTableCidrBlock: 路由表CIDR。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableCidrBlock: str\n        :param RouteTableName: 路由表名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableName: str\n        :param RouteTableId: 路由表ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableInfo(AbstractModel):
    """集群路由表对象

    """

    def __init__(self):
        """
        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        :param RouteTableCidrBlock: 路由表CIDR。\n        :type RouteTableCidrBlock: str\n        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesForNode(AbstractModel):
    """不同角色的节点配置参数

    """

    def __init__(self):
        """
        :param NodeRole: 节点角色，取值:MASTER_ETCD, WORKER。MASTER_ETCD只有在创建 INDEPENDENT_CLUSTER 独立集群时需要指定。MASTER_ETCD节点数量为3～7，建议为奇数。MASTER_ETCD节点最小配置为4C8G。\n        :type NodeRole: str\n        :param RunInstancesPara: CVM创建透传参数，json化字符串格式，详见[CVM创建实例](https://cloud.tencent.com/document/product/213/15730)接口，传入公共参数外的其他参数即可，其中ImageId会替换为TKE集群OS对应的镜像。\n        :type RunInstancesPara: list of str\n        :param InstanceAdvancedSettingsOverrides: 节点高级设置，该参数会覆盖集群级别设置的InstanceAdvancedSettings，和上边的RunInstancesPara按照顺序一一对应（当前只对节点自定义参数ExtraArgs生效）。\n        :type InstanceAdvancedSettingsOverrides: list of InstanceAdvancedSettings\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启[云监控](/document/product/248)服务。取值范围：<br><li>TRUE：表示开启云监控服务<br><li>FALSE：表示不开启云监控服务<br><br>默认取值：TRUE。\n        :type Enabled: bool\n        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开启[云安全](/document/product/296)服务。取值范围：<br><li>TRUE：表示开启云安全服务<br><li>FALSE：表示不开启云安全服务<br><br>默认取值：TRUE。\n        :type Enabled: bool\n        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionRequest(AbstractModel):
    """SetNodePoolNodeProtection请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群id\n        :type ClusterId: str\n        :param NodePoolId: 节点池id\n        :type NodePoolId: str\n        :param InstanceIds: 节点id\n        :type InstanceIds: list of str\n        :param ProtectedFromScaleIn: 节点是否需要移出保护\n        :type ProtectedFromScaleIn: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionResponse(AbstractModel):
    """SetNodePoolNodeProtection返回参数结构体

    """

    def __init__(self):
        """
        :param SucceedInstanceIds: 成功设置的节点id
注意：此字段可能返回 null，表示取不到有效值。\n        :type SucceedInstanceIds: list of str\n        :param FailedInstanceIds: 没有成功设置的节点id
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedInstanceIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SucceedInstanceIds = None
        self.FailedInstanceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SucceedInstanceIds = params.get("SucceedInstanceIds")
        self.FailedInstanceIds = params.get("FailedInstanceIds")
        self.RequestId = params.get("RequestId")


class SyncPrometheusTemplateRequest(AbstractModel):
    """SyncPrometheusTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 实例id\n        :type TemplateId: str\n        :param Targets: 同步目标\n        :type Targets: list of PrometheusTemplateSyncTarget\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPrometheusTemplateResponse(AbstractModel):
    """SyncPrometheusTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签绑定的资源类型，当前支持类型："cluster"

    """

    def __init__(self):
        """
        :param Key: 标签键\n        :type Key: str\n        :param Value: 标签值\n        :type Value: str\n        """
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
        


class TagSpecification(AbstractModel):
    """标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云主机实例。

    """

    def __init__(self):
        """
        :param ResourceType: 标签绑定的资源类型，当前支持类型："cluster"
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceType: str\n        :param Tags: 标签对列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Taint(AbstractModel):
    """kubernetes Taint

    """

    def __init__(self):
        """
        :param Key: Key\n        :type Key: str\n        :param Value: Value\n        :type Value: str\n        :param Effect: Effect\n        :type Effect: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStepInfo(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        """
        :param Step: 步骤名称\n        :type Step: str\n        :param LifeState: 生命周期
pending : 步骤未开始
running: 步骤执行中
success: 步骤成功完成
failed: 步骤失败\n        :type LifeState: str\n        :param StartAt: 步骤开始时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartAt: str\n        :param EndAt: 步骤结束时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndAt: str\n        :param FailedMsg: 若步骤生命周期为failed,则此字段显示错误信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailedMsg: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClusterVersionRequest(AbstractModel):
    """UpdateClusterVersion请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群 Id\n        :type ClusterId: str\n        :param DstVersion: 需要升级到的版本\n        :type DstVersion: str\n        :param ExtraArgs: 集群自定义参数\n        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`\n        :param MaxNotReadyPercent: 可容忍的最大不可用pod数目\n        :type MaxNotReadyPercent: float\n        :param SkipPreCheck: 是否跳过预检查阶段\n        :type SkipPreCheck: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClusterVersionResponse(AbstractModel):
    """UpdateClusterVersion返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateEKSClusterRequest(AbstractModel):
    """UpdateEKSCluster请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 弹性集群Id\n        :type ClusterId: str\n        :param ClusterName: 弹性集群名称\n        :type ClusterName: str\n        :param ClusterDesc: 弹性集群描述信息\n        :type ClusterDesc: str\n        :param SubnetIds: 子网Id 列表\n        :type SubnetIds: list of str\n        :param PublicLB: 弹性容器集群公网访问LB信息\n        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.ClusterPublicLB`\n        :param InternalLB: 弹性容器集群内网访问LB信息\n        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.ClusterInternalLB`\n        :param ServiceSubnetId: Service 子网Id\n        :type ServiceSubnetId: str\n        :param DnsServers: 集群自定义的dns 服务器信息\n        :type DnsServers: list of DnsServerConf\n        :param ClearDnsServer: 是否清空自定义dns 服务器设置。为1 表示 是。其他表示 否。\n        :type ClearDnsServer: str\n        :param NeedDeleteCbs: 将来删除集群时是否要删除cbs。默认为 FALSE\n        :type NeedDeleteCbs: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEKSClusterResponse(AbstractModel):
    """UpdateEKSCluster返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeAbleInstancesItem(AbstractModel):
    """可升级节点信息

    """

    def __init__(self):
        """
        :param InstanceId: 节点Id\n        :type InstanceId: str\n        :param Version: 节点的当前版本\n        :type Version: str\n        :param LatestVersion: 当前版本的最新小版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type LatestVersion: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesRequest(AbstractModel):
    """UpgradeClusterInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ClusterId: 集群ID\n        :type ClusterId: str\n        :param Operation: create 表示开始一次升级任务
pause 表示停止任务
resume表示继续任务
abort表示终止任务\n        :type Operation: str\n        :param UpgradeType: 升级类型，只有Operation是create需要设置
reset 大版本重装升级
hot 小版本热升级
major 大版本原地升级\n        :type UpgradeType: str\n        :param InstanceIds: 需要升级的节点列表\n        :type InstanceIds: list of str\n        :param ResetParam: 当节点重新加入集群时候所使用的参数，参考添加已有节点接口\n        :type ResetParam: :class:`tencentcloud.tke.v20180525.models.UpgradeNodeResetParam`\n        :param SkipPreCheck: 是否忽略节点升级前检查\n        :type SkipPreCheck: bool\n        :param MaxNotReadyPercent: 最大可容忍的不可用Pod比例\n        :type MaxNotReadyPercent: float\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesResponse(AbstractModel):
    """UpgradeClusterInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeNodeResetParam(AbstractModel):
    """节点升级重装参数

    """

    def __init__(self):
        """
        :param InstanceAdvancedSettings: 实例额外需要设置参数信息\n        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`\n        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。\n        :type EnhancedService: :class:`tencentcloud.tke.v20180525.models.EnhancedService`\n        :param LoginSettings: 节点登录信息（目前仅支持使用Password或者单个KeyIds）\n        :type LoginSettings: :class:`tencentcloud.tke.v20180525.models.LoginSettings`\n        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。（目前仅支持设置单个sgId）\n        :type SecurityGroupIds: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionInstance(AbstractModel):
    """版本信息

    """

    def __init__(self):
        """
        :param Name: 版本名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Version: 版本信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Version: str\n        :param Remark: Remark
注意：此字段可能返回 null，表示取不到有效值。\n        :type Remark: str\n        """
        self.Name = None
        self.Version = None
        self.Remark = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        