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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcquireClusterAdminRoleResponse(AbstractModel):
    """AcquireClusterAdminRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddClusterCIDRRequest(AbstractModel):
    """AddClusterCIDR请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterCIDRs: 增加的ClusterCIDR
        :type ClusterCIDRs: list of str
        :param IgnoreClusterCIDRConflict: 是否忽略ClusterCIDR与VPC路由表的冲突
        :type IgnoreClusterCIDRConflict: bool
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddExistedInstancesRequest(AbstractModel):
    """AddExistedInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddExistedInstancesResponse(AbstractModel):
    """AddExistedInstances返回参数结构体

    """

    def __init__(self):
        r"""
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


class AddNodeToNodePoolRequest(AbstractModel):
    """AddNodeToNodePool请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodeToNodePoolResponse(AbstractModel):
    """AddNodeToNodePool返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddVpcCniSubnetsRequest(AbstractModel):
    """AddVpcCniSubnets请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SubnetIds: 为集群容器网络增加的子网列表
        :type SubnetIds: list of str
        :param VpcId: 集群所属的VPC的ID
        :type VpcId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AppChart(AbstractModel):
    """app所支持的chart

    """

    def __init__(self):
        r"""
        :param Name: chart名称
        :type Name: str
        :param Label: chart的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param LatestVersion: chart的版本
        :type LatestVersion: str
        """
        self.Name = None
        self.Label = None
        self.LatestVersion = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Label = params.get("Label")
        self.LatestVersion = params.get("LatestVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalingGroupRange(AbstractModel):
    """集群关联的伸缩组最大实例数最小值实例数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoUpgradeClusterLevel(AbstractModel):
    """自动变配集群等级

    """

    def __init__(self):
        r"""
        :param IsAutoUpgrade: 是否开启自动变配集群等级
        :type IsAutoUpgrade: bool
        """
        self.IsAutoUpgrade = None


    def _deserialize(self, params):
        self.IsAutoUpgrade = params.get("IsAutoUpgrade")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Capabilities(AbstractModel):
    """cloudrun安全特性能力

    """

    def __init__(self):
        r"""
        :param Add: 启用安全能力项列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Add: list of str
        :param Drop: 禁用安全能力向列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Drop: list of str
        """
        self.Add = None
        self.Drop = None


    def _deserialize(self, params):
        self.Add = params.get("Add")
        self.Drop = params.get("Drop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CbsVolume(AbstractModel):
    """EKS Instnace CBS volume

    """

    def __init__(self):
        r"""
        :param Name: cbs volume 数据卷名称
        :type Name: str
        :param CbsDiskId: 腾讯云cbs盘Id
        :type CbsDiskId: str
        """
        self.Name = None
        self.CbsDiskId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CbsDiskId = params.get("CbsDiskId")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckInstancesUpgradeAbleResponse(AbstractModel):
    """CheckInstancesUpgradeAble返回参数结构体

    """

    def __init__(self):
        r"""
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


class Cluster(AbstractModel):
    """集群信息结构体

    """

    def __init__(self):
        r"""
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
        :param ClusterStatus: 集群状态 (Running 运行中  Creating 创建中 Idling 闲置中  Abnormal 异常  )
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
        :param EnableExternalNode: 集群是否开启第三方节点支持
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableExternalNode: bool
        :param ClusterLevel: 集群等级，针对托管集群生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: 自动变配集群等级，针对托管集群生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoUpgradeClusterLevel: bool
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
        self.EnableExternalNode = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None


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
        self.ClusterLevel = params.get("ClusterLevel")
        self.AutoUpgradeClusterLevel = params.get("AutoUpgradeClusterLevel")
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
        r"""
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
        :param VpcCniType: 区分共享网卡多IP模式和独立网卡模式，共享网卡多 IP 模式填写"tke-route-eni"，独立网卡模式填写"tke-direct-eni"，默认为共享网卡模式
        :type VpcCniType: str
        :param RuntimeVersion: 运行时版本
        :type RuntimeVersion: str
        :param EnableCustomizedPodCIDR: 是否开节点podCIDR大小的自定义模式
        :type EnableCustomizedPodCIDR: bool
        :param BasePodNumber: 自定义模式下的基础pod数量
        :type BasePodNumber: int
        :param CiliumMode: 启用 CiliumMode 的模式，空值表示不启用，“clusterIP” 表示启用 Cilium 支持 ClusterIP
        :type CiliumMode: str
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupAttribute(AbstractModel):
    """集群伸缩组属性

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterAsGroupOption(AbstractModel):
    """集群弹性伸缩配置

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterBasicSettings(AbstractModel):
    """描述集群的基本配置信息

    """

    def __init__(self):
        r"""
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
        :param NeedWorkSecurityGroup: 是否开启节点的默认安全组(默认: 否，Alpha特性)
        :type NeedWorkSecurityGroup: bool
        :param SubnetId: 当选择Cilium Overlay网络插件时，TKE会从该子网获取2个IP用来创建内网负载均衡
        :type SubnetId: str
        :param ClusterLevel: 集群等级，针对托管集群生效
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: 自动变配集群等级，针对托管集群生效
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
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
        self.SubnetId = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None


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
        self.SubnetId = params.get("SubnetId")
        self.ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self.AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self.AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
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
        r"""
        :param ClusterCIDR: 用于分配集群容器和服务 IP 的 CIDR，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突。且网段范围必须在内网网段内，例如:10.1.0.0/14, 192.168.0.1/18,172.16.0.0/16。
        :type ClusterCIDR: str
        :param IgnoreClusterCIDRConflict: 是否忽略 ClusterCIDR 冲突错误, 默认不忽略
        :type IgnoreClusterCIDRConflict: bool
        :param MaxNodePodNum: 集群中每个Node上最大的Pod数量。取值范围4～256。不为2的幂值时会向上取最接近的2的幂值。
        :type MaxNodePodNum: int
        :param MaxClusterServiceNum: 集群最大的service数量。取值范围32～32768，不为2的幂值时会向上取最接近的2的幂值。默认值256
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterCredential(AbstractModel):
    """接入k8s 的认证信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterExtraArgs(AbstractModel):
    """集群master自定义参数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterInternalLB(AbstractModel):
    """弹性容器集群内网访问LB信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterLevelAttribute(AbstractModel):
    """托管集群等级属性

    """

    def __init__(self):
        r"""
        :param Name: 集群等级
        :type Name: str
        :param Alias: 等级名称
        :type Alias: str
        :param NodeCount: 节点数量
        :type NodeCount: int
        :param PodCount: Pod数量
        :type PodCount: int
        :param ConfigMapCount: Configmap数量
        :type ConfigMapCount: int
        :param CRDCount: CRD数量
        :type CRDCount: int
        :param Enable: 是否启用
        :type Enable: bool
        :param OtherCount: 其他资源数量
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherCount: int
        """
        self.Name = None
        self.Alias = None
        self.NodeCount = None
        self.PodCount = None
        self.ConfigMapCount = None
        self.CRDCount = None
        self.Enable = None
        self.OtherCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Alias = params.get("Alias")
        self.NodeCount = params.get("NodeCount")
        self.PodCount = params.get("PodCount")
        self.ConfigMapCount = params.get("ConfigMapCount")
        self.CRDCount = params.get("CRDCount")
        self.Enable = params.get("Enable")
        self.OtherCount = params.get("OtherCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterLevelChangeRecord(AbstractModel):
    """集群等级变配记录

    """

    def __init__(self):
        r"""
        :param ID: 记录ID
        :type ID: str
        :param ClusterID: 集群ID
        :type ClusterID: str
        :param Status: 变配状态：trading 发货中,upgrading 变配中,success 变配成功,failed 变配失败。
        :type Status: str
        :param Message: 状态描述
        :type Message: str
        :param OldLevel: 变配前规模
        :type OldLevel: str
        :param NewLevel: 变配后规模
        :type NewLevel: str
        :param TriggerType: 变配触发类型：manual 手动,auto 自动
        :type TriggerType: str
        :param StartedAt: 开始时间
        :type StartedAt: str
        :param EndedAt: 结束时间
        :type EndedAt: str
        """
        self.ID = None
        self.ClusterID = None
        self.Status = None
        self.Message = None
        self.OldLevel = None
        self.NewLevel = None
        self.TriggerType = None
        self.StartedAt = None
        self.EndedAt = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.ClusterID = params.get("ClusterID")
        self.Status = params.get("Status")
        self.Message = params.get("Message")
        self.OldLevel = params.get("OldLevel")
        self.NewLevel = params.get("NewLevel")
        self.TriggerType = params.get("TriggerType")
        self.StartedAt = params.get("StartedAt")
        self.EndedAt = params.get("EndedAt")
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
        r"""
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
        :param KubeProxyMode: service的网络模式，当前参数只适用于ipvs+bpf模式
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeProxyMode: str
        :param ServiceCIDR: 用于分配service的IP range，不得与 VPC CIDR 冲突，也不得与同 VPC 内其他集群 CIDR 冲突
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCIDR: str
        :param Subnets: 集群关联的容器子网
注意：此字段可能返回 null，表示取不到有效值。
        :type Subnets: list of str
        """
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
        r"""
        :param Enabled: 是否开启公网访问LB
        :type Enabled: bool
        :param AllowFromCidrs: 允许访问的来源CIDR列表
        :type AllowFromCidrs: list of str
        :param SecurityPolicies: 安全策略放通单个IP或CIDR(例如: "192.168.1.0/24",默认为拒绝所有)
        :type SecurityPolicies: list of str
        :param ExtraParam: 外网访问相关的扩展参数，格式为json
        :type ExtraParam: str
        :param SecurityGroup: 新内外网功能，需要传递安全组
        :type SecurityGroup: str
        """
        self.Enabled = None
        self.AllowFromCidrs = None
        self.SecurityPolicies = None
        self.ExtraParam = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.AllowFromCidrs = params.get("AllowFromCidrs")
        self.SecurityPolicies = params.get("SecurityPolicies")
        self.ExtraParam = params.get("ExtraParam")
        self.SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterStatus(AbstractModel):
    """集群状态信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param ClusterState: 集群状态
        :type ClusterState: str
        :param ClusterInstanceState: 集群下机器实例的状态
        :type ClusterInstanceState: str
        :param ClusterBMonitor: 集群是否开启监控
        :type ClusterBMonitor: bool
        :param ClusterInitNodeNum: 集群创建中的节点数，-1表示获取节点状态超时，-2表示获取节点状态失败
        :type ClusterInitNodeNum: int
        :param ClusterRunningNodeNum: 集群运行中的节点数，-1表示获取节点状态超时，-2表示获取节点状态失败
        :type ClusterRunningNodeNum: int
        :param ClusterFailedNodeNum: 集群异常的节点数，-1表示获取节点状态超时，-2表示获取节点状态失败
        :type ClusterFailedNodeNum: int
        :param ClusterClosedNodeNum: 集群已关机的节点数，-1表示获取节点状态超时，-2表示获取节点状态失败
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterClosedNodeNum: int
        :param ClusterClosingNodeNum: 集群关机中的节点数，-1表示获取节点状态超时，-2表示获取节点状态失败
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterClosingNodeNum: int
        :param ClusterDeletionProtection: 集群是否开启删除保护
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterDeletionProtection: bool
        :param ClusterAuditEnabled: 集群是否可审计
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterAuditEnabled: bool
        """
        self.ClusterId = None
        self.ClusterState = None
        self.ClusterInstanceState = None
        self.ClusterBMonitor = None
        self.ClusterInitNodeNum = None
        self.ClusterRunningNodeNum = None
        self.ClusterFailedNodeNum = None
        self.ClusterClosedNodeNum = None
        self.ClusterClosingNodeNum = None
        self.ClusterDeletionProtection = None
        self.ClusterAuditEnabled = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterState = params.get("ClusterState")
        self.ClusterInstanceState = params.get("ClusterInstanceState")
        self.ClusterBMonitor = params.get("ClusterBMonitor")
        self.ClusterInitNodeNum = params.get("ClusterInitNodeNum")
        self.ClusterRunningNodeNum = params.get("ClusterRunningNodeNum")
        self.ClusterFailedNodeNum = params.get("ClusterFailedNodeNum")
        self.ClusterClosedNodeNum = params.get("ClusterClosedNodeNum")
        self.ClusterClosingNodeNum = params.get("ClusterClosingNodeNum")
        self.ClusterDeletionProtection = params.get("ClusterDeletionProtection")
        self.ClusterAuditEnabled = params.get("ClusterAuditEnabled")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommonName(AbstractModel):
    """账户UIN与客户端证书CommonName的映射

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Container(AbstractModel):
    """EKS Instance Container容器

    """

    def __init__(self):
        r"""
        :param Image: 镜像
        :type Image: str
        :param Name: 容器名
        :type Name: str
        :param Commands: 容器启动命令
        :type Commands: list of str
        :param Args: 容器启动参数
        :type Args: list of str
        :param EnvironmentVars: 容器内操作系统的环境变量
        :type EnvironmentVars: list of EnvironmentVariable
        :param Cpu: CPU，制改容器最多可使用的核数，该值不可超过容器实例的总核数。单位：核。
        :type Cpu: float
        :param Memory: 内存，限制该容器最多可使用的内存值，该值不可超过容器实例的总内存值。单位：GiB
        :type Memory: float
        :param VolumeMounts: 数据卷挂载信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMounts: list of VolumeMount
        :param CurrentState: 当前状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentState: :class:`tencentcloud.tke.v20180525.models.ContainerState`
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param WorkingDir: 容器工作目录
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkingDir: str
        :param LivenessProbe: 存活探针
注意：此字段可能返回 null，表示取不到有效值。
        :type LivenessProbe: :class:`tencentcloud.tke.v20180525.models.LivenessOrReadinessProbe`
        :param ReadinessProbe: 就绪探针
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadinessProbe: :class:`tencentcloud.tke.v20180525.models.LivenessOrReadinessProbe`
        :param GpuLimit: Gpu限制
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuLimit: int
        :param SecurityContext: 容器的安全上下文
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityContext: :class:`tencentcloud.tke.v20180525.models.SecurityContext`
        """
        self.Image = None
        self.Name = None
        self.Commands = None
        self.Args = None
        self.EnvironmentVars = None
        self.Cpu = None
        self.Memory = None
        self.VolumeMounts = None
        self.CurrentState = None
        self.RestartCount = None
        self.WorkingDir = None
        self.LivenessProbe = None
        self.ReadinessProbe = None
        self.GpuLimit = None
        self.SecurityContext = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Name = params.get("Name")
        self.Commands = params.get("Commands")
        self.Args = params.get("Args")
        if params.get("EnvironmentVars") is not None:
            self.EnvironmentVars = []
            for item in params.get("EnvironmentVars"):
                obj = EnvironmentVariable()
                obj._deserialize(item)
                self.EnvironmentVars.append(obj)
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        if params.get("VolumeMounts") is not None:
            self.VolumeMounts = []
            for item in params.get("VolumeMounts"):
                obj = VolumeMount()
                obj._deserialize(item)
                self.VolumeMounts.append(obj)
        if params.get("CurrentState") is not None:
            self.CurrentState = ContainerState()
            self.CurrentState._deserialize(params.get("CurrentState"))
        self.RestartCount = params.get("RestartCount")
        self.WorkingDir = params.get("WorkingDir")
        if params.get("LivenessProbe") is not None:
            self.LivenessProbe = LivenessOrReadinessProbe()
            self.LivenessProbe._deserialize(params.get("LivenessProbe"))
        if params.get("ReadinessProbe") is not None:
            self.ReadinessProbe = LivenessOrReadinessProbe()
            self.ReadinessProbe._deserialize(params.get("ReadinessProbe"))
        self.GpuLimit = params.get("GpuLimit")
        if params.get("SecurityContext") is not None:
            self.SecurityContext = SecurityContext()
            self.SecurityContext._deserialize(params.get("SecurityContext"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerState(AbstractModel):
    """容器状态

    """

    def __init__(self):
        r"""
        :param StartTime: 容器运行开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param State: 容器状态：created, running, exited, unknown
        :type State: str
        :param FinishTime: 容器运行结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FinishTime: str
        :param ExitCode: 容器运行退出码
注意：此字段可能返回 null，表示取不到有效值。
        :type ExitCode: int
        :param Reason: 容器状态 Reason
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param Message: 容器状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param RestartCount: 容器重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        """
        self.StartTime = None
        self.State = None
        self.FinishTime = None
        self.ExitCode = None
        self.Reason = None
        self.Message = None
        self.RestartCount = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.State = params.get("State")
        self.FinishTime = params.get("FinishTime")
        self.ExitCode = params.get("ExitCode")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        self.RestartCount = params.get("RestartCount")
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
        r"""
        :param Name: 控制器的名字
        :type Name: str
        :param Enabled: 控制器是否开启
        :type Enabled: bool
        """
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
        


class CreateClusterEndpointRequest(AbstractModel):
    """CreateClusterEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SubnetId: 集群端口所在的子网ID  (仅在开启非外网访问时需要填，必须为集群所在VPC内的子网)
        :type SubnetId: str
        :param IsExtranet: 是否为外网访问（TRUE 外网访问 FALSE 内网访问，默认值： FALSE）
        :type IsExtranet: bool
        :param Domain: 设置域名
        :type Domain: str
        :param SecurityGroup: 使用的安全组，只有外网访问需要传递
        :type SecurityGroup: str
        :param ExtensiveParameters: 创建lb参数，只有外网访问需要设置
        :type ExtensiveParameters: str
        """
        self.ClusterId = None
        self.SubnetId = None
        self.IsExtranet = None
        self.Domain = None
        self.SecurityGroup = None
        self.ExtensiveParameters = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SubnetId = params.get("SubnetId")
        self.IsExtranet = params.get("IsExtranet")
        self.Domain = params.get("Domain")
        self.SecurityGroup = params.get("SecurityGroup")
        self.ExtensiveParameters = params.get("ExtensiveParameters")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateClusterEndpointVipRequest(AbstractModel):
    """CreateClusterEndpointVip请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterEndpointVipResponse(AbstractModel):
    """CreateClusterEndpointVip返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateClusterInstancesRequest(AbstractModel):
    """CreateClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterInstancesResponse(AbstractModel):
    """CreateClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateClusterNodePoolFromExistingAsgRequest(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterNodePoolFromExistingAsgResponse(AbstractModel):
    """CreateClusterNodePoolFromExistingAsg返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateClusterNodePoolRequest(AbstractModel):
    """CreateClusterNodePool请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param Tags: 资源标签
        :type Tags: list of Tag
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
        self.Tags = None


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
        


class CreateClusterNodePoolResponse(AbstractModel):
    """CreateClusterNodePool返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param ExistedInstancesForNode: 已存在实例的配置信息。所有实例必须在同一个VPC中，最大数量不超过100，不支持添加竞价实例。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRouteResponse(AbstractModel):
    """CreateClusterRoute返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRouteTableResponse(AbstractModel):
    """CreateClusterRouteTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEKSClusterRequest(AbstractModel):
    """CreateEKSCluster请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEKSClusterResponse(AbstractModel):
    """CreateEKSCluster返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateEKSContainerInstancesRequest(AbstractModel):
    """CreateEKSContainerInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Containers: 容器组
        :type Containers: list of Container
        :param EksCiName: EKS Container Instance容器实例名称
        :type EksCiName: str
        :param SecurityGroupIds: 指定新创建实例所属于的安全组Id
        :type SecurityGroupIds: list of str
        :param SubnetId: 实例所属子网Id
        :type SubnetId: str
        :param VpcId: 实例所属VPC的Id
        :type VpcId: str
        :param Memory: 内存，单位：GiB。可参考[资源规格](https://cloud.tencent.com/document/product/457/39808)文档
        :type Memory: float
        :param Cpu: CPU，单位：核。可参考[资源规格](https://cloud.tencent.com/document/product/457/39808)文档
        :type Cpu: float
        :param RestartPolicy: 实例重启策略： Always(总是重启)、Never(从不重启)、OnFailure(失败时重启)，默认：Always。
        :type RestartPolicy: str
        :param ImageRegistryCredentials: 镜像仓库凭证数组
        :type ImageRegistryCredentials: list of ImageRegistryCredential
        :param EksCiVolume: 数据卷，包含NfsVolume数组和CbsVolume数组
        :type EksCiVolume: :class:`tencentcloud.tke.v20180525.models.EksCiVolume`
        :param Replicas: 实例副本数，默认为1
        :type Replicas: int
        :param InitContainers: Init 容器
        :type InitContainers: list of Container
        :param DnsConfig: 自定义DNS配置
        :type DnsConfig: :class:`tencentcloud.tke.v20180525.models.DNSConfig`
        :param ExistedEipIds: 用来绑定容器实例的已有EIP的列表。如传值，需要保证数值和Replicas相等。
另外此参数和AutoCreateEipAttribute互斥。
        :type ExistedEipIds: list of str
        :param AutoCreateEipAttribute: 自动创建EIP的可选参数。若传此参数，则会自动创建EIP。
另外此参数和ExistedEipIds互斥
        :type AutoCreateEipAttribute: :class:`tencentcloud.tke.v20180525.models.EipAttribute`
        :param AutoCreateEip: 是否为容器实例自动创建EIP，默认为false。若传true，则此参数和ExistedEipIds互斥
        :type AutoCreateEip: bool
        :param CpuType: Pod 所需的 CPU 资源型号，如果不填写则默认不强制指定 CPU 类型。目前支持型号如下：
intel
amd
- 支持优先级顺序写法，如 “amd,intel” 表示优先创建 amd 资源 Pod，如果所选地域可用区 amd 资源不足，则会创建 intel 资源 Pod。
        :type CpuType: str
        :param GpuType: 容器实例所需的 GPU 资源型号，目前支持型号如下：
1/4\*V100
1/2\*V100
V100
1/4\*T4
1/2\*T4
T4
        :type GpuType: str
        :param GpuCount: Pod 所需的 GPU 数量，如填写，请确保为支持的规格。默认单位为卡，无需再次注明。
        :type GpuCount: int
        :param CamRoleName: 为容器实例关联 CAM 角色，value 填写 CAM 角色名称，容器实例可获取该 CAM 角色包含的权限策略，方便 容器实例 内的程序进行如购买资源、读写存储等云资源操作。
        :type CamRoleName: str
        """
        self.Containers = None
        self.EksCiName = None
        self.SecurityGroupIds = None
        self.SubnetId = None
        self.VpcId = None
        self.Memory = None
        self.Cpu = None
        self.RestartPolicy = None
        self.ImageRegistryCredentials = None
        self.EksCiVolume = None
        self.Replicas = None
        self.InitContainers = None
        self.DnsConfig = None
        self.ExistedEipIds = None
        self.AutoCreateEipAttribute = None
        self.AutoCreateEip = None
        self.CpuType = None
        self.GpuType = None
        self.GpuCount = None
        self.CamRoleName = None


    def _deserialize(self, params):
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        self.EksCiName = params.get("EksCiName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.Memory = params.get("Memory")
        self.Cpu = params.get("Cpu")
        self.RestartPolicy = params.get("RestartPolicy")
        if params.get("ImageRegistryCredentials") is not None:
            self.ImageRegistryCredentials = []
            for item in params.get("ImageRegistryCredentials"):
                obj = ImageRegistryCredential()
                obj._deserialize(item)
                self.ImageRegistryCredentials.append(obj)
        if params.get("EksCiVolume") is not None:
            self.EksCiVolume = EksCiVolume()
            self.EksCiVolume._deserialize(params.get("EksCiVolume"))
        self.Replicas = params.get("Replicas")
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("DnsConfig") is not None:
            self.DnsConfig = DNSConfig()
            self.DnsConfig._deserialize(params.get("DnsConfig"))
        self.ExistedEipIds = params.get("ExistedEipIds")
        if params.get("AutoCreateEipAttribute") is not None:
            self.AutoCreateEipAttribute = EipAttribute()
            self.AutoCreateEipAttribute._deserialize(params.get("AutoCreateEipAttribute"))
        self.AutoCreateEip = params.get("AutoCreateEip")
        self.CpuType = params.get("CpuType")
        self.GpuType = params.get("GpuType")
        self.GpuCount = params.get("GpuCount")
        self.CamRoleName = params.get("CamRoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEKSContainerInstancesResponse(AbstractModel):
    """CreateEKSContainerInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiIds: EKS Container Instance Id集合，格式为eksci-xxx，是容器实例的唯一标识。
        :type EksCiIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EksCiIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EksCiIds = params.get("EksCiIds")
        self.RequestId = params.get("RequestId")


class CreateImageCacheRequest(AbstractModel):
    """CreateImageCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param Images: 用于制作镜像缓存的容器镜像列表
        :type Images: list of str
        :param SubnetId: 实例所属子网Id
        :type SubnetId: str
        :param VpcId: 实例所属VPC Id
        :type VpcId: str
        :param ImageCacheName: 镜像缓存名称
        :type ImageCacheName: str
        :param SecurityGroupIds: 安全组Id
        :type SecurityGroupIds: list of str
        :param ImageRegistryCredentials: 镜像仓库凭证数组
        :type ImageRegistryCredentials: list of ImageRegistryCredential
        :param ExistedEipId: 用来绑定容器实例的已有EIP
        :type ExistedEipId: str
        :param AutoCreateEip: 是否为容器实例自动创建EIP，默认为false。若传true，则此参数和ExistedEipIds互斥
        :type AutoCreateEip: bool
        :param AutoCreateEipAttribute: 自动创建EIP的可选参数。若传此参数，则会自动创建EIP。
另外此参数和ExistedEipIds互斥
        :type AutoCreateEipAttribute: :class:`tencentcloud.tke.v20180525.models.EipAttribute`
        :param ImageCacheSize: 镜像缓存的大小。默认为20 GiB。取值范围参考[云硬盘类型](https://cloud.tencent.com/document/product/362/2353)中的高性能云盘类型的大小限制。
        :type ImageCacheSize: int
        :param RetentionDays: 镜像缓存保留时间天数，过期将会自动清理，默认为0，永不过期。
        :type RetentionDays: int
        """
        self.Images = None
        self.SubnetId = None
        self.VpcId = None
        self.ImageCacheName = None
        self.SecurityGroupIds = None
        self.ImageRegistryCredentials = None
        self.ExistedEipId = None
        self.AutoCreateEip = None
        self.AutoCreateEipAttribute = None
        self.ImageCacheSize = None
        self.RetentionDays = None


    def _deserialize(self, params):
        self.Images = params.get("Images")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.ImageCacheName = params.get("ImageCacheName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("ImageRegistryCredentials") is not None:
            self.ImageRegistryCredentials = []
            for item in params.get("ImageRegistryCredentials"):
                obj = ImageRegistryCredential()
                obj._deserialize(item)
                self.ImageRegistryCredentials.append(obj)
        self.ExistedEipId = params.get("ExistedEipId")
        self.AutoCreateEip = params.get("AutoCreateEip")
        if params.get("AutoCreateEipAttribute") is not None:
            self.AutoCreateEipAttribute = EipAttribute()
            self.AutoCreateEipAttribute._deserialize(params.get("AutoCreateEipAttribute"))
        self.ImageCacheSize = params.get("ImageCacheSize")
        self.RetentionDays = params.get("RetentionDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageCacheResponse(AbstractModel):
    """CreateImageCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param ImageCacheId: 镜像缓存Id
        :type ImageCacheId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ImageCacheId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageCacheId = params.get("ImageCacheId")
        self.RequestId = params.get("RequestId")


class CreatePrometheusAlertPolicyRequest(AbstractModel):
    """CreatePrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param AlertRule: 告警配置
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertPolicyItem`
        """
        self.InstanceId = None
        self.AlertRule = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self.AlertRule = PrometheusAlertPolicyItem()
            self.AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusAlertPolicyResponse(AbstractModel):
    """CreatePrometheusAlertPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 告警id
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreatePrometheusAlertRuleRequest(AbstractModel):
    """CreatePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param AlertRule: 告警配置
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`
        """
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
        r"""
        :param Id: 告警id
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreatePrometheusDashboardRequest(AbstractModel):
    """CreatePrometheusDashboard请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusDashboardResponse(AbstractModel):
    """CreatePrometheusDashboard返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePrometheusGlobalNotificationRequest(AbstractModel):
    """CreatePrometheusGlobalNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Notification: 告警通知渠道
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotificationItem`
        """
        self.InstanceId = None
        self.Notification = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotificationItem()
            self.Notification._deserialize(params.get("Notification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusGlobalNotificationResponse(AbstractModel):
    """CreatePrometheusGlobalNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 全局告警通知渠道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class CreatePrometheusTempRequest(AbstractModel):
    """CreatePrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param Template: 模板设置
        :type Template: :class:`tencentcloud.tke.v20180525.models.PrometheusTemp`
        """
        self.Template = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = PrometheusTemp()
            self.Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusTempResponse(AbstractModel):
    """CreatePrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreatePrometheusTemplateRequest(AbstractModel):
    """CreatePrometheusTemplate请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrometheusTemplateResponse(AbstractModel):
    """CreatePrometheusTemplate返回参数结构体

    """

    def __init__(self):
        r"""
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


class DNSConfig(AbstractModel):
    """自定义DNS配置

    """

    def __init__(self):
        r"""
        :param Nameservers: DNS 服务器IP地址列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Nameservers: list of str
        :param Searches: DNS搜索域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Searches: list of str
        :param Options: 对象选项列表，每个对象由name和value（可选）构成
注意：此字段可能返回 null，表示取不到有效值。
        :type Options: list of DNSConfigOption
        """
        self.Nameservers = None
        self.Searches = None
        self.Options = None


    def _deserialize(self, params):
        self.Nameservers = params.get("Nameservers")
        self.Searches = params.get("Searches")
        if params.get("Options") is not None:
            self.Options = []
            for item in params.get("Options"):
                obj = DNSConfigOption()
                obj._deserialize(item)
                self.Options.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSConfigOption(AbstractModel):
    """DNS配置选项

    """

    def __init__(self):
        r"""
        :param Name: 配置项名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 项值
注意：此字段可能返回 null，表示取不到有效值。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataDisk(AbstractModel):
    """描述了k8s节点数据盘相关配置与信息。

    """

    def __init__(self):
        r"""
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
        :param DiskPartition: 挂载设备名或分区名，当且仅当添加已有节点时需要
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskPartition: str
        """
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterAsGroupsResponse(AbstractModel):
    """DeleteClusterAsGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointRequest(AbstractModel):
    """DeleteClusterEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterEndpointResponse(AbstractModel):
    """DeleteClusterEndpoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClusterEndpointVipRequest(AbstractModel):
    """DeleteClusterEndpointVip请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterEndpointVipResponse(AbstractModel):
    """DeleteClusterEndpointVip返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterInstancesResponse(AbstractModel):
    """DeleteClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
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


class DeleteClusterNodePoolRequest(AbstractModel):
    """DeleteClusterNodePool请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterNodePoolResponse(AbstractModel):
    """DeleteClusterNodePool返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteResponse(AbstractModel):
    """DeleteClusterRoute返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRouteTableResponse(AbstractModel):
    """DeleteClusterRouteTable返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEKSClusterRequest(AbstractModel):
    """DeleteEKSCluster请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEKSClusterResponse(AbstractModel):
    """DeleteEKSCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEKSContainerInstancesRequest(AbstractModel):
    """DeleteEKSContainerInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiIds: 需要删除的EksCi的Id。 最大数量不超过20
        :type EksCiIds: list of str
        :param ReleaseAutoCreatedEip: 是否释放为EksCi自动创建的Eip
        :type ReleaseAutoCreatedEip: bool
        """
        self.EksCiIds = None
        self.ReleaseAutoCreatedEip = None


    def _deserialize(self, params):
        self.EksCiIds = params.get("EksCiIds")
        self.ReleaseAutoCreatedEip = params.get("ReleaseAutoCreatedEip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEKSContainerInstancesResponse(AbstractModel):
    """DeleteEKSContainerInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageCachesRequest(AbstractModel):
    """DeleteImageCaches请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageCacheIds: 镜像缓存Id数组
        :type ImageCacheIds: list of str
        """
        self.ImageCacheIds = None


    def _deserialize(self, params):
        self.ImageCacheIds = params.get("ImageCacheIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageCachesResponse(AbstractModel):
    """DeleteImageCaches返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusAlertPolicyRequest(AbstractModel):
    """DeletePrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param AlertIds: 告警策略id列表
        :type AlertIds: list of str
        :param Names: 告警策略名称
        :type Names: list of str
        """
        self.InstanceId = None
        self.AlertIds = None
        self.Names = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AlertIds = params.get("AlertIds")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusAlertPolicyResponse(AbstractModel):
    """DeletePrometheusAlertPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusAlertRuleRequest(AbstractModel):
    """DeletePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param AlertIds: 告警规则id列表
        :type AlertIds: list of str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTempRequest(AbstractModel):
    """DeletePrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempResponse(AbstractModel):
    """DeletePrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTempSyncRequest(AbstractModel):
    """DeletePrometheusTempSync请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTempSyncResponse(AbstractModel):
    """DeletePrometheusTempSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTemplateRequest(AbstractModel):
    """DeletePrometheusTemplate请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTemplateResponse(AbstractModel):
    """DeletePrometheusTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePrometheusTemplateSyncRequest(AbstractModel):
    """DeletePrometheusTemplateSync请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrometheusTemplateSyncResponse(AbstractModel):
    """DeletePrometheusTemplateSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAvailableClusterVersionRequest(AbstractModel):
    """DescribeAvailableClusterVersion请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAvailableClusterVersionResponse(AbstractModel):
    """DescribeAvailableClusterVersion返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterAsGroupOptionRequest(AbstractModel):
    """DescribeClusterAsGroupOption请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAsGroupOptionResponse(AbstractModel):
    """DescribeClusterAsGroupOption返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterAsGroupsRequest(AbstractModel):
    """DescribeClusterAsGroups请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAsGroupsResponse(AbstractModel):
    """DescribeClusterAsGroups返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterAuthenticationOptionsRequest(AbstractModel):
    """DescribeClusterAuthenticationOptions请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterAuthenticationOptionsResponse(AbstractModel):
    """DescribeClusterAuthenticationOptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceAccounts: ServiceAccount认证配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceAccounts: :class:`tencentcloud.tke.v20180525.models.ServiceAccountAuthenticationOptions`
        :param LatestOperationState: 最近一次修改操作结果，返回值可能为：Updating，Success，Failed，TimeOut
注意：此字段可能返回 null，表示取不到有效值。
        :type LatestOperationState: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceAccounts = None
        self.LatestOperationState = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceAccounts") is not None:
            self.ServiceAccounts = ServiceAccountAuthenticationOptions()
            self.ServiceAccounts._deserialize(params.get("ServiceAccounts"))
        self.LatestOperationState = params.get("LatestOperationState")
        self.RequestId = params.get("RequestId")


class DescribeClusterCommonNamesRequest(AbstractModel):
    """DescribeClusterCommonNames请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterCommonNamesResponse(AbstractModel):
    """DescribeClusterCommonNames返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterControllersRequest(AbstractModel):
    """DescribeClusterControllers请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterControllersResponse(AbstractModel):
    """DescribeClusterControllers返回参数结构体

    """

    def __init__(self):
        r"""
        :param ControllerStatusSet: 描述集群中各个控制器的状态
        :type ControllerStatusSet: list of ControllerStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointStatusResponse(AbstractModel):
    """DescribeClusterEndpointStatus返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterEndpointVipStatusRequest(AbstractModel):
    """DescribeClusterEndpointVipStatus请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterEndpointVipStatusResponse(AbstractModel):
    """DescribeClusterEndpointVipStatus返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param Filters: 过滤条件列表；Name的可选值为nodepool-id、nodepool-instance-type；Name为nodepool-id表示根据节点池id过滤机器，Value的值为具体的节点池id，Name为nodepool-instance-type表示节点加入节点池的方式，Value的值为MANUALLY_ADDED（手动加入节点池）、AUTOSCALING_ADDED（伸缩组扩容方式加入节点池）、ALL（手动加入节点池 和 伸缩组扩容方式加入节点池）
        :type Filters: list of Filter
        """
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
        r"""
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


class DescribeClusterKubeconfigRequest(AbstractModel):
    """DescribeClusterKubeconfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param IsExtranet: 默认false 获取内网，是否获取外网访问的kubeconfig
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterKubeconfigResponse(AbstractModel):
    """DescribeClusterKubeconfig返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterLevelAttributeRequest(AbstractModel):
    """DescribeClusterLevelAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterID: 集群ID，变配时使用
        :type ClusterID: str
        """
        self.ClusterID = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterLevelAttributeResponse(AbstractModel):
    """DescribeClusterLevelAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param Items: 集群规模
        :type Items: list of ClusterLevelAttribute
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ClusterLevelAttribute()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterLevelChangeRecordsRequest(AbstractModel):
    """DescribeClusterLevelChangeRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterID: 集群ID
        :type ClusterID: str
        :param StartAt: 开始时间
        :type StartAt: str
        :param EndAt: 结束时间
        :type EndAt: str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20
        :type Limit: int
        """
        self.ClusterID = None
        self.StartAt = None
        self.EndAt = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.StartAt = params.get("StartAt")
        self.EndAt = params.get("EndAt")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterLevelChangeRecordsResponse(AbstractModel):
    """DescribeClusterLevelChangeRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param Items: 集群规模
        :type Items: list of ClusterLevelChangeRecord
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ClusterLevelChangeRecord()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterNodePoolDetailRequest(AbstractModel):
    """DescribeClusterNodePoolDetail请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterNodePoolDetailResponse(AbstractModel):
    """DescribeClusterNodePoolDetail返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterNodePoolsRequest(AbstractModel):
    """DescribeClusterNodePools请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: ClusterId（集群id）
        :type ClusterId: str
        :param Filters: ·  NodePoolsName
    按照【节点池名】进行过滤。
    类型：String
    必选：否

·  NodePoolsId
    按照【节点池id】进行过滤。
    类型：String
    必选：否

·  tags
    按照【标签键值对】进行过滤。
    类型：String
    必选：否

·  tag:tag-key
    按照【标签键值对】进行过滤。
    类型：String
    必选：否
        :type Filters: list of Filter
        """
        self.ClusterId = None
        self.Filters = None


    def _deserialize(self, params):
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
        


class DescribeClusterNodePoolsResponse(AbstractModel):
    """DescribeClusterNodePools返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterRouteTablesRequest(AbstractModel):
    """DescribeClusterRouteTables请求参数结构体

    """


class DescribeClusterRouteTablesResponse(AbstractModel):
    """DescribeClusterRouteTables返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterRoutesResponse(AbstractModel):
    """DescribeClusterRoutes返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterSecurityResponse(AbstractModel):
    """DescribeClusterSecurity返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeClusterStatusRequest(AbstractModel):
    """DescribeClusterStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterIds: 集群ID列表，不传默认拉取所有集群
        :type ClusterIds: list of str
        """
        self.ClusterIds = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterStatusResponse(AbstractModel):
    """DescribeClusterStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterStatusSet: 集群状态列表
        :type ClusterStatusSet: list of ClusterStatus
        :param TotalCount: 集群个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterStatusSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterStatusSet") is not None:
            self.ClusterStatusSet = []
            for item in params.get("ClusterStatusSet"):
                obj = ClusterStatus()
                obj._deserialize(item)
                self.ClusterStatusSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterIds: 集群ID列表(为空时，
表示获取账号下所有集群)
        :type ClusterIds: list of str
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param Filters: ·  ClusterName
    按照【集群名】进行过滤。
    类型：String
    必选：否

·  ClusterType
    按照【集群类型】进行过滤。
    类型：String
    必选：否

·  ClusterStatus
    按照【集群状态】进行过滤。
    类型：String
    必选：否

·  Tags
    按照【标签键值对】进行过滤。
    类型：String
    必选：否

·  vpc-id
    按照【VPC】进行过滤。
    类型：String
    必选：否

·  tag-key
    按照【标签键】进行过滤。
    类型：String
    必选：否

·  tag-value
    按照【标签值】进行过滤。
    类型：String
    必选：否

·  tag:tag-key
    按照【标签键值对】进行过滤。
    类型：String
    必选：否
        :type Filters: list of Filter
        :param ClusterType: 集群类型，例如：MANAGED_CLUSTER
        :type ClusterType: str
        """
        self.ClusterIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ClusterType = None


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
        self.ClusterType = params.get("ClusterType")
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
        r"""
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


class DescribeEKSClusterCredentialRequest(AbstractModel):
    """DescribeEKSClusterCredential请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEKSClusterCredentialResponse(AbstractModel):
    """DescribeEKSClusterCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param Addresses: 集群的接入地址信息
        :type Addresses: list of IPAddress
        :param Credential: 集群的认证信息
        :type Credential: :class:`tencentcloud.tke.v20180525.models.ClusterCredential`
        :param PublicLB: 集群的公网访问信息
        :type PublicLB: :class:`tencentcloud.tke.v20180525.models.ClusterPublicLB`
        :param InternalLB: 集群的内网访问信息
        :type InternalLB: :class:`tencentcloud.tke.v20180525.models.ClusterInternalLB`
        :param ProxyLB: 标记是否新的内外网功能
        :type ProxyLB: bool
        :param Kubeconfig: 连接用户集群k8s 的Config
        :type Kubeconfig: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Addresses = None
        self.Credential = None
        self.PublicLB = None
        self.InternalLB = None
        self.ProxyLB = None
        self.Kubeconfig = None
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
        self.ProxyLB = params.get("ProxyLB")
        self.Kubeconfig = params.get("Kubeconfig")
        self.RequestId = params.get("RequestId")


class DescribeEKSClustersRequest(AbstractModel):
    """DescribeEKSClusters请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEKSClustersResponse(AbstractModel):
    """DescribeEKSClusters返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeEKSContainerInstanceEventRequest(AbstractModel):
    """DescribeEKSContainerInstanceEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiId: 容器实例id
        :type EksCiId: str
        :param Limit: 最大事件数量。默认为50，最大取值100。
        :type Limit: int
        """
        self.EksCiId = None
        self.Limit = None


    def _deserialize(self, params):
        self.EksCiId = params.get("EksCiId")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEKSContainerInstanceEventResponse(AbstractModel):
    """DescribeEKSContainerInstanceEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Events: 事件集合
        :type Events: list of Event
        :param EksCiId: 容器实例id
        :type EksCiId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Events = None
        self.EksCiId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = Event()
                obj._deserialize(item)
                self.Events.append(obj)
        self.EksCiId = params.get("EksCiId")
        self.RequestId = params.get("RequestId")


class DescribeEKSContainerInstanceRegionsRequest(AbstractModel):
    """DescribeEKSContainerInstanceRegions请求参数结构体

    """


class DescribeEKSContainerInstanceRegionsResponse(AbstractModel):
    """DescribeEKSContainerInstanceRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param Regions: EKS Container Instance支持的地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of EksCiRegionInfo
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Regions = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self.Regions = []
            for item in params.get("Regions"):
                obj = EksCiRegionInfo()
                obj._deserialize(item)
                self.Regions.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEKSContainerInstancesRequest(AbstractModel):
    """DescribeEKSContainerInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过100
        :type Limit: int
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Filters: 过滤条件，可条件：
(1)实例名称
KeyName: eks-ci-name
类型：String

(2)实例状态
KeyName: status
类型：String
可选值："Pending", "Running", "Succeeded", "Failed"

(3)内网ip
KeyName: private-ip
类型：String

(4)EIP地址
KeyName: eip-address
类型：String

(5)VpcId
KeyName: vpc-id
类型：String
        :type Filters: list of Filter
        :param EksCiIds: 容器实例 ID 数组
        :type EksCiIds: list of str
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None
        self.EksCiIds = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.EksCiIds = params.get("EksCiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEKSContainerInstancesResponse(AbstractModel):
    """DescribeEKSContainerInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 容器组总数
        :type TotalCount: int
        :param EksCis: 容器组列表
        :type EksCis: list of EksCi
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EksCis = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EksCis") is not None:
            self.EksCis = []
            for item in params.get("EksCis"):
                obj = EksCi()
                obj._deserialize(item)
                self.EksCis.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEksContainerInstanceLogRequest(AbstractModel):
    """DescribeEksContainerInstanceLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiId: Eks Container Instance Id，即容器实例Id
        :type EksCiId: str
        :param ContainerName: 容器名称，单容器的实例可选填。如果为多容器实例，请指定容器名称。
        :type ContainerName: str
        :param Tail: 返回最新日志行数，默认500，最大2000。日志内容最大返回 1M 数据。
        :type Tail: int
        :param StartTime: UTC时间，RFC3339标准
        :type StartTime: str
        :param Previous: 是否是查上一个容器（如果容器退出重启了）
        :type Previous: bool
        :param SinceSeconds: 查询最近多少秒内的日志
        :type SinceSeconds: int
        :param LimitBytes: 日志总大小限制
        :type LimitBytes: int
        """
        self.EksCiId = None
        self.ContainerName = None
        self.Tail = None
        self.StartTime = None
        self.Previous = None
        self.SinceSeconds = None
        self.LimitBytes = None


    def _deserialize(self, params):
        self.EksCiId = params.get("EksCiId")
        self.ContainerName = params.get("ContainerName")
        self.Tail = params.get("Tail")
        self.StartTime = params.get("StartTime")
        self.Previous = params.get("Previous")
        self.SinceSeconds = params.get("SinceSeconds")
        self.LimitBytes = params.get("LimitBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEksContainerInstanceLogResponse(AbstractModel):
    """DescribeEksContainerInstanceLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerName: 容器名称
        :type ContainerName: str
        :param LogContent: 日志内容
        :type LogContent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerName = None
        self.LogContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ContainerName = params.get("ContainerName")
        self.LogContent = params.get("LogContent")
        self.RequestId = params.get("RequestId")


class DescribeEnableVpcCniProgressRequest(AbstractModel):
    """DescribeEnableVpcCniProgress请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEnableVpcCniProgressResponse(AbstractModel):
    """DescribeEnableVpcCniProgress返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeExistedInstancesRequest(AbstractModel):
    """DescribeExistedInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExistedInstancesResponse(AbstractModel):
    """DescribeExistedInstances返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeExternalClusterSpecRequest(AbstractModel):
    """DescribeExternalClusterSpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 注册集群ID
        :type ClusterId: str
        :param IsExtranet: 默认false 获取内网，是否获取外网版注册命令
        :type IsExtranet: bool
        :param IsRefreshExpirationTime: 默认false 不刷新有效时间 ，true刷新有效时间
        :type IsRefreshExpirationTime: bool
        """
        self.ClusterId = None
        self.IsExtranet = None
        self.IsRefreshExpirationTime = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.IsExtranet = params.get("IsExtranet")
        self.IsRefreshExpirationTime = params.get("IsRefreshExpirationTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExternalClusterSpecResponse(AbstractModel):
    """DescribeExternalClusterSpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param Spec: 导入第三方集群YAML定义
        :type Spec: str
        :param Expiration: agent.yaml文件过期时间字符串，时区UTC
        :type Expiration: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Spec = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Spec = params.get("Spec")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class DescribeImageCachesRequest(AbstractModel):
    """DescribeImageCaches请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageCacheIds: 镜像缓存Id数组
        :type ImageCacheIds: list of str
        :param ImageCacheNames: 镜像缓存名称数组
        :type ImageCacheNames: list of str
        :param Limit: 限定此次返回资源的数量。如果不设定，默认返回20，最大不能超过50
        :type Limit: int
        :param Offset: 偏移量,默认0
        :type Offset: int
        :param Filters: 过滤条件，可选条件：
(1)实例名称
KeyName: image-cache-name
类型：String
        :type Filters: list of Filter
        """
        self.ImageCacheIds = None
        self.ImageCacheNames = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ImageCacheIds = params.get("ImageCacheIds")
        self.ImageCacheNames = params.get("ImageCacheNames")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
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
        


class DescribeImageCachesResponse(AbstractModel):
    """DescribeImageCaches返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 镜像缓存总数
        :type TotalCount: int
        :param ImageCaches: 镜像缓存信息列表
        :type ImageCaches: list of ImageCache
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ImageCaches = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageCaches") is not None:
            self.ImageCaches = []
            for item in params.get("ImageCaches"):
                obj = ImageCache()
                obj._deserialize(item)
                self.ImageCaches.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImagesRequest(AbstractModel):
    """DescribeImages请求参数结构体

    """


class DescribeImagesResponse(AbstractModel):
    """DescribeImages返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusAgentInstancesRequest(AbstractModel):
    """DescribePrometheusAgentInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentInstancesResponse(AbstractModel):
    """DescribePrometheusAgentInstances返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusAgentsRequest(AbstractModel):
    """DescribePrometheusAgents请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAgentsResponse(AbstractModel):
    """DescribePrometheusAgents返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusAlertHistoryRequest(AbstractModel):
    """DescribePrometheusAlertHistory请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertHistoryResponse(AbstractModel):
    """DescribePrometheusAlertHistory返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusAlertPolicyRequest(AbstractModel):
    """DescribePrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertPolicyResponse(AbstractModel):
    """DescribePrometheusAlertPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param AlertRules: 告警详情
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertRules: list of PrometheusAlertPolicyItem
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
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self.AlertRules.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusAlertRuleRequest(AbstractModel):
    """DescribePrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusAlertRuleResponse(AbstractModel):
    """DescribePrometheusAlertRule返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusClusterAgentsRequest(AbstractModel):
    """DescribePrometheusClusterAgents请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusClusterAgentsResponse(AbstractModel):
    """DescribePrometheusClusterAgents返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusGlobalNotificationRequest(AbstractModel):
    """DescribePrometheusGlobalNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusGlobalNotificationResponse(AbstractModel):
    """DescribePrometheusGlobalNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param Notification: 全局告警通知渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotificationItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Notification = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotificationItem()
            self.Notification._deserialize(params.get("Notification"))
        self.RequestId = params.get("RequestId")


class DescribePrometheusInstanceRequest(AbstractModel):
    """DescribePrometheusInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        """
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
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Name: 实例名称
        :type Name: str
        :param VpcId: 私有网络id
        :type VpcId: str
        :param SubnetId: 子网id
        :type SubnetId: str
        :param COSBucket: cos桶名称
        :type COSBucket: str
        :param QueryAddress: 数据查询地址
        :type QueryAddress: str
        :param Grafana: 实例中grafana相关的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Grafana: :class:`tencentcloud.tke.v20180525.models.PrometheusGrafanaInfo`
        :param AlertManagerUrl: 用户自定义alertmanager
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertManagerUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribePrometheusInstancesOverviewRequest(AbstractModel):
    """DescribePrometheusInstancesOverview请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusInstancesOverviewResponse(AbstractModel):
    """DescribePrometheusInstancesOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 实例列表
        :type Instances: list of PrometheusInstancesOverview
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
                obj = PrometheusInstancesOverview()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusOverviewsRequest(AbstractModel):
    """DescribePrometheusOverviews请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusOverviewsResponse(AbstractModel):
    """DescribePrometheusOverviews返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusRecordRulesRequest(AbstractModel):
    """DescribePrometheusRecordRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param Offset: 分页
        :type Offset: int
        :param Limit: 分页
        :type Limit: int
        :param Filters: 过滤
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusRecordRulesResponse(AbstractModel):
    """DescribePrometheusRecordRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Records: 聚合规则
        :type Records: list of PrometheusRecordRuleYamlItem
        :param Total: 总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Records = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Records") is not None:
            self.Records = []
            for item in params.get("Records"):
                obj = PrometheusRecordRuleYamlItem()
                obj._deserialize(item)
                self.Records.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusTargetsRequest(AbstractModel):
    """DescribePrometheusTargets请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTargetsResponse(AbstractModel):
    """DescribePrometheusTargets返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusTempRequest(AbstractModel):
    """DescribePrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTempResponse(AbstractModel):
    """DescribePrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Templates: 模板列表
        :type Templates: list of PrometheusTemp
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
                obj = PrometheusTemp()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribePrometheusTempSyncRequest(AbstractModel):
    """DescribePrometheusTempSync请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTempSyncResponse(AbstractModel):
    """DescribePrometheusTempSync返回参数结构体

    """

    def __init__(self):
        r"""
        :param Targets: 同步目标详情
注意：此字段可能返回 null，表示取不到有效值。
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


class DescribePrometheusTemplateSyncRequest(AbstractModel):
    """DescribePrometheusTemplateSync请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTemplateSyncResponse(AbstractModel):
    """DescribePrometheusTemplateSync返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribePrometheusTemplatesRequest(AbstractModel):
    """DescribePrometheusTemplates请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrometheusTemplatesResponse(AbstractModel):
    """DescribePrometheusTemplates返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeResourceUsageRequest(AbstractModel):
    """DescribeResourceUsage请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceUsageResponse(AbstractModel):
    """DescribeResourceUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param CRDUsage: CRD使用量
        :type CRDUsage: :class:`tencentcloud.tke.v20180525.models.ResourceUsage`
        :param PodUsage: Pod使用量
        :type PodUsage: int
        :param ConfigMapUsage: ConfigMap使用量
        :type ConfigMapUsage: int
        :param OtherUsage: 其他资源使用量
        :type OtherUsage: :class:`tencentcloud.tke.v20180525.models.ResourceUsage`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CRDUsage = None
        self.PodUsage = None
        self.ConfigMapUsage = None
        self.OtherUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CRDUsage") is not None:
            self.CRDUsage = ResourceUsage()
            self.CRDUsage._deserialize(params.get("CRDUsage"))
        self.PodUsage = params.get("PodUsage")
        self.ConfigMapUsage = params.get("ConfigMapUsage")
        if params.get("OtherUsage") is not None:
            self.OtherUsage = ResourceUsage()
            self.OtherUsage._deserialize(params.get("OtherUsage"))
        self.RequestId = params.get("RequestId")


class DescribeRouteTableConflictsRequest(AbstractModel):
    """DescribeRouteTableConflicts请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTableConflictsResponse(AbstractModel):
    """DescribeRouteTableConflicts返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeTKEEdgeScriptRequest(AbstractModel):
    """DescribeTKEEdgeScript请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Interface: 网卡名
        :type Interface: str
        :param NodeName: 节点名字
        :type NodeName: str
        :param Config: json格式的节点配置
        :type Config: str
        """
        self.ClusterId = None
        self.Interface = None
        self.NodeName = None
        self.Config = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Interface = params.get("Interface")
        self.NodeName = params.get("NodeName")
        self.Config = params.get("Config")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTKEEdgeScriptResponse(AbstractModel):
    """DescribeTKEEdgeScript返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeVersionsRequest(AbstractModel):
    """DescribeVersions请求参数结构体

    """


class DescribeVersionsResponse(AbstractModel):
    """DescribeVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 版本数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param VersionInstanceSet: 版本列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionInstanceSet: list of VersionInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Zone: 查询的机型所在可用区，如：ap-guangzhou-3，默认为空，即不按可用区过滤信息
        :type Zone: str
        :param InstanceFamily: 查询的实例机型系列信息，如：S5，默认为空，即不按机型系列过滤信息
        :type InstanceFamily: str
        :param InstanceType: 查询的实例机型信息，如：S5.LARGE8，默认为空，即不按机型过滤信息
        :type InstanceType: str
        """
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
        r"""
        :param TotalCount: 机型数据数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param PodLimitsInstanceSet: 机型信息及其可支持的最大VPC-CNI模式Pod数量信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodLimitsInstanceSet: list of PodLimitsInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DisableClusterAuditRequest(AbstractModel):
    """DisableClusterAudit请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableClusterAuditResponse(AbstractModel):
    """DisableClusterAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableClusterDeletionProtectionRequest(AbstractModel):
    """DisableClusterDeletionProtection请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableClusterDeletionProtectionResponse(AbstractModel):
    """DisableClusterDeletionProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableEventPersistenceRequest(AbstractModel):
    """DisableEventPersistence请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableEventPersistenceResponse(AbstractModel):
    """DisableEventPersistence返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableVpcCniNetworkTypeRequest(AbstractModel):
    """DisableVpcCniNetworkType请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableVpcCniNetworkTypeResponse(AbstractModel):
    """DisableVpcCniNetworkType返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DnsServerConf(AbstractModel):
    """Eks 自定义域名服务器 配置

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAttribute(AbstractModel):
    """用以帮助用户自动创建EIP的配置

    """

    def __init__(self):
        r"""
        :param DeletePolicy: 容器实例删除后，EIP是否释放。
Never表示不释放，其他任意值（包括空字符串）表示释放。
        :type DeletePolicy: str
        :param InternetServiceProvider: EIP线路类型。默认值：BGP。
已开通静态单线IP白名单的用户，可选值：
CMCC：中国移动
CTCC：中国电信
CUCC：中国联通
注意：仅部分地域支持静态单线IP。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetServiceProvider: str
        :param InternetMaxBandwidthOut: EIP出带宽上限，单位：Mbps。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        """
        self.DeletePolicy = None
        self.InternetServiceProvider = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.DeletePolicy = params.get("DeletePolicy")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EksCi(AbstractModel):
    """EksContainerInstance实例类型

    """

    def __init__(self):
        r"""
        :param EksCiId: EKS Cotainer Instance Id
        :type EksCiId: str
        :param EksCiName: EKS Cotainer Instance Name
        :type EksCiName: str
        :param Memory: 内存大小
        :type Memory: float
        :param Cpu: CPU大小
        :type Cpu: float
        :param SecurityGroupIds: 安全组ID
        :type SecurityGroupIds: list of str
        :param RestartPolicy: 容器组的重启策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartPolicy: str
        :param Status: 返回容器组创建状态：Pending，Running，Succeeded，Failed。其中：
Failed （运行失败）指的容器组退出，RestartPolilcy为Never， 有容器exitCode非0；
Succeeded（运行成功）指的是容器组退出了，RestartPolicy为Never或onFailure，所有容器exitCode都为0；
Failed和Succeeded这两种状态都会停止运行，停止计费。
Pending是创建中，Running是 运行中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreationTime: 接到请求后的系统创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreationTime: str
        :param SucceededTime: 容器全部成功退出后的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SucceededTime: str
        :param Containers: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: list of Container
        :param EksCiVolume: 数据卷信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EksCiVolume: :class:`tencentcloud.tke.v20180525.models.EksCiVolume`
        :param SecurityContext: 容器组运行的安全上下文
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityContext: :class:`tencentcloud.tke.v20180525.models.SecurityContext`
        :param PrivateIp: 内网ip地址
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateIp: str
        :param EipAddress: 容器实例绑定的Eip地址，注意可能为空
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddress: str
        :param GpuType: GPU类型。如无使用GPU则不返回
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param CpuType: CPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuType: str
        :param GpuCount: GPU卡数量
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuCount: int
        :param VpcId: 实例所属VPC的Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 实例所属子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param InitContainers: 初始化容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InitContainers: list of Container
        :param CamRoleName: 为容器实例关联 CAM 角色，value 填写 CAM 角色名称，容器实例可获取该 CAM 角色包含的权限策略，方便 容器实例 内的程序进行如购买资源、读写存储等云资源操作。
注意：此字段可能返回 null，表示取不到有效值。
        :type CamRoleName: str
        :param AutoCreatedEipId: 自动为用户创建的EipId
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoCreatedEipId: str
        :param PersistStatus: 容器状态是否持久化
注意：此字段可能返回 null，表示取不到有效值。
        :type PersistStatus: bool
        """
        self.EksCiId = None
        self.EksCiName = None
        self.Memory = None
        self.Cpu = None
        self.SecurityGroupIds = None
        self.RestartPolicy = None
        self.Status = None
        self.CreationTime = None
        self.SucceededTime = None
        self.Containers = None
        self.EksCiVolume = None
        self.SecurityContext = None
        self.PrivateIp = None
        self.EipAddress = None
        self.GpuType = None
        self.CpuType = None
        self.GpuCount = None
        self.VpcId = None
        self.SubnetId = None
        self.InitContainers = None
        self.CamRoleName = None
        self.AutoCreatedEipId = None
        self.PersistStatus = None


    def _deserialize(self, params):
        self.EksCiId = params.get("EksCiId")
        self.EksCiName = params.get("EksCiName")
        self.Memory = params.get("Memory")
        self.Cpu = params.get("Cpu")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.RestartPolicy = params.get("RestartPolicy")
        self.Status = params.get("Status")
        self.CreationTime = params.get("CreationTime")
        self.SucceededTime = params.get("SucceededTime")
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        if params.get("EksCiVolume") is not None:
            self.EksCiVolume = EksCiVolume()
            self.EksCiVolume._deserialize(params.get("EksCiVolume"))
        if params.get("SecurityContext") is not None:
            self.SecurityContext = SecurityContext()
            self.SecurityContext._deserialize(params.get("SecurityContext"))
        self.PrivateIp = params.get("PrivateIp")
        self.EipAddress = params.get("EipAddress")
        self.GpuType = params.get("GpuType")
        self.CpuType = params.get("CpuType")
        self.GpuCount = params.get("GpuCount")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        self.CamRoleName = params.get("CamRoleName")
        self.AutoCreatedEipId = params.get("AutoCreatedEipId")
        self.PersistStatus = params.get("PersistStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EksCiRegionInfo(AbstractModel):
    """EksCi地域信息

    """

    def __init__(self):
        r"""
        :param Alias: 地域别名，形如gz
        :type Alias: str
        :param RegionName: 地域名，形如ap-guangzhou
        :type RegionName: str
        :param RegionId: 地域ID
        :type RegionId: int
        """
        self.Alias = None
        self.RegionName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EksCiVolume(AbstractModel):
    """EKS Instance Volume,  可选包括CbsVolume和NfsVolume

    """

    def __init__(self):
        r"""
        :param CbsVolumes: Cbs Volume
注意：此字段可能返回 null，表示取不到有效值。
        :type CbsVolumes: list of CbsVolume
        :param NfsVolumes: Nfs Volume
注意：此字段可能返回 null，表示取不到有效值。
        :type NfsVolumes: list of NfsVolume
        """
        self.CbsVolumes = None
        self.NfsVolumes = None


    def _deserialize(self, params):
        if params.get("CbsVolumes") is not None:
            self.CbsVolumes = []
            for item in params.get("CbsVolumes"):
                obj = CbsVolume()
                obj._deserialize(item)
                self.CbsVolumes.append(obj)
        if params.get("NfsVolumes") is not None:
            self.NfsVolumes = []
            for item in params.get("NfsVolumes"):
                obj = NfsVolume()
                obj._deserialize(item)
                self.NfsVolumes.append(obj)
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClusterAuditRequest(AbstractModel):
    """EnableClusterAudit请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param LogsetId: CLS日志集ID
        :type LogsetId: str
        :param TopicId: CLS日志主题ID
        :type TopicId: str
        """
        self.ClusterId = None
        self.LogsetId = None
        self.TopicId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClusterAuditResponse(AbstractModel):
    """EnableClusterAudit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableClusterDeletionProtectionRequest(AbstractModel):
    """EnableClusterDeletionProtection请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClusterDeletionProtectionResponse(AbstractModel):
    """EnableClusterDeletionProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableEventPersistenceRequest(AbstractModel):
    """EnableEventPersistence请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param LogsetId: cls服务的logsetID
        :type LogsetId: str
        :param TopicId: cls服务的topicID
        :type TopicId: str
        """
        self.ClusterId = None
        self.LogsetId = None
        self.TopicId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableEventPersistenceResponse(AbstractModel):
    """EnableEventPersistence返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableVpcCniNetworkTypeRequest(AbstractModel):
    """EnableVpcCniNetworkType请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcCniNetworkTypeResponse(AbstractModel):
    """EnableVpcCniNetworkType返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        r"""
        :param SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.tke.v20180525.models.RunSecurityServiceEnabled`
        :param MonitorService: 开启云监控服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.tke.v20180525.models.RunMonitorServiceEnabled`
        :param AutomationService: 开启云自动化助手服务。若不指定该参数，则默认不开启云自动化助手服务。
        :type AutomationService: :class:`tencentcloud.tke.v20180525.models.RunAutomationServiceEnabled`
        """
        self.SecurityService = None
        self.MonitorService = None
        self.AutomationService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        if params.get("AutomationService") is not None:
            self.AutomationService = RunAutomationServiceEnabled()
            self.AutomationService._deserialize(params.get("AutomationService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentVariable(AbstractModel):
    """EnvironmentVariable

    """

    def __init__(self):
        r"""
        :param Name: key
        :type Name: str
        :param Value: val
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """服务事件

    """

    def __init__(self):
        r"""
        :param PodName: pod名称
        :type PodName: str
        :param Reason: 事件原因内容
        :type Reason: str
        :param Type: 事件类型
        :type Type: str
        :param Count: 事件出现次数
        :type Count: int
        :param FirstTimestamp: 事件第一次出现时间
        :type FirstTimestamp: str
        :param LastTimestamp: 事件最后一次出现时间
        :type LastTimestamp: str
        :param Message: 事件内容
        :type Message: str
        """
        self.PodName = None
        self.Reason = None
        self.Type = None
        self.Count = None
        self.FirstTimestamp = None
        self.LastTimestamp = None
        self.Message = None


    def _deserialize(self, params):
        self.PodName = params.get("PodName")
        self.Reason = params.get("Reason")
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        self.FirstTimestamp = params.get("FirstTimestamp")
        self.LastTimestamp = params.get("LastTimestamp")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Exec(AbstractModel):
    """探针在容器内执行检测命令参数类型

    """

    def __init__(self):
        r"""
        :param Commands: 容器内检测的命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Commands: list of str
        """
        self.Commands = None


    def _deserialize(self, params):
        self.Commands = params.get("Commands")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesForNode(AbstractModel):
    """不同角色的已存在节点配置参数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExistedInstancesPara(AbstractModel):
    """已存在实例的重装参数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtensionAddon(AbstractModel):
    """创建集群时，选择安装的扩展组件的信息

    """

    def __init__(self):
        r"""
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
        


class ForwardApplicationRequestV3Request(AbstractModel):
    """ForwardApplicationRequestV3请求参数结构体

    """

    def __init__(self):
        r"""
        :param Method: 请求集群addon的访问
        :type Method: str
        :param Path: 请求集群addon的路径
        :type Path: str
        :param Accept: 请求集群addon后允许接收的数据格式
        :type Accept: str
        :param ContentType: 请求集群addon的数据格式
        :type ContentType: str
        :param RequestBody: 请求集群addon的数据
        :type RequestBody: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param EncodedBody: 是否编码请求内容
        :type EncodedBody: str
        """
        self.Method = None
        self.Path = None
        self.Accept = None
        self.ContentType = None
        self.RequestBody = None
        self.ClusterName = None
        self.EncodedBody = None


    def _deserialize(self, params):
        self.Method = params.get("Method")
        self.Path = params.get("Path")
        self.Accept = params.get("Accept")
        self.ContentType = params.get("ContentType")
        self.RequestBody = params.get("RequestBody")
        self.ClusterName = params.get("ClusterName")
        self.EncodedBody = params.get("EncodedBody")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardApplicationRequestV3Response(AbstractModel):
    """ForwardApplicationRequestV3返回参数结构体

    """

    def __init__(self):
        r"""
        :param ResponseBody: 请求集群addon后返回的数据
        :type ResponseBody: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ResponseBody = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ResponseBody = params.get("ResponseBody")
        self.RequestId = params.get("RequestId")


class GetClusterLevelPriceRequest(AbstractModel):
    """GetClusterLevelPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterLevel: 集群规格，托管集群询价
        :type ClusterLevel: str
        """
        self.ClusterLevel = None


    def _deserialize(self, params):
        self.ClusterLevel = params.get("ClusterLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetClusterLevelPriceResponse(AbstractModel):
    """GetClusterLevelPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param Cost: 询价结果，单位：分，打折后
        :type Cost: int
        :param TotalCost: 询价结果，单位：分，折扣前
        :type TotalCost: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Cost = None
        self.TotalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Cost = params.get("Cost")
        self.TotalCost = params.get("TotalCost")
        self.RequestId = params.get("RequestId")


class GetMostSuitableImageCacheRequest(AbstractModel):
    """GetMostSuitableImageCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param Images: 容器镜像列表
        :type Images: list of str
        """
        self.Images = None


    def _deserialize(self, params):
        self.Images = params.get("Images")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMostSuitableImageCacheResponse(AbstractModel):
    """GetMostSuitableImageCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param Found: 是否有匹配的镜像缓存
        :type Found: bool
        :param ImageCache: 匹配的镜像缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageCache: :class:`tencentcloud.tke.v20180525.models.ImageCache`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Found = None
        self.ImageCache = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Found = params.get("Found")
        if params.get("ImageCache") is not None:
            self.ImageCache = ImageCache()
            self.ImageCache._deserialize(params.get("ImageCache"))
        self.RequestId = params.get("RequestId")


class GetTkeAppChartListRequest(AbstractModel):
    """GetTkeAppChartList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Kind: app类型，取值log,scheduler,network,storage,monitor,dns,image,other,invisible
        :type Kind: str
        :param Arch: app支持的操作系统，取值arm32、arm64、amd64
        :type Arch: str
        :param ClusterType: 集群类型，取值tke、eks
        :type ClusterType: str
        """
        self.Kind = None
        self.Arch = None
        self.ClusterType = None


    def _deserialize(self, params):
        self.Kind = params.get("Kind")
        self.Arch = params.get("Arch")
        self.ClusterType = params.get("ClusterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTkeAppChartListResponse(AbstractModel):
    """GetTkeAppChartList返回参数结构体

    """

    def __init__(self):
        r"""
        :param AppCharts: 所支持的chart列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AppCharts: list of AppChart
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppCharts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AppCharts") is not None:
            self.AppCharts = []
            for item in params.get("AppCharts"):
                obj = AppChart()
                obj._deserialize(item)
                self.AppCharts.append(obj)
        self.RequestId = params.get("RequestId")


class GetUpgradeInstanceProgressRequest(AbstractModel):
    """GetUpgradeInstanceProgress请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUpgradeInstanceProgressResponse(AbstractModel):
    """GetUpgradeInstanceProgress返回参数结构体

    """

    def __init__(self):
        r"""
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


class HttpGet(AbstractModel):
    """Probe中的HttpGet

    """

    def __init__(self):
        r"""
        :param Path: HttpGet检测的路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Port: HttpGet检测的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Scheme: HTTP or HTTPS
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: str
        """
        self.Path = None
        self.Port = None
        self.Scheme = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Port = params.get("Port")
        self.Scheme = params.get("Scheme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPAddress(AbstractModel):
    """IP 地址

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageCache(AbstractModel):
    """镜像缓存的信息

    """

    def __init__(self):
        r"""
        :param ImageCacheId: 镜像缓存Id
        :type ImageCacheId: str
        :param ImageCacheName: 镜像缓存名称
        :type ImageCacheName: str
        :param ImageCacheSize: 镜像缓存大小。单位：GiB
        :type ImageCacheSize: int
        :param Images: 镜像缓存包含的镜像列表
        :type Images: list of str
        :param CreationTime: 创建时间
        :type CreationTime: str
        :param ExpireDateTime: 到期时间
        :type ExpireDateTime: str
        :param Events: 镜像缓存事件信息
        :type Events: list of ImageCacheEvent
        :param LastMatchedTime: 最新一次匹配到镜像缓存的时间
        :type LastMatchedTime: str
        :param SnapshotId: 镜像缓存对应的快照Id
        :type SnapshotId: str
        :param Status: 镜像缓存状态，可能取值：
Pending：创建中
Ready：创建完成
Failed：创建失败
Updating：更新中
UpdateFailed：更新失败
只有状态为Ready时，才能正常使用镜像缓存
        :type Status: str
        """
        self.ImageCacheId = None
        self.ImageCacheName = None
        self.ImageCacheSize = None
        self.Images = None
        self.CreationTime = None
        self.ExpireDateTime = None
        self.Events = None
        self.LastMatchedTime = None
        self.SnapshotId = None
        self.Status = None


    def _deserialize(self, params):
        self.ImageCacheId = params.get("ImageCacheId")
        self.ImageCacheName = params.get("ImageCacheName")
        self.ImageCacheSize = params.get("ImageCacheSize")
        self.Images = params.get("Images")
        self.CreationTime = params.get("CreationTime")
        self.ExpireDateTime = params.get("ExpireDateTime")
        if params.get("Events") is not None:
            self.Events = []
            for item in params.get("Events"):
                obj = ImageCacheEvent()
                obj._deserialize(item)
                self.Events.append(obj)
        self.LastMatchedTime = params.get("LastMatchedTime")
        self.SnapshotId = params.get("SnapshotId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageCacheEvent(AbstractModel):
    """镜像缓存的事件

    """

    def __init__(self):
        r"""
        :param ImageCacheId: 镜像缓存Id
        :type ImageCacheId: str
        :param Type: 事件类型, Normal或者Warning
        :type Type: str
        :param Reason: 事件原因简述
        :type Reason: str
        :param Message: 事件原因详述
        :type Message: str
        :param FirstTimestamp: 事件第一次出现时间
        :type FirstTimestamp: str
        :param LastTimestamp: 事件最后一次出现时间
        :type LastTimestamp: str
        """
        self.ImageCacheId = None
        self.Type = None
        self.Reason = None
        self.Message = None
        self.FirstTimestamp = None
        self.LastTimestamp = None


    def _deserialize(self, params):
        self.ImageCacheId = params.get("ImageCacheId")
        self.Type = params.get("Type")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        self.FirstTimestamp = params.get("FirstTimestamp")
        self.LastTimestamp = params.get("LastTimestamp")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageRegistryCredential(AbstractModel):
    """从镜像仓库拉取镜像的凭据

    """

    def __init__(self):
        r"""
        :param Server: 镜像仓库地址
        :type Server: str
        :param Username: 用户名
        :type Username: str
        :param Password: 密码
        :type Password: str
        :param Name: ImageRegistryCredential的名字
        :type Name: str
        """
        self.Server = None
        self.Username = None
        self.Password = None
        self.Name = None


    def _deserialize(self, params):
        self.Server = params.get("Server")
        self.Username = params.get("Username")
        self.Password = params.get("Password")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallLogAgentRequest(AbstractModel):
    """InstallLogAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: TKE集群ID
        :type ClusterId: str
        :param KubeletRootDir: kubelet根目录
        :type KubeletRootDir: str
        """
        self.ClusterId = None
        self.KubeletRootDir = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.KubeletRootDir = params.get("KubeletRootDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstallLogAgentResponse(AbstractModel):
    """InstallLogAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """集群的实例信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相关配置与信息。

    """

    def __init__(self):
        r"""
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
        :param DataDisks: 多盘数据盘挂载信息：新建节点时请确保购买CVM的参数传递了购买多个数据盘的信息，如CreateClusterInstances API的RunInstancesPara下的DataDisks也需要设置购买多个数据盘, 具体可以参考CreateClusterInstances接口的添加集群节点(多块数据盘)样例；添加已有节点时，请确保填写的分区信息在节点上真实存在
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        :param ExtraArgs: 节点相关的自定义参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        :param DesiredPodNumber: 该节点属于podCIDR大小自定义模式时，可指定节点上运行的pod数量上限
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredPodNumber: int
        :param PreStartUserScript: base64 编码的用户脚本，在初始化节点之前执行，目前只对添加已有节点生效
注意：此字段可能返回 null，表示取不到有效值。
        :type PreStartUserScript: str
        """
        self.MountTarget = None
        self.DockerGraphPath = None
        self.UserScript = None
        self.Unschedulable = None
        self.Labels = None
        self.DataDisks = None
        self.ExtraArgs = None
        self.DesiredPodNumber = None
        self.PreStartUserScript = None


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
        self.PreStartUserScript = params.get("PreStartUserScript")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtraArgs(AbstractModel):
    """节点自定义参数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeClusterStatus(AbstractModel):
    """节点升级过程中集群当前状态

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResult(AbstractModel):
    """某个节点升级前检查结果

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradePreCheckResultItem(AbstractModel):
    """节点升级检查项结果

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceUpgradeProgressItem(AbstractModel):
    """某个节点的升级进度

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s中标签，一般以数组的方式存在

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LivenessOrReadinessProbe(AbstractModel):
    """健康探针

    """

    def __init__(self):
        r"""
        :param Probe: 探针参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Probe: :class:`tencentcloud.tke.v20180525.models.Probe`
        :param HttpGet: HttpGet检测参数
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpGet: :class:`tencentcloud.tke.v20180525.models.HttpGet`
        :param Exec: 容器内检测命令参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Exec: :class:`tencentcloud.tke.v20180525.models.Exec`
        :param TcpSocket: TcpSocket检测的端口参数
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpSocket: :class:`tencentcloud.tke.v20180525.models.TcpSocket`
        """
        self.Probe = None
        self.HttpGet = None
        self.Exec = None
        self.TcpSocket = None


    def _deserialize(self, params):
        if params.get("Probe") is not None:
            self.Probe = Probe()
            self.Probe._deserialize(params.get("Probe"))
        if params.get("HttpGet") is not None:
            self.HttpGet = HttpGet()
            self.HttpGet._deserialize(params.get("HttpGet"))
        if params.get("Exec") is not None:
            self.Exec = Exec()
            self.Exec._deserialize(params.get("Exec"))
        if params.get("TcpSocket") is not None:
            self.TcpSocket = TcpSocket()
            self.TcpSocket._deserialize(params.get("TcpSocket"))
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManuallyAdded(AbstractModel):
    """手动加入的节点

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAsGroupOptionAttributeRequest(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAsGroupOptionAttributeResponse(AbstractModel):
    """ModifyClusterAsGroupOptionAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterAttributeRequest(AbstractModel):
    """ModifyClusterAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ProjectId: 集群所属项目
        :type ProjectId: int
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param ClusterDesc: 集群描述
        :type ClusterDesc: str
        :param ClusterLevel: 集群等级
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: 自动变配集群等级
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        """
        self.ClusterId = None
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self.AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self.AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
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
        r"""
        :param ProjectId: 集群所属项目
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: int
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param ClusterDesc: 集群描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param ClusterLevel: 集群等级
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterLevel: str
        :param AutoUpgradeClusterLevel: 自动变配集群等级
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoUpgradeClusterLevel: :class:`tencentcloud.tke.v20180525.models.AutoUpgradeClusterLevel`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.ClusterName = None
        self.ClusterDesc = None
        self.ClusterLevel = None
        self.AutoUpgradeClusterLevel = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ClusterName = params.get("ClusterName")
        self.ClusterDesc = params.get("ClusterDesc")
        self.ClusterLevel = params.get("ClusterLevel")
        if params.get("AutoUpgradeClusterLevel") is not None:
            self.AutoUpgradeClusterLevel = AutoUpgradeClusterLevel()
            self.AutoUpgradeClusterLevel._deserialize(params.get("AutoUpgradeClusterLevel"))
        self.RequestId = params.get("RequestId")


class ModifyClusterAuthenticationOptionsRequest(AbstractModel):
    """ModifyClusterAuthenticationOptions请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ServiceAccounts: ServiceAccount认证配置
        :type ServiceAccounts: :class:`tencentcloud.tke.v20180525.models.ServiceAccountAuthenticationOptions`
        """
        self.ClusterId = None
        self.ServiceAccounts = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ServiceAccounts") is not None:
            self.ServiceAccounts = ServiceAccountAuthenticationOptions()
            self.ServiceAccounts._deserialize(params.get("ServiceAccounts"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterAuthenticationOptionsResponse(AbstractModel):
    """ModifyClusterAuthenticationOptions返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterEndpointSPRequest(AbstractModel):
    """ModifyClusterEndpointSP请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterEndpointSPResponse(AbstractModel):
    """ModifyClusterEndpointSP返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterNodePoolRequest(AbstractModel):
    """ModifyClusterNodePool请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param ExtraArgs: 节点自定义参数
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.InstanceExtraArgs`
        :param Tags: 资源标签
        :type Tags: list of Tag
        :param Unschedulable: 设置加入的节点是否参与调度，默认值为0，表示参与调度；非0表示不参与调度, 待节点初始化完成之后, 可执行kubectl uncordon nodename使node加入调度.
        :type Unschedulable: int
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
        self.ExtraArgs = None
        self.Tags = None
        self.Unschedulable = None


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
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = InstanceExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Unschedulable = params.get("Unschedulable")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNodePoolDesiredCapacityAboutAsgRequest(AbstractModel):
    """ModifyNodePoolDesiredCapacityAboutAsg请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolDesiredCapacityAboutAsgResponse(AbstractModel):
    """ModifyNodePoolDesiredCapacityAboutAsg返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNodePoolInstanceTypesRequest(AbstractModel):
    """ModifyNodePoolInstanceTypes请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param InstanceTypes: 机型列表
        :type InstanceTypes: list of str
        """
        self.ClusterId = None
        self.NodePoolId = None
        self.InstanceTypes = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodePoolId = params.get("NodePoolId")
        self.InstanceTypes = params.get("InstanceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolInstanceTypesResponse(AbstractModel):
    """ModifyNodePoolInstanceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusAlertPolicyRequest(AbstractModel):
    """ModifyPrometheusAlertPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param AlertRule: 告警配置
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertPolicyItem`
        """
        self.InstanceId = None
        self.AlertRule = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AlertRule") is not None:
            self.AlertRule = PrometheusAlertPolicyItem()
            self.AlertRule._deserialize(params.get("AlertRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusAlertPolicyResponse(AbstractModel):
    """ModifyPrometheusAlertPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusAlertRuleRequest(AbstractModel):
    """ModifyPrometheusAlertRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param AlertRule: 告警配置
        :type AlertRule: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertRuleDetail`
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusGlobalNotificationRequest(AbstractModel):
    """ModifyPrometheusGlobalNotification请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Notification: 告警通知渠道
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotificationItem`
        """
        self.InstanceId = None
        self.Notification = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotificationItem()
            self.Notification._deserialize(params.get("Notification"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusGlobalNotificationResponse(AbstractModel):
    """ModifyPrometheusGlobalNotification返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusTempRequest(AbstractModel):
    """ModifyPrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param Template: 修改内容
        :type Template: :class:`tencentcloud.tke.v20180525.models.PrometheusTempModify`
        """
        self.TemplateId = None
        self.Template = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("Template") is not None:
            self.Template = PrometheusTempModify()
            self.Template._deserialize(params.get("Template"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusTempResponse(AbstractModel):
    """ModifyPrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrometheusTemplateRequest(AbstractModel):
    """ModifyPrometheusTemplate请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrometheusTemplateResponse(AbstractModel):
    """ModifyPrometheusTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NfsVolume(AbstractModel):
    """EKS Instance Nfs Volume

    """

    def __init__(self):
        r"""
        :param Name: nfs volume 数据卷名称
        :type Name: str
        :param Server: NFS 服务器地址
        :type Server: str
        :param Path: NFS 数据卷路径
        :type Path: str
        :param ReadOnly: 默认为 False
        :type ReadOnly: bool
        """
        self.Name = None
        self.Server = None
        self.Path = None
        self.ReadOnly = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Server = params.get("Server")
        self.Path = params.get("Path")
        self.ReadOnly = params.get("ReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeCountSummary(AbstractModel):
    """节点统计列表

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePool(AbstractModel):
    """节点池描述

    """

    def __init__(self):
        r"""
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
        :param Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
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
        self.Tags = None


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
        


class NodePoolOption(AbstractModel):
    """加入存量节点时的节点池选项

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodLimitsByType(AbstractModel):
    """某机型可支持的最大 VPC-CNI 模式的 Pod 数量

    """

    def __init__(self):
        r"""
        :param TKERouteENINonStaticIP: TKE共享网卡非固定IP模式可支持的Pod数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TKERouteENINonStaticIP: int
        :param TKERouteENIStaticIP: TKE共享网卡固定IP模式可支持的Pod数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TKERouteENIStaticIP: int
        :param TKEDirectENI: TKE独立网卡模式可支持的Pod数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TKEDirectENI: int
        """
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
        r"""
        :param Zone: 机型所在可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param InstanceFamily: 机型所属机型族
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceFamily: str
        :param InstanceType: 实例机型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param PodLimits: 机型可支持的最大VPC-CNI模式Pod数量信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PodLimits: :class:`tencentcloud.tke.v20180525.models.PodLimitsByType`
        """
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
        


class Probe(AbstractModel):
    """健康检查探测参数

    """

    def __init__(self):
        r"""
        :param InitialDelaySeconds: Number of seconds after the container has started before liveness probes are initiated.
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param TimeoutSeconds: Number of seconds after which the probe times out.
Defaults to 1 second. Minimum value is 1.
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutSeconds: int
        :param PeriodSeconds: How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodSeconds: int
        :param SuccessThreshold: Minimum consecutive successes for the probe to be considered successful after having failed.Defaults to 1. Must be 1 for liveness. Minimum value is 1.
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessThreshold: int
        :param FailureThreshold: Minimum consecutive failures for the probe to be considered failed after having succeeded.Defaults to 3. Minimum value is 1.
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureThreshold: int
        """
        self.InitialDelaySeconds = None
        self.TimeoutSeconds = None
        self.PeriodSeconds = None
        self.SuccessThreshold = None
        self.FailureThreshold = None


    def _deserialize(self, params):
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.TimeoutSeconds = params.get("TimeoutSeconds")
        self.PeriodSeconds = params.get("PeriodSeconds")
        self.SuccessThreshold = params.get("SuccessThreshold")
        self.FailureThreshold = params.get("FailureThreshold")
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
        r"""
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
        :param ExternalLabels: 额外labels
本集群的所有指标都会带上这几个label
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalLabels: list of Label
        """
        self.ClusterType = None
        self.ClusterId = None
        self.Status = None
        self.ClusterName = None
        self.ExternalLabels = None


    def _deserialize(self, params):
        self.ClusterType = params.get("ClusterType")
        self.ClusterId = params.get("ClusterId")
        self.Status = params.get("Status")
        self.ClusterName = params.get("ClusterName")
        if params.get("ExternalLabels") is not None:
            self.ExternalLabels = []
            for item in params.get("ExternalLabels"):
                obj = Label()
                obj._deserialize(item)
                self.ExternalLabels.append(obj)
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertManagerConfig(AbstractModel):
    """告警渠道使用自建alertmanager的配置

    """

    def __init__(self):
        r"""
        :param Url: alertmanager url
        :type Url: str
        :param ClusterType: alertmanager部署所在集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterType: str
        :param ClusterId: alertmanager部署所在集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self.Url = None
        self.ClusterType = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.ClusterType = params.get("ClusterType")
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusAlertPolicyItem(AbstractModel):
    """托管prometheus告警策略实例

    """

    def __init__(self):
        r"""
        :param Name: 策略名称
        :type Name: str
        :param Rules: 规则列表
        :type Rules: list of PrometheusAlertRule
        :param Id: 告警策略 id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param TemplateId: 如果该告警来自模板下发，则TemplateId为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param Notification: 告警渠道，模板中使用可能返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type Notification: :class:`tencentcloud.tke.v20180525.models.PrometheusNotificationItem`
        :param UpdatedAt: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param ClusterId: 如果告警策略来源于用户集群CRD资源定义，则ClusterId为所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self.Name = None
        self.Rules = None
        self.Id = None
        self.TemplateId = None
        self.Notification = None
        self.UpdatedAt = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = PrometheusAlertRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Id = params.get("Id")
        self.TemplateId = params.get("TemplateId")
        if params.get("Notification") is not None:
            self.Notification = PrometheusNotificationItem()
            self.Notification._deserialize(params.get("Notification"))
        self.UpdatedAt = params.get("UpdatedAt")
        self.ClusterId = params.get("ClusterId")
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
        r"""
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
        :param Annotations: 参考prometheus rule中的annotations
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of Label
        :param RuleState: 告警规则状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleState: int
        """
        self.Name = None
        self.Rule = None
        self.Labels = None
        self.Template = None
        self.For = None
        self.Describe = None
        self.Annotations = None
        self.RuleState = None


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
        self.RuleState = params.get("RuleState")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusConfigItem(AbstractModel):
    """prometheus配置

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusGrafanaInfo(AbstractModel):
    """托管prometheus中grafana的信息

    """

    def __init__(self):
        r"""
        :param Enabled: 是否启用
        :type Enabled: bool
        :param Domain: 域名，只有开启外网访问才有效果
        :type Domain: str
        :param Address: 内网地址，或者外网地址
        :type Address: str
        :param Internet: 是否开启了外网访问
close = 未开启外网访问
opening = 正在开启外网访问
open  = 已开启外网访问
        :type Internet: str
        :param AdminUser: grafana管理员用户名
        :type AdminUser: str
        """
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
        r"""
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
        :param GrafanaURL: grafana默认地址，如果开启外网访问得为域名，否则为内网地址
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaURL: str
        :param BoundTotal: 关联集群总数
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundTotal: int
        :param BoundNormal: 运行正常的集群数
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundNormal: int
        """
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
        


class PrometheusInstancesOverview(AbstractModel):
    """托管prometheusV2实例概览

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名
        :type InstanceName: str
        :param VpcId: VPC ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param InstanceStatus: 运行状态（1:正在创建；2:运行中；3:异常；4:重启中；5:销毁中； 6:已停机； 7: 已删除）
        :type InstanceStatus: int
        :param ChargeStatus: 计费状态（1:正常；2:过期; 3:销毁; 4:分配中; 5:分配失败）
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeStatus: int
        :param EnableGrafana: 是否开启 Grafana（0:不开启，1:开启）
        :type EnableGrafana: int
        :param GrafanaURL: Grafana 面板 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type GrafanaURL: str
        :param InstanceChargeType: 实例付费类型（1:试用版；2:预付费）
        :type InstanceChargeType: int
        :param SpecName: 规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecName: str
        :param DataRetentionTime: 存储周期
注意：此字段可能返回 null，表示取不到有效值。
        :type DataRetentionTime: int
        :param ExpireTime: 购买的实例过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param AutoRenewFlag: 自动续费标记(0:不自动续费；1:开启自动续费；2:禁止自动续费；-1:无效)
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param BoundTotal: 绑定集群总数
        :type BoundTotal: int
        :param BoundNormal: 绑定集群正常状态总数
        :type BoundNormal: int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceStatus = None
        self.ChargeStatus = None
        self.EnableGrafana = None
        self.GrafanaURL = None
        self.InstanceChargeType = None
        self.SpecName = None
        self.DataRetentionTime = None
        self.ExpireTime = None
        self.AutoRenewFlag = None
        self.BoundTotal = None
        self.BoundNormal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceStatus = params.get("InstanceStatus")
        self.ChargeStatus = params.get("ChargeStatus")
        self.EnableGrafana = params.get("EnableGrafana")
        self.GrafanaURL = params.get("GrafanaURL")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.SpecName = params.get("SpecName")
        self.DataRetentionTime = params.get("DataRetentionTime")
        self.ExpireTime = params.get("ExpireTime")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotification(AbstractModel):
    """amp告警渠道配置

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusNotificationItem(AbstractModel):
    """告警通知渠道配置

    """

    def __init__(self):
        r"""
        :param Enabled: 是否启用
        :type Enabled: bool
        :param Type: 通道类型，默认为amp，支持以下
amp
webhook
alertmanager
        :type Type: str
        :param WebHook: 如果Type为webhook, 则该字段为必填项
注意：此字段可能返回 null，表示取不到有效值。
        :type WebHook: str
        :param AlertManager: 如果Type为alertmanager, 则该字段为必填项
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertManager: :class:`tencentcloud.tke.v20180525.models.PrometheusAlertManagerConfig`
        :param RepeatInterval: 收敛时间
        :type RepeatInterval: str
        :param TimeRangeStart: 生效起始时间
        :type TimeRangeStart: str
        :param TimeRangeEnd: 生效结束时间
        :type TimeRangeEnd: str
        :param NotifyWay: 告警通知方式。目前有SMS、EMAIL、CALL、WECHAT方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type NotifyWay: list of str
        :param ReceiverGroups: 告警接收组（用户组）
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverGroups: list of str
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
        """
        self.Enabled = None
        self.Type = None
        self.WebHook = None
        self.AlertManager = None
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


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Type = params.get("Type")
        self.WebHook = params.get("WebHook")
        if params.get("AlertManager") is not None:
            self.AlertManager = PrometheusAlertManagerConfig()
            self.AlertManager._deserialize(params.get("AlertManager"))
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusRecordRuleYamlItem(AbstractModel):
    """prometheus聚合规则实例详情，包含所属集群ID

    """

    def __init__(self):
        r"""
        :param Name: 实例名称
        :type Name: str
        :param UpdateTime: 最近更新时间
        :type UpdateTime: str
        :param TemplateId: Yaml内容
        :type TemplateId: str
        :param Content: 如果该聚合规则来至模板，则TemplateId为模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param ClusterId: 该聚合规则如果来源于用户集群crd资源定义，则ClusterId为所属集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        """
        self.Name = None
        self.UpdateTime = None
        self.TemplateId = None
        self.Content = None
        self.ClusterId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.UpdateTime = params.get("UpdateTime")
        self.TemplateId = params.get("TemplateId")
        self.Content = params.get("Content")
        self.ClusterId = params.get("ClusterId")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemp(AbstractModel):
    """模板实例

    """

    def __init__(self):
        r"""
        :param Name: 模板名称
        :type Name: str
        :param Level: 模板维度，支持以下类型
instance 实例级别
cluster 集群级别
        :type Level: str
        :param Describe: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
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
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        :param TargetsTotal: 关联实例数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetsTotal: int
        """
        self.Name = None
        self.Level = None
        self.Describe = None
        self.RecordRules = None
        self.ServiceMonitors = None
        self.PodMonitors = None
        self.RawJobs = None
        self.TemplateId = None
        self.UpdateTime = None
        self.Version = None
        self.IsDefault = None
        self.AlertDetailRules = None
        self.TargetsTotal = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Level = params.get("Level")
        self.Describe = params.get("Describe")
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
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self.AlertDetailRules.append(obj)
        self.TargetsTotal = params.get("TargetsTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTempModify(AbstractModel):
    """云原生Prometheus模板可修改项

    """

    def __init__(self):
        r"""
        :param Name: 修改名称
        :type Name: str
        :param Describe: 修改描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
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
        :param RecordRules: 当Level为instance时有效，
模板中的聚合规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordRules: list of PrometheusConfigItem
        :param AlertDetailRules: 修改内容，只有当模板类型是Alert时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertDetailRules: list of PrometheusAlertPolicyItem
        """
        self.Name = None
        self.Describe = None
        self.ServiceMonitors = None
        self.PodMonitors = None
        self.RawJobs = None
        self.RecordRules = None
        self.AlertDetailRules = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Describe = params.get("Describe")
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
        if params.get("RecordRules") is not None:
            self.RecordRules = []
            for item in params.get("RecordRules"):
                obj = PrometheusConfigItem()
                obj._deserialize(item)
                self.RecordRules.append(obj)
        if params.get("AlertDetailRules") is not None:
            self.AlertDetailRules = []
            for item in params.get("AlertDetailRules"):
                obj = PrometheusAlertPolicyItem()
                obj._deserialize(item)
                self.AlertDetailRules.append(obj)
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateModify(AbstractModel):
    """云原生Prometheus模板可修改项

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrometheusTemplateSyncTarget(AbstractModel):
    """云原生Prometheus模板同步目标

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInstance(AbstractModel):
    """地域属性信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolRequest(AbstractModel):
    """RemoveNodeFromNodePool请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param NodePoolId: 节点池id
        :type NodePoolId: str
        :param InstanceIds: 节点id列表，一次最多支持100台
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveNodeFromNodePoolResponse(AbstractModel):
    """RemoveNodeFromNodePool返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceDeleteOption(AbstractModel):
    """资源删除选项

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsage(AbstractModel):
    """集群资源使用量

    """

    def __init__(self):
        r"""
        :param Name: 资源类型
        :type Name: str
        :param Usage: 资源使用量
        :type Usage: int
        :param Details: 资源使用详情
        :type Details: list of ResourceUsageDetail
        """
        self.Name = None
        self.Usage = None
        self.Details = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usage = params.get("Usage")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ResourceUsageDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceUsageDetail(AbstractModel):
    """资源使用明细

    """

    def __init__(self):
        r"""
        :param Name: 资源名称
        :type Name: str
        :param Usage: 资源使用量
        :type Usage: int
        """
        self.Name = None
        self.Usage = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Usage = params.get("Usage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartEKSContainerInstancesRequest(AbstractModel):
    """RestartEKSContainerInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiIds: EKS instance ids
        :type EksCiIds: list of str
        """
        self.EksCiIds = None


    def _deserialize(self, params):
        self.EksCiIds = params.get("EksCiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartEKSContainerInstancesResponse(AbstractModel):
    """RestartEKSContainerInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RouteInfo(AbstractModel):
    """集群路由对象

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableConflict(AbstractModel):
    """路由表冲突对象

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableInfo(AbstractModel):
    """集群路由表对象

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunAutomationServiceEnabled(AbstractModel):
    """描述了 “云自动化助手” 服务相关的信息

    """

    def __init__(self):
        r"""
        :param Enabled: 是否开启云自动化助手。取值范围：<br><li>TRUE：表示开启云自动化助手服务<br><li>FALSE：表示不开启云自动化助手服务<br><br>默认取值：FALSE。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesForNode(AbstractModel):
    """不同角色的节点配置参数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunMonitorServiceEnabled(AbstractModel):
    """描述了 “云监控” 服务相关的信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """描述了 “云安全” 服务相关的信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInClusterMasterRequest(AbstractModel):
    """ScaleInClusterMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群实例ID
        :type ClusterId: str
        :param ScaleInMasters: master缩容选项
        :type ScaleInMasters: list of ScaleInMaster
        """
        self.ClusterId = None
        self.ScaleInMasters = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ScaleInMasters") is not None:
            self.ScaleInMasters = []
            for item in params.get("ScaleInMasters"):
                obj = ScaleInMaster()
                obj._deserialize(item)
                self.ScaleInMasters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleInClusterMasterResponse(AbstractModel):
    """ScaleInClusterMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ScaleInMaster(AbstractModel):
    """master节点缩容参数

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param NodeRole: 缩容的实例角色：MASTER,ETCD,MASTER_ETCD
        :type NodeRole: str
        :param InstanceDeleteMode: 实例的保留模式
        :type InstanceDeleteMode: str
        """
        self.InstanceId = None
        self.NodeRole = None
        self.InstanceDeleteMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.NodeRole = params.get("NodeRole")
        self.InstanceDeleteMode = params.get("InstanceDeleteMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutClusterMasterRequest(AbstractModel):
    """ScaleOutClusterMaster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群实例ID
        :type ClusterId: str
        :param RunInstancesForNode: 新建节点参数
        :type RunInstancesForNode: list of RunInstancesForNode
        :param ExistedInstancesForNode: 添加已有节点相关参数
        :type ExistedInstancesForNode: list of ExistedInstancesForNode
        :param InstanceAdvancedSettings: 实例高级设置
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20180525.models.InstanceAdvancedSettings`
        :param ExtraArgs: 集群master组件自定义参数
        :type ExtraArgs: :class:`tencentcloud.tke.v20180525.models.ClusterExtraArgs`
        """
        self.ClusterId = None
        self.RunInstancesForNode = None
        self.ExistedInstancesForNode = None
        self.InstanceAdvancedSettings = None
        self.ExtraArgs = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("RunInstancesForNode") is not None:
            self.RunInstancesForNode = []
            for item in params.get("RunInstancesForNode"):
                obj = RunInstancesForNode()
                obj._deserialize(item)
                self.RunInstancesForNode.append(obj)
        if params.get("ExistedInstancesForNode") is not None:
            self.ExistedInstancesForNode = []
            for item in params.get("ExistedInstancesForNode"):
                obj = ExistedInstancesForNode()
                obj._deserialize(item)
                self.ExistedInstancesForNode.append(obj)
        if params.get("InstanceAdvancedSettings") is not None:
            self.InstanceAdvancedSettings = InstanceAdvancedSettings()
            self.InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        if params.get("ExtraArgs") is not None:
            self.ExtraArgs = ClusterExtraArgs()
            self.ExtraArgs._deserialize(params.get("ExtraArgs"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScaleOutClusterMasterResponse(AbstractModel):
    """ScaleOutClusterMaster返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SecurityContext(AbstractModel):
    """cloudrun安全特性

    """

    def __init__(self):
        r"""
        :param Capabilities: 安全能力清单
注意：此字段可能返回 null，表示取不到有效值。
        :type Capabilities: :class:`tencentcloud.tke.v20180525.models.Capabilities`
        """
        self.Capabilities = None


    def _deserialize(self, params):
        if params.get("Capabilities") is not None:
            self.Capabilities = Capabilities()
            self.Capabilities._deserialize(params.get("Capabilities"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceAccountAuthenticationOptions(AbstractModel):
    """ServiceAccount认证相关配置

    """

    def __init__(self):
        r"""
        :param Issuer: service-account-issuer
注意：此字段可能返回 null，表示取不到有效值。
        :type Issuer: str
        :param JWKSURI: service-account-jwks-uri
注意：此字段可能返回 null，表示取不到有效值。
        :type JWKSURI: str
        :param AutoCreateDiscoveryAnonymousAuth: 如果为true，则会自动创建允许匿名用户访问'/.well-known/openid-configuration'和/openid/v1/jwks的rbac规则
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoCreateDiscoveryAnonymousAuth: bool
        """
        self.Issuer = None
        self.JWKSURI = None
        self.AutoCreateDiscoveryAnonymousAuth = None


    def _deserialize(self, params):
        self.Issuer = params.get("Issuer")
        self.JWKSURI = params.get("JWKSURI")
        self.AutoCreateDiscoveryAnonymousAuth = params.get("AutoCreateDiscoveryAnonymousAuth")
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
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetNodePoolNodeProtectionResponse(AbstractModel):
    """SetNodePoolNodeProtection返回参数结构体

    """

    def __init__(self):
        r"""
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


class SyncPrometheusTempRequest(AbstractModel):
    """SyncPrometheusTemp请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPrometheusTempResponse(AbstractModel):
    """SyncPrometheusTemp返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SyncPrometheusTemplateRequest(AbstractModel):
    """SyncPrometheusTemplate请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncPrometheusTemplateResponse(AbstractModel):
    """SyncPrometheusTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签绑定的资源类型，当前支持类型："cluster"

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云主机实例。

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Taint(AbstractModel):
    """kubernetes Taint

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStepInfo(AbstractModel):
    """任务步骤信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcpSocket(AbstractModel):
    """探针使用TcpSocket检测容器

    """

    def __init__(self):
        r"""
        :param Port: TcpSocket检测的端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self.Port = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallLogAgentRequest(AbstractModel):
    """UninstallLogAgent请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UninstallLogAgentResponse(AbstractModel):
    """UninstallLogAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateClusterVersionRequest(AbstractModel):
    """UpdateClusterVersion请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateClusterVersionResponse(AbstractModel):
    """UpdateClusterVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateEKSClusterRequest(AbstractModel):
    """UpdateEKSCluster请求参数结构体

    """

    def __init__(self):
        r"""
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
        :param ProxyLB: 标记是否是新的内外网。默认为false
        :type ProxyLB: bool
        :param ExtraParam: 扩展参数。须是map[string]string 的json 格式。
        :type ExtraParam: str
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
        self.ProxyLB = None
        self.ExtraParam = None


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
        self.ProxyLB = params.get("ProxyLB")
        self.ExtraParam = params.get("ExtraParam")
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateEKSContainerInstanceRequest(AbstractModel):
    """UpdateEKSContainerInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiId: 容器实例 ID
        :type EksCiId: str
        :param RestartPolicy: 实例重启策略： Always(总是重启)、Never(从不重启)、OnFailure(失败时重启)
        :type RestartPolicy: str
        :param EksCiVolume: 数据卷，包含NfsVolume数组和CbsVolume数组
        :type EksCiVolume: :class:`tencentcloud.tke.v20180525.models.EksCiVolume`
        :param Containers: 容器组
        :type Containers: list of Container
        :param InitContainers: Init 容器组
        :type InitContainers: list of Container
        :param Name: 容器实例名称
        :type Name: str
        :param ImageRegistryCredentials: 镜像仓库凭证数组
        :type ImageRegistryCredentials: list of ImageRegistryCredential
        """
        self.EksCiId = None
        self.RestartPolicy = None
        self.EksCiVolume = None
        self.Containers = None
        self.InitContainers = None
        self.Name = None
        self.ImageRegistryCredentials = None


    def _deserialize(self, params):
        self.EksCiId = params.get("EksCiId")
        self.RestartPolicy = params.get("RestartPolicy")
        if params.get("EksCiVolume") is not None:
            self.EksCiVolume = EksCiVolume()
            self.EksCiVolume._deserialize(params.get("EksCiVolume"))
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        self.Name = params.get("Name")
        if params.get("ImageRegistryCredentials") is not None:
            self.ImageRegistryCredentials = []
            for item in params.get("ImageRegistryCredentials"):
                obj = ImageRegistryCredential()
                obj._deserialize(item)
                self.ImageRegistryCredentials.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEKSContainerInstanceResponse(AbstractModel):
    """UpdateEKSContainerInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param EksCiId: 容器实例 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EksCiId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EksCiId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EksCiId = params.get("EksCiId")
        self.RequestId = params.get("RequestId")


class UpdateImageCacheRequest(AbstractModel):
    """UpdateImageCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageCacheId: 镜像缓存Id
        :type ImageCacheId: str
        :param ImageCacheName: 镜像缓存名称
        :type ImageCacheName: str
        """
        self.ImageCacheId = None
        self.ImageCacheName = None


    def _deserialize(self, params):
        self.ImageCacheId = params.get("ImageCacheId")
        self.ImageCacheName = params.get("ImageCacheName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateImageCacheResponse(AbstractModel):
    """UpdateImageCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeAbleInstancesItem(AbstractModel):
    """可升级节点信息

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesRequest(AbstractModel):
    """UpgradeClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeClusterInstancesResponse(AbstractModel):
    """UpgradeClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeNodeResetParam(AbstractModel):
    """节点升级重装参数

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VersionInstance(AbstractModel):
    """版本信息

    """

    def __init__(self):
        r"""
        :param Name: 版本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Version: 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param Remark: Remark
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
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
        


class VolumeMount(AbstractModel):
    """数据卷挂载路径信息

    """

    def __init__(self):
        r"""
        :param Name: volume名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param MountPath: 挂载路径
注意：此字段可能返回 null，表示取不到有效值。
        :type MountPath: str
        :param ReadOnly: 是否只读
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: bool
        :param SubPath: 子路径
注意：此字段可能返回 null，表示取不到有效值。
        :type SubPath: str
        :param MountPropagation: 传播挂载方式
注意：此字段可能返回 null，表示取不到有效值。
        :type MountPropagation: str
        :param SubPathExpr: 子路径表达式
注意：此字段可能返回 null，表示取不到有效值。
        :type SubPathExpr: str
        """
        self.Name = None
        self.MountPath = None
        self.ReadOnly = None
        self.SubPath = None
        self.MountPropagation = None
        self.SubPathExpr = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MountPath = params.get("MountPath")
        self.ReadOnly = params.get("ReadOnly")
        self.SubPath = params.get("SubPath")
        self.MountPropagation = params.get("MountPropagation")
        self.SubPathExpr = params.get("SubPathExpr")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        