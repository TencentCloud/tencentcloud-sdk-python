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


class AddClusterStorageOptionRequest(AbstractModel):
    """AddClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _StorageOption: 集群存储选项。
        :type StorageOption: :class:`tencentcloud.thpc.v20220401.models.StorageOption`
        """
        self._ClusterId = None
        self._StorageOption = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def StorageOption(self):
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOption()
            self._StorageOption._deserialize(params.get("StorageOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterStorageOptionResponse(AbstractModel):
    """AddClusterStorageOption返回参数结构体

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


class AddNodesRequest(AbstractModel):
    """AddNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Placement: 集群中实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        :param _Count: 添加节点数量。
        :type Count: int
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜像和特定自定义镜像。
        :type ImageId: str
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: list of SystemDisk
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param _InstanceName: 节点显示名称。
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        :param _LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20220401.models.LoginSettings`
        :param _SecurityGroupIds: 集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param _ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param _QueueName: 队列名称。不指定则为默认队列。<li>SLURM默认队列为：compute。<li>SGE默认队列为：all.q。

        :type QueueName: str
        :param _NodeRole: 添加节点角色。默认值：Compute<br><li>Compute：计算节点。<br><li>Login：登录节点。
        :type NodeRole: str
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param _NodeType: 添加节点类型。默认取值：STATIC。<li>STATIC：静态节点，不会参与弹性伸缩流程。<li>DYNAMIC：弹性节点，会被弹性缩容的节点。管控节点和登录节点不支持此参数。
        :type NodeType: str
        """
        self._Placement = None
        self._ClusterId = None
        self._VirtualPrivateCloud = None
        self._Count = None
        self._ImageId = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._InstanceName = None
        self._LoginSettings = None
        self._SecurityGroupIds = None
        self._ClientToken = None
        self._QueueName = None
        self._NodeRole = None
        self._DryRun = None
        self._NodeType = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

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
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._ClusterId = params.get("ClusterId")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._Count = params.get("Count")
        self._ImageId = params.get("ImageId")
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
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        self._InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self._LoginSettings = LoginSettings()
            self._LoginSettings._deserialize(params.get("LoginSettings"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._ClientToken = params.get("ClientToken")
        self._QueueName = params.get("QueueName")
        self._NodeRole = params.get("NodeRole")
        self._DryRun = params.get("DryRun")
        self._NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodesResponse(AbstractModel):
    """AddNodes返回参数结构体

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


class AddQueueRequest(AbstractModel):
    """AddQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _QueueName: 队列名称。<br><li>最多支持32个字符。
        :type QueueName: str
        """
        self._ClusterId = None
        self._QueueName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddQueueResponse(AbstractModel):
    """AddQueue返回参数结构体

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


class CFSOption(AbstractModel):
    """描述CFS文件系统版本和挂载信息

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载ip及路径。
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
        


class CFSOptionOverview(AbstractModel):
    """CFS存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载ip及路径。
        :type RemotePath: str
        :param _Protocol: 文件系统协议类型。
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
        


class ClusterActivity(AbstractModel):
    """符合条件的集群活动信息。

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ActivityId: 集群活动ID。
        :type ActivityId: str
        :param _ActivityType: 集群活动类型。取值范围：<br><li>CreateAndAddNodes：创建实例并添加进集群<br><li>RemoveNodesFromCluster：从集群移除实例<br><li>TerminateNodes：销毁实例<br><li>MountStorageOption：增加挂载选项并进行挂载<br><li>UmountStorageOption：删除集群挂载存储选项并解挂载

        :type ActivityType: str
        :param _ActivityStatus: 集群活动状态。取值范围：<br><li>PENDING：等待运行<br><li>RUNNING：运行中<br><li>SUCCESSFUL：活动成功<br><li>PARTIALLY_SUCCESSFUL：活动部分成功<br><li>FAILED：活动失败
        :type ActivityStatus: str
        :param _ActivityStatusCode: 集群活动状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityStatusCode: str
        :param _ResultDetail: 集群活动结果详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultDetail: str
        :param _Cause: 集群活动起因。
        :type Cause: str
        :param _Description: 集群活动描述。
        :type Description: str
        :param _RelatedNodeActivitySet: 集群活动相关节点活动集合。
        :type RelatedNodeActivitySet: list of NodeActivity
        :param _StartTime: 集群活动开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 集群活动结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self._ClusterId = None
        self._ActivityId = None
        self._ActivityType = None
        self._ActivityStatus = None
        self._ActivityStatusCode = None
        self._ResultDetail = None
        self._Cause = None
        self._Description = None
        self._RelatedNodeActivitySet = None
        self._StartTime = None
        self._EndTime = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ActivityId(self):
        return self._ActivityId

    @ActivityId.setter
    def ActivityId(self, ActivityId):
        self._ActivityId = ActivityId

    @property
    def ActivityType(self):
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def ActivityStatus(self):
        return self._ActivityStatus

    @ActivityStatus.setter
    def ActivityStatus(self, ActivityStatus):
        self._ActivityStatus = ActivityStatus

    @property
    def ActivityStatusCode(self):
        return self._ActivityStatusCode

    @ActivityStatusCode.setter
    def ActivityStatusCode(self, ActivityStatusCode):
        self._ActivityStatusCode = ActivityStatusCode

    @property
    def ResultDetail(self):
        return self._ResultDetail

    @ResultDetail.setter
    def ResultDetail(self, ResultDetail):
        self._ResultDetail = ResultDetail

    @property
    def Cause(self):
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RelatedNodeActivitySet(self):
        return self._RelatedNodeActivitySet

    @RelatedNodeActivitySet.setter
    def RelatedNodeActivitySet(self, RelatedNodeActivitySet):
        self._RelatedNodeActivitySet = RelatedNodeActivitySet

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ActivityId = params.get("ActivityId")
        self._ActivityType = params.get("ActivityType")
        self._ActivityStatus = params.get("ActivityStatus")
        self._ActivityStatusCode = params.get("ActivityStatusCode")
        self._ResultDetail = params.get("ResultDetail")
        self._Cause = params.get("Cause")
        self._Description = params.get("Description")
        if params.get("RelatedNodeActivitySet") is not None:
            self._RelatedNodeActivitySet = []
            for item in params.get("RelatedNodeActivitySet"):
                obj = NodeActivity()
                obj._deserialize(item)
                self._RelatedNodeActivitySet.append(obj)
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
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
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
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
        :param _VpcId: 集群所属私有网络ID。
        :type VpcId: str
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
        self._VpcId = None

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

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


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
        self._VpcId = params.get("VpcId")
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
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
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
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param _ManagerNode: 指定管理节点。
        :type ManagerNode: :class:`tencentcloud.thpc.v20220401.models.ManagerNode`
        :param _ManagerNodeCount: 指定管理节点的数量。默认取值：1。取值范围：1～2。
        :type ManagerNodeCount: int
        :param _ComputeNode: 指定计算节点。
        :type ComputeNode: :class:`tencentcloud.thpc.v20220401.models.ComputeNode`
        :param _ComputeNodeCount: 指定计算节点的数量。默认取值：0。
        :type ComputeNodeCount: int
        :param _SchedulerType: 调度器类型。默认取值：SLURM。<br><li>SGE：SGE调度器。<br><li>SLURM：SLURM调度器。
        :type SchedulerType: str
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前支持部分公有镜像和自定义镜像。
        :type ImageId: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        :param _LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20220401.models.LoginSettings`
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
        :param _AccountType: 域名字服务类型。默认取值：NIS。
<li>NIS：NIS域名字服务。
        :type AccountType: str
        :param _ClusterName: 集群显示名称。
        :type ClusterName: str
        :param _StorageOption: 集群存储选项
        :type StorageOption: :class:`tencentcloud.thpc.v20220401.models.StorageOption`
        :param _LoginNode: 指定登录节点。
        :type LoginNode: :class:`tencentcloud.thpc.v20220401.models.LoginNode`
        :param _LoginNodeCount: 指定登录节点的数量。默认取值：0。取值范围：0～10。
        :type LoginNodeCount: int
        :param _Tags: 创建集群时同时绑定的标签对说明。
        :type Tags: list of Tag
        :param _AutoScalingType: 弹性伸缩类型。<br><li>AS：集群自动扩缩容由[弹性伸缩](https://cloud.tencent.com/document/product/377/3154)产品实现。<br><li>THPC_AS：集群自动扩缩容由THPC产品内部实现。
        :type AutoScalingType: str
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
        self._AutoScalingType = None

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

    @property
    def AutoScalingType(self):
        return self._AutoScalingType

    @AutoScalingType.setter
    def AutoScalingType(self, AutoScalingType):
        self._AutoScalingType = AutoScalingType


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
            self._LoginNode = LoginNode()
            self._LoginNode._deserialize(params.get("LoginNode"))
        self._LoginNodeCount = params.get("LoginNodeCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._AutoScalingType = params.get("AutoScalingType")
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DeleteClusterStorageOptionRequest(AbstractModel):
    """DeleteClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _LocalPath: 本地挂载路径。
        :type LocalPath: str
        """
        self._ClusterId = None
        self._LocalPath = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def LocalPath(self):
        return self._LocalPath

    @LocalPath.setter
    def LocalPath(self, LocalPath):
        self._LocalPath = LocalPath


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterStorageOptionResponse(AbstractModel):
    """DeleteClusterStorageOption返回参数结构体

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


class DeleteNodesRequest(AbstractModel):
    """DeleteNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _NodeIds: 节点ID。
        :type NodeIds: list of str
        """
        self._ClusterId = None
        self._NodeIds = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NodeIds(self):
        return self._NodeIds

    @NodeIds.setter
    def NodeIds(self, NodeIds):
        self._NodeIds = NodeIds


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNodesResponse(AbstractModel):
    """DeleteNodes返回参数结构体

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


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _QueueName: 队列名称。<br><li>最多支持32个字符。
        :type QueueName: str
        """
        self._ClusterId = None
        self._QueueName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回参数结构体

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


class DescribeAutoScalingConfigurationRequest(AbstractModel):
    """DescribeAutoScalingConfiguration请求参数结构体

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
        


class DescribeAutoScalingConfigurationResponse(AbstractModel):
    """DescribeAutoScalingConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。
        :type ExpansionBusyTime: int
        :param _ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。
        :type ShrinkIdleTime: int
        :param _QueueConfigs: 扩容队列配置概览列表。
        :type QueueConfigs: list of QueueConfigOverview
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterId = None
        self._ExpansionBusyTime = None
        self._ShrinkIdleTime = None
        self._QueueConfigs = None
        self._RequestId = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def QueueConfigs(self):
        return self._QueueConfigs

    @QueueConfigs.setter
    def QueueConfigs(self, QueueConfigs):
        self._QueueConfigs = QueueConfigs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ExpansionBusyTime = params.get("ExpansionBusyTime")
        self._ShrinkIdleTime = params.get("ShrinkIdleTime")
        if params.get("QueueConfigs") is not None:
            self._QueueConfigs = []
            for item in params.get("QueueConfigs"):
                obj = QueueConfigOverview()
                obj._deserialize(item)
                self._QueueConfigs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClusterActivitiesRequest(AbstractModel):
    """DescribeClusterActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。通过该参数指定需要查询活动历史记录的集群。
        :type ClusterId: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterActivitiesResponse(AbstractModel):
    """DescribeClusterActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterActivitySet: 集群活动历史记录列表。
        :type ClusterActivitySet: list of ClusterActivity
        :param _TotalCount: 集群活动历史记录数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ClusterActivitySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ClusterActivitySet(self):
        return self._ClusterActivitySet

    @ClusterActivitySet.setter
    def ClusterActivitySet(self, ClusterActivitySet):
        self._ClusterActivitySet = ClusterActivitySet

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
        if params.get("ClusterActivitySet") is not None:
            self._ClusterActivitySet = []
            for item in params.get("ClusterActivitySet"):
                obj = ClusterActivity()
                obj._deserialize(item)
                self._ClusterActivitySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeClusterStorageOptionRequest(AbstractModel):
    """DescribeClusterStorageOption请求参数结构体

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
        


class DescribeClusterStorageOptionResponse(AbstractModel):
    """DescribeClusterStorageOption返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StorageOption: 集群存储选项信息概览。
        :type StorageOption: :class:`tencentcloud.thpc.v20220401.models.StorageOptionOverview`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StorageOption = None
        self._RequestId = None

    @property
    def StorageOption(self):
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("StorageOption") is not None:
            self._StorageOption = StorageOptionOverview()
            self._StorageOption._deserialize(params.get("StorageOption"))
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeNodesRequest(AbstractModel):
    """DescribeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _Filters: <li><strong>queue-name</strong></li> <p style="padding-left: 30px;">按照【<strong>队列名称</strong>】进行过滤。队列名称形如：compute。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"><li><strong>node-role</strong></li> <p style="padding-left: 30px;">按照【<strong>节点角色</strong>】进行过滤。节点角色形如：Manager。（Manager：管控节点。Compute：计算节点。Login：登录节点。ManagerBackup：备用管控节点。）</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"><li><strong>node-type</strong></li> <p style="padding-left: 30px;">按照【<strong>节点类型</strong>】进行过滤。节点类型形如：STATIC。(STATIC：静态节点。DYNAMIC：弹性节点。)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
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
        


class DescribeNodesResponse(AbstractModel):
    """DescribeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeSet: 节点概览信息列表。
        :type NodeSet: list of NodeOverview
        :param _TotalCount: 符合条件的节点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NodeSet(self):
        return self._NodeSet

    @NodeSet.setter
    def NodeSet(self, NodeSet):
        self._NodeSet = NodeSet

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
        if params.get("NodeSet") is not None:
            self._NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeOverview()
                obj._deserialize(item)
                self._NodeSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeQueuesRequest(AbstractModel):
    """DescribeQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self._ClusterId = None
        self._Offset = None
        self._Limit = None

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


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueuesResponse(AbstractModel):
    """DescribeQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QueueSet: 队列概览信息列表。
        :type QueueSet: list of QueueOverview
        :param _TotalCount: 符合条件的节点数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QueueSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def QueueSet(self):
        return self._QueueSet

    @QueueSet.setter
    def QueueSet(self, QueueSet):
        self._QueueSet = QueueSet

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
        if params.get("QueueSet") is not None:
            self._QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueOverview()
                obj._deserialize(item)
                self._QueueSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ExpansionNodeConfig(AbstractModel):
    """弹性扩容节点配置信息。

    """

    def __init__(self):
        r"""
        :param _Placement: 扩容实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        """
        self._Placement = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._VirtualPrivateCloud = None

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

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
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpansionNodeConfigOverview(AbstractModel):
    """扩容节点配置信息概览。

    """

    def __init__(self):
        r"""
        :param _InstanceType: 节点机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Placement: 扩容实例所在的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param _VirtualPrivateCloud: 私有网络相关信息配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _InternetAccessible: 公网带宽相关信息设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param _SystemDisk: 节点系统盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        """
        self._InstanceType = None
        self._Placement = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None
        self._VirtualPrivateCloud = None
        self._ImageId = None
        self._InternetAccessible = None
        self._SystemDisk = None
        self._DataDisks = None

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Placement(self):
        return self._Placement

    @Placement.setter
    def Placement(self, Placement):
        self._Placement = Placement

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
    def VirtualPrivateCloud(self):
        return self._VirtualPrivateCloud

    @VirtualPrivateCloud.setter
    def VirtualPrivateCloud(self, VirtualPrivateCloud):
        self._VirtualPrivateCloud = VirtualPrivateCloud

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def InternetAccessible(self):
        return self._InternetAccessible

    @InternetAccessible.setter
    def InternetAccessible(self, InternetAccessible):
        self._InternetAccessible = InternetAccessible

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


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        if params.get("Placement") is not None:
            self._Placement = Placement()
            self._Placement._deserialize(params.get("Placement"))
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("VirtualPrivateCloud") is not None:
            self._VirtualPrivateCloud = VirtualPrivateCloud()
            self._VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self._ImageId = params.get("ImageId")
        if params.get("InternetAccessible") is not None:
            self._InternetAccessible = InternetAccessible()
            self._InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
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
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
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
        


class GooseFSOption(AbstractModel):
    """描述GooseFS挂载信息

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载路径。
        :type RemotePath: str
        :param _Masters: 文件系统master的ip和端口。
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
        


class GooseFSOptionOverview(AbstractModel):
    """GooseFS存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param _RemotePath: 文件系统远程挂载路径。
        :type RemotePath: str
        :param _Masters: 文件系统master的ip和端口。
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
        :param _InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
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
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param _InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
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
        


class NodeActivity(AbstractModel):
    """节点活动信息。

    """

    def __init__(self):
        r"""
        :param _NodeInstanceId: 节点活动所在的实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInstanceId: str
        :param _NodeActivityStatus: 节点活动状态。取值范围：<br><li>RUNNING：运行中<br><li>SUCCESSFUL：活动成功<br><li>FAILED：活动失败
        :type NodeActivityStatus: str
        :param _NodeActivityStatusCode: 节点活动状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeActivityStatusCode: str
        :param _NodeActivityStatusReason: 节点活动状态原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeActivityStatusReason: str
        """
        self._NodeInstanceId = None
        self._NodeActivityStatus = None
        self._NodeActivityStatusCode = None
        self._NodeActivityStatusReason = None

    @property
    def NodeInstanceId(self):
        return self._NodeInstanceId

    @NodeInstanceId.setter
    def NodeInstanceId(self, NodeInstanceId):
        self._NodeInstanceId = NodeInstanceId

    @property
    def NodeActivityStatus(self):
        return self._NodeActivityStatus

    @NodeActivityStatus.setter
    def NodeActivityStatus(self, NodeActivityStatus):
        self._NodeActivityStatus = NodeActivityStatus

    @property
    def NodeActivityStatusCode(self):
        return self._NodeActivityStatusCode

    @NodeActivityStatusCode.setter
    def NodeActivityStatusCode(self, NodeActivityStatusCode):
        self._NodeActivityStatusCode = NodeActivityStatusCode

    @property
    def NodeActivityStatusReason(self):
        return self._NodeActivityStatusReason

    @NodeActivityStatusReason.setter
    def NodeActivityStatusReason(self, NodeActivityStatusReason):
        self._NodeActivityStatusReason = NodeActivityStatusReason


    def _deserialize(self, params):
        self._NodeInstanceId = params.get("NodeInstanceId")
        self._NodeActivityStatus = params.get("NodeActivityStatus")
        self._NodeActivityStatusCode = params.get("NodeActivityStatusCode")
        self._NodeActivityStatusReason = params.get("NodeActivityStatusReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeOverview(AbstractModel):
    """节点概览信息。

    """

    def __init__(self):
        r"""
        :param _InstanceId: 节点实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _Zone: 节点所在可用区信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _NodeState: 节点状态。<br><li>SUBMITTED：已完成提交。<br><li>CREATING：创建中。<br><li>CREATED：完成创建。<br><li>INITING：初始化中。<br><li>INIT_FAILED：初始化失败。<br><li>RUNNING：运行中。<br><li>DELETING：销毁中。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeState: str
        :param _ImageId: 镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param _QueueName: 节点所属队列名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        :param _NodeRole: 节点角色。<br><li>Manager：管控节点。<br><li>Compute：计算节点。<br><li>Login：登录节点。<br><li>ManagerBackup：备用管控节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeRole: str
        :param _NodeType: 节点类型。<br><li>STATIC：静态节点。<br><li>DYNAMIC：弹性节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        """
        self._InstanceId = None
        self._Zone = None
        self._NodeState = None
        self._ImageId = None
        self._QueueName = None
        self._NodeRole = None
        self._NodeType = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def NodeState(self):
        return self._NodeState

    @NodeState.setter
    def NodeState(self, NodeState):
        self._NodeState = NodeState

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def NodeRole(self):
        return self._NodeRole

    @NodeRole.setter
    def NodeRole(self, NodeRole):
        self._NodeRole = NodeRole

    @property
    def NodeType(self):
        return self._NodeType

    @NodeType.setter
    def NodeType(self, NodeType):
        self._NodeType = NodeType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._NodeState = params.get("NodeState")
        self._ImageId = params.get("ImageId")
        self._QueueName = params.get("QueueName")
        self._NodeRole = params.get("NodeRole")
        self._NodeType = params.get("NodeType")
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
        


class QueueConfig(AbstractModel):
    """扩容队列配置。

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称。
        :type QueueName: str
        :param _MinSize: 队列中弹性节点数量最小值。取值范围0～200。
        :type MinSize: int
        :param _MaxSize: 队列中弹性节点数量最大值。取值范围0～200。
        :type MaxSize: int
        :param _EnableAutoExpansion: 是否开启自动扩容。
        :type EnableAutoExpansion: bool
        :param _EnableAutoShrink: 是否开启自动缩容。
        :type EnableAutoShrink: bool
        :param _ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜和特定自定义镜像。
        :type ImageId: str
        :param _SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param _DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param _InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param _ExpansionNodeConfigs: 扩容节点配置信息。
        :type ExpansionNodeConfigs: list of ExpansionNodeConfig
        """
        self._QueueName = None
        self._MinSize = None
        self._MaxSize = None
        self._EnableAutoExpansion = None
        self._EnableAutoShrink = None
        self._ImageId = None
        self._SystemDisk = None
        self._DataDisks = None
        self._InternetAccessible = None
        self._ExpansionNodeConfigs = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

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
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

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
    def ExpansionNodeConfigs(self):
        return self._ExpansionNodeConfigs

    @ExpansionNodeConfigs.setter
    def ExpansionNodeConfigs(self, ExpansionNodeConfigs):
        self._ExpansionNodeConfigs = ExpansionNodeConfigs


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._EnableAutoExpansion = params.get("EnableAutoExpansion")
        self._EnableAutoShrink = params.get("EnableAutoShrink")
        self._ImageId = params.get("ImageId")
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
        if params.get("ExpansionNodeConfigs") is not None:
            self._ExpansionNodeConfigs = []
            for item in params.get("ExpansionNodeConfigs"):
                obj = ExpansionNodeConfig()
                obj._deserialize(item)
                self._ExpansionNodeConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueConfigOverview(AbstractModel):
    """扩容队列配置概览。

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称。
        :type QueueName: str
        :param _MinSize: 队列中弹性节点数量最小值。取值范围0～200。
        :type MinSize: int
        :param _MaxSize: 队列中弹性节点数量最大值。取值范围0～200。
        :type MaxSize: int
        :param _EnableAutoExpansion: 是否开启自动扩容。
        :type EnableAutoExpansion: bool
        :param _EnableAutoShrink: 是否开启自动缩容。
        :type EnableAutoShrink: bool
        :param _ExpansionNodeConfigs: 扩容节点配置信息。
        :type ExpansionNodeConfigs: list of ExpansionNodeConfigOverview
        """
        self._QueueName = None
        self._MinSize = None
        self._MaxSize = None
        self._EnableAutoExpansion = None
        self._EnableAutoShrink = None
        self._ExpansionNodeConfigs = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName

    @property
    def MinSize(self):
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def MaxSize(self):
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

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
    def ExpansionNodeConfigs(self):
        return self._ExpansionNodeConfigs

    @ExpansionNodeConfigs.setter
    def ExpansionNodeConfigs(self, ExpansionNodeConfigs):
        self._ExpansionNodeConfigs = ExpansionNodeConfigs


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        self._MinSize = params.get("MinSize")
        self._MaxSize = params.get("MaxSize")
        self._EnableAutoExpansion = params.get("EnableAutoExpansion")
        self._EnableAutoShrink = params.get("EnableAutoShrink")
        if params.get("ExpansionNodeConfigs") is not None:
            self._ExpansionNodeConfigs = []
            for item in params.get("ExpansionNodeConfigs"):
                obj = ExpansionNodeConfigOverview()
                obj._deserialize(item)
                self._ExpansionNodeConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueOverview(AbstractModel):
    """队列信息概览。

    """

    def __init__(self):
        r"""
        :param _QueueName: 队列名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        """
        self._QueueName = None

    @property
    def QueueName(self):
        return self._QueueName

    @QueueName.setter
    def QueueName(self, QueueName):
        self._QueueName = QueueName


    def _deserialize(self, params):
        self._QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoScalingConfigurationRequest(AbstractModel):
    """SetAutoScalingConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID。
        :type ClusterId: str
        :param _ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。默认值120。
        :type ExpansionBusyTime: int
        :param _ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。单位秒。默认值300。
        :type ShrinkIdleTime: int
        :param _QueueConfigs: 扩容队列配置列表。
        :type QueueConfigs: list of QueueConfig
        :param _DryRun: 是否只预检此次请求。
true：发送检查请求，不会绑定弹性伸缩组。检查项包括是否填写了必需参数，请求格式，业务限制。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId。
false（默认）：发送正常请求，通过检查后直接绑定弹性伸缩组。
        :type DryRun: bool
        """
        self._ClusterId = None
        self._ExpansionBusyTime = None
        self._ShrinkIdleTime = None
        self._QueueConfigs = None
        self._DryRun = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

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
    def QueueConfigs(self):
        return self._QueueConfigs

    @QueueConfigs.setter
    def QueueConfigs(self, QueueConfigs):
        self._QueueConfigs = QueueConfigs

    @property
    def DryRun(self):
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ExpansionBusyTime = params.get("ExpansionBusyTime")
        self._ShrinkIdleTime = params.get("ShrinkIdleTime")
        if params.get("QueueConfigs") is not None:
            self._QueueConfigs = []
            for item in params.get("QueueConfigs"):
                obj = QueueConfig()
                obj._deserialize(item)
                self._QueueConfigs.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoScalingConfigurationResponse(AbstractModel):
    """SetAutoScalingConfiguration返回参数结构体

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


class StorageOption(AbstractModel):
    """描述集群文件系统选项

    """

    def __init__(self):
        r"""
        :param _CFSOptions: 集群挂载CFS文件系统选项。
        :type CFSOptions: list of CFSOption
        :param _GooseFSOptions: 集群挂载GooseFS文件系统选项。
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
        


class StorageOptionOverview(AbstractModel):
    """集群存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param _CFSOptions: CFS存储选项概览信息列表。
        :type CFSOptions: list of CFSOptionOverview
        :param _GooseFSOptions: GooseFS存储选项概览信息列表。
        :type GooseFSOptions: list of GooseFSOptionOverview
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
                obj = CFSOptionOverview()
                obj._deserialize(item)
                self._CFSOptions.append(obj)
        if params.get("GooseFSOptions") is not None:
            self._GooseFSOptions = []
            for item in params.get("GooseFSOptions"):
                obj = GooseFSOptionOverview()
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
        