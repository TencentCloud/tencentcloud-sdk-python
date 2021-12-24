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


class ApplicationBasicConfig(AbstractModel):
    """应用基本配置

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param WorkflowKind: 工作负载类型
        :type WorkflowKind: str
        :param Labels: 标签信息
        :type Labels: list of Label
        :param GridUniqKey: Grid唯一Key
        :type GridUniqKey: str
        :param NodeSelector: NodeSelector标签
        :type NodeSelector: list of Label
        :param Replicas: 实例数
        :type Replicas: int
        :param AvailableReplicas: 可用实例数
        :type AvailableReplicas: int
        :param EnableServiceLinks: 是否开启service环境变量注入pod
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableServiceLinks: bool
        """
        self.Name = None
        self.Namespace = None
        self.WorkflowKind = None
        self.Labels = None
        self.GridUniqKey = None
        self.NodeSelector = None
        self.Replicas = None
        self.AvailableReplicas = None
        self.EnableServiceLinks = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.WorkflowKind = params.get("WorkflowKind")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.GridUniqKey = params.get("GridUniqKey")
        if params.get("NodeSelector") is not None:
            self.NodeSelector = []
            for item in params.get("NodeSelector"):
                obj = Label()
                obj._deserialize(item)
                self.NodeSelector.append(obj)
        self.Replicas = params.get("Replicas")
        self.AvailableReplicas = params.get("AvailableReplicas")
        self.EnableServiceLinks = params.get("EnableServiceLinks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationBasicInfo(AbstractModel):
    """应用基本信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param ManageUrl: 管理URL地址
        :type ManageUrl: str
        :param Description: 描述信息
        :type Description: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.Name = None
        self.ManageUrl = None
        self.Description = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ManageUrl = params.get("ManageUrl")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationDeployMode(AbstractModel):
    """应用部署模式

    """

    def __init__(self):
        r"""
        :param Type: 1:指定节点部署 2:单元部署
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param ResourceID: 资源ID
        :type ResourceID: int
        :param ResourceName: 资源名
        :type ResourceName: str
        """
        self.Type = None
        self.ResourceID = None
        self.ResourceName = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.ResourceID = params.get("ResourceID")
        self.ResourceName = params.get("ResourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationStatusInfo(AbstractModel):
    """应用状态

    """

    def __init__(self):
        r"""
        :param Id: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Name: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Version: 应用版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param Status: 应用状态(1:待部署 2:部署中 3:运行中 4:待更新 5:更新中 6:待删除 7:删除中 8:已删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param ManageUrl: 管理地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageUrl: str
        :param WorkloadKind: 负载类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadKind: str
        :param DeployMode: 应用部署模式
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: :class:`tencentcloud.iecp.v20210914.models.ApplicationDeployMode`
        :param Replicas: 期望Pod数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param AvailableReplicas: 运行Pod数
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableReplicas: int
        """
        self.Id = None
        self.Name = None
        self.Version = None
        self.Status = None
        self.StartTime = None
        self.ManageUrl = None
        self.WorkloadKind = None
        self.DeployMode = None
        self.Replicas = None
        self.AvailableReplicas = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Version = params.get("Version")
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.ManageUrl = params.get("ManageUrl")
        self.WorkloadKind = params.get("WorkloadKind")
        if params.get("DeployMode") is not None:
            self.DeployMode = ApplicationDeployMode()
            self.DeployMode._deserialize(params.get("DeployMode"))
        self.Replicas = params.get("Replicas")
        self.AvailableReplicas = params.get("AvailableReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplicationTemplate(AbstractModel):
    """应用模板列表详情

    """

    def __init__(self):
        r"""
        :param Id: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Source: 来源。1 自定义应用模板 ;  2 官方应用模板
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param WorkloadKind: 应用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadKind: str
        :param ManageUrl: 管理地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageUrl: str
        :param DistributeTime: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DistributeTime: str
        """
        self.Id = None
        self.Name = None
        self.Source = None
        self.WorkloadKind = None
        self.ManageUrl = None
        self.DistributeTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Source = params.get("Source")
        self.WorkloadKind = params.get("WorkloadKind")
        self.ManageUrl = params.get("ManageUrl")
        self.DistributeTime = params.get("DistributeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyMarketComponentRequest(AbstractModel):
    """ApplyMarketComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 组件ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyMarketComponentResponse(AbstractModel):
    """ApplyMarketComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConfigMapBasicInfo(AbstractModel):
    """ConfigMap基本信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.Name = None
        self.Namespace = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Container(AbstractModel):
    """容器配置信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param ImageName: 镜像名
        :type ImageName: str
        :param ImageVersion: 镜像版本
        :type ImageVersion: str
        :param ImagePullPolicy: 镜像拉取策略(Always|Never|IfNotPresent)
        :type ImagePullPolicy: str
        :param VolumeMounts: 卷挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VolumeMounts: list of VolumeMount
        :param CpuRequest: cpu最低配置
        :type CpuRequest: str
        :param CpuLimit: cpu最高限制
        :type CpuLimit: str
        :param MemoryRequest: 内存最低要求
        :type MemoryRequest: str
        :param MemoryLimit: 内存最高要求
        :type MemoryLimit: str
        :param MemoryUnit: 内存单位
        :type MemoryUnit: str
        :param GpuLimit: gpu最高限制
        :type GpuLimit: str
        :param ResourceMapCloud: 资源配置
        :type ResourceMapCloud: list of KeyValueObj
        :param Envs: 环境配置
        :type Envs: list of Env
        :param WorkingDir: 工作目录
        :type WorkingDir: str
        :param Commands: 命令
        :type Commands: list of str
        :param Args: 参数
        :type Args: list of str
        :param SecurityContext: 安全配置
        :type SecurityContext: :class:`tencentcloud.iecp.v20210914.models.SecurityContext`
        :param ReadinessProbe: 就绪探针配置
        :type ReadinessProbe: :class:`tencentcloud.iecp.v20210914.models.Probe`
        """
        self.Name = None
        self.ImageName = None
        self.ImageVersion = None
        self.ImagePullPolicy = None
        self.VolumeMounts = None
        self.CpuRequest = None
        self.CpuLimit = None
        self.MemoryRequest = None
        self.MemoryLimit = None
        self.MemoryUnit = None
        self.GpuLimit = None
        self.ResourceMapCloud = None
        self.Envs = None
        self.WorkingDir = None
        self.Commands = None
        self.Args = None
        self.SecurityContext = None
        self.ReadinessProbe = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ImageName = params.get("ImageName")
        self.ImageVersion = params.get("ImageVersion")
        self.ImagePullPolicy = params.get("ImagePullPolicy")
        if params.get("VolumeMounts") is not None:
            self.VolumeMounts = []
            for item in params.get("VolumeMounts"):
                obj = VolumeMount()
                obj._deserialize(item)
                self.VolumeMounts.append(obj)
        self.CpuRequest = params.get("CpuRequest")
        self.CpuLimit = params.get("CpuLimit")
        self.MemoryRequest = params.get("MemoryRequest")
        self.MemoryLimit = params.get("MemoryLimit")
        self.MemoryUnit = params.get("MemoryUnit")
        self.GpuLimit = params.get("GpuLimit")
        if params.get("ResourceMapCloud") is not None:
            self.ResourceMapCloud = []
            for item in params.get("ResourceMapCloud"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self.ResourceMapCloud.append(obj)
        if params.get("Envs") is not None:
            self.Envs = []
            for item in params.get("Envs"):
                obj = Env()
                obj._deserialize(item)
                self.Envs.append(obj)
        self.WorkingDir = params.get("WorkingDir")
        self.Commands = params.get("Commands")
        self.Args = params.get("Args")
        if params.get("SecurityContext") is not None:
            self.SecurityContext = SecurityContext()
            self.SecurityContext._deserialize(params.get("SecurityContext"))
        if params.get("ReadinessProbe") is not None:
            self.ReadinessProbe = Probe()
            self.ReadinessProbe._deserialize(params.get("ReadinessProbe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerStatus(AbstractModel):
    """容器状态

    """

    def __init__(self):
        r"""
        :param Name: 容器名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param ID: 容器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param Image: 镜像
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param Status: 状态
        :type Status: str
        """
        self.Name = None
        self.ID = None
        self.Image = None
        self.RestartCount = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ID = params.get("ID")
        self.Image = params.get("Image")
        self.RestartCount = params.get("RestartCount")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationVisualizationRequest(AbstractModel):
    """CreateApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param BasicInfo: 基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param BasicConfig: 基本配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param Volumes: 卷列表
        :type Volumes: list of Volume
        :param Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param RestartPolicy: 重新运行策略
        :type RestartPolicy: str
        :param ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param InitContainers: 初始化容器列表
        :type InitContainers: list of Container
        :param Containers: 容器列表
        :type Containers: list of Container
        """
        self.BasicInfo = None
        self.BasicConfig = None
        self.Volumes = None
        self.Service = None
        self.Job = None
        self.CronJob = None
        self.RestartPolicy = None
        self.ImagePullSecrets = None
        self.HorizontalPodAutoscaler = None
        self.InitContainers = None
        self.Containers = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self.BasicConfig = ApplicationBasicConfig()
            self.BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self.Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self.Volumes.append(obj)
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self.CronJob = CronJob()
            self.CronJob._deserialize(params.get("CronJob"))
        self.RestartPolicy = params.get("RestartPolicy")
        self.ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationVisualizationResponse(AbstractModel):
    """CreateApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.RequestId = params.get("RequestId")


class CreateConfigMapRequest(AbstractModel):
    """CreateConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param ConfigMapName: ConfigMap名称
        :type ConfigMapName: str
        :param ConfigMapData: ConfigMap内容
        :type ConfigMapData: list of KeyValueObj
        :param ConfigMapNamespace: ConfigMap命名空间,默认：default
        :type ConfigMapNamespace: str
        """
        self.EdgeUnitID = None
        self.ConfigMapName = None
        self.ConfigMapData = None
        self.ConfigMapNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.ConfigMapName = params.get("ConfigMapName")
        if params.get("ConfigMapData") is not None:
            self.ConfigMapData = []
            for item in params.get("ConfigMapData"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self.ConfigMapData.append(obj)
        self.ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigMapResponse(AbstractModel):
    """CreateConfigMap返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEdgeNodeGroupRequest(AbstractModel):
    """CreateEdgeNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Name: NodeGroup名称
        :type Name: str
        :param Namespace: 命名空间，不填默认为default
        :type Namespace: str
        :param Description: 描述
        :type Description: str
        :param NodeUnitTemplateIDs: 模版ID数组
        :type NodeUnitTemplateIDs: list of int non-negative
        """
        self.EdgeUnitId = None
        self.Name = None
        self.Namespace = None
        self.Description = None
        self.NodeUnitTemplateIDs = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        self.NodeUnitTemplateIDs = params.get("NodeUnitTemplateIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeGroupResponse(AbstractModel):
    """CreateEdgeNodeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEdgeNodeRequest(AbstractModel):
    """CreateEdgeNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param Name: 节点名称
        :type Name: str
        """
        self.EdgeUnitId = None
        self.Name = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeResponse(AbstractModel):
    """CreateEdgeNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEdgeNodeUnitTemplateRequest(AbstractModel):
    """CreateEdgeNodeUnitTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Name: NodeUnit模版名称
        :type Name: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        :param Nodes: 包含的节点列表
        :type Nodes: list of str
        :param Description: 描述
        :type Description: str
        """
        self.EdgeUnitId = None
        self.Name = None
        self.Namespace = None
        self.Nodes = None
        self.Description = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.Nodes = params.get("Nodes")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeNodeUnitTemplateResponse(AbstractModel):
    """CreateEdgeNodeUnitTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateEdgeUnitApplicationVisualizationRequest(AbstractModel):
    """CreateEdgeUnitApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param BasicInfo: 基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param BasicConfig: 基本配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param Volumes: 卷列表
        :type Volumes: list of Volume
        :param Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param TemplateID: 模版ID
        :type TemplateID: int
        :param Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param RestartPolicy: 重新运行策略
        :type RestartPolicy: str
        :param ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param InitContainers: 初始化容器列表
        :type InitContainers: list of Container
        :param Containers: 容器列表
        :type Containers: list of Container
        """
        self.BasicInfo = None
        self.BasicConfig = None
        self.EdgeUnitId = None
        self.Volumes = None
        self.Service = None
        self.TemplateID = None
        self.Job = None
        self.CronJob = None
        self.RestartPolicy = None
        self.ImagePullSecrets = None
        self.HorizontalPodAutoscaler = None
        self.InitContainers = None
        self.Containers = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self.BasicConfig = ApplicationBasicConfig()
            self.BasicConfig._deserialize(params.get("BasicConfig"))
        self.EdgeUnitId = params.get("EdgeUnitId")
        if params.get("Volumes") is not None:
            self.Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self.Volumes.append(obj)
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.TemplateID = params.get("TemplateID")
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self.CronJob = CronJob()
            self.CronJob._deserialize(params.get("CronJob"))
        self.RestartPolicy = params.get("RestartPolicy")
        self.ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitApplicationVisualizationResponse(AbstractModel):
    """CreateEdgeUnitApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.RequestId = params.get("RequestId")


class CreateEdgeUnitApplicationYamlRequest(AbstractModel):
    """CreateEdgeUnitApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param BasicInfo: 基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param Yaml: Yaml配置
        :type Yaml: str
        """
        self.EdgeUnitId = None
        self.BasicInfo = None
        self.Yaml = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitApplicationYamlResponse(AbstractModel):
    """CreateEdgeUnitApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApplicationId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ApplicationId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.RequestId = params.get("RequestId")


class CreateEdgeUnitCloudRequest(AbstractModel):
    """CreateEdgeUnitCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 集群名称，长度小于32
        :type Name: str
        :param K8sVersion: k8s版本，仅支持1.16.7 和 1.18.2
        :type K8sVersion: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param Description: 集群描述
        :type Description: str
        :param PodCIDR: 集群pod cidr， 默认  10.1.0.0/16
        :type PodCIDR: str
        :param ServiceCIDR: 集群service cidr, 默认 10.2.0.0/16
        :type ServiceCIDR: str
        """
        self.Name = None
        self.K8sVersion = None
        self.VpcId = None
        self.Description = None
        self.PodCIDR = None
        self.ServiceCIDR = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.K8sVersion = params.get("K8sVersion")
        self.VpcId = params.get("VpcId")
        self.Description = params.get("Description")
        self.PodCIDR = params.get("PodCIDR")
        self.ServiceCIDR = params.get("ServiceCIDR")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeUnitCloudResponse(AbstractModel):
    """CreateEdgeUnitCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: tke集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param EdgeUnitId: IECP集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeUnitId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.EdgeUnitId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.RequestId = params.get("RequestId")


class CreateNamespaceRequest(AbstractModel):
    """CreateNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 描述信息
        :type Description: str
        """
        self.EdgeUnitID = None
        self.Namespace = None
        self.Description = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNamespaceResponse(AbstractModel):
    """CreateNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecretRequest(AbstractModel):
    """CreateSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param SecretName: secret名
        :type SecretName: str
        :param SecretNamespace: 命名空间（默认:default）
        :type SecretNamespace: str
        :param SecretType: secret类型(取值范围:DockerConfigJson,Opaque 默认Opaque)
        :type SecretType: str
        :param DockerConfigJson: DockerConfig的序列化base64编码后的字符串
        :type DockerConfigJson: str
        :param CloudData: Opaque类型的Secret内容
        :type CloudData: list of KeyValueObj
        :param DockerConfig: DockerConfig配置
        :type DockerConfig: :class:`tencentcloud.iecp.v20210914.models.DockerConfig`
        """
        self.EdgeUnitID = None
        self.SecretName = None
        self.SecretNamespace = None
        self.SecretType = None
        self.DockerConfigJson = None
        self.CloudData = None
        self.DockerConfig = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.SecretName = params.get("SecretName")
        self.SecretNamespace = params.get("SecretNamespace")
        self.SecretType = params.get("SecretType")
        self.DockerConfigJson = params.get("DockerConfigJson")
        if params.get("CloudData") is not None:
            self.CloudData = []
            for item in params.get("CloudData"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self.CloudData.append(obj)
        if params.get("DockerConfig") is not None:
            self.DockerConfig = DockerConfig()
            self.DockerConfig._deserialize(params.get("DockerConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecretResponse(AbstractModel):
    """CreateSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateUpdateNodeUnitRequest(AbstractModel):
    """CreateUpdateNodeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeGroupName: NodeUnit所属的NodeGroup名称
        :type NodeGroupName: str
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        :param NodeUnitName: NodeUnit名称，通过模版创建可不填
        :type NodeUnitName: str
        :param Nodes: NodeUnit包含的节点列表，通过模版创建可不填
        :type Nodes: list of str
        :param NodeUnitTemplateIDs: NodeUnit模版ID列表
        :type NodeUnitTemplateIDs: list of int non-negative
        """
        self.EdgeUnitId = None
        self.NodeGroupName = None
        self.Namespace = None
        self.NodeUnitName = None
        self.Nodes = None
        self.NodeUnitTemplateIDs = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeGroupName = params.get("NodeGroupName")
        self.Namespace = params.get("Namespace")
        self.NodeUnitName = params.get("NodeUnitName")
        self.Nodes = params.get("Nodes")
        self.NodeUnitTemplateIDs = params.get("NodeUnitTemplateIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUpdateNodeUnitResponse(AbstractModel):
    """CreateUpdateNodeUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CronJob(AbstractModel):
    """CronJob配置

    """

    def __init__(self):
        r"""
        :param Schedule: 调度配置
        :type Schedule: str
        :param StartingDeadlineSeconds: 运行时间
        :type StartingDeadlineSeconds: int
        :param ConcurrencyPolicy: job并行策略(Allow|Forbid|Replace)
        :type ConcurrencyPolicy: str
        :param Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        """
        self.Schedule = None
        self.StartingDeadlineSeconds = None
        self.ConcurrencyPolicy = None
        self.Job = None


    def _deserialize(self, params):
        self.Schedule = params.get("Schedule")
        self.StartingDeadlineSeconds = params.get("StartingDeadlineSeconds")
        self.ConcurrencyPolicy = params.get("ConcurrencyPolicy")
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationsRequest(AbstractModel):
    """DeleteApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationIds: 应用模板ID列表
        :type ApplicationIds: list of int non-negative
        """
        self.ApplicationIds = None


    def _deserialize(self, params):
        self.ApplicationIds = params.get("ApplicationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApplicationsResponse(AbstractModel):
    """DeleteApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteConfigMapRequest(AbstractModel):
    """DeleteConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param ConfigMapName: ConfigMap名
        :type ConfigMapName: str
        :param ConfigMapNamespace: ConfigMap命名空间，默认：default
        :type ConfigMapNamespace: str
        """
        self.EdgeUnitID = None
        self.ConfigMapName = None
        self.ConfigMapNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.ConfigMapName = params.get("ConfigMapName")
        self.ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigMapResponse(AbstractModel):
    """DeleteConfigMap返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeNodeGroupRequest(AbstractModel):
    """DeleteEdgeNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Name: NodeGroup名称
        :type Name: str
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.Name = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeNodeGroupResponse(AbstractModel):
    """DeleteEdgeNodeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeNodeUnitTemplatesRequest(AbstractModel):
    """DeleteEdgeNodeUnitTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeUnitTemplateIDs: 删除的NodeUnit模版ID列表
        :type NodeUnitTemplateIDs: list of int non-negative
        """
        self.EdgeUnitId = None
        self.NodeUnitTemplateIDs = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeUnitTemplateIDs = params.get("NodeUnitTemplateIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeNodeUnitTemplatesResponse(AbstractModel):
    """DeleteEdgeNodeUnitTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeNodesRequest(AbstractModel):
    """DeleteEdgeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeIds: IECP边缘节点ID列表
        :type NodeIds: list of int non-negative
        """
        self.EdgeUnitId = None
        self.NodeIds = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeIds = params.get("NodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeNodesResponse(AbstractModel):
    """DeleteEdgeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeUnitApplicationsRequest(AbstractModel):
    """DeleteEdgeUnitApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param ApplicationIDs: 应用ID列表
        :type ApplicationIDs: list of int non-negative
        """
        self.EdgeUnitID = None
        self.ApplicationIDs = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.ApplicationIDs = params.get("ApplicationIDs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitApplicationsResponse(AbstractModel):
    """DeleteEdgeUnitApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeUnitCloudRequest(AbstractModel):
    """DeleteEdgeUnitCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 边缘集群ID
        :type EdgeUnitId: int
        """
        self.EdgeUnitId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitCloudResponse(AbstractModel):
    """DeleteEdgeUnitCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeUnitDeployGridItemRequest(AbstractModel):
    """DeleteEdgeUnitDeployGridItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param GridItemName: Grid部署名称
        :type GridItemName: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.WorkloadKind = None
        self.GridItemName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.WorkloadKind = params.get("WorkloadKind")
        self.GridItemName = params.get("GridItemName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitDeployGridItemResponse(AbstractModel):
    """DeleteEdgeUnitDeployGridItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteEdgeUnitPodRequest(AbstractModel):
    """DeleteEdgeUnitPod请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterID: 集群ID
        :type ClusterID: str
        :param PodName: Pod名称
        :type PodName: str
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.ClusterID = None
        self.PodName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.ClusterID = params.get("ClusterID")
        self.PodName = params.get("PodName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeUnitPodResponse(AbstractModel):
    """DeleteEdgeUnitPod返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNamespaceRequest(AbstractModel):
    """DeleteNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.EdgeUnitID = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNamespaceResponse(AbstractModel):
    """DeleteNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNodeUnitRequest(AbstractModel):
    """DeleteNodeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeGroupName: NodeUnit所属的NodeGroup名称
        :type NodeGroupName: str
        :param NodeUnitName: NodeUnit名称
        :type NodeUnitName: str
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        :param Nodes: NodeUnit包含的节点列表
        :type Nodes: list of str
        """
        self.EdgeUnitId = None
        self.NodeGroupName = None
        self.NodeUnitName = None
        self.Namespace = None
        self.Nodes = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeGroupName = params.get("NodeGroupName")
        self.NodeUnitName = params.get("NodeUnitName")
        self.Namespace = params.get("Namespace")
        self.Nodes = params.get("Nodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNodeUnitResponse(AbstractModel):
    """DeleteNodeUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param SecretName: secret名称
        :type SecretName: str
        :param SecretNamespace: secret命名空间（默认:default）
        :type SecretNamespace: str
        """
        self.EdgeUnitID = None
        self.SecretName = None
        self.SecretNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.SecretName = params.get("SecretName")
        self.SecretNamespace = params.get("SecretNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeApplicationVisualizationRequest(AbstractModel):
    """DescribeApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用模板ID
        :type ApplicationId: int
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationVisualizationResponse(AbstractModel):
    """DescribeApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param BasicInfo: 基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param BasicConfig: 基本配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param Volumes: 卷配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Volumes: list of Volume
        :param InitContainers: 初始化容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InitContainers: list of Container
        :param Containers: 容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: list of Container
        :param Service: 服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param Job: Job配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param CronJob: CronJob配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param RestartPolicy: 重启策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartPolicy: str
        :param HorizontalPodAutoscaler: HPA
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param ImagePullSecrets: 镜像拉取Secret
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePullSecrets: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BasicInfo = None
        self.BasicConfig = None
        self.Volumes = None
        self.InitContainers = None
        self.Containers = None
        self.Service = None
        self.Job = None
        self.CronJob = None
        self.RestartPolicy = None
        self.HorizontalPodAutoscaler = None
        self.ImagePullSecrets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self.BasicConfig = ApplicationBasicConfig()
            self.BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self.Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self.Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self.CronJob = CronJob()
            self.CronJob._deserialize(params.get("CronJob"))
        self.RestartPolicy = params.get("RestartPolicy")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self.ImagePullSecrets = params.get("ImagePullSecrets")
        self.RequestId = params.get("RequestId")


class DescribeApplicationYamlErrorRequest(AbstractModel):
    """DescribeApplicationYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: Yaml配置
        :type Yaml: str
        """
        self.Yaml = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationYamlErrorResponse(AbstractModel):
    """DescribeApplicationYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckPass: 是否通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param ErrInfo: 错误信息
        :type ErrInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckPass = None
        self.ErrType = None
        self.ErrInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckPass = params.get("CheckPass")
        self.ErrType = params.get("ErrType")
        self.ErrInfo = params.get("ErrInfo")
        self.RequestId = params.get("RequestId")


class DescribeApplicationYamlRequest(AbstractModel):
    """DescribeApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用模板ID
        :type ApplicationId: int
        """
        self.ApplicationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationYamlResponse(AbstractModel):
    """DescribeApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: base64 后的yaml
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Yaml = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        self.RequestId = params.get("RequestId")


class DescribeApplicationsRequest(AbstractModel):
    """DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param NamePattern: 模糊搜索字符串
        :type NamePattern: str
        :param Offset: 默认 0
        :type Offset: int
        :param Limit: 默认 20
        :type Limit: int
        :param Sort: 仅支持对 DistributeTime 字段排序，ASC/DESC
        :type Sort: list of FieldSort
        """
        self.NamePattern = None
        self.Offset = None
        self.Limit = None
        self.Sort = None


    def _deserialize(self, params):
        self.NamePattern = params.get("NamePattern")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self.Sort = []
            for item in params.get("Sort"):
                obj = FieldSort()
                obj._deserialize(item)
                self.Sort.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    """DescribeApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApplicationSet: 详细列表
        :type ApplicationSet: list of ApplicationTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ApplicationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApplicationSet") is not None:
            self.ApplicationSet = []
            for item in params.get("ApplicationSet"):
                obj = ApplicationTemplate()
                obj._deserialize(item)
                self.ApplicationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeConfigMapRequest(AbstractModel):
    """DescribeConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param ConfigMapName: ConfigMap名称
        :type ConfigMapName: str
        :param ConfigMapNamespace: ConfigMap命名空间
        :type ConfigMapNamespace: str
        """
        self.EdgeUnitID = None
        self.ConfigMapName = None
        self.ConfigMapNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.ConfigMapName = params.get("ConfigMapName")
        self.ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMapResponse(AbstractModel):
    """DescribeConfigMap返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Yaml: yaml配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param Json: 配置项的json格式(base64编码)
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Namespace = None
        self.CreateTime = None
        self.Yaml = None
        self.Json = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreateTime = params.get("CreateTime")
        self.Yaml = params.get("Yaml")
        self.Json = params.get("Json")
        self.RequestId = params.get("RequestId")


class DescribeConfigMapYamlErrorRequest(AbstractModel):
    """DescribeConfigMapYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: yaml文件
        :type Yaml: str
        """
        self.Yaml = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMapYamlErrorResponse(AbstractModel):
    """DescribeConfigMapYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckPass: 校验是通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param ErrInfo: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckPass = None
        self.ErrType = None
        self.ErrInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckPass = params.get("CheckPass")
        self.ErrType = params.get("ErrType")
        self.ErrInfo = params.get("ErrInfo")
        self.RequestId = params.get("RequestId")


class DescribeConfigMapsRequest(AbstractModel):
    """DescribeConfigMaps请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param Offset: 翻页偏移量
        :type Offset: int
        :param Limit: 每页大小(最大100)
        :type Limit: int
        :param ConfigMapNamespace: 命名空间
        :type ConfigMapNamespace: str
        :param NamePattern: 模糊匹配的名称
        :type NamePattern: str
        :param Sort: Sort.Fileld填写CreateTime Sort.Order(ASC|DESC) 默认ASC
        :type Sort: :class:`tencentcloud.iecp.v20210914.models.FieldSort`
        """
        self.EdgeUnitID = None
        self.Offset = None
        self.Limit = None
        self.ConfigMapNamespace = None
        self.NamePattern = None
        self.Sort = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ConfigMapNamespace = params.get("ConfigMapNamespace")
        self.NamePattern = params.get("NamePattern")
        if params.get("Sort") is not None:
            self.Sort = FieldSort()
            self.Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigMapsResponse(AbstractModel):
    """DescribeConfigMaps返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: ConfigMap列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ConfigMapBasicInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ConfigMapBasicInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeAgentNodeInstallerRequest(AbstractModel):
    """DescribeEdgeAgentNodeInstaller请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeId: IECP边缘节点ID
        :type NodeId: int
        """
        self.EdgeUnitId = None
        self.NodeId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeAgentNodeInstallerResponse(AbstractModel):
    """DescribeEdgeAgentNodeInstaller返回参数结构体

    """

    def __init__(self):
        r"""
        :param Online: 节点在线安装信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: :class:`tencentcloud.iecp.v20210914.models.EdgeNodeInstallerOnline`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Online = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Online") is not None:
            self.Online = EdgeNodeInstallerOnline()
            self.Online._deserialize(params.get("Online"))
        self.RequestId = params.get("RequestId")


class DescribeEdgeDefaultVpcRequest(AbstractModel):
    """DescribeEdgeDefaultVpc请求参数结构体

    """


class DescribeEdgeDefaultVpcResponse(AbstractModel):
    """DescribeEdgeDefaultVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param VpcCidrBlock: 网络CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcCidrBlock: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param SubnetCidrBlock: 子网CIDR
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetCidrBlock: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcId = None
        self.VpcCidrBlock = None
        self.SubnetId = None
        self.SubnetCidrBlock = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetId = params.get("SubnetId")
        self.SubnetCidrBlock = params.get("SubnetCidrBlock")
        self.RequestId = params.get("RequestId")


class DescribeEdgeNodePodContainersRequest(AbstractModel):
    """DescribeEdgeNodePodContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeId: 节点ID
        :type NodeId: int
        :param PodName: Pod名称
        :type PodName: str
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.NodeId = None
        self.PodName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeId = params.get("NodeId")
        self.PodName = params.get("PodName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodePodContainersResponse(AbstractModel):
    """DescribeEdgeNodePodContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerSet: Pod容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerSet: list of EdgeNodePodContainerInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContainerSet") is not None:
            self.ContainerSet = []
            for item in params.get("ContainerSet"):
                obj = EdgeNodePodContainerInfo()
                obj._deserialize(item)
                self.ContainerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeNodePodsRequest(AbstractModel):
    """DescribeEdgeNodePods请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeId: 节点ID
        :type NodeId: int
        :param Namespace: 命名空间
        :type Namespace: str
        :param PodNamePattern: Pod名称过滤串
        :type PodNamePattern: str
        """
        self.EdgeUnitId = None
        self.NodeId = None
        self.Namespace = None
        self.PodNamePattern = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeId = params.get("NodeId")
        self.Namespace = params.get("Namespace")
        self.PodNamePattern = params.get("PodNamePattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodePodsResponse(AbstractModel):
    """DescribeEdgeNodePods返回参数结构体

    """

    def __init__(self):
        r"""
        :param PodSet: Pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSet: list of EdgeNodePodInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PodSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PodSet") is not None:
            self.PodSet = []
            for item in params.get("PodSet"):
                obj = EdgeNodePodInfo()
                obj._deserialize(item)
                self.PodSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeNodeRequest(AbstractModel):
    """DescribeEdgeNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeId: IECP边缘节点ID
        :type NodeId: int
        """
        self.EdgeUnitId = None
        self.NodeId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodeResponse(AbstractModel):
    """DescribeEdgeNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 节点ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Kind: 节点类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Kind: str
        :param Name: 节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 节点状态 （1健康｜2异常｜3离线｜4未激活）
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CpuArchitecture: CPU体系结构
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuArchitecture: str
        :param AiChipArchitecture: AI处理器体系结构
注意：此字段可能返回 null，表示取不到有效值。
        :type AiChipArchitecture: str
        :param Ip: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param Labels: 节点标签列表
        :type Labels: list of EdgeNodeLabel
        :param Resource: 节点资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.iecp.v20210914.models.EdgeNodeResourceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Id = None
        self.Kind = None
        self.Name = None
        self.Status = None
        self.CpuArchitecture = None
        self.AiChipArchitecture = None
        self.Ip = None
        self.Labels = None
        self.Resource = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Kind = params.get("Kind")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.CpuArchitecture = params.get("CpuArchitecture")
        self.AiChipArchitecture = params.get("AiChipArchitecture")
        self.Ip = params.get("Ip")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = EdgeNodeLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("Resource") is not None:
            self.Resource = EdgeNodeResourceInfo()
            self.Resource._deserialize(params.get("Resource"))
        self.RequestId = params.get("RequestId")


class DescribeEdgeNodesRequest(AbstractModel):
    """DescribeEdgeNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NamePattern: 边缘节点名称模糊搜索串
        :type NamePattern: str
        :param NameMatchedList: 边缘节点名称列表，支持批量查询 ，优先于模糊查询
        :type NameMatchedList: list of str
        :param Sort: 排序信息列表
        :type Sort: list of Sort
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 页面大小Limit
        :type Limit: int
        :param NodeType: 节点类型
        :type NodeType: int
        """
        self.EdgeUnitId = None
        self.NamePattern = None
        self.NameMatchedList = None
        self.Sort = None
        self.Offset = None
        self.Limit = None
        self.NodeType = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NamePattern = params.get("NamePattern")
        self.NameMatchedList = params.get("NameMatchedList")
        if params.get("Sort") is not None:
            self.Sort = []
            for item in params.get("Sort"):
                obj = Sort()
                obj._deserialize(item)
                self.Sort.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NodeType = params.get("NodeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeNodesResponse(AbstractModel):
    """DescribeEdgeNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 边缘节点数量
        :type TotalCount: int
        :param NodeSet: 节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeSet: list of EdgeNodeInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NodeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = EdgeNodeInfo()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeOperationLogsRequest(AbstractModel):
    """DescribeEdgeOperationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 翻页大小
        :type Limit: int
        :param Sort: 排序字段
        :type Sort: list of FieldSort
        :param Module: 模块
        :type Module: str
        :param Condition: 过滤条件
        :type Condition: :class:`tencentcloud.iecp.v20210914.models.OperationLogsCondition`
        """
        self.BeginTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Sort = None
        self.Module = None
        self.Condition = None


    def _deserialize(self, params):
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Sort") is not None:
            self.Sort = []
            for item in params.get("Sort"):
                obj = FieldSort()
                obj._deserialize(item)
                self.Sort.append(obj)
        self.Module = params.get("Module")
        if params.get("Condition") is not None:
            self.Condition = OperationLogsCondition()
            self.Condition._deserialize(params.get("Condition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeOperationLogsResponse(AbstractModel):
    """DescribeEdgeOperationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param OperationLogSet: 操作日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationLogSet: list of OperationLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.OperationLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("OperationLogSet") is not None:
            self.OperationLogSet = []
            for item in params.get("OperationLogSet"):
                obj = OperationLog()
                obj._deserialize(item)
                self.OperationLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgePodRequest(AbstractModel):
    """DescribeEdgePod请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Namespace: 命名空间
        :type Namespace: str
        :param Name: Pod名称
        :type Name: str
        """
        self.EdgeUnitId = None
        self.Namespace = None
        self.Name = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Namespace = params.get("Namespace")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgePodResponse(AbstractModel):
    """DescribeEdgePod返回参数结构体

    """

    def __init__(self):
        r"""
        :param Pod: Pod详情信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Pod: :class:`tencentcloud.iecp.v20210914.models.EdgeNodePodInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Pod = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Pod") is not None:
            self.Pod = EdgeNodePodInfo()
            self.Pod._deserialize(params.get("Pod"))
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationEventsRequest(AbstractModel):
    """DescribeEdgeUnitApplicationEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self.EdgeUnitId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationEventsResponse(AbstractModel):
    """DescribeEdgeUnitApplicationEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventSet: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSet: list of Event
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = Event()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationLogsRequest(AbstractModel):
    """DescribeEdgeUnitApplicationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        :param Limit: 最大条数
        :type Limit: int
        :param PodName: Pod名
        :type PodName: str
        :param ContainerName: 容器名
        :type ContainerName: str
        """
        self.EdgeUnitId = None
        self.ApplicationId = None
        self.Limit = None
        self.PodName = None
        self.ContainerName = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        self.Limit = params.get("Limit")
        self.PodName = params.get("PodName")
        self.ContainerName = params.get("ContainerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationLogsResponse(AbstractModel):
    """DescribeEdgeUnitApplicationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogSet: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogSet = params.get("LogSet")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationPodContainersRequest(AbstractModel):
    """DescribeEdgeUnitApplicationPodContainers请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        :param PodName: Pod名
        :type PodName: str
        """
        self.EdgeUnitId = None
        self.ApplicationId = None
        self.PodName = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        self.PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationPodContainersResponse(AbstractModel):
    """DescribeEdgeUnitApplicationPodContainers返回参数结构体

    """

    def __init__(self):
        r"""
        :param ContainerSet: 容器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ContainerSet: list of ContainerStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ContainerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ContainerSet") is not None:
            self.ContainerSet = []
            for item in params.get("ContainerSet"):
                obj = ContainerStatus()
                obj._deserialize(item)
                self.ContainerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationPodsRequest(AbstractModel):
    """DescribeEdgeUnitApplicationPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self.EdgeUnitId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationPodsResponse(AbstractModel):
    """DescribeEdgeUnitApplicationPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param PodSet: Pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSet: list of PodStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PodSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PodSet") is not None:
            self.PodSet = []
            for item in params.get("PodSet"):
                obj = PodStatus()
                obj._deserialize(item)
                self.PodSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationVisualizationRequest(AbstractModel):
    """DescribeEdgeUnitApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self.EdgeUnitId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationVisualizationResponse(AbstractModel):
    """DescribeEdgeUnitApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param BasicInfo: 基本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param BasicConfig: 基本配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param Volumes: 卷配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Volumes: list of Volume
        :param InitContainers: 初始化容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InitContainers: list of Container
        :param Containers: 容器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Containers: list of Container
        :param Service: 服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param Job: Job配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param CronJob: CronJob配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param RestartPolicy: 重启策略
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartPolicy: str
        :param HorizontalPodAutoscaler: HPA
注意：此字段可能返回 null，表示取不到有效值。
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param ImagePullSecrets: 镜像拉取Secret
注意：此字段可能返回 null，表示取不到有效值。
        :type ImagePullSecrets: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BasicInfo = None
        self.BasicConfig = None
        self.Volumes = None
        self.InitContainers = None
        self.Containers = None
        self.Service = None
        self.Job = None
        self.CronJob = None
        self.RestartPolicy = None
        self.HorizontalPodAutoscaler = None
        self.ImagePullSecrets = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        if params.get("BasicConfig") is not None:
            self.BasicConfig = ApplicationBasicConfig()
            self.BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self.Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self.Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self.CronJob = CronJob()
            self.CronJob._deserialize(params.get("CronJob"))
        self.RestartPolicy = params.get("RestartPolicy")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        self.ImagePullSecrets = params.get("ImagePullSecrets")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationYamlErrorRequest(AbstractModel):
    """DescribeEdgeUnitApplicationYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: Yaml配置
        :type Yaml: str
        """
        self.Yaml = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationYamlErrorResponse(AbstractModel):
    """DescribeEdgeUnitApplicationYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckPass: 是否通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param ErrInfo: 错误信息
        :type ErrInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckPass = None
        self.ErrType = None
        self.ErrInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckPass = params.get("CheckPass")
        self.ErrType = params.get("ErrType")
        self.ErrInfo = params.get("ErrInfo")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationYamlRequest(AbstractModel):
    """DescribeEdgeUnitApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self.EdgeUnitId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationYamlResponse(AbstractModel):
    """DescribeEdgeUnitApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: Yaml配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Yaml = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitApplicationsRequest(AbstractModel):
    """DescribeEdgeUnitApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param Offset: 翻页偏移
        :type Offset: int
        :param Limit: 翻页大小
        :type Limit: int
        :param NamePattern: 名称模糊匹配
        :type NamePattern: str
        :param Sort: 字段排序 (Sort.Filed为:StartTime）
        :type Sort: list of FieldSort
        :param Namespace: 命名空间过滤
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.Offset = None
        self.Limit = None
        self.NamePattern = None
        self.Sort = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamePattern = params.get("NamePattern")
        if params.get("Sort") is not None:
            self.Sort = []
            for item in params.get("Sort"):
                obj = FieldSort()
                obj._deserialize(item)
                self.Sort.append(obj)
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitApplicationsResponse(AbstractModel):
    """DescribeEdgeUnitApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApplicationSet: 应用列表
        :type ApplicationSet: list of ApplicationStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ApplicationSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApplicationSet") is not None:
            self.ApplicationSet = []
            for item in params.get("ApplicationSet"):
                obj = ApplicationStatusInfo()
                obj._deserialize(item)
                self.ApplicationSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitCloudRequest(AbstractModel):
    """DescribeEdgeUnitCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 边缘集群ID
        :type EdgeUnitId: int
        """
        self.EdgeUnitId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitCloudResponse(AbstractModel):
    """DescribeEdgeUnitCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 边缘集群名称
        :type Name: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param LiveTime: 集群最后探活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LiveTime: str
        :param MasterStatus: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterStatus: str
        :param K8sVersion: 版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type K8sVersion: str
        :param PodCIDR: pod cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type PodCIDR: str
        :param ServiceCIDR: service cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCIDR: str
        :param APIServerAddress: 集群内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type APIServerAddress: str
        :param APIServerExposeAddress: 集群外网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type APIServerExposeAddress: str
        :param UID: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UID: str
        :param UnitID: 集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitID: int
        :param Cluster: 集群标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param Node: 节点统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Node: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param Workload: 工作负载统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Workload: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param Grid: Grid应用统计
注意：此字段可能返回 null，表示取不到有效值。
        :type Grid: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param SubDevice: 设备统计
注意：此字段可能返回 null，表示取不到有效值。
        :type SubDevice: :class:`tencentcloud.iecp.v20210914.models.EdgeUnitStatisticItem`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.LiveTime = None
        self.MasterStatus = None
        self.K8sVersion = None
        self.PodCIDR = None
        self.ServiceCIDR = None
        self.APIServerAddress = None
        self.APIServerExposeAddress = None
        self.UID = None
        self.UnitID = None
        self.Cluster = None
        self.Node = None
        self.Workload = None
        self.Grid = None
        self.SubDevice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.LiveTime = params.get("LiveTime")
        self.MasterStatus = params.get("MasterStatus")
        self.K8sVersion = params.get("K8sVersion")
        self.PodCIDR = params.get("PodCIDR")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.APIServerAddress = params.get("APIServerAddress")
        self.APIServerExposeAddress = params.get("APIServerExposeAddress")
        self.UID = params.get("UID")
        self.UnitID = params.get("UnitID")
        self.Cluster = params.get("Cluster")
        if params.get("Node") is not None:
            self.Node = EdgeUnitStatisticItem()
            self.Node._deserialize(params.get("Node"))
        if params.get("Workload") is not None:
            self.Workload = EdgeUnitStatisticItem()
            self.Workload._deserialize(params.get("Workload"))
        if params.get("Grid") is not None:
            self.Grid = EdgeUnitStatisticItem()
            self.Grid._deserialize(params.get("Grid"))
        if params.get("SubDevice") is not None:
            self.SubDevice = EdgeUnitStatisticItem()
            self.SubDevice._deserialize(params.get("SubDevice"))
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitDeployGridItemRequest(AbstractModel):
    """DescribeEdgeUnitDeployGridItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param GridName: Grid名称
        :type GridName: str
        :param WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        :param Order: 排序，默认ASC
        :type Order: str
        """
        self.EdgeUnitId = None
        self.GridName = None
        self.WorkloadKind = None
        self.Namespace = None
        self.Order = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.GridName = params.get("GridName")
        self.WorkloadKind = params.get("WorkloadKind")
        self.Namespace = params.get("Namespace")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitDeployGridItemResponse(AbstractModel):
    """DescribeEdgeUnitDeployGridItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param DeploySet: Grid部署列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploySet: list of GridItemInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeploySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeploySet") is not None:
            self.DeploySet = []
            for item in params.get("DeploySet"):
                obj = GridItemInfo()
                obj._deserialize(item)
                self.DeploySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitDeployGridItemYamlRequest(AbstractModel):
    """DescribeEdgeUnitDeployGridItemYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param GridItemName: Grid部署项名称
        :type GridItemName: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.WorkloadKind = None
        self.GridItemName = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.WorkloadKind = params.get("WorkloadKind")
        self.GridItemName = params.get("GridItemName")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitDeployGridItemYamlResponse(AbstractModel):
    """DescribeEdgeUnitDeployGridItemYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: yaml，base64编码字符串
        :type Yaml: str
        :param Replicas: 对应类型的副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Yaml = None
        self.Replicas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        self.Replicas = params.get("Replicas")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitDeployGridRequest(AbstractModel):
    """DescribeEdgeUnitDeployGrid请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        :param NamePattern: 模糊匹配
        :type NamePattern: str
        :param Offset: 分页offset，默认为0
        :type Offset: int
        :param Limit: 分页limit，默认为20
        :type Limit: int
        :param Order: 排序，默认为ASC
        :type Order: str
        """
        self.EdgeUnitId = None
        self.Namespace = None
        self.NamePattern = None
        self.Offset = None
        self.Limit = None
        self.Order = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Namespace = params.get("Namespace")
        self.NamePattern = params.get("NamePattern")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitDeployGridResponse(AbstractModel):
    """DescribeEdgeUnitDeployGrid返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param GridSet: Grid列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GridSet: list of GridInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GridSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GridSet") is not None:
            self.GridSet = []
            for item in params.get("GridSet"):
                obj = GridInfo()
                obj._deserialize(item)
                self.GridSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitExtraRequest(AbstractModel):
    """DescribeEdgeUnitExtra请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        """
        self.EdgeUnitId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitExtraResponse(AbstractModel):
    """DescribeEdgeUnitExtra返回参数结构体

    """

    def __init__(self):
        r"""
        :param APIServerType: APIServer类型
        :type APIServerType: str
        :param APIServerURL: 域名URL
        :type APIServerURL: str
        :param APIServerURLPort: 域名URL对应的端口
        :type APIServerURLPort: str
        :param APIServerResolveIP: 域名URL对应的端口
        :type APIServerResolveIP: str
        :param APIServerExposeAddress: 对外可访问的IP
        :type APIServerExposeAddress: str
        :param IsCreatePrometheus: 是否开启监控
        :type IsCreatePrometheus: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.APIServerType = None
        self.APIServerURL = None
        self.APIServerURLPort = None
        self.APIServerResolveIP = None
        self.APIServerExposeAddress = None
        self.IsCreatePrometheus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.APIServerType = params.get("APIServerType")
        self.APIServerURL = params.get("APIServerURL")
        self.APIServerURLPort = params.get("APIServerURLPort")
        self.APIServerResolveIP = params.get("APIServerResolveIP")
        self.APIServerExposeAddress = params.get("APIServerExposeAddress")
        self.IsCreatePrometheus = params.get("IsCreatePrometheus")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitGridEventsRequest(AbstractModel):
    """DescribeEdgeUnitGridEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param GridName: Grid名称
        :type GridName: str
        :param WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        :param NodeUnit: NodeUnit名称
        :type NodeUnit: str
        :param PodName: Pod名称
        :type PodName: str
        """
        self.EdgeUnitId = None
        self.GridName = None
        self.WorkloadKind = None
        self.Namespace = None
        self.NodeUnit = None
        self.PodName = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.GridName = params.get("GridName")
        self.WorkloadKind = params.get("WorkloadKind")
        self.Namespace = params.get("Namespace")
        self.NodeUnit = params.get("NodeUnit")
        self.PodName = params.get("PodName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitGridEventsResponse(AbstractModel):
    """DescribeEdgeUnitGridEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param EventSet: 事件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EventSet: list of GridEventInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EventSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EventSet") is not None:
            self.EventSet = []
            for item in params.get("EventSet"):
                obj = GridEventInfo()
                obj._deserialize(item)
                self.EventSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitGridPodsRequest(AbstractModel):
    """DescribeEdgeUnitGridPods请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param GridName: Grid名称
        :type GridName: str
        :param WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param NodeUnit: NodeUnit名
        :type NodeUnit: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.GridName = None
        self.WorkloadKind = None
        self.NodeUnit = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.GridName = params.get("GridName")
        self.WorkloadKind = params.get("WorkloadKind")
        self.NodeUnit = params.get("NodeUnit")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitGridPodsResponse(AbstractModel):
    """DescribeEdgeUnitGridPods返回参数结构体

    """

    def __init__(self):
        r"""
        :param PodSet: Pod列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PodSet: list of GridPodInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PodSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PodSet") is not None:
            self.PodSet = []
            for item in params.get("PodSet"):
                obj = GridPodInfo()
                obj._deserialize(item)
                self.PodSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitMonitorStatusRequest(AbstractModel):
    """DescribeEdgeUnitMonitorStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        """
        self.EdgeUnitId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitMonitorStatusResponse(AbstractModel):
    """DescribeEdgeUnitMonitorStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param MonitorStatus: 监控状态描述：
"running" 单元监控正常运行
"deploying" 单元监控部署中
"norsc" 单元需要可用节点以部署监控
"abnormal" 单元监控异常
"none" 单元监控不可用
        :type MonitorStatus: str
        :param IsAvailable: 监控是否就绪
        :type IsAvailable: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MonitorStatus = None
        self.IsAvailable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MonitorStatus = params.get("MonitorStatus")
        self.IsAvailable = params.get("IsAvailable")
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitNodeGroupRequest(AbstractModel):
    """DescribeEdgeUnitNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        :param Offset: 分页offset，默认为0
        :type Offset: int
        :param Limit: 分页limit，默认为20
        :type Limit: int
        :param NameFilter: 模糊匹配参数，精确匹配时失效
        :type NameFilter: str
        :param NameMatched: 精确匹配参数
        :type NameMatched: str
        :param Order: 按时间排序，ASC/DESC，默认为DESC
        :type Order: str
        """
        self.EdgeUnitId = None
        self.Namespace = None
        self.Offset = None
        self.Limit = None
        self.NameFilter = None
        self.NameMatched = None
        self.Order = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Namespace = params.get("Namespace")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NameFilter = params.get("NameFilter")
        self.NameMatched = params.get("NameMatched")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitNodeGroupResponse(AbstractModel):
    """DescribeEdgeUnitNodeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param NodeGroupInfo: NodeGroup数组
        :type NodeGroupInfo: list of NodeGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.NodeGroupInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("NodeGroupInfo") is not None:
            self.NodeGroupInfo = []
            for item in params.get("NodeGroupInfo"):
                obj = NodeGroupInfo()
                obj._deserialize(item)
                self.NodeGroupInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitNodeUnitTemplatesRequest(AbstractModel):
    """DescribeEdgeUnitNodeUnitTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param Namespace: 命名空间，默认为default
        :type Namespace: str
        :param Offset: 分页查询offset，默认为0
        :type Offset: int
        :param Limit: 分页查询limit，默认为20
        :type Limit: int
        :param NameFilter: 模糊匹配，精确匹配时失效
        :type NameFilter: str
        :param NameMatched: 精确匹配
        :type NameMatched: str
        :param Order: 按时间排序顺序，默认为DESC
        :type Order: str
        """
        self.EdgeUnitId = None
        self.Namespace = None
        self.Offset = None
        self.Limit = None
        self.NameFilter = None
        self.NameMatched = None
        self.Order = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Namespace = params.get("Namespace")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NameFilter = params.get("NameFilter")
        self.NameMatched = params.get("NameMatched")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitNodeUnitTemplatesResponse(AbstractModel):
    """DescribeEdgeUnitNodeUnitTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 符合查询条件的记录总数
        :type Total: int
        :param NodeUnitTemplates: NodeUnit模版列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeUnitTemplates: list of NodeUnitTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.NodeUnitTemplates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("NodeUnitTemplates") is not None:
            self.NodeUnitTemplates = []
            for item in params.get("NodeUnitTemplates"):
                obj = NodeUnitTemplate()
                obj._deserialize(item)
                self.NodeUnitTemplates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEdgeUnitsCloudRequest(AbstractModel):
    """DescribeEdgeUnitsCloud请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: limit值
        :type Limit: int
        :param NamePattern: 集群名称模糊匹配
        :type NamePattern: str
        :param Order: 排序，ASC/DESC(默认)
        :type Order: str
        """
        self.Offset = None
        self.Limit = None
        self.NamePattern = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.NamePattern = params.get("NamePattern")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeUnitsCloudResponse(AbstractModel):
    """DescribeEdgeUnitsCloud返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EdgeUnitSet: 集群详情
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeUnitSet: list of EdgeCloudCluster
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.EdgeUnitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EdgeUnitSet") is not None:
            self.EdgeUnitSet = []
            for item in params.get("EdgeUnitSet"):
                obj = EdgeCloudCluster()
                obj._deserialize(item)
                self.EdgeUnitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMonitorMetricsRequest(AbstractModel):
    """DescribeMonitorMetrics请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param QueryType: 查询维度
        :type QueryType: str
        :param StartTime: 起始时间Unix秒时间戳
        :type StartTime: int
        :param EndTime: 终止时间Unix秒时间戳
        :type EndTime: int
        :param Interval: 步长（分钟）
        :type Interval: int
        :param NodeName: 节点名称，查询节点监控时必填
        :type NodeName: str
        :param Namespace: 命名空间，不填则默认为default
        :type Namespace: str
        :param PodName: Pod名称，查询Pod监控时必填
        :type PodName: str
        :param WorkloadName: Workload名称，查询Workload监控时必填
        :type WorkloadName: str
        """
        self.EdgeUnitId = None
        self.QueryType = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.NodeName = None
        self.Namespace = None
        self.PodName = None
        self.WorkloadName = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.QueryType = params.get("QueryType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.NodeName = params.get("NodeName")
        self.Namespace = params.get("Namespace")
        self.PodName = params.get("PodName")
        self.WorkloadName = params.get("WorkloadName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorMetricsResponse(AbstractModel):
    """DescribeMonitorMetrics返回参数结构体

    """

    def __init__(self):
        r"""
        :param Metrics: 查询监控指标结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of MonitorMetricsColumn
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Metrics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Metrics") is not None:
            self.Metrics = []
            for item in params.get("Metrics"):
                obj = MonitorMetricsColumn()
                obj._deserialize(item)
                self.Metrics.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNamespaceRequest(AbstractModel):
    """DescribeNamespace请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param Namespace: 命名空间名
        :type Namespace: str
        """
        self.EdgeUnitID = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespaceResourcesRequest(AbstractModel):
    """DescribeNamespaceResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param Namespace: 命名空间
        :type Namespace: str
        """
        self.EdgeUnitID = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespaceResourcesResponse(AbstractModel):
    """DescribeNamespaceResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param Resources: 资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of NamespaceResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Resources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Resources") is not None:
            self.Resources = []
            for item in params.get("Resources"):
                obj = NamespaceResource()
                obj._deserialize(item)
                self.Resources.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNamespaceResponse(AbstractModel):
    """DescribeNamespace返回参数结构体

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param Status: 状态 (Active|Terminating)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Protected: 是否保护-不允许删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Protected: bool
        :param Yaml: Yaml文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Namespace = None
        self.Status = None
        self.Description = None
        self.CreateTime = None
        self.Protected = None
        self.Yaml = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Protected = params.get("Protected")
        self.Yaml = params.get("Yaml")
        self.RequestId = params.get("RequestId")


class DescribeNamespacesRequest(AbstractModel):
    """DescribeNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: IECP边缘单元ID
        :type EdgeUnitID: int
        :param NamePattern: 边缘节点名称模糊搜索串
        :type NamePattern: str
        """
        self.EdgeUnitID = None
        self.NamePattern = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.NamePattern = params.get("NamePattern")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNamespacesResponse(AbstractModel):
    """DescribeNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param Items: 命名空间信息列表
        :type Items: list of NamespaceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = NamespaceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeUnitRequest(AbstractModel):
    """DescribeNodeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 边缘单元ID
        :type EdgeUnitId: int
        :param NodeGroupName: NodeUnit所属的NodeGroup名称
        :type NodeGroupName: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        :param Limit: 分页查询limit，默认20
        :type Limit: int
        :param Offset: 分页查询offset，默认0
        :type Offset: int
        :param NameFilter: 模糊匹配
        :type NameFilter: str
        """
        self.EdgeUnitId = None
        self.NodeGroupName = None
        self.Namespace = None
        self.Limit = None
        self.Offset = None
        self.NameFilter = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeGroupName = params.get("NodeGroupName")
        self.Namespace = params.get("Namespace")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.NameFilter = params.get("NameFilter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeUnitResponse(AbstractModel):
    """DescribeNodeUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的记录总数
        :type TotalCount: int
        :param NodeGridInfo: NodeUnit信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeGridInfo: list of NodeUnitInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.NodeGridInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NodeGridInfo") is not None:
            self.NodeGridInfo = []
            for item in params.get("NodeGridInfo"):
                obj = NodeUnitInfo()
                obj._deserialize(item)
                self.NodeGridInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeUnitTemplateOnNodeGroupRequest(AbstractModel):
    """DescribeNodeUnitTemplateOnNodeGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeGroupName: NodeGroup名称
        :type NodeGroupName: str
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        :param NodeUnitNamePattern: 名称模糊匹配
        :type NodeUnitNamePattern: str
        :param Offset: 分页查询offset，默认0
        :type Offset: int
        :param Limit: 分页查询limit，默认20
        :type Limit: int
        :param Order: 排序，默认DESC
        :type Order: str
        """
        self.EdgeUnitId = None
        self.NodeGroupName = None
        self.Namespace = None
        self.NodeUnitNamePattern = None
        self.Offset = None
        self.Limit = None
        self.Order = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeGroupName = params.get("NodeGroupName")
        self.Namespace = params.get("Namespace")
        self.NodeUnitNamePattern = params.get("NodeUnitNamePattern")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeUnitTemplateOnNodeGroupResponse(AbstractModel):
    """DescribeNodeUnitTemplateOnNodeGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param NodeUnitTemplates: NodeUnit模版
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeUnitTemplates: list of NodeGroupNodeUnitTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.NodeUnitTemplates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("NodeUnitTemplates") is not None:
            self.NodeUnitTemplates = []
            for item in params.get("NodeUnitTemplates"):
                obj = NodeGroupNodeUnitTemplateInfo()
                obj._deserialize(item)
                self.NodeUnitTemplates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 边缘单元ID
        :type EdgeUnitID: int
        :param SecretName: secret名
        :type SecretName: str
        :param SecretNamespace: 命名空间(默认值:default）
        :type SecretNamespace: str
        """
        self.EdgeUnitID = None
        self.SecretName = None
        self.SecretNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.SecretName = params.get("SecretName")
        self.SecretNamespace = params.get("SecretNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param Name: Secret名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Yaml: secret的yaml格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        :param Json: secret的json格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Json: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Name = None
        self.Namespace = None
        self.CreateTime = None
        self.Yaml = None
        self.Json = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreateTime = params.get("CreateTime")
        self.Yaml = params.get("Yaml")
        self.Json = params.get("Json")
        self.RequestId = params.get("RequestId")


class DescribeSecretYamlErrorRequest(AbstractModel):
    """DescribeSecretYamlError请求参数结构体

    """

    def __init__(self):
        r"""
        :param Yaml: yaml文件
        :type Yaml: str
        """
        self.Yaml = None


    def _deserialize(self, params):
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretYamlErrorResponse(AbstractModel):
    """DescribeSecretYamlError返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckPass: 校验是通过
注意：此字段可能返回 null，表示取不到有效值。
        :type CheckPass: bool
        :param ErrType: 错误类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrType: int
        :param ErrInfo: 错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrInfo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckPass = None
        self.ErrType = None
        self.ErrInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckPass = params.get("CheckPass")
        self.ErrType = params.get("ErrType")
        self.ErrInfo = params.get("ErrInfo")
        self.RequestId = params.get("RequestId")


class DescribeSecretsRequest(AbstractModel):
    """DescribeSecrets请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 边缘单元ID
        :type EdgeUnitID: int
        :param Offset: 页号
        :type Offset: int
        :param Limit: 每页数目
        :type Limit: int
        :param SecretNamespace: 命名空间
        :type SecretNamespace: str
        :param NamePattern: Secret名(模糊匹配)
        :type NamePattern: str
        :param Sort: Sort.Field:CreateTime Sort.Order:ASC|DESC
        :type Sort: :class:`tencentcloud.iecp.v20210914.models.FieldSort`
        :param SecretType: Secret类型(DockerConfigJson或Opaque)
        :type SecretType: str
        """
        self.EdgeUnitID = None
        self.Offset = None
        self.Limit = None
        self.SecretNamespace = None
        self.NamePattern = None
        self.Sort = None
        self.SecretType = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SecretNamespace = params.get("SecretNamespace")
        self.NamePattern = params.get("NamePattern")
        if params.get("Sort") is not None:
            self.Sort = FieldSort()
            self.Sort._deserialize(params.get("Sort"))
        self.SecretType = params.get("SecretType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretsResponse(AbstractModel):
    """DescribeSecrets返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数目
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Items: Secret列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SecretItem
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
                obj = SecretItem()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DockerConfig(AbstractModel):
    """docker配置

    """

    def __init__(self):
        r"""
        :param RegistryDomain: 镜像仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryDomain: str
        :param UserName: 用户名
        :type UserName: str
        :param Password: 密码
        :type Password: str
        """
        self.RegistryDomain = None
        self.UserName = None
        self.Password = None


    def _deserialize(self, params):
        self.RegistryDomain = params.get("RegistryDomain")
        self.UserName = params.get("UserName")
        self.Password = params.get("Password")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeCloudCluster(AbstractModel):
    """获取边缘集群列表

    """

    def __init__(self):
        r"""
        :param EdgeId: IECP侧边缘集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeId: int
        :param ClusterId: 边缘集群ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Region: 区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param ClusterName: 集群名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterName: str
        :param K8SVersion: 集群版本
注意：此字段可能返回 null，表示取不到有效值。
        :type K8SVersion: str
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param ClusterDesc: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterDesc: str
        :param Status: 集群状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param PodCIDR: pod cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type PodCIDR: str
        :param ServiceCIDR: service cidr
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCIDR: str
        :param EdgeClusterVersion: 边缘版本类型
注意：此字段可能返回 null，表示取不到有效值。
        :type EdgeClusterVersion: str
        :param UID: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UID: str
        """
        self.EdgeId = None
        self.ClusterId = None
        self.Region = None
        self.ClusterName = None
        self.K8SVersion = None
        self.VpcId = None
        self.ClusterDesc = None
        self.Status = None
        self.CreateTime = None
        self.PodCIDR = None
        self.ServiceCIDR = None
        self.EdgeClusterVersion = None
        self.UID = None


    def _deserialize(self, params):
        self.EdgeId = params.get("EdgeId")
        self.ClusterId = params.get("ClusterId")
        self.Region = params.get("Region")
        self.ClusterName = params.get("ClusterName")
        self.K8SVersion = params.get("K8SVersion")
        self.VpcId = params.get("VpcId")
        self.ClusterDesc = params.get("ClusterDesc")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.PodCIDR = params.get("PodCIDR")
        self.ServiceCIDR = params.get("ServiceCIDR")
        self.EdgeClusterVersion = params.get("EdgeClusterVersion")
        self.UID = params.get("UID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeInfo(AbstractModel):
    """边缘节点信息

    """

    def __init__(self):
        r"""
        :param Id: IECP边缘节点ID
        :type Id: int
        :param Name: 节点名称
        :type Name: str
        :param Status: 节点状态 （1健康｜2异常｜3离线｜4未激活）
        :type Status: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Resource: 节点资源信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Resource: :class:`tencentcloud.iecp.v20210914.models.EdgeNodeResourceInfo`
        :param CpuArchitecture: CPU体系结构
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuArchitecture: str
        :param Ip: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param OperatingSystem: 操作系统
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatingSystem: str
        :param NodeUnits: 节点所属的NodeUnit
key：NodeUnit模版ID，Value：NodeUnit模版名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeUnits: :class:`tencentcloud.iecp.v20210914.models.KeyValueObj`
        """
        self.Id = None
        self.Name = None
        self.Status = None
        self.CreateTime = None
        self.Resource = None
        self.CpuArchitecture = None
        self.Ip = None
        self.OperatingSystem = None
        self.NodeUnits = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        if params.get("Resource") is not None:
            self.Resource = EdgeNodeResourceInfo()
            self.Resource._deserialize(params.get("Resource"))
        self.CpuArchitecture = params.get("CpuArchitecture")
        self.Ip = params.get("Ip")
        self.OperatingSystem = params.get("OperatingSystem")
        if params.get("NodeUnits") is not None:
            self.NodeUnits = KeyValueObj()
            self.NodeUnits._deserialize(params.get("NodeUnits"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeInstallerOnline(AbstractModel):
    """节点在线安装信息

    """

    def __init__(self):
        r"""
        :param ScriptName: 节点安装脚本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptName: str
        :param ScriptDownloadUrl: 节点安装脚本下载链接
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptDownloadUrl: str
        :param Guide: 节点安装命令
注意：此字段可能返回 null，表示取不到有效值。
        :type Guide: str
        """
        self.ScriptName = None
        self.ScriptDownloadUrl = None
        self.Guide = None


    def _deserialize(self, params):
        self.ScriptName = params.get("ScriptName")
        self.ScriptDownloadUrl = params.get("ScriptDownloadUrl")
        self.Guide = params.get("Guide")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeLabel(AbstractModel):
    """边缘节点标签

    """

    def __init__(self):
        r"""
        :param Key: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param Value: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param Protected: 是否受保护
        :type Protected: bool
        """
        self.Key = None
        self.Value = None
        self.Protected = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        self.Protected = params.get("Protected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodePodContainerInfo(AbstractModel):
    """边缘节点Pod容器信息

    """

    def __init__(self):
        r"""
        :param Name: Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Id: 容器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param Image: 镜像（含版本号）
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param CpuRequest: CPU Request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param CpuLimit: CPU Limit
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuLimit: str
        :param MemoryRequest: Memory Request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryRequest: str
        :param MemoryLimit: Memory Limit
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryLimit: str
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param Status: 容器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.Name = None
        self.Id = None
        self.Image = None
        self.CpuRequest = None
        self.CpuLimit = None
        self.MemoryRequest = None
        self.MemoryLimit = None
        self.RestartCount = None
        self.Status = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Image = params.get("Image")
        self.CpuRequest = params.get("CpuRequest")
        self.CpuLimit = params.get("CpuLimit")
        self.MemoryRequest = params.get("MemoryRequest")
        self.MemoryLimit = params.get("MemoryLimit")
        self.RestartCount = params.get("RestartCount")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodePodInfo(AbstractModel):
    """边缘节点Pod信息

    """

    def __init__(self):
        r"""
        :param Name: Pod名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: Pod状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param NodeIp: 所在节点IP
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeIp: str
        :param Ip: 实例IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param CpuRequest: CPU Request
注意：此字段可能返回 null，表示取不到有效值。
        :type CpuRequest: str
        :param MemoryRequest: Memory Request
注意：此字段可能返回 null，表示取不到有效值。
        :type MemoryRequest: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param WorkloadType: 工作负载类型
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadType: str
        :param WorkloadName: 工作负载名称
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkloadName: str
        :param StartTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        :param ClusterID: 集群ID
        :type ClusterID: str
        """
        self.Name = None
        self.Status = None
        self.NodeIp = None
        self.Ip = None
        self.CpuRequest = None
        self.MemoryRequest = None
        self.Namespace = None
        self.WorkloadType = None
        self.WorkloadName = None
        self.StartTime = None
        self.RestartCount = None
        self.ClusterID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.NodeIp = params.get("NodeIp")
        self.Ip = params.get("Ip")
        self.CpuRequest = params.get("CpuRequest")
        self.MemoryRequest = params.get("MemoryRequest")
        self.Namespace = params.get("Namespace")
        self.WorkloadType = params.get("WorkloadType")
        self.WorkloadName = params.get("WorkloadName")
        self.StartTime = params.get("StartTime")
        self.RestartCount = params.get("RestartCount")
        self.ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeNodeResourceInfo(AbstractModel):
    """边缘节点资源信息

    """

    def __init__(self):
        r"""
        :param AllocatedCPU: 可使用的CPU 单位: m核
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedCPU: str
        :param TotalCPU: CPU总量 单位:m核
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCPU: str
        :param AllocatedMemory: 已分配的内存 单位G
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedMemory: str
        :param TotalMemory: 内存总量 单位G
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalMemory: str
        :param AllocatedGPU: 已分配的GPU资源
注意：此字段可能返回 null，表示取不到有效值。
        :type AllocatedGPU: str
        :param TotalGPU: GPU总量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalGPU: str
        :param AvailableCPU: 可使用的CPU 单位: m核
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableCPU: str
        :param AvailableMemory: 可使用的内存 单位: G
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableMemory: str
        :param AvailableGPU: 可使用的GPU资源
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableGPU: str
        """
        self.AllocatedCPU = None
        self.TotalCPU = None
        self.AllocatedMemory = None
        self.TotalMemory = None
        self.AllocatedGPU = None
        self.TotalGPU = None
        self.AvailableCPU = None
        self.AvailableMemory = None
        self.AvailableGPU = None


    def _deserialize(self, params):
        self.AllocatedCPU = params.get("AllocatedCPU")
        self.TotalCPU = params.get("TotalCPU")
        self.AllocatedMemory = params.get("AllocatedMemory")
        self.TotalMemory = params.get("TotalMemory")
        self.AllocatedGPU = params.get("AllocatedGPU")
        self.TotalGPU = params.get("TotalGPU")
        self.AvailableCPU = params.get("AvailableCPU")
        self.AvailableMemory = params.get("AvailableMemory")
        self.AvailableGPU = params.get("AvailableGPU")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeUnitStatisticItem(AbstractModel):
    """单元内的统计信息

    """

    def __init__(self):
        r"""
        :param Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param Online: 在线数
注意：此字段可能返回 null，表示取不到有效值。
        :type Online: int
        :param Abnormal: 异常数
注意：此字段可能返回 null，表示取不到有效值。
        :type Abnormal: int
        :param Offline: 离线数
注意：此字段可能返回 null，表示取不到有效值。
        :type Offline: int
        :param NotActive: 未激活
注意：此字段可能返回 null，表示取不到有效值。
        :type NotActive: int
        """
        self.Total = None
        self.Online = None
        self.Abnormal = None
        self.Offline = None
        self.NotActive = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Online = params.get("Online")
        self.Abnormal = params.get("Abnormal")
        self.Offline = params.get("Offline")
        self.NotActive = params.get("NotActive")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Env(AbstractModel):
    """环境变量

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Value: 值
        :type Value: str
        :param ValueFrom: 值引用
        :type ValueFrom: :class:`tencentcloud.iecp.v20210914.models.EnvValueSelector`
        """
        self.Name = None
        self.Value = None
        self.ValueFrom = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        if params.get("ValueFrom") is not None:
            self.ValueFrom = EnvValueSelector()
            self.ValueFrom._deserialize(params.get("ValueFrom"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvValueSelector(AbstractModel):
    """环境变量选择

    """

    def __init__(self):
        r"""
        :param Key: 健名
        :type Key: str
        :param ObjectName: 对象名
        :type ObjectName: str
        :param ObjectType: 对象值
        :type ObjectType: str
        """
        self.Key = None
        self.ObjectName = None
        self.ObjectType = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.ObjectName = params.get("ObjectName")
        self.ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Event(AbstractModel):
    """事件信息

    """

    def __init__(self):
        r"""
        :param FirstTime: 第一次出现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type FirstTime: str
        :param LastTime: 最后一次出现时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTime: str
        :param InvolvedObjectKind: 事件关联对象类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InvolvedObjectKind: str
        :param InvolvedObjectName: 事件关联对象名
注意：此字段可能返回 null，表示取不到有效值。
        :type InvolvedObjectName: str
        :param Type: 事件类型(Normal|Warning)
        :type Type: str
        :param Reason: 原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param Message: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param Count: 出现次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        """
        self.FirstTime = None
        self.LastTime = None
        self.InvolvedObjectKind = None
        self.InvolvedObjectName = None
        self.Type = None
        self.Reason = None
        self.Message = None
        self.Count = None


    def _deserialize(self, params):
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        self.InvolvedObjectKind = params.get("InvolvedObjectKind")
        self.InvolvedObjectName = params.get("InvolvedObjectName")
        self.Type = params.get("Type")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FieldSort(AbstractModel):
    """字段排序

    """

    def __init__(self):
        r"""
        :param Field: 字段名
        :type Field: str
        :param Order: 排序(ASC:升序 DESC:降序
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMarketComponentListRequest(AbstractModel):
    """GetMarketComponentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页偏移，从0开始
        :type Offset: int
        :param Limit: 每页条数
        :type Limit: int
        :param Filter: 名称模糊筛选
        :type Filter: str
        :param Order: 以名称排序，ASC、DESC
        :type Order: str
        """
        self.Offset = None
        self.Limit = None
        self.Filter = None
        self.Order = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Filter = params.get("Filter")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMarketComponentListResponse(AbstractModel):
    """GetMarketComponentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param ComponentList: 组件列表
        :type ComponentList: list of MarketComponentInfo
        :param TotalCount: 组件总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ComponentList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ComponentList") is not None:
            self.ComponentList = []
            for item in params.get("ComponentList"):
                obj = MarketComponentInfo()
                obj._deserialize(item)
                self.ComponentList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class GetMarketComponentRequest(AbstractModel):
    """GetMarketComponent请求参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 组件ID
        :type ID: int
        """
        self.ID = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetMarketComponentResponse(AbstractModel):
    """GetMarketComponent返回参数结构体

    """

    def __init__(self):
        r"""
        :param ID: 组件ID
        :type ID: int
        :param AppName: 组件名称
        :type AppName: str
        :param Author: 发行组织
        :type Author: str
        :param ReleaseTime: 发布时间
        :type ReleaseTime: str
        :param Outline: 组件简介
        :type Outline: str
        :param Detail: 详细介绍链接
        :type Detail: str
        :param Icon: 图标连接
        :type Icon: str
        :param Version: 组件版本
        :type Version: str
        :param WorkloadVisualConfig: 组件可视化配置
        :type WorkloadVisualConfig: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ID = None
        self.AppName = None
        self.Author = None
        self.ReleaseTime = None
        self.Outline = None
        self.Detail = None
        self.Icon = None
        self.Version = None
        self.WorkloadVisualConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.AppName = params.get("AppName")
        self.Author = params.get("Author")
        self.ReleaseTime = params.get("ReleaseTime")
        self.Outline = params.get("Outline")
        self.Detail = params.get("Detail")
        self.Icon = params.get("Icon")
        self.Version = params.get("Version")
        self.WorkloadVisualConfig = params.get("WorkloadVisualConfig")
        self.RequestId = params.get("RequestId")


class GridDetail(AbstractModel):
    """ServiceGroup中Grid信息

    """

    def __init__(self):
        r"""
        :param Name: Grid名称
        :type Name: str
        :param Id: GridID
        :type Id: int
        """
        self.Name = None
        self.Id = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridEventInfo(AbstractModel):
    """Grid事件信息

    """

    def __init__(self):
        r"""
        :param FirstTime: 首次出现时间
        :type FirstTime: str
        :param LastTime: 最后出现时间
        :type LastTime: str
        :param InvolvedObjectKind: 对象类型
        :type InvolvedObjectKind: str
        :param InvolvedObjectName: 对象名称
        :type InvolvedObjectName: str
        :param Type: 事件类型(Normal,Warning)
        :type Type: str
        :param Reason: 事件原因
        :type Reason: str
        :param Message: 事件内容
        :type Message: str
        :param Count: 次数
        :type Count: int
        :param NodeName: 节点名（Pod事件类型时有值）
        :type NodeName: str
        :param IP: 节点内部IP（Pod事件类型时有值）
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        """
        self.FirstTime = None
        self.LastTime = None
        self.InvolvedObjectKind = None
        self.InvolvedObjectName = None
        self.Type = None
        self.Reason = None
        self.Message = None
        self.Count = None
        self.NodeName = None
        self.IP = None


    def _deserialize(self, params):
        self.FirstTime = params.get("FirstTime")
        self.LastTime = params.get("LastTime")
        self.InvolvedObjectKind = params.get("InvolvedObjectKind")
        self.InvolvedObjectName = params.get("InvolvedObjectName")
        self.Type = params.get("Type")
        self.Reason = params.get("Reason")
        self.Message = params.get("Message")
        self.Count = params.get("Count")
        self.NodeName = params.get("NodeName")
        self.IP = params.get("IP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridInfo(AbstractModel):
    """Grid信息

    """

    def __init__(self):
        r"""
        :param Id: DeployGridId
        :type Id: int
        :param Name: 名称
        :type Name: str
        :param GridUniqKey: Key
        :type GridUniqKey: str
        :param Description: 描述
        :type Description: str
        :param WorkloadKind: 工作负载类型
        :type WorkloadKind: str
        :param StartTime: 启动时间
        :type StartTime: str
        :param Replicas: 副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param Publisher: 创建人
        :type Publisher: str
        :param Version: 版本信息
        :type Version: str
        """
        self.Id = None
        self.Name = None
        self.GridUniqKey = None
        self.Description = None
        self.WorkloadKind = None
        self.StartTime = None
        self.Replicas = None
        self.Publisher = None
        self.Version = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.GridUniqKey = params.get("GridUniqKey")
        self.Description = params.get("Description")
        self.WorkloadKind = params.get("WorkloadKind")
        self.StartTime = params.get("StartTime")
        self.Replicas = params.get("Replicas")
        self.Publisher = params.get("Publisher")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridItemInfo(AbstractModel):
    """Grid部署应用信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Replicas: 期望副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: int
        :param AvailableReplicas: 可用副本数
        :type AvailableReplicas: int
        :param StartTime: 启动时间
        :type StartTime: str
        :param WorkloadKind: 工作负载类型
        :type WorkloadKind: str
        """
        self.Name = None
        self.Replicas = None
        self.AvailableReplicas = None
        self.StartTime = None
        self.WorkloadKind = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Replicas = params.get("Replicas")
        self.AvailableReplicas = params.get("AvailableReplicas")
        self.StartTime = params.get("StartTime")
        self.WorkloadKind = params.get("WorkloadKind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GridPodInfo(AbstractModel):
    """GridPod信息

    """

    def __init__(self):
        r"""
        :param Name: Pod名称
        :type Name: str
        :param NameSpace: 命名空间
        :type NameSpace: str
        :param Status: 状态(Pending｜Running｜Succeeded｜Failed｜Unknown)
        :type Status: str
        :param NodeName: 节点名
        :type NodeName: str
        :param NodeIP: 节点IP
        :type NodeIP: str
        :param PodIP: Pod的IP
        :type PodIP: str
        :param StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param RunSec: 运行时长（秒）
注意：此字段可能返回 null，表示取不到有效值。
        :type RunSec: int
        :param RestartCount: 重启次数
        :type RestartCount: int
        :param ClusterID: 集群名称ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterID: str
        """
        self.Name = None
        self.NameSpace = None
        self.Status = None
        self.NodeName = None
        self.NodeIP = None
        self.PodIP = None
        self.StartTime = None
        self.RunSec = None
        self.RestartCount = None
        self.ClusterID = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.NameSpace = params.get("NameSpace")
        self.Status = params.get("Status")
        self.NodeName = params.get("NodeName")
        self.NodeIP = params.get("NodeIP")
        self.PodIP = params.get("PodIP")
        self.StartTime = params.get("StartTime")
        self.RunSec = params.get("RunSec")
        self.RestartCount = params.get("RestartCount")
        self.ClusterID = params.get("ClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HorizontalPodAutoscaler(AbstractModel):
    """pod水平伸缩配置

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param MinReplicas: 最小实例数
        :type MinReplicas: int
        :param MaxReplicas: 最大实例数
        :type MaxReplicas: int
        :param ResourceMetricTarget: 资源目标指标
        :type ResourceMetricTarget: list of ResourceMetricTarget
        """
        self.Name = None
        self.Namespace = None
        self.MinReplicas = None
        self.MaxReplicas = None
        self.ResourceMetricTarget = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.MinReplicas = params.get("MinReplicas")
        self.MaxReplicas = params.get("MaxReplicas")
        if params.get("ResourceMetricTarget") is not None:
            self.ResourceMetricTarget = []
            for item in params.get("ResourceMetricTarget"):
                obj = ResourceMetricTarget()
                obj._deserialize(item)
                self.ResourceMetricTarget.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeader(AbstractModel):
    """Http探测头

    """

    def __init__(self):
        r"""
        :param Name: HTTP头的名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: HTTP头的值
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
        


class HttpProbe(AbstractModel):
    """HTTP探测配置

    """

    def __init__(self):
        r"""
        :param Path: 请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Port: 请求端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Host: 请求地址，默认Pod的IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param Scheme: 请求模式  HTTP|HTTPS，默认HTTP
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: str
        :param Headers: HTTP的请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of HttpHeader
        """
        self.Path = None
        self.Port = None
        self.Host = None
        self.Scheme = None
        self.Headers = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Port = params.get("Port")
        self.Host = params.get("Host")
        self.Scheme = params.get("Scheme")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = HttpHeader()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """Job配置

    """

    def __init__(self):
        r"""
        :param Parallelism: 并发数
        :type Parallelism: int
        :param Completion: 完成数
        :type Completion: int
        :param ActiveDeadlineSeconds: 最大运行时间
        :type ActiveDeadlineSeconds: int
        :param BackOffLimit: 失败前重试次数
        :type BackOffLimit: int
        """
        self.Parallelism = None
        self.Completion = None
        self.ActiveDeadlineSeconds = None
        self.BackOffLimit = None


    def _deserialize(self, params):
        self.Parallelism = params.get("Parallelism")
        self.Completion = params.get("Completion")
        self.ActiveDeadlineSeconds = params.get("ActiveDeadlineSeconds")
        self.BackOffLimit = params.get("BackOffLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValueObj(AbstractModel):
    """KeyValue对象

    """

    def __init__(self):
        r"""
        :param Key: Key值
        :type Key: str
        :param Value: Value值
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
        


class Label(AbstractModel):
    """标签信息

    """

    def __init__(self):
        r"""
        :param Key: 健名
        :type Key: str
        :param Value: 健值
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
        


class MarketComponentInfo(AbstractModel):
    """组件市场的组件描述

    """

    def __init__(self):
        r"""
        :param ID: 组件ID
        :type ID: int
        :param AppName: 组件名称
        :type AppName: str
        :param Author: 发布者
        :type Author: str
        :param ReleaseTime: 发布时间
        :type ReleaseTime: str
        :param Outline: 组件简介
        :type Outline: str
        :param Detail: 指向详细描述的url
        :type Detail: str
        :param Icon: 图标链接
        :type Icon: str
        :param Version: 组件版本
        :type Version: str
        :param WorkloadVisualConfig: 组件可视化信息
        :type WorkloadVisualConfig: str
        """
        self.ID = None
        self.AppName = None
        self.Author = None
        self.ReleaseTime = None
        self.Outline = None
        self.Detail = None
        self.Icon = None
        self.Version = None
        self.WorkloadVisualConfig = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.AppName = params.get("AppName")
        self.Author = params.get("Author")
        self.ReleaseTime = params.get("ReleaseTime")
        self.Outline = params.get("Outline")
        self.Detail = params.get("Detail")
        self.Icon = params.get("Icon")
        self.Version = params.get("Version")
        self.WorkloadVisualConfig = params.get("WorkloadVisualConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationBasicInfoRequest(AbstractModel):
    """ModifyApplicationBasicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用模板ID
        :type ApplicationId: int
        :param BasicInfo: 应用模板基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        """
        self.ApplicationId = None
        self.BasicInfo = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationBasicInfoResponse(AbstractModel):
    """ModifyApplicationBasicInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApplicationVisualizationRequest(AbstractModel):
    """ModifyApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        :param BasicConfig: 应用配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param Volumes: 卷配置
        :type Volumes: list of Volume
        :param InitContainers: 初始容器
        :type InitContainers: list of Container
        :param Containers: 容器配置
        :type Containers: list of Container
        :param Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param RestartPolicy: 重启策略
        :type RestartPolicy: str
        :param ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        :param InitContainer: 单个初始化容器
        :type InitContainer: :class:`tencentcloud.iecp.v20210914.models.Container`
        """
        self.ApplicationId = None
        self.BasicConfig = None
        self.Volumes = None
        self.InitContainers = None
        self.Containers = None
        self.Service = None
        self.Job = None
        self.CronJob = None
        self.RestartPolicy = None
        self.ImagePullSecrets = None
        self.HorizontalPodAutoscaler = None
        self.InitContainer = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        if params.get("BasicConfig") is not None:
            self.BasicConfig = ApplicationBasicConfig()
            self.BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self.Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self.Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self.CronJob = CronJob()
            self.CronJob._deserialize(params.get("CronJob"))
        self.RestartPolicy = params.get("RestartPolicy")
        self.ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        if params.get("InitContainer") is not None:
            self.InitContainer = Container()
            self.InitContainer._deserialize(params.get("InitContainer"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationVisualizationResponse(AbstractModel):
    """ModifyApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyConfigMapRequest(AbstractModel):
    """ModifyConfigMap请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 单元ID
        :type EdgeUnitID: int
        :param ConfigMapName: ConfigMap名称
        :type ConfigMapName: str
        :param Yaml: Yaml配置
        :type Yaml: str
        :param ConfigMapNamespace: ConfigMap命名空间
        :type ConfigMapNamespace: str
        """
        self.EdgeUnitID = None
        self.ConfigMapName = None
        self.Yaml = None
        self.ConfigMapNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.ConfigMapName = params.get("ConfigMapName")
        self.Yaml = params.get("Yaml")
        self.ConfigMapNamespace = params.get("ConfigMapNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigMapResponse(AbstractModel):
    """ModifyConfigMap返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEdgeNodeLabelsRequest(AbstractModel):
    """ModifyEdgeNodeLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeId: IECP边缘节点ID
        :type NodeId: int
        :param Labels: 标签列表
        :type Labels: list of KeyValueObj
        """
        self.EdgeUnitId = None
        self.NodeId = None
        self.Labels = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeId = params.get("NodeId")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = KeyValueObj()
                obj._deserialize(item)
                self.Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeNodeLabelsResponse(AbstractModel):
    """ModifyEdgeNodeLabels返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEdgeUnitApplicationBasicInfoRequest(AbstractModel):
    """ModifyEdgeUnitApplicationBasicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param BasicInfo: 应用基本信息
        :type BasicInfo: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicInfo`
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self.BasicInfo = None
        self.EdgeUnitId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        if params.get("BasicInfo") is not None:
            self.BasicInfo = ApplicationBasicInfo()
            self.BasicInfo._deserialize(params.get("BasicInfo"))
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitApplicationBasicInfoResponse(AbstractModel):
    """ModifyEdgeUnitApplicationBasicInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEdgeUnitApplicationVisualizationRequest(AbstractModel):
    """ModifyEdgeUnitApplicationVisualization请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        :param BasicConfig: 应用配置
        :type BasicConfig: :class:`tencentcloud.iecp.v20210914.models.ApplicationBasicConfig`
        :param Volumes: 卷配置
        :type Volumes: list of Volume
        :param InitContainers: 初始容器列表
        :type InitContainers: list of Container
        :param Containers: 容器配置
        :type Containers: list of Container
        :param Service: 服务配置
        :type Service: :class:`tencentcloud.iecp.v20210914.models.Service`
        :param Job: Job配置
        :type Job: :class:`tencentcloud.iecp.v20210914.models.Job`
        :param CronJob: CronJob配置
        :type CronJob: :class:`tencentcloud.iecp.v20210914.models.CronJob`
        :param RestartPolicy: 重启策略
        :type RestartPolicy: str
        :param ImagePullSecrets: 镜像拉取密钥
        :type ImagePullSecrets: list of str
        :param HorizontalPodAutoscaler: HPA配置
        :type HorizontalPodAutoscaler: :class:`tencentcloud.iecp.v20210914.models.HorizontalPodAutoscaler`
        """
        self.EdgeUnitId = None
        self.ApplicationId = None
        self.BasicConfig = None
        self.Volumes = None
        self.InitContainers = None
        self.Containers = None
        self.Service = None
        self.Job = None
        self.CronJob = None
        self.RestartPolicy = None
        self.ImagePullSecrets = None
        self.HorizontalPodAutoscaler = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        if params.get("BasicConfig") is not None:
            self.BasicConfig = ApplicationBasicConfig()
            self.BasicConfig._deserialize(params.get("BasicConfig"))
        if params.get("Volumes") is not None:
            self.Volumes = []
            for item in params.get("Volumes"):
                obj = Volume()
                obj._deserialize(item)
                self.Volumes.append(obj)
        if params.get("InitContainers") is not None:
            self.InitContainers = []
            for item in params.get("InitContainers"):
                obj = Container()
                obj._deserialize(item)
                self.InitContainers.append(obj)
        if params.get("Containers") is not None:
            self.Containers = []
            for item in params.get("Containers"):
                obj = Container()
                obj._deserialize(item)
                self.Containers.append(obj)
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        if params.get("Job") is not None:
            self.Job = Job()
            self.Job._deserialize(params.get("Job"))
        if params.get("CronJob") is not None:
            self.CronJob = CronJob()
            self.CronJob._deserialize(params.get("CronJob"))
        self.RestartPolicy = params.get("RestartPolicy")
        self.ImagePullSecrets = params.get("ImagePullSecrets")
        if params.get("HorizontalPodAutoscaler") is not None:
            self.HorizontalPodAutoscaler = HorizontalPodAutoscaler()
            self.HorizontalPodAutoscaler._deserialize(params.get("HorizontalPodAutoscaler"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitApplicationVisualizationResponse(AbstractModel):
    """ModifyEdgeUnitApplicationVisualization返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEdgeUnitApplicationYamlRequest(AbstractModel):
    """ModifyEdgeUnitApplicationYaml请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        :param Yaml: Yaml配置
        :type Yaml: str
        """
        self.EdgeUnitId = None
        self.ApplicationId = None
        self.Yaml = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitApplicationYamlResponse(AbstractModel):
    """ModifyEdgeUnitApplicationYaml返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEdgeUnitDeployGridItemRequest(AbstractModel):
    """ModifyEdgeUnitDeployGridItem请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param GridItemName: Grid名称
        :type GridItemName: str
        :param WorkloadKind: 负载类型（StatefulSetGrid｜DeploymentGrid）
        :type WorkloadKind: str
        :param Replicas: 副本数
        :type Replicas: int
        :param Namespace: 命名空间，默认default
        :type Namespace: str
        """
        self.EdgeUnitId = None
        self.GridItemName = None
        self.WorkloadKind = None
        self.Replicas = None
        self.Namespace = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.GridItemName = params.get("GridItemName")
        self.WorkloadKind = params.get("WorkloadKind")
        self.Replicas = params.get("Replicas")
        self.Namespace = params.get("Namespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitDeployGridItemResponse(AbstractModel):
    """ModifyEdgeUnitDeployGridItem返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyEdgeUnitRequest(AbstractModel):
    """ModifyEdgeUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 边缘集群ID
        :type EdgeUnitId: int
        :param Name: 边缘集群名称，64字符以内
        :type Name: str
        :param Description: 集群描述，200字符以内
        :type Description: str
        """
        self.EdgeUnitId = None
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeUnitResponse(AbstractModel):
    """ModifyEdgeUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNodeUnitTemplateRequest(AbstractModel):
    """ModifyNodeUnitTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: IECP边缘单元ID
        :type EdgeUnitId: int
        :param NodeUnitTemplateID: NodeUnit模版ID
        :type NodeUnitTemplateID: int
        :param Nodes: 包含的节点列表
        :type Nodes: list of str
        """
        self.EdgeUnitId = None
        self.NodeUnitTemplateID = None
        self.Nodes = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.NodeUnitTemplateID = params.get("NodeUnitTemplateID")
        self.Nodes = params.get("Nodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNodeUnitTemplateResponse(AbstractModel):
    """ModifyNodeUnitTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecretRequest(AbstractModel):
    """ModifySecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitID: 边缘单元ID
        :type EdgeUnitID: int
        :param SecretName: Secret名
        :type SecretName: str
        :param Yaml: Secret的Yaml格式
        :type Yaml: str
        :param SecretNamespace: Secret命名空间（默认:default）
        :type SecretNamespace: str
        """
        self.EdgeUnitID = None
        self.SecretName = None
        self.Yaml = None
        self.SecretNamespace = None


    def _deserialize(self, params):
        self.EdgeUnitID = params.get("EdgeUnitID")
        self.SecretName = params.get("SecretName")
        self.Yaml = params.get("Yaml")
        self.SecretNamespace = params.get("SecretNamespace")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecretResponse(AbstractModel):
    """ModifySecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MonitorMetricsColumn(AbstractModel):
    """监控数据列

    """

    def __init__(self):
        r"""
        :param ColumnName: 数据名称
        :type ColumnName: str
        :param ColumnData: 数据内容
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnData: list of str
        :param ColumnBelong: 数据所属，查询Workload类型时有值
        :type ColumnBelong: str
        :param MaxValue: 最大值
        :type MaxValue: float
        :param MinValue: 最小值
        :type MinValue: float
        :param AvgValue: 平均值
        :type AvgValue: float
        :param ColumnTime: 时间戳数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ColumnTime: int
        """
        self.ColumnName = None
        self.ColumnData = None
        self.ColumnBelong = None
        self.MaxValue = None
        self.MinValue = None
        self.AvgValue = None
        self.ColumnTime = None


    def _deserialize(self, params):
        self.ColumnName = params.get("ColumnName")
        self.ColumnData = params.get("ColumnData")
        self.ColumnBelong = params.get("ColumnBelong")
        self.MaxValue = params.get("MaxValue")
        self.MinValue = params.get("MinValue")
        self.AvgValue = params.get("AvgValue")
        self.ColumnTime = params.get("ColumnTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceInfo(AbstractModel):
    """命名空间信息

    """

    def __init__(self):
        r"""
        :param Namespace: 命名空间名
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param Status: 状态(Active|Terminating)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param Protected: 是否保护(不允许删除)
注意：此字段可能返回 null，表示取不到有效值。
        :type Protected: bool
        :param Yaml: 对应的Yaml配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Yaml: str
        """
        self.Namespace = None
        self.Status = None
        self.Description = None
        self.CreateTime = None
        self.Protected = None
        self.Yaml = None


    def _deserialize(self, params):
        self.Namespace = params.get("Namespace")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Protected = params.get("Protected")
        self.Yaml = params.get("Yaml")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NamespaceResource(AbstractModel):
    """命名空间下资源描述

    """

    def __init__(self):
        r"""
        :param Type: 类型(workload|grid|configmap|secret)
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Count: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param Names: 名称(最多返回5个）
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        """
        self.Type = None
        self.Count = None
        self.Names = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Count = params.get("Count")
        self.Names = params.get("Names")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeGroupInfo(AbstractModel):
    """NodeGroup信息

    """

    def __init__(self):
        r"""
        :param Description: 描述
        :type Description: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param NodeGroupName: NodeGroup名称
        :type NodeGroupName: str
        :param DeploymentGridList: DeploymentGrid数组
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentGridList: list of GridDetail
        :param StatefulSetGridList: StatefulSetGrid数组
注意：此字段可能返回 null，表示取不到有效值。
        :type StatefulSetGridList: list of GridDetail
        :param Protect: 是否平台保护
注意：此字段可能返回 null，表示取不到有效值。
        :type Protect: bool
        """
        self.Description = None
        self.CreateTime = None
        self.NodeGroupName = None
        self.DeploymentGridList = None
        self.StatefulSetGridList = None
        self.Protect = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.NodeGroupName = params.get("NodeGroupName")
        if params.get("DeploymentGridList") is not None:
            self.DeploymentGridList = []
            for item in params.get("DeploymentGridList"):
                obj = GridDetail()
                obj._deserialize(item)
                self.DeploymentGridList.append(obj)
        if params.get("StatefulSetGridList") is not None:
            self.StatefulSetGridList = []
            for item in params.get("StatefulSetGridList"):
                obj = GridDetail()
                obj._deserialize(item)
                self.StatefulSetGridList.append(obj)
        self.Protect = params.get("Protect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeGroupNodeUnitTemplateInfo(AbstractModel):
    """指定NodeGroup中查询NodeUnit模版

    """

    def __init__(self):
        r"""
        :param ID: 模版ID
        :type ID: int
        :param Name: 名称
        :type Name: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 描述
        :type Description: str
        :param NodeList: 包含节点列表
        :type NodeList: list of NodeSimpleInfo
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param Relation: 是否关联
        :type Relation: bool
        """
        self.ID = None
        self.Name = None
        self.Namespace = None
        self.Description = None
        self.NodeList = None
        self.UpdateTime = None
        self.CreateTime = None
        self.Relation = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = NodeSimpleInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeSimpleInfo(AbstractModel):
    """节点基础信息

    """

    def __init__(self):
        r"""
        :param ID: 节点ID
        :type ID: int
        :param NodeName: 节点名称
        :type NodeName: str
        """
        self.ID = None
        self.NodeName = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeUnitInfo(AbstractModel):
    """NodeUnit信息

    """

    def __init__(self):
        r"""
        :param Id: NodeUnitId
        :type Id: int
        :param NodeUnitName: NodeUnit名称
        :type NodeUnitName: str
        :param NodeList: 包含节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeUnitNodeInfo
        """
        self.Id = None
        self.NodeUnitName = None
        self.NodeList = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.NodeUnitName = params.get("NodeUnitName")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = NodeUnitNodeInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeUnitNodeInfo(AbstractModel):
    """NodeUnit中边缘节点信息

    """

    def __init__(self):
        r"""
        :param Id: 节点ID
        :type Id: int
        :param Status: 节点状态  NodeStatusHealthy (健康)/NodeStatusAbnormal (异常)/NodeStatusOffline (下线)/NodeStatusNotActivated (未激活
        :type Status: str
        :param NodeName: 节点名称
        :type NodeName: str
        :param InternalIP: 内网节点IP
        :type InternalIP: str
        """
        self.Id = None
        self.Status = None
        self.NodeName = None
        self.InternalIP = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Status = params.get("Status")
        self.NodeName = params.get("NodeName")
        self.InternalIP = params.get("InternalIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeUnitTemplate(AbstractModel):
    """NodeUnit模版信息

    """

    def __init__(self):
        r"""
        :param ID: NodeUnit模版ID
        :type ID: int
        :param Name: NodeUnit模版名称
        :type Name: str
        :param Namespace: 命名空间
        :type Namespace: str
        :param Description: 描述
        :type Description: str
        :param NodeList: 包含节点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeList: list of NodeSimpleInfo
        :param NodeGroups: NodeGroup列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeGroups: list of str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ID = None
        self.Name = None
        self.Namespace = None
        self.Description = None
        self.NodeList = None
        self.NodeGroups = None
        self.UpdateTime = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ID = params.get("ID")
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.Description = params.get("Description")
        if params.get("NodeList") is not None:
            self.NodeList = []
            for item in params.get("NodeList"):
                obj = NodeSimpleInfo()
                obj._deserialize(item)
                self.NodeList.append(obj)
        self.NodeGroups = params.get("NodeGroups")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationLog(AbstractModel):
    """操作日志

    """

    def __init__(self):
        r"""
        :param OperateTime: 操作时间
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateTime: str
        :param Module: 模块名
注意：此字段可能返回 null，表示取不到有效值。
        :type Module: str
        :param Description: 操作信息
        :type Description: str
        :param UserId: 用户ID
        :type UserId: str
        :param Status: 状态: 1:成功 2:失败
        :type Status: int
        :param OperatorUserID: 操作用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorUserID: str
        :param Action: 操作动作
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        """
        self.OperateTime = None
        self.Module = None
        self.Description = None
        self.UserId = None
        self.Status = None
        self.OperatorUserID = None
        self.Action = None


    def _deserialize(self, params):
        self.OperateTime = params.get("OperateTime")
        self.Module = params.get("Module")
        self.Description = params.get("Description")
        self.UserId = params.get("UserId")
        self.Status = params.get("Status")
        self.OperatorUserID = params.get("OperatorUserID")
        self.Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperationLogsCondition(AbstractModel):
    """操作日志状态查询条件

    """

    def __init__(self):
        r"""
        :param Status: 状态列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: list of int
        """
        self.Status = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PodStatus(AbstractModel):
    """Pod状态信息

    """

    def __init__(self):
        r"""
        :param Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param NameSpace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param IP: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IP: str
        :param StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param RunSec: 运行时间
注意：此字段可能返回 null，表示取不到有效值。
        :type RunSec: int
        :param RestartCount: 重启次数
注意：此字段可能返回 null，表示取不到有效值。
        :type RestartCount: int
        """
        self.Name = None
        self.NameSpace = None
        self.Status = None
        self.IP = None
        self.StartTime = None
        self.RunSec = None
        self.RestartCount = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.NameSpace = params.get("NameSpace")
        self.Status = params.get("Status")
        self.IP = params.get("IP")
        self.StartTime = params.get("StartTime")
        self.RunSec = params.get("RunSec")
        self.RestartCount = params.get("RestartCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortConfig(AbstractModel):
    """端口配置

    """

    def __init__(self):
        r"""
        :param Protocol: 协议类型(tcp|udp)
        :type Protocol: str
        :param Port: 源端口
        :type Port: int
        :param TargetPort: 目标端口
        :type TargetPort: int
        :param NodePort: 节点端口
        :type NodePort: int
        """
        self.Protocol = None
        self.Port = None
        self.TargetPort = None
        self.NodePort = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.TargetPort = params.get("TargetPort")
        self.NodePort = params.get("NodePort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Probe(AbstractModel):
    """探针配置

    """

    def __init__(self):
        r"""
        :param InitialDelaySeconds: 启动后，延迟探测时间 单位:秒
注意：此字段可能返回 null，表示取不到有效值。
        :type InitialDelaySeconds: int
        :param PeriodSeconds: 探测间隔，单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodSeconds: int
        :param TimeoutSeconds: 探测超时时间 单位：秒
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeoutSeconds: int
        :param SuccessThreshold: 失败后检查成功的最小连续成功次数。默认为1.活跃度必须为1。最小值为1
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessThreshold: int
        :param FailureThreshold: 当Pod成功启动且检查失败时，放弃之前尝试次数。默认为3.最小值为1
注意：此字段可能返回 null，表示取不到有效值。
        :type FailureThreshold: int
        :param HttpProbe: HTTP探测配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpProbe: :class:`tencentcloud.iecp.v20210914.models.HttpProbe`
        :param TcpProbe: TCP探测配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpProbe: :class:`tencentcloud.iecp.v20210914.models.TcpProbe`
        """
        self.InitialDelaySeconds = None
        self.PeriodSeconds = None
        self.TimeoutSeconds = None
        self.SuccessThreshold = None
        self.FailureThreshold = None
        self.HttpProbe = None
        self.TcpProbe = None


    def _deserialize(self, params):
        self.InitialDelaySeconds = params.get("InitialDelaySeconds")
        self.PeriodSeconds = params.get("PeriodSeconds")
        self.TimeoutSeconds = params.get("TimeoutSeconds")
        self.SuccessThreshold = params.get("SuccessThreshold")
        self.FailureThreshold = params.get("FailureThreshold")
        if params.get("HttpProbe") is not None:
            self.HttpProbe = HttpProbe()
            self.HttpProbe._deserialize(params.get("HttpProbe"))
        if params.get("TcpProbe") is not None:
            self.TcpProbe = TcpProbe()
            self.TcpProbe._deserialize(params.get("TcpProbe"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedeployEdgeUnitApplicationRequest(AbstractModel):
    """RedeployEdgeUnitApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param EdgeUnitId: 单元ID
        :type EdgeUnitId: int
        :param ApplicationId: 应用ID
        :type ApplicationId: int
        """
        self.EdgeUnitId = None
        self.ApplicationId = None


    def _deserialize(self, params):
        self.EdgeUnitId = params.get("EdgeUnitId")
        self.ApplicationId = params.get("ApplicationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedeployEdgeUnitApplicationResponse(AbstractModel):
    """RedeployEdgeUnitApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceMetricTarget(AbstractModel):
    """资源目标指标

    """

    def __init__(self):
        r"""
        :param Type: 类型(cpu|memory)
        :type Type: str
        :param AverageValue: 平均值
        :type AverageValue: int
        :param Scale: 单位
        :type Scale: str
        :param AverageUtilization: 平均值
        :type AverageUtilization: int
        """
        self.Type = None
        self.AverageValue = None
        self.Scale = None
        self.AverageUtilization = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.AverageValue = params.get("AverageValue")
        self.Scale = params.get("Scale")
        self.AverageUtilization = params.get("AverageUtilization")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecretItem(AbstractModel):
    """Secret信息

    """

    def __init__(self):
        r"""
        :param Name: Secret名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param SecretType: Secret类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretType: str
        """
        self.Name = None
        self.Namespace = None
        self.CreateTime = None
        self.SecretType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Namespace = params.get("Namespace")
        self.CreateTime = params.get("CreateTime")
        self.SecretType = params.get("SecretType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityCapabilities(AbstractModel):
    """安全能力

    """

    def __init__(self):
        r"""
        :param Add: 允许操作列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Add: list of str
        :param Drop: 禁止操作列表
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
        


class SecurityContext(AbstractModel):
    """安全上下文

    """

    def __init__(self):
        r"""
        :param Privilege: 是否开启特权模式
        :type Privilege: bool
        :param ProcMount: 目录/Proc挂载方式
        :type ProcMount: str
        :param Capabilities: 安全配置
        :type Capabilities: :class:`tencentcloud.iecp.v20210914.models.SecurityCapabilities`
        """
        self.Privilege = None
        self.ProcMount = None
        self.Capabilities = None


    def _deserialize(self, params):
        self.Privilege = params.get("Privilege")
        self.ProcMount = params.get("ProcMount")
        if params.get("Capabilities") is not None:
            self.Capabilities = SecurityCapabilities()
            self.Capabilities._deserialize(params.get("Capabilities"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """服务配置

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Type: 类型 (ClusterIP|NodePort)
        :type Type: str
        :param Ports: 端口配置
        :type Ports: list of PortConfig
        :param Labels: 标签
        :type Labels: list of Label
        :param Namespace: 命名空间默认default
        :type Namespace: str
        :param ClusterIP: 服务IP
        :type ClusterIP: str
        """
        self.Name = None
        self.Type = None
        self.Ports = None
        self.Labels = None
        self.Namespace = None
        self.ClusterIP = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        if params.get("Ports") is not None:
            self.Ports = []
            for item in params.get("Ports"):
                obj = PortConfig()
                obj._deserialize(item)
                self.Ports.append(obj)
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = Label()
                obj._deserialize(item)
                self.Labels.append(obj)
        self.Namespace = params.get("Namespace")
        self.ClusterIP = params.get("ClusterIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """查询结果排序条件

    """

    def __init__(self):
        r"""
        :param Field: 排序字段
        :type Field: str
        :param Order: 排序方式，升序ASC / 降序DESC
        :type Order: str
        """
        self.Field = None
        self.Order = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TcpProbe(AbstractModel):
    """TCP探测配置

    """

    def __init__(self):
        r"""
        :param Port: 连接端口
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
        


class Volume(AbstractModel):
    """卷

    """

    def __init__(self):
        r"""
        :param Source: 来源(emptyDir|hostPath|configMap|secret|nfs)
        :type Source: str
        :param Name: 名称
        :type Name: str
        :param HostPath: Host挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HostPath: :class:`tencentcloud.iecp.v20210914.models.VolumeHostPath`
        :param ConfigMap: ConfigMap挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigMap: :class:`tencentcloud.iecp.v20210914.models.VolumeConfigMap`
        :param Secret: Secret挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Secret: :class:`tencentcloud.iecp.v20210914.models.VolumeConfigMap`
        :param NFS: NFS挂载配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NFS: :class:`tencentcloud.iecp.v20210914.models.VolumeNFS`
        """
        self.Source = None
        self.Name = None
        self.HostPath = None
        self.ConfigMap = None
        self.Secret = None
        self.NFS = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Name = params.get("Name")
        if params.get("HostPath") is not None:
            self.HostPath = VolumeHostPath()
            self.HostPath._deserialize(params.get("HostPath"))
        if params.get("ConfigMap") is not None:
            self.ConfigMap = VolumeConfigMap()
            self.ConfigMap._deserialize(params.get("ConfigMap"))
        if params.get("Secret") is not None:
            self.Secret = VolumeConfigMap()
            self.Secret._deserialize(params.get("Secret"))
        if params.get("NFS") is not None:
            self.NFS = VolumeNFS()
            self.NFS._deserialize(params.get("NFS"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeConfigMap(AbstractModel):
    """ConfigMap挂载卷

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param Items: Key列表配置
        :type Items: list of VolumeConfigMapKeyToPath
        """
        self.Name = None
        self.Items = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = VolumeConfigMapKeyToPath()
                obj._deserialize(item)
                self.Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeConfigMapKeyToPath(AbstractModel):
    """ConfigMap的key挂载到路径

    """

    def __init__(self):
        r"""
        :param Key: 健名
        :type Key: str
        :param Path: 对应本地路径
        :type Path: str
        :param Mode: 对应权限模式
        :type Mode: str
        """
        self.Key = None
        self.Path = None
        self.Mode = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Path = params.get("Path")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeHostPath(AbstractModel):
    """数据卷主机路径，取值参考: https://kubernetes.io/docs/concepts/storage/volumes#hostpath

    """

    def __init__(self):
        r"""
        :param Type: 类型
        :type Type: str
        :param Path: 路径
        :type Path: str
        """
        self.Type = None
        self.Path = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeMount(AbstractModel):
    """数据挂载

    """

    def __init__(self):
        r"""
        :param Name: 名称
        :type Name: str
        :param MountPath: 挂载路径
        :type MountPath: str
        :param SubPath: 子路径
注意：此字段可能返回 null，表示取不到有效值。
        :type SubPath: str
        :param ReadOnly: 是否只读
注意：此字段可能返回 null，表示取不到有效值。
        :type ReadOnly: bool
        """
        self.Name = None
        self.MountPath = None
        self.SubPath = None
        self.ReadOnly = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.MountPath = params.get("MountPath")
        self.SubPath = params.get("SubPath")
        self.ReadOnly = params.get("ReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VolumeNFS(AbstractModel):
    """NFS挂载卷

    """

    def __init__(self):
        r"""
        :param Server: 服务地址
        :type Server: str
        :param ServerPath: 对应服务器路径
        :type ServerPath: str
        :param Path: 对应本地路径
        :type Path: str
        """
        self.Server = None
        self.ServerPath = None
        self.Path = None


    def _deserialize(self, params):
        self.Server = params.get("Server")
        self.ServerPath = params.get("ServerPath")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        