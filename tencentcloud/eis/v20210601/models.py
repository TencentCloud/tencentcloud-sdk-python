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


class AbstractRuntimeMC(AbstractModel):
    r"""运行时精简信息

    """

    def __init__(self):
        r"""
        :param _RuntimeId: 环境id
        :type RuntimeId: int
        :param _DisplayName: 环境名称，用户输入，同一uin内唯一
        :type DisplayName: str
        :param _Type: 环境类型：0: sandbox, 1:shared, 2:private
        :type Type: int
        :param _Zone: 环境所在地域，tianjin，beijiing，guangzhou等
        :type Zone: str
        :param _Area: 环境所在地域，tianjin，beijiing，guangzhou等（同Zone）
        :type Area: str
        :param _Addr: 环境应用listener地址后缀
        :type Addr: str
        :param _Status: 环境状态
        :type Status: int
        :param _ExpiredAt: 环境过期时间
        :type ExpiredAt: int
        :param _RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        :param _Deployed: 是否已在当前环境发布
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployed: bool
        :param _MatchExtensions: 环境扩展组件是否满足应用要求：0=true, 1=false 表示该应用需要扩展组件0(cdc)以及1(java)，但是独立环境有cdc无java，不满足发布要求
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchExtensions: str
        """
        self._RuntimeId = None
        self._DisplayName = None
        self._Type = None
        self._Zone = None
        self._Area = None
        self._Addr = None
        self._Status = None
        self._ExpiredAt = None
        self._RuntimeClass = None
        self._Deployed = None
        self._MatchExtensions = None

    @property
    def RuntimeId(self):
        r"""环境id
        :rtype: int
        """
        return self._RuntimeId

    @RuntimeId.setter
    def RuntimeId(self, RuntimeId):
        self._RuntimeId = RuntimeId

    @property
    def DisplayName(self):
        r"""环境名称，用户输入，同一uin内唯一
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Type(self):
        r"""环境类型：0: sandbox, 1:shared, 2:private
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Zone(self):
        r"""环境所在地域，tianjin，beijiing，guangzhou等
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Area(self):
        r"""环境所在地域，tianjin，beijiing，guangzhou等（同Zone）
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Addr(self):
        r"""环境应用listener地址后缀
        :rtype: str
        """
        return self._Addr

    @Addr.setter
    def Addr(self, Addr):
        self._Addr = Addr

    @property
    def Status(self):
        r"""环境状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpiredAt(self):
        r"""环境过期时间
        :rtype: int
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def RuntimeClass(self):
        r"""环境运行类型：0:运行时类型、1:api类型
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass

    @property
    def Deployed(self):
        r"""是否已在当前环境发布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Deployed

    @Deployed.setter
    def Deployed(self, Deployed):
        self._Deployed = Deployed

    @property
    def MatchExtensions(self):
        r"""环境扩展组件是否满足应用要求：0=true, 1=false 表示该应用需要扩展组件0(cdc)以及1(java)，但是独立环境有cdc无java，不满足发布要求
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MatchExtensions

    @MatchExtensions.setter
    def MatchExtensions(self, MatchExtensions):
        self._MatchExtensions = MatchExtensions


    def _deserialize(self, params):
        self._RuntimeId = params.get("RuntimeId")
        self._DisplayName = params.get("DisplayName")
        self._Type = params.get("Type")
        self._Zone = params.get("Zone")
        self._Area = params.get("Area")
        self._Addr = params.get("Addr")
        self._Status = params.get("Status")
        self._ExpiredAt = params.get("ExpiredAt")
        self._RuntimeClass = params.get("RuntimeClass")
        self._Deployed = params.get("Deployed")
        self._MatchExtensions = params.get("MatchExtensions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuntimeMCRequest(AbstractModel):
    r"""GetRuntimeMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuntimeId: 环境id
        :type RuntimeId: int
        :param _Zone: 环境地域
        :type Zone: str
        :param _RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        """
        self._RuntimeId = None
        self._Zone = None
        self._RuntimeClass = None

    @property
    def RuntimeId(self):
        r"""环境id
        :rtype: int
        """
        return self._RuntimeId

    @RuntimeId.setter
    def RuntimeId(self, RuntimeId):
        self._RuntimeId = RuntimeId

    @property
    def Zone(self):
        r"""环境地域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def RuntimeClass(self):
        r"""环境运行类型：0:运行时类型、1:api类型
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass


    def _deserialize(self, params):
        self._RuntimeId = params.get("RuntimeId")
        self._Zone = params.get("Zone")
        self._RuntimeClass = params.get("RuntimeClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuntimeMCResponse(AbstractModel):
    r"""GetRuntimeMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Runtime: 运行时详情
        :type Runtime: :class:`tencentcloud.eis.v20210601.models.RuntimeMC`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Runtime = None
        self._RequestId = None

    @property
    def Runtime(self):
        r"""运行时详情
        :rtype: :class:`tencentcloud.eis.v20210601.models.RuntimeMC`
        """
        return self._Runtime

    @Runtime.setter
    def Runtime(self, Runtime):
        self._Runtime = Runtime

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Runtime") is not None:
            self._Runtime = RuntimeMC()
            self._Runtime._deserialize(params.get("Runtime"))
        self._RequestId = params.get("RequestId")


class GetRuntimeResourceMonitorMetricMCRequest(AbstractModel):
    r"""GetRuntimeResourceMonitorMetricMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuntimeId: 运行时id
        :type RuntimeId: int
        :param _StartTime: 起始时间
        :type StartTime: int
        :param _EndTime: 结束时间
        :type EndTime: int
        :param _MetricType: 指标类型：0:CPU, 1:MemUsageBytes, 2:K8sWorkloadNetworkReceiveBytesBw, 3:K8sWorkloadNetworkTransmitBytesBw
        :type MetricType: int
        :param _RateType: 是否返回百分比数值，仅支持CPU，Memory
        :type RateType: bool
        :param _Interval: 采样粒度：60(s), 300(s), 3600(s), 86400(s)
        :type Interval: int
        :param _RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        :param _AggregationType: 资源指标聚合类型：0: 环境维度 1:执行引擎维度 2:datatwaypy维度 3.datawayjava维度
        :type AggregationType: int
        """
        self._RuntimeId = None
        self._StartTime = None
        self._EndTime = None
        self._MetricType = None
        self._RateType = None
        self._Interval = None
        self._RuntimeClass = None
        self._AggregationType = None

    @property
    def RuntimeId(self):
        r"""运行时id
        :rtype: int
        """
        return self._RuntimeId

    @RuntimeId.setter
    def RuntimeId(self, RuntimeId):
        self._RuntimeId = RuntimeId

    @property
    def StartTime(self):
        r"""起始时间
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricType(self):
        r"""指标类型：0:CPU, 1:MemUsageBytes, 2:K8sWorkloadNetworkReceiveBytesBw, 3:K8sWorkloadNetworkTransmitBytesBw
        :rtype: int
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def RateType(self):
        r"""是否返回百分比数值，仅支持CPU，Memory
        :rtype: bool
        """
        return self._RateType

    @RateType.setter
    def RateType(self, RateType):
        self._RateType = RateType

    @property
    def Interval(self):
        r"""采样粒度：60(s), 300(s), 3600(s), 86400(s)
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RuntimeClass(self):
        r"""环境运行类型：0:运行时类型、1:api类型
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass

    @property
    def AggregationType(self):
        r"""资源指标聚合类型：0: 环境维度 1:执行引擎维度 2:datatwaypy维度 3.datawayjava维度
        :rtype: int
        """
        return self._AggregationType

    @AggregationType.setter
    def AggregationType(self, AggregationType):
        self._AggregationType = AggregationType


    def _deserialize(self, params):
        self._RuntimeId = params.get("RuntimeId")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricType = params.get("MetricType")
        self._RateType = params.get("RateType")
        self._Interval = params.get("Interval")
        self._RuntimeClass = params.get("RuntimeClass")
        self._AggregationType = params.get("AggregationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRuntimeResourceMonitorMetricMCResponse(AbstractModel):
    r"""GetRuntimeResourceMonitorMetricMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricType: 指标名称，K8sWorkloadCpuCoreUsed，K8sWorkloadMemUsageBytes，K8sWorkloadNetworkReceiveBytesBw，K8sWorkloadNetworkTransmitBytesBw
        :type MetricType: str
        :param _Values: metric数值列表
        :type Values: list of MetricValueMC
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricType = None
        self._Values = None
        self._RequestId = None

    @property
    def MetricType(self):
        r"""指标名称，K8sWorkloadCpuCoreUsed，K8sWorkloadMemUsageBytes，K8sWorkloadNetworkReceiveBytesBw，K8sWorkloadNetworkTransmitBytesBw
        :rtype: str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def Values(self):
        r"""metric数值列表
        :rtype: list of MetricValueMC
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MetricType = params.get("MetricType")
        if params.get("Values") is not None:
            self._Values = []
            for item in params.get("Values"):
                obj = MetricValueMC()
                obj._deserialize(item)
                self._Values.append(obj)
        self._RequestId = params.get("RequestId")


class ListDeployableRuntimesMCRequest(AbstractModel):
    r"""ListDeployableRuntimesMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 应用id
        :type ProjectId: int
        :param _InstanceId: 实例id
        :type InstanceId: int
        :param _PlanType: 版本类型 0-pro 1-lite
        :type PlanType: int
        :param _RuntimeClass: 0：应用集成，1：API，2：ETL
        :type RuntimeClass: int
        """
        self._ProjectId = None
        self._InstanceId = None
        self._PlanType = None
        self._RuntimeClass = None

    @property
    def ProjectId(self):
        r"""应用id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def InstanceId(self):
        r"""实例id
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PlanType(self):
        r"""版本类型 0-pro 1-lite
        :rtype: int
        """
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType

    @property
    def RuntimeClass(self):
        r"""0：应用集成，1：API，2：ETL
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._InstanceId = params.get("InstanceId")
        self._PlanType = params.get("PlanType")
        self._RuntimeClass = params.get("RuntimeClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDeployableRuntimesMCResponse(AbstractModel):
    r"""ListDeployableRuntimesMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Runtimes: 运行时列表
        :type Runtimes: list of AbstractRuntimeMC
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Runtimes = None
        self._RequestId = None

    @property
    def Runtimes(self):
        r"""运行时列表
        :rtype: list of AbstractRuntimeMC
        """
        return self._Runtimes

    @Runtimes.setter
    def Runtimes(self, Runtimes):
        self._Runtimes = Runtimes

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = AbstractRuntimeMC()
                obj._deserialize(item)
                self._Runtimes.append(obj)
        self._RequestId = params.get("RequestId")


class ListRuntimeDeployedInstancesMCRequest(AbstractModel):
    r"""ListRuntimeDeployedInstancesMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuntimeId: 运行时id
        :type RuntimeId: int
        :param _Limit: 最大请求数量
        :type Limit: int
        :param _Offset: 请求偏移量
        :type Offset: int
        :param _SortType: 排序类型：1:创建时间排序, 2:更新时间排序（默认）
        :type SortType: int
        :param _Sort: 排序方式：asc，desc（默认）
        :type Sort: str
        :param _Zone: 运行时地域
        :type Zone: str
        :param _ApiVersion: 1:3.0版本新控制台传1；否则传0
        :type ApiVersion: int
        :param _GroupId: -1:不按项目筛选，获取所有
>=0: 按项目id筛选
        :type GroupId: int
        :param _Status: -2: 不按状态筛选，获取所有
0: 运行中
2: 已停止
        :type Status: int
        :param _RuntimeClass: 0: 应用集成
1: API管理
2: ETL
        :type RuntimeClass: int
        """
        self._RuntimeId = None
        self._Limit = None
        self._Offset = None
        self._SortType = None
        self._Sort = None
        self._Zone = None
        self._ApiVersion = None
        self._GroupId = None
        self._Status = None
        self._RuntimeClass = None

    @property
    def RuntimeId(self):
        r"""运行时id
        :rtype: int
        """
        return self._RuntimeId

    @RuntimeId.setter
    def RuntimeId(self, RuntimeId):
        self._RuntimeId = RuntimeId

    @property
    def Limit(self):
        r"""最大请求数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""请求偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def SortType(self):
        r"""排序类型：1:创建时间排序, 2:更新时间排序（默认）
        :rtype: int
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Sort(self):
        r"""排序方式：asc，desc（默认）
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Zone(self):
        r"""运行时地域
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ApiVersion(self):
        r"""1:3.0版本新控制台传1；否则传0
        :rtype: int
        """
        return self._ApiVersion

    @ApiVersion.setter
    def ApiVersion(self, ApiVersion):
        self._ApiVersion = ApiVersion

    @property
    def GroupId(self):
        r"""-1:不按项目筛选，获取所有
>=0: 按项目id筛选
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Status(self):
        r"""-2: 不按状态筛选，获取所有
0: 运行中
2: 已停止
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuntimeClass(self):
        r"""0: 应用集成
1: API管理
2: ETL
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass


    def _deserialize(self, params):
        self._RuntimeId = params.get("RuntimeId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._SortType = params.get("SortType")
        self._Sort = params.get("Sort")
        self._Zone = params.get("Zone")
        self._ApiVersion = params.get("ApiVersion")
        self._GroupId = params.get("GroupId")
        self._Status = params.get("Status")
        self._RuntimeClass = params.get("RuntimeClass")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRuntimeDeployedInstancesMCResponse(AbstractModel):
    r"""ListRuntimeDeployedInstancesMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instances: 运行时所部属的应用实例列表
        :type Instances: list of RuntimeDeployedInstanceMC
        :param _TotalCount: 满足条件的记录总数，用于分页器
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instances = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Instances(self):
        r"""运行时所部属的应用实例列表
        :rtype: list of RuntimeDeployedInstanceMC
        """
        return self._Instances

    @Instances.setter
    def Instances(self, Instances):
        self._Instances = Instances

    @property
    def TotalCount(self):
        r"""满足条件的记录总数，用于分页器
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Instances") is not None:
            self._Instances = []
            for item in params.get("Instances"):
                obj = RuntimeDeployedInstanceMC()
                obj._deserialize(item)
                self._Instances.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListRuntimesMCRequest(AbstractModel):
    r"""ListRuntimesMC请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuntimeClass: 环境运行类型：0:运行时类型、1:api类型
        :type RuntimeClass: int
        :param _PlanType: 计划类型：0-pro 1-lite
        :type PlanType: int
        """
        self._RuntimeClass = None
        self._PlanType = None

    @property
    def RuntimeClass(self):
        r"""环境运行类型：0:运行时类型、1:api类型
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass

    @property
    def PlanType(self):
        r"""计划类型：0-pro 1-lite
        :rtype: int
        """
        return self._PlanType

    @PlanType.setter
    def PlanType(self, PlanType):
        self._PlanType = PlanType


    def _deserialize(self, params):
        self._RuntimeClass = params.get("RuntimeClass")
        self._PlanType = params.get("PlanType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRuntimesMCResponse(AbstractModel):
    r"""ListRuntimesMC返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Runtimes: 运行时列表
        :type Runtimes: list of RuntimeMC
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Runtimes = None
        self._RequestId = None

    @property
    def Runtimes(self):
        r"""运行时列表
        :rtype: list of RuntimeMC
        """
        return self._Runtimes

    @Runtimes.setter
    def Runtimes(self, Runtimes):
        self._Runtimes = Runtimes

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
                obj = RuntimeMC()
                obj._deserialize(item)
                self._Runtimes.append(obj)
        self._RequestId = params.get("RequestId")


class MetricValueMC(AbstractModel):
    r"""GetMonitorMetricResponse

    """

    def __init__(self):
        r"""
        :param _Time: 时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Time: int
        :param _Val: 对应的value值
注意：此字段可能返回 null，表示取不到有效值。
        :type Val: str
        """
        self._Time = None
        self._Val = None

    @property
    def Time(self):
        r"""时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Val(self):
        r"""对应的value值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Val

    @Val.setter
    def Val(self, Val):
        self._Val = Val


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Val = params.get("Val")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeDeployedInstanceMC(AbstractModel):
    r"""运行时部署的应用实例详情

    """

    def __init__(self):
        r"""
        :param _GroupId: 项目id
        :type GroupId: int
        :param _GroupName: 项目名称
        :type GroupName: str
        :param _ProjectId: 应用id
        :type ProjectId: int
        :param _ProjectName: 应用名称
        :type ProjectName: str
        :param _InstanceId: 应用实例id
        :type InstanceId: int
        :param _InstanceVersion: 应用实例版本
        :type InstanceVersion: int
        :param _InstanceCreatedAt: 应用实例创建时间
        :type InstanceCreatedAt: int
        :param _Status: 应用实例部署状态. 0:running, 1:deleting
        :type Status: int
        :param _CreatedAt: 应用实例部署创建时间
        :type CreatedAt: int
        :param _UpdatedAt: 应用实例部署更新时间
        :type UpdatedAt: int
        :param _ProjectType: 应用类型：0:NormalApp普通应用 1:TemplateApp模板应用 2:LightApp轻应用 3:MicroConnTemplate微连接模板 4:MicroConnApp微连接应用
        :type ProjectType: int
        :param _ProjectVersion: 应用版本：0:旧版 1:3.0新控制台
        :type ProjectVersion: int
        """
        self._GroupId = None
        self._GroupName = None
        self._ProjectId = None
        self._ProjectName = None
        self._InstanceId = None
        self._InstanceVersion = None
        self._InstanceCreatedAt = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._ProjectType = None
        self._ProjectVersion = None

    @property
    def GroupId(self):
        r"""项目id
        :rtype: int
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""项目名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def ProjectId(self):
        r"""应用id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        r"""应用名称
        :rtype: str
        """
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def InstanceId(self):
        r"""应用实例id
        :rtype: int
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceVersion(self):
        r"""应用实例版本
        :rtype: int
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def InstanceCreatedAt(self):
        r"""应用实例创建时间
        :rtype: int
        """
        return self._InstanceCreatedAt

    @InstanceCreatedAt.setter
    def InstanceCreatedAt(self, InstanceCreatedAt):
        self._InstanceCreatedAt = InstanceCreatedAt

    @property
    def Status(self):
        r"""应用实例部署状态. 0:running, 1:deleting
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        r"""应用实例部署创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""应用实例部署更新时间
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def ProjectType(self):
        r"""应用类型：0:NormalApp普通应用 1:TemplateApp模板应用 2:LightApp轻应用 3:MicroConnTemplate微连接模板 4:MicroConnApp微连接应用
        :rtype: int
        """
        return self._ProjectType

    @ProjectType.setter
    def ProjectType(self, ProjectType):
        self._ProjectType = ProjectType

    @property
    def ProjectVersion(self):
        r"""应用版本：0:旧版 1:3.0新控制台
        :rtype: int
        """
        return self._ProjectVersion

    @ProjectVersion.setter
    def ProjectVersion(self, ProjectVersion):
        self._ProjectVersion = ProjectVersion


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._InstanceId = params.get("InstanceId")
        self._InstanceVersion = params.get("InstanceVersion")
        self._InstanceCreatedAt = params.get("InstanceCreatedAt")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._ProjectType = params.get("ProjectType")
        self._ProjectVersion = params.get("ProjectVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeExtensionMC(AbstractModel):
    r"""运行环境扩展组件

    """

    def __init__(self):
        r"""
        :param _Type: 扩展组件类型：0:cdc 1:dataway-java
        :type Type: int
        :param _Size: 部署规格vcore数
        :type Size: float
        :param _Replica: 副本数
        :type Replica: int
        :param _Name: 扩展组件名称
        :type Name: str
        :param _Status: 状态 1:未启用 2:已启用
        :type Status: int
        :param _CreatedAt: 创建时间
        :type CreatedAt: int
        :param _UpdatedAt: 修改时间
        :type UpdatedAt: int
        """
        self._Type = None
        self._Size = None
        self._Replica = None
        self._Name = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def Type(self):
        r"""扩展组件类型：0:cdc 1:dataway-java
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        r"""部署规格vcore数
        :rtype: float
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def Replica(self):
        r"""副本数
        :rtype: int
        """
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def Name(self):
        r"""扩展组件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""状态 1:未启用 2:已启用
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        r"""创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""修改时间
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._Replica = params.get("Replica")
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuntimeMC(AbstractModel):
    r"""运行时详细信息

    """

    def __init__(self):
        r"""
        :param _RuntimeId: 环境id
        :type RuntimeId: int
        :param _Uin: 主账号uin
        :type Uin: str
        :param _DisplayName: 环境名称，用户输入，同一uin内唯一
        :type DisplayName: str
        :param _Zone: 环境所在地域，tianjin，beijiing，guangzhou等
        :type Zone: str
        :param _Type: 环境类型：0: sandbox, 1:shared, 2:private 3: trial
        :type Type: int
        :param _Status: 运行时状态：1:running, 2:deleting, 3:creating, 4:scaling, 5:unavailable, 6:deleted, 7:errored
        :type Status: int
        :param _CreatedAt: 环境创建时间
        :type CreatedAt: int
        :param _UpdatedAt: 环境更新时间
        :type UpdatedAt: int
        :param _WorkerSize: 环境资源配置，worker总配额，0:0vCore0G, 1:1vCore2G, 2:2vCore4G, 4:4vCore8G, 8:8vCore16G, 12:12vCore24G, 16:16vCore32G, 100:unlimited
        :type WorkerSize: int
        :param _WorkerReplica: 环境资源配置，worker副本数
        :type WorkerReplica: int
        :param _RunningInstanceCount: 正在运行的应用实例数量
        :type RunningInstanceCount: int
        :param _CpuUsed: 已使用cpu核数
        :type CpuUsed: float
        :param _CpuLimit: cpu核数上限
        :type CpuLimit: float
        :param _MemoryUsed: 已使用内存 MB
        :type MemoryUsed: float
        :param _MemoryLimit: 内存上限 MB
        :type MemoryLimit: float
        :param _ExpiredAt: 环境过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredAt: int
        :param _ChargeType: 收费类型：0:缺省，1:自助下单页购买(支持续费/升配等操作)，2:代销下单页购买
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: int
        :param _ResourceLimitType: 资源限制类型：0:无限制，1:有限制
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceLimitType: int
        :param _AutoRenewal: 是否开启自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewal: bool
        :param _WorkerExtensions: 扩展组件列表
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkerExtensions: list of RuntimeExtensionMC
        :param _RuntimeType: 环境类型：0: sandbox, 1:shared, 2:private 3: trial
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeType: int
        :param _RuntimeClass: 环境运行类型：0:运行时类型、1:api类型、2:etl环境
注意：此字段可能返回 null，表示取不到有效值。
        :type RuntimeClass: int
        :param _BandwidthOutUsed: 已使用出带宽 Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthOutUsed: float
        :param _BandwidthOutLimit: 出带宽上限 Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthOutLimit: float
        """
        self._RuntimeId = None
        self._Uin = None
        self._DisplayName = None
        self._Zone = None
        self._Type = None
        self._Status = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._WorkerSize = None
        self._WorkerReplica = None
        self._RunningInstanceCount = None
        self._CpuUsed = None
        self._CpuLimit = None
        self._MemoryUsed = None
        self._MemoryLimit = None
        self._ExpiredAt = None
        self._ChargeType = None
        self._ResourceLimitType = None
        self._AutoRenewal = None
        self._WorkerExtensions = None
        self._RuntimeType = None
        self._RuntimeClass = None
        self._BandwidthOutUsed = None
        self._BandwidthOutLimit = None

    @property
    def RuntimeId(self):
        r"""环境id
        :rtype: int
        """
        return self._RuntimeId

    @RuntimeId.setter
    def RuntimeId(self, RuntimeId):
        self._RuntimeId = RuntimeId

    @property
    def Uin(self):
        r"""主账号uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def DisplayName(self):
        r"""环境名称，用户输入，同一uin内唯一
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Zone(self):
        r"""环境所在地域，tianjin，beijiing，guangzhou等
        :rtype: str
        """
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def Type(self):
        r"""环境类型：0: sandbox, 1:shared, 2:private 3: trial
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        r"""运行时状态：1:running, 2:deleting, 3:creating, 4:scaling, 5:unavailable, 6:deleted, 7:errored
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedAt(self):
        r"""环境创建时间
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""环境更新时间
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def WorkerSize(self):
        r"""环境资源配置，worker总配额，0:0vCore0G, 1:1vCore2G, 2:2vCore4G, 4:4vCore8G, 8:8vCore16G, 12:12vCore24G, 16:16vCore32G, 100:unlimited
        :rtype: int
        """
        return self._WorkerSize

    @WorkerSize.setter
    def WorkerSize(self, WorkerSize):
        self._WorkerSize = WorkerSize

    @property
    def WorkerReplica(self):
        r"""环境资源配置，worker副本数
        :rtype: int
        """
        return self._WorkerReplica

    @WorkerReplica.setter
    def WorkerReplica(self, WorkerReplica):
        self._WorkerReplica = WorkerReplica

    @property
    def RunningInstanceCount(self):
        r"""正在运行的应用实例数量
        :rtype: int
        """
        return self._RunningInstanceCount

    @RunningInstanceCount.setter
    def RunningInstanceCount(self, RunningInstanceCount):
        self._RunningInstanceCount = RunningInstanceCount

    @property
    def CpuUsed(self):
        r"""已使用cpu核数
        :rtype: float
        """
        return self._CpuUsed

    @CpuUsed.setter
    def CpuUsed(self, CpuUsed):
        self._CpuUsed = CpuUsed

    @property
    def CpuLimit(self):
        r"""cpu核数上限
        :rtype: float
        """
        return self._CpuLimit

    @CpuLimit.setter
    def CpuLimit(self, CpuLimit):
        self._CpuLimit = CpuLimit

    @property
    def MemoryUsed(self):
        r"""已使用内存 MB
        :rtype: float
        """
        return self._MemoryUsed

    @MemoryUsed.setter
    def MemoryUsed(self, MemoryUsed):
        self._MemoryUsed = MemoryUsed

    @property
    def MemoryLimit(self):
        r"""内存上限 MB
        :rtype: float
        """
        return self._MemoryLimit

    @MemoryLimit.setter
    def MemoryLimit(self, MemoryLimit):
        self._MemoryLimit = MemoryLimit

    @property
    def ExpiredAt(self):
        r"""环境过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpiredAt

    @ExpiredAt.setter
    def ExpiredAt(self, ExpiredAt):
        self._ExpiredAt = ExpiredAt

    @property
    def ChargeType(self):
        r"""收费类型：0:缺省，1:自助下单页购买(支持续费/升配等操作)，2:代销下单页购买
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def ResourceLimitType(self):
        r"""资源限制类型：0:无限制，1:有限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceLimitType

    @ResourceLimitType.setter
    def ResourceLimitType(self, ResourceLimitType):
        self._ResourceLimitType = ResourceLimitType

    @property
    def AutoRenewal(self):
        r"""是否开启自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoRenewal

    @AutoRenewal.setter
    def AutoRenewal(self, AutoRenewal):
        self._AutoRenewal = AutoRenewal

    @property
    def WorkerExtensions(self):
        r"""扩展组件列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RuntimeExtensionMC
        """
        return self._WorkerExtensions

    @WorkerExtensions.setter
    def WorkerExtensions(self, WorkerExtensions):
        self._WorkerExtensions = WorkerExtensions

    @property
    def RuntimeType(self):
        r"""环境类型：0: sandbox, 1:shared, 2:private 3: trial
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RuntimeType

    @RuntimeType.setter
    def RuntimeType(self, RuntimeType):
        self._RuntimeType = RuntimeType

    @property
    def RuntimeClass(self):
        r"""环境运行类型：0:运行时类型、1:api类型、2:etl环境
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RuntimeClass

    @RuntimeClass.setter
    def RuntimeClass(self, RuntimeClass):
        self._RuntimeClass = RuntimeClass

    @property
    def BandwidthOutUsed(self):
        r"""已使用出带宽 Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._BandwidthOutUsed

    @BandwidthOutUsed.setter
    def BandwidthOutUsed(self, BandwidthOutUsed):
        self._BandwidthOutUsed = BandwidthOutUsed

    @property
    def BandwidthOutLimit(self):
        r"""出带宽上限 Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._BandwidthOutLimit

    @BandwidthOutLimit.setter
    def BandwidthOutLimit(self, BandwidthOutLimit):
        self._BandwidthOutLimit = BandwidthOutLimit


    def _deserialize(self, params):
        self._RuntimeId = params.get("RuntimeId")
        self._Uin = params.get("Uin")
        self._DisplayName = params.get("DisplayName")
        self._Zone = params.get("Zone")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._WorkerSize = params.get("WorkerSize")
        self._WorkerReplica = params.get("WorkerReplica")
        self._RunningInstanceCount = params.get("RunningInstanceCount")
        self._CpuUsed = params.get("CpuUsed")
        self._CpuLimit = params.get("CpuLimit")
        self._MemoryUsed = params.get("MemoryUsed")
        self._MemoryLimit = params.get("MemoryLimit")
        self._ExpiredAt = params.get("ExpiredAt")
        self._ChargeType = params.get("ChargeType")
        self._ResourceLimitType = params.get("ResourceLimitType")
        self._AutoRenewal = params.get("AutoRenewal")
        if params.get("WorkerExtensions") is not None:
            self._WorkerExtensions = []
            for item in params.get("WorkerExtensions"):
                obj = RuntimeExtensionMC()
                obj._deserialize(item)
                self._WorkerExtensions.append(obj)
        self._RuntimeType = params.get("RuntimeType")
        self._RuntimeClass = params.get("RuntimeClass")
        self._BandwidthOutUsed = params.get("BandwidthOutUsed")
        self._BandwidthOutLimit = params.get("BandwidthOutLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        