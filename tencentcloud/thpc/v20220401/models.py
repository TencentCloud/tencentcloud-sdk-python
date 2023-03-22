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
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param StorageOption: 集群存储选项。
        :type StorageOption: :class:`tencentcloud.thpc.v20220401.models.StorageOption`
        """
        self.ClusterId = None
        self.StorageOption = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("StorageOption") is not None:
            self.StorageOption = StorageOption()
            self.StorageOption._deserialize(params.get("StorageOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterStorageOptionResponse(AbstractModel):
    """AddClusterStorageOption返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddNodesRequest(AbstractModel):
    """AddNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param Placement: 集群中实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        :param Count: 添加节点数量。
        :type Count: int
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜像和特定自定义镜像。
        :type ImageId: str
        :param InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param InstanceType: 节点机型。不同实例机型指定了不同的资源规格。<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: list of SystemDisk
        :param DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param InstanceName: 节点显示名称。
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        :param LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20220401.models.LoginSettings`
        :param SecurityGroupIds: 集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param QueueName: 队列名称。不指定则为默认队列。<li>SLURM默认队列为：compute。<li>SGE默认队列为：all.q。

        :type QueueName: str
        :param NodeRole: 添加节点角色。默认值：Compute<br><li>Compute：计算节点。<br><li>Login：登录节点。
        :type NodeRole: str
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param NodeType: 添加节点类型。默认取值：STATIC。<li>STATIC：静态节点，不会参与弹性伸缩流程。<li>DYNAMIC：弹性节点，会被弹性缩容的节点。管控节点和登录节点不支持此参数。
        :type NodeType: str
        """
        self.Placement = None
        self.ClusterId = None
        self.VirtualPrivateCloud = None
        self.Count = None
        self.ImageId = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.ClientToken = None
        self.QueueName = None
        self.NodeRole = None
        self.DryRun = None
        self.NodeType = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClusterId = params.get("ClusterId")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.Count = params.get("Count")
        self.ImageId = params.get("ImageId")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = []
            for item in params.get("SystemDisk"):
                obj = SystemDisk()
                obj._deserialize(item)
                self.SystemDisk.append(obj)
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ClientToken = params.get("ClientToken")
        self.QueueName = params.get("QueueName")
        self.NodeRole = params.get("NodeRole")
        self.DryRun = params.get("DryRun")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddNodesResponse(AbstractModel):
    """AddNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddQueueRequest(AbstractModel):
    """AddQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param QueueName: 队列名称。<br><li>最多支持32个字符。
        :type QueueName: str
        """
        self.ClusterId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddQueueResponse(AbstractModel):
    """AddQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindAutoScalingGroupRequest(AbstractModel):
    """BindAutoScalingGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param LaunchConfigurationId: 弹性伸缩启动配置ID。
        :type LaunchConfigurationId: str
        :param AutoScalingGroupId: 弹性伸缩组ID。
        :type AutoScalingGroupId: str
        :param QueueName: 队列名称。
        :type QueueName: str
        :param ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。默认值120。
        :type ExpansionBusyTime: int
        :param ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。单位秒。默认值300。
        :type ShrinkIdleTime: int
        :param EnableAutoExpansion: 是否开启自动扩容，默认值true。
        :type EnableAutoExpansion: bool
        :param EnableAutoShrink: 是否开启自动缩容，默认值true。
        :type EnableAutoShrink: bool
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会绑定弹性伸缩组。检查项包括是否填写了必需参数，请求格式，业务限制。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId。
false（默认）：发送正常请求，通过检查后直接绑定弹性伸缩组。
        :type DryRun: bool
        """
        self.ClusterId = None
        self.LaunchConfigurationId = None
        self.AutoScalingGroupId = None
        self.QueueName = None
        self.ExpansionBusyTime = None
        self.ShrinkIdleTime = None
        self.EnableAutoExpansion = None
        self.EnableAutoShrink = None
        self.DryRun = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.LaunchConfigurationId = params.get("LaunchConfigurationId")
        self.AutoScalingGroupId = params.get("AutoScalingGroupId")
        self.QueueName = params.get("QueueName")
        self.ExpansionBusyTime = params.get("ExpansionBusyTime")
        self.ShrinkIdleTime = params.get("ShrinkIdleTime")
        self.EnableAutoExpansion = params.get("EnableAutoExpansion")
        self.EnableAutoShrink = params.get("EnableAutoShrink")
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoScalingGroupResponse(AbstractModel):
    """BindAutoScalingGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CFSOption(AbstractModel):
    """描述CFS文件系统版本和挂载信息

    """

    def __init__(self):
        r"""
        :param LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param RemotePath: 文件系统远程挂载ip及路径。
        :type RemotePath: str
        :param Protocol: 文件系统协议类型，默认值NFS 3.0。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :type Protocol: str
        :param StorageType: 文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :type StorageType: str
        """
        self.LocalPath = None
        self.RemotePath = None
        self.Protocol = None
        self.StorageType = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.RemotePath = params.get("RemotePath")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CFSOptionOverview(AbstractModel):
    """CFS存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param RemotePath: 文件系统远程挂载ip及路径。
        :type RemotePath: str
        :param Protocol: 文件系统协议类型。
<li>NFS 3.0。
<li>NFS 4.0。
<li>TURBO。
        :type Protocol: str
        :param StorageType: 文件系统存储类型，默认值SD；其中 SD 为通用标准型标准型存储， HP为通用性能型存储， TB为turbo标准型， TP 为turbo性能型。
        :type StorageType: str
        """
        self.LocalPath = None
        self.RemotePath = None
        self.Protocol = None
        self.StorageType = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.RemotePath = params.get("RemotePath")
        self.Protocol = params.get("Protocol")
        self.StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterActivity(AbstractModel):
    """符合条件的集群活动信息。

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param ActivityId: 集群活动ID。
        :type ActivityId: str
        :param ActivityType: 集群活动类型。取值范围：<br><li>CreateAndAddNodes：创建实例并添加进集群<br><li>RemoveNodesFromCluster：从集群移除实例<br><li>TerminateNodes：销毁实例<br><li>MountStorageOption：增加挂载选项并进行挂载<br><li>UmountStorageOption：删除集群挂载存储选项并解挂载

        :type ActivityType: str
        :param ActivityStatus: 集群活动状态。取值范围：<br><li>PENDING：等待运行<br><li>RUNNING：运行中<br><li>SUCCESSFUL：活动成功<br><li>PARTIALLY_SUCCESSFUL：活动部分成功<br><li>FAILED：活动失败
        :type ActivityStatus: str
        :param ActivityStatusCode: 集群活动状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivityStatusCode: str
        :param ResultDetail: 集群活动结果详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultDetail: str
        :param Cause: 集群活动起因。
        :type Cause: str
        :param Description: 集群活动描述。
        :type Description: str
        :param RelatedNodeActivitySet: 集群活动相关节点活动集合。
        :type RelatedNodeActivitySet: list of NodeActivity
        :param StartTime: 集群活动开始时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param EndTime: 集群活动结束时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        """
        self.ClusterId = None
        self.ActivityId = None
        self.ActivityType = None
        self.ActivityStatus = None
        self.ActivityStatusCode = None
        self.ResultDetail = None
        self.Cause = None
        self.Description = None
        self.RelatedNodeActivitySet = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ActivityId = params.get("ActivityId")
        self.ActivityType = params.get("ActivityType")
        self.ActivityStatus = params.get("ActivityStatus")
        self.ActivityStatusCode = params.get("ActivityStatusCode")
        self.ResultDetail = params.get("ResultDetail")
        self.Cause = params.get("Cause")
        self.Description = params.get("Description")
        if params.get("RelatedNodeActivitySet") is not None:
            self.RelatedNodeActivitySet = []
            for item in params.get("RelatedNodeActivitySet"):
                obj = NodeActivity()
                obj._deserialize(item)
                self.RelatedNodeActivitySet.append(obj)
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterOverview(AbstractModel):
    """集群概览信息。

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param ClusterStatus: 集群状态。取值范围：<br><li>PENDING：创建中<br><li>INITING：初始化中<br><li>INIT_FAILED：初始化失败<br><li>RUNNING：运行中<br><li>TERMINATING：销毁中
        :type ClusterStatus: str
        :param ClusterName: 集群名称。
        :type ClusterName: str
        :param Placement: 集群位置信息。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param CreateTime: 集群创建时间。
        :type CreateTime: str
        :param SchedulerType: 集群调度器。
        :type SchedulerType: str
        :param ComputeNodeCount: 计算节点数量。
        :type ComputeNodeCount: int
        :param ComputeNodeSet: 计算节点概览。
        :type ComputeNodeSet: list of ComputeNodeOverview
        :param ManagerNodeCount: 管控节点数量。
        :type ManagerNodeCount: int
        :param ManagerNodeSet: 管控节点概览。
        :type ManagerNodeSet: list of ManagerNodeOverview
        :param LoginNodeSet: 登录节点概览。
        :type LoginNodeSet: list of LoginNodeOverview
        :param LoginNodeCount: 登录节点数量。
        :type LoginNodeCount: int
        :param VpcId: 集群所属私有网络ID。
        :type VpcId: str
        """
        self.ClusterId = None
        self.ClusterStatus = None
        self.ClusterName = None
        self.Placement = None
        self.CreateTime = None
        self.SchedulerType = None
        self.ComputeNodeCount = None
        self.ComputeNodeSet = None
        self.ManagerNodeCount = None
        self.ManagerNodeSet = None
        self.LoginNodeSet = None
        self.LoginNodeCount = None
        self.VpcId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterStatus = params.get("ClusterStatus")
        self.ClusterName = params.get("ClusterName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        self.SchedulerType = params.get("SchedulerType")
        self.ComputeNodeCount = params.get("ComputeNodeCount")
        if params.get("ComputeNodeSet") is not None:
            self.ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNodeOverview()
                obj._deserialize(item)
                self.ComputeNodeSet.append(obj)
        self.ManagerNodeCount = params.get("ManagerNodeCount")
        if params.get("ManagerNodeSet") is not None:
            self.ManagerNodeSet = []
            for item in params.get("ManagerNodeSet"):
                obj = ManagerNodeOverview()
                obj._deserialize(item)
                self.ManagerNodeSet.append(obj)
        if params.get("LoginNodeSet") is not None:
            self.LoginNodeSet = []
            for item in params.get("LoginNodeSet"):
                obj = LoginNodeOverview()
                obj._deserialize(item)
                self.LoginNodeSet.append(obj)
        self.LoginNodeCount = params.get("LoginNodeCount")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNode(AbstractModel):
    """计算节点信息。

    """

    def __init__(self):
        r"""
        :param InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        """
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeNodeOverview(AbstractModel):
    """计算节点概览。

    """

    def __init__(self):
        r"""
        :param NodeId: 计算节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClusterRequest(AbstractModel):
    """CreateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param Placement: 集群中实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param ManagerNode: 指定管理节点。
        :type ManagerNode: :class:`tencentcloud.thpc.v20220401.models.ManagerNode`
        :param ManagerNodeCount: 指定管理节点的数量。默认取值：1。取值范围：1～2。
        :type ManagerNodeCount: int
        :param ComputeNode: 指定计算节点。
        :type ComputeNode: :class:`tencentcloud.thpc.v20220401.models.ComputeNode`
        :param ComputeNodeCount: 指定计算节点的数量。默认取值：0。
        :type ComputeNodeCount: int
        :param SchedulerType: 调度器类型。默认取值：SLURM。<br><li>SGE：SGE调度器。<br><li>SLURM：SLURM调度器。
        :type SchedulerType: str
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前支持部分公有镜像和自定义镜像。
        :type ImageId: str
        :param VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        :param LoginSettings: 集群登录设置。
        :type LoginSettings: :class:`tencentcloud.thpc.v20220401.models.LoginSettings`
        :param SecurityGroupIds: 集群中实例所属安全组。该参数可以通过调用 [DescribeSecurityGroups](https://cloud.tencent.com/document/api/215/15808) 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。
        :type SecurityGroupIds: list of str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数，请求格式，业务限制和云服务器库存。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId.
false（默认）：发送正常请求，通过检查后直接创建实例
        :type DryRun: bool
        :param AccountType: 域名字服务类型。默认取值：NIS。
<li>NIS：NIS域名字服务。
        :type AccountType: str
        :param ClusterName: 集群显示名称。
        :type ClusterName: str
        :param StorageOption: 集群存储选项
        :type StorageOption: :class:`tencentcloud.thpc.v20220401.models.StorageOption`
        :param LoginNode: 指定登录节点。
        :type LoginNode: :class:`tencentcloud.thpc.v20220401.models.LoginNode`
        :param LoginNodeCount: 指定登录节点的数量。默认取值：0。取值范围：0～10。
        :type LoginNodeCount: int
        :param Tags: 创建集群时同时绑定的标签对说明。
        :type Tags: list of Tag
        :param AutoScalingType: 弹性伸缩类型。<br><li>AS：集群自动扩缩容由[弹性伸缩](https://cloud.tencent.com/document/product/377/3154)产品实现。<br><li>THPC_AS：集群自动扩缩容由THPC产品内部实现。
        :type AutoScalingType: str
        """
        self.Placement = None
        self.ManagerNode = None
        self.ManagerNodeCount = None
        self.ComputeNode = None
        self.ComputeNodeCount = None
        self.SchedulerType = None
        self.ImageId = None
        self.VirtualPrivateCloud = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.ClientToken = None
        self.DryRun = None
        self.AccountType = None
        self.ClusterName = None
        self.StorageOption = None
        self.LoginNode = None
        self.LoginNodeCount = None
        self.Tags = None
        self.AutoScalingType = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("ManagerNode") is not None:
            self.ManagerNode = ManagerNode()
            self.ManagerNode._deserialize(params.get("ManagerNode"))
        self.ManagerNodeCount = params.get("ManagerNodeCount")
        if params.get("ComputeNode") is not None:
            self.ComputeNode = ComputeNode()
            self.ComputeNode._deserialize(params.get("ComputeNode"))
        self.ComputeNodeCount = params.get("ComputeNodeCount")
        self.SchedulerType = params.get("SchedulerType")
        self.ImageId = params.get("ImageId")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.ClientToken = params.get("ClientToken")
        self.DryRun = params.get("DryRun")
        self.AccountType = params.get("AccountType")
        self.ClusterName = params.get("ClusterName")
        if params.get("StorageOption") is not None:
            self.StorageOption = StorageOption()
            self.StorageOption._deserialize(params.get("StorageOption"))
        if params.get("LoginNode") is not None:
            self.LoginNode = LoginNode()
            self.LoginNode._deserialize(params.get("LoginNode"))
        self.LoginNodeCount = params.get("LoginNodeCount")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AutoScalingType = params.get("AutoScalingType")
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
        :param ClusterId: 集群ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        r"""
        :param DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[存储概述](https://cloud.tencent.com/document/product/213/4952)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param DiskType: 数据盘类型。数据盘类型限制详见[存储概述](https://cloud.tencent.com/document/product/213/4952)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>LOCAL_NVME：本地NVME硬盘，与InstanceType强相关，不支持指定<br><li>LOCAL_PRO：本地HDD硬盘，与InstanceType强相关，不支持指定<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_HSSD：增强型SSD云硬盘<br><li>CLOUD_TSSD：极速型SSD云硬盘<br><br>默认取值：LOCAL_BASIC。
        :type DiskType: str
        """
        self.DiskSize = None
        self.DiskType = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterRequest(AbstractModel):
    """DeleteCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
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


class DeleteClusterStorageOptionRequest(AbstractModel):
    """DeleteClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param LocalPath: 本地挂载路径。
        :type LocalPath: str
        """
        self.ClusterId = None
        self.LocalPath = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.LocalPath = params.get("LocalPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClusterStorageOptionResponse(AbstractModel):
    """DeleteClusterStorageOption返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNodesRequest(AbstractModel):
    """DeleteNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param NodeIds: 节点ID。
        :type NodeIds: list of str
        """
        self.ClusterId = None
        self.NodeIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNodesResponse(AbstractModel):
    """DeleteNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteQueueRequest(AbstractModel):
    """DeleteQueue请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param QueueName: 队列名称。<br><li>最多支持32个字符。
        :type QueueName: str
        """
        self.ClusterId = None
        self.QueueName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQueueResponse(AbstractModel):
    """DeleteQueue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAutoScalingConfigurationRequest(AbstractModel):
    """DescribeAutoScalingConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。	
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
        


class DescribeAutoScalingConfigurationResponse(AbstractModel):
    """DescribeAutoScalingConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。
        :type ExpansionBusyTime: int
        :param ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。
        :type ShrinkIdleTime: int
        :param QueueConfigs: 扩容队列配置概览列表。
        :type QueueConfigs: list of QueueConfigOverview
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.ExpansionBusyTime = None
        self.ShrinkIdleTime = None
        self.QueueConfigs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ExpansionBusyTime = params.get("ExpansionBusyTime")
        self.ShrinkIdleTime = params.get("ShrinkIdleTime")
        if params.get("QueueConfigs") is not None:
            self.QueueConfigs = []
            for item in params.get("QueueConfigs"):
                obj = QueueConfigOverview()
                obj._deserialize(item)
                self.QueueConfigs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterActivitiesRequest(AbstractModel):
    """DescribeClusterActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。通过该参数指定需要查询活动历史记录的集群。
        :type ClusterId: str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterActivitiesResponse(AbstractModel):
    """DescribeClusterActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterActivitySet: 集群活动历史记录列表。
        :type ClusterActivitySet: list of ClusterActivity
        :param TotalCount: 集群活动历史记录数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterActivitySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterActivitySet") is not None:
            self.ClusterActivitySet = []
            for item in params.get("ClusterActivitySet"):
                obj = ClusterActivity()
                obj._deserialize(item)
                self.ClusterActivitySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeClusterStorageOptionRequest(AbstractModel):
    """DescribeClusterStorageOption请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
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
        


class DescribeClusterStorageOptionResponse(AbstractModel):
    """DescribeClusterStorageOption返回参数结构体

    """

    def __init__(self):
        r"""
        :param StorageOption: 集群存储选项信息概览。
        :type StorageOption: :class:`tencentcloud.thpc.v20220401.models.StorageOptionOverview`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StorageOption = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StorageOption") is not None:
            self.StorageOption = StorageOptionOverview()
            self.StorageOption._deserialize(params.get("StorageOption"))
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterIds: 集群ID列表。通过该参数可以指定需要查询信息的集群列表。<br>如果您不指定该参数，则返回Limit数量以内的集群信息。
        :type ClusterIds: list of str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ClusterIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterIds = params.get("ClusterIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param ClusterSet: 集群概览信息列表。
        :type ClusterSet: list of ClusterOverview
        :param TotalCount: 集群数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = ClusterOverview()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNodesRequest(AbstractModel):
    """DescribeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param Filters: <li><strong>queue-name</strong></li> <p style="padding-left: 30px;">按照【<strong>队列名称</strong>】进行过滤。队列名称形如：compute。</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"><li><strong>node-role</strong></li> <p style="padding-left: 30px;">按照【<strong>节点角色</strong>】进行过滤。节点角色形如：Manager。（Manager：管控节点。Compute：计算节点。Login：登录节点。ManagerBackup：备用管控节点。）</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;"><li><strong>node-type</strong></li> <p style="padding-left: 30px;">按照【<strong>节点类型</strong>】进行过滤。节点类型形如：STATIC。(STATIC：静态节点。DYNAMIC：弹性节点。)</p><p style="padding-left: 30px;">类型：String</p><p style="padding-left: 30px;">必选：否</p><p style="padding-left: 30px;">每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ClusterId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
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
        


class DescribeNodesResponse(AbstractModel):
    """DescribeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param NodeSet: 节点概览信息列表。
        :type NodeSet: list of NodeOverview
        :param TotalCount: 符合条件的节点数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NodeSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = NodeOverview()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeQueuesRequest(AbstractModel):
    """DescribeQueues请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        """
        self.ClusterId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQueuesResponse(AbstractModel):
    """DescribeQueues返回参数结构体

    """

    def __init__(self):
        r"""
        :param QueueSet: 队列概览信息列表。
        :type QueueSet: list of QueueOverview
        :param TotalCount: 符合条件的节点数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QueueSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QueueSet") is not None:
            self.QueueSet = []
            for item in params.get("QueueSet"):
                obj = QueueOverview()
                obj._deserialize(item)
                self.QueueSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ExpansionNodeConfig(AbstractModel):
    """弹性扩容节点配置信息。

    """

    def __init__(self):
        r"""
        :param Placement: 扩容实例所在的位置。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param VirtualPrivateCloud: 私有网络相关信息配置。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        """
        self.Placement = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.VirtualPrivateCloud = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExpansionNodeConfigOverview(AbstractModel):
    """扩容节点配置信息概览。

    """

    def __init__(self):
        r"""
        :param InstanceType: 节点机型。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param Placement: 扩容实例所在的位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Placement: :class:`tencentcloud.thpc.v20220401.models.Placement`
        :param InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param VirtualPrivateCloud: 私有网络相关信息配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPrivateCloud: :class:`tencentcloud.thpc.v20220401.models.VirtualPrivateCloud`
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param InternetAccessible: 公网带宽相关信息设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param SystemDisk: 节点系统盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param DataDisks: 节点数据盘配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataDisks: list of DataDisk
        """
        self.InstanceType = None
        self.Placement = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.VirtualPrivateCloud = None
        self.ImageId = None
        self.InternetAccessible = None
        self.SystemDisk = None
        self.DataDisks = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ImageId = params.get("ImageId")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
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
        


class GooseFSOption(AbstractModel):
    """描述GooseFS挂载信息

    """

    def __init__(self):
        r"""
        :param LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param RemotePath: 文件系统远程挂载路径。
        :type RemotePath: str
        :param Masters: 文件系统master的ip和端口。
        :type Masters: list of str
        """
        self.LocalPath = None
        self.RemotePath = None
        self.Masters = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.RemotePath = params.get("RemotePath")
        self.Masters = params.get("Masters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GooseFSOptionOverview(AbstractModel):
    """GooseFS存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param LocalPath: 文件系统本地挂载路径。
        :type LocalPath: str
        :param RemotePath: 文件系统远程挂载路径。
        :type RemotePath: str
        :param Masters: 文件系统master的ip和端口。
        :type Masters: list of str
        """
        self.LocalPath = None
        self.RemotePath = None
        self.Masters = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.RemotePath = params.get("RemotePath")
        self.Masters = params.get("Masters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    """描述了实例的计费模式

    """

    def __init__(self):
        r"""
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围：
NOTIFY_AND_AUTO_RENEW：通知过期且自动续费
NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：不通知过期不自动续费

默认取值：NOTIFY_AND_MANUAL_RENEW。若该参数指定为NOTIFY_AND_AUTO_RENEW，在账户余额充足的情况下，实例到期后将按月自动续费。
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        r"""
        :param InternetChargeType: 网络计费类型。取值范围：
BANDWIDTH_PREPAID：预付费按带宽结算
TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费
BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费
BANDWIDTH_PACKAGE：带宽包用户
默认取值：非带宽包用户默认与子机付费类型保持一致。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见购买网络带宽。
        :type InternetMaxBandwidthOut: int
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginNode(AbstractModel):
    """登录节点信息。

    """

    def __init__(self):
        r"""
        :param InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: list of SystemDisk
        :param DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: list of InternetAccessible
        :param InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
最多支持60个字符。
        :type InstanceName: str
        """
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = []
            for item in params.get("SystemDisk"):
                obj = SystemDisk()
                obj._deserialize(item)
                self.SystemDisk.append(obj)
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = []
            for item in params.get("InternetAccessible"):
                obj = InternetAccessible()
                obj._deserialize(item)
                self.InternetAccessible.append(obj)
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginNodeOverview(AbstractModel):
    """登录节点概览。

    """

    def __init__(self):
        r"""
        :param NodeId: 登录节点ID。
        :type NodeId: str
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
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
        :type Password: str
        """
        self.Password = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerNode(AbstractModel):
    """管控节点信息

    """

    def __init__(self):
        r"""
        :param InstanceChargeType: 节点[计费类型](https://cloud.tencent.com/document/product/213/2180)。<br><li>PREPAID：预付费，即包年包月<br><li>POSTPAID_BY_HOUR：按小时后付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月节点的购买时长、是否设置自动续费等属性。若指定节点的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.thpc.v20220401.models.InstanceChargePrepaid`
        :param InstanceType: 节点机型。不同实例机型指定了不同的资源规格。
<br><li>对于付费模式为PREPAID或POSTPAID\_BY\_HOUR的实例创建，具体取值可通过调用接口[DescribeInstanceTypeConfigs](https://cloud.tencent.com/document/api/213/15749)来获得最新的规格表或参见[实例规格](https://cloud.tencent.com/document/product/213/11518)描述。
        :type InstanceType: str
        :param SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param InstanceName: 节点显示名称。<br><li>
不指定节点显示名称则默认显示‘未命名’。
</li><li>购买多个节点，如果指定模式串`{R:x}`，表示生成数字[`[x, x+n-1]`，其中`n`表示购买节点的数量，例如`server_{R:3}`，购买1个时，节点显示名称为`server_3`；购买2个时，节点显示名称分别为`server_3`，`server_4`。支持指定多个模式串`{R:x}`。
购买多个节点，如果不指定模式串，则在节点显示名称添加后缀`1、2...n`，其中`n`表示购买节点的数量，例如`server_`，购买2个时，节点显示名称分别为`server_1`，`server_2`。</li><li>
最多支持60个字符（包含模式串）。
        :type InstanceName: str
        """
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerNodeOverview(AbstractModel):
    """管控节点概览。

    """

    def __init__(self):
        r"""
        :param NodeId: 管控节点ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeId: str
        """
        self.NodeId = None


    def _deserialize(self, params):
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeActivity(AbstractModel):
    """节点活动信息。

    """

    def __init__(self):
        r"""
        :param NodeInstanceId: 节点活动所在的实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeInstanceId: str
        :param NodeActivityStatus: 节点活动状态。取值范围：<br><li>RUNNING：运行中<br><li>SUCCESSFUL：活动成功<br><li>FAILED：活动失败
        :type NodeActivityStatus: str
        :param NodeActivityStatusCode: 节点活动状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeActivityStatusCode: str
        :param NodeActivityStatusReason: 节点活动状态原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeActivityStatusReason: str
        """
        self.NodeInstanceId = None
        self.NodeActivityStatus = None
        self.NodeActivityStatusCode = None
        self.NodeActivityStatusReason = None


    def _deserialize(self, params):
        self.NodeInstanceId = params.get("NodeInstanceId")
        self.NodeActivityStatus = params.get("NodeActivityStatus")
        self.NodeActivityStatusCode = params.get("NodeActivityStatusCode")
        self.NodeActivityStatusReason = params.get("NodeActivityStatusReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeOverview(AbstractModel):
    """节点概览信息。

    """

    def __init__(self):
        r"""
        :param InstanceId: 节点实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param Zone: 节点所在可用区信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param NodeState: 节点状态。<br><li>SUBMITTED：已完成提交。<br><li>CREATING：创建中。<br><li>CREATED：完成创建。<br><li>INITING：初始化中。<br><li>INIT_FAILED：初始化失败。<br><li>RUNNING：运行中。<br><li>DELETING：销毁中。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeState: str
        :param ImageId: 镜像ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageId: str
        :param QueueName: 节点所属队列名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        :param NodeRole: 节点角色。<br><li>Manager：管控节点。<br><li>Compute：计算节点。<br><li>Login：登录节点。<br><li>ManagerBackup：备用管控节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeRole: str
        :param NodeType: 节点类型。<br><li>STATIC：静态节点。<br><li>DYNAMIC：弹性节点。
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeType: str
        """
        self.InstanceId = None
        self.Zone = None
        self.NodeState = None
        self.ImageId = None
        self.QueueName = None
        self.NodeRole = None
        self.NodeType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        self.NodeState = params.get("NodeState")
        self.ImageId = params.get("ImageId")
        self.QueueName = params.get("QueueName")
        self.NodeRole = params.get("NodeRole")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Placement(AbstractModel):
    """描述了实例的抽象位置

    """

    def __init__(self):
        r"""
        :param Zone: 实例所属的可用区名称。该参数可以通过调用  [DescribeZones](https://cloud.tencent.com/document/product/213/15707) 的返回值中的Zone字段来获取。
        :type Zone: str
        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueConfig(AbstractModel):
    """扩容队列配置。

    """

    def __init__(self):
        r"""
        :param QueueName: 队列名称。
        :type QueueName: str
        :param MinSize: 队列中弹性节点数量最小值。取值范围0～200。
        :type MinSize: int
        :param MaxSize: 队列中弹性节点数量最大值。取值范围0～200。
        :type MaxSize: int
        :param EnableAutoExpansion: 是否开启自动扩容。
        :type EnableAutoExpansion: bool
        :param EnableAutoShrink: 是否开启自动缩容。
        :type EnableAutoShrink: bool
        :param ImageId: 指定有效的[镜像](https://cloud.tencent.com/document/product/213/4940)ID，格式形如`img-xxx`。目前仅支持公有镜和特定自定义镜像。
        :type ImageId: str
        :param SystemDisk: 节点系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.thpc.v20220401.models.SystemDisk`
        :param DataDisks: 节点数据盘配置信息。若不指定该参数，则默认不购买数据盘。支持购买的时候指定21块数据盘，其中最多包含1块LOCAL_BASIC数据盘或者LOCAL_SSD数据盘，最多包含20块CLOUD_BASIC数据盘、CLOUD_PREMIUM数据盘或者CLOUD_SSD数据盘。
        :type DataDisks: list of DataDisk
        :param InternetAccessible: 公网带宽相关信息设置。若不指定该参数，则默认公网带宽为0Mbps。
        :type InternetAccessible: :class:`tencentcloud.thpc.v20220401.models.InternetAccessible`
        :param ExpansionNodeConfigs: 扩容节点配置信息。
        :type ExpansionNodeConfigs: list of ExpansionNodeConfig
        """
        self.QueueName = None
        self.MinSize = None
        self.MaxSize = None
        self.EnableAutoExpansion = None
        self.EnableAutoShrink = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.InternetAccessible = None
        self.ExpansionNodeConfigs = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.EnableAutoExpansion = params.get("EnableAutoExpansion")
        self.EnableAutoShrink = params.get("EnableAutoShrink")
        self.ImageId = params.get("ImageId")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = SystemDisk()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DataDisk()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("ExpansionNodeConfigs") is not None:
            self.ExpansionNodeConfigs = []
            for item in params.get("ExpansionNodeConfigs"):
                obj = ExpansionNodeConfig()
                obj._deserialize(item)
                self.ExpansionNodeConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueConfigOverview(AbstractModel):
    """扩容队列配置概览。

    """

    def __init__(self):
        r"""
        :param QueueName: 队列名称。
        :type QueueName: str
        :param MinSize: 队列中弹性节点数量最小值。取值范围0～200。
        :type MinSize: int
        :param MaxSize: 队列中弹性节点数量最大值。取值范围0～200。
        :type MaxSize: int
        :param EnableAutoExpansion: 是否开启自动扩容。
        :type EnableAutoExpansion: bool
        :param EnableAutoShrink: 是否开启自动缩容。
        :type EnableAutoShrink: bool
        :param ExpansionNodeConfigs: 扩容节点配置信息。
        :type ExpansionNodeConfigs: list of ExpansionNodeConfigOverview
        """
        self.QueueName = None
        self.MinSize = None
        self.MaxSize = None
        self.EnableAutoExpansion = None
        self.EnableAutoShrink = None
        self.ExpansionNodeConfigs = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")
        self.EnableAutoExpansion = params.get("EnableAutoExpansion")
        self.EnableAutoShrink = params.get("EnableAutoShrink")
        if params.get("ExpansionNodeConfigs") is not None:
            self.ExpansionNodeConfigs = []
            for item in params.get("ExpansionNodeConfigs"):
                obj = ExpansionNodeConfigOverview()
                obj._deserialize(item)
                self.ExpansionNodeConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueueOverview(AbstractModel):
    """队列信息概览。

    """

    def __init__(self):
        r"""
        :param QueueName: 队列名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type QueueName: str
        """
        self.QueueName = None


    def _deserialize(self, params):
        self.QueueName = params.get("QueueName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoScalingConfigurationRequest(AbstractModel):
    """SetAutoScalingConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID。
        :type ClusterId: str
        :param ExpansionBusyTime: 任务连续等待时间，队列的任务处于连续等待的时间。单位秒。默认值120。
        :type ExpansionBusyTime: int
        :param ShrinkIdleTime: 节点连续空闲（未运行作业）时间，一个节点连续处于空闲状态时间。单位秒。默认值300。
        :type ShrinkIdleTime: int
        :param QueueConfigs: 扩容队列配置列表。
        :type QueueConfigs: list of QueueConfig
        :param DryRun: 是否只预检此次请求。
true：发送检查请求，不会绑定弹性伸缩组。检查项包括是否填写了必需参数，请求格式，业务限制。
如果检查不通过，则返回对应错误码；
如果检查通过，则返回RequestId。
false（默认）：发送正常请求，通过检查后直接绑定弹性伸缩组。
        :type DryRun: bool
        """
        self.ClusterId = None
        self.ExpansionBusyTime = None
        self.ShrinkIdleTime = None
        self.QueueConfigs = None
        self.DryRun = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ExpansionBusyTime = params.get("ExpansionBusyTime")
        self.ShrinkIdleTime = params.get("ShrinkIdleTime")
        if params.get("QueueConfigs") is not None:
            self.QueueConfigs = []
            for item in params.get("QueueConfigs"):
                obj = QueueConfig()
                obj._deserialize(item)
                self.QueueConfigs.append(obj)
        self.DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAutoScalingConfigurationResponse(AbstractModel):
    """SetAutoScalingConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StorageOption(AbstractModel):
    """描述集群文件系统选项

    """

    def __init__(self):
        r"""
        :param CFSOptions: 集群挂载CFS文件系统选项。
        :type CFSOptions: list of CFSOption
        :param GooseFSOptions: 集群挂载GooseFS文件系统选项。
        :type GooseFSOptions: list of GooseFSOption
        """
        self.CFSOptions = None
        self.GooseFSOptions = None


    def _deserialize(self, params):
        if params.get("CFSOptions") is not None:
            self.CFSOptions = []
            for item in params.get("CFSOptions"):
                obj = CFSOption()
                obj._deserialize(item)
                self.CFSOptions.append(obj)
        if params.get("GooseFSOptions") is not None:
            self.GooseFSOptions = []
            for item in params.get("GooseFSOptions"):
                obj = GooseFSOption()
                obj._deserialize(item)
                self.GooseFSOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOptionOverview(AbstractModel):
    """集群存储选项概览信息。

    """

    def __init__(self):
        r"""
        :param CFSOptions: CFS存储选项概览信息列表。
        :type CFSOptions: list of CFSOptionOverview
        :param GooseFSOptions: GooseFS存储选项概览信息列表。
        :type GooseFSOptions: list of GooseFSOptionOverview
        """
        self.CFSOptions = None
        self.GooseFSOptions = None


    def _deserialize(self, params):
        if params.get("CFSOptions") is not None:
            self.CFSOptions = []
            for item in params.get("CFSOptions"):
                obj = CFSOptionOverview()
                obj._deserialize(item)
                self.CFSOptions.append(obj)
        if params.get("GooseFSOptions") is not None:
            self.GooseFSOptions = []
            for item in params.get("GooseFSOptions"):
                obj = GooseFSOptionOverview()
                obj._deserialize(item)
                self.GooseFSOptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param DiskType: 系统盘类型。系统盘类型限制详见存储概述。取值范围：
LOCAL_BASIC：本地硬盘
LOCAL_SSD：本地SSD硬盘
CLOUD_BASIC：普通云硬盘
CLOUD_SSD：SSD云硬盘
CLOUD_PREMIUM：高性能云硬盘

默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对。

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
        


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息

    """

    def __init__(self):
        r"""
        :param VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。若在创建子机时VpcId与SubnetId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。若在创建子机时SubnetId与VpcId同时传入`DEFAULT`，则强制使用默认vpc网络。
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        