# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


class Activity(AbstractModel):
    """计算环境的创建或销毁活动

    """

    def __init__(self):
        """
        :param ActivityId: 活动ID
        :type ActivityId: str
        :param ComputeNodeId: 计算节点ID
        :type ComputeNodeId: str
        :param ComputeNodeActivityType: 计算节点活动类型，创建或者销毁
        :type ComputeNodeActivityType: str
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param Cause: 起因
        :type Cause: str
        :param ActivityState: 活动状态
        :type ActivityState: str
        :param StateReason: 状态原因
        :type StateReason: str
        :param StartTime: 活动开始时间
        :type StartTime: str
        :param EndTime: 活动结束时间
        :type EndTime: str
        """
        self.ActivityId = None
        self.ComputeNodeId = None
        self.ComputeNodeActivityType = None
        self.EnvId = None
        self.Cause = None
        self.ActivityState = None
        self.StateReason = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.ComputeNodeId = params.get("ComputeNodeId")
        self.ComputeNodeActivityType = params.get("ComputeNodeActivityType")
        self.EnvId = params.get("EnvId")
        self.Cause = params.get("Cause")
        self.ActivityState = params.get("ActivityState")
        self.StateReason = params.get("StateReason")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class AgentRunningMode(AbstractModel):
    """agent运行模式

    """

    def __init__(self):
        """
        :param Scene: 场景类型，支持WINDOWS
        :type Scene: str
        :param User: 运行Agent的User
        :type User: str
        :param Session: 运行Agent的Session
        :type Session: str
        """
        self.Scene = None
        self.User = None
        self.Session = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.User = params.get("User")
        self.Session = params.get("Session")


class AnonymousComputeEnv(AbstractModel):
    """计算环境

    """

    def __init__(self):
        """
        :param EnvType: 计算环境管理类型
        :type EnvType: str
        :param EnvData: 计算环境具体参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param AgentRunningMode: agent运行模式，适用于Windows系统
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        """
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.AgentRunningMode = None


    def _deserialize(self, params):
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("AgentRunningMode") is not None:
            self.AgentRunningMode = AgentRunningMode()
            self.AgentRunningMode._deserialize(params.get("AgentRunningMode"))


class Application(AbstractModel):
    """应用程序信息

    """

    def __init__(self):
        """
        :param Command: 任务执行命令
        :type Command: str
        :param DeliveryForm: 应用程序的交付方式，包括PACKAGE、LOCAL 两种取值，分别指远程存储的软件包、计算环境本地。
        :type DeliveryForm: str
        :param PackagePath: 应用程序软件包的远程存储路径
        :type PackagePath: str
        :param Docker: 应用使用Docker的相关配置。在使用Docker配置的情况下，DeliveryForm 为 LOCAL 表示直接使用Docker镜像内部的应用软件，通过Docker方式运行；DeliveryForm 为 PACKAGE，表示将远程应用包注入到Docker镜像后，通过Docker方式运行。为避免Docker不同版本的兼容性问题，Docker安装包及相关依赖由Batch统一负责，对于已安装Docker的自定义镜像，请卸载后再使用Docker特性。
        :type Docker: :class:`tencentcloud.batch.v20170312.models.Docker`
        """
        self.Command = None
        self.DeliveryForm = None
        self.PackagePath = None
        self.Docker = None


    def _deserialize(self, params):
        self.Command = params.get("Command")
        self.DeliveryForm = params.get("DeliveryForm")
        self.PackagePath = params.get("PackagePath")
        if params.get("Docker") is not None:
            self.Docker = Docker()
            self.Docker._deserialize(params.get("Docker"))


class Authentication(AbstractModel):
    """授权认证信息

    """

    def __init__(self):
        """
        :param Scene: 授权场景，例如COS
        :type Scene: str
        :param SecretId: SecretId
        :type SecretId: str
        :param SecretKey: SecretKey
        :type SecretKey: str
        """
        self.Scene = None
        self.SecretId = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.SecretId = params.get("SecretId")
        self.SecretKey = params.get("SecretKey")


class ComputeEnvCreateInfo(AbstractModel):
    """计算环境创建信息。

    """

    def __init__(self):
        """
        :param EnvId: 计算环境 ID
        :type EnvId: str
        :param EnvName: 计算环境名称
        :type EnvName: str
        :param EnvDescription: 计算环境描述
        :type EnvDescription: str
        :param EnvType: 计算环境类型，仅支持“MANAGED”类型
        :type EnvType: str
        :param EnvData: 计算环境参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param InputMappings: 输入映射
        :type InputMappings: list of InputMapping
        :param Authentications: 授权信息
        :type Authentications: list of Authentication
        :param Notifications: 通知信息
        :type Notifications: list of Notification
        :param DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        """
        self.EnvId = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.InputMappings = None
        self.Authentications = None
        self.Notifications = None
        self.DesiredComputeNodeCount = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")


class ComputeEnvView(AbstractModel):
    """计算环境信息

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param EnvName: 计算环境名称
        :type EnvName: str
        :param Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ComputeNodeMetrics: 计算节点统计指标
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param EnvType: 计算环境类型
        :type EnvType: str
        :param DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        """
        self.EnvId = None
        self.EnvName = None
        self.Placement = None
        self.CreateTime = None
        self.ComputeNodeMetrics = None
        self.EnvType = None
        self.DesiredComputeNodeCount = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeMetrics") is not None:
            self.ComputeNodeMetrics = ComputeNodeMetrics()
            self.ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self.EnvType = params.get("EnvType")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")


class ComputeNode(AbstractModel):
    """计算节点

    """

    def __init__(self):
        """
        :param ComputeNodeId: 计算节点ID
        :type ComputeNodeId: str
        :param ComputeNodeInstanceId: 计算节点实例ID，对于CVM场景，即为CVM的InstanceId
        :type ComputeNodeInstanceId: str
        :param ComputeNodeState: 计算节点状态
        :type ComputeNodeState: str
        :param Cpu: CPU核数
        :type Cpu: int
        :param Mem: 内存容量，单位GiB
        :type Mem: int
        :param ResourceCreatedTime: 资源创建完成时间
        :type ResourceCreatedTime: str
        :param TaskInstanceNumAvailable: 计算节点运行  TaskInstance 可用容量。0表示计算节点忙碌。
        :type TaskInstanceNumAvailable: int
        :param AgentVersion: Batch Agent 版本
        :type AgentVersion: str
        :param PrivateIpAddresses: 实例内网IP
        :type PrivateIpAddresses: list of str
        :param PublicIpAddresses: 实例公网IP
        :type PublicIpAddresses: list of str
        """
        self.ComputeNodeId = None
        self.ComputeNodeInstanceId = None
        self.ComputeNodeState = None
        self.Cpu = None
        self.Mem = None
        self.ResourceCreatedTime = None
        self.TaskInstanceNumAvailable = None
        self.AgentVersion = None
        self.PrivateIpAddresses = None
        self.PublicIpAddresses = None


    def _deserialize(self, params):
        self.ComputeNodeId = params.get("ComputeNodeId")
        self.ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self.ComputeNodeState = params.get("ComputeNodeState")
        self.Cpu = params.get("Cpu")
        self.Mem = params.get("Mem")
        self.ResourceCreatedTime = params.get("ResourceCreatedTime")
        self.TaskInstanceNumAvailable = params.get("TaskInstanceNumAvailable")
        self.AgentVersion = params.get("AgentVersion")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.PublicIpAddresses = params.get("PublicIpAddresses")


class ComputeNodeMetrics(AbstractModel):
    """计算节点统计指标

    """

    def __init__(self):
        """
        :param SubmittedCount: 已经完成提交的计算节点数量
        :type SubmittedCount: str
        :param CreatingCount: 创建中的计算节点数量
        :type CreatingCount: str
        :param CreationFailedCount: 创建失败的计算节点数量
        :type CreationFailedCount: str
        :param CreatedCount: 完成创建的计算节点数量
        :type CreatedCount: str
        :param RunningCount: 运行中的计算节点数量
        :type RunningCount: str
        :param DeletingCount: 销毁中的计算节点数量
        :type DeletingCount: str
        :param AbnormalCount: 异常的计算节点数量
        :type AbnormalCount: str
        """
        self.SubmittedCount = None
        self.CreatingCount = None
        self.CreationFailedCount = None
        self.CreatedCount = None
        self.RunningCount = None
        self.DeletingCount = None
        self.AbnormalCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.CreatingCount = params.get("CreatingCount")
        self.CreationFailedCount = params.get("CreationFailedCount")
        self.CreatedCount = params.get("CreatedCount")
        self.RunningCount = params.get("RunningCount")
        self.DeletingCount = params.get("DeletingCount")
        self.AbnormalCount = params.get("AbnormalCount")


class CreateComputeEnvRequest(AbstractModel):
    """CreateComputeEnv请求参数结构体

    """

    def __init__(self):
        """
        :param ComputeEnv: 计算环境信息
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.NamedComputeEnv`
        :param Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        """
        self.ComputeEnv = None
        self.Placement = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = NamedComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.ClientToken = params.get("ClientToken")


class CreateComputeEnvResponse(AbstractModel):
    """CreateComputeEnv返回参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.RequestId = params.get("RequestId")


class CreateTaskTemplateRequest(AbstractModel):
    """CreateTaskTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TaskTemplateName: 任务模板名称
        :type TaskTemplateName: str
        :param TaskTemplateInfo: 任务模板内容，参数要求与任务一致
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param TaskTemplateDescription: 任务模板描述
        :type TaskTemplateDescription: str
        """
        self.TaskTemplateName = None
        self.TaskTemplateInfo = None
        self.TaskTemplateDescription = None


    def _deserialize(self, params):
        self.TaskTemplateName = params.get("TaskTemplateName")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")


class CreateTaskTemplateResponse(AbstractModel):
    """CreateTaskTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param TaskTemplateId: 任务模板ID
        :type TaskTemplateId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskTemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.RequestId = params.get("RequestId")


class DataDisk(AbstractModel):
    """描述了数据盘的信息

    """

    def __init__(self):
        """
        :param DiskSize: 数据盘大小，单位：GB。最小调整步长为10G，不同数据盘类型取值范围不同，具体限制详见：[CVM实例配置](/document/product/213/2177)。默认值为0，表示不购买数据盘。更多限制详见产品文档。
        :type DiskSize: int
        :param DiskType: 数据盘类型。数据盘类型限制详见[CVM实例配置](/document/product/213/2177)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><br>默认取值：LOCAL_BASIC。<br><br>该参数对`ResizeInstanceDisk`接口无效。
        :type DiskType: str
        :param DiskId: 数据盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。
        :type DiskId: str
        """
        self.DiskSize = None
        self.DiskType = None
        self.DiskId = None


    def _deserialize(self, params):
        self.DiskSize = params.get("DiskSize")
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")


class DeleteComputeEnvRequest(AbstractModel):
    """DeleteComputeEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DeleteComputeEnvResponse(AbstractModel):
    """DeleteComputeEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTaskTemplatesRequest(AbstractModel):
    """DeleteTaskTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param TaskTemplateIds: 用于删除任务模板信息
        :type TaskTemplateIds: list of str
        """
        self.TaskTemplateIds = None


    def _deserialize(self, params):
        self.TaskTemplateIds = params.get("TaskTemplateIds")


class DeleteTaskTemplatesResponse(AbstractModel):
    """DeleteTaskTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Dependence(AbstractModel):
    """依赖关系

    """

    def __init__(self):
        """
        :param StartTask: 依赖关系的起点任务名称
        :type StartTask: str
        :param EndTask: 依赖关系的终点任务名称
        :type EndTask: str
        """
        self.StartTask = None
        self.EndTask = None


    def _deserialize(self, params):
        self.StartTask = params.get("StartTask")
        self.EndTask = params.get("EndTask")


class DescribeAvailableCvmInstanceTypesRequest(AbstractModel):
    """DescribeAvailableCvmInstanceTypes请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeAvailableCvmInstanceTypesResponse(AbstractModel):
    """DescribeAvailableCvmInstanceTypes返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceTypeConfigSet: 机型配置数组
        :type InstanceTypeConfigSet: list of InstanceTypeConfig
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvActivitiesRequest(AbstractModel):
    """DescribeComputeEnvActivities请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: u8ba1u7b97u73afu5883ID
        :type EnvId: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        :param Filters: 过滤条件
        :type Filters: :class:`tencentcloud.batch.v20170312.models.Filter`
        """
        self.EnvId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))


class DescribeComputeEnvActivitiesResponse(AbstractModel):
    """DescribeComputeEnvActivities返回参数结构体

    """

    def __init__(self):
        """
        :param ActivitySet: 计算环境中的活动列表
        :type ActivitySet: list of Activity
        :param TotalCount: 活动数量
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ActivitySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ActivitySet") is not None:
            self.ActivitySet = []
            for item in params.get("ActivitySet"):
                obj = Activity()
                obj._deserialize(item)
                self.ActivitySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfoRequest(AbstractModel):
    """DescribeComputeEnvCreateInfo请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeComputeEnvCreateInfoResponse(AbstractModel):
    """DescribeComputeEnvCreateInfo返回参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境 ID
        :type EnvId: str
        :param EnvName: 计算环境名称
        :type EnvName: str
        :param EnvDescription: 计算环境描述
        :type EnvDescription: str
        :param EnvType: 计算环境类型，仅支持“MANAGED”类型
        :type EnvType: str
        :param EnvData: 计算环境参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param InputMappings: 输入映射
        :type InputMappings: list of InputMapping
        :param Authentications: 授权信息
        :type Authentications: list of Authentication
        :param Notifications: 通知信息
        :type Notifications: list of Notification
        :param DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.EnvName = None
        self.EnvDescription = None
        self.EnvType = None
        self.EnvData = None
        self.MountDataDisks = None
        self.InputMappings = None
        self.Authentications = None
        self.Notifications = None
        self.DesiredComputeNodeCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        self.EnvDescription = params.get("EnvDescription")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvCreateInfosRequest(AbstractModel):
    """DescribeComputeEnvCreateInfos请求参数结构体

    """

    def __init__(self):
        """
        :param EnvIds: 计算环境ID
        :type EnvIds: list of str
        :param Filters: 过滤条件
<li> zone - String - 是否必填：否 -（过滤条件）按照可用区过滤。</li>
<li> env-id - String - 是否必填：否 -（过滤条件）按照计算环境ID过滤。</li>
<li> env-name - String - 是否必填：否 -（过滤条件）按照计算环境名称过滤。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.EnvIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvIds = params.get("EnvIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeComputeEnvCreateInfosResponse(AbstractModel):
    """DescribeComputeEnvCreateInfos返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 计算环境数量
        :type TotalCount: int
        :param ComputeEnvCreateInfoSet: 计算环境创建信息列表
        :type ComputeEnvCreateInfoSet: list of ComputeEnvCreateInfo
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ComputeEnvCreateInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ComputeEnvCreateInfoSet") is not None:
            self.ComputeEnvCreateInfoSet = []
            for item in params.get("ComputeEnvCreateInfoSet"):
                obj = ComputeEnvCreateInfo()
                obj._deserialize(item)
                self.ComputeEnvCreateInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvRequest(AbstractModel):
    """DescribeComputeEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        """
        self.EnvId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")


class DescribeComputeEnvResponse(AbstractModel):
    """DescribeComputeEnv返回参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param EnvName: 计算环境名称
        :type EnvName: str
        :param Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param CreateTime: 计算环境创建时间
        :type CreateTime: str
        :param ComputeNodeSet: 计算节点列表信息
        :type ComputeNodeSet: list of ComputeNode
        :param ComputeNodeMetrics: 计算节点统计指标
        :type ComputeNodeMetrics: :class:`tencentcloud.batch.v20170312.models.ComputeNodeMetrics`
        :param DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param EnvType: 计算环境类型
        :type EnvType: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.EnvId = None
        self.EnvName = None
        self.Placement = None
        self.CreateTime = None
        self.ComputeNodeSet = None
        self.ComputeNodeMetrics = None
        self.DesiredComputeNodeCount = None
        self.EnvType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.EnvName = params.get("EnvName")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        if params.get("ComputeNodeSet") is not None:
            self.ComputeNodeSet = []
            for item in params.get("ComputeNodeSet"):
                obj = ComputeNode()
                obj._deserialize(item)
                self.ComputeNodeSet.append(obj)
        if params.get("ComputeNodeMetrics") is not None:
            self.ComputeNodeMetrics = ComputeNodeMetrics()
            self.ComputeNodeMetrics._deserialize(params.get("ComputeNodeMetrics"))
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvType = params.get("EnvType")
        self.RequestId = params.get("RequestId")


class DescribeComputeEnvsRequest(AbstractModel):
    """DescribeComputeEnvs请求参数结构体

    """

    def __init__(self):
        """
        :param EnvIds: 计算环境ID
        :type EnvIds: list of str
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.EnvIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EnvIds = params.get("EnvIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeComputeEnvsResponse(AbstractModel):
    """DescribeComputeEnvs返回参数结构体

    """

    def __init__(self):
        """
        :param ComputeEnvSet: 计算环境列表
        :type ComputeEnvSet: list of ComputeEnvView
        :param TotalCount: 计算环境数量
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ComputeEnvSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ComputeEnvSet") is not None:
            self.ComputeEnvSet = []
            for item in params.get("ComputeEnvSet"):
                obj = ComputeEnvView()
                obj._deserialize(item)
                self.ComputeEnvSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCvmZoneInstanceConfigInfosRequest(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件
        :type Filters: :class:`tencentcloud.batch.v20170312.models.Filter`
        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))


class DescribeCvmZoneInstanceConfigInfosResponse(AbstractModel):
    """DescribeCvmZoneInstanceConfigInfos返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceTypeQuotaSet: 可用区机型配置列表。
        :type InstanceTypeQuotaSet: list of InstanceTypeQuotaItem
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.InstanceTypeQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceTypeQuotaSet") is not None:
            self.InstanceTypeQuotaSet = []
            for item in params.get("InstanceTypeQuotaSet"):
                obj = InstanceTypeQuotaItem()
                obj._deserialize(item)
                self.InstanceTypeQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobRequest(AbstractModel):
    """DescribeJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业标识
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeJobResponse(AbstractModel):
    """DescribeJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        :param JobName: 作业名称
        :type JobName: str
        :param Zone: 可用区信息
        :type Zone: str
        :param Priority: 作业优先级
        :type Priority: int
        :param JobState: 作业状态
        :type JobState: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param TaskSet: 任务视图信息
        :type TaskSet: list of TaskView
        :param DependenceSet: 任务间依赖信息
        :type DependenceSet: list of Dependence
        :param TaskMetrics: 任务统计指标
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        :param TaskInstanceMetrics: 任务实例统计指标
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceView`
        :param StateReason: 作业失败原因
        :type StateReason: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.Zone = None
        self.Priority = None
        self.JobState = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskSet = None
        self.DependenceSet = None
        self.TaskMetrics = None
        self.TaskInstanceMetrics = None
        self.StateReason = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.Zone = params.get("Zone")
        self.Priority = params.get("Priority")
        self.JobState = params.get("JobState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskView()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        if params.get("DependenceSet") is not None:
            self.DependenceSet = []
            for item in params.get("DependenceSet"):
                obj = Dependence()
                obj._deserialize(item)
                self.DependenceSet.append(obj)
        if params.get("TaskMetrics") is not None:
            self.TaskMetrics = TaskMetrics()
            self.TaskMetrics._deserialize(params.get("TaskMetrics"))
        if params.get("TaskInstanceMetrics") is not None:
            self.TaskInstanceMetrics = TaskInstanceView()
            self.TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self.StateReason = params.get("StateReason")
        self.RequestId = params.get("RequestId")


class DescribeJobSubmitInfoRequest(AbstractModel):
    """DescribeJobSubmitInfo请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class DescribeJobSubmitInfoResponse(AbstractModel):
    """DescribeJobSubmitInfo返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        :param JobName: 作业名称
        :type JobName: str
        :param JobDescription: 作业描述
        :type JobDescription: str
        :param Priority: 作业优先级，任务（Task）和任务实例（TaskInstance）会继承作业优先级
        :type Priority: int
        :param Tasks: 任务信息
        :type Tasks: list of Task
        :param Dependences: 依赖信息
        :type Dependences: list of Dependence
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.JobName = None
        self.JobDescription = None
        self.Priority = None
        self.Tasks = None
        self.Dependences = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobDescription = params.get("JobDescription")
        self.Priority = params.get("Priority")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        if params.get("Dependences") is not None:
            self.Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self.Dependences.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeJobsRequest(AbstractModel):
    """DescribeJobs请求参数结构体

    """

    def __init__(self):
        """
        :param JobIds: 作业ID
        :type JobIds: list of str
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.JobIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.JobIds = params.get("JobIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeJobsResponse(AbstractModel):
    """DescribeJobs返回参数结构体

    """

    def __init__(self):
        """
        :param JobSet: 作业列表
        :type JobSet: :class:`tencentcloud.batch.v20170312.models.JobView`
        :param TotalCount: 符合条件的作业数量
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("JobSet") is not None:
            self.JobSet = JobView()
            self.JobSet._deserialize(params.get("JobSet"))
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskRequest(AbstractModel):
    """DescribeTask请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        :param TaskName: 任务名称
        :type TaskName: str
        """
        self.JobId = None
        self.TaskName = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")


class DescribeTaskResponse(AbstractModel):
    """DescribeTask返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param TaskState: 任务状态
        :type TaskState: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param TaskInstanceTotalCount: 任务实例总数
        :type TaskInstanceTotalCount: int
        :param TaskInstanceSet: 任务实例信息
        :type TaskInstanceSet: list of TaskInstanceView
        :param TaskInstanceMetrics: 任务实例统计指标
        :type TaskInstanceMetrics: :class:`tencentcloud.batch.v20170312.models.TaskInstanceMetrics`
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.TaskName = None
        self.TaskState = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskInstanceTotalCount = None
        self.TaskInstanceSet = None
        self.TaskInstanceMetrics = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskState = params.get("TaskState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        self.TaskInstanceTotalCount = params.get("TaskInstanceTotalCount")
        if params.get("TaskInstanceSet") is not None:
            self.TaskInstanceSet = []
            for item in params.get("TaskInstanceSet"):
                obj = TaskInstanceView()
                obj._deserialize(item)
                self.TaskInstanceSet.append(obj)
        if params.get("TaskInstanceMetrics") is not None:
            self.TaskInstanceMetrics = TaskInstanceMetrics()
            self.TaskInstanceMetrics._deserialize(params.get("TaskInstanceMetrics"))
        self.RequestId = params.get("RequestId")


class DescribeTaskTemplatesRequest(AbstractModel):
    """DescribeTaskTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param TaskTemplateIds: 任务模板ID
        :type TaskTemplateIds: list of str
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.TaskTemplateIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TaskTemplateIds = params.get("TaskTemplateIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTaskTemplatesResponse(AbstractModel):
    """DescribeTaskTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TaskTemplateSet: 任务模板列表
        :type TaskTemplateSet: list of TaskTemplateView
        :param TotalCount: 任务模板数量
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TaskTemplateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskTemplateSet") is not None:
            self.TaskTemplateSet = []
            for item in params.get("TaskTemplateSet"):
                obj = TaskTemplateView()
                obj._deserialize(item)
                self.TaskTemplateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Docker(AbstractModel):
    """Docker容器信息

    """

    def __init__(self):
        """
        :param User: Docker Hub 用户名或 Tencent Registry 用户名
        :type User: str
        :param Password: Docker Hub 密码或 Tencent Registry 密码
        :type Password: str
        :param Image: Docker Hub填写“[user/repo]:[tag]”，Tencent Registry填写“ccr.ccs.tencentyun.com/[namespace/repo]:[tag]”
        :type Image: str
        :param Server: Docker Hub 可以不填，但确保具有公网访问能力。或者是 Tencent Registry 服务地址“ccr.ccs.tencentyun.com”
        :type Server: str
        """
        self.User = None
        self.Password = None
        self.Image = None
        self.Server = None


    def _deserialize(self, params):
        self.User = params.get("User")
        self.Password = params.get("Password")
        self.Image = params.get("Image")
        self.Server = params.get("Server")


class EnhancedService(AbstractModel):
    """描述了实例的增强服务启用情况与其设置，如云安全，云监控等实例 Agent

    """

    def __init__(self):
        """
        :param SecurityService: 开启云安全服务。若不指定该参数，则默认开启云安全服务。
        :type SecurityService: :class:`tencentcloud.batch.v20170312.models.RunSecurityServiceEnabled`
        :param MonitorService: 开启云安全服务。若不指定该参数，则默认开启云监控服务。
        :type MonitorService: :class:`tencentcloud.batch.v20170312.models.RunMonitorServiceEnabled`
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


class EnvData(AbstractModel):
    """计算环境数据

    """

    def __init__(self):
        """
        :param InstanceType: CVM实例类型
        :type InstanceType: str
        :param ImageId: CVM镜像ID
        :type ImageId: str
        :param SystemDisk: 实例系统盘配置信息
        :type SystemDisk: :class:`tencentcloud.batch.v20170312.models.SystemDisk`
        :param DataDisks: 实例数据盘配置信息
        :type DataDisks: list of DataDisk
        :param VirtualPrivateCloud: 私有网络相关信息配置
        :type VirtualPrivateCloud: :class:`tencentcloud.batch.v20170312.models.VirtualPrivateCloud`
        :param InternetAccessible: 公网带宽相关信息设置
        :type InternetAccessible: :class:`tencentcloud.batch.v20170312.models.InternetAccessible`
        :param InstanceName: CVM实例显示名称
        :type InstanceName: str
        :param LoginSettings: 实例登录设置
        :type LoginSettings: :class:`tencentcloud.batch.v20170312.models.LoginSettings`
        :param SecurityGroupIds: 实例所属安全组
        :type SecurityGroupIds: list of str
        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认开启云监控、云安全服务。
        :type EnhancedService: :class:`tencentcloud.batch.v20170312.models.EnhancedService`
        :param InstanceChargeType: CVM实例计费类型<br><li>POSTPAID_BY_HOUR：按小时后付费<br><li>SPOTPAID：竞价付费<br>默认值：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        :param InstanceMarketOptions: 实例的市场相关选项，如竞价实例相关参数
        :type InstanceMarketOptions: :class:`tencentcloud.batch.v20170312.models.InstanceMarketOptionsRequest`
        """
        self.InstanceType = None
        self.ImageId = None
        self.SystemDisk = None
        self.DataDisks = None
        self.VirtualPrivateCloud = None
        self.InternetAccessible = None
        self.InstanceName = None
        self.LoginSettings = None
        self.SecurityGroupIds = None
        self.EnhancedService = None
        self.InstanceChargeType = None
        self.InstanceMarketOptions = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
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
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = InternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        self.InstanceName = params.get("InstanceName")
        if params.get("LoginSettings") is not None:
            self.LoginSettings = LoginSettings()
            self.LoginSettings._deserialize(params.get("LoginSettings"))
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceMarketOptions") is not None:
            self.InstanceMarketOptions = InstanceMarketOptionsRequest()
            self.InstanceMarketOptions._deserialize(params.get("InstanceMarketOptions"))


class EnvVar(AbstractModel):
    """环境变量

    """

    def __init__(self):
        """
        :param Name: 环境变量名称
        :type Name: str
        :param Value: 环境变量取值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class EventConfig(AbstractModel):
    """事件配置

    """

    def __init__(self):
        """
        :param EventName: 事件类型
        :type EventName: str
        :param EventVars: 自定义键值对
        :type EventVars: list of EventVar
        """
        self.EventName = None
        self.EventVars = None


    def _deserialize(self, params):
        self.EventName = params.get("EventName")
        if params.get("EventVars") is not None:
            self.EventVars = []
            for item in params.get("EventVars"):
                obj = EventVar()
                obj._deserialize(item)
                self.EventVars.append(obj)


class EventVar(AbstractModel):
    """自定义键值对

    """

    def __init__(self):
        """
        :param Name: 自定义键
        :type Name: str
        :param Value: 自定义值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class Externals(AbstractModel):
    """扩展数据

    """

    def __init__(self):
        """
        :param ReleaseAddress: 释放地址
        :type ReleaseAddress: bool
        :param UnsupportNetworks: 不支持的网络类型
        :type UnsupportNetworks: list of str
        :param StorageBlockAttr: HDD本地存储属性
        :type StorageBlockAttr: :class:`tencentcloud.batch.v20170312.models.StorageBlock`
        """
        self.ReleaseAddress = None
        self.UnsupportNetworks = None
        self.StorageBlockAttr = None


    def _deserialize(self, params):
        self.ReleaseAddress = params.get("ReleaseAddress")
        self.UnsupportNetworks = params.get("UnsupportNetworks")
        if params.get("StorageBlockAttr") is not None:
            self.StorageBlockAttr = StorageBlock()
            self.StorageBlockAttr._deserialize(params.get("StorageBlockAttr"))


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeInstances](https://cloud.tencent.com/document/api/213/9388)接口的`Filter`为例。若我们需要查询可用区（`zone`）为广州一区 ***并且*** 实例计费模式（`instance-charge-type`）为包年包月 ***或者*** 按量计费的实例时，可如下实现：
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


class InputMapping(AbstractModel):
    """输入映射

    """

    def __init__(self):
        """
        :param SourcePath: 源端路径
        :type SourcePath: str
        :param DestinationPath: 目的端路径
        :type DestinationPath: str
        :param MountOptionParameter: 挂载配置项参数
        :type MountOptionParameter: str
        """
        self.SourcePath = None
        self.DestinationPath = None
        self.MountOptionParameter = None


    def _deserialize(self, params):
        self.SourcePath = params.get("SourcePath")
        self.DestinationPath = params.get("DestinationPath")
        self.MountOptionParameter = params.get("MountOptionParameter")


class InstanceMarketOptionsRequest(AbstractModel):
    """竞价请求相关选项

    """

    def __init__(self):
        """
        :param MarketType: 市场选项类型，当前只支持取值：spot
        :type MarketType: str
        :param SpotOptions: 竞价相关选项
        :type SpotOptions: :class:`tencentcloud.batch.v20170312.models.SpotMarketOptions`
        """
        self.MarketType = None
        self.SpotOptions = None


    def _deserialize(self, params):
        self.MarketType = params.get("MarketType")
        if params.get("SpotOptions") is not None:
            self.SpotOptions = SpotMarketOptions()
            self.SpotOptions._deserialize(params.get("SpotOptions"))


class InstanceTypeConfig(AbstractModel):
    """描述实例机型配置信息

    """

    def __init__(self):
        """
        :param Zone: 可用区。
        :type Zone: str
        :param InstanceType: 实例机型。
        :type InstanceType: str
        :param InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param GPU: GPU核数，单位：核。
        :type GPU: int
        :param CPU: CPU核数，单位：核。
        :type CPU: int
        :param Memory: 内存容量，单位：`GB`。
        :type Memory: int
        :param CbsSupport: 是否支持云硬盘。取值范围：<br><li>`TRUE`：表示支持云硬盘；<br><li>`FALSE`：表示不支持云硬盘。
        :type CbsSupport: str
        :param InstanceTypeState: 机型状态。取值范围：<br><li>`AVAILABLE`：表示机型可用；<br><li>`UNAVAILABLE`：表示机型不可用。
        :type InstanceTypeState: str
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceFamily = None
        self.GPU = None
        self.CPU = None
        self.Memory = None
        self.CbsSupport = None
        self.InstanceTypeState = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceFamily = params.get("InstanceFamily")
        self.GPU = params.get("GPU")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.CbsSupport = params.get("CbsSupport")
        self.InstanceTypeState = params.get("InstanceTypeState")


class InstanceTypeQuotaItem(AbstractModel):
    """描述实例机型配额信息。

    """

    def __init__(self):
        """
        :param Zone: 可用区。
        :type Zone: str
        :param InstanceType: 实例机型。
        :type InstanceType: str
        :param InstanceChargeType: 实例计费模式。取值范围： <br><li>PREPAID：表示预付费，即包年包月<br><li>POSTPAID_BY_HOUR：表示后付费，即按量计费<br><li>CDHPAID：表示[CDH](https://cloud.tencent.com/document/product/416)付费，即只对CDH计费，不对CDH上的实例计费。
        :type InstanceChargeType: str
        :param NetworkCard: 网卡类型，例如：25代表25G网卡
        :type NetworkCard: int
        :param Externals: 扩展属性。
        :type Externals: :class:`tencentcloud.batch.v20170312.models.Externals`
        :param Cpu: 实例的CPU核数，单位：核。
        :type Cpu: int
        :param Memory: 实例内存容量，单位：`GB`。
        :type Memory: int
        :param InstanceFamily: 实例机型系列。
        :type InstanceFamily: str
        :param TypeName: 机型名称。
        :type TypeName: str
        :param LocalDiskTypeList: 本地磁盘规格列表。
        :type LocalDiskTypeList: list of LocalDiskType
        :param Status: 实例是否售卖。
        :type Status: str
        :param Price: 实例的售卖价格。
        :type Price: :class:`tencentcloud.batch.v20170312.models.ItemPrice`
        """
        self.Zone = None
        self.InstanceType = None
        self.InstanceChargeType = None
        self.NetworkCard = None
        self.Externals = None
        self.Cpu = None
        self.Memory = None
        self.InstanceFamily = None
        self.TypeName = None
        self.LocalDiskTypeList = None
        self.Status = None
        self.Price = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceType = params.get("InstanceType")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.NetworkCard = params.get("NetworkCard")
        if params.get("Externals") is not None:
            self.Externals = Externals()
            self.Externals._deserialize(params.get("Externals"))
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceFamily = params.get("InstanceFamily")
        self.TypeName = params.get("TypeName")
        if params.get("LocalDiskTypeList") is not None:
            self.LocalDiskTypeList = []
            for item in params.get("LocalDiskTypeList"):
                obj = LocalDiskType()
                obj._deserialize(item)
                self.LocalDiskTypeList.append(obj)
        self.Status = params.get("Status")
        if params.get("Price") is not None:
            self.Price = ItemPrice()
            self.Price._deserialize(params.get("Price"))


class InternetAccessible(AbstractModel):
    """描述了实例的公网可访问性，声明了实例的公网使用计费模式，最大带宽等

    """

    def __init__(self):
        """
        :param InternetChargeType: 网络计费类型。取值范围：<br><li>BANDWIDTH_PREPAID：预付费按带宽结算<br><li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费<br><li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费<br><li>BANDWIDTH_PACKAGE：带宽包用户<br>默认取值：TRAFFIC_POSTPAID_BY_HOUR。
        :type InternetChargeType: str
        :param InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。默认值：0Mbps。不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](/document/product/213/509)。
        :type InternetMaxBandwidthOut: int
        :param PublicIpAssigned: 是否分配公网IP。取值范围：<br><li>TRUE：表示分配公网IP<br><li>FALSE：表示不分配公网IP<br><br>当公网带宽大于0Mbps时，可自由选择开通与否，默认开通公网IP；当公网带宽为0，则不允许分配公网IP。
        :type PublicIpAssigned: bool
        """
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.PublicIpAssigned = None


    def _deserialize(self, params):
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.PublicIpAssigned = params.get("PublicIpAssigned")


class ItemPrice(AbstractModel):
    """描述了单项的价格信息

    """

    def __init__(self):
        """
        :param UnitPrice: 后续单价，单位：元。
        :type UnitPrice: float
        :param ChargeUnit: 后续计价单元，可取值范围： <br><li>HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）：<br><li>GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。
        :type ChargeUnit: str
        :param OriginalPrice: 预支费用的原价，单位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 预支费用的折扣价，单位：元。
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class Job(AbstractModel):
    """作业

    """

    def __init__(self):
        """
        :param JobName: 作业名称
        :type JobName: str
        :param Priority: 作业优先级，任务（Task）和任务实例（TaskInstance）会继承作业优先级
        :type Priority: int
        :param Tasks: 任务信息
        :type Tasks: list of Task
        :param JobDescription: 作业描述
        :type JobDescription: str
        :param Dependences: 依赖信息
        :type Dependences: list of Dependence
        :param Notifications: 通知信息
        :type Notifications: list of Notification
        :param TaskExecutionDependOn: 对于存在依赖关系的任务中，后序任务执行对于前序任务的依赖条件。取值范围包括 PRE_TASK_SUCCEED，PRE_TASK_AT_LEAST_PARTLY_SUCCEED，PRE_TASK_FINISHED，默认值为PRE_TASK_SUCCEED。
        :type TaskExecutionDependOn: str
        :param StateIfCreateCvmFailed: 表示创建 CVM 失败按照何种策略处理。取值范围包括 FAILED，RUNNABLE。FAILED 表示创建 CVM 失败按照一次执行失败处理，RUNNABLE 表示创建 CVM 失败按照继续等待处理。默认值为FAILED。StateIfCreateCvmFailed对于提交的指定计算环境的作业无效。
        :type StateIfCreateCvmFailed: str
        """
        self.JobName = None
        self.Priority = None
        self.Tasks = None
        self.JobDescription = None
        self.Dependences = None
        self.Notifications = None
        self.TaskExecutionDependOn = None
        self.StateIfCreateCvmFailed = None


    def _deserialize(self, params):
        self.JobName = params.get("JobName")
        self.Priority = params.get("Priority")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = Task()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.JobDescription = params.get("JobDescription")
        if params.get("Dependences") is not None:
            self.Dependences = []
            for item in params.get("Dependences"):
                obj = Dependence()
                obj._deserialize(item)
                self.Dependences.append(obj)
        if params.get("Notifications") is not None:
            self.Notifications = []
            for item in params.get("Notifications"):
                obj = Notification()
                obj._deserialize(item)
                self.Notifications.append(obj)
        self.TaskExecutionDependOn = params.get("TaskExecutionDependOn")
        self.StateIfCreateCvmFailed = params.get("StateIfCreateCvmFailed")


class JobView(AbstractModel):
    """作业信息

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        :param JobName: 作业名称
        :type JobName: str
        :param JobState: 作业状态
        :type JobState: str
        :param Priority: 作业优先级
        :type Priority: int
        :param Placement: 位置信息
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param TaskMetrics: 任务统计指标
        :type TaskMetrics: :class:`tencentcloud.batch.v20170312.models.TaskMetrics`
        """
        self.JobId = None
        self.JobName = None
        self.JobState = None
        self.Priority = None
        self.Placement = None
        self.CreateTime = None
        self.EndTime = None
        self.TaskMetrics = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.JobName = params.get("JobName")
        self.JobState = params.get("JobState")
        self.Priority = params.get("Priority")
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")
        if params.get("TaskMetrics") is not None:
            self.TaskMetrics = TaskMetrics()
            self.TaskMetrics._deserialize(params.get("TaskMetrics"))


class LocalDiskType(AbstractModel):
    """本地磁盘规格

    """

    def __init__(self):
        """
        :param Type: 本地磁盘类型。
        :type Type: str
        :param PartitionType: 本地磁盘属性。
        :type PartitionType: str
        :param MinSize: 本地磁盘最小值。
        :type MinSize: int
        :param MaxSize: 本地磁盘最大值。
        :type MaxSize: int
        """
        self.Type = None
        self.PartitionType = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.PartitionType = params.get("PartitionType")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class LoginSettings(AbstractModel):
    """描述了实例登录相关配置与信息。

    """

    def __init__(self):
        """
        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：<br><li>Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = | { } [ ] : ; ' , . ? / ]中的特殊符号。<br><li>Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & * - + = { } [ ] : ; ' , . ? /]中的特殊符号。<br><br>若不指定该参数，则由系统随机生成密码，并通过站内信方式通知到用户。
        :type Password: str
        :param KeyIds: 密钥ID列表。关联密钥后，就可以通过对应的私钥来访问实例；KeyId可通过接口DescribeKeyPairs获取，密钥与密码不能同时指定，同时Windows操作系统不支持指定密钥。当前仅支持购买的时候指定一个密钥。
        :type KeyIds: list of str
        :param KeepImageLogin: 保持镜像的原始设置。该参数与Password或KeyIds.N不能同时指定。只有使用自定义镜像、共享镜像或外部导入镜像创建实例时才能指定该参数为TRUE。取值范围：<br><li>TRUE：表示保持镜像的登录设置<br><li>FALSE：表示不保持镜像的登录设置<br><br>默认取值：FALSE。
        :type KeepImageLogin: str
        """
        self.Password = None
        self.KeyIds = None
        self.KeepImageLogin = None


    def _deserialize(self, params):
        self.Password = params.get("Password")
        self.KeyIds = params.get("KeyIds")
        self.KeepImageLogin = params.get("KeepImageLogin")


class ModifyComputeEnvRequest(AbstractModel):
    """ModifyComputeEnv请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        """
        self.EnvId = None
        self.DesiredComputeNodeCount = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")


class ModifyComputeEnvResponse(AbstractModel):
    """ModifyComputeEnv返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTaskTemplateRequest(AbstractModel):
    """ModifyTaskTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TaskTemplateId: 任务模板ID
        :type TaskTemplateId: str
        :param TaskTemplateName: 任务模板名称
        :type TaskTemplateName: str
        :param TaskTemplateDescription: 任务模板描述
        :type TaskTemplateDescription: str
        :param TaskTemplateInfo: 任务模板信息
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        """
        self.TaskTemplateId = None
        self.TaskTemplateName = None
        self.TaskTemplateDescription = None
        self.TaskTemplateInfo = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.TaskTemplateName = params.get("TaskTemplateName")
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))


class ModifyTaskTemplateResponse(AbstractModel):
    """ModifyTaskTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MountDataDisk(AbstractModel):
    """数据盘挂载选项

    """

    def __init__(self):
        """
        :param LocalPath: 挂载点，Linux系统合法路径，或Windows系统盘符,比如"H:\\"
        :type LocalPath: str
        :param FileSystemType: 文件系统类型，Linux系统下支持"EXT3"和"EXT4"两种，默认"EXT3"；Windows系统下仅支持"NTFS"
        :type FileSystemType: str
        """
        self.LocalPath = None
        self.FileSystemType = None


    def _deserialize(self, params):
        self.LocalPath = params.get("LocalPath")
        self.FileSystemType = params.get("FileSystemType")


class NamedComputeEnv(AbstractModel):
    """计算环境

    """

    def __init__(self):
        """
        :param EnvName: 计算环境名称
        :type EnvName: str
        :param EnvType: 计算环境管理类型
        :type EnvType: str
        :param EnvData: 计算环境具体参数
        :type EnvData: :class:`tencentcloud.batch.v20170312.models.EnvData`
        :param DesiredComputeNodeCount: 计算节点期望个数
        :type DesiredComputeNodeCount: int
        :param EnvDescription: 计算环境描述
        :type EnvDescription: str
        :param MountDataDisks: 数据盘挂载选项
        :type MountDataDisks: list of MountDataDisk
        :param Authentications: 授权信息
        :type Authentications: list of Authentication
        :param InputMappings: 输入映射信息
        :type InputMappings: list of InputMapping
        :param AgentRunningMode: agent运行模式，适用于Windows系统
        :type AgentRunningMode: :class:`tencentcloud.batch.v20170312.models.AgentRunningMode`
        :param Notifications: 通知信息
        :type Notifications: :class:`tencentcloud.batch.v20170312.models.Notification`
        :param ActionIfComputeNodeInactive: 非活跃节点处理策略，默认“RECREATE”，即对于实例创建失败或异常退还的计算节点，定期重新创建实例资源。
        :type ActionIfComputeNodeInactive: str
        """
        self.EnvName = None
        self.EnvType = None
        self.EnvData = None
        self.DesiredComputeNodeCount = None
        self.EnvDescription = None
        self.MountDataDisks = None
        self.Authentications = None
        self.InputMappings = None
        self.AgentRunningMode = None
        self.Notifications = None
        self.ActionIfComputeNodeInactive = None


    def _deserialize(self, params):
        self.EnvName = params.get("EnvName")
        self.EnvType = params.get("EnvType")
        if params.get("EnvData") is not None:
            self.EnvData = EnvData()
            self.EnvData._deserialize(params.get("EnvData"))
        self.DesiredComputeNodeCount = params.get("DesiredComputeNodeCount")
        self.EnvDescription = params.get("EnvDescription")
        if params.get("MountDataDisks") is not None:
            self.MountDataDisks = []
            for item in params.get("MountDataDisks"):
                obj = MountDataDisk()
                obj._deserialize(item)
                self.MountDataDisks.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = Authentication()
                obj._deserialize(item)
                self.Authentications.append(obj)
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("AgentRunningMode") is not None:
            self.AgentRunningMode = AgentRunningMode()
            self.AgentRunningMode._deserialize(params.get("AgentRunningMode"))
        if params.get("Notifications") is not None:
            self.Notifications = Notification()
            self.Notifications._deserialize(params.get("Notifications"))
        self.ActionIfComputeNodeInactive = params.get("ActionIfComputeNodeInactive")


class Notification(AbstractModel):
    """通知信息

    """

    def __init__(self):
        """
        :param TopicName: CMQ主题名字，要求主题名有效且关联订阅
        :type TopicName: str
        :param EventConfigs: 事件配置
        :type EventConfigs: list of EventConfig
        """
        self.TopicName = None
        self.EventConfigs = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        if params.get("EventConfigs") is not None:
            self.EventConfigs = []
            for item in params.get("EventConfigs"):
                obj = EventConfig()
                obj._deserialize(item)
                self.EventConfigs.append(obj)


class OutputMapping(AbstractModel):
    """输出映射

    """

    def __init__(self):
        """
        :param SourcePath: 源端路径
        :type SourcePath: str
        :param DestinationPath: 目的端路径
        :type DestinationPath: str
        """
        self.SourcePath = None
        self.DestinationPath = None


    def _deserialize(self, params):
        self.SourcePath = params.get("SourcePath")
        self.DestinationPath = params.get("DestinationPath")


class OutputMappingConfig(AbstractModel):
    """输出映射配置

    """

    def __init__(self):
        """
        :param Scene: 存储类型，仅支持COS
        :type Scene: str
        :param WorkerNum: 并行worker数量
        :type WorkerNum: int
        :param WorkerPartSize: worker分块大小
        :type WorkerPartSize: int
        """
        self.Scene = None
        self.WorkerNum = None
        self.WorkerPartSize = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.WorkerNum = params.get("WorkerNum")
        self.WorkerPartSize = params.get("WorkerPartSize")


class Placement(AbstractModel):
    """描述了实例的抽象位置，包括其所在的可用区，所属的项目，宿主机等（仅CDH产品可用）

    """

    def __init__(self):
        """
        :param Zone: 实例所属的[可用区](/document/product/213/9452#zone)ID。该参数也可以通过调用  [DescribeZones](/document/api/213/9455) 的返回值中的Zone字段来获取。
        :type Zone: str
        :param ProjectId: 实例所属项目ID。该参数可以通过调用 [DescribeProject](/document/api/378/4400) 的返回值中的 projectId 字段来获取。不填为默认项目。
        :type ProjectId: int
        :param HostIds: 实例所属的专用宿主机ID列表。如果您有购买专用宿主机并且指定了该参数，则您购买的实例就会随机的部署在这些专用宿主机上。
        :type HostIds: list of str
        """
        self.Zone = None
        self.ProjectId = None
        self.HostIds = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ProjectId = params.get("ProjectId")
        self.HostIds = params.get("HostIds")


class RedirectInfo(AbstractModel):
    """重定向信息

    """

    def __init__(self):
        """
        :param StdoutRedirectPath: 标准输出重定向路径
        :type StdoutRedirectPath: str
        :param StderrRedirectPath: 标准错误重定向路径
        :type StderrRedirectPath: str
        :param StdoutRedirectFileName: 标准输出重定向文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutRedirectFileName: str
        :param StderrRedirectFileName: 标准错误重定向文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StderrRedirectFileName: str
        """
        self.StdoutRedirectPath = None
        self.StderrRedirectPath = None
        self.StdoutRedirectFileName = None
        self.StderrRedirectFileName = None


    def _deserialize(self, params):
        self.StdoutRedirectPath = params.get("StdoutRedirectPath")
        self.StderrRedirectPath = params.get("StderrRedirectPath")
        self.StdoutRedirectFileName = params.get("StdoutRedirectFileName")
        self.StderrRedirectFileName = params.get("StderrRedirectFileName")


class RedirectLocalInfo(AbstractModel):
    """本地重定向信息

    """

    def __init__(self):
        """
        :param StdoutLocalPath: 标准输出重定向本地路径
        :type StdoutLocalPath: str
        :param StderrLocalPath: 标准错误重定向本地路径
        :type StderrLocalPath: str
        :param StdoutLocalFileName: 标准输出重定向本地文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StdoutLocalFileName: str
        :param StderrLocalFileName: 标准错误重定向本地文件名，支持三个占位符${BATCH_JOB_ID}、${BATCH_TASK_NAME}、${BATCH_TASK_INSTANCE_INDEX}
        :type StderrLocalFileName: str
        """
        self.StdoutLocalPath = None
        self.StderrLocalPath = None
        self.StdoutLocalFileName = None
        self.StderrLocalFileName = None


    def _deserialize(self, params):
        self.StdoutLocalPath = params.get("StdoutLocalPath")
        self.StderrLocalPath = params.get("StderrLocalPath")
        self.StdoutLocalFileName = params.get("StdoutLocalFileName")
        self.StderrLocalFileName = params.get("StderrLocalFileName")


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


class SpotMarketOptions(AbstractModel):
    """竞价相关选项

    """

    def __init__(self):
        """
        :param MaxPrice: 竞价出价
        :type MaxPrice: str
        :param SpotInstanceType: 竞价请求类型，当前仅支持类型：one-time
        :type SpotInstanceType: str
        """
        self.MaxPrice = None
        self.SpotInstanceType = None


    def _deserialize(self, params):
        self.MaxPrice = params.get("MaxPrice")
        self.SpotInstanceType = params.get("SpotInstanceType")


class StorageBlock(AbstractModel):
    """HDD的本地存储信息

    """

    def __init__(self):
        """
        :param Type: HDD本地存储类型，值为：LOCAL_PRO.
        :type Type: str
        :param MinSize: HDD本地存储的最小容量
        :type MinSize: int
        :param MaxSize: HDD本地存储的最大容量
        :type MaxSize: int
        """
        self.Type = None
        self.MinSize = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.MinSize = params.get("MinSize")
        self.MaxSize = params.get("MaxSize")


class SubmitJobRequest(AbstractModel):
    """SubmitJob请求参数结构体

    """

    def __init__(self):
        """
        :param Placement: 作业所提交的位置信息。通过该参数可以指定作业关联CVM所属可用区等信息。
        :type Placement: :class:`tencentcloud.batch.v20170312.models.Placement`
        :param Job: 作业信息
        :type Job: :class:`tencentcloud.batch.v20170312.models.Job`
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由用户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
        :type ClientToken: str
        """
        self.Placement = None
        self.Job = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("Placement") is not None:
            self.Placement = Placement()
            self.Placement._deserialize(params.get("Placement"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        self.ClientToken = params.get("ClientToken")


class SubmitJobResponse(AbstractModel):
    """SubmitJob返回参数结构体

    """

    def __init__(self):
        """
        :param JobId: 当通过本接口来提交作业时会返回该参数，表示一个作业ID。返回作业ID列表并不代表作业解析/运行成功，可根据 DescribeJob 接口查询其状态。
        :type JobId: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.JobId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.RequestId = params.get("RequestId")


class SystemDisk(AbstractModel):
    """描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        """
        :param DiskType: 系统盘类型。系统盘类型限制详见[CVM实例配置](/document/product/213/2177)。取值范围：<br><li>LOCAL_BASIC：本地硬盘<br><li>LOCAL_SSD：本地SSD硬盘<br><li>CLOUD_BASIC：普通云硬盘<br><li>CLOUD_SSD：SSD云硬盘<br><li>CLOUD_PREMIUM：高性能云硬盘<br><br>默认取值：CLOUD_BASIC。
        :type DiskType: str
        :param DiskId: 系统盘ID。LOCAL_BASIC 和 LOCAL_SSD 类型没有ID。暂时不支持该参数。
        :type DiskId: str
        :param DiskSize: 系统盘大小，单位：GB。默认值为 50
        :type DiskSize: int
        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")


class Task(AbstractModel):
    """任务

    """

    def __init__(self):
        """
        :param TaskName: 任务名称，在一个作业内部唯一
        :type TaskName: str
        :param TaskInstanceNum: 任务实例运行个数
        :type TaskInstanceNum: int
        :param Application: 应用程序信息
        :type Application: :class:`tencentcloud.batch.v20170312.models.Application`
        :param RedirectInfo: 重定向信息
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param MaxRetryCount: 任务失败后的最大重试次数，默认为0
        :type MaxRetryCount: int
        :param Timeout: 任务启动后的超时时间，单位秒，默认为3600秒
        :type Timeout: int
        :param ComputeEnv: 运行环境信息，ComputeEnv 和 EnvId 必须指定一个（且只有一个）参数。
        :type ComputeEnv: :class:`tencentcloud.batch.v20170312.models.AnonymousComputeEnv`
        :param EnvId: 计算环境ID，ComputeEnv 和 EnvId 必须指定一个（且只有一个）参数。
        :type EnvId: str
        :param RedirectLocalInfo: 重定向本地信息
        :type RedirectLocalInfo: :class:`tencentcloud.batch.v20170312.models.RedirectLocalInfo`
        :param InputMappings: 输入映射
        :type InputMappings: list of InputMapping
        :param OutputMappings: 输出映射
        :type OutputMappings: list of OutputMapping
        :param OutputMappingConfigs: 输出映射配置
        :type OutputMappingConfigs: list of OutputMappingConfig
        :param EnvVars: 自定义环境变量
        :type EnvVars: list of Authentication
        :param Authentications: 授权信息
        :type Authentications: list of EnvVar
        :param FailedAction: TaskInstance失败后处理方式，取值包括TERMINATE（默认）、INTERRUPT、FAST_INTERRUPT。
        :type FailedAction: str
        """
        self.TaskName = None
        self.TaskInstanceNum = None
        self.Application = None
        self.RedirectInfo = None
        self.MaxRetryCount = None
        self.Timeout = None
        self.ComputeEnv = None
        self.EnvId = None
        self.RedirectLocalInfo = None
        self.InputMappings = None
        self.OutputMappings = None
        self.OutputMappingConfigs = None
        self.EnvVars = None
        self.Authentications = None
        self.FailedAction = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskInstanceNum = params.get("TaskInstanceNum")
        if params.get("Application") is not None:
            self.Application = Application()
            self.Application._deserialize(params.get("Application"))
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = RedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.MaxRetryCount = params.get("MaxRetryCount")
        self.Timeout = params.get("Timeout")
        if params.get("ComputeEnv") is not None:
            self.ComputeEnv = AnonymousComputeEnv()
            self.ComputeEnv._deserialize(params.get("ComputeEnv"))
        self.EnvId = params.get("EnvId")
        if params.get("RedirectLocalInfo") is not None:
            self.RedirectLocalInfo = RedirectLocalInfo()
            self.RedirectLocalInfo._deserialize(params.get("RedirectLocalInfo"))
        if params.get("InputMappings") is not None:
            self.InputMappings = []
            for item in params.get("InputMappings"):
                obj = InputMapping()
                obj._deserialize(item)
                self.InputMappings.append(obj)
        if params.get("OutputMappings") is not None:
            self.OutputMappings = []
            for item in params.get("OutputMappings"):
                obj = OutputMapping()
                obj._deserialize(item)
                self.OutputMappings.append(obj)
        if params.get("OutputMappingConfigs") is not None:
            self.OutputMappingConfigs = []
            for item in params.get("OutputMappingConfigs"):
                obj = OutputMappingConfig()
                obj._deserialize(item)
                self.OutputMappingConfigs.append(obj)
        if params.get("EnvVars") is not None:
            self.EnvVars = []
            for item in params.get("EnvVars"):
                obj = Authentication()
                obj._deserialize(item)
                self.EnvVars.append(obj)
        if params.get("Authentications") is not None:
            self.Authentications = []
            for item in params.get("Authentications"):
                obj = EnvVar()
                obj._deserialize(item)
                self.Authentications.append(obj)
        self.FailedAction = params.get("FailedAction")


class TaskInstanceMetrics(AbstractModel):
    """任务实例统计指标

    """

    def __init__(self):
        """
        :param SubmittedCount: Submitted个数
        :type SubmittedCount: int
        :param PendingCount: Pending个数
        :type PendingCount: int
        :param RunnableCount: Runnable个数
        :type RunnableCount: int
        :param StartingCount: Starting个数
        :type StartingCount: int
        :param RunningCount: Running个数
        :type RunningCount: int
        :param SucceedCount: Succeed个数
        :type SucceedCount: int
        :param FailedInterruptedCount: FailedInterrupted个数
        :type FailedInterruptedCount: int
        :param FailedCount: Failed个数
        :type FailedCount: int
        """
        self.SubmittedCount = None
        self.PendingCount = None
        self.RunnableCount = None
        self.StartingCount = None
        self.RunningCount = None
        self.SucceedCount = None
        self.FailedInterruptedCount = None
        self.FailedCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.PendingCount = params.get("PendingCount")
        self.RunnableCount = params.get("RunnableCount")
        self.StartingCount = params.get("StartingCount")
        self.RunningCount = params.get("RunningCount")
        self.SucceedCount = params.get("SucceedCount")
        self.FailedInterruptedCount = params.get("FailedInterruptedCount")
        self.FailedCount = params.get("FailedCount")


class TaskInstanceView(AbstractModel):
    """任务实例视图信息

    """

    def __init__(self):
        """
        :param TaskInstanceIndex: 任务实例索引
        :type TaskInstanceIndex: int
        :param TaskInstanceState: 任务实例状态
        :type TaskInstanceState: str
        :param ExitCode: 应用程序执行结束的exit code
        :type ExitCode: int
        :param StateReason: 任务实例状态原因，任务实例失败时，会记录失败原因
        :type StateReason: str
        :param ComputeNodeInstanceId: 任务实例运行时所在计算节点（例如CVM）的InstanceId。任务实例未运行或者完结时，本字段为空。任务实例重试时，本字段会随之变化
        :type ComputeNodeInstanceId: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param LaunchTime: 启动时间
        :type LaunchTime: str
        :param RunningTime: 开始运行时间
        :type RunningTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param RedirectInfo: 重定向信息
        :type RedirectInfo: :class:`tencentcloud.batch.v20170312.models.RedirectInfo`
        :param StateDetailedReason: 任务实例状态原因详情，任务实例失败时，会记录失败原因
        :type StateDetailedReason: str
        """
        self.TaskInstanceIndex = None
        self.TaskInstanceState = None
        self.ExitCode = None
        self.StateReason = None
        self.ComputeNodeInstanceId = None
        self.CreateTime = None
        self.LaunchTime = None
        self.RunningTime = None
        self.EndTime = None
        self.RedirectInfo = None
        self.StateDetailedReason = None


    def _deserialize(self, params):
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")
        self.TaskInstanceState = params.get("TaskInstanceState")
        self.ExitCode = params.get("ExitCode")
        self.StateReason = params.get("StateReason")
        self.ComputeNodeInstanceId = params.get("ComputeNodeInstanceId")
        self.CreateTime = params.get("CreateTime")
        self.LaunchTime = params.get("LaunchTime")
        self.RunningTime = params.get("RunningTime")
        self.EndTime = params.get("EndTime")
        if params.get("RedirectInfo") is not None:
            self.RedirectInfo = RedirectInfo()
            self.RedirectInfo._deserialize(params.get("RedirectInfo"))
        self.StateDetailedReason = params.get("StateDetailedReason")


class TaskMetrics(AbstractModel):
    """任务统计指标

    """

    def __init__(self):
        """
        :param SubmittedCount: Submitted个数
        :type SubmittedCount: int
        :param PendingCount: Pending个数
        :type PendingCount: int
        :param RunnableCount: Runnable个数
        :type RunnableCount: int
        :param StartingCount: Starting个数
        :type StartingCount: int
        :param RunningCount: Running个数
        :type RunningCount: int
        :param SucceedCount: Succeed个数
        :type SucceedCount: int
        :param FailedInterruptedCount: FailedInterrupted个数
        :type FailedInterruptedCount: int
        :param FailedCount: Failed个数
        :type FailedCount: int
        """
        self.SubmittedCount = None
        self.PendingCount = None
        self.RunnableCount = None
        self.StartingCount = None
        self.RunningCount = None
        self.SucceedCount = None
        self.FailedInterruptedCount = None
        self.FailedCount = None


    def _deserialize(self, params):
        self.SubmittedCount = params.get("SubmittedCount")
        self.PendingCount = params.get("PendingCount")
        self.RunnableCount = params.get("RunnableCount")
        self.StartingCount = params.get("StartingCount")
        self.RunningCount = params.get("RunningCount")
        self.SucceedCount = params.get("SucceedCount")
        self.FailedInterruptedCount = params.get("FailedInterruptedCount")
        self.FailedCount = params.get("FailedCount")


class TaskTemplateView(AbstractModel):
    """任务模板信息

    """

    def __init__(self):
        """
        :param TaskTemplateId: 任务模板ID
        :type TaskTemplateId: str
        :param TaskTemplateName: 任务模板名称
        :type TaskTemplateName: str
        :param TaskTemplateDescription: 任务模板描述
        :type TaskTemplateDescription: str
        :param TaskTemplateInfo: 任务模板信息
        :type TaskTemplateInfo: :class:`tencentcloud.batch.v20170312.models.Task`
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.TaskTemplateId = None
        self.TaskTemplateName = None
        self.TaskTemplateDescription = None
        self.TaskTemplateInfo = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskTemplateId = params.get("TaskTemplateId")
        self.TaskTemplateName = params.get("TaskTemplateName")
        self.TaskTemplateDescription = params.get("TaskTemplateDescription")
        if params.get("TaskTemplateInfo") is not None:
            self.TaskTemplateInfo = Task()
            self.TaskTemplateInfo._deserialize(params.get("TaskTemplateInfo"))
        self.CreateTime = params.get("CreateTime")


class TaskView(AbstractModel):
    """任务视图信息

    """

    def __init__(self):
        """
        :param TaskName: 任务名称
        :type TaskName: str
        :param TaskState: 任务状态
        :type TaskState: str
        :param CreateTime: 开始时间
        :type CreateTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.TaskName = None
        self.TaskState = None
        self.CreateTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.TaskName = params.get("TaskName")
        self.TaskState = params.get("TaskState")
        self.CreateTime = params.get("CreateTime")
        self.EndTime = params.get("EndTime")


class TerminateComputeNodeRequest(AbstractModel):
    """TerminateComputeNode请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param ComputeNodeId: 计算节点ID
        :type ComputeNodeId: str
        """
        self.EnvId = None
        self.ComputeNodeId = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ComputeNodeId = params.get("ComputeNodeId")


class TerminateComputeNodeResponse(AbstractModel):
    """TerminateComputeNode返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateComputeNodesRequest(AbstractModel):
    """TerminateComputeNodes请求参数结构体

    """

    def __init__(self):
        """
        :param EnvId: 计算环境ID
        :type EnvId: str
        :param ComputeNodeIds: 计算节点ID列表
        :type ComputeNodeIds: list of str
        """
        self.EnvId = None
        self.ComputeNodeIds = None


    def _deserialize(self, params):
        self.EnvId = params.get("EnvId")
        self.ComputeNodeIds = params.get("ComputeNodeIds")


class TerminateComputeNodesResponse(AbstractModel):
    """TerminateComputeNodes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateJobRequest(AbstractModel):
    """TerminateJob请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        """
        self.JobId = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")


class TerminateJobResponse(AbstractModel):
    """TerminateJob返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TerminateTaskInstanceRequest(AbstractModel):
    """TerminateTaskInstance请求参数结构体

    """

    def __init__(self):
        """
        :param JobId: 作业ID
        :type JobId: str
        :param TaskName: 任务名称
        :type TaskName: str
        :param TaskInstanceIndex: 任务实例索引
        :type TaskInstanceIndex: int
        """
        self.JobId = None
        self.TaskName = None
        self.TaskInstanceIndex = None


    def _deserialize(self, params):
        self.JobId = params.get("JobId")
        self.TaskName = params.get("TaskName")
        self.TaskInstanceIndex = params.get("TaskInstanceIndex")


class TerminateTaskInstanceResponse(AbstractModel):
    """TerminateTaskInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """描述了VPC相关信息，包括子网，IP信息等

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID，形如`vpc-xxx`。有效的VpcId可通过登录[控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)查询；也可以调用接口 [DescribeVpcEx](/document/api/215/1372) ，从接口返回中的`unVpcId`字段获取。
        :type VpcId: str
        :param SubnetId: 私有网络子网ID，形如`subnet-xxx`。有效的私有网络子网ID可通过登录[控制台](https://console.cloud.tencent.com/vpc/subnet?rid=1)查询；也可以调用接口  [DescribeSubnets](/document/api/215/15784) ，从接口返回中的`unSubnetId`字段获取。
        :type SubnetId: str
        :param AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：<br><li>TRUE：表示用作公网网关<br><li>FALSE：表示不用作公网网关<br><br>默认取值：FALSE。
        :type AsVpcGateway: bool
        :param PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。当前仅批量创建多台实例时支持传入相同子网的多个 IP。
        :type PrivateIpAddresses: list of str
        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")