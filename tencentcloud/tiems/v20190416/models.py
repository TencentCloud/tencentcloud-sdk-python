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


class Conditions(AbstractModel):
    """状态

    """

    def __init__(self):
        r"""
        :param _Reason: 原因
        :type Reason: str
        :param _Count: 具有相同原因的副本个数
        :type Count: int
        """
        self._Reason = None
        self._Count = None

    @property
    def Reason(self):
        """原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def Count(self):
        """具有相同原因的副本个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._Reason = params.get("Reason")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Config(AbstractModel):
    """配置

    """

    def __init__(self):
        r"""
        :param _Id: Id
        :type Id: str
        :param _Name: 配置名
        :type Name: str
        :param _ModelUri: 模型地址
        :type ModelUri: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Runtime: 运行环境
        :type Runtime: str
        :param _Version: 配置版本
        :type Version: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Description: 配置描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Id = None
        self._Name = None
        self._ModelUri = None
        self._CreateTime = None
        self._Runtime = None
        self._Version = None
        self._UpdateTime = None
        self._Description = None

    @property
    def Id(self):
        """Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """配置名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ModelUri(self):
        """模型地址
        :rtype: str
        """
        return self._ModelUri

    @ModelUri.setter
    def ModelUri(self, ModelUri):
        self._ModelUri = ModelUri

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Runtime(self):
        """运行环境
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Version(self):
        """配置版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Description(self):
        """配置描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._ModelUri = params.get("ModelUri")
        self._CreateTime = params.get("CreateTime")
        self._Runtime = params.get("Runtime")
        self._Version = params.get("Version")
        self._UpdateTime = params.get("UpdateTime")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobRequest(AbstractModel):
    """CreateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 任务名称
        :type Name: str
        :param _ResourceGroupId: 使用的资源组 Id，默认使用共享资源组
        :type ResourceGroupId: str
        :param _Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
        :type Cpu: int
        :param _Memory: 内存配置, 单位为1M；范围[100, 256000]
        :type Memory: int
        :param _Cluster: 运行集群
        :type Cluster: str
        :param _PredictInput: 预测输入
        :type PredictInput: :class:`tencentcloud.tiems.v20190416.models.PredictInput`
        :param _Description: 任务描述
        :type Description: str
        :param _WorkerCount: 同时处理任务的 Worker 个数
        :type WorkerCount: int
        :param _ConfigId: 使用的配置 Id
        :type ConfigId: str
        :param _Gpu: GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
        :type Gpu: int
        :param _GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
        :type GpuMemory: int
        :param _GpuType: GPU类型
        :type GpuType: str
        :param _QuantizationInput: 量化输入
        :type QuantizationInput: :class:`tencentcloud.tiems.v20190416.models.QuantizationInput`
        :param _LogTopicId: Cls日志主题ID
        :type LogTopicId: str
        """
        self._Name = None
        self._ResourceGroupId = None
        self._Cpu = None
        self._Memory = None
        self._Cluster = None
        self._PredictInput = None
        self._Description = None
        self._WorkerCount = None
        self._ConfigId = None
        self._Gpu = None
        self._GpuMemory = None
        self._GpuType = None
        self._QuantizationInput = None
        self._LogTopicId = None

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ResourceGroupId(self):
        """使用的资源组 Id，默认使用共享资源组
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Cpu(self):
        """处理器配置, 单位为1/1000核；范围[100, 256000]
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存配置, 单位为1M；范围[100, 256000]
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Cluster(self):
        """运行集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def PredictInput(self):
        """预测输入
        :rtype: :class:`tencentcloud.tiems.v20190416.models.PredictInput`
        """
        return self._PredictInput

    @PredictInput.setter
    def PredictInput(self, PredictInput):
        self._PredictInput = PredictInput

    @property
    def Description(self):
        """任务描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkerCount(self):
        """同时处理任务的 Worker 个数
        :rtype: int
        """
        return self._WorkerCount

    @WorkerCount.setter
    def WorkerCount(self, WorkerCount):
        self._WorkerCount = WorkerCount

    @property
    def ConfigId(self):
        """使用的配置 Id
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def Gpu(self):
        """GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuMemory(self):
        """显存配置, 单位为1M，范围 [0, 256000]
        :rtype: int
        """
        return self._GpuMemory

    @GpuMemory.setter
    def GpuMemory(self, GpuMemory):
        self._GpuMemory = GpuMemory

    @property
    def GpuType(self):
        """GPU类型
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def QuantizationInput(self):
        """量化输入
        :rtype: :class:`tencentcloud.tiems.v20190416.models.QuantizationInput`
        """
        return self._QuantizationInput

    @QuantizationInput.setter
    def QuantizationInput(self, QuantizationInput):
        self._QuantizationInput = QuantizationInput

    @property
    def LogTopicId(self):
        """Cls日志主题ID
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Cluster = params.get("Cluster")
        if params.get("PredictInput") is not None:
            self._PredictInput = PredictInput()
            self._PredictInput._deserialize(params.get("PredictInput"))
        self._Description = params.get("Description")
        self._WorkerCount = params.get("WorkerCount")
        self._ConfigId = params.get("ConfigId")
        self._Gpu = params.get("Gpu")
        self._GpuMemory = params.get("GpuMemory")
        self._GpuType = params.get("GpuType")
        if params.get("QuantizationInput") is not None:
            self._QuantizationInput = QuantizationInput()
            self._QuantizationInput._deserialize(params.get("QuantizationInput"))
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJobResponse(AbstractModel):
    """CreateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 任务
        :type Job: :class:`tencentcloud.tiems.v20190416.models.Job`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        """任务
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Job`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class CreateRsgAsGroupRequest(AbstractModel):
    """CreateRsgAsGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RsgId: 资源组 ID
        :type RsgId: str
        :param _MaxSize: 伸缩组允许的最大节点数
        :type MaxSize: int
        :param _MinSize: 伸缩组允许的最小节点数
        :type MinSize: int
        :param _InstanceType: 伸缩组的节点规格
        :type InstanceType: str
        :param _Cluster: 资源组所在的集群名
        :type Cluster: str
        :param _Name: 伸缩组名称
        :type Name: str
        :param _DesiredSize: 伸缩组期望的节点数
        :type DesiredSize: int
        """
        self._RsgId = None
        self._MaxSize = None
        self._MinSize = None
        self._InstanceType = None
        self._Cluster = None
        self._Name = None
        self._DesiredSize = None

    @property
    def RsgId(self):
        """资源组 ID
        :rtype: str
        """
        return self._RsgId

    @RsgId.setter
    def RsgId(self, RsgId):
        self._RsgId = RsgId

    @property
    def MaxSize(self):
        """伸缩组允许的最大节点数
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """伸缩组允许的最小节点数
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def InstanceType(self):
        """伸缩组的节点规格
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Cluster(self):
        """资源组所在的集群名
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Name(self):
        """伸缩组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DesiredSize(self):
        """伸缩组期望的节点数
        :rtype: int
        """
        return self._DesiredSize

    @DesiredSize.setter
    def DesiredSize(self, DesiredSize):
        self._DesiredSize = DesiredSize


    def _deserialize(self, params):
        self._RsgId = params.get("RsgId")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._InstanceType = params.get("InstanceType")
        self._Cluster = params.get("Cluster")
        self._Name = params.get("Name")
        self._DesiredSize = params.get("DesiredSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRsgAsGroupResponse(AbstractModel):
    """CreateRsgAsGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RsgAsGroup: 所创建的资源组的伸缩组
        :type RsgAsGroup: :class:`tencentcloud.tiems.v20190416.models.RsgAsGroup`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RsgAsGroup = None
        self._RequestId = None

    @property
    def RsgAsGroup(self):
        """所创建的资源组的伸缩组
        :rtype: :class:`tencentcloud.tiems.v20190416.models.RsgAsGroup`
        """
        return self._RsgAsGroup

    @RsgAsGroup.setter
    def RsgAsGroup(self, RsgAsGroup):
        self._RsgAsGroup = RsgAsGroup

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RsgAsGroup") is not None:
            self._RsgAsGroup = RsgAsGroup()
            self._RsgAsGroup._deserialize(params.get("RsgAsGroup"))
        self._RequestId = params.get("RequestId")


class CreateRuntimeRequest(AbstractModel):
    """CreateRuntime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 全局唯一的运行环境名称
        :type Name: str
        :param _Image: 运行环境镜像地址
        :type Image: str
        :param _Framework: 运行环境框架
        :type Framework: str
        :param _Description: 运行环境描述
        :type Description: str
        :param _HealthCheckOn: 是否支持健康检查，默认为False
        :type HealthCheckOn: bool
        """
        self._Name = None
        self._Image = None
        self._Framework = None
        self._Description = None
        self._HealthCheckOn = None

    @property
    def Name(self):
        """全局唯一的运行环境名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Image(self):
        """运行环境镜像地址
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Framework(self):
        """运行环境框架
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def Description(self):
        """运行环境描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def HealthCheckOn(self):
        """是否支持健康检查，默认为False
        :rtype: bool
        """
        return self._HealthCheckOn

    @HealthCheckOn.setter
    def HealthCheckOn(self, HealthCheckOn):
        self._HealthCheckOn = HealthCheckOn


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Image = params.get("Image")
        self._Framework = params.get("Framework")
        self._Description = params.get("Description")
        self._HealthCheckOn = params.get("HealthCheckOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuntimeResponse(AbstractModel):
    """CreateRuntime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Runtime: 运行环境
        :type Runtime: :class:`tencentcloud.tiems.v20190416.models.Runtime`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Runtime = None
        self._RequestId = None

    @property
    def Runtime(self):
        """运行环境
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Runtime`
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Runtime") is not None:
            self._Runtime = Runtime()
            self._Runtime._deserialize(params.get("Runtime"))
        self._RequestId = params.get("RequestId")


class CreateServiceConfigRequest(AbstractModel):
    """CreateServiceConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 配置名称
        :type Name: str
        :param _Runtime: 运行环境
        :type Runtime: str
        :param _ModelUri: 模型地址，支持cos路径，格式为 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夹路径。为模型文件的上一层文件夹地址。
        :type ModelUri: str
        :param _Description: 配置描述
        :type Description: str
        """
        self._Name = None
        self._Runtime = None
        self._ModelUri = None
        self._Description = None

    @property
    def Name(self):
        """配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Runtime(self):
        """运行环境
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def ModelUri(self):
        """模型地址，支持cos路径，格式为 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夹路径。为模型文件的上一层文件夹地址。
        :rtype: str
        """
        return self._ModelUri

    @ModelUri.setter
    def ModelUri(self, ModelUri):
        self._ModelUri = ModelUri

    @property
    def Description(self):
        """配置描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Runtime = params.get("Runtime")
        self._ModelUri = params.get("ModelUri")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceConfigResponse(AbstractModel):
    """CreateServiceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceConfig: 服务配置
        :type ServiceConfig: :class:`tencentcloud.tiems.v20190416.models.Config`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceConfig = None
        self._RequestId = None

    @property
    def ServiceConfig(self):
        """服务配置
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Config`
        """
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = Config()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        self._RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Scaler: 扩缩容配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param _ServiceConfigId: 服务配置Id
        :type ServiceConfigId: str
        :param _Name: 服务名称
        :type Name: str
        :param _ScaleMode: 扩缩容方式，支持AUTO, MANUAL，分别表示自动扩缩容和手动扩缩容
        :type ScaleMode: str
        :param _ResourceGroupId: 部署要使用的资源组Id，默认为共享资源组
        :type ResourceGroupId: str
        :param _Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
        :type Cpu: int
        :param _Memory: 内存配置, 单位为1M；范围[100, 256000]
        :type Memory: int
        :param _Cluster: 集群，不填则使用默认集群
        :type Cluster: str
        :param _Authentication: 默认为空，表示不需要鉴权，TOKEN 表示选择 Token 鉴权方式
        :type Authentication: str
        :param _Gpu: GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
        :type Gpu: int
        :param _GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
        :type GpuMemory: int
        :param _Description: 备注
        :type Description: str
        :param _GpuType: GPU类型
        :type GpuType: str
        :param _LogTopicId: Cls日志主题ID
        :type LogTopicId: str
        """
        self._Scaler = None
        self._ServiceConfigId = None
        self._Name = None
        self._ScaleMode = None
        self._ResourceGroupId = None
        self._Cpu = None
        self._Memory = None
        self._Cluster = None
        self._Authentication = None
        self._Gpu = None
        self._GpuMemory = None
        self._Description = None
        self._GpuType = None
        self._LogTopicId = None

    @property
    def Scaler(self):
        """扩缩容配置
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        """
        return self._Scaler

    @Scaler.setter
    def Scaler(self, Scaler):
        self._Scaler = Scaler

    @property
    def ServiceConfigId(self):
        """服务配置Id
        :rtype: str
        """
        return self._ServiceConfigId

    @ServiceConfigId.setter
    def ServiceConfigId(self, ServiceConfigId):
        self._ServiceConfigId = ServiceConfigId

    @property
    def Name(self):
        """服务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ScaleMode(self):
        """扩缩容方式，支持AUTO, MANUAL，分别表示自动扩缩容和手动扩缩容
        :rtype: str
        """
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def ResourceGroupId(self):
        """部署要使用的资源组Id，默认为共享资源组
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Cpu(self):
        """处理器配置, 单位为1/1000核；范围[100, 256000]
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存配置, 单位为1M；范围[100, 256000]
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Cluster(self):
        """集群，不填则使用默认集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Authentication(self):
        """默认为空，表示不需要鉴权，TOKEN 表示选择 Token 鉴权方式
        :rtype: str
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Gpu(self):
        """GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuMemory(self):
        """显存配置, 单位为1M，范围 [0, 256000]
        :rtype: int
        """
        return self._GpuMemory

    @GpuMemory.setter
    def GpuMemory(self, GpuMemory):
        self._GpuMemory = GpuMemory

    @property
    def Description(self):
        """备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GpuType(self):
        """GPU类型
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def LogTopicId(self):
        """Cls日志主题ID
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        if params.get("Scaler") is not None:
            self._Scaler = Scaler()
            self._Scaler._deserialize(params.get("Scaler"))
        self._ServiceConfigId = params.get("ServiceConfigId")
        self._Name = params.get("Name")
        self._ScaleMode = params.get("ScaleMode")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Cluster = params.get("Cluster")
        self._Authentication = params.get("Authentication")
        self._Gpu = params.get("Gpu")
        self._GpuMemory = params.get("GpuMemory")
        self._Description = params.get("Description")
        self._GpuType = params.get("GpuType")
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceResponse(AbstractModel):
    """CreateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 服务
        :type Service: :class:`tencentcloud.tiems.v20190416.models.ModelService`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Service = None
        self._RequestId = None

    @property
    def Service(self):
        """服务
        :rtype: :class:`tencentcloud.tiems.v20190416.models.ModelService`
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = ModelService()
            self._Service._deserialize(params.get("Service"))
        self._RequestId = params.get("RequestId")


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 要删除的节点 ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """要删除的节点 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteJobRequest(AbstractModel):
    """DeleteJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 Id
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        """任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteJobResponse(AbstractModel):
    """DeleteJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteResourceGroupRequest(AbstractModel):
    """DeleteResourceGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceGroupId: 要删除的资源组 ID
        :type ResourceGroupId: str
        """
        self._ResourceGroupId = None

    @property
    def ResourceGroupId(self):
        """要删除的资源组 ID
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId


    def _deserialize(self, params):
        self._ResourceGroupId = params.get("ResourceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceGroupResponse(AbstractModel):
    """DeleteResourceGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRsgAsGroupRequest(AbstractModel):
    """DeleteRsgAsGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组 ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """伸缩组 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRsgAsGroupResponse(AbstractModel):
    """DeleteRsgAsGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRuntimeRequest(AbstractModel):
    """DeleteRuntime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Runtime: 要删除的Runtime名
        :type Runtime: str
        """
        self._Runtime = None

    @property
    def Runtime(self):
        """要删除的Runtime名
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime


    def _deserialize(self, params):
        self._Runtime = params.get("Runtime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuntimeResponse(AbstractModel):
    """DeleteRuntime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteServiceConfigRequest(AbstractModel):
    """DeleteServiceConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceConfigId: 服务配置Id
        :type ServiceConfigId: str
        :param _ServiceConfigName: 服务配置名称
        :type ServiceConfigName: str
        """
        self._ServiceConfigId = None
        self._ServiceConfigName = None

    @property
    def ServiceConfigId(self):
        """服务配置Id
        :rtype: str
        """
        return self._ServiceConfigId

    @ServiceConfigId.setter
    def ServiceConfigId(self, ServiceConfigId):
        self._ServiceConfigId = ServiceConfigId

    @property
    def ServiceConfigName(self):
        """服务配置名称
        :rtype: str
        """
        return self._ServiceConfigName

    @ServiceConfigName.setter
    def ServiceConfigName(self, ServiceConfigName):
        self._ServiceConfigName = ServiceConfigName


    def _deserialize(self, params):
        self._ServiceConfigId = params.get("ServiceConfigId")
        self._ServiceConfigName = params.get("ServiceConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceConfigResponse(AbstractModel):
    """DeleteServiceConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务Id
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        """服务Id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选选项
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为200
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        :param _ResourceGroupId: 要查询的资源组 ID
        :type ResourceGroupId: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._ResourceGroupId = None

    @property
    def Filters(self):
        """筛选选项
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def ResourceGroupId(self):
        """要查询的资源组 ID
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        self._ResourceGroupId = params.get("ResourceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源组下节点总数
        :type TotalCount: int
        :param _Instances: 资源组下节点列表
        :type Instances: list of Instance
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Instances = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """资源组下节点总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Instances(self):
        """资源组下节点列表
        :rtype: list of Instance
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = Instance()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceGroupsRequest(AbstractModel):
    """DescribeResourceGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选选项
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为200
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        """筛选选项
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceGroupsResponse(AbstractModel):
    """DescribeResourceGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 资源组总数
        :type TotalCount: int
        :param _ResourceGroups: 资源组列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroups: list of ResourceGroup
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """资源组总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceGroups(self):
        """资源组列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ResourceGroup
        """
        return self._ResourceGroups

    @ResourceGroups.setter
    def ResourceGroups(self, ResourceGroups):
        self._ResourceGroups = ResourceGroups

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ResourceGroups") is not None:
            self._ResourceGroups = []
            for item in params.get("ResourceGroups"):
                obj = ResourceGroup()
                obj._deserialize(item)
                self._ResourceGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRsgAsGroupActivitiesRequest(AbstractModel):
    """DescribeRsgAsGroupActivities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组 ID
        :type Id: str
        :param _StartTime: 查询活动的开始时间
        :type StartTime: str
        :param _EndTime: 查询互动的结束时间
        :type EndTime: str
        :param _Filters: 筛选选项
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 200
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围："ASC", "DESC"
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self._Id = None
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Id(self):
        """伸缩组 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def StartTime(self):
        """查询活动的开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询互动的结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        """筛选选项
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为 20，最大值为 200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """输出列表的排列顺序。取值范围："ASC", "DESC"
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRsgAsGroupActivitiesResponse(AbstractModel):
    """DescribeRsgAsGroupActivities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RsgAsGroupActivitySet: 伸缩组活动数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RsgAsGroupActivitySet: list of RsgAsGroupActivity
        :param _TotalCount: 所查询的伸缩组活动总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RsgAsGroupActivitySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RsgAsGroupActivitySet(self):
        """伸缩组活动数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RsgAsGroupActivity
        """
        return self._RsgAsGroupActivitySet

    @RsgAsGroupActivitySet.setter
    def RsgAsGroupActivitySet(self, RsgAsGroupActivitySet):
        self._RsgAsGroupActivitySet = RsgAsGroupActivitySet

    @property
    def TotalCount(self):
        """所查询的伸缩组活动总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RsgAsGroupActivitySet") is not None:
            self._RsgAsGroupActivitySet = []
            for item in params.get("RsgAsGroupActivitySet"):
                obj = RsgAsGroupActivity()
                obj._deserialize(item)
                self._RsgAsGroupActivitySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRsgAsGroupsRequest(AbstractModel):
    """DescribeRsgAsGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选选项
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 200
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围："ASC", "DESC"
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        """筛选选项
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为 20，最大值为 200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """输出列表的排列顺序。取值范围："ASC", "DESC"
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRsgAsGroupsResponse(AbstractModel):
    """DescribeRsgAsGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RsgAsGroupSet: 所查询的伸缩组数组
        :type RsgAsGroupSet: list of RsgAsGroup
        :param _TotalCount: 伸缩组数组总数目
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RsgAsGroupSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RsgAsGroupSet(self):
        """所查询的伸缩组数组
        :rtype: list of RsgAsGroup
        """
        return self._RsgAsGroupSet

    @RsgAsGroupSet.setter
    def RsgAsGroupSet(self, RsgAsGroupSet):
        self._RsgAsGroupSet = RsgAsGroupSet

    @property
    def TotalCount(self):
        """伸缩组数组总数目
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RsgAsGroupSet") is not None:
            self._RsgAsGroupSet = []
            for item in params.get("RsgAsGroupSet"):
                obj = RsgAsGroup()
                obj._deserialize(item)
                self._RsgAsGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRuntimesRequest(AbstractModel):
    """DescribeRuntimes请求参数结构体

    """


class DescribeRuntimesResponse(AbstractModel):
    """DescribeRuntimes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Runtimes: TIEMS支持的运行环境列表
        :type Runtimes: list of Runtime
        :param _UserAccess: 用户对runtime对权限
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAccess: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Runtimes = None
        self._UserAccess = None
        self._RequestId = None

    @property
    def Runtimes(self):
        """TIEMS支持的运行环境列表
        :rtype: list of Runtime
        """
        return self._Runtimes

    @Runtimes.setter
    def Runtimes(self, Runtimes):
        self._Runtimes = Runtimes

    @property
    def UserAccess(self):
        """用户对runtime对权限
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UserAccess

    @UserAccess.setter
    def UserAccess(self, UserAccess):
        self._UserAccess = UserAccess

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Runtimes") is not None:
            self._Runtimes = []
            for item in params.get("Runtimes"):
                obj = Runtime()
                obj._deserialize(item)
                self._Runtimes.append(obj)
        self._UserAccess = params.get("UserAccess")
        self._RequestId = params.get("RequestId")


class DescribeServiceConfigsRequest(AbstractModel):
    """DescribeServiceConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选选项，支持按照name等进行筛选
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为1000
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        :param _PageByName: 是否按照配置名分页
        :type PageByName: bool
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None
        self._PageByName = None

    @property
    def Filters(self):
        """筛选选项，支持按照name等进行筛选
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def PageByName(self):
        """是否按照配置名分页
        :rtype: bool
        """
        return self._PageByName

    @PageByName.setter
    def PageByName(self, PageByName):
        self._PageByName = PageByName


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        self._PageByName = params.get("PageByName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceConfigsResponse(AbstractModel):
    """DescribeServiceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceConfigs: 服务配置
        :type ServiceConfigs: list of Config
        :param _TotalCount: 服务配置总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceConfigs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ServiceConfigs(self):
        """服务配置
        :rtype: list of Config
        """
        return self._ServiceConfigs

    @ServiceConfigs.setter
    def ServiceConfigs(self, ServiceConfigs):
        self._ServiceConfigs = ServiceConfigs

    @property
    def TotalCount(self):
        """服务配置总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ServiceConfigs") is not None:
            self._ServiceConfigs = []
            for item in params.get("ServiceConfigs"):
                obj = Config()
                obj._deserialize(item)
                self._ServiceConfigs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeServicesRequest(AbstractModel):
    """DescribeServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 筛选选项，支持筛选的字段：id, region, zone, cluster, status, runtime, rsg_id
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param _OrderField: 排序的依据字段， 取值范围 "CREATE_TIME" "UPDATE_TIME"
        :type OrderField: str
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._OrderField = None

    @property
    def Filters(self):
        """筛选选项，支持筛选的字段：id, region, zone, cluster, status, runtime, rsg_id
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        """输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def OrderField(self):
        """排序的依据字段， 取值范围 "CREATE_TIME" "UPDATE_TIME"
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServicesResponse(AbstractModel):
    """DescribeServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Services: 服务列表
        :type Services: list of ModelService
        :param _TotalCount: 服务总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Services = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Services(self):
        """服务列表
        :rtype: list of ModelService
        """
        return self._Services

    @Services.setter
    def Services(self, Services):
        self._Services = Services

    @property
    def TotalCount(self):
        """服务总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Services") is not None:
            self._Services = []
            for item in params.get("Services"):
                obj = ModelService()
                obj._deserialize(item)
                self._Services.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DisableRsgAsGroupRequest(AbstractModel):
    """DisableRsgAsGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组 ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """伸缩组 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRsgAsGroupResponse(AbstractModel):
    """DisableRsgAsGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableRsgAsGroupRequest(AbstractModel):
    """EnableRsgAsGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组 ID
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
        """伸缩组 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRsgAsGroupResponse(AbstractModel):
    """EnableRsgAsGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ExposeInfo(AbstractModel):
    """暴露信息

    """

    def __init__(self):
        r"""
        :param _ExposeType: 暴露方式，支持 EXTERNAL（外网暴露），VPC （VPC内网打通）
        :type ExposeType: str
        :param _Ip: 暴露Ip。暴露方式为 EXTERNAL 为外网 Ip，暴露方式为 VPC 时为指定 Vpc 下的Vip
        :type Ip: str
        :param _VpcId: 暴露方式为 VPC 时，打通的私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 暴露方式为 VPC 时，打通的子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _GateWayServiceId: GATEWAY 服务id，ExposeType = GATEWAY 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type GateWayServiceId: str
        :param _GateWayAPIId: GATEWAY api id，ExposeType = GATEWAY 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type GateWayAPIId: str
        :param _GateWayDomain: GATEWAY domain，ExposeType = GATEWAY 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type GateWayDomain: str
        """
        self._ExposeType = None
        self._Ip = None
        self._VpcId = None
        self._SubnetId = None
        self._GateWayServiceId = None
        self._GateWayAPIId = None
        self._GateWayDomain = None

    @property
    def ExposeType(self):
        """暴露方式，支持 EXTERNAL（外网暴露），VPC （VPC内网打通）
        :rtype: str
        """
        return self._ExposeType

    @ExposeType.setter
    def ExposeType(self, ExposeType):
        self._ExposeType = ExposeType

    @property
    def Ip(self):
        """暴露Ip。暴露方式为 EXTERNAL 为外网 Ip，暴露方式为 VPC 时为指定 Vpc 下的Vip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def VpcId(self):
        """暴露方式为 VPC 时，打通的私有网络Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """暴露方式为 VPC 时，打通的子网Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def GateWayServiceId(self):
        """GATEWAY 服务id，ExposeType = GATEWAY 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GateWayServiceId

    @GateWayServiceId.setter
    def GateWayServiceId(self, GateWayServiceId):
        self._GateWayServiceId = GateWayServiceId

    @property
    def GateWayAPIId(self):
        """GATEWAY api id，ExposeType = GATEWAY 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GateWayAPIId

    @GateWayAPIId.setter
    def GateWayAPIId(self, GateWayAPIId):
        self._GateWayAPIId = GateWayAPIId

    @property
    def GateWayDomain(self):
        """GATEWAY domain，ExposeType = GATEWAY 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GateWayDomain

    @GateWayDomain.setter
    def GateWayDomain(self, GateWayDomain):
        self._GateWayDomain = GateWayDomain


    def _deserialize(self, params):
        self._ExposeType = params.get("ExposeType")
        self._Ip = params.get("Ip")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._GateWayServiceId = params.get("GateWayServiceId")
        self._GateWayAPIId = params.get("GateWayAPIId")
        self._GateWayDomain = params.get("GateWayDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposeServiceRequest(AbstractModel):
    """ExposeService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务Id
        :type ServiceId: str
        :param _ExposeType: 暴露方式，支持 EXTERNAL（外网暴露），VPC （VPC内网打通）
        :type ExposeType: str
        :param _VpcId: 暴露方式为 VPC 时，填写需要打通的私有网络Id
        :type VpcId: str
        :param _SubnetId: 暴露方式为 VPC 时，填写需要打通的子网Id
        :type SubnetId: str
        """
        self._ServiceId = None
        self._ExposeType = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def ServiceId(self):
        """服务Id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ExposeType(self):
        """暴露方式，支持 EXTERNAL（外网暴露），VPC （VPC内网打通）
        :rtype: str
        """
        return self._ExposeType

    @ExposeType.setter
    def ExposeType(self, ExposeType):
        self._ExposeType = ExposeType

    @property
    def VpcId(self):
        """暴露方式为 VPC 时，填写需要打通的私有网络Id
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """暴露方式为 VPC 时，填写需要打通的子网Id
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ExposeType = params.get("ExposeType")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExposeServiceResponse(AbstractModel):
    """ExposeService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Expose: 暴露方式
        :type Expose: :class:`tencentcloud.tiems.v20190416.models.ExposeInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Expose = None
        self._RequestId = None

    @property
    def Expose(self):
        """暴露方式
        :rtype: :class:`tencentcloud.tiems.v20190416.models.ExposeInfo`
        """
        return self._Expose

    @Expose.setter
    def Expose(self, Expose):
        self._Expose = Expose

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Expose") is not None:
            self._Expose = ExposeInfo()
            self._Expose._deserialize(params.get("Expose"))
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """筛选项

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Values: 取值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """取值
        :rtype: list of str
        """
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
        


class Instance(AbstractModel):
    """节点

    """

    def __init__(self):
        r"""
        :param _Id: 节点 ID
        :type Id: str
        :param _Zone: 节点所在地区
        :type Zone: str
        :param _InstanceType: 节点类型
        :type InstanceType: str
        :param _InstanceChargeType: 节点充值类型
        :type InstanceChargeType: str
        :param _Cpu: Cpu 核数
        :type Cpu: int
        :param _Memory: 内存
        :type Memory: int
        :param _Gpu: Gpu 核数
        :type Gpu: int
        :param _State: 节点状态
        :type State: str
        :param _AbnormalReason: 节点故障信息
        :type AbnormalReason: str
        :param _Created: 创建时间
        :type Created: str
        :param _Updated: 更新时间
        :type Updated: str
        :param _DeadlineTime: 到期时间
        :type DeadlineTime: str
        :param _ResourceGroupId: 所属资源组 ID
        :type ResourceGroupId: str
        :param _RenewFlag: 自动续费标签
        :type RenewFlag: str
        :param _Region: 节点所在地域
        :type Region: str
        :param _CpuRequested: 当前 Cpu 申请使用量
        :type CpuRequested: int
        :param _MemoryRequested: 当前 Memory 申请使用量
        :type MemoryRequested: int
        :param _GpuRequested: 当前 Gpu 申请使用量
        :type GpuRequested: int
        :param _RsgAsGroupId: 节点所在伸缩组 ID
        :type RsgAsGroupId: str
        """
        self._Id = None
        self._Zone = None
        self._InstanceType = None
        self._InstanceChargeType = None
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._State = None
        self._AbnormalReason = None
        self._Created = None
        self._Updated = None
        self._DeadlineTime = None
        self._ResourceGroupId = None
        self._RenewFlag = None
        self._Region = None
        self._CpuRequested = None
        self._MemoryRequested = None
        self._GpuRequested = None
        self._RsgAsGroupId = None

    @property
    def Id(self):
        """节点 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Zone(self):
        """节点所在地区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceType(self):
        """节点类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceChargeType(self):
        """节点充值类型
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def Cpu(self):
        """Cpu 核数
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        """Gpu 核数
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def State(self):
        """节点状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def AbnormalReason(self):
        """节点故障信息
        :rtype: str
        """
        return self._AbnormalReason

    @AbnormalReason.setter
    def AbnormalReason(self, AbnormalReason):
        self._AbnormalReason = AbnormalReason

    @property
    def Created(self):
        """创建时间
        :rtype: str
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Updated(self):
        """更新时间
        :rtype: str
        """
        return self._Updated

    @Updated.setter
    def Updated(self, Updated):
        self._Updated = Updated

    @property
    def DeadlineTime(self):
        """到期时间
        :rtype: str
        """
        return self._DeadlineTime

    @DeadlineTime.setter
    def DeadlineTime(self, DeadlineTime):
        self._DeadlineTime = DeadlineTime

    @property
    def ResourceGroupId(self):
        """所属资源组 ID
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def RenewFlag(self):
        """自动续费标签
        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def Region(self):
        """节点所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def CpuRequested(self):
        """当前 Cpu 申请使用量
        :rtype: int
        """
        return self._CpuRequested

    @CpuRequested.setter
    def CpuRequested(self, CpuRequested):
        self._CpuRequested = CpuRequested

    @property
    def MemoryRequested(self):
        """当前 Memory 申请使用量
        :rtype: int
        """
        return self._MemoryRequested

    @MemoryRequested.setter
    def MemoryRequested(self, MemoryRequested):
        self._MemoryRequested = MemoryRequested

    @property
    def GpuRequested(self):
        """当前 Gpu 申请使用量
        :rtype: int
        """
        return self._GpuRequested

    @GpuRequested.setter
    def GpuRequested(self, GpuRequested):
        self._GpuRequested = GpuRequested

    @property
    def RsgAsGroupId(self):
        """节点所在伸缩组 ID
        :rtype: str
        """
        return self._RsgAsGroupId

    @RsgAsGroupId.setter
    def RsgAsGroupId(self, RsgAsGroupId):
        self._RsgAsGroupId = RsgAsGroupId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Zone = params.get("Zone")
        self._InstanceType = params.get("InstanceType")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._State = params.get("State")
        self._AbnormalReason = params.get("AbnormalReason")
        self._Created = params.get("Created")
        self._Updated = params.get("Updated")
        self._DeadlineTime = params.get("DeadlineTime")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._RenewFlag = params.get("RenewFlag")
        self._Region = params.get("Region")
        self._CpuRequested = params.get("CpuRequested")
        self._MemoryRequested = params.get("MemoryRequested")
        self._GpuRequested = params.get("GpuRequested")
        self._RsgAsGroupId = params.get("RsgAsGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    """任务

    """

    def __init__(self):
        r"""
        :param _Id: 任务 Id
        :type Id: str
        :param _Cluster: 集群名
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param _Region: Region 名
        :type Region: str
        :param _Name: 任务名称
        :type Name: str
        :param _Runtime: Worker 使用的运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type Runtime: str
        :param _Description: 任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ConfigId: 配置 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: str
        :param _PredictInput: 预测输入
注意：此字段可能返回 null，表示取不到有效值。
        :type PredictInput: :class:`tencentcloud.tiems.v20190416.models.PredictInput`
        :param _Status: 任务状态
        :type Status: :class:`tencentcloud.tiems.v20190416.models.JobStatus`
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _StartTime: 任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CancelTime: 任务取消时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CancelTime: str
        :param _ResourceGroupId: 任务使用资源组 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Memory: 内存配置, 单位为1M；范围[100, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Gpu: GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param _GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuMemory: int
        :param _ResourceGroupName: 任务使用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _GpuType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param _ConfigName: 配置名
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigName: str
        :param _ConfigVersion: 配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param _JobType: Job类型
注意：此字段可能返回 null，表示取不到有效值。
        :type JobType: str
        :param _QuantizationInput: 量化输入
注意：此字段可能返回 null，表示取不到有效值。
        :type QuantizationInput: :class:`tencentcloud.tiems.v20190416.models.QuantizationInput`
        :param _LogTopicId: Cls日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        """
        self._Id = None
        self._Cluster = None
        self._Region = None
        self._Name = None
        self._Runtime = None
        self._Description = None
        self._ConfigId = None
        self._PredictInput = None
        self._Status = None
        self._CreateTime = None
        self._StartTime = None
        self._EndTime = None
        self._CancelTime = None
        self._ResourceGroupId = None
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuMemory = None
        self._ResourceGroupName = None
        self._GpuType = None
        self._ConfigName = None
        self._ConfigVersion = None
        self._JobType = None
        self._QuantizationInput = None
        self._LogTopicId = None

    @property
    def Id(self):
        """任务 Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Cluster(self):
        """集群名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Region(self):
        """Region 名
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Name(self):
        """任务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Runtime(self):
        """Worker 使用的运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def Description(self):
        """任务描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConfigId(self):
        """配置 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def PredictInput(self):
        """预测输入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tiems.v20190416.models.PredictInput`
        """
        return self._PredictInput

    @PredictInput.setter
    def PredictInput(self, PredictInput):
        self._PredictInput = PredictInput

    @property
    def Status(self):
        """任务状态
        :rtype: :class:`tencentcloud.tiems.v20190416.models.JobStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def StartTime(self):
        """任务开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """任务结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CancelTime(self):
        """任务取消时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CancelTime

    @CancelTime.setter
    def CancelTime(self, CancelTime):
        self._CancelTime = CancelTime

    @property
    def ResourceGroupId(self):
        """任务使用资源组 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Cpu(self):
        """处理器配置, 单位为1/1000核；范围[100, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存配置, 单位为1M；范围[100, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        """GPU算力配置，单位为1/1000 卡，范围 [0, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuMemory(self):
        """显存配置, 单位为1M，范围 [0, 256000]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._GpuMemory

    @GpuMemory.setter
    def GpuMemory(self, GpuMemory):
        self._GpuMemory = GpuMemory

    @property
    def ResourceGroupName(self):
        """任务使用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def GpuType(self):
        """GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def ConfigName(self):
        """配置名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def ConfigVersion(self):
        """配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigVersion

    @ConfigVersion.setter
    def ConfigVersion(self, ConfigVersion):
        self._ConfigVersion = ConfigVersion

    @property
    def JobType(self):
        """Job类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._JobType

    @JobType.setter
    def JobType(self, JobType):
        self._JobType = JobType

    @property
    def QuantizationInput(self):
        """量化输入
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tiems.v20190416.models.QuantizationInput`
        """
        return self._QuantizationInput

    @QuantizationInput.setter
    def QuantizationInput(self, QuantizationInput):
        self._QuantizationInput = QuantizationInput

    @property
    def LogTopicId(self):
        """Cls日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Cluster = params.get("Cluster")
        self._Region = params.get("Region")
        self._Name = params.get("Name")
        self._Runtime = params.get("Runtime")
        self._Description = params.get("Description")
        self._ConfigId = params.get("ConfigId")
        if params.get("PredictInput") is not None:
            self._PredictInput = PredictInput()
            self._PredictInput._deserialize(params.get("PredictInput"))
        if params.get("Status") is not None:
            self._Status = JobStatus()
            self._Status._deserialize(params.get("Status"))
        self._CreateTime = params.get("CreateTime")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CancelTime = params.get("CancelTime")
        self._ResourceGroupId = params.get("ResourceGroupId")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._GpuMemory = params.get("GpuMemory")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._GpuType = params.get("GpuType")
        self._ConfigName = params.get("ConfigName")
        self._ConfigVersion = params.get("ConfigVersion")
        self._JobType = params.get("JobType")
        if params.get("QuantizationInput") is not None:
            self._QuantizationInput = QuantizationInput()
            self._QuantizationInput._deserialize(params.get("QuantizationInput"))
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class JobStatus(AbstractModel):
    """任务状态

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态
        :type Status: str
        :param _Message: 错误时为错误描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _DesiredWorkers: 预期Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredWorkers: int
        :param _CurrentWorkers: 当前Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentWorkers: int
        :param _Replicas: 副本名
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        :param _ReplicaInfos: 副本实例
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicaInfos: list of ReplicaInfo
        """
        self._Status = None
        self._Message = None
        self._DesiredWorkers = None
        self._CurrentWorkers = None
        self._Replicas = None
        self._ReplicaInfos = None

    @property
    def Status(self):
        """任务状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """错误时为错误描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def DesiredWorkers(self):
        """预期Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DesiredWorkers

    @DesiredWorkers.setter
    def DesiredWorkers(self, DesiredWorkers):
        self._DesiredWorkers = DesiredWorkers

    @property
    def CurrentWorkers(self):
        """当前Worker数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CurrentWorkers

    @CurrentWorkers.setter
    def CurrentWorkers(self, CurrentWorkers):
        self._CurrentWorkers = CurrentWorkers

    @property
    def Replicas(self):
        """副本名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def ReplicaInfos(self):
        """副本实例
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ReplicaInfo
        """
        return self._ReplicaInfos

    @ReplicaInfos.setter
    def ReplicaInfos(self, ReplicaInfos):
        self._ReplicaInfos = ReplicaInfos


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._DesiredWorkers = params.get("DesiredWorkers")
        self._CurrentWorkers = params.get("CurrentWorkers")
        self._Replicas = params.get("Replicas")
        if params.get("ReplicaInfos") is not None:
            self._ReplicaInfos = []
            for item in params.get("ReplicaInfos"):
                obj = ReplicaInfo()
                obj._deserialize(item)
                self._ReplicaInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelService(AbstractModel):
    """模型服务

    """

    def __init__(self):
        r"""
        :param _Id: 服务ID
        :type Id: str
        :param _Cluster: 运行集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param _Name: 服务名称
        :type Name: str
        :param _Runtime: 运行环境
        :type Runtime: str
        :param _ModelUri: 模型地址
        :type ModelUri: str
        :param _Cpu: 处理器配置, 单位为1/1000核
        :type Cpu: int
        :param _Memory: 内存配置, 单位为1M
        :type Memory: int
        :param _Gpu: GPU 配置, 单位为1/1000 卡
        :type Gpu: int
        :param _GpuMemory: 显存配置, 单位为1M
        :type GpuMemory: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _ScaleMode: 支持AUTO, MANUAL
        :type ScaleMode: str
        :param _Scaler: 弹性伸缩配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param _Status: 服务状态
        :type Status: :class:`tencentcloud.tiems.v20190416.models.ServiceStatus`
        :param _AccessToken: 访问密钥
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessToken: str
        :param _ConfigId: 服务配置Id
        :type ConfigId: str
        :param _ConfigName: 服务配置名
        :type ConfigName: str
        :param _ServeSeconds: 服务运行时长
        :type ServeSeconds: int
        :param _ConfigVersion: 配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigVersion: str
        :param _ResourceGroupId: 服务使用资源组 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupId: str
        :param _Exposes: 暴露方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Exposes: list of ExposeInfo
        :param _Region: Region 名
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _ResourceGroupName: 服务使用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceGroupName: str
        :param _Description: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _GpuType: GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: str
        :param _LogTopicId: Cls日志主题Id
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        """
        self._Id = None
        self._Cluster = None
        self._Name = None
        self._Runtime = None
        self._ModelUri = None
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._GpuMemory = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ScaleMode = None
        self._Scaler = None
        self._Status = None
        self._AccessToken = None
        self._ConfigId = None
        self._ConfigName = None
        self._ServeSeconds = None
        self._ConfigVersion = None
        self._ResourceGroupId = None
        self._Exposes = None
        self._Region = None
        self._ResourceGroupName = None
        self._Description = None
        self._GpuType = None
        self._LogTopicId = None

    @property
    def Id(self):
        """服务ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Cluster(self):
        """运行集群
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Name(self):
        """服务名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Runtime(self):
        """运行环境
        :rtype: str
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def ModelUri(self):
        """模型地址
        :rtype: str
        """
        return self._ModelUri

    @ModelUri.setter
    def ModelUri(self, ModelUri):
        self._ModelUri = ModelUri

    @property
    def Cpu(self):
        """处理器配置, 单位为1/1000核
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存配置, 单位为1M
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        """GPU 配置, 单位为1/1000 卡
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def GpuMemory(self):
        """显存配置, 单位为1M
        :rtype: int
        """
        return self._GpuMemory

    @GpuMemory.setter
    def GpuMemory(self, GpuMemory):
        self._GpuMemory = GpuMemory

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ScaleMode(self):
        """支持AUTO, MANUAL
        :rtype: str
        """
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def Scaler(self):
        """弹性伸缩配置
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        """
        return self._Scaler

    @Scaler.setter
    def Scaler(self, Scaler):
        self._Scaler = Scaler

    @property
    def Status(self):
        """服务状态
        :rtype: :class:`tencentcloud.tiems.v20190416.models.ServiceStatus`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccessToken(self):
        """访问密钥
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessToken

    @AccessToken.setter
    def AccessToken(self, AccessToken):
        self._AccessToken = AccessToken

    @property
    def ConfigId(self):
        """服务配置Id
        :rtype: str
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def ConfigName(self):
        """服务配置名
        :rtype: str
        """
        return self._ConfigName

    @ConfigName.setter
    def ConfigName(self, ConfigName):
        self._ConfigName = ConfigName

    @property
    def ServeSeconds(self):
        """服务运行时长
        :rtype: int
        """
        return self._ServeSeconds

    @ServeSeconds.setter
    def ServeSeconds(self, ServeSeconds):
        self._ServeSeconds = ServeSeconds

    @property
    def ConfigVersion(self):
        """配置版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigVersion

    @ConfigVersion.setter
    def ConfigVersion(self, ConfigVersion):
        self._ConfigVersion = ConfigVersion

    @property
    def ResourceGroupId(self):
        """服务使用资源组 Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupId

    @ResourceGroupId.setter
    def ResourceGroupId(self, ResourceGroupId):
        self._ResourceGroupId = ResourceGroupId

    @property
    def Exposes(self):
        """暴露方式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExposeInfo
        """
        return self._Exposes

    @Exposes.setter
    def Exposes(self, Exposes):
        self._Exposes = Exposes

    @property
    def Region(self):
        """Region 名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ResourceGroupName(self):
        """服务使用资源组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceGroupName

    @ResourceGroupName.setter
    def ResourceGroupName(self, ResourceGroupName):
        self._ResourceGroupName = ResourceGroupName

    @property
    def Description(self):
        """备注
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GpuType(self):
        """GPU类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def LogTopicId(self):
        """Cls日志主题Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Cluster = params.get("Cluster")
        self._Name = params.get("Name")
        self._Runtime = params.get("Runtime")
        self._ModelUri = params.get("ModelUri")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._GpuMemory = params.get("GpuMemory")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ScaleMode = params.get("ScaleMode")
        if params.get("Scaler") is not None:
            self._Scaler = Scaler()
            self._Scaler._deserialize(params.get("Scaler"))
        if params.get("Status") is not None:
            self._Status = ServiceStatus()
            self._Status._deserialize(params.get("Status"))
        self._AccessToken = params.get("AccessToken")
        self._ConfigId = params.get("ConfigId")
        self._ConfigName = params.get("ConfigName")
        self._ServeSeconds = params.get("ServeSeconds")
        self._ConfigVersion = params.get("ConfigVersion")
        self._ResourceGroupId = params.get("ResourceGroupId")
        if params.get("Exposes") is not None:
            self._Exposes = []
            for item in params.get("Exposes"):
                obj = ExposeInfo()
                obj._deserialize(item)
                self._Exposes.append(obj)
        self._Region = params.get("Region")
        self._ResourceGroupName = params.get("ResourceGroupName")
        self._Description = params.get("Description")
        self._GpuType = params.get("GpuType")
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Option(AbstractModel):
    """配置项

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Value: 取值
        :type Value: int
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """取值
        :rtype: int
        """
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
        


class PredictInput(AbstractModel):
    """预测输入

    """

    def __init__(self):
        r"""
        :param _InputPath: 输入路径，支持 cos 格式路径文件夹或文件
        :type InputPath: str
        :param _OutputPath: 输出路径，支持 cos 格式路径
        :type OutputPath: str
        :param _InputDataFormat: 输入数据格式，目前支持：JSON
        :type InputDataFormat: str
        :param _OutputDataFormat: 输出数据格式，目前支持：JSON
        :type OutputDataFormat: str
        :param _BatchSize: 预测批大小，默认为 64
        :type BatchSize: int
        :param _SignatureName: 模型签名
注意：此字段可能返回 null，表示取不到有效值。
        :type SignatureName: str
        """
        self._InputPath = None
        self._OutputPath = None
        self._InputDataFormat = None
        self._OutputDataFormat = None
        self._BatchSize = None
        self._SignatureName = None

    @property
    def InputPath(self):
        """输入路径，支持 cos 格式路径文件夹或文件
        :rtype: str
        """
        return self._InputPath

    @InputPath.setter
    def InputPath(self, InputPath):
        self._InputPath = InputPath

    @property
    def OutputPath(self):
        """输出路径，支持 cos 格式路径
        :rtype: str
        """
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def InputDataFormat(self):
        """输入数据格式，目前支持：JSON
        :rtype: str
        """
        return self._InputDataFormat

    @InputDataFormat.setter
    def InputDataFormat(self, InputDataFormat):
        self._InputDataFormat = InputDataFormat

    @property
    def OutputDataFormat(self):
        """输出数据格式，目前支持：JSON
        :rtype: str
        """
        return self._OutputDataFormat

    @OutputDataFormat.setter
    def OutputDataFormat(self, OutputDataFormat):
        self._OutputDataFormat = OutputDataFormat

    @property
    def BatchSize(self):
        """预测批大小，默认为 64
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def SignatureName(self):
        """模型签名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SignatureName

    @SignatureName.setter
    def SignatureName(self, SignatureName):
        self._SignatureName = SignatureName


    def _deserialize(self, params):
        self._InputPath = params.get("InputPath")
        self._OutputPath = params.get("OutputPath")
        self._InputDataFormat = params.get("InputDataFormat")
        self._OutputDataFormat = params.get("OutputDataFormat")
        self._BatchSize = params.get("BatchSize")
        self._SignatureName = params.get("SignatureName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuantizationInput(AbstractModel):
    """量化输入

    """

    def __init__(self):
        r"""
        :param _InputPath: 量化输入路径
        :type InputPath: str
        :param _OutputPath: 量化输出路径
        :type OutputPath: str
        :param _BatchSize: 量化批大小
        :type BatchSize: int
        :param _Precision: 量化精度，支持：FP32，FP16，INT8
        :type Precision: str
        :param _ConvertType: 转换类型
        :type ConvertType: str
        """
        self._InputPath = None
        self._OutputPath = None
        self._BatchSize = None
        self._Precision = None
        self._ConvertType = None

    @property
    def InputPath(self):
        """量化输入路径
        :rtype: str
        """
        return self._InputPath

    @InputPath.setter
    def InputPath(self, InputPath):
        self._InputPath = InputPath

    @property
    def OutputPath(self):
        """量化输出路径
        :rtype: str
        """
        return self._OutputPath

    @OutputPath.setter
    def OutputPath(self, OutputPath):
        self._OutputPath = OutputPath

    @property
    def BatchSize(self):
        """量化批大小
        :rtype: int
        """
        return self._BatchSize

    @BatchSize.setter
    def BatchSize(self, BatchSize):
        self._BatchSize = BatchSize

    @property
    def Precision(self):
        """量化精度，支持：FP32，FP16，INT8
        :rtype: str
        """
        return self._Precision

    @Precision.setter
    def Precision(self, Precision):
        self._Precision = Precision

    @property
    def ConvertType(self):
        """转换类型
        :rtype: str
        """
        return self._ConvertType

    @ConvertType.setter
    def ConvertType(self, ConvertType):
        self._ConvertType = ConvertType


    def _deserialize(self, params):
        self._InputPath = params.get("InputPath")
        self._OutputPath = params.get("OutputPath")
        self._BatchSize = params.get("BatchSize")
        self._Precision = params.get("Precision")
        self._ConvertType = params.get("ConvertType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplicaInfo(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _Name: 实例名称
        :type Name: str
        :param _EniIp: 弹性网卡模式时，弹性网卡Ip
注意：此字段可能返回 null，表示取不到有效值。
        :type EniIp: str
        :param _Status: Normal: 正常运行中; Abnormal: 异常；Waiting：等待中
        :type Status: str
        :param _Message: 当 status为 Abnormal 的时候，一些额外的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _StartTime: 启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Restarted: 重启次数
        :type Restarted: int
        """
        self._Name = None
        self._EniIp = None
        self._Status = None
        self._Message = None
        self._StartTime = None
        self._CreateTime = None
        self._Restarted = None

    @property
    def Name(self):
        """实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EniIp(self):
        """弹性网卡模式时，弹性网卡Ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EniIp

    @EniIp.setter
    def EniIp(self, EniIp):
        self._EniIp = EniIp

    @property
    def Status(self):
        """Normal: 正常运行中; Abnormal: 异常；Waiting：等待中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        """当 status为 Abnormal 的时候，一些额外的信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def StartTime(self):
        """启动时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Restarted(self):
        """重启次数
        :rtype: int
        """
        return self._Restarted

    @Restarted.setter
    def Restarted(self, Restarted):
        self._Restarted = Restarted


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EniIp = params.get("EniIp")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._StartTime = params.get("StartTime")
        self._CreateTime = params.get("CreateTime")
        self._Restarted = params.get("Restarted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceGroup(AbstractModel):
    """资源组

    """

    def __init__(self):
        r"""
        :param _Id: 资源组 Id
        :type Id: str
        :param _Region: 地域
        :type Region: str
        :param _Cluster: 集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Cluster: str
        :param _Name: 资源组名称
        :type Name: str
        :param _Description: 资源组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Created: 创建时间
        :type Created: str
        :param _Updated: 更新时间
        :type Updated: str
        :param _InstanceCount: 资源组主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceCount: int
        :param _ServiceCount: 使用资源组的服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceCount: int
        :param _JobCount: 使用资源组的任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :type JobCount: int
        :param _Public: 资源组是否为公共资源组
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: bool
        :param _InstanceType: 机器类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _Status: 资源组状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Gpu: 显卡总张数
注意：此字段可能返回 null，表示取不到有效值。
        :type Gpu: int
        :param _Cpu: 处理器总核数
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Memory: 内存总量，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        :param _Zone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _GpuType: Gpu类型
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuType: list of str
        :param _HasPrepaid: 该资源组下是否有预付费资源
注意：此字段可能返回 null，表示取不到有效值。
        :type HasPrepaid: bool
        :param _PayMode: 资源组是否允许预付费或后付费模式
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        """
        self._Id = None
        self._Region = None
        self._Cluster = None
        self._Name = None
        self._Description = None
        self._Created = None
        self._Updated = None
        self._InstanceCount = None
        self._ServiceCount = None
        self._JobCount = None
        self._Public = None
        self._InstanceType = None
        self._Status = None
        self._Gpu = None
        self._Cpu = None
        self._Memory = None
        self._Zone = None
        self._GpuType = None
        self._HasPrepaid = None
        self._PayMode = None

    @property
    def Id(self):
        """资源组 Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Region(self):
        """地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Cluster(self):
        """集群
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def Name(self):
        """资源组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        """资源组描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Created(self):
        """创建时间
        :rtype: str
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Updated(self):
        """更新时间
        :rtype: str
        """
        return self._Updated

    @Updated.setter
    def Updated(self, Updated):
        self._Updated = Updated

    @property
    def InstanceCount(self):
        """资源组主机数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def ServiceCount(self):
        """使用资源组的服务数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ServiceCount

    @ServiceCount.setter
    def ServiceCount(self, ServiceCount):
        self._ServiceCount = ServiceCount

    @property
    def JobCount(self):
        """使用资源组的任务数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._JobCount

    @JobCount.setter
    def JobCount(self, JobCount):
        self._JobCount = JobCount

    @property
    def Public(self):
        """资源组是否为公共资源组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def InstanceType(self):
        """机器类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Status(self):
        """资源组状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Gpu(self):
        """显卡总张数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def Cpu(self):
        """处理器总核数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存总量，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Zone(self):
        """可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GpuType(self):
        """Gpu类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def HasPrepaid(self):
        """该资源组下是否有预付费资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HasPrepaid

    @HasPrepaid.setter
    def HasPrepaid(self, HasPrepaid):
        self._HasPrepaid = HasPrepaid

    @property
    def PayMode(self):
        """资源组是否允许预付费或后付费模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Region = params.get("Region")
        self._Cluster = params.get("Cluster")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Created = params.get("Created")
        self._Updated = params.get("Updated")
        self._InstanceCount = params.get("InstanceCount")
        self._ServiceCount = params.get("ServiceCount")
        self._JobCount = params.get("JobCount")
        self._Public = params.get("Public")
        self._InstanceType = params.get("InstanceType")
        self._Status = params.get("Status")
        self._Gpu = params.get("Gpu")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Zone = params.get("Zone")
        self._GpuType = params.get("GpuType")
        self._HasPrepaid = params.get("HasPrepaid")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsgAsActivityRelatedInstance(AbstractModel):
    """伸缩组活动关联的节点

    """

    def __init__(self):
        r"""
        :param _InstanceId: 节点 ID
        :type InstanceId: str
        :param _InstanceStatus: 节点状态
        :type InstanceStatus: str
        """
        self._InstanceId = None
        self._InstanceStatus = None

    @property
    def InstanceId(self):
        """节点 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceStatus(self):
        """节点状态
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceStatus = params.get("InstanceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsgAsGroup(AbstractModel):
    """资源组的伸缩组

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组 ID
        :type Id: str
        :param _Region: 伸缩组所在地域
        :type Region: str
        :param _Zone: 伸缩组所在可用区
        :type Zone: str
        :param _Cluster: 伸缩组所在集群
        :type Cluster: str
        :param _RsgId: 伸缩组所在资源组 ID
        :type RsgId: str
        :param _Name: 伸缩组名称
        :type Name: str
        :param _MaxSize: 伸缩组允许的最大节点个数
        :type MaxSize: int
        :param _MinSize: 伸缩组允许的最小节点个数
        :type MinSize: int
        :param _CreateTime: 伸缩组创建时间
        :type CreateTime: str
        :param _UpdateTime: 伸缩组更新时间
        :type UpdateTime: str
        :param _Status: 伸缩组状态
        :type Status: str
        :param _InstanceType: 伸缩组节点类型
        :type InstanceType: str
        :param _InstanceCount: 伸缩组内节点个数
        :type InstanceCount: int
        :param _DesiredSize: 伸缩组起始节点数
        :type DesiredSize: int
        """
        self._Id = None
        self._Region = None
        self._Zone = None
        self._Cluster = None
        self._RsgId = None
        self._Name = None
        self._MaxSize = None
        self._MinSize = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Status = None
        self._InstanceType = None
        self._InstanceCount = None
        self._DesiredSize = None

    @property
    def Id(self):
        """伸缩组 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Region(self):
        """伸缩组所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Zone(self):
        """伸缩组所在可用区
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Cluster(self):
        """伸缩组所在集群
        :rtype: str
        """
        return self._Cluster

    @Cluster.setter
    def Cluster(self, Cluster):
        self._Cluster = Cluster

    @property
    def RsgId(self):
        """伸缩组所在资源组 ID
        :rtype: str
        """
        return self._RsgId

    @RsgId.setter
    def RsgId(self, RsgId):
        self._RsgId = RsgId

    @property
    def Name(self):
        """伸缩组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MaxSize(self):
        """伸缩组允许的最大节点个数
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """伸缩组允许的最小节点个数
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def CreateTime(self):
        """伸缩组创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """伸缩组更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Status(self):
        """伸缩组状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def InstanceType(self):
        """伸缩组节点类型
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceCount(self):
        """伸缩组内节点个数
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def DesiredSize(self):
        """伸缩组起始节点数
        :rtype: int
        """
        return self._DesiredSize

    @DesiredSize.setter
    def DesiredSize(self, DesiredSize):
        self._DesiredSize = DesiredSize


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Region = params.get("Region")
        self._Zone = params.get("Zone")
        self._Cluster = params.get("Cluster")
        self._RsgId = params.get("RsgId")
        self._Name = params.get("Name")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Status = params.get("Status")
        self._InstanceType = params.get("InstanceType")
        self._InstanceCount = params.get("InstanceCount")
        self._DesiredSize = params.get("DesiredSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RsgAsGroupActivity(AbstractModel):
    """伸缩组活动信息

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组活动 ID
        :type Id: str
        :param _RsgAsGroupId: 关联的伸缩组 ID
        :type RsgAsGroupId: str
        :param _ActivityType: 活动类型
        :type ActivityType: str
        :param _StatusCode: 状态的编码
        :type StatusCode: str
        :param _StatusMessage: 状态的消息
        :type StatusMessage: str
        :param _Cause: 活动原因
        :type Cause: str
        :param _Description: 活动描述
        :type Description: str
        :param _StartTime: 活动开始时间
        :type StartTime: str
        :param _EndTime: 活动结束时间
        :type EndTime: str
        :param _CreateTime: 活动创建时间
        :type CreateTime: str
        :param _RsgAsActivityRelatedInstance: 活动相关联的节点
        :type RsgAsActivityRelatedInstance: list of RsgAsActivityRelatedInstance
        :param _StatusMessageSimplified: 简略的状态消息
        :type StatusMessageSimplified: str
        """
        self._Id = None
        self._RsgAsGroupId = None
        self._ActivityType = None
        self._StatusCode = None
        self._StatusMessage = None
        self._Cause = None
        self._Description = None
        self._StartTime = None
        self._EndTime = None
        self._CreateTime = None
        self._RsgAsActivityRelatedInstance = None
        self._StatusMessageSimplified = None

    @property
    def Id(self):
        """伸缩组活动 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RsgAsGroupId(self):
        """关联的伸缩组 ID
        :rtype: str
        """
        return self._RsgAsGroupId

    @RsgAsGroupId.setter
    def RsgAsGroupId(self, RsgAsGroupId):
        self._RsgAsGroupId = RsgAsGroupId

    @property
    def ActivityType(self):
        """活动类型
        :rtype: str
        """
        return self._ActivityType

    @ActivityType.setter
    def ActivityType(self, ActivityType):
        self._ActivityType = ActivityType

    @property
    def StatusCode(self):
        """状态的编码
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def StatusMessage(self):
        """状态的消息
        :rtype: str
        """
        return self._StatusMessage

    @StatusMessage.setter
    def StatusMessage(self, StatusMessage):
        self._StatusMessage = StatusMessage

    @property
    def Cause(self):
        """活动原因
        :rtype: str
        """
        return self._Cause

    @Cause.setter
    def Cause(self, Cause):
        self._Cause = Cause

    @property
    def Description(self):
        """活动描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        """活动开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """活动结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreateTime(self):
        """活动创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RsgAsActivityRelatedInstance(self):
        """活动相关联的节点
        :rtype: list of RsgAsActivityRelatedInstance
        """
        return self._RsgAsActivityRelatedInstance

    @RsgAsActivityRelatedInstance.setter
    def RsgAsActivityRelatedInstance(self, RsgAsActivityRelatedInstance):
        self._RsgAsActivityRelatedInstance = RsgAsActivityRelatedInstance

    @property
    def StatusMessageSimplified(self):
        """简略的状态消息
        :rtype: str
        """
        return self._StatusMessageSimplified

    @StatusMessageSimplified.setter
    def StatusMessageSimplified(self, StatusMessageSimplified):
        self._StatusMessageSimplified = StatusMessageSimplified


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RsgAsGroupId = params.get("RsgAsGroupId")
        self._ActivityType = params.get("ActivityType")
        self._StatusCode = params.get("StatusCode")
        self._StatusMessage = params.get("StatusMessage")
        self._Cause = params.get("Cause")
        self._Description = params.get("Description")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreateTime = params.get("CreateTime")
        if params.get("RsgAsActivityRelatedInstance") is not None:
            self._RsgAsActivityRelatedInstance = []
            for item in params.get("RsgAsActivityRelatedInstance"):
                obj = RsgAsActivityRelatedInstance()
                obj._deserialize(item)
                self._RsgAsActivityRelatedInstance.append(obj)
        self._StatusMessageSimplified = params.get("StatusMessageSimplified")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Runtime(AbstractModel):
    """运行环境

    """

    def __init__(self):
        r"""
        :param _Name: 运行环境名称
        :type Name: str
        :param _Framework: 运行环境框架
        :type Framework: str
        :param _Description: 运行环境描述
        :type Description: str
        :param _Public: 是否为公开运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: bool
        :param _HealthCheckOn: 是否打开健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckOn: bool
        :param _Image: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._Name = None
        self._Framework = None
        self._Description = None
        self._Public = None
        self._HealthCheckOn = None
        self._Image = None
        self._CreateTime = None

    @property
    def Name(self):
        """运行环境名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Framework(self):
        """运行环境框架
        :rtype: str
        """
        return self._Framework

    @Framework.setter
    def Framework(self, Framework):
        self._Framework = Framework

    @property
    def Description(self):
        """运行环境描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Public(self):
        """是否为公开运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Public

    @Public.setter
    def Public(self, Public):
        self._Public = Public

    @property
    def HealthCheckOn(self):
        """是否打开健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._HealthCheckOn

    @HealthCheckOn.setter
    def HealthCheckOn(self, HealthCheckOn):
        self._HealthCheckOn = HealthCheckOn

    @property
    def Image(self):
        """镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Framework = params.get("Framework")
        self._Description = params.get("Description")
        self._Public = params.get("Public")
        self._HealthCheckOn = params.get("HealthCheckOn")
        self._Image = params.get("Image")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Scaler(AbstractModel):
    """扩缩容配置

    """

    def __init__(self):
        r"""
        :param _MaxReplicas: 最大副本数，ScaleMode 为 MANUAL 时辞会此值会被置为 StartReplicas 取值
        :type MaxReplicas: int
        :param _MinReplicas: 最小副本数，ScaleMode 为 MANUAL 时辞会此值会被置为 StartReplicas 取值
        :type MinReplicas: int
        :param _StartReplicas: 起始副本数
        :type StartReplicas: int
        :param _HpaMetrics: 扩缩容指标，选择自动扩缩容时至少需要选择一个指标，支持CPU-UTIL、MEMORY-UTIL
        :type HpaMetrics: list of Option
        """
        self._MaxReplicas = None
        self._MinReplicas = None
        self._StartReplicas = None
        self._HpaMetrics = None

    @property
    def MaxReplicas(self):
        """最大副本数，ScaleMode 为 MANUAL 时辞会此值会被置为 StartReplicas 取值
        :rtype: int
        """
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def MinReplicas(self):
        """最小副本数，ScaleMode 为 MANUAL 时辞会此值会被置为 StartReplicas 取值
        :rtype: int
        """
        return self._MinReplicas

    @MinReplicas.setter
    def MinReplicas(self, MinReplicas):
        self._MinReplicas = MinReplicas

    @property
    def StartReplicas(self):
        """起始副本数
        :rtype: int
        """
        return self._StartReplicas

    @StartReplicas.setter
    def StartReplicas(self, StartReplicas):
        self._StartReplicas = StartReplicas

    @property
    def HpaMetrics(self):
        """扩缩容指标，选择自动扩缩容时至少需要选择一个指标，支持CPU-UTIL、MEMORY-UTIL
        :rtype: list of Option
        """
        return self._HpaMetrics

    @HpaMetrics.setter
    def HpaMetrics(self, HpaMetrics):
        self._HpaMetrics = HpaMetrics


    def _deserialize(self, params):
        self._MaxReplicas = params.get("MaxReplicas")
        self._MinReplicas = params.get("MinReplicas")
        self._StartReplicas = params.get("StartReplicas")
        if params.get("HpaMetrics") is not None:
            self._HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self._HpaMetrics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceStatus(AbstractModel):
    """服务状态

    """

    def __init__(self):
        r"""
        :param _DesiredReplicas: 预期副本数
        :type DesiredReplicas: int
        :param _CurrentReplicas: 当前副本数
        :type CurrentReplicas: int
        :param _Status: Normal：正常运行中；Abnormal：服务异常，例如容器启动失败等；Waiting：服务等待中，例如容器下载镜像过程等；Stopped：已停止 Stopping 停止中；Resuming：重启中；Updating：服务更新中
        :type Status: str
        :param _Conditions: 服务处于当前状态的原因集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of Conditions
        :param _Replicas: 副本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        :param _Message: 运行状态对额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _ReplicaInfos: 副本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplicaInfos: list of ReplicaInfo
        """
        self._DesiredReplicas = None
        self._CurrentReplicas = None
        self._Status = None
        self._Conditions = None
        self._Replicas = None
        self._Message = None
        self._ReplicaInfos = None

    @property
    def DesiredReplicas(self):
        """预期副本数
        :rtype: int
        """
        return self._DesiredReplicas

    @DesiredReplicas.setter
    def DesiredReplicas(self, DesiredReplicas):
        self._DesiredReplicas = DesiredReplicas

    @property
    def CurrentReplicas(self):
        """当前副本数
        :rtype: int
        """
        return self._CurrentReplicas

    @CurrentReplicas.setter
    def CurrentReplicas(self, CurrentReplicas):
        self._CurrentReplicas = CurrentReplicas

    @property
    def Status(self):
        """Normal：正常运行中；Abnormal：服务异常，例如容器启动失败等；Waiting：服务等待中，例如容器下载镜像过程等；Stopped：已停止 Stopping 停止中；Resuming：重启中；Updating：服务更新中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Conditions(self):
        """服务处于当前状态的原因集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Conditions
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Replicas(self):
        """副本名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def Message(self):
        """运行状态对额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ReplicaInfos(self):
        """副本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ReplicaInfo
        """
        return self._ReplicaInfos

    @ReplicaInfos.setter
    def ReplicaInfos(self, ReplicaInfos):
        self._ReplicaInfos = ReplicaInfos


    def _deserialize(self, params):
        self._DesiredReplicas = params.get("DesiredReplicas")
        self._CurrentReplicas = params.get("CurrentReplicas")
        self._Status = params.get("Status")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = Conditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Replicas = params.get("Replicas")
        self._Message = params.get("Message")
        if params.get("ReplicaInfos") is not None:
            self._ReplicaInfos = []
            for item in params.get("ReplicaInfos"):
                obj = ReplicaInfo()
                obj._deserialize(item)
                self._ReplicaInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateJobRequest(AbstractModel):
    """UpdateJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 Id
        :type JobId: str
        :param _JobAction: 任务更新动作，支持：Cancel
        :type JobAction: str
        :param _Description: 备注
        :type Description: str
        """
        self._JobId = None
        self._JobAction = None
        self._Description = None

    @property
    def JobId(self):
        """任务 Id
        :rtype: str
        """
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def JobAction(self):
        """任务更新动作，支持：Cancel
        :rtype: str
        """
        return self._JobAction

    @JobAction.setter
    def JobAction(self, JobAction):
        self._JobAction = JobAction

    @property
    def Description(self):
        """备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._JobAction = params.get("JobAction")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateJobResponse(AbstractModel):
    """UpdateJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Job: 任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Job: :class:`tencentcloud.tiems.v20190416.models.Job`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Job = None
        self._RequestId = None

    @property
    def Job(self):
        """任务
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Job`
        """
        return self._Job

    @Job.setter
    def Job(self, Job):
        self._Job = Job

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Job") is not None:
            self._Job = Job()
            self._Job._deserialize(params.get("Job"))
        self._RequestId = params.get("RequestId")


class UpdateRsgAsGroupRequest(AbstractModel):
    """UpdateRsgAsGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 伸缩组 ID
        :type Id: str
        :param _Name: 重命名名称
        :type Name: str
        :param _MaxSize: 伸缩组最大节点数
        :type MaxSize: int
        :param _MinSize: 伸缩组最小节点数
        :type MinSize: int
        :param _DesiredSize: 伸缩组期望的节点数
        :type DesiredSize: int
        """
        self._Id = None
        self._Name = None
        self._MaxSize = None
        self._MinSize = None
        self._DesiredSize = None

    @property
    def Id(self):
        """伸缩组 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """重命名名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MaxSize(self):
        """伸缩组最大节点数
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize

    @property
    def MinSize(self):
        """伸缩组最小节点数
        :rtype: int
        """
        return self._MinSize

    @MinSize.setter
    def MinSize(self, MinSize):
        self._MinSize = MinSize

    @property
    def DesiredSize(self):
        """伸缩组期望的节点数
        :rtype: int
        """
        return self._DesiredSize

    @DesiredSize.setter
    def DesiredSize(self, DesiredSize):
        self._DesiredSize = DesiredSize


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MaxSize = params.get("MaxSize")
        self._MinSize = params.get("MinSize")
        self._DesiredSize = params.get("DesiredSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRsgAsGroupResponse(AbstractModel):
    """UpdateRsgAsGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RsgAsGroup: 资源组的伸缩组
        :type RsgAsGroup: :class:`tencentcloud.tiems.v20190416.models.RsgAsGroup`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RsgAsGroup = None
        self._RequestId = None

    @property
    def RsgAsGroup(self):
        """资源组的伸缩组
        :rtype: :class:`tencentcloud.tiems.v20190416.models.RsgAsGroup`
        """
        return self._RsgAsGroup

    @RsgAsGroup.setter
    def RsgAsGroup(self, RsgAsGroup):
        self._RsgAsGroup = RsgAsGroup

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RsgAsGroup") is not None:
            self._RsgAsGroup = RsgAsGroup()
            self._RsgAsGroup._deserialize(params.get("RsgAsGroup"))
        self._RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务Id
        :type ServiceId: str
        :param _Scaler: 扩缩容配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param _ServiceConfigId: 服务配置Id
        :type ServiceConfigId: str
        :param _ScaleMode: 支持AUTO, MANUAL，分别表示自动扩缩容，手动扩缩容
        :type ScaleMode: str
        :param _ServiceAction: 支持STOP(停止) RESUME(重启)
        :type ServiceAction: str
        :param _Description: 备注
        :type Description: str
        :param _GpuType: GPU卡类型
        :type GpuType: str
        :param _Cpu: 处理器配置，单位为 1/1000 核
        :type Cpu: int
        :param _Memory: 内存配置，单位为1M
        :type Memory: int
        :param _Gpu: 显卡配置，单位为 1/1000 卡
        :type Gpu: int
        :param _LogTopicId: Cls日志主题ID
        :type LogTopicId: str
        """
        self._ServiceId = None
        self._Scaler = None
        self._ServiceConfigId = None
        self._ScaleMode = None
        self._ServiceAction = None
        self._Description = None
        self._GpuType = None
        self._Cpu = None
        self._Memory = None
        self._Gpu = None
        self._LogTopicId = None

    @property
    def ServiceId(self):
        """服务Id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Scaler(self):
        """扩缩容配置
        :rtype: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        """
        return self._Scaler

    @Scaler.setter
    def Scaler(self, Scaler):
        self._Scaler = Scaler

    @property
    def ServiceConfigId(self):
        """服务配置Id
        :rtype: str
        """
        return self._ServiceConfigId

    @ServiceConfigId.setter
    def ServiceConfigId(self, ServiceConfigId):
        self._ServiceConfigId = ServiceConfigId

    @property
    def ScaleMode(self):
        """支持AUTO, MANUAL，分别表示自动扩缩容，手动扩缩容
        :rtype: str
        """
        return self._ScaleMode

    @ScaleMode.setter
    def ScaleMode(self, ScaleMode):
        self._ScaleMode = ScaleMode

    @property
    def ServiceAction(self):
        """支持STOP(停止) RESUME(重启)
        :rtype: str
        """
        return self._ServiceAction

    @ServiceAction.setter
    def ServiceAction(self, ServiceAction):
        self._ServiceAction = ServiceAction

    @property
    def Description(self):
        """备注
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GpuType(self):
        """GPU卡类型
        :rtype: str
        """
        return self._GpuType

    @GpuType.setter
    def GpuType(self, GpuType):
        self._GpuType = GpuType

    @property
    def Cpu(self):
        """处理器配置，单位为 1/1000 核
        :rtype: int
        """
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        """内存配置，单位为1M
        :rtype: int
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Gpu(self):
        """显卡配置，单位为 1/1000 卡
        :rtype: int
        """
        return self._Gpu

    @Gpu.setter
    def Gpu(self, Gpu):
        self._Gpu = Gpu

    @property
    def LogTopicId(self):
        """Cls日志主题ID
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        if params.get("Scaler") is not None:
            self._Scaler = Scaler()
            self._Scaler._deserialize(params.get("Scaler"))
        self._ServiceConfigId = params.get("ServiceConfigId")
        self._ScaleMode = params.get("ScaleMode")
        self._ServiceAction = params.get("ServiceAction")
        self._Description = params.get("Description")
        self._GpuType = params.get("GpuType")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        self._Gpu = params.get("Gpu")
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 服务
        :type Service: :class:`tencentcloud.tiems.v20190416.models.ModelService`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Service = None
        self._RequestId = None

    @property
    def Service(self):
        """服务
        :rtype: :class:`tencentcloud.tiems.v20190416.models.ModelService`
        """
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self._Service = ModelService()
            self._Service._deserialize(params.get("Service"))
        self._RequestId = params.get("RequestId")