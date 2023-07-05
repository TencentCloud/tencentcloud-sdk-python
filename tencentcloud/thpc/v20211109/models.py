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


class BindAutoScalingGroupRequest(AbstractModel):
    """BindAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _LaunchConfigurationId: 弹性伸缩启动配置ID。
        :type LaunchConfigurationId: str
        :param _AutoScalingGroupId: 弹性伸缩组ID。
        :type AutoScalingGroupId: str
        :param _QueueName: 队列名称。
        :type QueueName: str
        :param _ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。默认值120。
        :type ExpansionBusyTime: int
        :param _ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。单位秒。默认值300。
        :type ShrinkIdleTime: int
        :param _EnableAutoExpansion: 是否开启自动扩容，默认值true。
        :type EnableAutoExpansion: bool
        :param _EnableAutoShrink: 是否开启自动缩容，默认值true。
        :type EnableAutoShrink: bool
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会绑定弹性伸缩组。检查项包括是否填写了必需参数，请求格式，业务限制。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId。
false（默认）：发送正常请求，通过检查后直接绑定弹性伸缩组。
        :type DryRun: bool
        """
        self._ClusterId = None
        self._LaunchConfigurationId = None
        self._AutoScalingGroupId = None
        self._QueueName = None
        self._ExpansionBusyTime = None
        self._ShrinkIdleTime = None
        self._EnableAutoExpansion = None
        self._EnableAutoShrink = None
        self._DryRun = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def LaunchConfigurationId(self):
        return self._LaunchConfigurationId

    @LaunchConfigurationId.setter
    def LaunchConfigurationId(self, LaunchConfigurationId):
        self._LaunchConfigurationId = LaunchConfigurationId

    @property
    def AutoScalingGroupId(self):
        return self._AutoScalingGroupId

    @AutoScalingGroupId.setter
    def AutoScalingGroupId(self, AutoScalingGroupId):
        self._AutoScalingGroupId = AutoScalingGroupId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def ExpansionBusyTime(self):
        return self._ExpansionBusyTime

    @ExpansionBusyTime.setter
    def ExpansionBusyTime(self, ExpansionBusyTime):
        self._ExpansionBusyTime = ExpansionBusyTime

    @property
    def ShrinkIdleTime(self):
        return self._ShrinkIdleTime

    @ShrinkIdleTime.setter
    def ShrinkIdleTime(self, ShrinkIdleTime):
        self._ShrinkIdleTime = ShrinkIdleTime

    @property
    def EnableAutoExpansion(self):
        return self._EnableAutoExpansion

    @EnableAutoExpansion.setter
    def EnableAutoExpansion(self, EnableAutoExpansion):
        self._EnableAutoExpansion = EnableAutoExpansion

    @property
    def EnableAutoShrink(self):
        return self._EnableAutoShrink

    @EnableAutoShrink.setter
    def EnableAutoShrink(self, EnableAutoShrink):
        self._EnableAutoShrink = EnableAutoShrink

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._LaunchConfigurationId = params.get("LaunchConfigurationId")
        self._AutoScalingGroupId = params.get("AutoScalingGroupId")
        self._QueueName = params.get("QueueName")
        self._ExpansionBusyTime = params.get("ExpansionBusyTime")
        self._ShrinkIdleTime = params.get("ShrinkIdleTime")
        self._EnableAutoExpansion = params.get("EnableAutoExpansion")
        self._EnableAutoShrink = params.get("EnableAutoShrink")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoScalingGroupResponse(AbstractModel):
    """BindAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class CFSOption(AbstractModel):
    """描述CFS文件系统版本和挂载信息

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载ip及路径
        :type RemotePath: str
        :param _Protocol: 文件系统协议类型，默认值NFS 3.0。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :type Protocol: str
        :param _StorageType: 文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :type StorageType: str
        """
        self._LocalPath = None
        self._RemotePath = None
        self._Protocol = None
        self._StorageType = None

    @property
    def LocalPath(self):
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._Protocol = params.get("Protocol")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOverview(AbstractModel):
    """集群概览信息。

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ClusterStatus: 集群状态。取值范围：<br><li>PENDING：创建中<br><li>INITING：初始化中<br><li>INIT_FAILED：初始化失败<br><li>RUNNING：运行中<br><li>TERMINATING：销毁中
        :type ClusterStatus: str
        :param _ClusterName: 集群名称。
        :type ClusterName: str
        :param _Placement: 集群位置信息。
        :type Placement: :class:`tencentcloud.thpc.v20211109.models.Placement`
        :param _CreateTime: 集群创建时间。
        :type CreateTime: str
        :param _SchedulerType: 集群调度器。
        :type SchedulerType: str
        :param _ComputeNodeCount: 计算节点数量。
        :type ComputeNodeCount: int
        :param _ComputeNodeSet: 计算节点概览。
        :type ComputeNodeSet: list of ComputeNodeOverview
        :param _ManagerNodeCount: 管控节点数量。
        :type ManagerNodeCount: int
        :param _ManagerNodeSet: 管控节点概览。
        :type ManagerNodeSet: list of ManagerNodeOverview
        :param _LoginNodeSet: 登录节点概览。
        :type LoginNodeSet: list of LoginNodeOverview
        :param _LoginNodeCount: 登录节点数量。
        :type LoginNodeCount: int
        """
        self._ClusterId = None
        self._ClusterStatus = None
        self._ClusterName = None
        self._Placement = None
        self._CreateTime = None
        self._SchedulerType = None
        self._ComputeNodeCount = None
        self._ComputeNodeSet = None
        self._ManagerNodeCount = None
        self._ManagerNodeSet = None
        self._LoginNodeSet = None
        self._LoginNodeCount = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterStatus(self):
        return self._ClusterStatus

    @ClusterStatus.setter
    def ClusterStatus(self, ClusterStatus):
        self._ClusterStatus = ClusterStatus

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SchedulerType(self):
        return self._SchedulerType

    @SchedulerType.setter
    def SchedulerType(self, SchedulerType):
        self._SchedulerType = SchedulerType

    @property
    def ComputeNodeCount(self):
        return self._ComputeNodeCount

    @ComputeNodeCount.setter
    def ComputeNodeCount(self, ComputeNodeCount):
        self._ComputeNodeCount = ComputeNodeCount

    @property
    def ComputeNodeSet(self):
        return self._ComputeNodeSet

    @ComputeNodeSet.setter
    def ComputeNodeSet(self, ComputeNodeSet):
        self._ComputeNodeSet = ComputeNodeSet

    @property
    def ManagerNodeCount(self):
        return self._ManagerNodeCount

    @ManagerNodeCount.setter
    def ManagerNodeCount(self, ManagerNodeCount):
        self._ManagerNodeCount = ManagerNodeCount

    @property
    def ManagerNodeSet(self):
        return self._ManagerNodeSet

    @ManagerNodeSet.setter
    def ManagerNodeSet(self, ManagerNodeSet):
        self._ManagerNodeSet = ManagerNodeSet

    @property
    def LoginNodeSet(self):
        return self._LoginNodeSet

    @LoginNodeSet.setter
    def LoginNodeSet(self, LoginNodeSet):
        self._LoginNodeSet = LoginNodeSet

    @property
    def LoginNodeCount(self):
        return self._LoginNodeCount

    @LoginNodeCount.setter
    def LoginNodeCount(self, LoginNodeCount):
        self._LoginNodeCount = LoginNodeCount


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterStatus = params.get("ClusterStatus")
        self._ClusterName = params.get("ClusterName")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._CreateTime = params.get("CreateTime")
        self._SchedulerType = params.get("SchedulerType")
        self._ComputeNodeCount = params.get("ComputeNodeCount")
        if params.get("ComputeNodeSet") is not None:
            self._ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNodeOverview()
                obj._deserialize(item)
                self._ComputeNodeSet.append(obj)
        self._ManagerNodeCount = params.get("ManagerNodeCount")
        if params.get("ManagerNodeSet") is not None:
            self._ManagerNodeSet = []
            for item in params.get("ManagerNodeSet"):
                obj = ManagerNodeOverview()
                obj._deserialize(item)
                self._ManagerNodeSet.append(obj)
        if params.get("LoginNodeSet") is not None:
            self._LoginNodeSet = []
            for item in params.get("LoginNodeSet"):
                obj = LoginNodeOverview()
                obj._deserialize(item)
                self._LoginNodeSet.append(obj)
        self._LoginNodeCount = params.get("LoginNodeCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNode(AbstractModel):
    """计算节点信息。

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20211109.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20211109.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20211109.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNodeOverview(AbstractModel):
    """计算节点概览。

    """

    def __init__(self):
        r"""
        :param _NodeId: 计算节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 集群中实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20211109.models.Placement`
        :param _ManagerNode: 指定管理节点。
        :type ManagerNode: :class:`tencentcloud.thpc.v20211109.models.ManagerNode`
        :param _ManagerNodeCount: 指定管理节点的数量。默认取值：1。取值范围：1～2。
        :type ManagerNodeCount: int
        :param _ComputeNode: 指定计算节点。
        :type ComputeNode: :class:`tencentcloud.thpc.v20211109.models.ComputeNode`
        :param _ComputeNodeCount: 指定计算节点的数量。默认取值：0。
        :type ComputeNodeCount: int
        :param _SchedulerType: 调度器类型。<br><li>SGE：SGE调度器。<br><li>SLURM：SLURM调度器。
        :type SchedulerType: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜像。
        :type ImageId: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20211109.models.VirtualPrivateCloud`
        :param _LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20211109.models.LoginSettings`
        :param _SecurityGroupIds: 集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param _AccountType: 域名字服务类型。默认值：NIS
<li>NIS：NIS域名字服务。
        :type AccountType: str
        :param _ClusterName: 集群显示名称。
        :type ClusterName: str
        :param _StorageOption: 集群存储选项
        :type StorageOption: :class:`tencentcloud.thpc.v20211109.models.StorageOption`
        :param _LoginNode: 已废弃。
指定登录节点。
        :type LoginNode: list of LoginNode
        :param _LoginNodeCount: 已废弃。
指定登录节点的数量。默认取值：0。取值范围：0～10。
        :type LoginNodeCount: int
        :param _Tags: 创建集群时同时绑定的标签对说明。
        :type Tags: list of Tag
        """
        self._Placement = None
        self._ManagerNode = None
        self._ManagerNodeCount = None
        self._ComputeNode = None
        self._ComputeNodeCount = None
        self._SchedulerType = None
        self._ImageId = None
        self._VirtualPrivateCloud = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._ClientToken = None
        self._DryRun = None
        self._AccountType = None
        self._ClusterName = None
        self._StorageOption = None
        self._LoginNode = None
        self._LoginNodeCount = None
        self._Tags = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ManagerNode(self):
        return self._ManagerNode

    @ManagerNode.setter
    def ManagerNode(self, ManagerNode):
        self._ManagerNode = ManagerNode

    @property
    def ManagerNodeCount(self):
        return self._ManagerNodeCount

    @ManagerNodeCount.setter
    def ManagerNodeCount(self, ManagerNodeCount):
        self._ManagerNodeCount = ManagerNodeCount

    @property
    def ComputeNode(self):
        return self._ComputeNode

    @ComputeNode.setter
    def ComputeNode(self, ComputeNode):
        self._ComputeNode = ComputeNode

    @property
    def ComputeNodeCount(self):
        return self._ComputeNodeCount

    @ComputeNodeCount.setter
    def ComputeNodeCount(self, ComputeNodeCount):
        self._ComputeNodeCount = ComputeNodeCount

    @property
    def SchedulerType(self):
        return self._SchedulerType

    @SchedulerType.setter
    def SchedulerType(self, SchedulerType):
        self._SchedulerType = SchedulerType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def LoginSettings(self):
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def SecurityGroupIds(self):
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def ClientToken(self):
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def AccountType(self):
        return self._AccountType

    @AccountType.setter
    def AccountType(self, AccountType):
        self._AccountType = AccountType

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def StorageOption(self):
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def LoginNode(self):
        return self._LoginNode

    @LoginNode.setter
    def LoginNode(self, LoginNode):
        self._LoginNode = LoginNode

    @property
    def LoginNodeCount(self):
        return self._LoginNodeCount

    @LoginNodeCount.setter
    def LoginNodeCount(self, LoginNodeCount):
        self._LoginNodeCount = LoginNodeCount

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        if params.get("ManagerNode") is not None:
            self._ManagerNode = ManagerNode()
            self._ManagerNode._deserialize(params.get("ManagerNode"))
        self._ManagerNodeCount = params.get("ManagerNodeCount")
        if params.get("ComputeNode") is not None:
            self._ComputeNode = ComputeNode()
            self._ComputeNode._deserialize(params.get("ComputeNode"))
        self._ComputeNodeCount = params.get("ComputeNodeCount")
        self._SchedulerType = params.get("SchedulerType")
        self._ImageId = params.get("ImageId")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        self._AccountType = params.get("AccountType")
        self._ClusterName = params.get("ClusterName")
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        if params.get("LoginNode") is not None:
            self._LoginNode = []
            for item in params.get("LoginNode"):
                obj = LoginNode()
                obj._deserialize(item)
                self._LoginNode.append(obj)
        self._LoginNodeCount = params.get("LoginNodeCount")
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
        


class CreateClusterResponse(AbstractModel):
    """CreateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param _DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br><li>LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><br>默认取值：LOCAL_BASIC。
        :type DiskType: str
        """
        self._DiskSize = None
        self._DiskType = None

    @property
    def DiskSize(self):
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskType(self):
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType


    def _deserialize(self, params):
        self._DiskSize = params.get("DiskSize")
        self._DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        """
        self._ClusterId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterResponse(AbstractModel):
    """DeleteCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterIds: 集群ID列表。通过该参数可以指定需要查询信息的集群列表。<br>如果您不指定该参数，则返回Limit数量以内的集群信息。
        :type ClusterIds: list of str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ClusterIds = None
        self._Offset = None
        self._Limit = None

    @property
    def ClusterIds(self):
        return self._ClusterIds

    @ClusterIds.setter
    def ClusterIds(self, ClusterIds):
        self._ClusterIds = ClusterIds

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
        self._ClusterIds = params.get("ClusterIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterSet: 集群概览信息列表。
        :type ClusterSet: list of ClusterOverview
        :param _TotalCount: 集群数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterSet(self):
        return self._ClusterSet

    @ClusterSet.setter
    def ClusterSet(self, ClusterSet):
        self._ClusterSet = ClusterSet

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
        if params.get("ClusterSet") is not None:
            self._ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = ClusterOverview()
                obj._deserialize(item)
                self._ClusterSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GooseFSOption(AbstractModel):
    """描述GooseFS挂载信息

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载路径
        :type RemotePath: str
        :param _Masters: 文件系统master的ip和端口
        :type Masters: list of str
        """
        self._LocalPath = None
        self._RemotePath = None
        self._Masters = None

    @property
    def LocalPath(self):
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath

    @property
    def RemotePath(self):
        return self._RemotePath

    @RemotePath.setter
    def RemotePath(self, RemotePath):
        self._RemotePath = RemotePath

    @property
    def Masters(self):
        return self._Masters

    @Masters.setter
    def Masters(self, Masters):
        self._Masters = Masters


    def _deserialize(self, params):
        self._LocalPath = params.get("LocalPath")
        self._RemotePath = params.get("RemotePath")
        self._Masters = params.get("Masters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param _Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
        :type Period: int
        :param _RenewFlag: 自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
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
        


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param _InternetChargeType: 网络计费类型。取值范围：
BANDWIDTH_PREPAID：预付费按带宽结算
TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费
BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费
BANDWIDTH_PACKAGE：带宽包用户
默认取值：非带宽包用户默认与子机付费类型保持一致。
        :type InternetChargeType: str
        :param _InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见购买网络带宽。
        :type InternetMaxBandwidthOut: int
        """
        self._InternetChargeType = None
        self._InternetMaxBandwidthOut = None

    @property
    def InternetChargeType(self):
        return self._InternetChargeType

    @InternetChargeType.setter
    def InternetChargeType(self, InternetChargeType):
        self._InternetChargeType = InternetChargeType

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut


    def _deserialize(self, params):
        self._InternetChargeType = params.get("InternetChargeType")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginNode(AbstractModel):
    """登录节点信息。

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20211109.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: list of SystemDisk
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: list of InternetAccessible
        :param _InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = []
            for item in params.get("SystemDisk"):
                obj = SystemDisk()
                obj._deserialize(item)
                self._SystemDisk.append(obj)
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = []
            for item in params.get("InternetAccessible"):
                obj = InternetAccessible()
                obj._deserialize(item)
                self._InternetAccessible.append(obj)
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginNodeOverview(AbstractModel):
    """登录节点概览。

    """

    def __init__(self):
        r"""
        :param _NodeId: 登录节点ID。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        r"""
        :param _Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) \` ~ ! @ # $ % ^ & *  - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) \` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        """
        self._Password = None

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password


    def _deserialize(self, params):
        self._Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerNode(AbstractModel):
    """管控节点信息

    """

    def __init__(self):
        r"""
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20211109.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20211109.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20211109.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
</li><li>购买多个节点，如果指定模式串`{R:x}`，表示生成数字[`[x, x+n-1]`，其中`n`表示购买节点的数量，例如`server_{R:3}`，购买1个时，节点显示名称为`server_3`；购买2个时，节点显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。
购买多个节点，如果不指定模式串，则在节点显示名称添加后缀`1、2...n`，其中`n`表示购买节点的数量，例如`server_`，购买2个时，节点显示名称分别为`server_1`，`server_2`。</li><li>
最多支持60个字符（包含模式串）。
        :type InstanceName: str
        """
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None

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
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SystemDisk(self):
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def DataDisks(self):
        return self._DataDisks

    @DataDisks.setter
    def DataDisks(self, DataDisks):
        self._DataDisks = DataDisks

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self._DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self._DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerNodeOverview(AbstractModel):
    """管控节点概览。

    """

    def __init__(self):
        r"""
        :param _NodeId: 管控节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        """
        self._NodeId = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置

    """

    def __init__(self):
        r"""
        :param _Zone: 实例所属的可用区名称。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        """
        self._Zone = None

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone


    def _deserialize(self, params):
        self._Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """描述集群文件系统选项

    """

    def __init__(self):
        r"""
        :param _CFSOptions: 集群挂载CFS文件系统选项
        :type CFSOptions: list of CFSOption
        :param _GooseFSOptions: 集群挂在GooseFS文件系统选项
        :type GooseFSOptions: list of GooseFSOption
        """
        self._CFSOptions = None
        self._GooseFSOptions = None

    @property
    def CFSOptions(self):
        return self._CFSOptions

    @CFSOptions.setter
    def CFSOptions(self, CFSOptions):
        self._CFSOptions = CFSOptions

    @property
    def GooseFSOptions(self):
        return self._GooseFSOptions

    @GooseFSOptions.setter
    def GooseFSOptions(self, GooseFSOptions):
        self._GooseFSOptions = GooseFSOptions


    def _deserialize(self, params):
        if params.get("CFSOptions") is not None:
            self._CFSOptions = []
            for item in params.get("CFSOptions"):
                obj = CFSOption()
                obj._deserialize(item)
                self._CFSOptions.append(obj)
        if params.get("GooseFSOptions") is not None:
            self._GooseFSOptions = []
            for item in params.get("GooseFSOptions"):
                obj = GooseFSOption()
                obj._deserialize(item)
                self._GooseFSOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。系统盘类型限制详见存储概述。取值范围：
LOCAL_BASIC：本地硬盘
LOCAL_SSD：本地SSD硬盘
CLOUD_BASIC：普通云硬盘
CLOUD_SSD：SSD云硬盘
CLOUD_PREMIUM：高性能云硬盘

默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        """
        self._DiskType = None
        self._DiskSize = None

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


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对。

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
        


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type VpcId: str
        :param _SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        