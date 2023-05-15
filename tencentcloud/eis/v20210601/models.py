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


class AbstractRuntimeMC(AbstractModel):
    """运行时精简信息

    """

    def __init__(self):
        r"""
        :param RuntimeId: 环境id
        :type RuntimeId: int
        :param DisplayName: 环境名称，用户输入，同一uin内唯一
        :type DisplayName: str
        :param Type: 环境类型：0: sandbox, 1:shared, 2:private
        :type Type: int
        :param Zone: 环境所在地域，tianjin，beijiing，guangzhou等
        :type Zone: str
        :param Area: 环境所在地域，tianjin，beijiing，guangzhou等（同Zone）
        :type Area: str
        :param Addr: 环境应用listener地址后缀
        :type Addr: str
        :param Status: 环境状态
        :type Status: int
        :param ExpiredAt: 环境过期时间
        :type ExpiredAt: int
        :param RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        :param Deployed: 是否已在当前环境发布
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployed: bool
        """
        self.RuntimeId = None
        self.DisplayName = None
        self.Type = None
        self.Zone = None
        self.Area = None
        self.Addr = None
        self.Status = None
        self.ExpiredAt = None
        self.RuntimeClass = None
        self.Deployed = None


    def _deserialize(self, params):
        self.RuntimeId = params.get("RuntimeId")
        self.DisplayName = params.get("DisplayName")
        self.Type = params.get("Type")
        self.Zone = params.get("Zone")
        self.Area = params.get("Area")
        self.Addr = params.get("Addr")
        self.Status = params.get("Status")
        self.ExpiredAt = params.get("ExpiredAt")
        self.RuntimeClass = params.get("RuntimeClass")
        self.Deployed = params.get("Deployed")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuntimeMCRequest(AbstractModel):
    """GetRuntimeMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuntimeId: 环境id
        :type RuntimeId: int
        :param Zone: 环境地域
        :type Zone: str
        :param RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        """
        self.RuntimeId = None
        self.Zone = None
        self.RuntimeClass = None


    def _deserialize(self, params):
        self.RuntimeId = params.get("RuntimeId")
        self.Zone = params.get("Zone")
        self.RuntimeClass = params.get("RuntimeClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuntimeMCResponse(AbstractModel):
    """GetRuntimeMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Runtime: 运行时详情
        :type Runtime: :class:`tencentcloud.eis.v20210601.models.RuntimeMC`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Runtime = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtime") is not None:
            self.Runtime = RuntimeMC()
            self.Runtime._deserialize(params.get("Runtime"))
        self.RequestId = params.get("RequestId")


class GetRuntimeResourceMonitorMetricMCRequest(AbstractModel):
    """GetRuntimeResourceMonitorMetricMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuntimeId: 运行时id
        :type RuntimeId: int
        :param StartTime: 起始时间
        :type StartTime: int
        :param EndTime: 结束时间
        :type EndTime: int
        :param MetricType: 指标类型：0:CPU, 1:MemUsageBytes, 2:K8sWorkloadNetworkReceiveBytesBw, 3:K8sWorkloadNetworkTransmitBytesBw
        :type MetricType: int
        :param RateType: 是否返回百分比数值，仅支持CPU，Memory
        :type RateType: bool
        :param Interval: 采样粒度：60(s), 300(s), 3600(s), 86400(s)
        :type Interval: int
        :param RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        """
        self.RuntimeId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricType = None
        self.RateType = None
        self.Interval = None
        self.RuntimeClass = None


    def _deserialize(self, params):
        self.RuntimeId = params.get("RuntimeId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricType = params.get("MetricType")
        self.RateType = params.get("RateType")
        self.Interval = params.get("Interval")
        self.RuntimeClass = params.get("RuntimeClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuntimeResourceMonitorMetricMCResponse(AbstractModel):
    """GetRuntimeResourceMonitorMetricMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param MetricType: 指标名称，K8sWorkloadCpuCoreUsed，K8sWorkloadMemUsageBytes，K8sWorkloadNetworkReceiveBytesBw，K8sWorkloadNetworkTransmitBytesBw
        :type MetricType: str
        :param Values: metric数值列表
        :type Values: list of MetricValueMC
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MetricType = None
        self.Values = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MetricType = params.get("MetricType")
        if params.get("Values") is not None:
            self.Values = []
            for item in params.get("Values"):
                obj = MetricValueMC()
                obj._deserialize(item)
                self.Values.append(obj)
        self.RequestId = params.get("RequestId")


class ListDeployableRuntimesMCRequest(AbstractModel):
    """ListDeployableRuntimesMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 应用id
        :type ProjectId: int
        :param InstanceId: 实例id
        :type InstanceId: int
        :param PlanType: 版本类型 0-pro 1-lite
        :type PlanType: int
        """
        self.ProjectId = None
        self.InstanceId = None
        self.PlanType = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.InstanceId = params.get("InstanceId")
        self.PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeployableRuntimesMCResponse(AbstractModel):
    """ListDeployableRuntimesMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Runtimes: 运行时列表
        :type Runtimes: list of AbstractRuntimeMC
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Runtimes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtimes") is not None:
            self.Runtimes = []
            for item in params.get("Runtimes"):
                obj = AbstractRuntimeMC()
                obj._deserialize(item)
                self.Runtimes.append(obj)
        self.RequestId = params.get("RequestId")


class ListRuntimeDeployedInstancesMCRequest(AbstractModel):
    """ListRuntimeDeployedInstancesMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuntimeId: 运行时id
        :type RuntimeId: int
        :param Limit: 最大请求数量
        :type Limit: int
        :param Offset: 请求偏移量
        :type Offset: int
        :param SortType: 排序类型：1:创建时间排序, 2:更新时间排序（默认）
        :type SortType: int
        :param Sort: 排序方式：asc，desc（默认）
        :type Sort: str
        :param Zone: 运行时地域
        :type Zone: str
        :param ApiVersion: 1:3.0版本新控制台传1；否则传0
        :type ApiVersion: int
        :param GroupId: -1:不按项目筛选，获取所有
>=0: 按项目id筛选
        :type GroupId: int
        :param Status: -2: 不按状态筛选，获取所有
0: 运行中
2: 已停止
        :type Status: int
        """
        self.RuntimeId = None
        self.Limit = None
        self.Offset = None
        self.SortType = None
        self.Sort = None
        self.Zone = None
        self.ApiVersion = None
        self.GroupId = None
        self.Status = None


    def _deserialize(self, params):
        self.RuntimeId = params.get("RuntimeId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SortType = params.get("SortType")
        self.Sort = params.get("Sort")
        self.Zone = params.get("Zone")
        self.ApiVersion = params.get("ApiVersion")
        self.GroupId = params.get("GroupId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRuntimeDeployedInstancesMCResponse(AbstractModel):
    """ListRuntimeDeployedInstancesMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Instances: 运行时所部属的应用实例列表
        :type Instances: list of RuntimeDeployedInstanceMC
        :param TotalCount: 满足条件的记录总数，用于分页器
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Instances = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = RuntimeDeployedInstanceMC()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class ListRuntimesMCRequest(AbstractModel):
    """ListRuntimesMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        :param PlanType: 计划类型：0-pro 1-lite
        :type PlanType: int
        """
        self.RuntimeClass = None
        self.PlanType = None


    def _deserialize(self, params):
        self.RuntimeClass = params.get("RuntimeClass")
        self.PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRuntimesMCResponse(AbstractModel):
    """ListRuntimesMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param Runtimes: 运行时列表
        :type Runtimes: list of RuntimeMC
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Runtimes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Runtimes") is not None:
            self.Runtimes = []
            for item in params.get("Runtimes"):
                obj = RuntimeMC()
                obj._deserialize(item)
                self.Runtimes.append(obj)
        self.RequestId = params.get("RequestId")


class MetricValueMC(AbstractModel):
    """GetMonitorMetricResponse

    """

    def __init__(self):
        r"""
        :param Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param Val: 对应的value值
注意：此字段可能返回 null，表示取不到有效值。
        :type Val: str
        """
        self.Time = None
        self.Val = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeDeployedInstanceMC(AbstractModel):
    """运行时部署的应用实例详情

    """

    def __init__(self):
        r"""
        :param GroupId: 项目id
        :type GroupId: int
        :param GroupName: 项目名称
        :type GroupName: str
        :param ProjectId: 应用id
        :type ProjectId: int
        :param ProjectName: 应用名称
        :type ProjectName: str
        :param InstanceId: 应用实例id
        :type InstanceId: int
        :param InstanceVersion: 应用实例版本
        :type InstanceVersion: int
        :param InstanceCreatedAt: 应用实例创建时间
        :type InstanceCreatedAt: int
        :param Status: 应用实例部署状态. 0:running, 1:deleting
        :type Status: int
        :param CreatedAt: 应用实例部署创建时间
        :type CreatedAt: int
        :param UpdatedAt: 应用实例部署更新时间
        :type UpdatedAt: int
        :param ProjectType: 应用类型：0:NormalApp普通应用 1:TemplateApp模板应用 2:LightApp轻应用 3:MicroConnTemplate微连接模板 4:MicroConnApp微连接应用
        :type ProjectType: int
        :param ProjectVersion: 应用版本：0:旧版 1:3.0新控制台
        :type ProjectVersion: int
        """
        self.GroupId = None
        self.GroupName = None
        self.ProjectId = None
        self.ProjectName = None
        self.InstanceId = None
        self.InstanceVersion = None
        self.InstanceCreatedAt = None
        self.Status = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.ProjectType = None
        self.ProjectVersion = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceVersion = params.get("InstanceVersion")
        self.InstanceCreatedAt = params.get("InstanceCreatedAt")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.ProjectType = params.get("ProjectType")
        self.ProjectVersion = params.get("ProjectVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeExtensionMC(AbstractModel):
    """运行环境扩展组件

    """

    def __init__(self):
        r"""
        :param Type: 扩展组件类型：0:cdc
        :type Type: int
        :param Size: 部署规格vcore数
        :type Size: float
        :param Replica: 副本数
        :type Replica: int
        :param Name: 扩展组件名称
        :type Name: str
        :param Status: 状态 1:未启用 2:已启用
        :type Status: int
        :param CreatedAt: 创建时间
        :type CreatedAt: int
        :param UpdatedAt: 修改时间
        :type UpdatedAt: int
        """
        self.Type = None
        self.Size = None
        self.Replica = None
        self.Name = None
        self.Status = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        self.Replica = params.get("Replica")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeMC(AbstractModel):
    """运行时详细信息

    """

    def __init__(self):
        r"""
        :param RuntimeId: 环境id
        :type RuntimeId: int
        :param Uin: 主账号uin
        :type Uin: str
        :param DisplayName: 环境名称，用户输入，同一uin内唯一
        :type DisplayName: str
        :param Zone: 环境所在地域，tianjin，beijiing，guangzhou等
        :type Zone: str
        :param Type: 环境类型：0: sandbox, 1:shared, 2:private 3: trial
        :type Type: int
        :param Status: 运行时状态：1:running, 2:deleting, 3:creating, 4:scaling, 5:unavailable, 6:deleted, 7:errored
        :type Status: int
        :param CreatedAt: 环境创建时间
        :type CreatedAt: int
        :param UpdatedAt: 环境更新时间
        :type UpdatedAt: int
        :param WorkerSize: 环境资源配置，worker总配额，0:0vCore0G, 1:1vCore2G, 2:2vCore4G, 4:4vCore8G, 8:8vCore16G, 12:12vCore24G, 16:16vCore32G, 100:unlimited
        :type WorkerSize: int
        :param WorkerReplica: 环境资源配置，worker副本数
        :type WorkerReplica: int
        :param RunningInstanceCount: 正在运行的应用实例数量
        :type RunningInstanceCount: int
        :param CpuUsed: 已使用cpu核数
        :type CpuUsed: float
        :param CpuLimit: cpu核数上限
        :type CpuLimit: float
        :param MemoryUsed: 已使用内存 MB
        :type MemoryUsed: float
        :param MemoryLimit: 内存上限 MB
        :type MemoryLimit: float
        :param ExpiredAt: 环境过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: int
        :param ChargeType: 收费类型：0:缺省，1:自助下单页购买(支持续费/升配等操作)，2:代销下单页购买
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param ResourceLimitType: 资源限制类型：0:无限制，1:有限制
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceLimitType: int
        :param AutoRenewal: 是否开启自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewal: bool
        :param WorkerExtensions: 扩展组件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkerExtensions: list of RuntimeExtensionMC
        :param RuntimeType: 环境类型：0: sandbox, 1:shared, 2:private 3: trial
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeType: int
        :param RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeClass: int
        :param BandwidthOutUsed: 已使用出带宽 Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthOutUsed: float
        :param BandwidthOutLimit: 出带宽上限 Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthOutLimit: float
        """
        self.RuntimeId = None
        self.Uin = None
        self.DisplayName = None
        self.Zone = None
        self.Type = None
        self.Status = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.WorkerSize = None
        self.WorkerReplica = None
        self.RunningInstanceCount = None
        self.CpuUsed = None
        self.CpuLimit = None
        self.MemoryUsed = None
        self.MemoryLimit = None
        self.ExpiredAt = None
        self.ChargeType = None
        self.ResourceLimitType = None
        self.AutoRenewal = None
        self.WorkerExtensions = None
        self.RuntimeType = None
        self.RuntimeClass = None
        self.BandwidthOutUsed = None
        self.BandwidthOutLimit = None


    def _deserialize(self, params):
        self.RuntimeId = params.get("RuntimeId")
        self.Uin = params.get("Uin")
        self.DisplayName = params.get("DisplayName")
        self.Zone = params.get("Zone")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.WorkerSize = params.get("WorkerSize")
        self.WorkerReplica = params.get("WorkerReplica")
        self.RunningInstanceCount = params.get("RunningInstanceCount")
        self.CpuUsed = params.get("CpuUsed")
        self.CpuLimit = params.get("CpuLimit")
        self.MemoryUsed = params.get("MemoryUsed")
        self.MemoryLimit = params.get("MemoryLimit")
        self.ExpiredAt = params.get("ExpiredAt")
        self.ChargeType = params.get("ChargeType")
        self.ResourceLimitType = params.get("ResourceLimitType")
        self.AutoRenewal = params.get("AutoRenewal")
        if params.get("WorkerExtensions") is not None:
            self.WorkerExtensions = []
            for item in params.get("WorkerExtensions"):
                obj = RuntimeExtensionMC()
                obj._deserialize(item)
                self.WorkerExtensions.append(obj)
        self.RuntimeType = params.get("RuntimeType")
        self.RuntimeClass = params.get("RuntimeClass")
        self.BandwidthOutUsed = params.get("BandwidthOutUsed")
        self.BandwidthOutLimit = params.get("BandwidthOutLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        