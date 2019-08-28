# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


class Conditions(AbstractModel):
    """状态

    """

    def __init__(self):
        """
        :param Reason: 原因
        :type Reason: str
        :param Count: 具有相同原因的副本个数
        :type Count: int
        """
        self.Reason = None
        self.Count = None


    def _deserialize(self, params):
        self.Reason = params.get("Reason")
        self.Count = params.get("Count")


class CreateServiceConfigRequest(AbstractModel):
    """CreateServiceConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 配置名称
        :type Name: str
        :param Runtime: 运行环境
        :type Runtime: str
        :param ModelUri: 模型地址，支持cos路径，格式为 cos://bucket名-appid.cos.region名.myqcloud.com/模型文件夹路径。为模型文件的上一层文件夹地址。
        :type ModelUri: str
        :param Cpu: 处理器配置, 单位为1/1000核；范围[100, 256000]
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M；范围[100, 256000]
        :type Memory: int
        :param TflopUnits: GPU算力配置，单位为1/100 tflops，范围 [0, 256000]
        :type TflopUnits: int
        :param GpuMemory: 显存配置, 单位为1M，范围 [0, 256000]
        :type GpuMemory: int
        """
        self.Name = None
        self.Runtime = None
        self.ModelUri = None
        self.Cpu = None
        self.Memory = None
        self.TflopUnits = None
        self.GpuMemory = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.ModelUri = params.get("ModelUri")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.TflopUnits = params.get("TflopUnits")
        self.GpuMemory = params.get("GpuMemory")


class CreateServiceConfigResponse(AbstractModel):
    """CreateServiceConfig返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceConfig: 服务配置
        :type ServiceConfig: :class:`tencentcloud.tiems.v20190416.models.ServiceConfig`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceConfig = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService请求参数结构体

    """

    def __init__(self):
        """
        :param Scaler: 扩缩容配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param ServiceConfigId: 服务配置Id
        :type ServiceConfigId: int
        :param Name: 服务名称
        :type Name: str
        :param ScaleMode: 扩缩容方式，支持AUTO, MANUAL，分别表示自动扩缩容和手动扩缩容
        :type ScaleMode: str
        :param Cluster: 集群，不填则使用默认集群。
        :type Cluster: str
        """
        self.Scaler = None
        self.ServiceConfigId = None
        self.Name = None
        self.ScaleMode = None
        self.Cluster = None


    def _deserialize(self, params):
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.Name = params.get("Name")
        self.ScaleMode = params.get("ScaleMode")
        self.Cluster = params.get("Cluster")


class CreateServiceResponse(AbstractModel):
    """CreateService返回参数结构体

    """

    def __init__(self):
        """
        :param Service: 服务
        :type Service: :class:`tencentcloud.tiems.v20190416.models.Service`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")


class DeleteServiceConfigRequest(AbstractModel):
    """DeleteServiceConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceConfigId: 服务配置Id (deprecated)
        :type ServiceConfigId: int
        :param ServiceConfigName: 服务配置名称
        :type ServiceConfigName: str
        """
        self.ServiceConfigId = None
        self.ServiceConfigName = None


    def _deserialize(self, params):
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ServiceConfigName = params.get("ServiceConfigName")


class DeleteServiceConfigResponse(AbstractModel):
    """DeleteServiceConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务Id
        :type ServiceId: int
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeRuntimesRequest(AbstractModel):
    """DescribeRuntimes请求参数结构体

    """


class DescribeRuntimesResponse(AbstractModel):
    """DescribeRuntimes返回参数结构体

    """

    def __init__(self):
        """
        :param Runtimes: TIEMS支持的运行环境列表
        :type Runtimes: list of Runtime
        :param UserAccess: 用户对runtime对权限
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAccess: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Runtimes = None
        self.UserAccess = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtimes") is not None:
            self.Runtimes = []
            for item in params.get("Runtimes"):
                obj = Runtime()
                obj._deserialize(item)
                self.Runtimes.append(obj)
        self.UserAccess = params.get("UserAccess")
        self.RequestId = params.get("RequestId")


class DescribeServiceConfigsRequest(AbstractModel):
    """DescribeServiceConfigs请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 筛选选项，支持按照name等进行筛选
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为1000
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CREATE_TIME", "UPDATE_TIME", "NAME"
        :type OrderField: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeServiceConfigsResponse(AbstractModel):
    """DescribeServiceConfigs返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceConfigs: 服务配置
        :type ServiceConfigs: list of ServiceConfig
        :param TotalCount: 服务配置总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceConfigs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceConfigs") is not None:
            self.ServiceConfigs = []
            for item in params.get("ServiceConfigs"):
                obj = ServiceConfig()
                obj._deserialize(item)
                self.ServiceConfigs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServicesRequest(AbstractModel):
    """DescribeServices请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 筛选选项，支持按照name等字段进行筛选
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param Order: 输出列表的排列顺序。取值范围：ASC：升序排列 DESC：降序排列
        :type Order: str
        :param OrderField: 排序的依据字段， 取值范围 "CREATE_TIME" "UPDATE_TIME"
        :type OrderField: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")


class DescribeServicesResponse(AbstractModel):
    """DescribeServices返回参数结构体

    """

    def __init__(self):
        """
        :param Services: 服务列表
        :type Services: list of Service
        :param TotalCount: 服务总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Services = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Services") is not None:
            self.Services = []
            for item in params.get("Services"):
                obj = Service()
                obj._deserialize(item)
                self.Services.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """筛选项

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Values: 取值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class Option(AbstractModel):
    """配置项

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Value: 取值
        :type Value: int
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class Runtime(AbstractModel):
    """运行环境

    """

    def __init__(self):
        """
        :param Name: 运行环境名称
        :type Name: str
        :param Framework: 运行环境框架
        :type Framework: str
        :param Description: 运行环境描述
        :type Description: str
        :param Public: 是否为公开运行环境
注意：此字段可能返回 null，表示取不到有效值。
        :type Public: bool
        :param HealthCheckOn: 是否打开健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthCheckOn: bool
        :param Image: 镜像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Image: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.Name = None
        self.Framework = None
        self.Description = None
        self.Public = None
        self.HealthCheckOn = None
        self.Image = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Framework = params.get("Framework")
        self.Description = params.get("Description")
        self.Public = params.get("Public")
        self.HealthCheckOn = params.get("HealthCheckOn")
        self.Image = params.get("Image")
        self.CreateTime = params.get("CreateTime")


class Scaler(AbstractModel):
    """扩缩容配置

    """

    def __init__(self):
        """
        :param MaxReplicas: 最大副本数
        :type MaxReplicas: int
        :param MinReplicas: 最小副本数
        :type MinReplicas: int
        :param StartReplicas: 起始副本数
        :type StartReplicas: int
        :param HpaMetrics: 扩缩容指标，选择自动扩缩容时至少需要选择一个指标，支持CPU-UTIL、MEMORY-UTIL
        :type HpaMetrics: list of Option
        """
        self.MaxReplicas = None
        self.MinReplicas = None
        self.StartReplicas = None
        self.HpaMetrics = None


    def _deserialize(self, params):
        self.MaxReplicas = params.get("MaxReplicas")
        self.MinReplicas = params.get("MinReplicas")
        self.StartReplicas = params.get("StartReplicas")
        if params.get("HpaMetrics") is not None:
            self.HpaMetrics = []
            for item in params.get("HpaMetrics"):
                obj = Option()
                obj._deserialize(item)
                self.HpaMetrics.append(obj)


class Service(AbstractModel):
    """模型服务

    """

    def __init__(self):
        """
        :param Id: 服务ID
        :type Id: int
        :param Cluster: 运行集群
        :type Cluster: str
        :param Name: 服务名称
        :type Name: str
        :param Runtime: 运行环境
        :type Runtime: str
        :param ModelUri: 模型地址
        :type ModelUri: str
        :param Cpu: 处理器配置, 单位为1/1000核
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M
        :type Memory: int
        :param TflopUnits: 处理器配置, 单位为1/100 tflops
        :type TflopUnits: int
        :param GpuMemory: 显存配置, 单位为1M
        :type GpuMemory: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ScaleMode: 支持AUTO, MANUAL
        :type ScaleMode: str
        :param Scaler: 弹性伸缩配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param Status: 服务状态
        :type Status: :class:`tencentcloud.tiems.v20190416.models.ServiceStatus`
        :param ServingIp: 服务地址
        :type ServingIp: str
        :param AccessToken: 访问密钥
        :type AccessToken: str
        :param ServiceConfigId: 服务配置Id
        :type ServiceConfigId: int
        :param ServiceConfigName: 服务配置名
        :type ServiceConfigName: str
        :param ServeSeconds: 服务运行时长
        :type ServeSeconds: int
        :param ServiceConfigVersion: 配置版本
        :type ServiceConfigVersion: str
        """
        self.Id = None
        self.Cluster = None
        self.Name = None
        self.Runtime = None
        self.ModelUri = None
        self.Cpu = None
        self.Memory = None
        self.TflopUnits = None
        self.GpuMemory = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ScaleMode = None
        self.Scaler = None
        self.Status = None
        self.ServingIp = None
        self.AccessToken = None
        self.ServiceConfigId = None
        self.ServiceConfigName = None
        self.ServeSeconds = None
        self.ServiceConfigVersion = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Cluster = params.get("Cluster")
        self.Name = params.get("Name")
        self.Runtime = params.get("Runtime")
        self.ModelUri = params.get("ModelUri")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.TflopUnits = params.get("TflopUnits")
        self.GpuMemory = params.get("GpuMemory")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ScaleMode = params.get("ScaleMode")
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        if params.get("Status") is not None:
            self.Status = ServiceStatus()
            self.Status._deserialize(params.get("Status"))
        self.ServingIp = params.get("ServingIp")
        self.AccessToken = params.get("AccessToken")
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ServiceConfigName = params.get("ServiceConfigName")
        self.ServeSeconds = params.get("ServeSeconds")
        self.ServiceConfigVersion = params.get("ServiceConfigVersion")


class ServiceConfig(AbstractModel):
    """服务配置

    """

    def __init__(self):
        """
        :param Id: Id
        :type Id: int
        :param Name: 配置名
        :type Name: str
        :param ModelUri: 模型地址
        :type ModelUri: str
        :param Cpu: 处理器配置, 单位为1/1000核
        :type Cpu: int
        :param Memory: 内存配置, 单位为1M
        :type Memory: int
        :param TflopUnits: GPU算力，单位为1/100 tflops
注意：此字段可能返回 null，表示取不到有效值。
        :type TflopUnits: int
        :param GpuMemory: 显存配置, 单位为1M
注意：此字段可能返回 null，表示取不到有效值。
        :type GpuMemory: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Runtime: 运行环境
        :type Runtime: str
        :param Version: 配置版本
        :type Version: str
        """
        self.Id = None
        self.Name = None
        self.ModelUri = None
        self.Cpu = None
        self.Memory = None
        self.TflopUnits = None
        self.GpuMemory = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Runtime = None
        self.Version = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.ModelUri = params.get("ModelUri")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.TflopUnits = params.get("TflopUnits")
        self.GpuMemory = params.get("GpuMemory")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Runtime = params.get("Runtime")
        self.Version = params.get("Version")


class ServiceStatus(AbstractModel):
    """服务状态

    """

    def __init__(self):
        """
        :param DesiredReplicas: 预期副本数
        :type DesiredReplicas: int
        :param CurrentReplicas: 当前副本数
        :type CurrentReplicas: int
        :param Status: Normal：正常运行中；Abnormal：服务异常，例如容器启动失败等；Waiting：服务等待中，例如容器下载镜像过程等；Stopped：已停止 Stopping 停止中；Resuming：重启中；Updating：服务更新中
        :type Status: str
        :param Conditions: 服务处于当前状态的原因集合
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of Conditions
        :param Replicas: 副本名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Replicas: list of str
        """
        self.DesiredReplicas = None
        self.CurrentReplicas = None
        self.Status = None
        self.Conditions = None
        self.Replicas = None


    def _deserialize(self, params):
        self.DesiredReplicas = params.get("DesiredReplicas")
        self.CurrentReplicas = params.get("CurrentReplicas")
        self.Status = params.get("Status")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = Conditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Replicas = params.get("Replicas")


class UpdateServiceRequest(AbstractModel):
    """UpdateService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务Id
        :type ServiceId: int
        :param Scaler: 扩缩容配置
        :type Scaler: :class:`tencentcloud.tiems.v20190416.models.Scaler`
        :param ServiceConfigId: 服务配置Id
        :type ServiceConfigId: int
        :param ScaleMode: 支持AUTO, MANUAL，分别表示自动扩缩容，手动扩缩容
        :type ScaleMode: str
        :param ServiceAction: 支持STOP(停止) RESUME(重启)
        :type ServiceAction: str
        """
        self.ServiceId = None
        self.Scaler = None
        self.ServiceConfigId = None
        self.ScaleMode = None
        self.ServiceAction = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("Scaler") is not None:
            self.Scaler = Scaler()
            self.Scaler._deserialize(params.get("Scaler"))
        self.ServiceConfigId = params.get("ServiceConfigId")
        self.ScaleMode = params.get("ScaleMode")
        self.ServiceAction = params.get("ServiceAction")


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回参数结构体

    """

    def __init__(self):
        """
        :param Service: 服务
        :type Service: :class:`tencentcloud.tiems.v20190416.models.Service`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Service = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Service") is not None:
            self.Service = Service()
            self.Service._deserialize(params.get("Service"))
        self.RequestId = params.get("RequestId")