# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class ApplicationInfo(AbstractModel):
    r"""应用信息

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用id

        :type ApplicationId: str
        :param _ApplicationName: 应用名称
        :type ApplicationName: str
        :param _Description: 应用描述

        :type Description: str
        :param _ConfigEnvironment: 应用的环境配置
        :type ConfigEnvironment: str
        :param _MinSystemDiskSize: 系统盘大小下限，单位GB
        :type MinSystemDiskSize: int
        :param _ApplicationType: 应用类型，目前该项取值可以为PUBLIC_APPLICATION（公共应用）；PRIVATE_APPLICATION（自定义应用）；COMMUNITY_APPLICATION（社区应用）
        :type ApplicationType: str
        :param _ApplicationState: 应用状态：CREATING-创建中；ONLINE -正常在线；DELETING -删除中；ARREARS - 欠费隔离
示例值：ONLINE
        :type ApplicationState: str
        :param _CreateTime: 应用创建时间，格式：%Y-%m-%d %H:%M:%S
        :type CreateTime: str
        :param _ApplicationSize: 应用大小，单位GB
        :type ApplicationSize: int
        """
        self._ApplicationId = None
        self._ApplicationName = None
        self._Description = None
        self._ConfigEnvironment = None
        self._MinSystemDiskSize = None
        self._ApplicationType = None
        self._ApplicationState = None
        self._CreateTime = None
        self._ApplicationSize = None

    @property
    def ApplicationId(self):
        r"""应用id

        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def ApplicationName(self):
        r"""应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def Description(self):
        r"""应用描述

        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ConfigEnvironment(self):
        r"""应用的环境配置
        :rtype: str
        """
        return self._ConfigEnvironment

    @ConfigEnvironment.setter
    def ConfigEnvironment(self, ConfigEnvironment):
        self._ConfigEnvironment = ConfigEnvironment

    @property
    def MinSystemDiskSize(self):
        r"""系统盘大小下限，单位GB
        :rtype: int
        """
        return self._MinSystemDiskSize

    @MinSystemDiskSize.setter
    def MinSystemDiskSize(self, MinSystemDiskSize):
        self._MinSystemDiskSize = MinSystemDiskSize

    @property
    def ApplicationType(self):
        r"""应用类型，目前该项取值可以为PUBLIC_APPLICATION（公共应用）；PRIVATE_APPLICATION（自定义应用）；COMMUNITY_APPLICATION（社区应用）
        :rtype: str
        """
        return self._ApplicationType

    @ApplicationType.setter
    def ApplicationType(self, ApplicationType):
        self._ApplicationType = ApplicationType

    @property
    def ApplicationState(self):
        r"""应用状态：CREATING-创建中；ONLINE -正常在线；DELETING -删除中；ARREARS - 欠费隔离
示例值：ONLINE
        :rtype: str
        """
        return self._ApplicationState

    @ApplicationState.setter
    def ApplicationState(self, ApplicationState):
        self._ApplicationState = ApplicationState

    @property
    def CreateTime(self):
        r"""应用创建时间，格式：%Y-%m-%d %H:%M:%S
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ApplicationSize(self):
        r"""应用大小，单位GB
        :rtype: int
        """
        return self._ApplicationSize

    @ApplicationSize.setter
    def ApplicationSize(self, ApplicationSize):
        self._ApplicationSize = ApplicationSize


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._ApplicationName = params.get("ApplicationName")
        self._Description = params.get("Description")
        self._ConfigEnvironment = params.get("ConfigEnvironment")
        self._MinSystemDiskSize = params.get("MinSystemDiskSize")
        self._ApplicationType = params.get("ApplicationType")
        self._ApplicationState = params.get("ApplicationState")
        self._CreateTime = params.get("CreateTime")
        self._ApplicationSize = params.get("ApplicationSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class COSStorage(AbstractModel):
    r"""cos挂载信息

    """

    def __init__(self):
        r"""
        :param _URI: cos桶uri
        :type URI: str
        """
        self._URI = None

    @property
    def URI(self):
        r"""cos桶uri
        :rtype: str
        """
        return self._URI

    @URI.setter
    def URI(self, URI):
        self._URI = URI


    def _deserialize(self, params):
        self._URI = params.get("URI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeDetail(AbstractModel):
    r"""算力详情

    """

    def __init__(self):
        r"""
        :param _BundleType: 算力套餐ID
        :type BundleType: str
        :param _Count: 节点数量
        :type Count: int
        :param _GPUCount: 显卡数量
        :type GPUCount: str
        :param _GPUMemory: 显存
        :type GPUMemory: str
        :param _GPUPerformance: 算力
        :type GPUPerformance: str
        :param _CPU: CPU核数
        :type CPU: str
        :param _Memory: 内存
        :type Memory: str
        """
        self._BundleType = None
        self._Count = None
        self._GPUCount = None
        self._GPUMemory = None
        self._GPUPerformance = None
        self._CPU = None
        self._Memory = None

    @property
    def BundleType(self):
        r"""算力套餐ID
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def Count(self):
        r"""节点数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def GPUCount(self):
        r"""显卡数量
        :rtype: str
        """
        return self._GPUCount

    @GPUCount.setter
    def GPUCount(self, GPUCount):
        self._GPUCount = GPUCount

    @property
    def GPUMemory(self):
        r"""显存
        :rtype: str
        """
        return self._GPUMemory

    @GPUMemory.setter
    def GPUMemory(self, GPUMemory):
        self._GPUMemory = GPUMemory

    @property
    def GPUPerformance(self):
        r"""算力
        :rtype: str
        """
        return self._GPUPerformance

    @GPUPerformance.setter
    def GPUPerformance(self, GPUPerformance):
        self._GPUPerformance = GPUPerformance

    @property
    def CPU(self):
        r"""CPU核数
        :rtype: str
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""内存
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._BundleType = params.get("BundleType")
        self._Count = params.get("Count")
        self._GPUCount = params.get("GPUCount")
        self._GPUMemory = params.get("GPUMemory")
        self._GPUPerformance = params.get("GPUPerformance")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeInfo(AbstractModel):
    r"""资源相关信息

    """

    def __init__(self):
        r"""
        :param _ComputeResources: 资源类型及数量
        :type ComputeResources: list of ComputeResource
        :param _Replicas: 副本数
        :type Replicas: int
        """
        self._ComputeResources = None
        self._Replicas = None

    @property
    def ComputeResources(self):
        r"""资源类型及数量
        :rtype: list of ComputeResource
        """
        return self._ComputeResources

    @ComputeResources.setter
    def ComputeResources(self, ComputeResources):
        self._ComputeResources = ComputeResources

    @property
    def Replicas(self):
        r"""副本数
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas


    def _deserialize(self, params):
        if params.get("ComputeResources") is not None:
            self._ComputeResources = []
            for item in params.get("ComputeResources"):
                obj = ComputeResource()
                obj._deserialize(item)
                self._ComputeResources.append(obj)
        self._Replicas = params.get("Replicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputeResource(AbstractModel):
    r"""推理服务的算力资源

    """

    def __init__(self):
        r"""
        :param _BundleType: 算力套餐的类型
        :type BundleType: str
        :param _Count: 节点数量
        :type Count: int
        """
        self._BundleType = None
        self._Count = None

    @property
    def BundleType(self):
        r"""算力套餐的类型
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def Count(self):
        r"""节点数量
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        self._BundleType = params.get("BundleType")
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ContainerInfo(AbstractModel):
    r"""容器信息

    """

    def __init__(self):
        r"""
        :param _Image: 镜像相关信息
        :type Image: :class:`tencentcloud.hai.v20230812.models.ImageInfo`
        :param _Port: 服务监听端口
        :type Port: str
        :param _Scripts: 启动命令
        :type Scripts: list of str
        :param _Envs: 环境变量列表
        :type Envs: list of EnvParam
        :param _Storages: 存储挂载配置
        :type Storages: list of StorageInfo
        """
        self._Image = None
        self._Port = None
        self._Scripts = None
        self._Envs = None
        self._Storages = None

    @property
    def Image(self):
        r"""镜像相关信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.ImageInfo`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Port(self):
        r"""服务监听端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Scripts(self):
        r"""启动命令
        :rtype: list of str
        """
        return self._Scripts

    @Scripts.setter
    def Scripts(self, Scripts):
        self._Scripts = Scripts

    @property
    def Envs(self):
        r"""环境变量列表
        :rtype: list of EnvParam
        """
        return self._Envs

    @Envs.setter
    def Envs(self, Envs):
        self._Envs = Envs

    @property
    def Storages(self):
        r"""存储挂载配置
        :rtype: list of StorageInfo
        """
        return self._Storages

    @Storages.setter
    def Storages(self, Storages):
        self._Storages = Storages


    def _deserialize(self, params):
        if params.get("Image") is not None:
            self._Image = ImageInfo()
            self._Image._deserialize(params.get("Image"))
        self._Port = params.get("Port")
        self._Scripts = params.get("Scripts")
        if params.get("Envs") is not None:
            self._Envs = []
            for item in params.get("Envs"):
                obj = EnvParam()
                obj._deserialize(item)
                self._Envs.append(obj)
        if params.get("Storages") is not None:
            self._Storages = []
            for item in params.get("Storages"):
                obj = StorageInfo()
                obj._deserialize(item)
                self._Storages.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationRequest(AbstractModel):
    r"""CreateApplication请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要制作自定义应用的HAI实例ID
        :type InstanceId: str
        :param _ApplicationName: 自定义应用的应用名称
        :type ApplicationName: str
        :param _ApplicationDescription: 自定义应用的描述
        :type ApplicationDescription: str
        """
        self._InstanceId = None
        self._ApplicationName = None
        self._ApplicationDescription = None

    @property
    def InstanceId(self):
        r"""需要制作自定义应用的HAI实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ApplicationName(self):
        r"""自定义应用的应用名称
        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def ApplicationDescription(self):
        r"""自定义应用的描述
        :rtype: str
        """
        return self._ApplicationDescription

    @ApplicationDescription.setter
    def ApplicationDescription(self, ApplicationDescription):
        self._ApplicationDescription = ApplicationDescription


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ApplicationName = params.get("ApplicationName")
        self._ApplicationDescription = params.get("ApplicationDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApplicationResponse(AbstractModel):
    r"""CreateApplication返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: HAI自定义应用ID
        :type ApplicationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApplicationId = None
        self._RequestId = None

    @property
    def ApplicationId(self):
        r"""HAI自定义应用ID
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._RequestId = params.get("RequestId")


class CreateInferServiceByTemplateRequest(AbstractModel):
    r"""CreateInferServiceByTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模版ID
        :type TemplateId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _Replicas: 副本数
        :type Replicas: int
        :param _ServiceChargeType: 付费方式，POSTPAID_BY_HOUR按量后付费
        :type ServiceChargeType: str
        :param _HyperParam: 描述了服务的超参数配置
        :type HyperParam: :class:`tencentcloud.hai.v20230812.models.HyperParam`
        :param _NetworkSetting: 网络设置
        :type NetworkSetting: :class:`tencentcloud.hai.v20230812.models.NetworkSetting`
        """
        self._TemplateId = None
        self._ServiceName = None
        self._Replicas = None
        self._ServiceChargeType = None
        self._HyperParam = None
        self._NetworkSetting = None

    @property
    def TemplateId(self):
        r"""模版ID
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ServiceName(self):
        r"""服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Replicas(self):
        r"""副本数
        :rtype: int
        """
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

    @property
    def ServiceChargeType(self):
        r"""付费方式，POSTPAID_BY_HOUR按量后付费
        :rtype: str
        """
        return self._ServiceChargeType

    @ServiceChargeType.setter
    def ServiceChargeType(self, ServiceChargeType):
        self._ServiceChargeType = ServiceChargeType

    @property
    def HyperParam(self):
        r"""描述了服务的超参数配置
        :rtype: :class:`tencentcloud.hai.v20230812.models.HyperParam`
        """
        return self._HyperParam

    @HyperParam.setter
    def HyperParam(self, HyperParam):
        self._HyperParam = HyperParam

    @property
    def NetworkSetting(self):
        r"""网络设置
        :rtype: :class:`tencentcloud.hai.v20230812.models.NetworkSetting`
        """
        return self._NetworkSetting

    @NetworkSetting.setter
    def NetworkSetting(self, NetworkSetting):
        self._NetworkSetting = NetworkSetting


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._ServiceName = params.get("ServiceName")
        self._Replicas = params.get("Replicas")
        self._ServiceChargeType = params.get("ServiceChargeType")
        if params.get("HyperParam") is not None:
            self._HyperParam = HyperParam()
            self._HyperParam._deserialize(params.get("HyperParam"))
        if params.get("NetworkSetting") is not None:
            self._NetworkSetting = NetworkSetting()
            self._NetworkSetting._deserialize(params.get("NetworkSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInferServiceByTemplateResponse(AbstractModel):
    r"""CreateInferServiceByTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._RequestId = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._RequestId = params.get("RequestId")


class CreateMuskPromptRequest(AbstractModel):
    r"""CreateMuskPrompt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkgroupId: workgroup id
        :type WorkgroupId: str
        :param _WorkflowId: workflow id
        :type WorkflowId: str
        :param _PromptParams: prompt 参数
        :type PromptParams: str
        """
        self._WorkgroupId = None
        self._WorkflowId = None
        self._PromptParams = None

    @property
    def WorkgroupId(self):
        r"""workgroup id
        :rtype: str
        """
        return self._WorkgroupId

    @WorkgroupId.setter
    def WorkgroupId(self, WorkgroupId):
        self._WorkgroupId = WorkgroupId

    @property
    def WorkflowId(self):
        r"""workflow id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def PromptParams(self):
        r"""prompt 参数
        :rtype: str
        """
        return self._PromptParams

    @PromptParams.setter
    def PromptParams(self, PromptParams):
        self._PromptParams = PromptParams


    def _deserialize(self, params):
        self._WorkgroupId = params.get("WorkgroupId")
        self._WorkflowId = params.get("WorkflowId")
        self._PromptParams = params.get("PromptParams")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMuskPromptResponse(AbstractModel):
    r"""CreateMuskPrompt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PromptId: prompt id
        :type PromptId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PromptId = None
        self._RequestId = None

    @property
    def PromptId(self):
        r"""prompt id
        :rtype: str
        """
        return self._PromptId

    @PromptId.setter
    def PromptId(self, PromptId):
        self._PromptId = PromptId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PromptId = params.get("PromptId")
        self._RequestId = params.get("RequestId")


class DeployInferServiceRequest(AbstractModel):
    r"""DeployInferService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceMetaData: 服务元数据信息，如服务名
        :type ServiceMetaData: :class:`tencentcloud.hai.v20230812.models.ServiceMetaData`
        :param _ComputeInfo: 资源相关信息
        :type ComputeInfo: :class:`tencentcloud.hai.v20230812.models.ComputeInfo`
        :param _DeploymentConfigs: 服务部署信息
        :type DeploymentConfigs: list of DeploymentConfig
        :param _HyperParam: 服务超参数配置
        :type HyperParam: :class:`tencentcloud.hai.v20230812.models.HyperParam`
        :param _NetworkSetting: 网络设置
        :type NetworkSetting: :class:`tencentcloud.hai.v20230812.models.NetworkSetting`
        """
        self._ServiceMetaData = None
        self._ComputeInfo = None
        self._DeploymentConfigs = None
        self._HyperParam = None
        self._NetworkSetting = None

    @property
    def ServiceMetaData(self):
        r"""服务元数据信息，如服务名
        :rtype: :class:`tencentcloud.hai.v20230812.models.ServiceMetaData`
        """
        return self._ServiceMetaData

    @ServiceMetaData.setter
    def ServiceMetaData(self, ServiceMetaData):
        self._ServiceMetaData = ServiceMetaData

    @property
    def ComputeInfo(self):
        r"""资源相关信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.ComputeInfo`
        """
        return self._ComputeInfo

    @ComputeInfo.setter
    def ComputeInfo(self, ComputeInfo):
        self._ComputeInfo = ComputeInfo

    @property
    def DeploymentConfigs(self):
        r"""服务部署信息
        :rtype: list of DeploymentConfig
        """
        return self._DeploymentConfigs

    @DeploymentConfigs.setter
    def DeploymentConfigs(self, DeploymentConfigs):
        self._DeploymentConfigs = DeploymentConfigs

    @property
    def HyperParam(self):
        r"""服务超参数配置
        :rtype: :class:`tencentcloud.hai.v20230812.models.HyperParam`
        """
        return self._HyperParam

    @HyperParam.setter
    def HyperParam(self, HyperParam):
        self._HyperParam = HyperParam

    @property
    def NetworkSetting(self):
        r"""网络设置
        :rtype: :class:`tencentcloud.hai.v20230812.models.NetworkSetting`
        """
        return self._NetworkSetting

    @NetworkSetting.setter
    def NetworkSetting(self, NetworkSetting):
        self._NetworkSetting = NetworkSetting


    def _deserialize(self, params):
        if params.get("ServiceMetaData") is not None:
            self._ServiceMetaData = ServiceMetaData()
            self._ServiceMetaData._deserialize(params.get("ServiceMetaData"))
        if params.get("ComputeInfo") is not None:
            self._ComputeInfo = ComputeInfo()
            self._ComputeInfo._deserialize(params.get("ComputeInfo"))
        if params.get("DeploymentConfigs") is not None:
            self._DeploymentConfigs = []
            for item in params.get("DeploymentConfigs"):
                obj = DeploymentConfig()
                obj._deserialize(item)
                self._DeploymentConfigs.append(obj)
        if params.get("HyperParam") is not None:
            self._HyperParam = HyperParam()
            self._HyperParam._deserialize(params.get("HyperParam"))
        if params.get("NetworkSetting") is not None:
            self._NetworkSetting = NetworkSetting()
            self._NetworkSetting._deserialize(params.get("NetworkSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployInferServiceResponse(AbstractModel):
    r"""DeployInferService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._RequestId = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._RequestId = params.get("RequestId")


class DeploymentConfig(AbstractModel):
    r"""服务部署信息

    """

    def __init__(self):
        r"""
        :param _Container: 容器配置
        :type Container: :class:`tencentcloud.hai.v20230812.models.ContainerInfo`
        :param _ContainerCount: 容器数量
        :type ContainerCount: int
        """
        self._Container = None
        self._ContainerCount = None

    @property
    def Container(self):
        r"""容器配置
        :rtype: :class:`tencentcloud.hai.v20230812.models.ContainerInfo`
        """
        return self._Container

    @Container.setter
    def Container(self, Container):
        self._Container = Container

    @property
    def ContainerCount(self):
        r"""容器数量
        :rtype: int
        """
        return self._ContainerCount

    @ContainerCount.setter
    def ContainerCount(self, ContainerCount):
        self._ContainerCount = ContainerCount


    def _deserialize(self, params):
        if params.get("Container") is not None:
            self._Container = ContainerInfo()
            self._Container._deserialize(params.get("Container"))
        self._ContainerCount = params.get("ContainerCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsRequest(AbstractModel):
    r"""DescribeApplications请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationIds: 应用id列表。单次请求数量上限为100个。
        :type ApplicationIds: list of str
        :param _Filters: 过滤器，跟ApplicationIds不能共用，支持的filter主要有：application-id: 精确匹配;scene-id: 精确匹配，通过调用接口 [DescribeScenes](https://cloud.tencent.com/document/api/1721/101608)获取;application-name: 模糊匹配;application-type: 精确匹配，枚举类型如下：PUBLIC_APPLICATION（公共应用）/ PRIVATE_APPLICATION（自定义应用）/ COMMUNITY_APPLICATION（社区应用）;
        :type Filters: list of Filter
        :param _Offset: 偏移量，不得小于0，默认为0
        :type Offset: int
        :param _Limit: 返回量，不得大于100，默认为20
        :type Limit: int
        :param _OrderField: 应用列表排序的依据字段。取值范围："CREATED_TIME"：依据应用的创建时间排序。 "APPLICATION_SIZE"：依据应用的大小排序。默认按应用的创建时间排序。
        :type OrderField: str
        :param _Order: 输出应用列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :type Order: str
        """
        self._ApplicationIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._OrderField = None
        self._Order = None

    @property
    def ApplicationIds(self):
        r"""应用id列表。单次请求数量上限为100个。
        :rtype: list of str
        """
        return self._ApplicationIds

    @ApplicationIds.setter
    def ApplicationIds(self, ApplicationIds):
        self._ApplicationIds = ApplicationIds

    @property
    def Filters(self):
        r"""过滤器，跟ApplicationIds不能共用，支持的filter主要有：application-id: 精确匹配;scene-id: 精确匹配，通过调用接口 [DescribeScenes](https://cloud.tencent.com/document/api/1721/101608)获取;application-name: 模糊匹配;application-type: 精确匹配，枚举类型如下：PUBLIC_APPLICATION（公共应用）/ PRIVATE_APPLICATION（自定义应用）/ COMMUNITY_APPLICATION（社区应用）;
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，不得小于0，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回量，不得大于100，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderField(self):
        r"""应用列表排序的依据字段。取值范围："CREATED_TIME"：依据应用的创建时间排序。 "APPLICATION_SIZE"：依据应用的大小排序。默认按应用的创建时间排序。
        :rtype: str
        """
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def Order(self):
        r"""输出应用列表的排列顺序。取值范围："ASC"：升序排列。 "DESC"：降序排列。默认按降序排列。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._ApplicationIds = params.get("ApplicationIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderField = params.get("OrderField")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApplicationsResponse(AbstractModel):
    r"""DescribeApplications返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 应用总数
        :type TotalCount: int
        :param _ApplicationSet: 分页返回的应用列表
        :type ApplicationSet: list of ApplicationInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ApplicationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""应用总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApplicationSet(self):
        r"""分页返回的应用列表
        :rtype: list of ApplicationInfo
        """
        return self._ApplicationSet

    @ApplicationSet.setter
    def ApplicationSet(self, ApplicationSet):
        self._ApplicationSet = ApplicationSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApplicationSet") is not None:
            self._ApplicationSet = []
            for item in params.get("ApplicationSet"):
                obj = ApplicationInfo()
                obj._deserialize(item)
                self._ApplicationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeployTemplatesRequest(AbstractModel):
    r"""DescribeDeployTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelId: 模型ID
        :type ModelId: str
        """
        self._ModelId = None

    @property
    def ModelId(self):
        r"""模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployTemplatesResponse(AbstractModel):
    r"""DescribeDeployTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateSet: 模板列表
        :type TemplateSet: list of TemplateDetail
        :param _EngineTypes: 支持的推理引擎
        :type EngineTypes: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TemplateSet = None
        self._EngineTypes = None
        self._RequestId = None

    @property
    def TemplateSet(self):
        r"""模板列表
        :rtype: list of TemplateDetail
        """
        return self._TemplateSet

    @TemplateSet.setter
    def TemplateSet(self, TemplateSet):
        self._TemplateSet = TemplateSet

    @property
    def EngineTypes(self):
        r"""支持的推理引擎
        :rtype: list of str
        """
        return self._EngineTypes

    @EngineTypes.setter
    def EngineTypes(self, EngineTypes):
        self._EngineTypes = EngineTypes

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TemplateSet") is not None:
            self._TemplateSet = []
            for item in params.get("TemplateSet"):
                obj = TemplateDetail()
                obj._deserialize(item)
                self._TemplateSet.append(obj)
        self._EngineTypes = params.get("EngineTypes")
        self._RequestId = params.get("RequestId")


class DescribeInstanceNetworkStatusRequest(AbstractModel):
    r"""DescribeInstanceNetworkStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID数组，单次请求最多不超过100个实例；实例ID通过调用接口[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612)获取。
        :type InstanceIds: list of str
        """
        self._InstanceIds = None

    @property
    def InstanceIds(self):
        r"""实例ID数组，单次请求最多不超过100个实例；实例ID通过调用接口[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612)获取。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceNetworkStatusResponse(AbstractModel):
    r"""DescribeInstanceNetworkStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询结果集长度
        :type TotalCount: int
        :param _NetworkStatusSet: 查询结果集
        :type NetworkStatusSet: list of NetworkStatus
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._NetworkStatusSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""查询结果集长度
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NetworkStatusSet(self):
        r"""查询结果集
        :rtype: list of NetworkStatus
        """
        return self._NetworkStatusSet

    @NetworkStatusSet.setter
    def NetworkStatusSet(self, NetworkStatusSet):
        self._NetworkStatusSet = NetworkStatusSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NetworkStatusSet") is not None:
            self._NetworkStatusSet = []
            for item in params.get("NetworkStatusSet"):
                obj = NetworkStatus()
                obj._deserialize(item)
                self._NetworkStatusSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    r"""DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例元组，数量上限100
        :type InstanceIds: list of str
        :param _Filters: 描述键值对过滤器，用于条件过滤查询。目前支持的过滤器有： instance-id，实例id； instance-state，实例状态：RUNNING，PENDING，STOPPED，ARREARS，STOPPED_NO_CHARGE； charge-type，付费方式：PREPAID_BY_MONTH，POSTPAID_BY_HOUR； public-ip-address，公网IP过滤
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0，不得大于100
        :type Offset: int
        :param _Limit: 返回量，默认为20，不能小于0
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        r"""实例元组，数量上限100
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        r"""描述键值对过滤器，用于条件过滤查询。目前支持的过滤器有： instance-id，实例id； instance-state，实例状态：RUNNING，PENDING，STOPPED，ARREARS，STOPPED_NO_CHARGE； charge-type，付费方式：PREPAID_BY_MONTH，POSTPAID_BY_HOUR； public-ip-address，公网IP过滤
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，默认为0，不得大于100
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回量，默认为20，不能小于0
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
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
        


class DescribeInstancesResponse(AbstractModel):
    r"""DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 实例总数

        :type TotalCount: int
        :param _InstanceSet: 分页实例详情

        :type InstanceSet: list of Instance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""实例总数

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        r"""分页实例详情

        :rtype: list of Instance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
        self._RequestId = params.get("RequestId")


class DescribeModelsRequest(AbstractModel):
    r"""DescribeModels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelIds: 模型id
        :type ModelIds: list of str
        :param _Filters: 过滤器。Name的可选值有scene-id
        :type Filters: list of Filter
        :param _Offset: 偏移量，不得小于0，默认为0
        :type Offset: int
        :param _Limit: 返回量，不得大于100，默认为20
        :type Limit: int
        """
        self._ModelIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ModelIds(self):
        r"""模型id
        :rtype: list of str
        """
        return self._ModelIds

    @ModelIds.setter
    def ModelIds(self, ModelIds):
        self._ModelIds = ModelIds

    @property
    def Filters(self):
        r"""过滤器。Name的可选值有scene-id
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量，不得小于0，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回量，不得大于100，默认为20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ModelIds = params.get("ModelIds")
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
        


class DescribeModelsResponse(AbstractModel):
    r"""DescribeModels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 模型总数
        :type TotalCount: int
        :param _ModelSet: 分页返回的模型列表
        :type ModelSet: list of ModelDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ModelSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""模型总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ModelSet(self):
        r"""分页返回的模型列表
        :rtype: list of ModelDetail
        """
        return self._ModelSet

    @ModelSet.setter
    def ModelSet(self, ModelSet):
        self._ModelSet = ModelSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ModelSet") is not None:
            self._ModelSet = []
            for item in params.get("ModelSet"):
                obj = ModelDetail()
                obj._deserialize(item)
                self._ModelSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMuskPromptsRequest(AbstractModel):
    r"""DescribeMuskPrompts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkgroupId: workgroup id
        :type WorkgroupId: str
        :param _WorkflowId: workflow id
        :type WorkflowId: str
        :param _Offset: offset 
        :type Offset: int
        :param _Limit: limit
        :type Limit: int
        :param _Filters: 过滤参数 支持过滤的键值： PromptId，Status
        :type Filters: list of Filter
        """
        self._WorkgroupId = None
        self._WorkflowId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def WorkgroupId(self):
        r"""workgroup id
        :rtype: str
        """
        return self._WorkgroupId

    @WorkgroupId.setter
    def WorkgroupId(self, WorkgroupId):
        self._WorkgroupId = WorkgroupId

    @property
    def WorkflowId(self):
        r"""workflow id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def Offset(self):
        r"""offset 
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤参数 支持过滤的键值： PromptId，Status
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._WorkgroupId = params.get("WorkgroupId")
        self._WorkflowId = params.get("WorkflowId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMuskPromptsResponse(AbstractModel):
    r"""DescribeMuskPrompts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: total count
        :type TotalCount: int
        :param _MuskPromptInfos: prompt列表详情
        :type MuskPromptInfos: list of MuskPromptInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MuskPromptInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""total count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MuskPromptInfos(self):
        r"""prompt列表详情
        :rtype: list of MuskPromptInfo
        """
        return self._MuskPromptInfos

    @MuskPromptInfos.setter
    def MuskPromptInfos(self, MuskPromptInfos):
        self._MuskPromptInfos = MuskPromptInfos

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("MuskPromptInfos") is not None:
            self._MuskPromptInfos = []
            for item in params.get("MuskPromptInfos"):
                obj = MuskPromptInfo()
                obj._deserialize(item)
                self._MuskPromptInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    r"""DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    r"""DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegionSet: 地域列表
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegionSet = None
        self._RequestId = None

    @property
    def RegionSet(self):
        r"""地域列表
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    r"""DescribeScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneIds: 场景id列表，单次能查询100个场景id
        :type SceneIds: list of str
        """
        self._SceneIds = None

    @property
    def SceneIds(self):
        r"""场景id列表，单次能查询100个场景id
        :rtype: list of str
        """
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScenesResponse(AbstractModel):
    r"""DescribeScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneSet: 场景详情
        :type SceneSet: list of SceneInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SceneSet = None
        self._RequestId = None

    @property
    def SceneSet(self):
        r"""场景详情
        :rtype: list of SceneInfo
        """
        return self._SceneSet

    @SceneSet.setter
    def SceneSet(self, SceneSet):
        self._SceneSet = SceneSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SceneSet") is not None:
            self._SceneSet = []
            for item in params.get("SceneSet"):
                obj = SceneInfo()
                obj._deserialize(item)
                self._SceneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceLoginSettingsRequest(AbstractModel):
    r"""DescribeServiceLoginSettings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID通过调用接口[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612)获取。
        :type InstanceId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        """
        self._InstanceId = None
        self._ServiceName = None

    @property
    def InstanceId(self):
        r"""实例ID通过调用接口[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612)获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ServiceName(self):
        r"""服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceLoginSettingsResponse(AbstractModel):
    r"""DescribeServiceLoginSettings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoginSettings: 服务登录配置详情
        :type LoginSettings: list of LoginSetting
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoginSettings = None
        self._RequestId = None

    @property
    def LoginSettings(self):
        r"""服务登录配置详情
        :rtype: list of LoginSetting
        """
        return self._LoginSettings

    @LoginSettings.setter
    def LoginSettings(self, LoginSettings):
        self._LoginSettings = LoginSettings

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("LoginSettings") is not None:
            self._LoginSettings = []
            for item in params.get("LoginSettings"):
                obj = LoginSetting()
                obj._deserialize(item)
                self._LoginSettings.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServicesRequest(AbstractModel):
    r"""DescribeServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceIds: 服务列表
        :type ServiceIds: list of str
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._ServiceIds = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceIds(self):
        r"""服务列表
        :rtype: list of str
        """
        return self._ServiceIds

    @ServiceIds.setter
    def ServiceIds(self, ServiceIds):
        self._ServiceIds = ServiceIds

    @property
    def Limit(self):
        r"""分页大小
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceIds = params.get("ServiceIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServicesResponse(AbstractModel):
    r"""DescribeServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _ServiceInfoSet: 服务列表
        :type ServiceInfoSet: list of ServiceDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ServiceInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceInfoSet(self):
        r"""服务列表
        :rtype: list of ServiceDetail
        """
        return self._ServiceInfoSet

    @ServiceInfoSet.setter
    def ServiceInfoSet(self, ServiceInfoSet):
        self._ServiceInfoSet = ServiceInfoSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceInfoSet") is not None:
            self._ServiceInfoSet = []
            for item in params.get("ServiceInfoSet"):
                obj = ServiceDetail()
                obj._deserialize(item)
                self._ServiceInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class EnvParam(AbstractModel):
    r"""环境变量键值对

    """

    def __init__(self):
        r"""
        :param _Name: 环境变量名
        :type Name: str
        :param _Value: 环境变量值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""环境变量名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""环境变量值
        :rtype: str
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
        


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    - 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    - 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

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
        r"""需要过滤的字段。	
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""字段的过滤值。
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
        


class HiCacheInfo(AbstractModel):
    r"""HiCache信息

    """

    def __init__(self):
        r"""
        :param _HiCacheLevel: HiCache缓存等级
        :type HiCacheLevel: str
        """
        self._HiCacheLevel = None

    @property
    def HiCacheLevel(self):
        r"""HiCache缓存等级
        :rtype: str
        """
        return self._HiCacheLevel

    @HiCacheLevel.setter
    def HiCacheLevel(self, HiCacheLevel):
        self._HiCacheLevel = HiCacheLevel


    def _deserialize(self, params):
        self._HiCacheLevel = params.get("HiCacheLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HyperParam(AbstractModel):
    r"""描述了服务的超参数配置

    """

    def __init__(self):
        r"""
        :param _HiCache: HiCache缓存
        :type HiCache: :class:`tencentcloud.hai.v20230812.models.HiCacheInfo`
        """
        self._HiCache = None

    @property
    def HiCache(self):
        r"""HiCache缓存
        :rtype: :class:`tencentcloud.hai.v20230812.models.HiCacheInfo`
        """
        return self._HiCache

    @HiCache.setter
    def HiCache(self, HiCache):
        self._HiCache = HiCache


    def _deserialize(self, params):
        if params.get("HiCache") is not None:
            self._HiCache = HiCacheInfo()
            self._HiCache._deserialize(params.get("HiCache"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageInfo(AbstractModel):
    r"""镜像相关配置

    """

    def __init__(self):
        r"""
        :param _ImageRegistryUrl: tcr仓库地址
        :type ImageRegistryUrl: str
        """
        self._ImageRegistryUrl = None

    @property
    def ImageRegistryUrl(self):
        r"""tcr仓库地址
        :rtype: str
        """
        return self._ImageRegistryUrl

    @ImageRegistryUrl.setter
    def ImageRegistryUrl(self, ImageRegistryUrl):
        self._ImageRegistryUrl = ImageRegistryUrl


    def _deserialize(self, params):
        self._ImageRegistryUrl = params.get("ImageRegistryUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRunInstancesRequest(AbstractModel):
    r"""InquirePriceRunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID通过调用接口[DescribeApplications](https://cloud.tencent.com/document/api/1721/101609)获取。
        :type ApplicationId: str
        :param _BundleType: 算力套餐类型, 枚举：XL,XL_2X, 3XL, 3XL_2X, 4XL, 24GB_A.
        :type BundleType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        :param _InstanceCount: 购买实例数量，单次请求实例数量上限为10。
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称，名称长度限制为128个字符。
        :type InstanceName: str
        :param _ClientToken: 幂等请求token
        :type ClientToken: str
        :param _DryRun: DryRun为True就是只验接口连通性，默认为False
        :type DryRun: bool
        :param _InstanceChargeType: 付费方式，POSTPAID_BY_HOUR按量后付费，PREPAID_BY_MONTH预付费按月，PREPAID_BY_DAY预付费按天
        :type InstanceChargeType: str
        :param _InstanceChargePrepaid: 预付费参数
        :type InstanceChargePrepaid: :class:`tencentcloud.hai.v20230812.models.InstanceChargePrepaid`
        """
        self._ApplicationId = None
        self._BundleType = None
        self._SystemDisk = None
        self._InstanceCount = None
        self._InstanceName = None
        self._ClientToken = None
        self._DryRun = None
        self._InstanceChargeType = None
        self._InstanceChargePrepaid = None

    @property
    def ApplicationId(self):
        r"""应用ID通过调用接口[DescribeApplications](https://cloud.tencent.com/document/api/1721/101609)获取。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BundleType(self):
        r"""算力套餐类型, 枚举：XL,XL_2X, 3XL, 3XL_2X, 4XL, 24GB_A.
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def SystemDisk(self):
        r"""实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceCount(self):
        r"""购买实例数量，单次请求实例数量上限为10。
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        r"""实例显示名称，名称长度限制为128个字符。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClientToken(self):
        r"""幂等请求token
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""DryRun为True就是只验接口连通性，默认为False
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def InstanceChargeType(self):
        r"""付费方式，POSTPAID_BY_HOUR按量后付费，PREPAID_BY_MONTH预付费按月，PREPAID_BY_DAY预付费按天
        :rtype: str
        """
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceChargePrepaid(self):
        r"""预付费参数
        :rtype: :class:`tencentcloud.hai.v20230812.models.InstanceChargePrepaid`
        """
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._BundleType = params.get("BundleType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        self._InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRunInstancesResponse(AbstractModel):
    r"""InquirePriceRunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 发货参数对应的价格组合，当DryRun=True，会返回空
        :type Price: :class:`tencentcloud.hai.v20230812.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""发货参数对应的价格组合，当DryRun=True，会返回空
        :rtype: :class:`tencentcloud.hai.v20230812.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InquirePriceUpdateServiceConfigsRequest(AbstractModel):
    r"""InquirePriceUpdateServiceConfigs请求参数结构体

    """


class InquirePriceUpdateServiceConfigsResponse(AbstractModel):
    r"""InquirePriceUpdateServiceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 发货参数对应的价格组合。
        :type Price: :class:`tencentcloud.hai.v20230812.models.ServicePriceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""发货参数对应的价格组合。
        :rtype: :class:`tencentcloud.hai.v20230812.models.ServicePriceDetail`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self._Price = ServicePriceDetail()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class Instance(AbstractModel):
    r"""实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _InstanceState: 实例状态：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
ARREARS：表示待回收
STOPPED_NO_CHARGE：表示关机不收费
TERMINATING：表示销毁中
TERMINATED：表示已销毁
        :type InstanceState: str
        :param _ApplicationName: 应用名称

        :type ApplicationName: str
        :param _BundleName: 算力套餐名称

        :type BundleName: str
        :param _GPUCount: 实例所包含的GPU卡数
        :type GPUCount: int
        :param _GPUPerformance: 算力

        :type GPUPerformance: str
        :param _GPUMemory: 显存，单位：GB
        :type GPUMemory: str
        :param _CPU: CPU核数，单位：核
        :type CPU: str
        :param _Memory: 内存，单位：GB

        :type Memory: str
        :param _SystemDisk: 系统盘数据
        :type SystemDisk: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        :param _PrivateIpAddresses: 内网ip地址
        :type PrivateIpAddresses: list of str
        :param _PublicIpAddresses: 公网ip地址
        :type PublicIpAddresses: list of str
        :param _SecurityGroupIds: 安全组ID

        :type SecurityGroupIds: list of str
        :param _LatestOperation: 实例最新操作
        :type LatestOperation: str
        :param _LatestOperationState: 实例最新操作状态：
SUCCESS：表示操作成功
OPERATING：表示操作执行中
FAILED：表示操作失败

        :type LatestOperationState: str
        :param _CreateTime: 实例创建时间，时间格式："YYYY-MM-DD HH:MM:SS"
        :type CreateTime: str
        :param _MaxOutBandwidth: 公网出带宽上限，默认10Mbps，单位：Mbps
        :type MaxOutBandwidth: str
        :param _MaxFreeTraffic: 每月免费流量，默认500G，单位：GB
        :type MaxFreeTraffic: str
        :param _ConfigurationEnvironment: 应用配置环境
        :type ConfigurationEnvironment: str
        :param _LoginServices: 实例包含的登录服务详情
        :type LoginServices: list of LoginService
        :param _OSType: 应用服务的操作系统类型；参数：linux、windows
        :type OSType: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceState = None
        self._ApplicationName = None
        self._BundleName = None
        self._GPUCount = None
        self._GPUPerformance = None
        self._GPUMemory = None
        self._CPU = None
        self._Memory = None
        self._SystemDisk = None
        self._PrivateIpAddresses = None
        self._PublicIpAddresses = None
        self._SecurityGroupIds = None
        self._LatestOperation = None
        self._LatestOperationState = None
        self._CreateTime = None
        self._MaxOutBandwidth = None
        self._MaxFreeTraffic = None
        self._ConfigurationEnvironment = None
        self._LoginServices = None
        self._OSType = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceState(self):
        r"""实例状态：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
ARREARS：表示待回收
STOPPED_NO_CHARGE：表示关机不收费
TERMINATING：表示销毁中
TERMINATED：表示已销毁
        :rtype: str
        """
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def ApplicationName(self):
        r"""应用名称

        :rtype: str
        """
        return self._ApplicationName

    @ApplicationName.setter
    def ApplicationName(self, ApplicationName):
        self._ApplicationName = ApplicationName

    @property
    def BundleName(self):
        r"""算力套餐名称

        :rtype: str
        """
        return self._BundleName

    @BundleName.setter
    def BundleName(self, BundleName):
        self._BundleName = BundleName

    @property
    def GPUCount(self):
        r"""实例所包含的GPU卡数
        :rtype: int
        """
        return self._GPUCount

    @GPUCount.setter
    def GPUCount(self, GPUCount):
        self._GPUCount = GPUCount

    @property
    def GPUPerformance(self):
        r"""算力

        :rtype: str
        """
        return self._GPUPerformance

    @GPUPerformance.setter
    def GPUPerformance(self, GPUPerformance):
        self._GPUPerformance = GPUPerformance

    @property
    def GPUMemory(self):
        r"""显存，单位：GB
        :rtype: str
        """
        return self._GPUMemory

    @GPUMemory.setter
    def GPUMemory(self, GPUMemory):
        self._GPUMemory = GPUMemory

    @property
    def CPU(self):
        r"""CPU核数，单位：核
        :rtype: str
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""内存，单位：GB

        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def SystemDisk(self):
        r"""系统盘数据
        :rtype: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def PrivateIpAddresses(self):
        r"""内网ip地址
        :rtype: list of str
        """
        return self._PrivateIpAddresses

    @PrivateIpAddresses.setter
    def PrivateIpAddresses(self, PrivateIpAddresses):
        self._PrivateIpAddresses = PrivateIpAddresses

    @property
    def PublicIpAddresses(self):
        r"""公网ip地址
        :rtype: list of str
        """
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses

    @property
    def SecurityGroupIds(self):
        r"""安全组ID

        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def LatestOperation(self):
        r"""实例最新操作
        :rtype: str
        """
        return self._LatestOperation

    @LatestOperation.setter
    def LatestOperation(self, LatestOperation):
        self._LatestOperation = LatestOperation

    @property
    def LatestOperationState(self):
        r"""实例最新操作状态：
SUCCESS：表示操作成功
OPERATING：表示操作执行中
FAILED：表示操作失败

        :rtype: str
        """
        return self._LatestOperationState

    @LatestOperationState.setter
    def LatestOperationState(self, LatestOperationState):
        self._LatestOperationState = LatestOperationState

    @property
    def CreateTime(self):
        r"""实例创建时间，时间格式："YYYY-MM-DD HH:MM:SS"
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxOutBandwidth(self):
        r"""公网出带宽上限，默认10Mbps，单位：Mbps
        :rtype: str
        """
        return self._MaxOutBandwidth

    @MaxOutBandwidth.setter
    def MaxOutBandwidth(self, MaxOutBandwidth):
        self._MaxOutBandwidth = MaxOutBandwidth

    @property
    def MaxFreeTraffic(self):
        r"""每月免费流量，默认500G，单位：GB
        :rtype: str
        """
        return self._MaxFreeTraffic

    @MaxFreeTraffic.setter
    def MaxFreeTraffic(self, MaxFreeTraffic):
        self._MaxFreeTraffic = MaxFreeTraffic

    @property
    def ConfigurationEnvironment(self):
        r"""应用配置环境
        :rtype: str
        """
        return self._ConfigurationEnvironment

    @ConfigurationEnvironment.setter
    def ConfigurationEnvironment(self, ConfigurationEnvironment):
        self._ConfigurationEnvironment = ConfigurationEnvironment

    @property
    def LoginServices(self):
        r"""实例包含的登录服务详情
        :rtype: list of LoginService
        """
        return self._LoginServices

    @LoginServices.setter
    def LoginServices(self, LoginServices):
        self._LoginServices = LoginServices

    @property
    def OSType(self):
        r"""应用服务的操作系统类型；参数：linux、windows
        :rtype: str
        """
        return self._OSType

    @OSType.setter
    def OSType(self, OSType):
        self._OSType = OSType


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceState = params.get("InstanceState")
        self._ApplicationName = params.get("ApplicationName")
        self._BundleName = params.get("BundleName")
        self._GPUCount = params.get("GPUCount")
        self._GPUPerformance = params.get("GPUPerformance")
        self._GPUMemory = params.get("GPUMemory")
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._PrivateIpAddresses = params.get("PrivateIpAddresses")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        self._LatestOperation = params.get("LatestOperation")
        self._LatestOperationState = params.get("LatestOperationState")
        self._CreateTime = params.get("CreateTime")
        self._MaxOutBandwidth = params.get("MaxOutBandwidth")
        self._MaxFreeTraffic = params.get("MaxFreeTraffic")
        self._ConfigurationEnvironment = params.get("ConfigurationEnvironment")
        if params.get("LoginServices") is not None:
            self._LoginServices = []
            for item in params.get("LoginServices"):
                obj = LoginService()
                obj._deserialize(item)
                self._LoginServices.append(obj)
        self._OSType = params.get("OSType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceChargePrepaid(AbstractModel):
    r"""实例预付费入参

    """

    def __init__(self):
        r"""
        :param _Period: 时长，默认值：1
        :type Period: int
        :param _RenewFlag: 续费标志可选参数：
NOTIFY_AND_MANUAL_RENEW：表示默认状态(用户未设置，即初始状态：若用户有预付费不停服特权，也会对该值进行自动续费)
NOTIFY_AND_AUTO_RENEW：表示自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：表示明确不自动续费(用户设置)
默认值：NOTIFY_AND_MANUAL_RENEW

        :type RenewFlag: str
        :param _TimeUnit: 时长单位，枚举： MONTH, DAY, HOUR；释义：月，日，小时
        :type TimeUnit: str
        """
        self._Period = None
        self._RenewFlag = None
        self._TimeUnit = None

    @property
    def Period(self):
        r"""时长，默认值：1
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RenewFlag(self):
        r"""续费标志可选参数：
NOTIFY_AND_MANUAL_RENEW：表示默认状态(用户未设置，即初始状态：若用户有预付费不停服特权，也会对该值进行自动续费)
NOTIFY_AND_AUTO_RENEW：表示自动续费
DISABLE_NOTIFY_AND_MANUAL_RENEW：表示明确不自动续费(用户设置)
默认值：NOTIFY_AND_MANUAL_RENEW

        :rtype: str
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeUnit(self):
        r"""时长单位，枚举： MONTH, DAY, HOUR；释义：月，日，小时
        :rtype: str
        """
        return self._TimeUnit

    @TimeUnit.setter
    def TimeUnit(self, TimeUnit):
        self._TimeUnit = TimeUnit


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RenewFlag = params.get("RenewFlag")
        self._TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    r"""套餐价格

    """

    def __init__(self):
        r"""
        :param _UnitPrice: 原单价，元
        :type UnitPrice: float
        :param _DiscountUnitPrice: 折扣后单价，元
        :type DiscountUnitPrice: float
        :param _Discount: 折扣
        :type Discount: float
        :param _ChargeUnit: 单位：时/月

        :type ChargeUnit: str
        :param _Amount: 商品数量
        :type Amount: int
        :param _OriginPrice: 原价
        :type OriginPrice: float
        :param _DiscountPrice: 折扣价
        :type DiscountPrice: float
        """
        self._UnitPrice = None
        self._DiscountUnitPrice = None
        self._Discount = None
        self._ChargeUnit = None
        self._Amount = None
        self._OriginPrice = None
        self._DiscountPrice = None

    @property
    def UnitPrice(self):
        r"""原单价，元
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def DiscountUnitPrice(self):
        r"""折扣后单价，元
        :rtype: float
        """
        return self._DiscountUnitPrice

    @DiscountUnitPrice.setter
    def DiscountUnitPrice(self, DiscountUnitPrice):
        self._DiscountUnitPrice = DiscountUnitPrice

    @property
    def Discount(self):
        r"""折扣
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def ChargeUnit(self):
        r"""单位：时/月

        :rtype: str
        """
        return self._ChargeUnit

    @ChargeUnit.setter
    def ChargeUnit(self, ChargeUnit):
        self._ChargeUnit = ChargeUnit

    @property
    def Amount(self):
        r"""商品数量
        :rtype: int
        """
        return self._Amount

    @Amount.setter
    def Amount(self, Amount):
        self._Amount = Amount

    @property
    def OriginPrice(self):
        r"""原价
        :rtype: float
        """
        return self._OriginPrice

    @OriginPrice.setter
    def OriginPrice(self, OriginPrice):
        self._OriginPrice = OriginPrice

    @property
    def DiscountPrice(self):
        r"""折扣价
        :rtype: float
        """
        return self._DiscountPrice

    @DiscountPrice.setter
    def DiscountPrice(self, DiscountPrice):
        self._DiscountPrice = DiscountPrice


    def _deserialize(self, params):
        self._UnitPrice = params.get("UnitPrice")
        self._DiscountUnitPrice = params.get("DiscountUnitPrice")
        self._Discount = params.get("Discount")
        self._ChargeUnit = params.get("ChargeUnit")
        self._Amount = params.get("Amount")
        self._OriginPrice = params.get("OriginPrice")
        self._DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPriceDetail(AbstractModel):
    r"""分实例价格

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _InstancePrice: 实例价格详情
        :type InstancePrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _CloudDiskPrice: 磁盘价格详情
        :type CloudDiskPrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _InstanceTotalPrice: 该实例的总价钱
        :type InstanceTotalPrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        self._InstanceId = None
        self._InstancePrice = None
        self._CloudDiskPrice = None
        self._InstanceTotalPrice = None

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstancePrice(self):
        r"""实例价格详情
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def CloudDiskPrice(self):
        r"""磁盘价格详情
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._CloudDiskPrice

    @CloudDiskPrice.setter
    def CloudDiskPrice(self, CloudDiskPrice):
        self._CloudDiskPrice = CloudDiskPrice

    @property
    def InstanceTotalPrice(self):
        r"""该实例的总价钱
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._InstanceTotalPrice

    @InstanceTotalPrice.setter
    def InstanceTotalPrice(self, InstanceTotalPrice):
        self._InstanceTotalPrice = InstanceTotalPrice


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("CloudDiskPrice") is not None:
            self._CloudDiskPrice = ItemPrice()
            self._CloudDiskPrice._deserialize(params.get("CloudDiskPrice"))
        if params.get("InstanceTotalPrice") is not None:
            self._InstanceTotalPrice = ItemPrice()
            self._InstanceTotalPrice._deserialize(params.get("InstanceTotalPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginService(AbstractModel):
    r"""登录服务详情

    """

    def __init__(self):
        r"""
        :param _ServiceName: 登录方式名称
        :type ServiceName: str
        """
        self._ServiceName = None

    @property
    def ServiceName(self):
        r"""登录方式名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoginSetting(AbstractModel):
    r"""某服务的登录配置

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _Url: 服务登录url
        :type Url: str
        """
        self._ServiceName = None
        self._Url = None

    @property
    def ServiceName(self):
        r"""服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Url(self):
        r"""服务登录url
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelDetail(AbstractModel):
    r"""模型详情

    """

    def __init__(self):
        r"""
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _Description: 应用描述	
        :type Description: str
        :param _CommunityUrl: 官方社区链接	
        :type CommunityUrl: str
        :param _GuideUrl: 最佳实践链接
        :type GuideUrl: str
        :param _ModelState: 模型状态
        :type ModelState: str
        :param _Tags: 应用对应的标签，如机器学习
        :type Tags: list of str
        :param _ConfigEnvironment: 配置环境
        :type ConfigEnvironment: str
        """
        self._ModelName = None
        self._ModelId = None
        self._Description = None
        self._CommunityUrl = None
        self._GuideUrl = None
        self._ModelState = None
        self._Tags = None
        self._ConfigEnvironment = None

    @property
    def ModelName(self):
        r"""模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ModelId(self):
        r"""模型ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Description(self):
        r"""应用描述	
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommunityUrl(self):
        r"""官方社区链接	
        :rtype: str
        """
        return self._CommunityUrl

    @CommunityUrl.setter
    def CommunityUrl(self, CommunityUrl):
        self._CommunityUrl = CommunityUrl

    @property
    def GuideUrl(self):
        r"""最佳实践链接
        :rtype: str
        """
        return self._GuideUrl

    @GuideUrl.setter
    def GuideUrl(self, GuideUrl):
        self._GuideUrl = GuideUrl

    @property
    def ModelState(self):
        r"""模型状态
        :rtype: str
        """
        return self._ModelState

    @ModelState.setter
    def ModelState(self, ModelState):
        self._ModelState = ModelState

    @property
    def Tags(self):
        r"""应用对应的标签，如机器学习
        :rtype: list of str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ConfigEnvironment(self):
        r"""配置环境
        :rtype: str
        """
        return self._ConfigEnvironment

    @ConfigEnvironment.setter
    def ConfigEnvironment(self, ConfigEnvironment):
        self._ConfigEnvironment = ConfigEnvironment


    def _deserialize(self, params):
        self._ModelName = params.get("ModelName")
        self._ModelId = params.get("ModelId")
        self._Description = params.get("Description")
        self._CommunityUrl = params.get("CommunityUrl")
        self._GuideUrl = params.get("GuideUrl")
        self._ModelState = params.get("ModelState")
        self._Tags = params.get("Tags")
        self._ConfigEnvironment = params.get("ConfigEnvironment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MuskPromptInfo(AbstractModel):
    r"""musk prompt详情

    """

    def __init__(self):
        r"""
        :param _WorkflowId: workflow id
        :type WorkflowId: str
        :param _WorkgroupId: workgroup id
        :type WorkgroupId: str
        :param _PromptId: prompt id
        :type PromptId: str
        :param _OutputResource: 生成的内容
        :type OutputResource: list of str
        :param _Status: prompt status 
0: 执行中
1: 执行成功
2: 执行失败
        :type Status: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Cost: 任务执行耗时，单位毫秒
        :type Cost: int
        :param _ErrorMessage: 任务执行失败错误信息
        :type ErrorMessage: str
        """
        self._WorkflowId = None
        self._WorkgroupId = None
        self._PromptId = None
        self._OutputResource = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Cost = None
        self._ErrorMessage = None

    @property
    def WorkflowId(self):
        r"""workflow id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkgroupId(self):
        r"""workgroup id
        :rtype: str
        """
        return self._WorkgroupId

    @WorkgroupId.setter
    def WorkgroupId(self, WorkgroupId):
        self._WorkgroupId = WorkgroupId

    @property
    def PromptId(self):
        r"""prompt id
        :rtype: str
        """
        return self._PromptId

    @PromptId.setter
    def PromptId(self, PromptId):
        self._PromptId = PromptId

    @property
    def OutputResource(self):
        r"""生成的内容
        :rtype: list of str
        """
        return self._OutputResource

    @OutputResource.setter
    def OutputResource(self, OutputResource):
        self._OutputResource = OutputResource

    @property
    def Status(self):
        r"""prompt status 
0: 执行中
1: 执行成功
2: 执行失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Cost(self):
        r"""任务执行耗时，单位毫秒
        :rtype: int
        """
        return self._Cost

    @Cost.setter
    def Cost(self, Cost):
        self._Cost = Cost

    @property
    def ErrorMessage(self):
        r"""任务执行失败错误信息
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage


    def _deserialize(self, params):
        self._WorkflowId = params.get("WorkflowId")
        self._WorkgroupId = params.get("WorkgroupId")
        self._PromptId = params.get("PromptId")
        self._OutputResource = params.get("OutputResource")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Cost = params.get("Cost")
        self._ErrorMessage = params.get("ErrorMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkSetting(AbstractModel):
    r"""推理集群的网络设置

    """

    def __init__(self):
        r"""
        :param _PublicEndpointEnable: 公网访问
        :type PublicEndpointEnable: bool
        :param _VpcEndpointEnable: 内网访问
        :type VpcEndpointEnable: bool
        :param _VpcId: vpc内网ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._PublicEndpointEnable = None
        self._VpcEndpointEnable = None
        self._VpcId = None
        self._SubnetId = None

    @property
    def PublicEndpointEnable(self):
        r"""公网访问
        :rtype: bool
        """
        return self._PublicEndpointEnable

    @PublicEndpointEnable.setter
    def PublicEndpointEnable(self, PublicEndpointEnable):
        self._PublicEndpointEnable = PublicEndpointEnable

    @property
    def VpcEndpointEnable(self):
        r"""内网访问
        :rtype: bool
        """
        return self._VpcEndpointEnable

    @VpcEndpointEnable.setter
    def VpcEndpointEnable(self, VpcEndpointEnable):
        self._VpcEndpointEnable = VpcEndpointEnable

    @property
    def VpcId(self):
        r"""vpc内网ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        r"""子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._PublicEndpointEnable = params.get("PublicEndpointEnable")
        self._VpcEndpointEnable = params.get("VpcEndpointEnable")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkStatus(AbstractModel):
    r"""HAI 实例的网络配置和消耗情况

    """

    def __init__(self):
        r"""
        :param _InstanceId: HAI 的实例 ID
        :type InstanceId: str
        :param _AddressIp: 公网 IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIp: str
        :param _Bandwidth: 出带宽上限，单位Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type Bandwidth: int
        :param _TotalTrafficAmount: 流量包总量，单位GB
        :type TotalTrafficAmount: float
        :param _RemainingTrafficAmount: 流量包剩余量，单位GB
        :type RemainingTrafficAmount: float
        """
        self._InstanceId = None
        self._AddressIp = None
        self._Bandwidth = None
        self._TotalTrafficAmount = None
        self._RemainingTrafficAmount = None

    @property
    def InstanceId(self):
        r"""HAI 的实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AddressIp(self):
        r"""公网 IP 地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddressIp

    @AddressIp.setter
    def AddressIp(self, AddressIp):
        self._AddressIp = AddressIp

    @property
    def Bandwidth(self):
        r"""出带宽上限，单位Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def TotalTrafficAmount(self):
        r"""流量包总量，单位GB
        :rtype: float
        """
        return self._TotalTrafficAmount

    @TotalTrafficAmount.setter
    def TotalTrafficAmount(self, TotalTrafficAmount):
        self._TotalTrafficAmount = TotalTrafficAmount

    @property
    def RemainingTrafficAmount(self):
        r"""流量包剩余量，单位GB
        :rtype: float
        """
        return self._RemainingTrafficAmount

    @RemainingTrafficAmount.setter
    def RemainingTrafficAmount(self, RemainingTrafficAmount):
        self._RemainingTrafficAmount = RemainingTrafficAmount


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._AddressIp = params.get("AddressIp")
        self._Bandwidth = params.get("Bandwidth")
        self._TotalTrafficAmount = params.get("TotalTrafficAmount")
        self._RemainingTrafficAmount = params.get("RemainingTrafficAmount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    r"""费用数据结构体

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 实例价格信息
        :type InstancePrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _CloudDiskPrice: 云盘价格信息
        :type CloudDiskPrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        :param _PriceDetailSet: 分实例价格
        :type PriceDetailSet: list of ItemPriceDetail
        """
        self._InstancePrice = None
        self._CloudDiskPrice = None
        self._PriceDetailSet = None

    @property
    def InstancePrice(self):
        r"""实例价格信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def CloudDiskPrice(self):
        r"""云盘价格信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._CloudDiskPrice

    @CloudDiskPrice.setter
    def CloudDiskPrice(self, CloudDiskPrice):
        self._CloudDiskPrice = CloudDiskPrice

    @property
    def PriceDetailSet(self):
        r"""分实例价格
        :rtype: list of ItemPriceDetail
        """
        return self._PriceDetailSet

    @PriceDetailSet.setter
    def PriceDetailSet(self, PriceDetailSet):
        self._PriceDetailSet = PriceDetailSet


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = ItemPrice()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("CloudDiskPrice") is not None:
            self._CloudDiskPrice = ItemPrice()
            self._CloudDiskPrice._deserialize(params.get("CloudDiskPrice"))
        if params.get("PriceDetailSet") is not None:
            self._PriceDetailSet = []
            for item in params.get("PriceDetailSet"):
                obj = ItemPriceDetail()
                obj._deserialize(item)
                self._PriceDetailSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    r"""地域列表

    """

    def __init__(self):
        r"""
        :param _Region: 地域
        :type Region: str
        :param _RegionName: 地域名称
        :type RegionName: str
        :param _RegionState: 地域是否可用状态
AVAILABLE：可用

        :type RegionState: str
        :param _ScholarRocketSupportState: 学术加速是否支持：
NO_NEED_SUPPORT表示不需支持；NOT_SUPPORT_YET表示暂未支持；ALREADY_SUPPORT表示已经支持。
        :type ScholarRocketSupportState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None
        self._ScholarRocketSupportState = None

    @property
    def Region(self):
        r"""地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        r"""地域名称
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        r"""地域是否可用状态
AVAILABLE：可用

        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState

    @property
    def ScholarRocketSupportState(self):
        r"""学术加速是否支持：
NO_NEED_SUPPORT表示不需支持；NOT_SUPPORT_YET表示暂未支持；ALREADY_SUPPORT表示已经支持。
        :rtype: str
        """
        return self._ScholarRocketSupportState

    @ScholarRocketSupportState.setter
    def ScholarRocketSupportState(self, ScholarRocketSupportState):
        self._ScholarRocketSupportState = ScholarRocketSupportState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        self._ScholarRocketSupportState = params.get("ScholarRocketSupportState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordRequest(AbstractModel):
    r"""ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param _Password: 实例密码必须8-30位，推荐使用12位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br><li>小写字母：[a-z]</li><br><li>大写字母：[A-Z]</li><br><li>数字：0-9</li><br><li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;'<>,.?/</li>
        :type Password: str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceIds = None
        self._Password = None
        self._DryRun = None

    @property
    def InstanceIds(self):
        r"""实例ID列表
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Password(self):
        r"""实例密码必须8-30位，推荐使用12位以上密码，不能以“/”开头，至少包含以下字符中的三种不同字符，字符种类：<br><li>小写字母：[a-z]</li><br><li>大写字母：[A-Z]</li><br><li>数字：0-9</li><br><li>特殊字符： ()\`\~!@#$%^&\*-+=\_|{}[]:;'<>,.?/</li>
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def DryRun(self):
        r"""默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._Password = params.get("Password")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    r"""ResetInstancesPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: task任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""task任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class ResizeInstanceDiskRequest(AbstractModel):
    r"""ResizeInstanceDisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 需要扩容云盘的HAI实例ID
        :type InstanceId: str
        :param _DiskSize: 扩容云硬盘大小，单位为GB，必须大于当前云硬盘大小。
        :type DiskSize: int
        """
        self._InstanceId = None
        self._DiskSize = None

    @property
    def InstanceId(self):
        r"""需要扩容云盘的HAI实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DiskSize(self):
        r"""扩容云硬盘大小，单位为GB，必须大于当前云硬盘大小。
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResizeInstanceDiskResponse(AbstractModel):
    r"""ResizeInstanceDisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class RunInstancesRequest(AbstractModel):
    r"""RunInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplicationId: 应用ID通过调用接口[DescribeApplications](https://cloud.tencent.com/document/api/1721/101609)获取。
        :type ApplicationId: str
        :param _BundleType: 算力套餐类型, 枚举：XL,XL_2X, 3XL, 3XL_2X, 4XL, 24GB_A
        :type BundleType: str
        :param _SystemDisk: 实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :type SystemDisk: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        :param _InstanceCount: 购买实例数量，单次请求实例数量上限为10.
        :type InstanceCount: int
        :param _InstanceName: 实例显示名称，名称长度限制为128个字符.
        :type InstanceName: str
        :param _ClientToken: 幂等请求的token
        :type ClientToken: str
        :param _DryRun: DryRun为True就是只验接口连通性，默认为False
        :type DryRun: bool
        """
        self._ApplicationId = None
        self._BundleType = None
        self._SystemDisk = None
        self._InstanceCount = None
        self._InstanceName = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def ApplicationId(self):
        r"""应用ID通过调用接口[DescribeApplications](https://cloud.tencent.com/document/api/1721/101609)获取。
        :rtype: str
        """
        return self._ApplicationId

    @ApplicationId.setter
    def ApplicationId(self, ApplicationId):
        self._ApplicationId = ApplicationId

    @property
    def BundleType(self):
        r"""算力套餐类型, 枚举：XL,XL_2X, 3XL, 3XL_2X, 4XL, 24GB_A
        :rtype: str
        """
        return self._BundleType

    @BundleType.setter
    def BundleType(self, BundleType):
        self._BundleType = BundleType

    @property
    def SystemDisk(self):
        r"""实例系统盘配置信息。若不指定该参数，则按照系统默认值进行分配。
        :rtype: :class:`tencentcloud.hai.v20230812.models.SystemDisk`
        """
        return self._SystemDisk

    @SystemDisk.setter
    def SystemDisk(self, SystemDisk):
        self._SystemDisk = SystemDisk

    @property
    def InstanceCount(self):
        r"""购买实例数量，单次请求实例数量上限为10.
        :rtype: int
        """
        return self._InstanceCount

    @InstanceCount.setter
    def InstanceCount(self, InstanceCount):
        self._InstanceCount = InstanceCount

    @property
    def InstanceName(self):
        r"""实例显示名称，名称长度限制为128个字符.
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ClientToken(self):
        r"""幂等请求的token
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""DryRun为True就是只验接口连通性，默认为False
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ApplicationId = params.get("ApplicationId")
        self._BundleType = params.get("BundleType")
        if params.get("SystemDisk") is not None:
            self._SystemDisk = SystemDisk()
            self._SystemDisk._deserialize(params.get("SystemDisk"))
        self._InstanceCount = params.get("InstanceCount")
        self._InstanceName = params.get("InstanceName")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    r"""RunInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdSet: 实例ID列表
        :type InstanceIdSet: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceIdSet = None
        self._RequestId = None

    @property
    def InstanceIdSet(self):
        r"""实例ID列表
        :rtype: list of str
        """
        return self._InstanceIdSet

    @InstanceIdSet.setter
    def InstanceIdSet(self, InstanceIdSet):
        self._InstanceIdSet = InstanceIdSet

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceIdSet = params.get("InstanceIdSet")
        self._RequestId = params.get("RequestId")


class SceneInfo(AbstractModel):
    r"""场景详情

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景id

        :type SceneId: str
        :param _SceneName: 场景名

        :type SceneName: str
        """
        self._SceneId = None
        self._SceneName = None

    @property
    def SceneId(self):
        r"""场景id

        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def SceneName(self):
        r"""场景名

        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._SceneName = params.get("SceneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceDetail(AbstractModel):
    r"""服务详情

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _ServiceState: 服务状态
        :type ServiceState: str
        :param _RunningReplicas: 运行中的副本数
        :type RunningReplicas: int
        :param _TotalReplicas: 期望的副本总数
        :type TotalReplicas: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ComputeSet: 算力套餐详情
        :type ComputeSet: list of ComputeDetail
        :param _ModelName: 模型名称
        :type ModelName: str
        :param _DeploymentConfigs: 服务部署信息
        :type DeploymentConfigs: list of DeploymentConfig
        :param _HyperParam: 服务超参数配置
        :type HyperParam: :class:`tencentcloud.hai.v20230812.models.HyperParam`
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceState = None
        self._RunningReplicas = None
        self._TotalReplicas = None
        self._CreateTime = None
        self._ComputeSet = None
        self._ModelName = None
        self._DeploymentConfigs = None
        self._HyperParam = None

    @property
    def ServiceId(self):
        r"""服务id
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        r"""服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceState(self):
        r"""服务状态
        :rtype: str
        """
        return self._ServiceState

    @ServiceState.setter
    def ServiceState(self, ServiceState):
        self._ServiceState = ServiceState

    @property
    def RunningReplicas(self):
        r"""运行中的副本数
        :rtype: int
        """
        return self._RunningReplicas

    @RunningReplicas.setter
    def RunningReplicas(self, RunningReplicas):
        self._RunningReplicas = RunningReplicas

    @property
    def TotalReplicas(self):
        r"""期望的副本总数
        :rtype: int
        """
        return self._TotalReplicas

    @TotalReplicas.setter
    def TotalReplicas(self, TotalReplicas):
        self._TotalReplicas = TotalReplicas

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ComputeSet(self):
        r"""算力套餐详情
        :rtype: list of ComputeDetail
        """
        return self._ComputeSet

    @ComputeSet.setter
    def ComputeSet(self, ComputeSet):
        self._ComputeSet = ComputeSet

    @property
    def ModelName(self):
        r"""模型名称
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def DeploymentConfigs(self):
        r"""服务部署信息
        :rtype: list of DeploymentConfig
        """
        return self._DeploymentConfigs

    @DeploymentConfigs.setter
    def DeploymentConfigs(self, DeploymentConfigs):
        self._DeploymentConfigs = DeploymentConfigs

    @property
    def HyperParam(self):
        r"""服务超参数配置
        :rtype: :class:`tencentcloud.hai.v20230812.models.HyperParam`
        """
        return self._HyperParam

    @HyperParam.setter
    def HyperParam(self, HyperParam):
        self._HyperParam = HyperParam


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceState = params.get("ServiceState")
        self._RunningReplicas = params.get("RunningReplicas")
        self._TotalReplicas = params.get("TotalReplicas")
        self._CreateTime = params.get("CreateTime")
        if params.get("ComputeSet") is not None:
            self._ComputeSet = []
            for item in params.get("ComputeSet"):
                obj = ComputeDetail()
                obj._deserialize(item)
                self._ComputeSet.append(obj)
        self._ModelName = params.get("ModelName")
        if params.get("DeploymentConfigs") is not None:
            self._DeploymentConfigs = []
            for item in params.get("DeploymentConfigs"):
                obj = DeploymentConfig()
                obj._deserialize(item)
                self._DeploymentConfigs.append(obj)
        if params.get("HyperParam") is not None:
            self._HyperParam = HyperParam()
            self._HyperParam._deserialize(params.get("HyperParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceMetaData(AbstractModel):
    r"""服务元数据信息，如服务名

    """

    def __init__(self):
        r"""
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _ServiceChargeType: 收费类型
        :type ServiceChargeType: str
        """
        self._ServiceName = None
        self._ServiceChargeType = None

    @property
    def ServiceName(self):
        r"""服务名称
        :rtype: str
        """
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceChargeType(self):
        r"""收费类型
        :rtype: str
        """
        return self._ServiceChargeType

    @ServiceChargeType.setter
    def ServiceChargeType(self, ServiceChargeType):
        self._ServiceChargeType = ServiceChargeType


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._ServiceChargeType = params.get("ServiceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicePriceDetail(AbstractModel):
    r"""推理集群费用数据结构体

    """

    def __init__(self):
        r"""
        :param _ServicePrice: 推理集群价格信息	
        :type ServicePrice: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        self._ServicePrice = None

    @property
    def ServicePrice(self):
        r"""推理集群价格信息	
        :rtype: :class:`tencentcloud.hai.v20230812.models.ItemPrice`
        """
        return self._ServicePrice

    @ServicePrice.setter
    def ServicePrice(self, ServicePrice):
        self._ServicePrice = ServicePrice


    def _deserialize(self, params):
        if params.get("ServicePrice") is not None:
            self._ServicePrice = ItemPrice()
            self._ServicePrice._deserialize(params.get("ServicePrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceRequest(AbstractModel):
    r"""StartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612) API获取实例ID。
        :type InstanceId: str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceId = None
        self._DryRun = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612) API获取实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DryRun(self):
        r"""默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstanceResponse(AbstractModel):
    r"""StartInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: task任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""task任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StopInstanceRequest(AbstractModel):
    r"""StopInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612) API获取实例ID。
        :type InstanceId: str
        :param _StopMode: hai实例关机的模式，目前仅支持关机不收费：
STOP_CHARGE -- 关闭hai实例，释放计算资源，停止收取计算资源的费用。
注意：默认值为STOP_CHARGE
        :type StopMode: str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceId = None
        self._StopMode = None
        self._DryRun = None

    @property
    def InstanceId(self):
        r"""实例ID。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612) API获取实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def StopMode(self):
        r"""hai实例关机的模式，目前仅支持关机不收费：
STOP_CHARGE -- 关闭hai实例，释放计算资源，停止收取计算资源的费用。
注意：默认值为STOP_CHARGE
        :rtype: str
        """
        return self._StopMode

    @StopMode.setter
    def StopMode(self, StopMode):
        self._StopMode = StopMode

    @property
    def DryRun(self):
        r"""默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._StopMode = params.get("StopMode")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstanceResponse(AbstractModel):
    r"""StopInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: task任务id
        :type TaskId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        r"""task任务id
        :rtype: int
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class StorageInfo(AbstractModel):
    r"""存储信息

    """

    def __init__(self):
        r"""
        :param _MountPath: 挂载路径
        :type MountPath: str
        :param _COSStorage: cos挂载信息
        :type COSStorage: :class:`tencentcloud.hai.v20230812.models.COSStorage`
        """
        self._MountPath = None
        self._COSStorage = None

    @property
    def MountPath(self):
        r"""挂载路径
        :rtype: str
        """
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath

    @property
    def COSStorage(self):
        r"""cos挂载信息
        :rtype: :class:`tencentcloud.hai.v20230812.models.COSStorage`
        """
        return self._COSStorage

    @COSStorage.setter
    def COSStorage(self, COSStorage):
        self._COSStorage = COSStorage


    def _deserialize(self, params):
        self._MountPath = params.get("MountPath")
        if params.get("COSStorage") is not None:
            self._COSStorage = COSStorage()
            self._COSStorage._deserialize(params.get("COSStorage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemDisk(AbstractModel):
    r"""描述了操作系统所在块设备即系统盘的信息

    """

    def __init__(self):
        r"""
        :param _DiskType: 系统盘类型。取值范围：<li>CLOUD_PREMIUM：高性能云硬盘</li><li>CLOUD_HSSD：增强型SSD云盘</li>默认取值：当前有库存的硬盘类型。
        :type DiskType: str
        :param _DiskSize: 系统盘大小，单位：GB。默认值为 80，取值范围：80-1000
        :type DiskSize: int
        :param _DiskName: 系统盘分区盘符
        :type DiskName: str
        """
        self._DiskType = None
        self._DiskSize = None
        self._DiskName = None

    @property
    def DiskType(self):
        r"""系统盘类型。取值范围：<li>CLOUD_PREMIUM：高性能云硬盘</li><li>CLOUD_HSSD：增强型SSD云盘</li>默认取值：当前有库存的硬盘类型。
        :rtype: str
        """
        return self._DiskType

    @DiskType.setter
    def DiskType(self, DiskType):
        self._DiskType = DiskType

    @property
    def DiskSize(self):
        r"""系统盘大小，单位：GB。默认值为 80，取值范围：80-1000
        :rtype: int
        """
        return self._DiskSize

    @DiskSize.setter
    def DiskSize(self, DiskSize):
        self._DiskSize = DiskSize

    @property
    def DiskName(self):
        r"""系统盘分区盘符
        :rtype: str
        """
        return self._DiskName

    @DiskName.setter
    def DiskName(self, DiskName):
        self._DiskName = DiskName


    def _deserialize(self, params):
        self._DiskType = params.get("DiskType")
        self._DiskSize = params.get("DiskSize")
        self._DiskName = params.get("DiskName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateDetail(AbstractModel):
    r"""模板详情

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板id
        :type TemplateId: str
        :param _DeployMode: 部署方式
        :type DeployMode: str
        :param _EngineType: 推理引擎
        :type EngineType: str
        :param _ComputeSet: 算力详情
        :type ComputeSet: list of ComputeDetail
        :param _SupportFunc: 当前部署模板所支持的增强功能
        :type SupportFunc: list of str
        """
        self._TemplateId = None
        self._DeployMode = None
        self._EngineType = None
        self._ComputeSet = None
        self._SupportFunc = None

    @property
    def TemplateId(self):
        r"""模板id
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def DeployMode(self):
        r"""部署方式
        :rtype: str
        """
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def EngineType(self):
        r"""推理引擎
        :rtype: str
        """
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def ComputeSet(self):
        r"""算力详情
        :rtype: list of ComputeDetail
        """
        return self._ComputeSet

    @ComputeSet.setter
    def ComputeSet(self, ComputeSet):
        self._ComputeSet = ComputeSet

    @property
    def SupportFunc(self):
        r"""当前部署模板所支持的增强功能
        :rtype: list of str
        """
        return self._SupportFunc

    @SupportFunc.setter
    def SupportFunc(self, SupportFunc):
        self._SupportFunc = SupportFunc


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._DeployMode = params.get("DeployMode")
        self._EngineType = params.get("EngineType")
        if params.get("ComputeSet") is not None:
            self._ComputeSet = []
            for item in params.get("ComputeSet"):
                obj = ComputeDetail()
                obj._deserialize(item)
                self._ComputeSet.append(obj)
        self._SupportFunc = params.get("SupportFunc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    r"""TerminateInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 实例ID列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612) API获取实例ID列表。单次能查询100个InstanceId。
        :type InstanceIds: list of str
        :param _DryRun: 默认为False，True代表只验证接口连通性
        :type DryRun: bool
        """
        self._InstanceIds = None
        self._DryRun = None

    @property
    def InstanceIds(self):
        r"""实例ID列表。可通过[DescribeInstances](https://cloud.tencent.com/document/api/1721/101612) API获取实例ID列表。单次能查询100个InstanceId。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def DryRun(self):
        r"""默认为False，True代表只验证接口连通性
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    r"""TerminateInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateServiceConfigsRequest(AbstractModel):
    r"""UpdateServiceConfigs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _TargetReplicas: 期望副本数
        :type TargetReplicas: int
        """
        self._ServiceId = None
        self._TargetReplicas = None

    @property
    def ServiceId(self):
        r"""服务ID
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def TargetReplicas(self):
        r"""期望副本数
        :rtype: int
        """
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._TargetReplicas = params.get("TargetReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceConfigsResponse(AbstractModel):
    r"""UpdateServiceConfigs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")