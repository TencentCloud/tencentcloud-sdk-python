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


class Annotation(AbstractModel):
    """k8s中标注，一般以数组的方式存在

    """

    def __init__(self):
        r"""
        :param _Name: map表中的Name
        :type Name: str
        :param _Value: map表中的Value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoUpgradeOptions(AbstractModel):
    """托管节点池运维窗口设置

    """

    def __init__(self):
        r"""
        :param _AutoUpgradeStartTime: 自动升级开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoUpgradeStartTime: str
        :param _Duration: 自动升级持续时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param _WeeklyPeriod: 运维日期
注意：此字段可能返回 null，表示取不到有效值。
        :type WeeklyPeriod: list of str
        """
        self._AutoUpgradeStartTime = None
        self._Duration = None
        self._WeeklyPeriod = None

    @property
    def AutoUpgradeStartTime(self):
        return self._AutoUpgradeStartTime

    @AutoUpgradeStartTime.setter
    def AutoUpgradeStartTime(self, AutoUpgradeStartTime):
        self._AutoUpgradeStartTime = AutoUpgradeStartTime

    @property
    def Duration(self):
        return self._Duration

    @Duration.setter
    def Duration(self, Duration):
        self._Duration = Duration

    @property
    def WeeklyPeriod(self):
        return self._WeeklyPeriod

    @WeeklyPeriod.setter
    def WeeklyPeriod(self, WeeklyPeriod):
        self._WeeklyPeriod = WeeklyPeriod


    def _deserialize(self, params):
        self._AutoUpgradeStartTime = params.get("AutoUpgradeStartTime")
        self._Duration = params.get("Duration")
        self._WeeklyPeriod = params.get("WeeklyPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoscalingAdded(AbstractModel):
    """自动扩缩容的节点

    """

    def __init__(self):
        r"""
        :param _Joining: 正在加入中的节点数量
        :type Joining: int
        :param _Initializing: 初始化中的节点数量
        :type Initializing: int
        :param _Normal: 正常的节点数量
        :type Normal: int
        :param _Total: 节点总数
        :type Total: int
        """
        self._Joining = None
        self._Initializing = None
        self._Normal = None
        self._Total = None

    @property
    def Joining(self):
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Joining = params.get("Joining")
        self._Initializing = params.get("Initializing")
        self._Normal = params.get("Normal")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckPolicyRequest(AbstractModel):
    """CreateHealthCheckPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _HealthCheckPolicy: 健康检测策略
        :type HealthCheckPolicy: :class:`tencentcloud.tke.v20220501.models.HealthCheckPolicy`
        """
        self._ClusterId = None
        self._HealthCheckPolicy = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def HealthCheckPolicy(self):
        return self._HealthCheckPolicy

    @HealthCheckPolicy.setter
    def HealthCheckPolicy(self, HealthCheckPolicy):
        self._HealthCheckPolicy = HealthCheckPolicy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("HealthCheckPolicy") is not None:
            self._HealthCheckPolicy = HealthCheckPolicy()
            self._HealthCheckPolicy._deserialize(params.get("HealthCheckPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckPolicyResponse(AbstractModel):
    """CreateHealthCheckPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckPolicyName: 健康检测策略名称
        :type HealthCheckPolicyName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthCheckPolicyName = None
        self._RequestId = None

    @property
    def HealthCheckPolicyName(self):
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._RequestId = params.get("RequestId")


class CreateNativeNodePoolParam(AbstractModel):
    """原生节点池创建参数

    """

    def __init__(self):
        r"""
        :param _Scaling: 节点池伸缩配置
        :type Scaling: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        :param _SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param _InstanceChargeType: 节点计费类型。PREPAID：包年包月；POSTPAID_BY_HOUR：按量计费（默认）；
        :type InstanceChargeType: str
        :param _SystemDisk: 系统盘配置
        :type SystemDisk: :class:`tencentcloud.tke.v20220501.models.Disk`
        :param _InstanceTypes: 机型列表
        :type InstanceTypes: list of str
        :param _SecurityGroupIds: 安全组列表
        :type SecurityGroupIds: list of str
        :param _UpgradeSettings: 自动升级配置
        :type UpgradeSettings: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        :param _AutoRepair: 是否开启自愈能力
        :type AutoRepair: bool
        :param _InstanceChargePrepaid: 包年包月机型计费配置
        :type InstanceChargePrepaid: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        :param _Management: 节点池 Management 参数设置
        :type Management: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        :param _HealthCheckPolicyName: 故障自愈规则名称
        :type HealthCheckPolicyName: str
        :param _HostNamePattern: 原生节点池hostName模式串
        :type HostNamePattern: str
        :param _KubeletArgs: kubelet 自定义参数
        :type KubeletArgs: list of str
        :param _Lifecycle: 预定义脚本
        :type Lifecycle: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        :param _RuntimeRootDir: 运行时根目录
        :type RuntimeRootDir: str
        :param _EnableAutoscaling: 是否开启弹性伸缩
        :type EnableAutoscaling: bool
        :param _Replicas: 期望节点数
        :type Replicas: int
        :param _InternetAccessible: 公网带宽设置
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _DataDisks: 原生节点池数据盘列表
        :type DataDisks: list of DataDisk
        :param _KeyIds: 节点池ssh公钥id数组
        :type KeyIds: list of str
        """
        self._Scaling = None
        self._SubnetIds = None
        self._InstanceChargeType = None
        self._SystemDisk = None
        self._InstanceTypes = None
        self._SecurityGroupIds = None
        self._UpgradeSettings = None
        self._AutoRepair = None
        self._InstanceChargePrepaid = None
        self._Management = None
        self._HealthCheckPolicyName = None
        self._HostNamePattern = None
        self._KubeletArgs = None
        self._Lifecycle = None
        self._RuntimeRootDir = None
        self._EnableAutoscaling = None
        self._Replicas = None
        self._InternetAccessible = None
        self._DataDisks = None
        self._KeyIds = None

    @property
    def Scaling(self):
        return self._Scaling

    @Scaling.setter
    def Scaling(self, Scaling):
        self._Scaling = Scaling

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeSettings(self):
        return self._UpgradeSettings

    @UpgradeSettings.setter
    def UpgradeSettings(self, UpgradeSettings):
        self._UpgradeSettings = UpgradeSettings

    @property
    def AutoRepair(self):
        return self._AutoRepair

    @AutoRepair.setter
    def AutoRepair(self, AutoRepair):
        self._AutoRepair = AutoRepair

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def Management(self):
        return self._Management

    @Management.setter
    def Management(self, Management):
        self._Management = Management

    @property
    def HealthCheckPolicyName(self):
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def HostNamePattern(self):
        return self._HostNamePattern

    @HostNamePattern.setter
    def HostNamePattern(self, HostNamePattern):
        self._HostNamePattern = HostNamePattern

    @property
    def KubeletArgs(self):
        return self._KubeletArgs

    @KubeletArgs.setter
    def KubeletArgs(self, KubeletArgs):
        self._KubeletArgs = KubeletArgs

    @property
    def Lifecycle(self):
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def RuntimeRootDir(self):
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir

    @property
    def EnableAutoscaling(self):
        return self._EnableAutoscaling

    @EnableAutoscaling.setter
    def EnableAutoscaling(self, EnableAutoscaling):
        self._EnableAutoscaling = EnableAutoscaling

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        if params.get("Scaling") is not None:
            self._Scaling = MachineSetScaling()
            self._Scaling._deserialize(params.get("Scaling"))
        self._SubnetIds = params.get("SubnetIds")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceTypes = params.get("InstanceTypes")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeSettings") is not None:
            self._UpgradeSettings = MachineUpgradeSettings()
            self._UpgradeSettings._deserialize(params.get("UpgradeSettings"))
        self._AutoRepair = params.get("AutoRepair")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("Management") is not None:
            self._Management = ManagementConfig()
            self._Management._deserialize(params.get("Management"))
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._HostNamePattern = params.get("HostNamePattern")
        self._KubeletArgs = params.get("KubeletArgs")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifecycleConfig()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        self._EnableAutoscaling = params.get("EnableAutoscaling")
        self._Replicas = params.get("Replicas")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNodePoolRequest(AbstractModel):
    """CreateNodePool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Name: 节点池名称
        :type Name: str
        :param _Type: 节点池类型
        :type Type: str
        :param _Labels: 节点  Labels
        :type Labels: list of Label
        :param _Taints: 节点污点
        :type Taints: list of Taint
        :param _Tags: 节点标签
        :type Tags: list of TagSpecification
        :param _DeletionProtection: 是否开启删除保护
        :type DeletionProtection: bool
        :param _Unschedulable: 节点是否默认不可调度
        :type Unschedulable: bool
        :param _Native: 原生节点池创建参数
        :type Native: :class:`tencentcloud.tke.v20220501.models.CreateNativeNodePoolParam`
        :param _Annotations: 节点 Annotation 列表
        :type Annotations: list of Annotation
        """
        self._ClusterId = None
        self._Name = None
        self._Type = None
        self._Labels = None
        self._Taints = None
        self._Tags = None
        self._DeletionProtection = None
        self._Unschedulable = None
        self._Native = None
        self._Annotations = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Native(self):
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Unschedulable = params.get("Unschedulable")
        if params.get("Native") is not None:
            self._Native = CreateNativeNodePoolParam()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNodePoolResponse(AbstractModel):
    """CreateNodePool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodePoolId: 节点池 ID
        :type NodePoolId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodePoolId = None
        self._RequestId = None

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NodePoolId = params.get("NodePoolId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了k8s节点数据盘相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _DiskType: 云盘类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskType: str
        :param _FileSystem: 文件系统(ext3/ext4/xfs)
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSystem: str
        :param _DiskSize: 云盘大小(G）
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskSize: int
        :param _AutoFormatAndMount: 是否自动化格式盘并挂载
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoFormatAndMount: bool
        :param _DiskPartition: 挂载设备名或分区名
注意：此字段可能返回 null，表示取不到有效值。
        :type DiskPartition: str
        :param _MountTarget: 挂载目录
注意：此字段可能返回 null，表示取不到有效值。
        :type MountTarget: str
        :param _Encrypt: 传入该参数用于创建加密云盘，取值固定为ENCRYPT
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: str
        :param _KmsKeyId: 购买加密盘时自定义密钥，当传入该参数时, Encrypt入参不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type KmsKeyId: str
        :param _SnapshotId: 快照ID，如果传入则根据此快照创建云硬盘，快照类型必须为数据盘快照
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotId: str
        :param _ThroughputPerformance: 云硬盘性能，单位：MB/s。使用此参数可给云硬盘购买额外的性能
注意：此字段可能返回 null，表示取不到有效值。
        :type ThroughputPerformance: int
        """
        self._DiskType = None
        self._FileSystem = None
        self._DiskSize = None
        self._AutoFormatAndMount = None
        self._DiskPartition = None
        self._MountTarget = None
        self._Encrypt = None
        self._KmsKeyId = None
        self._SnapshotId = None
        self._ThroughputPerformance = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def AutoFormatAndMount(self):
        return self._AutoFormatAndMount

    @AutoFormatAndMount.setter
    def AutoFormatAndMount(self, AutoFormatAndMount):
        self._AutoFormatAndMount = AutoFormatAndMount

    @property
    def DiskPartition(self):
        return self._DiskPartition

    @DiskPartition.setter
    def DiskPartition(self, DiskPartition):
        self._DiskPartition = DiskPartition

    @property
    def MountTarget(self):
        return self._MountTarget

    @MountTarget.setter
    def MountTarget(self, MountTarget):
        self._MountTarget = MountTarget

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def KmsKeyId(self):
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def SnapshotId(self):
        return self._SnapshotId

    @SnapshotId.setter
    def SnapshotId(self, SnapshotId):
        self._SnapshotId = SnapshotId

    @property
    def ThroughputPerformance(self):
        return self._ThroughputPerformance

    @ThroughputPerformance.setter
    def ThroughputPerformance(self, ThroughputPerformance):
        self._ThroughputPerformance = ThroughputPerformance


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._FileSystem = params.get("FileSystem")
        self._DiskSize = params.get("DiskSize")
        self._AutoFormatAndMount = params.get("AutoFormatAndMount")
        self._DiskPartition = params.get("DiskPartition")
        self._MountTarget = params.get("MountTarget")
        self._Encrypt = params.get("Encrypt")
        self._KmsKeyId = params.get("KmsKeyId")
        self._SnapshotId = params.get("SnapshotId")
        self._ThroughputPerformance = params.get("ThroughputPerformance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckPolicyRequest(AbstractModel):
    """DeleteHealthCheckPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _HealthCheckPolicyName: 健康检测策略名称
        :type HealthCheckPolicyName: str
        """
        self._ClusterId = None
        self._HealthCheckPolicyName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def HealthCheckPolicyName(self):
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckPolicyResponse(AbstractModel):
    """DeleteHealthCheckPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteNodePoolRequest(AbstractModel):
    """DeleteNodePool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _NodePoolId: 节点池 ID
        :type NodePoolId: str
        """
        self._ClusterId = None
        self._NodePoolId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNodePoolResponse(AbstractModel):
    """DeleteNodePool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeClusterInstancesRequest(AbstractModel):
    """DescribeClusterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Filters: 过滤条件列表:
InstanceIds(实例ID),InstanceType(实例类型：Regular，Native，Virtual，External),VagueIpAddress(模糊匹配IP),Labels(k8s节点label),NodePoolNames(节点池名称),VagueInstanceName(模糊匹配节点名),InstanceStates(节点状态),Unschedulable(是否封锁),NodePoolIds(节点池ID)
        :type Filters: list of Filter
        :param _SortBy: 排序信息
        :type SortBy: :class:`tencentcloud.tke.v20220501.models.SortBy`
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._SortBy = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstancesResponse(AbstractModel):
    """DescribeClusterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集群中实例总数
        :type TotalCount: int
        :param _InstanceSet: 集群中实例列表
        :type InstanceSet: list of Instance
        :param _Errors: 错误信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Errors: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._Errors = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def Errors(self):
        return self._Errors

    @Errors.setter
    def Errors(self, Errors):
        self._Errors = Errors

    @property
    def RequestId(self):
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
        self._Errors = params.get("Errors")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckPoliciesRequest(AbstractModel):
    """DescribeHealthCheckPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Filters: ·  HealthCheckPolicyName
    按照【健康检测策略名称】进行过滤。
    类型：String
    必选：否
        :type Filters: list of Filter
        :param _Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        """
        self._ClusterId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthCheckPoliciesResponse(AbstractModel):
    """DescribeHealthCheckPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckPolicies: 健康检测策略数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckPolicies: list of HealthCheckPolicy
        :param _TotalCount: 数组总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthCheckPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HealthCheckPolicies(self):
        return self._HealthCheckPolicies

    @HealthCheckPolicies.setter
    def HealthCheckPolicies(self, HealthCheckPolicies):
        self._HealthCheckPolicies = HealthCheckPolicies

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthCheckPolicies") is not None:
            self._HealthCheckPolicies = []
            for item in params.get("HealthCheckPolicies"):
                obj = HealthCheckPolicy()
                obj._deserialize(item)
                self._HealthCheckPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckPolicyBindingsRequest(AbstractModel):
    """DescribeHealthCheckPolicyBindings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Filter: ·  HealthCheckPolicyName
    按照【健康检测规则名称】进行过滤。
    类型：String
    必选：否
        :type Filter: list of Filter
        :param _Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        :param _Offset: 偏移量，默认0
        :type Offset: int
        """
        self._ClusterId = None
        self._Filter = None
        self._Limit = None
        self._Offset = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filter(self):
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("Filter") is not None:
            self._Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self._Filter.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthCheckPolicyBindingsResponse(AbstractModel):
    """DescribeHealthCheckPolicyBindings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckPolicyBindings: 健康检测规则数组
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckPolicyBindings: list of HealthCheckPolicyBinding
        :param _TotalCount: 健康检测规则数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthCheckPolicyBindings = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HealthCheckPolicyBindings(self):
        return self._HealthCheckPolicyBindings

    @HealthCheckPolicyBindings.setter
    def HealthCheckPolicyBindings(self, HealthCheckPolicyBindings):
        self._HealthCheckPolicyBindings = HealthCheckPolicyBindings

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthCheckPolicyBindings") is not None:
            self._HealthCheckPolicyBindings = []
            for item in params.get("HealthCheckPolicyBindings"):
                obj = HealthCheckPolicyBinding()
                obj._deserialize(item)
                self._HealthCheckPolicyBindings.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckTemplateRequest(AbstractModel):
    """DescribeHealthCheckTemplate请求参数结构体

    """


class DescribeHealthCheckTemplateResponse(AbstractModel):
    """DescribeHealthCheckTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplate: 健康检测策略模板
        :type HealthCheckTemplate: :class:`tencentcloud.tke.v20220501.models.HealthCheckTemplate`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthCheckTemplate = None
        self._RequestId = None

    @property
    def HealthCheckTemplate(self):
        return self._HealthCheckTemplate

    @HealthCheckTemplate.setter
    def HealthCheckTemplate(self, HealthCheckTemplate):
        self._HealthCheckTemplate = HealthCheckTemplate

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HealthCheckTemplate") is not None:
            self._HealthCheckTemplate = HealthCheckTemplate()
            self._HealthCheckTemplate._deserialize(params.get("HealthCheckTemplate"))
        self._RequestId = params.get("RequestId")


class DescribeNodePoolsRequest(AbstractModel):
    """DescribeNodePools请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _Filters: 查询过滤条件：
·  NodePoolsName
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
        :param _Offset: 偏移量，默认0
        :type Offset: int
        :param _Limit: 最大输出条数，默认20，最大为100
        :type Limit: int
        """
        self._ClusterId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
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
        


class DescribeNodePoolsResponse(AbstractModel):
    """DescribeNodePools返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodePools: 节点池列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePools: list of NodePool
        :param _TotalCount: 资源总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodePools = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodePools(self):
        return self._NodePools

    @NodePools.setter
    def NodePools(self, NodePools):
        self._NodePools = NodePools

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NodePools") is not None:
            self._NodePools = []
            for item in params.get("NodePools"):
                obj = NodePool()
                obj._deserialize(item)
                self._NodePools.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class Disk(AbstractModel):
    """节点系统盘和数据盘配置

    """

    def __init__(self):
        r"""
        :param _DiskType: 云盘类型
        :type DiskType: str
        :param _DiskSize: 云盘大小(G）
        :type DiskSize: int
        :param _AutoFormatAndMount: 是否自动化格式盘并挂载
        :type AutoFormatAndMount: bool
        :param _FileSystem: 文件系统
        :type FileSystem: str
        :param _MountTarget: 挂载目录
        :type MountTarget: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._AutoFormatAndMount = None
        self._FileSystem = None
        self._MountTarget = None

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def AutoFormatAndMount(self):
        return self._AutoFormatAndMount

    @AutoFormatAndMount.setter
    def AutoFormatAndMount(self, AutoFormatAndMount):
        self._AutoFormatAndMount = AutoFormatAndMount

    @property
    def FileSystem(self):
        return self._FileSystem

    @FileSystem.setter
    def FileSystem(self, FileSystem):
        self._FileSystem = FileSystem

    @property
    def MountTarget(self):
        return self._MountTarget

    @MountTarget.setter
    def MountTarget(self, MountTarget):
        self._MountTarget = MountTarget


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._AutoFormatAndMount = params.get("AutoFormatAndMount")
        self._FileSystem = params.get("FileSystem")
        self._MountTarget = params.get("MountTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalNodeInfo(AbstractModel):
    """第三方节点

    """

    def __init__(self):
        r"""
        :param _Name: 第三方节点名称
        :type Name: str
        :param _CPU: CPU核数，单位：核
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: int
        :param _Memory: 节点内存容量，单位：`GB`
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _K8SVersion: 第三方节点kubelet版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type K8SVersion: str
        """
        self._Name = None
        self._CPU = None
        self._Memory = None
        self._K8SVersion = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def K8SVersion(self):
        return self._K8SVersion

    @K8SVersion.setter
    def K8SVersion(self, K8SVersion):
        self._K8SVersion = K8SVersion


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._K8SVersion = params.get("K8SVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalNodePoolInfo(AbstractModel):
    """第三方节点池信息

    """

    def __init__(self):
        r"""
        :param _RuntimeConfig: 第三方节点Runtime配置
        :type RuntimeConfig: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        :param _NodesNum: 节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type NodesNum: int
        """
        self._RuntimeConfig = None
        self._NodesNum = None

    @property
    def RuntimeConfig(self):
        return self._RuntimeConfig

    @RuntimeConfig.setter
    def RuntimeConfig(self, RuntimeConfig):
        self._RuntimeConfig = RuntimeConfig

    @property
    def NodesNum(self):
        return self._NodesNum

    @NodesNum.setter
    def NodesNum(self, NodesNum):
        self._NodesNum = NodesNum


    def _deserialize(self, params):
        if params.get("RuntimeConfig") is not None:
            self._RuntimeConfig = RuntimeConfig()
            self._RuntimeConfig._deserialize(params.get("RuntimeConfig"))
        self._NodesNum = params.get("NodesNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
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
        


class HealthCheckPolicy(AbstractModel):
    """健康检测规则

    """

    def __init__(self):
        r"""
        :param _Name: 健康检测策略名称
        :type Name: str
        :param _Rules: 健康检测策略规则列表
        :type Rules: list of HealthCheckPolicyRule
        """
        self._Name = None
        self._Rules = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = HealthCheckPolicyRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckPolicyBinding(AbstractModel):
    """健康检测策略和节点池的绑定关系

    """

    def __init__(self):
        r"""
        :param _Name: 健康检测策略名称
        :type Name: str
        :param _CreatedAt: 规则创建时间
        :type CreatedAt: str
        :param _NodePools: 关联节点池数组
        :type NodePools: list of str
        """
        self._Name = None
        self._CreatedAt = None
        self._NodePools = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def NodePools(self):
        return self._NodePools

    @NodePools.setter
    def NodePools(self, NodePools):
        self._NodePools = NodePools


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CreatedAt = params.get("CreatedAt")
        self._NodePools = params.get("NodePools")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckPolicyRule(AbstractModel):
    """健康检测规则

    """

    def __init__(self):
        r"""
        :param _Name: 健康检测规则
        :type Name: str
        :param _Enabled: 是否检测此项目
        :type Enabled: bool
        :param _AutoRepairEnabled: 是否启用修复
        :type AutoRepairEnabled: bool
        """
        self._Name = None
        self._Enabled = None
        self._AutoRepairEnabled = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def AutoRepairEnabled(self):
        return self._AutoRepairEnabled

    @AutoRepairEnabled.setter
    def AutoRepairEnabled(self, AutoRepairEnabled):
        self._AutoRepairEnabled = AutoRepairEnabled


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Enabled = params.get("Enabled")
        self._AutoRepairEnabled = params.get("AutoRepairEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckTemplate(AbstractModel):
    """健康检测模板

    """

    def __init__(self):
        r"""
        :param _Rules: 健康检测项
        :type Rules: list of HealthCheckTemplateRule
        """
        self._Rules = None

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = HealthCheckTemplateRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckTemplateRule(AbstractModel):
    """健康检测模板规则

    """

    def __init__(self):
        r"""
        :param _Name: 健康检测项目名称
        :type Name: str
        :param _Description: 健康检测规则描述
        :type Description: str
        :param _RepairAction: 修复动作
        :type RepairAction: str
        :param _RepairEffect: 修复影响
        :type RepairEffect: str
        :param _ShouldEnable: 是否建议开启检测
        :type ShouldEnable: bool
        :param _ShouldRepair: 是否建议修复
        :type ShouldRepair: bool
        :param _Severity: 问题严重程度
        :type Severity: str
        """
        self._Name = None
        self._Description = None
        self._RepairAction = None
        self._RepairEffect = None
        self._ShouldEnable = None
        self._ShouldRepair = None
        self._Severity = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RepairAction(self):
        return self._RepairAction

    @RepairAction.setter
    def RepairAction(self, RepairAction):
        self._RepairAction = RepairAction

    @property
    def RepairEffect(self):
        return self._RepairEffect

    @RepairEffect.setter
    def RepairEffect(self, RepairEffect):
        self._RepairEffect = RepairEffect

    @property
    def ShouldEnable(self):
        return self._ShouldEnable

    @ShouldEnable.setter
    def ShouldEnable(self, ShouldEnable):
        self._ShouldEnable = ShouldEnable

    @property
    def ShouldRepair(self):
        return self._ShouldRepair

    @ShouldRepair.setter
    def ShouldRepair(self, ShouldRepair):
        self._ShouldRepair = ShouldRepair

    @property
    def Severity(self):
        return self._Severity

    @Severity.setter
    def Severity(self, Severity):
        self._Severity = Severity


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._RepairAction = params.get("RepairAction")
        self._RepairEffect = params.get("RepairEffect")
        self._ShouldEnable = params.get("ShouldEnable")
        self._ShouldRepair = params.get("ShouldRepair")
        self._Severity = params.get("Severity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Instance(AbstractModel):
    """集群的实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceRole: 节点角色, MASTER, WORKER, ETCD, MASTER_ETCD,ALL, 默认为WORKER
        :type InstanceRole: str
        :param _FailedReason: 实例异常(或者处于初始化中)的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedReason: str
        :param _InstanceState: 实例的状态
- initializing创建中
- running 运行中
- failed 异常
        :type InstanceState: str
        :param _Unschedulable: 是否不可调度
注意：此字段可能返回 null，表示取不到有效值。
        :type Unschedulable: bool
        :param _CreatedTime: 添加时间
        :type CreatedTime: str
        :param _LanIP: 节点内网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LanIP: str
        :param _NodePoolId: 资源池ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolId: str
        :param _Native: 原生节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Native: :class:`tencentcloud.tke.v20220501.models.NativeNodeInfo`
        :param _Regular: 普通节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Regular: :class:`tencentcloud.tke.v20220501.models.RegularNodeInfo`
        :param _Super: 超级节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Super: :class:`tencentcloud.tke.v20220501.models.SuperNodeInfo`
        :param _External: 第三方节点参数
注意：此字段可能返回 null，表示取不到有效值。
        :type External: :class:`tencentcloud.tke.v20220501.models.ExternalNodeInfo`
        :param _NodeType: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        """
        self._InstanceId = None
        self._InstanceRole = None
        self._FailedReason = None
        self._InstanceState = None
        self._Unschedulable = None
        self._CreatedTime = None
        self._LanIP = None
        self._NodePoolId = None
        self._Native = None
        self._Regular = None
        self._Super = None
        self._External = None
        self._NodeType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceRole(self):
        return self._InstanceRole

    @InstanceRole.setter
    def InstanceRole(self, InstanceRole):
        self._InstanceRole = InstanceRole

    @property
    def FailedReason(self):
        return self._FailedReason

    @FailedReason.setter
    def FailedReason(self, FailedReason):
        self._FailedReason = FailedReason

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def LanIP(self):
        return self._LanIP

    @LanIP.setter
    def LanIP(self, LanIP):
        self._LanIP = LanIP

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Native(self):
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Regular(self):
        return self._Regular

    @Regular.setter
    def Regular(self, Regular):
        self._Regular = Regular

    @property
    def Super(self):
        return self._Super

    @Super.setter
    def Super(self, Super):
        self._Super = Super

    @property
    def External(self):
        return self._External

    @External.setter
    def External(self, External):
        self._External = External

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceRole = params.get("InstanceRole")
        self._FailedReason = params.get("FailedReason")
        self._InstanceState = params.get("InstanceState")
        self._Unschedulable = params.get("Unschedulable")
        self._CreatedTime = params.get("CreatedTime")
        self._LanIP = params.get("LanIP")
        self._NodePoolId = params.get("NodePoolId")
        if params.get("Native") is not None:
            self._Native = NativeNodeInfo()
            self._Native._deserialize(params.get("Native"))
        if params.get("Regular") is not None:
            self._Regular = RegularNodeInfo()
            self._Regular._deserialize(params.get("Regular"))
        if params.get("Super") is not None:
            self._Super = SuperNodeInfo()
            self._Super._deserialize(params.get("Super"))
        if params.get("External") is not None:
            self._External = ExternalNodeInfo()
            self._External._deserialize(params.get("External"))
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceAdvancedSettings(AbstractModel):
    """描述了k8s集群相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _DesiredPodNumber: 该节点属于podCIDR大小自定义模式时，可指定节点上运行的pod数量上限
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredPodNumber: int
        :param _PreStartUserScript: base64 编码的用户脚本，在初始化节点之前执行，目前只对添加已有节点生效
注意：此字段可能返回 null，表示取不到有效值。
        :type PreStartUserScript: str
        :param _RuntimeConfig: 运行时描述
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeConfig: :class:`tencentcloud.tke.v20220501.models.RuntimeConfig`
        :param _UserScript: base64 编码的用户脚本, 此脚本会在 k8s 组件运行后执行, 需要用户保证脚本的可重入及重试逻辑, 脚本及其生成的日志文件可在节点的 /data/ccs_userscript/ 路径查看, 如果要求节点需要在进行初始化完成后才可加入调度, 可配合 unschedulable 参数使用, 在 userScript 最后初始化完成后, 添加 kubectl uncordon nodename --kubeconfig=/root/.kube/config 命令使节点加入调度
注意：此字段可能返回 null，表示取不到有效值。
        :type UserScript: str
        :param _ExtraArgs: 节点相关的自定义参数信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraArgs: :class:`tencentcloud.tke.v20220501.models.InstanceExtraArgs`
        """
        self._DesiredPodNumber = None
        self._PreStartUserScript = None
        self._RuntimeConfig = None
        self._UserScript = None
        self._ExtraArgs = None

    @property
    def DesiredPodNumber(self):
        return self._DesiredPodNumber

    @DesiredPodNumber.setter
    def DesiredPodNumber(self, DesiredPodNumber):
        self._DesiredPodNumber = DesiredPodNumber

    @property
    def PreStartUserScript(self):
        return self._PreStartUserScript

    @PreStartUserScript.setter
    def PreStartUserScript(self, PreStartUserScript):
        self._PreStartUserScript = PreStartUserScript

    @property
    def RuntimeConfig(self):
        return self._RuntimeConfig

    @RuntimeConfig.setter
    def RuntimeConfig(self, RuntimeConfig):
        self._RuntimeConfig = RuntimeConfig

    @property
    def UserScript(self):
        return self._UserScript

    @UserScript.setter
    def UserScript(self, UserScript):
        self._UserScript = UserScript

    @property
    def ExtraArgs(self):
        return self._ExtraArgs

    @ExtraArgs.setter
    def ExtraArgs(self, ExtraArgs):
        self._ExtraArgs = ExtraArgs


    def _deserialize(self, params):
        self._DesiredPodNumber = params.get("DesiredPodNumber")
        self._PreStartUserScript = params.get("PreStartUserScript")
        if params.get("RuntimeConfig") is not None:
            self._RuntimeConfig = RuntimeConfig()
            self._RuntimeConfig._deserialize(params.get("RuntimeConfig"))
        self._UserScript = params.get("UserScript")
        if params.get("ExtraArgs") is not None:
            self._ExtraArgs = InstanceExtraArgs()
            self._ExtraArgs._deserialize(params.get("ExtraArgs"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """包年包月配置

    """

    def __init__(self):
        r"""
        :param _Period: 后付费计费周期，单位（月）：
1，2，3，4，5，，6，7， 8，9，10，11，12，24，36，48，60
        :type Period: int
        :param _RenewFlag: 预付费续费方式：
- NOTIFY_AND_AUTO_RENEW：通知用户过期，且自动续费 (默认）
- NOTIFY_AND_MANUAL_RENEW：通知用户过期，但不自动续费
- DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知用户过期，也不自动续费

        :type RenewFlag: str
        """
        self._Period = None
        self._RenewFlag = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceExtraArgs(AbstractModel):
    """节点自定义参数

    """

    def __init__(self):
        r"""
        :param _Kubelet: kubelet自定义参数，参数格式为["k1=v1", "k1=v2"]， 例如["root-dir=/var/lib/kubelet","feature-gates=PodShareProcessNamespace=true,DynamicKubeletConfig=true"]
注意：此字段可能返回 null，表示取不到有效值。
        :type Kubelet: list of str
        """
        self._Kubelet = None

    @property
    def Kubelet(self):
        return self._Kubelet

    @Kubelet.setter
    def Kubelet(self, Kubelet):
        self._Kubelet = Kubelet


    def _deserialize(self, params):
        self._Kubelet = params.get("Kubelet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntOrString(AbstractModel):
    """数值结构

    """

    def __init__(self):
        r"""
        :param _Type: 数值类型，0是int,  1是字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param _IntVal: 整数
注意：此字段可能返回 null，表示取不到有效值。
        :type IntVal: int
        :param _StrVal: 字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type StrVal: str
        """
        self._Type = None
        self._IntVal = None
        self._StrVal = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IntVal(self):
        return self._IntVal

    @IntVal.setter
    def IntVal(self, IntVal):
        self._IntVal = IntVal

    @property
    def StrVal(self):
        return self._StrVal

    @StrVal.setter
    def StrVal(self, StrVal):
        self._StrVal = StrVal


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._IntVal = params.get("IntVal")
        self._StrVal = params.get("StrVal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """公网带宽

    """

    def __init__(self):
        r"""
        :param _MaxBandwidthOut: 带宽
        :type MaxBandwidthOut: int
        :param _ChargeType: 网络计费方式
        :type ChargeType: str
        :param _BandwidthPackageId: 带宽包 ID
        :type BandwidthPackageId: str
        """
        self._MaxBandwidthOut = None
        self._ChargeType = None
        self._BandwidthPackageId = None

    @property
    def MaxBandwidthOut(self):
        return self._MaxBandwidthOut

    @MaxBandwidthOut.setter
    def MaxBandwidthOut(self, MaxBandwidthOut):
        self._MaxBandwidthOut = MaxBandwidthOut

    @property
    def ChargeType(self):
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def BandwidthPackageId(self):
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._MaxBandwidthOut = params.get("MaxBandwidthOut")
        self._ChargeType = params.get("ChargeType")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Label(AbstractModel):
    """k8s中标签，一般以数组的方式存在

    """

    def __init__(self):
        r"""
        :param _Name: map表中的Name
        :type Name: str
        :param _Value: map表中的Value
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleConfig(AbstractModel):
    """节点池自定义脚本

    """

    def __init__(self):
        r"""
        :param _PreInit: 节点初始化前自定义脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type PreInit: str
        :param _PostInit: 节点初始化后自定义脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type PostInit: str
        """
        self._PreInit = None
        self._PostInit = None

    @property
    def PreInit(self):
        return self._PreInit

    @PreInit.setter
    def PreInit(self, PreInit):
        self._PreInit = PreInit

    @property
    def PostInit(self):
        return self._PostInit

    @PostInit.setter
    def PostInit(self, PostInit):
        self._PostInit = PostInit


    def _deserialize(self, params):
        self._PreInit = params.get("PreInit")
        self._PostInit = params.get("PostInit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineSetScaling(AbstractModel):
    """节点池弹性伸缩配置

    """

    def __init__(self):
        r"""
        :param _MinReplicas: 节点池最小副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinReplicas: int
        :param _MaxReplicas: 节点池最大副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param _CreatePolicy: 节点池扩容策略。ZoneEquality：多可用区打散；ZonePriority：首选可用区优先；
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatePolicy: str
        """
        self._MinReplicas = None
        self._MaxReplicas = None
        self._CreatePolicy = None

    @property
    def MinReplicas(self):
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def CreatePolicy(self):
        return self._CreatePolicy

    @CreatePolicy.setter
    def CreatePolicy(self, CreatePolicy):
        self._CreatePolicy = CreatePolicy


    def _deserialize(self, params):
        self._MinReplicas = params.get("MinReplicas")
        self._MaxReplicas = params.get("MaxReplicas")
        self._CreatePolicy = params.get("CreatePolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MachineUpgradeSettings(AbstractModel):
    """托管节点池自动升级配置

    """

    def __init__(self):
        r"""
        :param _AutoUpgrade: 是否开启自动升级
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoUpgrade: bool
        :param _UpgradeOptions: 运维窗口
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeOptions: :class:`tencentcloud.tke.v20220501.models.AutoUpgradeOptions`
        :param _Components: 升级项
注意：此字段可能返回 null，表示取不到有效值。
        :type Components: list of str
        :param _MaxUnavailable: 升级时，最大不可升级的节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxUnavailable: :class:`tencentcloud.tke.v20220501.models.IntOrString`
        """
        self._AutoUpgrade = None
        self._UpgradeOptions = None
        self._Components = None
        self._MaxUnavailable = None

    @property
    def AutoUpgrade(self):
        return self._AutoUpgrade

    @AutoUpgrade.setter
    def AutoUpgrade(self, AutoUpgrade):
        self._AutoUpgrade = AutoUpgrade

    @property
    def UpgradeOptions(self):
        return self._UpgradeOptions

    @UpgradeOptions.setter
    def UpgradeOptions(self, UpgradeOptions):
        self._UpgradeOptions = UpgradeOptions

    @property
    def Components(self):
        return self._Components

    @Components.setter
    def Components(self, Components):
        self._Components = Components

    @property
    def MaxUnavailable(self):
        return self._MaxUnavailable

    @MaxUnavailable.setter
    def MaxUnavailable(self, MaxUnavailable):
        self._MaxUnavailable = MaxUnavailable


    def _deserialize(self, params):
        self._AutoUpgrade = params.get("AutoUpgrade")
        if params.get("UpgradeOptions") is not None:
            self._UpgradeOptions = AutoUpgradeOptions()
            self._UpgradeOptions._deserialize(params.get("UpgradeOptions"))
        self._Components = params.get("Components")
        if params.get("MaxUnavailable") is not None:
            self._MaxUnavailable = IntOrString()
            self._MaxUnavailable._deserialize(params.get("MaxUnavailable"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagementConfig(AbstractModel):
    """托管节点池Management配置

    """

    def __init__(self):
        r"""
        :param _Nameservers: dns 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Nameservers: list of str
        :param _Hosts: hosts 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Hosts: list of str
        :param _KernelArgs: 内核参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type KernelArgs: list of str
        """
        self._Nameservers = None
        self._Hosts = None
        self._KernelArgs = None

    @property
    def Nameservers(self):
        return self._Nameservers

    @Nameservers.setter
    def Nameservers(self, Nameservers):
        self._Nameservers = Nameservers

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def KernelArgs(self):
        return self._KernelArgs

    @KernelArgs.setter
    def KernelArgs(self, KernelArgs):
        self._KernelArgs = KernelArgs


    def _deserialize(self, params):
        self._Nameservers = params.get("Nameservers")
        self._Hosts = params.get("Hosts")
        self._KernelArgs = params.get("KernelArgs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManuallyAdded(AbstractModel):
    """手动加入的节点

    """

    def __init__(self):
        r"""
        :param _Joining: 加入中的节点数量
        :type Joining: int
        :param _Initializing: 初始化中的节点数量
        :type Initializing: int
        :param _Normal: 正常的节点数量
        :type Normal: int
        :param _Total: 节点总数
        :type Total: int
        """
        self._Joining = None
        self._Initializing = None
        self._Normal = None
        self._Total = None

    @property
    def Joining(self):
        return self._Joining

    @Joining.setter
    def Joining(self, Joining):
        self._Joining = Joining

    @property
    def Initializing(self):
        return self._Initializing

    @Initializing.setter
    def Initializing(self, Initializing):
        self._Initializing = Initializing

    @property
    def Normal(self):
        return self._Normal

    @Normal.setter
    def Normal(self, Normal):
        self._Normal = Normal

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._Joining = params.get("Joining")
        self._Initializing = params.get("Initializing")
        self._Normal = params.get("Normal")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckPolicyRequest(AbstractModel):
    """ModifyHealthCheckPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _HealthCheckPolicy: 健康检测策略
        :type HealthCheckPolicy: :class:`tencentcloud.tke.v20220501.models.HealthCheckPolicy`
        """
        self._ClusterId = None
        self._HealthCheckPolicy = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def HealthCheckPolicy(self):
        return self._HealthCheckPolicy

    @HealthCheckPolicy.setter
    def HealthCheckPolicy(self, HealthCheckPolicy):
        self._HealthCheckPolicy = HealthCheckPolicy


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("HealthCheckPolicy") is not None:
            self._HealthCheckPolicy = HealthCheckPolicy()
            self._HealthCheckPolicy._deserialize(params.get("HealthCheckPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckPolicyResponse(AbstractModel):
    """ModifyHealthCheckPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNodePoolRequest(AbstractModel):
    """ModifyNodePool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _NodePoolId: 节点池 ID
        :type NodePoolId: str
        :param _Name: 节点池名称
        :type Name: str
        :param _Labels: 节点  Labels
        :type Labels: list of Label
        :param _Taints: 节点污点
        :type Taints: list of Taint
        :param _Tags: 节点标签
        :type Tags: list of TagSpecification
        :param _DeletionProtection: 是否开启删除保护
        :type DeletionProtection: bool
        :param _Unschedulable: 节点是否不可调度
        :type Unschedulable: bool
        :param _Native: 原生节点池更新参数
        :type Native: :class:`tencentcloud.tke.v20220501.models.UpdateNativeNodePoolParam`
        :param _Annotations: 节点 Annotation 列表
        :type Annotations: list of Annotation
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Name = None
        self._Labels = None
        self._Taints = None
        self._Tags = None
        self._DeletionProtection = None
        self._Unschedulable = None
        self._Native = None
        self._Annotations = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Native(self):
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        self._Name = params.get("Name")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Unschedulable = params.get("Unschedulable")
        if params.get("Native") is not None:
            self._Native = UpdateNativeNodePoolParam()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodePoolResponse(AbstractModel):
    """ModifyNodePool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NativeNodeInfo(AbstractModel):
    """节点信息

    """

    def __init__(self):
        r"""
        :param _MachineName: 节点名称
        :type MachineName: str
        :param _MachineState: Machine 状态
        :type MachineState: str
        :param _Zone: Machine 所在可用区
        :type Zone: str
        :param _InstanceChargeType: 节点计费类型。PREPAID：包年包月；POSTPAID_BY_HOUR：按量计费（默认）；
        :type InstanceChargeType: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _LoginStatus: Machine 登录状态
注意：此字段可能返回 null，表示取不到有效值。
        :type LoginStatus: str
        :param _IsProtectedFromScaleIn: 是否开启缩容保护
注意：此字段可能返回 null，表示取不到有效值。
        :type IsProtectedFromScaleIn: bool
        :param _DisplayName: Machine 名字
注意：此字段可能返回 null，表示取不到有效值。
        :type DisplayName: str
        :param _CPU: CPU核数，单位：核
        :type CPU: int
        :param _GPU: GPU核数，单位：核
注意：此字段可能返回 null，表示取不到有效值。
        :type GPU: int
        :param _RenewFlag: 自动续费标识
        :type RenewFlag: str
        :param _PayMode: 节点计费模式（已弃用）
        :type PayMode: str
        :param _Memory: 节点内存容量，单位：`GB`
        :type Memory: int
        :param _InternetAccessible: 公网带宽相关信息设置
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _InstanceFamily: 机型所属机型族
        :type InstanceFamily: str
        :param _LanIp: 节点内网 IP
        :type LanIp: str
        :param _InstanceType: 机型
        :type InstanceType: str
        :param _ExpiredTime: 包年包月节点计费过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _SecurityGroupIDs: 安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIDs: list of str
        :param _VpcId: VPC 唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _OsImage: OS的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OsImage: str
        """
        self._MachineName = None
        self._MachineState = None
        self._Zone = None
        self._InstanceChargeType = None
        self._CreatedAt = None
        self._LoginStatus = None
        self._IsProtectedFromScaleIn = None
        self._DisplayName = None
        self._CPU = None
        self._GPU = None
        self._RenewFlag = None
        self._PayMode = None
        self._Memory = None
        self._InternetAccessible = None
        self._InstanceFamily = None
        self._LanIp = None
        self._InstanceType = None
        self._ExpiredTime = None
        self._SecurityGroupIDs = None
        self._VpcId = None
        self._SubnetId = None
        self._OsImage = None

    @property
    def MachineName(self):
        return self._MachineName

    @MachineName.setter
    def MachineName(self, MachineName):
        self._MachineName = MachineName

    @property
    def MachineState(self):
        return self._MachineState

    @MachineState.setter
    def MachineState(self, MachineState):
        self._MachineState = MachineState

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def LoginStatus(self):
        return self._LoginStatus

    @LoginStatus.setter
    def LoginStatus(self, LoginStatus):
        self._LoginStatus = LoginStatus

    @property
    def IsProtectedFromScaleIn(self):
        return self._IsProtectedFromScaleIn

    @IsProtectedFromScaleIn.setter
    def IsProtectedFromScaleIn(self, IsProtectedFromScaleIn):
        self._IsProtectedFromScaleIn = IsProtectedFromScaleIn

    @property
    def DisplayName(self):
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def GPU(self):
        return self._GPU

    @GPU.setter
    def GPU(self, GPU):
        self._GPU = GPU

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceFamily(self):
        return self._InstanceFamily

    @InstanceFamily.setter
    def InstanceFamily(self, InstanceFamily):
        self._InstanceFamily = InstanceFamily

    @property
    def LanIp(self):
        return self._LanIp

    @LanIp.setter
    def LanIp(self, LanIp):
        self._LanIp = LanIp

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def SecurityGroupIDs(self):
        return self._SecurityGroupIDs

    @SecurityGroupIDs.setter
    def SecurityGroupIDs(self, SecurityGroupIDs):
        self._SecurityGroupIDs = SecurityGroupIDs

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def OsImage(self):
        return self._OsImage

    @OsImage.setter
    def OsImage(self, OsImage):
        self._OsImage = OsImage


    def _deserialize(self, params):
        self._MachineName = params.get("MachineName")
        self._MachineState = params.get("MachineState")
        self._Zone = params.get("Zone")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._CreatedAt = params.get("CreatedAt")
        self._LoginStatus = params.get("LoginStatus")
        self._IsProtectedFromScaleIn = params.get("IsProtectedFromScaleIn")
        self._DisplayName = params.get("DisplayName")
        self._CPU = params.get("CPU")
        self._GPU = params.get("GPU")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._Memory = params.get("Memory")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceFamily = params.get("InstanceFamily")
        self._LanIp = params.get("LanIp")
        self._InstanceType = params.get("InstanceType")
        self._ExpiredTime = params.get("ExpiredTime")
        self._SecurityGroupIDs = params.get("SecurityGroupIDs")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._OsImage = params.get("OsImage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeNodePoolInfo(AbstractModel):
    """原生节点池信息

    """

    def __init__(self):
        r"""
        :param _Scaling: 伸缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Scaling: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        :param _SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param _SecurityGroupIds: 安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        :param _UpgradeSettings: 自动升级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UpgradeSettings: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        :param _AutoRepair: 是否开启自愈能力
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRepair: bool
        :param _InstanceChargeType: 节点计费类型
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 包年包月机型计费配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        :param _SystemDisk: 系统盘配置
        :type SystemDisk: :class:`tencentcloud.tke.v20220501.models.Disk`
        :param _KeyIds: 密钥 ID 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyIds: list of str
        :param _Management: Machine 系统配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Management: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        :param _HealthCheckPolicyName: 故障自愈规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckPolicyName: str
        :param _HostNamePattern: 原生节点池hostName模式串
注意：此字段可能返回 null，表示取不到有效值。
        :type HostNamePattern: str
        :param _KubeletArgs: kubelet 自定义参数
注意：此字段可能返回 null，表示取不到有效值。
        :type KubeletArgs: list of str
        :param _Lifecycle: 预定义脚本
注意：此字段可能返回 null，表示取不到有效值。
        :type Lifecycle: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        :param _RuntimeRootDir: 运行时根目录
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeRootDir: str
        :param _EnableAutoscaling: 是否开启弹性伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableAutoscaling: bool
        :param _InstanceTypes: 机型列表
        :type InstanceTypes: list of str
        :param _Replicas: 期望节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param _ReadyReplicas: 就绪 Machine 个数
        :type ReadyReplicas: int
        :param _InternetAccessible: 公网带宽设置
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAccessible: :class:`tencentcloud.tke.v20220501.models.InternetAccessible`
        :param _DataDisks: 原生节点池数据盘
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        """
        self._Scaling = None
        self._SubnetIds = None
        self._SecurityGroupIds = None
        self._UpgradeSettings = None
        self._AutoRepair = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._SystemDisk = None
        self._KeyIds = None
        self._Management = None
        self._HealthCheckPolicyName = None
        self._HostNamePattern = None
        self._KubeletArgs = None
        self._Lifecycle = None
        self._RuntimeRootDir = None
        self._EnableAutoscaling = None
        self._InstanceTypes = None
        self._Replicas = None
        self._ReadyReplicas = None
        self._InternetAccessible = None
        self._DataDisks = None

    @property
    def Scaling(self):
        return self._Scaling

    @Scaling.setter
    def Scaling(self, Scaling):
        self._Scaling = Scaling

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeSettings(self):
        return self._UpgradeSettings

    @UpgradeSettings.setter
    def UpgradeSettings(self, UpgradeSettings):
        self._UpgradeSettings = UpgradeSettings

    @property
    def AutoRepair(self):
        return self._AutoRepair

    @AutoRepair.setter
    def AutoRepair(self, AutoRepair):
        self._AutoRepair = AutoRepair

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds

    @property
    def Management(self):
        return self._Management

    @Management.setter
    def Management(self, Management):
        self._Management = Management

    @property
    def HealthCheckPolicyName(self):
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def HostNamePattern(self):
        return self._HostNamePattern

    @HostNamePattern.setter
    def HostNamePattern(self, HostNamePattern):
        self._HostNamePattern = HostNamePattern

    @property
    def KubeletArgs(self):
        return self._KubeletArgs

    @KubeletArgs.setter
    def KubeletArgs(self, KubeletArgs):
        self._KubeletArgs = KubeletArgs

    @property
    def Lifecycle(self):
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def RuntimeRootDir(self):
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir

    @property
    def EnableAutoscaling(self):
        return self._EnableAutoscaling

    @EnableAutoscaling.setter
    def EnableAutoscaling(self, EnableAutoscaling):
        self._EnableAutoscaling = EnableAutoscaling

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def ReadyReplicas(self):
        return self._ReadyReplicas

    @ReadyReplicas.setter
    def ReadyReplicas(self, ReadyReplicas):
        self._ReadyReplicas = ReadyReplicas

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks


    def _deserialize(self, params):
        if params.get("Scaling") is not None:
            self._Scaling = MachineSetScaling()
            self._Scaling._deserialize(params.get("Scaling"))
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeSettings") is not None:
            self._UpgradeSettings = MachineUpgradeSettings()
            self._UpgradeSettings._deserialize(params.get("UpgradeSettings"))
        self._AutoRepair = params.get("AutoRepair")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._KeyIds = params.get("KeyIds")
        if params.get("Management") is not None:
            self._Management = ManagementConfig()
            self._Management._deserialize(params.get("Management"))
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._HostNamePattern = params.get("HostNamePattern")
        self._KubeletArgs = params.get("KubeletArgs")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifecycleConfig()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        self._EnableAutoscaling = params.get("EnableAutoscaling")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Replicas = params.get("Replicas")
        self._ReadyReplicas = params.get("ReadyReplicas")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
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
        


class NodeCountSummary(AbstractModel):
    """节点统计列表

    """

    def __init__(self):
        r"""
        :param _ManuallyAdded: 手动管理的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ManuallyAdded: :class:`tencentcloud.tke.v20220501.models.ManuallyAdded`
        :param _AutoscalingAdded: 自动管理的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingAdded: :class:`tencentcloud.tke.v20220501.models.AutoscalingAdded`
        """
        self._ManuallyAdded = None
        self._AutoscalingAdded = None

    @property
    def ManuallyAdded(self):
        return self._ManuallyAdded

    @ManuallyAdded.setter
    def ManuallyAdded(self, ManuallyAdded):
        self._ManuallyAdded = ManuallyAdded

    @property
    def AutoscalingAdded(self):
        return self._AutoscalingAdded

    @AutoscalingAdded.setter
    def AutoscalingAdded(self, AutoscalingAdded):
        self._AutoscalingAdded = AutoscalingAdded


    def _deserialize(self, params):
        if params.get("ManuallyAdded") is not None:
            self._ManuallyAdded = ManuallyAdded()
            self._ManuallyAdded._deserialize(params.get("ManuallyAdded"))
        if params.get("AutoscalingAdded") is not None:
            self._AutoscalingAdded = AutoscalingAdded()
            self._AutoscalingAdded._deserialize(params.get("AutoscalingAdded"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodePool(AbstractModel):
    """节点池信息

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群 ID
        :type ClusterId: str
        :param _NodePoolId: 节点池 ID
        :type NodePoolId: str
        :param _Tags: 节点标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagSpecification
        :param _Taints: 节点污点
注意：此字段可能返回 null，表示取不到有效值。
        :type Taints: list of Taint
        :param _DeletionProtection: 是否开启删除保护
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionProtection: bool
        :param _Unschedulable: 节点是否不可调度
注意：此字段可能返回 null，表示取不到有效值。
        :type Unschedulable: bool
        :param _Type: 节点池类型
        :type Type: str
        :param _Labels: 节点  Labels
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of Label
        :param _LifeState: 节点池状态
        :type LifeState: str
        :param _CreatedAt: 创建时间
        :type CreatedAt: str
        :param _Name: 节点池名称
        :type Name: str
        :param _Native: 原生节点池参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Native: :class:`tencentcloud.tke.v20220501.models.NativeNodePoolInfo`
        :param _Annotations: 节点 Annotation 列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotations: list of Annotation
        :param _Super: 超级节点池参数，在Type等于Super该字段才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type Super: :class:`tencentcloud.tke.v20220501.models.SuperNodePoolInfo`
        :param _Regular: 普通节点池参数，在Type等于Regular该字段才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type Regular: :class:`tencentcloud.tke.v20220501.models.RegularNodePoolInfo`
        :param _External: 第三方节点池参数，在Type等于External该字段才有值
注意：此字段可能返回 null，表示取不到有效值。
        :type External: :class:`tencentcloud.tke.v20220501.models.ExternalNodePoolInfo`
        """
        self._ClusterId = None
        self._NodePoolId = None
        self._Tags = None
        self._Taints = None
        self._DeletionProtection = None
        self._Unschedulable = None
        self._Type = None
        self._Labels = None
        self._LifeState = None
        self._CreatedAt = None
        self._Name = None
        self._Native = None
        self._Annotations = None
        self._Super = None
        self._Regular = None
        self._External = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodePoolId(self):
        return self._NodePoolId

    @NodePoolId.setter
    def NodePoolId(self, NodePoolId):
        self._NodePoolId = NodePoolId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Taints(self):
        return self._Taints

    @Taints.setter
    def Taints(self, Taints):
        self._Taints = Taints

    @property
    def DeletionProtection(self):
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Unschedulable(self):
        return self._Unschedulable

    @Unschedulable.setter
    def Unschedulable(self, Unschedulable):
        self._Unschedulable = Unschedulable

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def LifeState(self):
        return self._LifeState

    @LifeState.setter
    def LifeState(self, LifeState):
        self._LifeState = LifeState

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Native(self):
        return self._Native

    @Native.setter
    def Native(self, Native):
        self._Native = Native

    @property
    def Annotations(self):
        return self._Annotations

    @Annotations.setter
    def Annotations(self, Annotations):
        self._Annotations = Annotations

    @property
    def Super(self):
        return self._Super

    @Super.setter
    def Super(self, Super):
        self._Super = Super

    @property
    def Regular(self):
        return self._Regular

    @Regular.setter
    def Regular(self, Regular):
        self._Regular = Regular

    @property
    def External(self):
        return self._External

    @External.setter
    def External(self, External):
        self._External = External


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodePoolId = params.get("NodePoolId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagSpecification()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("Taints") is not None:
            self._Taints = []
            for item in params.get("Taints"):
                obj = Taint()
                obj._deserialize(item)
                self._Taints.append(obj)
        self._DeletionProtection = params.get("DeletionProtection")
        self._Unschedulable = params.get("Unschedulable")
        self._Type = params.get("Type")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self._Labels.append(obj)
        self._LifeState = params.get("LifeState")
        self._CreatedAt = params.get("CreatedAt")
        self._Name = params.get("Name")
        if params.get("Native") is not None:
            self._Native = NativeNodePoolInfo()
            self._Native._deserialize(params.get("Native"))
        if params.get("Annotations") is not None:
            self._Annotations = []
            for item in params.get("Annotations"):
                obj = Annotation()
                obj._deserialize(item)
                self._Annotations.append(obj)
        if params.get("Super") is not None:
            self._Super = SuperNodePoolInfo()
            self._Super._deserialize(params.get("Super"))
        if params.get("Regular") is not None:
            self._Regular = RegularNodePoolInfo()
            self._Regular._deserialize(params.get("Regular"))
        if params.get("External") is not None:
            self._External = ExternalNodePoolInfo()
            self._External._deserialize(params.get("External"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegularNodeInfo(AbstractModel):
    """普通节点信息

    """

    def __init__(self):
        r"""
        :param _InstanceAdvancedSettings: 节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        :param _AutoscalingGroupId: 自动伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupId: str
        """
        self._InstanceAdvancedSettings = None
        self._AutoscalingGroupId = None

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId


    def _deserialize(self, params):
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegularNodePoolInfo(AbstractModel):
    """普通节点池信息

    """

    def __init__(self):
        r"""
        :param _LaunchConfigurationId: LaunchConfigurationId 配置
        :type LaunchConfigurationId: str
        :param _AutoscalingGroupId: AutoscalingGroupId 分组id
        :type AutoscalingGroupId: str
        :param _NodeCountSummary: NodeCountSummary 节点列表
        :type NodeCountSummary: :class:`tencentcloud.tke.v20220501.models.NodeCountSummary`
        :param _AutoscalingGroupStatus: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoscalingGroupStatus: str
        :param _MaxNodesNum: 最大节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxNodesNum: int
        :param _MinNodesNum: 最小节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MinNodesNum: int
        :param _DesiredNodesNum: 期望的节点数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredNodesNum: int
        :param _NodePoolOs: 节点池osName
注意：此字段可能返回 null，表示取不到有效值。
        :type NodePoolOs: str
        :param _InstanceAdvancedSettings: 节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAdvancedSettings: :class:`tencentcloud.tke.v20220501.models.InstanceAdvancedSettings`
        """
        self._LaunchConfigurationId = None
        self._AutoscalingGroupId = None
        self._NodeCountSummary = None
        self._AutoscalingGroupStatus = None
        self._MaxNodesNum = None
        self._MinNodesNum = None
        self._DesiredNodesNum = None
        self._NodePoolOs = None
        self._InstanceAdvancedSettings = None

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def AutoscalingGroupId(self):
        return self._AutoscalingGroupId

    @AutoscalingGroupId.setter
    def AutoscalingGroupId(self, AutoscalingGroupId):
        self._AutoscalingGroupId = AutoscalingGroupId

    @property
    def NodeCountSummary(self):
        return self._NodeCountSummary

    @NodeCountSummary.setter
    def NodeCountSummary(self, NodeCountSummary):
        self._NodeCountSummary = NodeCountSummary

    @property
    def AutoscalingGroupStatus(self):
        return self._AutoscalingGroupStatus

    @AutoscalingGroupStatus.setter
    def AutoscalingGroupStatus(self, AutoscalingGroupStatus):
        self._AutoscalingGroupStatus = AutoscalingGroupStatus

    @property
    def MaxNodesNum(self):
        return self._MaxNodesNum

    @MaxNodesNum.setter
    def MaxNodesNum(self, MaxNodesNum):
        self._MaxNodesNum = MaxNodesNum

    @property
    def MinNodesNum(self):
        return self._MinNodesNum

    @MinNodesNum.setter
    def MinNodesNum(self, MinNodesNum):
        self._MinNodesNum = MinNodesNum

    @property
    def DesiredNodesNum(self):
        return self._DesiredNodesNum

    @DesiredNodesNum.setter
    def DesiredNodesNum(self, DesiredNodesNum):
        self._DesiredNodesNum = DesiredNodesNum

    @property
    def NodePoolOs(self):
        return self._NodePoolOs

    @NodePoolOs.setter
    def NodePoolOs(self, NodePoolOs):
        self._NodePoolOs = NodePoolOs

    @property
    def InstanceAdvancedSettings(self):
        return self._InstanceAdvancedSettings

    @InstanceAdvancedSettings.setter
    def InstanceAdvancedSettings(self, InstanceAdvancedSettings):
        self._InstanceAdvancedSettings = InstanceAdvancedSettings


    def _deserialize(self, params):
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._AutoscalingGroupId = params.get("AutoscalingGroupId")
        if params.get("NodeCountSummary") is not None:
            self._NodeCountSummary = NodeCountSummary()
            self._NodeCountSummary._deserialize(params.get("NodeCountSummary"))
        self._AutoscalingGroupStatus = params.get("AutoscalingGroupStatus")
        self._MaxNodesNum = params.get("MaxNodesNum")
        self._MinNodesNum = params.get("MinNodesNum")
        self._DesiredNodesNum = params.get("DesiredNodesNum")
        self._NodePoolOs = params.get("NodePoolOs")
        if params.get("InstanceAdvancedSettings") is not None:
            self._InstanceAdvancedSettings = InstanceAdvancedSettings()
            self._InstanceAdvancedSettings._deserialize(params.get("InstanceAdvancedSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeConfig(AbstractModel):
    """运行时配置

    """

    def __init__(self):
        r"""
        :param _RuntimeType: 运行时类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeType: str
        :param _RuntimeVersion: 运行时版本
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeVersion: str
        :param _RuntimeRootDir: 运行时根目录
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeRootDir: str
        """
        self._RuntimeType = None
        self._RuntimeVersion = None
        self._RuntimeRootDir = None

    @property
    def RuntimeType(self):
        return self._RuntimeType

    @RuntimeType.setter
    def RuntimeType(self, RuntimeType):
        self._RuntimeType = RuntimeType

    @property
    def RuntimeVersion(self):
        return self._RuntimeVersion

    @RuntimeVersion.setter
    def RuntimeVersion(self, RuntimeVersion):
        self._RuntimeVersion = RuntimeVersion

    @property
    def RuntimeRootDir(self):
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir


    def _deserialize(self, params):
        self._RuntimeType = params.get("RuntimeType")
        self._RuntimeVersion = params.get("RuntimeVersion")
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SortBy(AbstractModel):
    """排序信息

    """

    def __init__(self):
        r"""
        :param _FieldName: 排序指标
        :type FieldName: str
        :param _OrderType: 排序方式
        :type OrderType: str
        """
        self._FieldName = None
        self._OrderType = None

    @property
    def FieldName(self):
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._FieldName = params.get("FieldName")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperNodeInfo(AbstractModel):
    """超级节点信息

    """

    def __init__(self):
        r"""
        :param _Name: 实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _AutoRenewFlag: 自动续费标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _CPU: 节点的 CPU 规格，单位：核。
注意：此字段可能返回 null，表示取不到有效值。
        :type CPU: float
        :param _UsedCPU: 节点上 Pod 的 CPU总和，单位：核。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedCPU: float
        :param _Memory: 节点的内存规格，单位：Gi。
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: float
        :param _UsedMemory: 节点上 Pod 的内存总和，单位：Gi。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsedMemory: float
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _VpcId: VPC 唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网唯一 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ActiveAt: 生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveAt: str
        :param _ExpireAt: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireAt: str
        :param _MaxCPUScheduledPod: 可调度的单 Pod 最大 CPU 规格
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCPUScheduledPod: int
        :param _InstanceAttribute: 实例属性
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceAttribute: str
        """
        self._Name = None
        self._AutoRenewFlag = None
        self._ResourceType = None
        self._CPU = None
        self._UsedCPU = None
        self._Memory = None
        self._UsedMemory = None
        self._Zone = None
        self._VpcId = None
        self._SubnetId = None
        self._ActiveAt = None
        self._ExpireAt = None
        self._MaxCPUScheduledPod = None
        self._InstanceAttribute = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def CPU(self):
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def UsedCPU(self):
        return self._UsedCPU

    @UsedCPU.setter
    def UsedCPU(self, UsedCPU):
        self._UsedCPU = UsedCPU

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def UsedMemory(self):
        return self._UsedMemory

    @UsedMemory.setter
    def UsedMemory(self, UsedMemory):
        self._UsedMemory = UsedMemory

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ActiveAt(self):
        return self._ActiveAt

    @ActiveAt.setter
    def ActiveAt(self, ActiveAt):
        self._ActiveAt = ActiveAt

    @property
    def ExpireAt(self):
        return self._ExpireAt

    @ExpireAt.setter
    def ExpireAt(self, ExpireAt):
        self._ExpireAt = ExpireAt

    @property
    def MaxCPUScheduledPod(self):
        return self._MaxCPUScheduledPod

    @MaxCPUScheduledPod.setter
    def MaxCPUScheduledPod(self, MaxCPUScheduledPod):
        self._MaxCPUScheduledPod = MaxCPUScheduledPod

    @property
    def InstanceAttribute(self):
        return self._InstanceAttribute

    @InstanceAttribute.setter
    def InstanceAttribute(self, InstanceAttribute):
        self._InstanceAttribute = InstanceAttribute


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ResourceType = params.get("ResourceType")
        self._CPU = params.get("CPU")
        self._UsedCPU = params.get("UsedCPU")
        self._Memory = params.get("Memory")
        self._UsedMemory = params.get("UsedMemory")
        self._Zone = params.get("Zone")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._ActiveAt = params.get("ActiveAt")
        self._ExpireAt = params.get("ExpireAt")
        self._MaxCPUScheduledPod = params.get("MaxCPUScheduledPod")
        self._InstanceAttribute = params.get("InstanceAttribute")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuperNodePoolInfo(AbstractModel):
    """虚拟节点池信息

    """

    def __init__(self):
        r"""
        :param _SubnetIds: 子网列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _SecurityGroupIds: 安全组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityGroupIds: list of str
        """
        self._SubnetIds = None
        self._SecurityGroupIds = None

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签绑定的资源类型，当前支持类型："cluster"

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
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
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
        


class TagSpecification(AbstractModel):
    """标签描述列表。通过指定该参数可以同时绑定标签到相应的资源实例，当前仅支持绑定标签到云主机实例。

    """

    def __init__(self):
        r"""
        :param _ResourceType: 标签绑定的资源类型，当前支持类型："cluster"
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _Tags: 标签对列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ResourceType = None
        self._Tags = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Tags(self):
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
        


class Taint(AbstractModel):
    """kubernetes Taint

    """

    def __init__(self):
        r"""
        :param _Key: Taint的Key
        :type Key: str
        :param _Value: Taint的Value
        :type Value: str
        :param _Effect: Taint的Effect
        :type Effect: str
        """
        self._Key = None
        self._Value = None
        self._Effect = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._Effect = params.get("Effect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateNativeNodePoolParam(AbstractModel):
    """修改原生节点池参数

    """

    def __init__(self):
        r"""
        :param _Scaling: 伸缩配置
        :type Scaling: :class:`tencentcloud.tke.v20220501.models.MachineSetScaling`
        :param _SubnetIds: 子网列表
        :type SubnetIds: list of str
        :param _SecurityGroupIds: 安全组列表
        :type SecurityGroupIds: list of str
        :param _UpgradeSettings: 自动升级配置
        :type UpgradeSettings: :class:`tencentcloud.tke.v20220501.models.MachineUpgradeSettings`
        :param _AutoRepair: 是否开启自愈能力
        :type AutoRepair: bool
        :param _InstanceChargeType: 节点计费类型变更
当前仅支持按量计费转包年包月：
- PREPAID

        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 包年包月机型计费配置
        :type InstanceChargePrepaid: :class:`tencentcloud.tke.v20220501.models.InstanceChargePrepaid`
        :param _SystemDisk: 系统盘配置
        :type SystemDisk: :class:`tencentcloud.tke.v20220501.models.Disk`
        :param _Management: Machine 系统配置
        :type Management: :class:`tencentcloud.tke.v20220501.models.ManagementConfig`
        :param _HealthCheckPolicyName: 故障自愈规则名称
        :type HealthCheckPolicyName: str
        :param _HostNamePattern: 原生节点池hostName模式串
        :type HostNamePattern: str
        :param _KubeletArgs: kubelet 自定义参数
        :type KubeletArgs: list of str
        :param _Lifecycle: 预定义脚本
        :type Lifecycle: :class:`tencentcloud.tke.v20220501.models.LifecycleConfig`
        :param _RuntimeRootDir: 运行时根目录
        :type RuntimeRootDir: str
        :param _EnableAutoscaling: 是否开启弹性伸缩
        :type EnableAutoscaling: bool
        :param _InstanceTypes: 机型列表
        :type InstanceTypes: list of str
        :param _Replicas: 期望节点数
        :type Replicas: int
        :param _DataDisks: 数据盘列表
        :type DataDisks: list of DataDisk
        :param _KeyIds: ssh公钥id数组
        :type KeyIds: list of str
        """
        self._Scaling = None
        self._SubnetIds = None
        self._SecurityGroupIds = None
        self._UpgradeSettings = None
        self._AutoRepair = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._SystemDisk = None
        self._Management = None
        self._HealthCheckPolicyName = None
        self._HostNamePattern = None
        self._KubeletArgs = None
        self._Lifecycle = None
        self._RuntimeRootDir = None
        self._EnableAutoscaling = None
        self._InstanceTypes = None
        self._Replicas = None
        self._DataDisks = None
        self._KeyIds = None

    @property
    def Scaling(self):
        return self._Scaling

    @Scaling.setter
    def Scaling(self, Scaling):
        self._Scaling = Scaling

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def UpgradeSettings(self):
        return self._UpgradeSettings

    @UpgradeSettings.setter
    def UpgradeSettings(self, UpgradeSettings):
        self._UpgradeSettings = UpgradeSettings

    @property
    def AutoRepair(self):
        return self._AutoRepair

    @AutoRepair.setter
    def AutoRepair(self, AutoRepair):
        self._AutoRepair = AutoRepair

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def Management(self):
        return self._Management

    @Management.setter
    def Management(self, Management):
        self._Management = Management

    @property
    def HealthCheckPolicyName(self):
        return self._HealthCheckPolicyName

    @HealthCheckPolicyName.setter
    def HealthCheckPolicyName(self, HealthCheckPolicyName):
        self._HealthCheckPolicyName = HealthCheckPolicyName

    @property
    def HostNamePattern(self):
        return self._HostNamePattern

    @HostNamePattern.setter
    def HostNamePattern(self, HostNamePattern):
        self._HostNamePattern = HostNamePattern

    @property
    def KubeletArgs(self):
        return self._KubeletArgs

    @KubeletArgs.setter
    def KubeletArgs(self, KubeletArgs):
        self._KubeletArgs = KubeletArgs

    @property
    def Lifecycle(self):
        return self._Lifecycle

    @Lifecycle.setter
    def Lifecycle(self, Lifecycle):
        self._Lifecycle = Lifecycle

    @property
    def RuntimeRootDir(self):
        return self._RuntimeRootDir

    @RuntimeRootDir.setter
    def RuntimeRootDir(self, RuntimeRootDir):
        self._RuntimeRootDir = RuntimeRootDir

    @property
    def EnableAutoscaling(self):
        return self._EnableAutoscaling

    @EnableAutoscaling.setter
    def EnableAutoscaling(self, EnableAutoscaling):
        self._EnableAutoscaling = EnableAutoscaling

    @property
    def InstanceTypes(self):
        return self._InstanceTypes

    @InstanceTypes.setter
    def InstanceTypes(self, InstanceTypes):
        self._InstanceTypes = InstanceTypes

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        if params.get("Scaling") is not None:
            self._Scaling = MachineSetScaling()
            self._Scaling._deserialize(params.get("Scaling"))
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("UpgradeSettings") is not None:
            self._UpgradeSettings = MachineUpgradeSettings()
            self._UpgradeSettings._deserialize(params.get("UpgradeSettings"))
        self._AutoRepair = params.get("AutoRepair")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("SystemDisk") is not None:
            self._SystemDisk = Disk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("Management") is not None:
            self._Management = ManagementConfig()
            self._Management._deserialize(params.get("Management"))
        self._HealthCheckPolicyName = params.get("HealthCheckPolicyName")
        self._HostNamePattern = params.get("HostNamePattern")
        self._KubeletArgs = params.get("KubeletArgs")
        if params.get("Lifecycle") is not None:
            self._Lifecycle = LifecycleConfig()
            self._Lifecycle._deserialize(params.get("Lifecycle"))
        self._RuntimeRootDir = params.get("RuntimeRootDir")
        self._EnableAutoscaling = params.get("EnableAutoscaling")
        self._InstanceTypes = params.get("InstanceTypes")
        self._Replicas = params.get("Replicas")
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        