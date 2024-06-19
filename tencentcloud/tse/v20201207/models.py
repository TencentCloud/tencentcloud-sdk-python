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


class AccurateQpsThreshold(AbstractModel):
    """云原生网关限流插件参数限流的精确Qps阈值

    """

    def __init__(self):
        r"""
        :param _Unit: qps阈值控制维度,包含:second、minute、hour、day、month、year
        :type Unit: str
        :param _GlobalConfigId: 全局配置ID
        :type GlobalConfigId: str
        """
        self._Unit = None
        self._GlobalConfigId = None

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def GlobalConfigId(self):
        return self._GlobalConfigId

    @GlobalConfigId.setter
    def GlobalConfigId(self, GlobalConfigId):
        self._GlobalConfigId = GlobalConfigId


    def _deserialize(self, params):
        self._Unit = params.get("Unit")
        self._GlobalConfigId = params.get("GlobalConfigId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApolloEnvParam(AbstractModel):
    """Apollo 环境配置参数

    """

    def __init__(self):
        r"""
        :param _Name: 环境名称
        :type Name: str
        :param _EngineResourceSpec: 环境内引擎的节点规格 ID
-1C2G
-2C4G
兼容原spec-xxxxxx形式的规格ID
        :type EngineResourceSpec: str
        :param _EngineNodeNum: 环境内引擎的节点数量
        :type EngineNodeNum: int
        :param _StorageCapacity: 配置存储空间大小，以GB为单位
        :type StorageCapacity: int
        :param _VpcId: VPC ID。在 VPC 的子网内分配一个 IP 作为 ConfigServer 的访问地址
        :type VpcId: str
        :param _SubnetId: 子网 ID。在 VPC 的子网内分配一个 IP 作为 ConfigServer 的访问地址
        :type SubnetId: str
        :param _EnvDesc: 环境描述
        :type EnvDesc: str
        """
        self._Name = None
        self._EngineResourceSpec = None
        self._EngineNodeNum = None
        self._StorageCapacity = None
        self._VpcId = None
        self._SubnetId = None
        self._EnvDesc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EngineResourceSpec(self):
        return self._EngineResourceSpec

    @EngineResourceSpec.setter
    def EngineResourceSpec(self, EngineResourceSpec):
        self._EngineResourceSpec = EngineResourceSpec

    @property
    def EngineNodeNum(self):
        return self._EngineNodeNum

    @EngineNodeNum.setter
    def EngineNodeNum(self, EngineNodeNum):
        self._EngineNodeNum = EngineNodeNum

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

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

    @property
    def EnvDesc(self):
        return self._EnvDesc

    @EnvDesc.setter
    def EnvDesc(self, EnvDesc):
        self._EnvDesc = EnvDesc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._EngineResourceSpec = params.get("EngineResourceSpec")
        self._EngineNodeNum = params.get("EngineNodeNum")
        self._StorageCapacity = params.get("StorageCapacity")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._EnvDesc = params.get("EnvDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalerBehavior(AbstractModel):
    """指标伸缩行为

    """

    def __init__(self):
        r"""
        :param _ScaleUp: 扩容行为配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleUp: :class:`tencentcloud.tse.v20201207.models.AutoScalerRules`
        :param _ScaleDown: 缩容行为配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ScaleDown: :class:`tencentcloud.tse.v20201207.models.AutoScalerRules`
        """
        self._ScaleUp = None
        self._ScaleDown = None

    @property
    def ScaleUp(self):
        return self._ScaleUp

    @ScaleUp.setter
    def ScaleUp(self, ScaleUp):
        self._ScaleUp = ScaleUp

    @property
    def ScaleDown(self):
        return self._ScaleDown

    @ScaleDown.setter
    def ScaleDown(self, ScaleDown):
        self._ScaleDown = ScaleDown


    def _deserialize(self, params):
        if params.get("ScaleUp") is not None:
            self._ScaleUp = AutoScalerRules()
            self._ScaleUp._deserialize(params.get("ScaleUp"))
        if params.get("ScaleDown") is not None:
            self._ScaleDown = AutoScalerRules()
            self._ScaleDown._deserialize(params.get("ScaleDown"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalerPolicy(AbstractModel):
    """扩容策略

    """

    def __init__(self):
        r"""
        :param _Type: 类型，Pods
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Value: 数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        :param _PeriodSeconds: 扩容周期
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodSeconds: int
        """
        self._Type = None
        self._Value = None
        self._PeriodSeconds = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def PeriodSeconds(self):
        return self._PeriodSeconds

    @PeriodSeconds.setter
    def PeriodSeconds(self, PeriodSeconds):
        self._PeriodSeconds = PeriodSeconds


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._PeriodSeconds = params.get("PeriodSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoScalerRules(AbstractModel):
    """指标伸缩的规则

    """

    def __init__(self):
        r"""
        :param _StabilizationWindowSeconds: 稳定窗口时间，扩容时默认0，缩容时默认300
注意：此字段可能返回 null，表示取不到有效值。
        :type StabilizationWindowSeconds: int
        :param _SelectPolicy: 选择策略依据
注意：此字段可能返回 null，表示取不到有效值。
        :type SelectPolicy: str
        :param _Policies: 扩缩容策略
注意：此字段可能返回 null，表示取不到有效值。
        :type Policies: list of AutoScalerPolicy
        """
        self._StabilizationWindowSeconds = None
        self._SelectPolicy = None
        self._Policies = None

    @property
    def StabilizationWindowSeconds(self):
        return self._StabilizationWindowSeconds

    @StabilizationWindowSeconds.setter
    def StabilizationWindowSeconds(self, StabilizationWindowSeconds):
        self._StabilizationWindowSeconds = StabilizationWindowSeconds

    @property
    def SelectPolicy(self):
        return self._SelectPolicy

    @SelectPolicy.setter
    def SelectPolicy(self, SelectPolicy):
        self._SelectPolicy = SelectPolicy

    @property
    def Policies(self):
        return self._Policies

    @Policies.setter
    def Policies(self, Policies):
        self._Policies = Policies


    def _deserialize(self, params):
        self._StabilizationWindowSeconds = params.get("StabilizationWindowSeconds")
        self._SelectPolicy = params.get("SelectPolicy")
        if params.get("Policies") is not None:
            self._Policies = []
            for item in params.get("Policies"):
                obj = AutoScalerPolicy()
                obj._deserialize(item)
                self._Policies.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoScalerResourceStrategyToGroupsRequest(AbstractModel):
    """BindAutoScalerResourceStrategyToGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        :param _GroupIds: 网关分组ID列表
        :type GroupIds: list of str
        """
        self._GatewayId = None
        self._StrategyId = None
        self._GroupIds = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindAutoScalerResourceStrategyToGroupsResponse(AbstractModel):
    """BindAutoScalerResourceStrategyToGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BoundK8SInfo(AbstractModel):
    """服务治理引擎绑定的kubernetes信息

    """

    def __init__(self):
        r"""
        :param _BoundClusterId: 绑定的kubernetes集群ID
        :type BoundClusterId: str
        :param _BoundClusterType: 绑定的kubernetes的集群类型，分tke和eks两种
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundClusterType: str
        :param _SyncMode: 服务同步模式，all为全量同步，demand为按需同步
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncMode: str
        :param _BindRegion: 绑定的kubernetes集群所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type BindRegion: str
        """
        self._BoundClusterId = None
        self._BoundClusterType = None
        self._SyncMode = None
        self._BindRegion = None

    @property
    def BoundClusterId(self):
        return self._BoundClusterId

    @BoundClusterId.setter
    def BoundClusterId(self, BoundClusterId):
        self._BoundClusterId = BoundClusterId

    @property
    def BoundClusterType(self):
        return self._BoundClusterType

    @BoundClusterType.setter
    def BoundClusterType(self, BoundClusterType):
        self._BoundClusterType = BoundClusterType

    @property
    def SyncMode(self):
        return self._SyncMode

    @SyncMode.setter
    def SyncMode(self, SyncMode):
        self._SyncMode = SyncMode

    @property
    def BindRegion(self):
        return self._BindRegion

    @BindRegion.setter
    def BindRegion(self, BindRegion):
        self._BindRegion = BindRegion


    def _deserialize(self, params):
        self._BoundClusterId = params.get("BoundClusterId")
        self._BoundClusterType = params.get("BoundClusterType")
        self._SyncMode = params.get("SyncMode")
        self._BindRegion = params.get("BindRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CLBMultiRegion(AbstractModel):
    """CLB多可用区信息

    """

    def __init__(self):
        r"""
        :param _CLBMultiZoneFlag: 是否启用多可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type CLBMultiZoneFlag: bool
        :param _CLBMasterZone: 主可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CLBMasterZone: str
        :param _CLBSlaveZone: 备可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CLBSlaveZone: str
        """
        self._CLBMultiZoneFlag = None
        self._CLBMasterZone = None
        self._CLBSlaveZone = None

    @property
    def CLBMultiZoneFlag(self):
        return self._CLBMultiZoneFlag

    @CLBMultiZoneFlag.setter
    def CLBMultiZoneFlag(self, CLBMultiZoneFlag):
        self._CLBMultiZoneFlag = CLBMultiZoneFlag

    @property
    def CLBMasterZone(self):
        return self._CLBMasterZone

    @CLBMasterZone.setter
    def CLBMasterZone(self, CLBMasterZone):
        self._CLBMasterZone = CLBMasterZone

    @property
    def CLBSlaveZone(self):
        return self._CLBSlaveZone

    @CLBSlaveZone.setter
    def CLBSlaveZone(self, CLBSlaveZone):
        self._CLBSlaveZone = CLBSlaveZone


    def _deserialize(self, params):
        self._CLBMultiZoneFlag = params.get("CLBMultiZoneFlag")
        self._CLBMasterZone = params.get("CLBMasterZone")
        self._CLBSlaveZone = params.get("CLBSlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfo(AbstractModel):
    """证书信息

    """

    def __init__(self):
        r"""
        :param _Id: 唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        """
        self._Id = None

    @property
    def Id(self):
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
        


class CloseWafProtectionRequest(AbstractModel):
    """CloseWafProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Type:  防护资源的类型。
- Global  实例
- Service  服务
- Route  路由
- Object  对象
        :type Type: str
        :param _List: 当资源类型 Type 是 Service 或 Route 的时候，传入的服务或路由的列表
        :type List: list of str
        """
        self._GatewayId = None
        self._Type = None
        self._List = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Type = params.get("Type")
        self._List = params.get("List")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseWafProtectionResponse(AbstractModel):
    """CloseWafProtection返回参数结构体

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


class CloudAPIGatewayCanaryRuleList(AbstractModel):
    """灰度规则列表

    """

    def __init__(self):
        r"""
        :param _CanaryRuleList: 灰度规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CanaryRuleList: list of CloudNativeAPIGatewayCanaryRule
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._CanaryRuleList = None
        self._TotalCount = None

    @property
    def CanaryRuleList(self):
        return self._CanaryRuleList

    @CanaryRuleList.setter
    def CanaryRuleList(self, CanaryRuleList):
        self._CanaryRuleList = CanaryRuleList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("CanaryRuleList") is not None:
            self._CanaryRuleList = []
            for item in params.get("CanaryRuleList"):
                obj = CloudNativeAPIGatewayCanaryRule()
                obj._deserialize(item)
                self._CanaryRuleList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayBalancedService(AbstractModel):
    """含百分比流量配置的服务

    """

    def __init__(self):
        r"""
        :param _ServiceID: 服务 ID，作为入参时，必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceID: str
        :param _ServiceName: 服务名称，作为入参时，无意义
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _UpstreamName: Upstream 名称，作为入参时，无意义
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamName: str
        :param _Percent: 百分比，10 即 10%，范围0-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: float
        """
        self._ServiceID = None
        self._ServiceName = None
        self._UpstreamName = None
        self._Percent = None

    @property
    def ServiceID(self):
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def Percent(self):
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._ServiceID = params.get("ServiceID")
        self._ServiceName = params.get("ServiceName")
        self._UpstreamName = params.get("UpstreamName")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayCanaryRule(AbstractModel):
    """灰度规则

    """

    def __init__(self):
        r"""
        :param _Priority: 优先级，值范围为 0 到 100；值越大，优先级越高；不同规则间优先级不可重复
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _Enabled: 是否启用规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        :param _ConditionList: 参数匹配条件
注意：此字段可能返回 null，表示取不到有效值。
        :type ConditionList: list of CloudNativeAPIGatewayCanaryRuleCondition
        :param _BalancedServiceList: 服务的流量百分比配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BalancedServiceList: list of CloudNativeAPIGatewayBalancedService
        :param _ServiceId: 归属服务 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _ServiceName: 归属服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _RuleType: 灰度规则类别
Standard｜Lane
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _MatchType: 全链路灰度策略多个条件之间的匹配方式，与AND，或OR
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchType: str
        :param _GroupId: 泳道组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 泳道组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _LaneId: 泳道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneId: str
        :param _LaneName: 泳道名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneName: str
        :param _MatchMode: 泳道匹配规则：严格STRICT｜宽松PERMISSIVE
注意：此字段可能返回 null，表示取不到有效值。
        :type MatchMode: str
        :param _LaneTag: 泳道标签
注意：此字段可能返回 null，表示取不到有效值。
        :type LaneTag: str
        """
        self._Priority = None
        self._Enabled = None
        self._ConditionList = None
        self._BalancedServiceList = None
        self._ServiceId = None
        self._ServiceName = None
        self._RuleType = None
        self._MatchType = None
        self._GroupId = None
        self._GroupName = None
        self._LaneId = None
        self._LaneName = None
        self._MatchMode = None
        self._LaneTag = None

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ConditionList(self):
        return self._ConditionList

    @ConditionList.setter
    def ConditionList(self, ConditionList):
        self._ConditionList = ConditionList

    @property
    def BalancedServiceList(self):
        return self._BalancedServiceList

    @BalancedServiceList.setter
    def BalancedServiceList(self, BalancedServiceList):
        self._BalancedServiceList = BalancedServiceList

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def MatchType(self):
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def LaneId(self):
        return self._LaneId

    @LaneId.setter
    def LaneId(self, LaneId):
        self._LaneId = LaneId

    @property
    def LaneName(self):
        return self._LaneName

    @LaneName.setter
    def LaneName(self, LaneName):
        self._LaneName = LaneName

    @property
    def MatchMode(self):
        return self._MatchMode

    @MatchMode.setter
    def MatchMode(self, MatchMode):
        self._MatchMode = MatchMode

    @property
    def LaneTag(self):
        return self._LaneTag

    @LaneTag.setter
    def LaneTag(self, LaneTag):
        self._LaneTag = LaneTag


    def _deserialize(self, params):
        self._Priority = params.get("Priority")
        self._Enabled = params.get("Enabled")
        if params.get("ConditionList") is not None:
            self._ConditionList = []
            for item in params.get("ConditionList"):
                obj = CloudNativeAPIGatewayCanaryRuleCondition()
                obj._deserialize(item)
                self._ConditionList.append(obj)
        if params.get("BalancedServiceList") is not None:
            self._BalancedServiceList = []
            for item in params.get("BalancedServiceList"):
                obj = CloudNativeAPIGatewayBalancedService()
                obj._deserialize(item)
                self._BalancedServiceList.append(obj)
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._RuleType = params.get("RuleType")
        self._MatchType = params.get("MatchType")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._LaneId = params.get("LaneId")
        self._LaneName = params.get("LaneName")
        self._MatchMode = params.get("MatchMode")
        self._LaneTag = params.get("LaneTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayCanaryRuleCondition(AbstractModel):
    """灰度规则中的条件配置

    """

    def __init__(self):
        r"""
        :param _Type: 条件类型，支持 path, method, query, header, cookie, body 和 system。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Key: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Operator: 操作符，支持 "le", "eq", "lt", "ne", "ge", "gt", "regex", "exists", "in", "not in",  "prefix" ,"exact", "regex" 等
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Value: 目标参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Delimiter: 分隔符，当 Operator 为 in 或者 not in 时生效。支持值为英文逗号，英文分号，空格，换行符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Delimiter: str
        :param _GlobalConfigId: 全局配置 Id
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalConfigId: str
        :param _GlobalConfigName: 全局配置名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalConfigName: str
        """
        self._Type = None
        self._Key = None
        self._Operator = None
        self._Value = None
        self._Delimiter = None
        self._GlobalConfigId = None
        self._GlobalConfigName = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Delimiter(self):
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def GlobalConfigId(self):
        return self._GlobalConfigId

    @GlobalConfigId.setter
    def GlobalConfigId(self, GlobalConfigId):
        self._GlobalConfigId = GlobalConfigId

    @property
    def GlobalConfigName(self):
        return self._GlobalConfigName

    @GlobalConfigName.setter
    def GlobalConfigName(self, GlobalConfigName):
        self._GlobalConfigName = GlobalConfigName


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        self._Delimiter = params.get("Delimiter")
        self._GlobalConfigId = params.get("GlobalConfigId")
        self._GlobalConfigName = params.get("GlobalConfigName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayConfig(AbstractModel):
    """云原生API网关配置信息。

    """

    def __init__(self):
        r"""
        :param _ConsoleType: 控制台类型。
        :type ConsoleType: str
        :param _HttpUrl: HTTP链接地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpUrl: str
        :param _HttpsUrl: HTTPS链接地址。
        :type HttpsUrl: str
        :param _NetType: 网络类型, Open|Internal。
        :type NetType: str
        :param _AdminUser: 管理员用户名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminUser: str
        :param _AdminPassword: 管理员密码。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPassword: str
        :param _Status: 网络状态, Open|Closed|Updating
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _AccessControl: 网络访问策略
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessControl: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        :param _SubnetId: 内网子网 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _VpcId: 内网VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _Description: 负载均衡的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _SlaType: 负载均衡的规格类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaType: str
        :param _SlaName: clb规格名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaName: str
        :param _Vip: clb vip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _InternetMaxBandwidthOut: 带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _MultiZoneFlag: 是否多可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiZoneFlag: bool
        :param _MasterZoneId: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZoneId: str
        :param _SlaveZoneId: 备可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZoneId: str
        :param _MasterZoneName: 主可用区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZoneName: str
        :param _SlaveZoneName: 备可用区名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZoneName: str
        :param _NetworkId: 网络 id
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkId: str
        """
        self._ConsoleType = None
        self._HttpUrl = None
        self._HttpsUrl = None
        self._NetType = None
        self._AdminUser = None
        self._AdminPassword = None
        self._Status = None
        self._AccessControl = None
        self._SubnetId = None
        self._VpcId = None
        self._Description = None
        self._SlaType = None
        self._SlaName = None
        self._Vip = None
        self._InternetMaxBandwidthOut = None
        self._MultiZoneFlag = None
        self._MasterZoneId = None
        self._SlaveZoneId = None
        self._MasterZoneName = None
        self._SlaveZoneName = None
        self._NetworkId = None

    @property
    def ConsoleType(self):
        return self._ConsoleType

    @ConsoleType.setter
    def ConsoleType(self, ConsoleType):
        self._ConsoleType = ConsoleType

    @property
    def HttpUrl(self):
        return self._HttpUrl

    @HttpUrl.setter
    def HttpUrl(self, HttpUrl):
        self._HttpUrl = HttpUrl

    @property
    def HttpsUrl(self):
        return self._HttpsUrl

    @HttpsUrl.setter
    def HttpsUrl(self, HttpsUrl):
        self._HttpsUrl = HttpsUrl

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def AdminUser(self):
        return self._AdminUser

    @AdminUser.setter
    def AdminUser(self, AdminUser):
        self._AdminUser = AdminUser

    @property
    def AdminPassword(self):
        return self._AdminPassword

    @AdminPassword.setter
    def AdminPassword(self, AdminPassword):
        self._AdminPassword = AdminPassword

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccessControl(self):
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def SlaName(self):
        return self._SlaName

    @SlaName.setter
    def SlaName(self, SlaName):
        self._SlaName = SlaName

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def MultiZoneFlag(self):
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def MasterZoneId(self):
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId

    @property
    def MasterZoneName(self):
        return self._MasterZoneName

    @MasterZoneName.setter
    def MasterZoneName(self, MasterZoneName):
        self._MasterZoneName = MasterZoneName

    @property
    def SlaveZoneName(self):
        return self._SlaveZoneName

    @SlaveZoneName.setter
    def SlaveZoneName(self, SlaveZoneName):
        self._SlaveZoneName = SlaveZoneName

    @property
    def NetworkId(self):
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId


    def _deserialize(self, params):
        self._ConsoleType = params.get("ConsoleType")
        self._HttpUrl = params.get("HttpUrl")
        self._HttpsUrl = params.get("HttpsUrl")
        self._NetType = params.get("NetType")
        self._AdminUser = params.get("AdminUser")
        self._AdminPassword = params.get("AdminPassword")
        self._Status = params.get("Status")
        if params.get("AccessControl") is not None:
            self._AccessControl = NetworkAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        self._SubnetId = params.get("SubnetId")
        self._VpcId = params.get("VpcId")
        self._Description = params.get("Description")
        self._SlaType = params.get("SlaType")
        self._SlaName = params.get("SlaName")
        self._Vip = params.get("Vip")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._MasterZoneId = params.get("MasterZoneId")
        self._SlaveZoneId = params.get("SlaveZoneId")
        self._MasterZoneName = params.get("MasterZoneName")
        self._SlaveZoneName = params.get("SlaveZoneName")
        self._NetworkId = params.get("NetworkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayNode(AbstractModel):
    """云原生API网关节点信息。

    """

    def __init__(self):
        r"""
        :param _NodeId: 云原生网关节点 id
        :type NodeId: str
        :param _NodeIp: 节点 ip
        :type NodeIp: str
        :param _ZoneId: Zone id
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Zone: Zone
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 分组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Weight: 节点权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _IsDefaultWeight: 是否默认权重
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDefaultWeight: bool
        """
        self._NodeId = None
        self._NodeIp = None
        self._ZoneId = None
        self._Zone = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None
        self._Weight = None
        self._IsDefaultWeight = None

    @property
    def NodeId(self):
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeIp(self):
        return self._NodeIp

    @NodeIp.setter
    def NodeIp(self, NodeIp):
        self._NodeIp = NodeIp

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def IsDefaultWeight(self):
        return self._IsDefaultWeight

    @IsDefaultWeight.setter
    def IsDefaultWeight(self, IsDefaultWeight):
        self._IsDefaultWeight = IsDefaultWeight


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeIp = params.get("NodeIp")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._IsDefaultWeight = params.get("IsDefaultWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayNodeConfig(AbstractModel):
    """云原生API网关节点配置。

    """

    def __init__(self):
        r"""
        :param _Specification: 节点配置, 1c2g|2c4g|4c8g|8c16g。
注意：此字段可能返回 null，表示取不到有效值。
        :type Specification: str
        :param _Number: 节点数量，2-9。
注意：此字段可能返回 null，表示取不到有效值。
        :type Number: int
        """
        self._Specification = None
        self._Number = None

    @property
    def Specification(self):
        return self._Specification

    @Specification.setter
    def Specification(self, Specification):
        self._Specification = Specification

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._Specification = params.get("Specification")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayRateLimitDetail(AbstractModel):
    """云原生网关Tse 限流插件配置

    """

    def __init__(self):
        r"""
        :param _Enabled: 插件启用状态
        :type Enabled: bool
        :param _QpsThresholds: qps阈值
        :type QpsThresholds: list of QpsThreshold
        :param _Path: 需要进行流量控制的请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Header: 需要进行流量控制的请求头Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: str
        :param _LimitBy: 限流依据
ip service consumer credential path header
        :type LimitBy: str
        :param _ExternalRedis: 外部redis配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ExternalRedis: :class:`tencentcloud.tse.v20201207.models.ExternalRedis`
        :param _Policy: 计数器策略 
local 单机
redis  默认redis
external_redis 外部redis

注意：此字段可能返回 null，表示取不到有效值。
        :type Policy: str
        :param _RateLimitResponse: 响应配置，响应策略为text

注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitResponse: :class:`tencentcloud.tse.v20201207.models.RateLimitResponse`
        :param _RateLimitResponseUrl: 请求转发地址
注意：此字段可能返回 null，表示取不到有效值。
        :type RateLimitResponseUrl: str
        :param _ResponseType: 响应策略
url请求转发
text 响应配置
default 直接返回

        :type ResponseType: str
        :param _HideClientHeaders: 是否隐藏限流客户端响应头
        :type HideClientHeaders: bool
        :param _LineUpTime: 排队时间
        :type LineUpTime: int
        :param _IsDelay: 是否开启请求排队
        :type IsDelay: bool
        :param _BasicLimitQpsThresholds: 基础限流
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicLimitQpsThresholds: list of QpsThreshold
        :param _LimitRules: 参数限流的规则
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitRules: list of LimitRule
        """
        self._Enabled = None
        self._QpsThresholds = None
        self._Path = None
        self._Header = None
        self._LimitBy = None
        self._ExternalRedis = None
        self._Policy = None
        self._RateLimitResponse = None
        self._RateLimitResponseUrl = None
        self._ResponseType = None
        self._HideClientHeaders = None
        self._LineUpTime = None
        self._IsDelay = None
        self._BasicLimitQpsThresholds = None
        self._LimitRules = None

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def QpsThresholds(self):
        return self._QpsThresholds

    @QpsThresholds.setter
    def QpsThresholds(self, QpsThresholds):
        self._QpsThresholds = QpsThresholds

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Header(self):
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def LimitBy(self):
        return self._LimitBy

    @LimitBy.setter
    def LimitBy(self, LimitBy):
        self._LimitBy = LimitBy

    @property
    def ExternalRedis(self):
        return self._ExternalRedis

    @ExternalRedis.setter
    def ExternalRedis(self, ExternalRedis):
        self._ExternalRedis = ExternalRedis

    @property
    def Policy(self):
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def RateLimitResponse(self):
        return self._RateLimitResponse

    @RateLimitResponse.setter
    def RateLimitResponse(self, RateLimitResponse):
        self._RateLimitResponse = RateLimitResponse

    @property
    def RateLimitResponseUrl(self):
        return self._RateLimitResponseUrl

    @RateLimitResponseUrl.setter
    def RateLimitResponseUrl(self, RateLimitResponseUrl):
        self._RateLimitResponseUrl = RateLimitResponseUrl

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def HideClientHeaders(self):
        return self._HideClientHeaders

    @HideClientHeaders.setter
    def HideClientHeaders(self, HideClientHeaders):
        self._HideClientHeaders = HideClientHeaders

    @property
    def LineUpTime(self):
        return self._LineUpTime

    @LineUpTime.setter
    def LineUpTime(self, LineUpTime):
        self._LineUpTime = LineUpTime

    @property
    def IsDelay(self):
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

    @property
    def BasicLimitQpsThresholds(self):
        return self._BasicLimitQpsThresholds

    @BasicLimitQpsThresholds.setter
    def BasicLimitQpsThresholds(self, BasicLimitQpsThresholds):
        self._BasicLimitQpsThresholds = BasicLimitQpsThresholds

    @property
    def LimitRules(self):
        return self._LimitRules

    @LimitRules.setter
    def LimitRules(self, LimitRules):
        self._LimitRules = LimitRules


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        if params.get("QpsThresholds") is not None:
            self._QpsThresholds = []
            for item in params.get("QpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._QpsThresholds.append(obj)
        self._Path = params.get("Path")
        self._Header = params.get("Header")
        self._LimitBy = params.get("LimitBy")
        if params.get("ExternalRedis") is not None:
            self._ExternalRedis = ExternalRedis()
            self._ExternalRedis._deserialize(params.get("ExternalRedis"))
        self._Policy = params.get("Policy")
        if params.get("RateLimitResponse") is not None:
            self._RateLimitResponse = RateLimitResponse()
            self._RateLimitResponse._deserialize(params.get("RateLimitResponse"))
        self._RateLimitResponseUrl = params.get("RateLimitResponseUrl")
        self._ResponseType = params.get("ResponseType")
        self._HideClientHeaders = params.get("HideClientHeaders")
        self._LineUpTime = params.get("LineUpTime")
        self._IsDelay = params.get("IsDelay")
        if params.get("BasicLimitQpsThresholds") is not None:
            self._BasicLimitQpsThresholds = []
            for item in params.get("BasicLimitQpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._BasicLimitQpsThresholds.append(obj)
        if params.get("LimitRules") is not None:
            self._LimitRules = []
            for item in params.get("LimitRules"):
                obj = LimitRule()
                obj._deserialize(item)
                self._LimitRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategy(AbstractModel):
    """网关实例策略

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略ID
        :type StrategyId: str
        :param _StrategyName: 策略名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _Description: 策略描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Config: 弹性伸缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        :param _GatewayId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _CronConfig: 定时伸缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CronConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        :param _MaxReplicas: 最大节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        """
        self._StrategyId = None
        self._StrategyName = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Description = None
        self._Config = None
        self._GatewayId = None
        self._CronConfig = None
        self._MaxReplicas = None

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def CronConfig(self):
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig

    @property
    def MaxReplicas(self):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        self._MaxReplicas = MaxReplicas


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Description = params.get("Description")
        if params.get("Config") is not None:
            self._Config = CloudNativeAPIGatewayStrategyAutoScalerConfig()
            self._Config._deserialize(params.get("Config"))
        self._GatewayId = params.get("GatewayId")
        if params.get("CronConfig") is not None:
            self._CronConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronConfig._deserialize(params.get("CronConfig"))
        self._MaxReplicas = params.get("MaxReplicas")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyAutoScalerConfig(AbstractModel):
    """弹性伸缩策略

    """

    def __init__(self):
        r"""
        :param _MaxReplicas: 最大副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxReplicas: int
        :param _Metrics: 指标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Metrics: list of CloudNativeAPIGatewayStrategyAutoScalerConfigMetric
        :param _Enabled: 是否开启指标伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _StrategyId: 弹性策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: str
        :param _AutoScalerId: 指标配置ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoScalerId: str
        :param _Behavior: 指标伸缩行为配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Behavior: :class:`tencentcloud.tse.v20201207.models.AutoScalerBehavior`
        """
        self._MaxReplicas = None
        self._Metrics = None
        self._Enabled = None
        self._CreateTime = None
        self._ModifyTime = None
        self._StrategyId = None
        self._AutoScalerId = None
        self._Behavior = None

    @property
    def MaxReplicas(self):
        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        self._MaxReplicas = MaxReplicas

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Enabled(self):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        self._Enabled = Enabled

    @property
    def CreateTime(self):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        self._ModifyTime = ModifyTime

    @property
    def StrategyId(self):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        self._StrategyId = StrategyId

    @property
    def AutoScalerId(self):
        warnings.warn("parameter `AutoScalerId` is deprecated", DeprecationWarning) 

        return self._AutoScalerId

    @AutoScalerId.setter
    def AutoScalerId(self, AutoScalerId):
        warnings.warn("parameter `AutoScalerId` is deprecated", DeprecationWarning) 

        self._AutoScalerId = AutoScalerId

    @property
    def Behavior(self):
        return self._Behavior

    @Behavior.setter
    def Behavior(self, Behavior):
        self._Behavior = Behavior


    def _deserialize(self, params):
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("Metrics") is not None:
            self._Metrics = []
            for item in params.get("Metrics"):
                obj = CloudNativeAPIGatewayStrategyAutoScalerConfigMetric()
                obj._deserialize(item)
                self._Metrics.append(obj)
        self._Enabled = params.get("Enabled")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._StrategyId = params.get("StrategyId")
        self._AutoScalerId = params.get("AutoScalerId")
        if params.get("Behavior") is not None:
            self._Behavior = AutoScalerBehavior()
            self._Behavior._deserialize(params.get("Behavior"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyAutoScalerConfigMetric(AbstractModel):
    """弹性伸缩配置指标

    """

    def __init__(self):
        r"""
        :param _Type: 指标类型
- Resource
        :type Type: str
        :param _ResourceName: 指标资源名称
- cpu
- memory
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _TargetType: 指标目标类型，目前只支持百分比Utilization
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetType: str
        :param _TargetValue: 指标目标值
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetValue: int
        """
        self._Type = None
        self._ResourceName = None
        self._TargetType = None
        self._TargetValue = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceName(self):
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetValue(self):
        return self._TargetValue

    @TargetValue.setter
    def TargetValue(self, TargetValue):
        self._TargetValue = TargetValue


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ResourceName = params.get("ResourceName")
        self._TargetType = params.get("TargetType")
        self._TargetValue = params.get("TargetValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyBindingGroupInfo(AbstractModel):
    """策略绑定的网关分组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 网关分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _NodeConfig: 节点配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _BindTime: 绑定时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BindTime: str
        :param _GroupName: 网关分组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _Status: 绑定状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._GroupId = None
        self._NodeConfig = None
        self._BindTime = None
        self._GroupName = None
        self._Status = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NodeConfig(self):
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def BindTime(self):
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        self._BindTime = params.get("BindTime")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyCronScalerConfig(AbstractModel):
    """定时伸缩策略配置

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启定时伸缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: bool
        :param _Params: 定时伸缩配置参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Params: list of CloudNativeAPIGatewayStrategyCronScalerConfigParam
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _StrategyId: 弹性策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: str
        """
        self._Enabled = None
        self._Params = None
        self._CreateTime = None
        self._ModifyTime = None
        self._StrategyId = None

    @property
    def Enabled(self):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        warnings.warn("parameter `Enabled` is deprecated", DeprecationWarning) 

        self._Enabled = Enabled

    @property
    def Params(self):
        return self._Params

    @Params.setter
    def Params(self, Params):
        self._Params = Params

    @property
    def CreateTime(self):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        warnings.warn("parameter `CreateTime` is deprecated", DeprecationWarning) 

        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        warnings.warn("parameter `ModifyTime` is deprecated", DeprecationWarning) 

        self._ModifyTime = ModifyTime

    @property
    def StrategyId(self):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        warnings.warn("parameter `StrategyId` is deprecated", DeprecationWarning) 

        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        if params.get("Params") is not None:
            self._Params = []
            for item in params.get("Params"):
                obj = CloudNativeAPIGatewayStrategyCronScalerConfigParam()
                obj._deserialize(item)
                self._Params.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayStrategyCronScalerConfigParam(AbstractModel):
    """定时伸缩配置参数

    """

    def __init__(self):
        r"""
        :param _Period: 定时伸缩周期
注意：此字段可能返回 null，表示取不到有效值。
        :type Period: str
        :param _StartAt: 定时伸缩开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartAt: str
        :param _TargetReplicas: 定时伸缩目标节点数，不超过指标伸缩中定义的最大节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetReplicas: int
        :param _Crontab: 定时伸缩cron表达式，无需输入
注意：此字段可能返回 null，表示取不到有效值。
        :type Crontab: str
        """
        self._Period = None
        self._StartAt = None
        self._TargetReplicas = None
        self._Crontab = None

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartAt(self):
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def TargetReplicas(self):
        return self._TargetReplicas

    @TargetReplicas.setter
    def TargetReplicas(self, TargetReplicas):
        self._TargetReplicas = TargetReplicas

    @property
    def Crontab(self):
        return self._Crontab

    @Crontab.setter
    def Crontab(self, Crontab):
        self._Crontab = Crontab


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StartAt = params.get("StartAt")
        self._TargetReplicas = params.get("TargetReplicas")
        self._Crontab = params.get("Crontab")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudNativeAPIGatewayVpcConfig(AbstractModel):
    """云原生API网关vpc配置。

    """

    def __init__(self):
        r"""
        :param _VpcId: 私有网络ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网ID。
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ConfigFile(AbstractModel):
    """配置文件

    """

    def __init__(self):
        r"""
        :param _Id: 配置文件id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 配置文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 配置文件命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Group: 配置文件组
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: str
        :param _Content: 配置文件内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Format: 配置文件格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _Comment: 配置文件注释
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Status: 配置文件状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Tags: 配置文件标签数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ConfigFileTag
        :param _CreateTime: 配置文件创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CreateBy: 配置文件创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateBy: str
        :param _ModifyTime: 配置文件修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _ModifyBy: 配置文件修改者
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyBy: str
        :param _ReleaseTime: 配置文件发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        :param _ReleaseBy: 配置文件发布者
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseBy: str
        """
        self._Id = None
        self._Name = None
        self._Namespace = None
        self._Group = None
        self._Content = None
        self._Format = None
        self._Comment = None
        self._Status = None
        self._Tags = None
        self._CreateTime = None
        self._CreateBy = None
        self._ModifyTime = None
        self._ModifyBy = None
        self._ReleaseTime = None
        self._ReleaseBy = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyBy(self):
        return self._ModifyBy

    @ModifyBy.setter
    def ModifyBy(self, ModifyBy):
        self._ModifyBy = ModifyBy

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime

    @property
    def ReleaseBy(self):
        return self._ReleaseBy

    @ReleaseBy.setter
    def ReleaseBy(self, ReleaseBy):
        self._ReleaseBy = ReleaseBy


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Content = params.get("Content")
        self._Format = params.get("Format")
        self._Comment = params.get("Comment")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ConfigFileTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._CreateBy = params.get("CreateBy")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyBy = params.get("ModifyBy")
        self._ReleaseTime = params.get("ReleaseTime")
        self._ReleaseBy = params.get("ReleaseBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigFileGroup(AbstractModel):
    """配置文件组

    """

    def __init__(self):
        r"""
        :param _Id: 配置文件组id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 配置文件组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Comment: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CreateBy: 创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateBy: str
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _ModifyBy: 修改者
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyBy: str
        :param _FileCount: 文件数
注意：此字段可能返回 null，表示取不到有效值。
        :type FileCount: int
        :param _UserIds: 关联用户，link_users
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIds: list of str
        :param _GroupIds: 组id，link_groups
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupIds: list of str
        :param _RemoveUserIds: remove_link_users
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveUserIds: list of str
        :param _RemoveGroupIds: remove_link_groups
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveGroupIds: list of str
        :param _Editable: 是否可编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type Editable: bool
        :param _Owner: 归属者
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param _Department: 部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: str
        :param _Business: 业务
注意：此字段可能返回 null，表示取不到有效值。
        :type Business: str
        :param _ConfigFileGroupTags: 配置文件组标签
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFileGroupTags: list of ConfigFileGroupTag
        """
        self._Id = None
        self._Name = None
        self._Namespace = None
        self._Comment = None
        self._CreateTime = None
        self._CreateBy = None
        self._ModifyTime = None
        self._ModifyBy = None
        self._FileCount = None
        self._UserIds = None
        self._GroupIds = None
        self._RemoveUserIds = None
        self._RemoveGroupIds = None
        self._Editable = None
        self._Owner = None
        self._Department = None
        self._Business = None
        self._ConfigFileGroupTags = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyBy(self):
        return self._ModifyBy

    @ModifyBy.setter
    def ModifyBy(self, ModifyBy):
        self._ModifyBy = ModifyBy

    @property
    def FileCount(self):
        return self._FileCount

    @FileCount.setter
    def FileCount(self, FileCount):
        self._FileCount = FileCount

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RemoveUserIds(self):
        return self._RemoveUserIds

    @RemoveUserIds.setter
    def RemoveUserIds(self, RemoveUserIds):
        self._RemoveUserIds = RemoveUserIds

    @property
    def RemoveGroupIds(self):
        return self._RemoveGroupIds

    @RemoveGroupIds.setter
    def RemoveGroupIds(self, RemoveGroupIds):
        self._RemoveGroupIds = RemoveGroupIds

    @property
    def Editable(self):
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def ConfigFileGroupTags(self):
        return self._ConfigFileGroupTags

    @ConfigFileGroupTags.setter
    def ConfigFileGroupTags(self, ConfigFileGroupTags):
        self._ConfigFileGroupTags = ConfigFileGroupTags


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Comment = params.get("Comment")
        self._CreateTime = params.get("CreateTime")
        self._CreateBy = params.get("CreateBy")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyBy = params.get("ModifyBy")
        self._FileCount = params.get("FileCount")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._RemoveUserIds = params.get("RemoveUserIds")
        self._RemoveGroupIds = params.get("RemoveGroupIds")
        self._Editable = params.get("Editable")
        self._Owner = params.get("Owner")
        self._Department = params.get("Department")
        self._Business = params.get("Business")
        if params.get("ConfigFileGroupTags") is not None:
            self._ConfigFileGroupTags = []
            for item in params.get("ConfigFileGroupTags"):
                obj = ConfigFileGroupTag()
                obj._deserialize(item)
                self._ConfigFileGroupTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigFileGroupTag(AbstractModel):
    """配置文件标签

    """

    def __init__(self):
        r"""
        :param _Key: key-value 键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: key-value 值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ConfigFilePublishInfo(AbstractModel):
    """发布详情

    """

    def __init__(self):
        r"""
        :param _ReleaseName: 发布名称
        :type ReleaseName: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 发布组
        :type Group: str
        :param _FileName: 文件名
        :type FileName: str
        :param _Content: 内容
        :type Content: str
        :param _Comment: 描述
        :type Comment: str
        :param _Format: 格式
        :type Format: str
        :param _CreateBy: 创建者
        :type CreateBy: str
        :param _ModifyBy: 修改者
        :type ModifyBy: str
        :param _Tags: 标签
        :type Tags: list of ConfigFileTag
        """
        self._ReleaseName = None
        self._Namespace = None
        self._Group = None
        self._FileName = None
        self._Content = None
        self._Comment = None
        self._Format = None
        self._CreateBy = None
        self._ModifyBy = None
        self._Tags = None

    @property
    def ReleaseName(self):
        return self._ReleaseName

    @ReleaseName.setter
    def ReleaseName(self, ReleaseName):
        self._ReleaseName = ReleaseName

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def ModifyBy(self):
        return self._ModifyBy

    @ModifyBy.setter
    def ModifyBy(self, ModifyBy):
        self._ModifyBy = ModifyBy

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ReleaseName = params.get("ReleaseName")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        self._Content = params.get("Content")
        self._Comment = params.get("Comment")
        self._Format = params.get("Format")
        self._CreateBy = params.get("CreateBy")
        self._ModifyBy = params.get("ModifyBy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ConfigFileTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigFileRelease(AbstractModel):
    """配置文件发布

    """

    def __init__(self):
        r"""
        :param _Id: 配置文件发布id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 配置文件发布名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 配置文件发布命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Group: 配置文件发布组
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: str
        :param _FileName: 配置文件发布文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _Content: 配置文件发布内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Comment: 配置文件发布注释
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Md5: 配置文件发布Md5
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param _Version: 配置文件发布版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param _CreateTime: 配置文件发布创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CreateBy: 配置文件发布创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateBy: str
        :param _ModifyTime: 配置文件发布修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _ModifyBy: 配置文件发布修改者
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyBy: str
        :param _ReleaseDescription: 发布描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDescription: str
        :param _Active: 是否生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Active: bool
        :param _Format: 格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        """
        self._Id = None
        self._Name = None
        self._Namespace = None
        self._Group = None
        self._FileName = None
        self._Content = None
        self._Comment = None
        self._Md5 = None
        self._Version = None
        self._CreateTime = None
        self._CreateBy = None
        self._ModifyTime = None
        self._ModifyBy = None
        self._ReleaseDescription = None
        self._Active = None
        self._Format = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyBy(self):
        return self._ModifyBy

    @ModifyBy.setter
    def ModifyBy(self, ModifyBy):
        self._ModifyBy = ModifyBy

    @property
    def ReleaseDescription(self):
        return self._ReleaseDescription

    @ReleaseDescription.setter
    def ReleaseDescription(self, ReleaseDescription):
        self._ReleaseDescription = ReleaseDescription

    @property
    def Active(self):
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        self._Content = params.get("Content")
        self._Comment = params.get("Comment")
        self._Md5 = params.get("Md5")
        self._Version = params.get("Version")
        self._CreateTime = params.get("CreateTime")
        self._CreateBy = params.get("CreateBy")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyBy = params.get("ModifyBy")
        self._ReleaseDescription = params.get("ReleaseDescription")
        self._Active = params.get("Active")
        self._Format = params.get("Format")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigFileReleaseDeletion(AbstractModel):
    """配置发布删除

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Group: 配置分组
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: str
        :param _FileName: 文件名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _ReleaseVersion: 发布版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseVersion: str
        """
        self._Namespace = None
        self._Group = None
        self._FileName = None
        self._ReleaseVersion = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def ReleaseVersion(self):
        return self._ReleaseVersion

    @ReleaseVersion.setter
    def ReleaseVersion(self, ReleaseVersion):
        self._ReleaseVersion = ReleaseVersion


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        self._ReleaseVersion = params.get("ReleaseVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigFileReleaseHistory(AbstractModel):
    """配置文件发布历史

    """

    def __init__(self):
        r"""
        :param _Id: 配置文件发布历史记录id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 配置文件发布历史名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 配置文件发布历史命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Group: 配置文件发布历史组
注意：此字段可能返回 null，表示取不到有效值。
        :type Group: str
        :param _FileName: 配置文件发布历史名称
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _Content: 配置文件发布历史内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Format: 配置文件发布历史格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _Comment: 配置文件发布历史注释
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _Md5: 配置文件发布历史Md5
注意：此字段可能返回 null，表示取不到有效值。
        :type Md5: str
        :param _Type: 配置文件发布历史类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status: 配置文件发布历史状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Tags: 配置文件发布历史标签组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ConfigFileTag
        :param _CreateTime: 配置文件发布创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CreateBy: 配置文件发布创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateBy: str
        :param _ModifyTime: 配置文件发布修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _ModifyBy: 配置文件发布修改者
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyBy: str
        :param _ReleaseDescription: 发布描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDescription: str
        :param _ReleaseReason: 原因，用于失败时原因展示
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseReason: str
        """
        self._Id = None
        self._Name = None
        self._Namespace = None
        self._Group = None
        self._FileName = None
        self._Content = None
        self._Format = None
        self._Comment = None
        self._Md5 = None
        self._Type = None
        self._Status = None
        self._Tags = None
        self._CreateTime = None
        self._CreateBy = None
        self._ModifyTime = None
        self._ModifyBy = None
        self._ReleaseDescription = None
        self._ReleaseReason = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Md5(self):
        return self._Md5

    @Md5.setter
    def Md5(self, Md5):
        self._Md5 = Md5

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyBy(self):
        return self._ModifyBy

    @ModifyBy.setter
    def ModifyBy(self, ModifyBy):
        self._ModifyBy = ModifyBy

    @property
    def ReleaseDescription(self):
        return self._ReleaseDescription

    @ReleaseDescription.setter
    def ReleaseDescription(self, ReleaseDescription):
        self._ReleaseDescription = ReleaseDescription

    @property
    def ReleaseReason(self):
        return self._ReleaseReason

    @ReleaseReason.setter
    def ReleaseReason(self, ReleaseReason):
        self._ReleaseReason = ReleaseReason


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        self._Content = params.get("Content")
        self._Format = params.get("Format")
        self._Comment = params.get("Comment")
        self._Md5 = params.get("Md5")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ConfigFileTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._CreateBy = params.get("CreateBy")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyBy = params.get("ModifyBy")
        self._ReleaseDescription = params.get("ReleaseDescription")
        self._ReleaseReason = params.get("ReleaseReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigFileTag(AbstractModel):
    """配置文件标签

    """

    def __init__(self):
        r"""
        :param _Key: key-value 键
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: key-value 值
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ConfigFileTemplate(AbstractModel):
    """配置文件模板

    """

    def __init__(self):
        r"""
        :param _Id: 配置文件模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 配置文件模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Content: 配置文件模板内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Format: 配置文件模板格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Format: str
        :param _Comment: 配置文件模板注释
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreateTime: 配置文件模板创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _CreateBy: 配置文件模板创建者
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateBy: str
        :param _ModifyTime: 配置文件模板修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _ModifyBy: 配置文件模板修改者
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyBy: str
        """
        self._Id = None
        self._Name = None
        self._Content = None
        self._Format = None
        self._Comment = None
        self._CreateTime = None
        self._CreateBy = None
        self._ModifyTime = None
        self._ModifyBy = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def CreateBy(self):
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def ModifyBy(self):
        return self._ModifyBy

    @ModifyBy.setter
    def ModifyBy(self, ModifyBy):
        self._ModifyBy = ModifyBy


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Format = params.get("Format")
        self._Comment = params.get("Comment")
        self._CreateTime = params.get("CreateTime")
        self._CreateBy = params.get("CreateBy")
        self._ModifyTime = params.get("ModifyTime")
        self._ModifyBy = params.get("ModifyBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalerResourceStrategyRequest(AbstractModel):
    """CreateAutoScalerResourceStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyName: 策略名称
        :type StrategyName: str
        :param _Description: 策略描述
        :type Description: str
        :param _Config: 指标伸缩配置
        :type Config: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        :param _CronScalerConfig: 定时伸缩配置列表
        :type CronScalerConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        :param _MaxReplicas: 最大节点数
        :type MaxReplicas: int
        :param _CronConfig: 定时伸缩配置
        :type CronConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        self._GatewayId = None
        self._StrategyName = None
        self._Description = None
        self._Config = None
        self._CronScalerConfig = None
        self._MaxReplicas = None
        self._CronConfig = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CronScalerConfig(self):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        return self._CronScalerConfig

    @CronScalerConfig.setter
    def CronScalerConfig(self, CronScalerConfig):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        self._CronScalerConfig = CronScalerConfig

    @property
    def MaxReplicas(self):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        self._MaxReplicas = MaxReplicas

    @property
    def CronConfig(self):
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyName = params.get("StrategyName")
        self._Description = params.get("Description")
        if params.get("Config") is not None:
            self._Config = CloudNativeAPIGatewayStrategyAutoScalerConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("CronScalerConfig") is not None:
            self._CronScalerConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronScalerConfig._deserialize(params.get("CronScalerConfig"))
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("CronConfig") is not None:
            self._CronConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronConfig._deserialize(params.get("CronConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAutoScalerResourceStrategyResponse(AbstractModel):
    """CreateAutoScalerResourceStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _StrategyId: 策略Id
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._StrategyId = None
        self._RequestId = None

    @property
    def Result(self):
        warnings.warn("parameter `Result` is deprecated", DeprecationWarning) 

        return self._Result

    @Result.setter
    def Result(self, Result):
        warnings.warn("parameter `Result` is deprecated", DeprecationWarning) 

        self._Result = Result

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._StrategyId = params.get("StrategyId")
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayCanaryRuleRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayCanaryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关 ID
        :type GatewayId: str
        :param _ServiceId: 服务 ID
        :type ServiceId: str
        :param _CanaryRule: 灰度规则配置
        :type CanaryRule: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        """
        self._GatewayId = None
        self._ServiceId = None
        self._CanaryRule = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def CanaryRule(self):
        return self._CanaryRule

    @CanaryRule.setter
    def CanaryRule(self, CanaryRule):
        self._CanaryRule = CanaryRule


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        if params.get("CanaryRule") is not None:
            self._CanaryRule = CloudNativeAPIGatewayCanaryRule()
            self._CanaryRule._deserialize(params.get("CanaryRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayCanaryRuleResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayCanaryRule返回参数结构体

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


class CreateCloudNativeAPIGatewayCertificateRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _BindDomains: 绑定的域名
        :type BindDomains: list of str
        :param _CertId: ssl平台证书 Id
        :type CertId: str
        :param _Name: 证书名称
        :type Name: str
        :param _Key: 证书私钥
        :type Key: str
        :param _Crt: 证书pem格式
        :type Crt: str
        """
        self._GatewayId = None
        self._BindDomains = None
        self._CertId = None
        self._Name = None
        self._Key = None
        self._Crt = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def BindDomains(self):
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        warnings.warn("parameter `Key` is deprecated", DeprecationWarning) 

        return self._Key

    @Key.setter
    def Key(self, Key):
        warnings.warn("parameter `Key` is deprecated", DeprecationWarning) 

        self._Key = Key

    @property
    def Crt(self):
        warnings.warn("parameter `Crt` is deprecated", DeprecationWarning) 

        return self._Crt

    @Crt.setter
    def Crt(self, Crt):
        warnings.warn("parameter `Crt` is deprecated", DeprecationWarning) 

        self._Crt = Crt


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._BindDomains = params.get("BindDomains")
        self._CertId = params.get("CertId")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Crt = params.get("Crt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayCertificateResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建证书结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.CertificateInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CertificateInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayPublicNetworkRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayPublicNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 分组id。
        :type GroupId: str
        :param _InternetConfig: 公网负载均衡配置。
        :type InternetConfig: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        self._GatewayId = None
        self._GroupId = None
        self._InternetConfig = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InternetConfig(self):
        return self._InternetConfig

    @InternetConfig.setter
    def InternetConfig(self, InternetConfig):
        self._InternetConfig = InternetConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        if params.get("InternetConfig") is not None:
            self._InternetConfig = InternetConfig()
            self._InternetConfig._deserialize(params.get("InternetConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayPublicNetworkResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayPublicNetwork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreatePublicNetworkResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreatePublicNetworkResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayRequest(AbstractModel):
    """CreateCloudNativeAPIGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 云原生API网关名字, 最多支持60个字符。
        :type Name: str
        :param _Type: 云原生API网关类型, 目前只支持kong。
        :type Type: str
        :param _GatewayVersion: 云原生API网关版本。参考值：
- 2.4.1
- 2.5.1
        :type GatewayVersion: str
        :param _NodeConfig: 云原生API网关节点配置。
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _VpcConfig: 云原生API网关vpc配置。
        :type VpcConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayVpcConfig`
        :param _Description: 云原生API网关描述信息, 最多支持120个字符。
        :type Description: str
        :param _Tags: 标签列表
        :type Tags: list of InstanceTagInfo
        :param _EnableCls: 是否开启 CLS 日志。默认值：fasle
        :type EnableCls: bool
        :param _FeatureVersion: 产品版本。参考值：
- TRIAL：开发版
- STANDARD：标准版 （默认值）
- PROFESSIONAL：专业版
        :type FeatureVersion: str
        :param _InternetMaxBandwidthOut: 公网出流量带宽，[1,2048]Mbps
        :type InternetMaxBandwidthOut: int
        :param _EngineRegion: 实例实际的地域信息，默认值：ap-guangzhou
        :type EngineRegion: str
        :param _IngressClassName: ingress Class名称
        :type IngressClassName: str
        :param _TradeType: 付费类型。参考值：
0：后付费（默认值）
1：预付费（接口暂不支持创建预付费实例）
        :type TradeType: int
        :param _InternetConfig: 公网相关配置
        :type InternetConfig: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        self._Name = None
        self._Type = None
        self._GatewayVersion = None
        self._NodeConfig = None
        self._VpcConfig = None
        self._Description = None
        self._Tags = None
        self._EnableCls = None
        self._FeatureVersion = None
        self._InternetMaxBandwidthOut = None
        self._EngineRegion = None
        self._IngressClassName = None
        self._TradeType = None
        self._InternetConfig = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GatewayVersion(self):
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion

    @property
    def NodeConfig(self):
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableCls(self):
        return self._EnableCls

    @EnableCls.setter
    def EnableCls(self, EnableCls):
        self._EnableCls = EnableCls

    @property
    def FeatureVersion(self):
        return self._FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, FeatureVersion):
        self._FeatureVersion = FeatureVersion

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def IngressClassName(self):
        return self._IngressClassName

    @IngressClassName.setter
    def IngressClassName(self, IngressClassName):
        self._IngressClassName = IngressClassName

    @property
    def TradeType(self):
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def InternetConfig(self):
        return self._InternetConfig

    @InternetConfig.setter
    def InternetConfig(self, InternetConfig):
        self._InternetConfig = InternetConfig


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._GatewayVersion = params.get("GatewayVersion")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = CloudNativeAPIGatewayVpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnableCls = params.get("EnableCls")
        self._FeatureVersion = params.get("FeatureVersion")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._EngineRegion = params.get("EngineRegion")
        self._IngressClassName = params.get("IngressClassName")
        self._TradeType = params.get("TradeType")
        if params.get("InternetConfig") is not None:
            self._InternetConfig = InternetConfig()
            self._InternetConfig._deserialize(params.get("InternetConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayResponse(AbstractModel):
    """CreateCloudNativeAPIGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建云原生API网关实例响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateCloudNativeAPIGatewayResult(AbstractModel):
    """创建云原生API网关响应结果。

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关ID。
        :type GatewayId: str
        :param _Status: 云原生网关状态。
        :type Status: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._GatewayId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayRouteRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Id: 路由id，或路由名称。
不支持“未命名”
        :type Id: str
        :param _LimitDetail: 限流配置
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Id = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LimitDetail(self):
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayRouteRateLimit返回参数结构体

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


class CreateCloudNativeAPIGatewayRouteRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _ServiceID: 所属服务的ID
        :type ServiceID: str
        :param _RouteName: 路由的名字，实例级别唯一，可以不提供
        :type RouteName: str
        :param _Methods: 路由的方法，其中方法可选值：
- GET
- POST
- DELETE
- PUT
- OPTIONS
- PATCH
- HEAD
- ANY
- TRACE
- COPY
- MOVE
- PROPFIND
- PROPPATCH
- MKCOL
- LOCK
- UNLOCK
        :type Methods: list of str
        :param _Hosts: 路由的域名
        :type Hosts: list of str
        :param _Paths: 路由的路径
        :type Paths: list of str
        :param _Protocols: 路由的协议，可选
- https
- http
        :type Protocols: list of str
        :param _PreserveHost: 转发到后端时是否保留Host
        :type PreserveHost: bool
        :param _HttpsRedirectStatusCode: https重定向状态码
        :type HttpsRedirectStatusCode: int
        :param _StripPath: 转发到后端时是否StripPath
        :type StripPath: bool
        :param _ForceHttps: 是否开启强制HTTPS
        :type ForceHttps: bool
        :param _DestinationPorts: 四层匹配的目的端口
        :type DestinationPorts: list of int non-negative
        :param _Headers: 路由的Headers
        :type Headers: list of KVMapping
        """
        self._GatewayId = None
        self._ServiceID = None
        self._RouteName = None
        self._Methods = None
        self._Hosts = None
        self._Paths = None
        self._Protocols = None
        self._PreserveHost = None
        self._HttpsRedirectStatusCode = None
        self._StripPath = None
        self._ForceHttps = None
        self._DestinationPorts = None
        self._Headers = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceID(self):
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def RouteName(self):
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Methods(self):
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def PreserveHost(self):
        return self._PreserveHost

    @PreserveHost.setter
    def PreserveHost(self, PreserveHost):
        self._PreserveHost = PreserveHost

    @property
    def HttpsRedirectStatusCode(self):
        return self._HttpsRedirectStatusCode

    @HttpsRedirectStatusCode.setter
    def HttpsRedirectStatusCode(self, HttpsRedirectStatusCode):
        self._HttpsRedirectStatusCode = HttpsRedirectStatusCode

    @property
    def StripPath(self):
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def ForceHttps(self):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        self._ForceHttps = ForceHttps

    @property
    def DestinationPorts(self):
        return self._DestinationPorts

    @DestinationPorts.setter
    def DestinationPorts(self, DestinationPorts):
        self._DestinationPorts = DestinationPorts

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceID = params.get("ServiceID")
        self._RouteName = params.get("RouteName")
        self._Methods = params.get("Methods")
        self._Hosts = params.get("Hosts")
        self._Paths = params.get("Paths")
        self._Protocols = params.get("Protocols")
        self._PreserveHost = params.get("PreserveHost")
        self._HttpsRedirectStatusCode = params.get("HttpsRedirectStatusCode")
        self._StripPath = params.get("StripPath")
        self._ForceHttps = params.get("ForceHttps")
        self._DestinationPorts = params.get("DestinationPorts")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayRouteResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayRoute返回参数结构体

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


class CreateCloudNativeAPIGatewayServerGroupResult(AbstractModel):
    """创建网关分组信息

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _GroupId: 分组id
        :type GroupId: str
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayServiceRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 服务名称，或服务ID
        :type Name: str
        :param _LimitDetail: 限流配置
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Name = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LimitDetail(self):
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayServiceRateLimit返回参数结构体

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


class CreateCloudNativeAPIGatewayServiceRequest(AbstractModel):
    """CreateCloudNativeAPIGatewayService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 服务名称
        :type Name: str
        :param _Protocol: 请求协议：
- https
- http
- tcp
- udp
        :type Protocol: str
        :param _Path: 请求路径
        :type Path: str
        :param _Timeout: 超时时间，单位ms
        :type Timeout: int
        :param _Retries: 重试次数
        :type Retries: int
        :param _UpstreamType: 服务类型: 
- Kubernetes 
- Registry
- IPList
- HostIP
- Scf	
        :type UpstreamType: str
        :param _UpstreamInfo: 服务配置信息
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        """
        self._GatewayId = None
        self._Name = None
        self._Protocol = None
        self._Path = None
        self._Timeout = None
        self._Retries = None
        self._UpstreamType = None
        self._UpstreamInfo = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def UpstreamInfo(self):
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Path = params.get("Path")
        self._Timeout = params.get("Timeout")
        self._Retries = params.get("Retries")
        self._UpstreamType = params.get("UpstreamType")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCloudNativeAPIGatewayServiceResponse(AbstractModel):
    """CreateCloudNativeAPIGatewayService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 网关服务创建结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreateGatewayServiceResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateGatewayServiceResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateConfigFileGroupRequest(AbstractModel):
    """CreateConfigFileGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse 实例 id
        :type InstanceId: str
        :param _ConfigFileGroup: 配置文件组实体
        :type ConfigFileGroup: :class:`tencentcloud.tse.v20201207.models.ConfigFileGroup`
        """
        self._InstanceId = None
        self._ConfigFileGroup = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFileGroup(self):
        return self._ConfigFileGroup

    @ConfigFileGroup.setter
    def ConfigFileGroup(self, ConfigFileGroup):
        self._ConfigFileGroup = ConfigFileGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFileGroup") is not None:
            self._ConfigFileGroup = ConfigFileGroup()
            self._ConfigFileGroup._deserialize(params.get("ConfigFileGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigFileGroupResponse(AbstractModel):
    """CreateConfigFileGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否创建成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateConfigFileRequest(AbstractModel):
    """CreateConfigFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE 实例id
        :type InstanceId: str
        :param _ConfigFile: 配置文件列表详情
        :type ConfigFile: :class:`tencentcloud.tse.v20201207.models.ConfigFile`
        """
        self._InstanceId = None
        self._ConfigFile = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFile(self):
        return self._ConfigFile

    @ConfigFile.setter
    def ConfigFile(self, ConfigFile):
        self._ConfigFile = ConfigFile


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFile") is not None:
            self._ConfigFile = ConfigFile()
            self._ConfigFile._deserialize(params.get("ConfigFile"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConfigFileResponse(AbstractModel):
    """CreateConfigFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否创建成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateEngineRequest(AbstractModel):
    """CreateEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EngineType: 引擎类型。参考值：
- zookeeper
- nacos
- consul
- apollo
- eureka
- polaris
        :type EngineType: str
        :param _EngineVersion: 引擎的开源版本。每种引擎支持的开源版本不同，请参考产品文档或者控制台购买页
        :type EngineVersion: str
        :param _EngineProductVersion: 引擎的产品版本。参考值：
- STANDARD： 标准版
- PROFESSIONAL: 专业版（Zookeeper）/企业版（PolarisMesh）

引擎各版本及可选择的规格、节点数说明：
apollo - STANDARD版本
规格列表：1C2G、2C4G、4C8G、8C16G、16C32G
节点数：1，2，3，4，5

eureka - STANDARD版本
规格列表：1C2G、2C4G、4C8G、8C16G、16C32G
节点数：3，4，5

polarismesh - STANDARD版本
规格列表：NUM50、NUM100、NUM200、NUM500、NUM1000、NUM5000、NUM10000、NUM50000

兼容原spec-xxxxxx形式的规格ID
        :type EngineProductVersion: str
        :param _EngineRegion: 引擎所在地域。参考值说明：
中国区 参考值：
- ap-guangzhou：广州
- ap-beijing：北京
- ap-chengdu：成都
- ap-chongqing：重庆
- ap-nanjing：南京
- ap-shanghai：上海
- ap-hongkong：香港
- ap-taipei：台北
亚太区 参考值：
- ap-jakarta：雅加达
- ap-singapore：新加坡
北美区 参考值
- na-toronto：多伦多
金融专区 参考值
- ap-beijing-fsi：北京金融
- ap-shanghai-fsi：上海金融
- ap-shenzhen-fsi：深圳金融
        :type EngineRegion: str
        :param _EngineName: 引擎名称。参考值：
- eurek-test
        :type EngineName: str
        :param _TradeType: 付费类型。参考值：
- 0：后付费
- 1：预付费（接口暂不支持创建预付费实例）
        :type TradeType: int
        :param _EngineResourceSpec: 引擎的节点规格 ID。参见EngineProductVersion字段说明
        :type EngineResourceSpec: str
        :param _EngineNodeNum: 引擎的节点数量。参见EngineProductVersion字段说明
        :type EngineNodeNum: int
        :param _VpcId: VPC ID。在 VPC 的子网内分配一个 IP 作为引擎的访问地址。参考值：
- vpc-conz6aix
        :type VpcId: str
        :param _SubnetId: 子网 ID。在 VPC 的子网内分配一个 IP 作为引擎的访问地址。参考值：
- subnet-ahde9me9
        :type SubnetId: str
        :param _ApolloEnvParams: Apollo 环境配置参数列表。参数说明：
如果创建Apollo类型，此参数为必填的环境信息列表，最多可选4个环境。环境信息参数说明：
- Name：环境名。参考值：prod, dev, fat, uat
- EngineResourceSpec：环境内引擎的节点规格ID。参见EngineProductVersion参数说明
- EngineNodeNum：环境内引擎的节点数量。参见EngineProductVersion参数说明，其中prod环境支持的节点数为2，3，4，5
- StorageCapacity：配置存储空间大小，以GB为单位，步长为5.参考值：35
- VpcId：VPC ID。参考值：vpc-conz6aix
- SubnetId：子网 ID。参考值：subnet-ahde9me9
        :type ApolloEnvParams: list of ApolloEnvParam
        :param _EngineTags: 引擎的标签列表。用户自定义的key/value形式，无参考值
        :type EngineTags: list of InstanceTagInfo
        :param _EngineAdmin: 引擎的初始账号信息。可设置参数：
- Name：控制台初始用户名
- Password：控制台初始密码
- Token：引擎接口的管理员 Token
        :type EngineAdmin: :class:`tencentcloud.tse.v20201207.models.EngineAdmin`
        :param _PrepaidPeriod: 预付费时长，以月为单位
        :type PrepaidPeriod: int
        :param _PrepaidRenewFlag: 自动续费标记，仅预付费使用。参考值：
- 0：不自动续费
- 1：自动续费
        :type PrepaidRenewFlag: int
        :param _EngineRegionInfos: 跨地域部署的引擎地域配置详情
zk标准版没有跨地域部署，请不要填写
zk专业版跨地域部署开启了固定Leader所在地域，需要满足以下条件
- 固定Leader所在地域当前仅支持跨两个地域
- leader地域的副本数必须是3/2 + 1，5/2+1，7/2+1，也就是 2，3，4
        :type EngineRegionInfos: list of EngineRegionInfo
        :param _StorageType: zk标准版请填CLOUD_PREMIUM，zk标准版无法选择磁盘类型和磁盘容量，默认为CLOUD_PREMIUM
zk专业版可以为：CLOUD_SSD,CLOUD_SSD_PLUS,CLOUD_PREMIUM
        :type StorageType: str
        :param _StorageCapacity: zk标准版请填50，zk标准版无法选择磁盘类型和磁盘容量，磁盘容量默认为50
        :type StorageCapacity: int
        :param _StorageOption: zk专业版至多有两个盘，且磁盘的容量在50-3200之间
如果只有一个磁盘，storageCapacity与storageOption里面的capacity应该一致
        :type StorageOption: list of StorageOption
        :param _AffinityConstraint: ZK引擎实例，可用区分布约束，STRICT:强约束，PERMISSIVE: 弱约束
        :type AffinityConstraint: str
        """
        self._EngineType = None
        self._EngineVersion = None
        self._EngineProductVersion = None
        self._EngineRegion = None
        self._EngineName = None
        self._TradeType = None
        self._EngineResourceSpec = None
        self._EngineNodeNum = None
        self._VpcId = None
        self._SubnetId = None
        self._ApolloEnvParams = None
        self._EngineTags = None
        self._EngineAdmin = None
        self._PrepaidPeriod = None
        self._PrepaidRenewFlag = None
        self._EngineRegionInfos = None
        self._StorageType = None
        self._StorageCapacity = None
        self._StorageOption = None
        self._AffinityConstraint = None

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def EngineVersion(self):
        return self._EngineVersion

    @EngineVersion.setter
    def EngineVersion(self, EngineVersion):
        self._EngineVersion = EngineVersion

    @property
    def EngineProductVersion(self):
        return self._EngineProductVersion

    @EngineProductVersion.setter
    def EngineProductVersion(self, EngineProductVersion):
        self._EngineProductVersion = EngineProductVersion

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def EngineName(self):
        return self._EngineName

    @EngineName.setter
    def EngineName(self, EngineName):
        self._EngineName = EngineName

    @property
    def TradeType(self):
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def EngineResourceSpec(self):
        return self._EngineResourceSpec

    @EngineResourceSpec.setter
    def EngineResourceSpec(self, EngineResourceSpec):
        self._EngineResourceSpec = EngineResourceSpec

    @property
    def EngineNodeNum(self):
        return self._EngineNodeNum

    @EngineNodeNum.setter
    def EngineNodeNum(self, EngineNodeNum):
        self._EngineNodeNum = EngineNodeNum

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

    @property
    def ApolloEnvParams(self):
        return self._ApolloEnvParams

    @ApolloEnvParams.setter
    def ApolloEnvParams(self, ApolloEnvParams):
        self._ApolloEnvParams = ApolloEnvParams

    @property
    def EngineTags(self):
        return self._EngineTags

    @EngineTags.setter
    def EngineTags(self, EngineTags):
        self._EngineTags = EngineTags

    @property
    def EngineAdmin(self):
        return self._EngineAdmin

    @EngineAdmin.setter
    def EngineAdmin(self, EngineAdmin):
        self._EngineAdmin = EngineAdmin

    @property
    def PrepaidPeriod(self):
        return self._PrepaidPeriod

    @PrepaidPeriod.setter
    def PrepaidPeriod(self, PrepaidPeriod):
        self._PrepaidPeriod = PrepaidPeriod

    @property
    def PrepaidRenewFlag(self):
        return self._PrepaidRenewFlag

    @PrepaidRenewFlag.setter
    def PrepaidRenewFlag(self, PrepaidRenewFlag):
        self._PrepaidRenewFlag = PrepaidRenewFlag

    @property
    def EngineRegionInfos(self):
        return self._EngineRegionInfos

    @EngineRegionInfos.setter
    def EngineRegionInfos(self, EngineRegionInfos):
        self._EngineRegionInfos = EngineRegionInfos

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

    @property
    def StorageOption(self):
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def AffinityConstraint(self):
        return self._AffinityConstraint

    @AffinityConstraint.setter
    def AffinityConstraint(self, AffinityConstraint):
        self._AffinityConstraint = AffinityConstraint


    def _deserialize(self, params):
        self._EngineType = params.get("EngineType")
        self._EngineVersion = params.get("EngineVersion")
        self._EngineProductVersion = params.get("EngineProductVersion")
        self._EngineRegion = params.get("EngineRegion")
        self._EngineName = params.get("EngineName")
        self._TradeType = params.get("TradeType")
        self._EngineResourceSpec = params.get("EngineResourceSpec")
        self._EngineNodeNum = params.get("EngineNodeNum")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        if params.get("ApolloEnvParams") is not None:
            self._ApolloEnvParams = []
            for item in params.get("ApolloEnvParams"):
                obj = ApolloEnvParam()
                obj._deserialize(item)
                self._ApolloEnvParams.append(obj)
        if params.get("EngineTags") is not None:
            self._EngineTags = []
            for item in params.get("EngineTags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._EngineTags.append(obj)
        if params.get("EngineAdmin") is not None:
            self._EngineAdmin = EngineAdmin()
            self._EngineAdmin._deserialize(params.get("EngineAdmin"))
        self._PrepaidPeriod = params.get("PrepaidPeriod")
        self._PrepaidRenewFlag = params.get("PrepaidRenewFlag")
        if params.get("EngineRegionInfos") is not None:
            self._EngineRegionInfos = []
            for item in params.get("EngineRegionInfos"):
                obj = EngineRegionInfo()
                obj._deserialize(item)
                self._EngineRegionInfos.append(obj)
        self._StorageType = params.get("StorageType")
        self._StorageCapacity = params.get("StorageCapacity")
        if params.get("StorageOption") is not None:
            self._StorageOption = []
            for item in params.get("StorageOption"):
                obj = StorageOption()
                obj._deserialize(item)
                self._StorageOption.append(obj)
        self._AffinityConstraint = params.get("AffinityConstraint")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEngineResponse(AbstractModel):
    """CreateEngine返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例 ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateGatewayServiceResult(AbstractModel):
    """创建云原生网关服务结果

    """

    def __init__(self):
        r"""
        :param _ServiceId: 网关服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
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
        


class CreateGovernanceAliasRequest(AbstractModel):
    """CreateGovernanceAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _Alias: 服务别名
        :type Alias: str
        :param _AliasNamespace: 服务别名命名空间
        :type AliasNamespace: str
        :param _Service: 服务别名所指向的服务名
        :type Service: str
        :param _Namespace: 服务别名所指向的命名空间
        :type Namespace: str
        :param _Comment: 服务别名描述
        :type Comment: str
        """
        self._InstanceId = None
        self._Alias = None
        self._AliasNamespace = None
        self._Service = None
        self._Namespace = None
        self._Comment = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def AliasNamespace(self):
        return self._AliasNamespace

    @AliasNamespace.setter
    def AliasNamespace(self, AliasNamespace):
        self._AliasNamespace = AliasNamespace

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._AliasNamespace = params.get("AliasNamespace")
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGovernanceAliasResponse(AbstractModel):
    """CreateGovernanceAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateGovernanceInstancesRequest(AbstractModel):
    """CreateGovernanceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceInstances: 服务实例信息。
        :type GovernanceInstances: list of GovernanceInstanceInput
        """
        self._InstanceId = None
        self._GovernanceInstances = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceInstances(self):
        return self._GovernanceInstances

    @GovernanceInstances.setter
    def GovernanceInstances(self, GovernanceInstances):
        self._GovernanceInstances = GovernanceInstances


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceInstances") is not None:
            self._GovernanceInstances = []
            for item in params.get("GovernanceInstances"):
                obj = GovernanceInstanceInput()
                obj._deserialize(item)
                self._GovernanceInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGovernanceInstancesResponse(AbstractModel):
    """CreateGovernanceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateGovernanceNamespacesRequest(AbstractModel):
    """CreateGovernanceNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse 实例id。
        :type InstanceId: str
        :param _GovernanceNamespaces: 命名空间信息。
        :type GovernanceNamespaces: list of GovernanceNamespaceInput
        """
        self._InstanceId = None
        self._GovernanceNamespaces = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceNamespaces(self):
        return self._GovernanceNamespaces

    @GovernanceNamespaces.setter
    def GovernanceNamespaces(self, GovernanceNamespaces):
        self._GovernanceNamespaces = GovernanceNamespaces


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceNamespaces") is not None:
            self._GovernanceNamespaces = []
            for item in params.get("GovernanceNamespaces"):
                obj = GovernanceNamespaceInput()
                obj._deserialize(item)
                self._GovernanceNamespaces.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGovernanceNamespacesResponse(AbstractModel):
    """CreateGovernanceNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateGovernanceServicesRequest(AbstractModel):
    """CreateGovernanceServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse 实例 id。
        :type InstanceId: str
        :param _GovernanceServices: 服务信息。
        :type GovernanceServices: list of GovernanceServiceInput
        """
        self._InstanceId = None
        self._GovernanceServices = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceServices(self):
        return self._GovernanceServices

    @GovernanceServices.setter
    def GovernanceServices(self, GovernanceServices):
        self._GovernanceServices = GovernanceServices


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceServices") is not None:
            self._GovernanceServices = []
            for item in params.get("GovernanceServices"):
                obj = GovernanceServiceInput()
                obj._deserialize(item)
                self._GovernanceServices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGovernanceServicesResponse(AbstractModel):
    """CreateGovernanceServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateNativeGatewayServerGroupRequest(AbstractModel):
    """CreateNativeGatewayServerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id。
只支持后付费实例
        :type GatewayId: str
        :param _Name: 网关分组名
        :type Name: str
        :param _NodeConfig: 节点配置
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _SubnetId: 子网id
        :type SubnetId: str
        :param _Description: 描述信息
        :type Description: str
        :param _InternetMaxBandwidthOut: 公网带宽信息
        :type InternetMaxBandwidthOut: int
        :param _InternetConfig: 公网配置。
        :type InternetConfig: :class:`tencentcloud.tse.v20201207.models.InternetConfig`
        """
        self._GatewayId = None
        self._Name = None
        self._NodeConfig = None
        self._SubnetId = None
        self._Description = None
        self._InternetMaxBandwidthOut = None
        self._InternetConfig = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NodeConfig(self):
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def InternetConfig(self):
        return self._InternetConfig

    @InternetConfig.setter
    def InternetConfig(self, InternetConfig):
        self._InternetConfig = InternetConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        self._SubnetId = params.get("SubnetId")
        self._Description = params.get("Description")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("InternetConfig") is not None:
            self._InternetConfig = InternetConfig()
            self._InternetConfig._deserialize(params.get("InternetConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNativeGatewayServerGroupResponse(AbstractModel):
    """CreateNativeGatewayServerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 网关分组创建信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.CreateCloudNativeAPIGatewayServerGroupResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateCloudNativeAPIGatewayServerGroupResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateOrUpdateConfigFileAndReleaseRequest(AbstractModel):
    """CreateOrUpdateConfigFileAndRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ConfigFilePublishInfo: 配置文件列表详情	
        :type ConfigFilePublishInfo: :class:`tencentcloud.tse.v20201207.models.ConfigFilePublishInfo`
        """
        self._InstanceId = None
        self._ConfigFilePublishInfo = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFilePublishInfo(self):
        return self._ConfigFilePublishInfo

    @ConfigFilePublishInfo.setter
    def ConfigFilePublishInfo(self, ConfigFilePublishInfo):
        self._ConfigFilePublishInfo = ConfigFilePublishInfo


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFilePublishInfo") is not None:
            self._ConfigFilePublishInfo = ConfigFilePublishInfo()
            self._ConfigFilePublishInfo._deserialize(params.get("ConfigFilePublishInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrUpdateConfigFileAndReleaseResponse(AbstractModel):
    """CreateOrUpdateConfigFileAndRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreatePublicNetworkResult(AbstractModel):
    """创建kong客户端公网结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _NetworkId: 客户端公网网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkId(self):
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkId = params.get("NetworkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWafDomainsRequest(AbstractModel):
    """CreateWafDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Domains: WAF 防护域名列表
        :type Domains: list of str
        """
        self._GatewayId = None
        self._Domains = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWafDomainsResponse(AbstractModel):
    """CreateWafDomains返回参数结构体

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


class DeleteAutoScalerResourceStrategyRequest(AbstractModel):
    """DeleteAutoScalerResourceStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        """
        self._GatewayId = None
        self._StrategyId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAutoScalerResourceStrategyResponse(AbstractModel):
    """DeleteAutoScalerResourceStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayCanaryRuleRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayCanaryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关 ID
        :type GatewayId: str
        :param _ServiceId: 服务 ID
        :type ServiceId: str
        :param _Priority: 优先级
        :type Priority: int
        """
        self._GatewayId = None
        self._ServiceId = None
        self._Priority = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayCanaryRuleResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayCanaryRule返回参数结构体

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


class DeleteCloudNativeAPIGatewayCertificateRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Id: 证书Id
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayCertificateResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayCertificate返回参数结构体

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


class DeleteCloudNativeAPIGatewayPublicNetworkRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayPublicNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 分组id，kong类型时必填
        :type GroupId: str
        :param _InternetAddressVersion: 公网类型
- IPV4 （默认值）
- IPV6
        :type InternetAddressVersion: str
        :param _Vip: 公网ip，存在多个公网时必填
        :type Vip: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._InternetAddressVersion = None
        self._Vip = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def InternetAddressVersion(self):
        return self._InternetAddressVersion

    @InternetAddressVersion.setter
    def InternetAddressVersion(self, InternetAddressVersion):
        self._InternetAddressVersion = InternetAddressVersion

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._InternetAddressVersion = params.get("InternetAddressVersion")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayPublicNetworkResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayPublicNetwork返回参数结构体

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


class DeleteCloudNativeAPIGatewayRequest(AbstractModel):
    """DeleteCloudNativeAPIGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _DeleteClsTopic: 是否删除实例关联的 CLS 日志主题。
        :type DeleteClsTopic: bool
        """
        self._GatewayId = None
        self._DeleteClsTopic = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def DeleteClsTopic(self):
        return self._DeleteClsTopic

    @DeleteClsTopic.setter
    def DeleteClsTopic(self, DeleteClsTopic):
        self._DeleteClsTopic = DeleteClsTopic


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._DeleteClsTopic = params.get("DeleteClsTopic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayResponse(AbstractModel):
    """DeleteCloudNativeAPIGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除云原生API网关实例响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DeleteCloudNativeAPIGatewayResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DeleteCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteCloudNativeAPIGatewayResult(AbstractModel):
    """删除云原生API网关响应结果。

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生网关ID。
        :type GatewayId: str
        :param _Status: 云原生网关状态。
        :type Status: str
        """
        self._GatewayId = None
        self._Status = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayRouteRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关Id
        :type GatewayId: str
        :param _Id: 路由Id，或路由名称。
不支持“未命名”
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayRouteRateLimit返回参数结构体

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


class DeleteCloudNativeAPIGatewayRouteRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 路由的ID或名字，不支持名称“未命名”
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayRouteResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayRoute返回参数结构体

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


class DeleteCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayServiceRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关Id
        :type GatewayId: str
        :param _Name: 服务名称，或服务ID
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayServiceRateLimit返回参数结构体

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


class DeleteCloudNativeAPIGatewayServiceRequest(AbstractModel):
    """DeleteCloudNativeAPIGatewayService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 服务名字，服务ID
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCloudNativeAPIGatewayServiceResponse(AbstractModel):
    """DeleteCloudNativeAPIGatewayService返回参数结构体

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


class DeleteConfigFileGroupRequest(AbstractModel):
    """DeleteConfigFileGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse 实例 id。	
        :type InstanceId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 组
        :type Group: str
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFileGroupResponse(AbstractModel):
    """DeleteConfigFileGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否删除成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteConfigFileReleasesRequest(AbstractModel):
    """DeleteConfigFileReleases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _ConfigFileReleases: 待删除配置发布详情
        :type ConfigFileReleases: list of ConfigFileReleaseDeletion
        """
        self._InstanceId = None
        self._ConfigFileReleases = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFileReleases(self):
        return self._ConfigFileReleases

    @ConfigFileReleases.setter
    def ConfigFileReleases(self, ConfigFileReleases):
        self._ConfigFileReleases = ConfigFileReleases


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFileReleases") is not None:
            self._ConfigFileReleases = []
            for item in params.get("ConfigFileReleases"):
                obj = ConfigFileReleaseDeletion()
                obj._deserialize(item)
                self._ConfigFileReleases.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFileReleasesResponse(AbstractModel):
    """DeleteConfigFileReleases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除配置发布结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteConfigFilesRequest(AbstractModel):
    """DeleteConfigFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 配置分组名称
        :type Group: str
        :param _Name: 配置文件名称
        :type Name: str
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigFilesResponse(AbstractModel):
    """DeleteConfigFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteEngineRequest(AbstractModel):
    """DeleteEngine请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例 ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DeleteEngineResponse(AbstractModel):
    """DeleteEngine返回参数结构体

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


class DeleteGovernanceAliasesRequest(AbstractModel):
    """DeleteGovernanceAliases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceAliases: 服务别名列表
        :type GovernanceAliases: list of GovernanceAlias
        """
        self._InstanceId = None
        self._GovernanceAliases = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceAliases(self):
        return self._GovernanceAliases

    @GovernanceAliases.setter
    def GovernanceAliases(self, GovernanceAliases):
        self._GovernanceAliases = GovernanceAliases


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceAliases") is not None:
            self._GovernanceAliases = []
            for item in params.get("GovernanceAliases"):
                obj = GovernanceAlias()
                obj._deserialize(item)
                self._GovernanceAliases.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceAliasesResponse(AbstractModel):
    """DeleteGovernanceAliases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteGovernanceInstancesByHostRequest(AbstractModel):
    """DeleteGovernanceInstancesByHost请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceInstances: 要删除的服务实例信息。
        :type GovernanceInstances: list of GovernanceInstanceUpdate
        """
        self._InstanceId = None
        self._GovernanceInstances = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceInstances(self):
        return self._GovernanceInstances

    @GovernanceInstances.setter
    def GovernanceInstances(self, GovernanceInstances):
        self._GovernanceInstances = GovernanceInstances


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceInstances") is not None:
            self._GovernanceInstances = []
            for item in params.get("GovernanceInstances"):
                obj = GovernanceInstanceUpdate()
                obj._deserialize(item)
                self._GovernanceInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceInstancesByHostResponse(AbstractModel):
    """DeleteGovernanceInstancesByHost返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteGovernanceInstancesRequest(AbstractModel):
    """DeleteGovernanceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceInstances: 要删除的服务实例信息。
        :type GovernanceInstances: list of GovernanceInstanceUpdate
        """
        self._InstanceId = None
        self._GovernanceInstances = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceInstances(self):
        return self._GovernanceInstances

    @GovernanceInstances.setter
    def GovernanceInstances(self, GovernanceInstances):
        self._GovernanceInstances = GovernanceInstances


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceInstances") is not None:
            self._GovernanceInstances = []
            for item in params.get("GovernanceInstances"):
                obj = GovernanceInstanceUpdate()
                obj._deserialize(item)
                self._GovernanceInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceInstancesResponse(AbstractModel):
    """DeleteGovernanceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteGovernanceNamespacesRequest(AbstractModel):
    """DeleteGovernanceNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse 实例 id。
        :type InstanceId: str
        :param _GovernanceNamespaces: 命名空间信息。
        :type GovernanceNamespaces: list of GovernanceNamespaceInput
        """
        self._InstanceId = None
        self._GovernanceNamespaces = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceNamespaces(self):
        return self._GovernanceNamespaces

    @GovernanceNamespaces.setter
    def GovernanceNamespaces(self, GovernanceNamespaces):
        self._GovernanceNamespaces = GovernanceNamespaces


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceNamespaces") is not None:
            self._GovernanceNamespaces = []
            for item in params.get("GovernanceNamespaces"):
                obj = GovernanceNamespaceInput()
                obj._deserialize(item)
                self._GovernanceNamespaces.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceNamespacesResponse(AbstractModel):
    """DeleteGovernanceNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteGovernanceServicesRequest(AbstractModel):
    """DeleteGovernanceServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceServices: 服务信息。
        :type GovernanceServices: list of GovernanceServiceInput
        """
        self._InstanceId = None
        self._GovernanceServices = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceServices(self):
        return self._GovernanceServices

    @GovernanceServices.setter
    def GovernanceServices(self, GovernanceServices):
        self._GovernanceServices = GovernanceServices


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceServices") is not None:
            self._GovernanceServices = []
            for item in params.get("GovernanceServices"):
                obj = GovernanceServiceInput()
                obj._deserialize(item)
                self._GovernanceServices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGovernanceServicesResponse(AbstractModel):
    """DeleteGovernanceServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除服务结果。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteNativeGatewayServerGroupRequest(AbstractModel):
    """DeleteNativeGatewayServerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id。
只支持后付费实例
        :type GatewayId: str
        :param _GroupId: 网关分组id
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNativeGatewayServerGroupResponse(AbstractModel):
    """DeleteNativeGatewayServerGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除信息
        :type Result: :class:`tencentcloud.tse.v20201207.models.DeleteNativeGatewayServerGroupResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DeleteNativeGatewayServerGroupResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteNativeGatewayServerGroupResult(AbstractModel):
    """删除网关实例结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _GroupId: 网关分组id
        :type GroupId: str
        :param _Status: 删除状态
        :type Status: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWafDomainsRequest(AbstractModel):
    """DeleteWafDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Domains: WAF 防护域名列表
        :type Domains: list of str
        """
        self._GatewayId = None
        self._Domains = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWafDomainsResponse(AbstractModel):
    """DeleteWafDomains返回参数结构体

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


class DescribeAllConfigFileTemplatesRequest(AbstractModel):
    """DescribeAllConfigFileTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
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
        


class DescribeAllConfigFileTemplatesResponse(AbstractModel):
    """DescribeAllConfigFileTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据总数量
        :type TotalCount: int
        :param _ConfigFileTemplates: 配置文件模板列表
        :type ConfigFileTemplates: list of ConfigFileTemplate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigFileTemplates = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigFileTemplates(self):
        return self._ConfigFileTemplates

    @ConfigFileTemplates.setter
    def ConfigFileTemplates(self, ConfigFileTemplates):
        self._ConfigFileTemplates = ConfigFileTemplates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigFileTemplates") is not None:
            self._ConfigFileTemplates = []
            for item in params.get("ConfigFileTemplates"):
                obj = ConfigFileTemplate()
                obj._deserialize(item)
                self._ConfigFileTemplates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAutoScalerResourceStrategiesRequest(AbstractModel):
    """DescribeAutoScalerResourceStrategies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        """
        self._GatewayId = None
        self._StrategyId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalerResourceStrategiesResponse(AbstractModel):
    """DescribeAutoScalerResourceStrategies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生API网关实例弹性伸缩策略列表响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayStrategyResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayStrategyResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAutoScalerResourceStrategyBindingGroupsRequest(AbstractModel):
    """DescribeAutoScalerResourceStrategyBindingGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        :param _Offset: 查询偏移量
        :type Offset: int
        :param _Limit: 查询数量限制
        :type Limit: int
        """
        self._GatewayId = None
        self._StrategyId = None
        self._Offset = None
        self._Limit = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

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
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAutoScalerResourceStrategyBindingGroupsResponse(AbstractModel):
    """DescribeAutoScalerResourceStrategyBindingGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 云原生API网关实例策略绑定网关分组列表响应结果
        :type Result: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCanaryRulesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayCanaryRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _ServiceId: 服务 ID
        :type ServiceId: str
        :param _RuleType: 灰度规则类别 Standard｜Lane
        :type RuleType: str
        :param _Limit: 列表数量
        :type Limit: int
        :param _Offset: 列表offset
        :type Offset: int
        """
        self._GatewayId = None
        self._ServiceId = None
        self._RuleType = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        self._RuleType = params.get("RuleType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCanaryRulesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayCanaryRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 灰度规则列表
        :type Result: :class:`tencentcloud.tse.v20201207.models.CloudAPIGatewayCanaryRuleList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CloudAPIGatewayCanaryRuleList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCertificateDetailsRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayCertificateDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Id: 证书Id
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCertificateDetailsResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayCertificateDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongCertificate`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongCertificate()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayCertificatesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Limit: 列表数量
        :type Limit: int
        :param _Offset: 列表offset
        :type Offset: int
        :param _Filters: 过滤条件，多个过滤条件之间是与的关系，支持BindDomain ，Name
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayCertificatesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongCertificatesList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongCertificatesList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayConfigRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 分组id，不填时为默认分组
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayConfigResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生API网关响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayConfigResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayConfigResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayConfigResult(AbstractModel):
    """获取云原生API网关实例网络配置结果。

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID。
        :type GatewayId: str
        :param _ConfigList: 分组网络配置列表。
        :type ConfigList: list of CloudNativeAPIGatewayConfig
        :param _GroupSubnetId: 分组子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupSubnetId: str
        :param _GroupVpcId: 分组VPC信息
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupVpcId: str
        :param _GroupId: 分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
        self._GatewayId = None
        self._ConfigList = None
        self._GroupSubnetId = None
        self._GroupVpcId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def GroupSubnetId(self):
        return self._GroupSubnetId

    @GroupSubnetId.setter
    def GroupSubnetId(self, GroupSubnetId):
        self._GroupSubnetId = GroupSubnetId

    @property
    def GroupVpcId(self):
        return self._GroupVpcId

    @GroupVpcId.setter
    def GroupVpcId(self, GroupVpcId):
        self._GroupVpcId = GroupVpcId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = CloudNativeAPIGatewayConfig()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._GroupSubnetId = params.get("GroupSubnetId")
        self._GroupVpcId = params.get("GroupVpcId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayNodesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 实例分组id
        :type GroupId: str
        :param _Limit: 翻页获取多少个
        :type Limit: int
        :param _Offset: 翻页从第几个开始获取
        :type Offset: int
        """
        self._GatewayId = None
        self._GroupId = None
        self._Limit = None
        self._Offset = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayNodesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生网关节点列表结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayNodesResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayNodesResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayNodesResult(AbstractModel):
    """获取网关节点信息

    """

    def __init__(self):
        r"""
        :param _TotalCount: 获取云原生API网关节点列表响应结果。
        :type TotalCount: int
        :param _NodeList: 云原生API网关节点列表。
        :type NodeList: list of CloudNativeAPIGatewayNode
        """
        self._TotalCount = None
        self._NodeList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NodeList(self):
        return self._NodeList

    @NodeList.setter
    def NodeList(self, NodeList):
        self._NodeList = NodeList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("NodeList") is not None:
            self._NodeList = []
            for item in params.get("NodeList"):
                obj = CloudNativeAPIGatewayNode()
                obj._deserialize(item)
                self._NodeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayPortsRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayPorts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayPortsResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayPorts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 云原生API网关实例协议端口列表响应结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeGatewayInstancePortResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeGatewayInstancePortResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayRequest(AbstractModel):
    """DescribeCloudNativeAPIGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayResponse(AbstractModel):
    """DescribeCloudNativeAPIGateway返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生API网关基础信息响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeCloudNativeAPIGatewayResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayResult(AbstractModel):
    """获取云原生API网关基础信息响应结果。

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关ID。
        :type GatewayId: str
        :param _Status: 云原生API网关状态。
        :type Status: str
        :param _Name: 云原生API网关名。
        :type Name: str
        :param _Type: 云原生API网关类型。
        :type Type: str
        :param _GatewayVersion: 实例版本：
- 2.4.1
- 2.5.1
        :type GatewayVersion: str
        :param _NodeConfig: 云原生API网关节点信息。
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _VpcConfig: 云原生API网关vpc配置。
        :type VpcConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayVpcConfig`
        :param _Description: 云原生API网关描述。
        :type Description: str
        :param _CreateTime: 云原生API网关创建时间。
        :type CreateTime: str
        :param _Tags: 实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of InstanceTagInfo
        :param _EnableCls: 是否开启 cls 日志
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableCls: bool
        :param _TradeType: 付费模式，0表示后付费，1预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeType: int
        :param _FeatureVersion: 实例版本，当前支持开发版、标准版、专业版【TRIAL、STANDARD、PROFESSIONAL】
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureVersion: str
        :param _InternetMaxBandwidthOut: 公网出流量带宽，[1,2048]Mbps
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _AutoRenewFlag: 自动续费标记，0表示默认状态(用户未设置，即初始状态)；
1表示自动续费，2表示明确不自动续费(用户设置)，若业务无续费概念或无需自动续费，需要设置为0
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _CurDeadline: 到期时间，预付费时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        :param _IsolateTime: 隔离时间，实例隔离时使用
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _EnableInternet: 是否开启客户端公网。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableInternet: bool
        :param _EngineRegion: 实例实际的地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param _IngressClassName: Ingress class名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IngressClassName: str
        :param _InternetPayMode: 公网计费方式。可选取值 BANDWIDTH | TRAFFIC ，表示按带宽和按流量计费。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetPayMode: str
        :param _GatewayMinorVersion: 云原生API网关小版本号
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayMinorVersion: str
        :param _InstancePort: 实例监听的端口信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstancePort: :class:`tencentcloud.tse.v20201207.models.InstancePort`
        :param _LoadBalancerType: 公网CLB默认类型
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerType: str
        :param _PublicIpAddresses: 公网IP地址列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicIpAddresses: list of str
        """
        self._GatewayId = None
        self._Status = None
        self._Name = None
        self._Type = None
        self._GatewayVersion = None
        self._NodeConfig = None
        self._VpcConfig = None
        self._Description = None
        self._CreateTime = None
        self._Tags = None
        self._EnableCls = None
        self._TradeType = None
        self._FeatureVersion = None
        self._InternetMaxBandwidthOut = None
        self._AutoRenewFlag = None
        self._CurDeadline = None
        self._IsolateTime = None
        self._EnableInternet = None
        self._EngineRegion = None
        self._IngressClassName = None
        self._InternetPayMode = None
        self._GatewayMinorVersion = None
        self._InstancePort = None
        self._LoadBalancerType = None
        self._PublicIpAddresses = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def GatewayVersion(self):
        return self._GatewayVersion

    @GatewayVersion.setter
    def GatewayVersion(self, GatewayVersion):
        self._GatewayVersion = GatewayVersion

    @property
    def NodeConfig(self):
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableCls(self):
        return self._EnableCls

    @EnableCls.setter
    def EnableCls(self, EnableCls):
        self._EnableCls = EnableCls

    @property
    def TradeType(self):
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def FeatureVersion(self):
        return self._FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, FeatureVersion):
        self._FeatureVersion = FeatureVersion

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def IngressClassName(self):
        return self._IngressClassName

    @IngressClassName.setter
    def IngressClassName(self, IngressClassName):
        self._IngressClassName = IngressClassName

    @property
    def InternetPayMode(self):
        return self._InternetPayMode

    @InternetPayMode.setter
    def InternetPayMode(self, InternetPayMode):
        self._InternetPayMode = InternetPayMode

    @property
    def GatewayMinorVersion(self):
        return self._GatewayMinorVersion

    @GatewayMinorVersion.setter
    def GatewayMinorVersion(self, GatewayMinorVersion):
        self._GatewayMinorVersion = GatewayMinorVersion

    @property
    def InstancePort(self):
        return self._InstancePort

    @InstancePort.setter
    def InstancePort(self, InstancePort):
        self._InstancePort = InstancePort

    @property
    def LoadBalancerType(self):
        return self._LoadBalancerType

    @LoadBalancerType.setter
    def LoadBalancerType(self, LoadBalancerType):
        self._LoadBalancerType = LoadBalancerType

    @property
    def PublicIpAddresses(self):
        return self._PublicIpAddresses

    @PublicIpAddresses.setter
    def PublicIpAddresses(self, PublicIpAddresses):
        self._PublicIpAddresses = PublicIpAddresses


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._GatewayVersion = params.get("GatewayVersion")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = CloudNativeAPIGatewayVpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = InstanceTagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnableCls = params.get("EnableCls")
        self._TradeType = params.get("TradeType")
        self._FeatureVersion = params.get("FeatureVersion")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        self._IsolateTime = params.get("IsolateTime")
        self._EnableInternet = params.get("EnableInternet")
        self._EngineRegion = params.get("EngineRegion")
        self._IngressClassName = params.get("IngressClassName")
        self._InternetPayMode = params.get("InternetPayMode")
        self._GatewayMinorVersion = params.get("GatewayMinorVersion")
        if params.get("InstancePort") is not None:
            self._InstancePort = InstancePort()
            self._InstancePort._deserialize(params.get("InstancePort"))
        self._LoadBalancerType = params.get("LoadBalancerType")
        self._PublicIpAddresses = params.get("PublicIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayRouteRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关Id
        :type GatewayId: str
        :param _Id: 路由Id，或路由名称。
不支持“未命名”
        :type Id: str
        """
        self._GatewayId = None
        self._Id = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayRouteRateLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生网关限流插件(路由)
        :type Result: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CloudNativeAPIGatewayRateLimitDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayRoutesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayRoutes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Limit: 翻页单页查询限制数量[0,1000], 默认值0
        :type Limit: int
        :param _Offset: 翻页单页偏移量，默认值0
        :type Offset: int
        :param _ServiceName: 服务的名字，精确匹配
        :type ServiceName: str
        :param _RouteName: 路由的名字，精确匹配
        :type RouteName: str
        :param _Filters: 过滤条件，多个过滤条件之间是与的关系，支持 name, path, host, method, service, protocol
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._ServiceName = None
        self._RouteName = None
        self._Filters = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def RouteName(self):
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ServiceName = params.get("ServiceName")
        self._RouteName = params.get("RouteName")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayRoutesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayRoutes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongServiceRouteList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongServiceRouteList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayServiceRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关Id
        :type GatewayId: str
        :param _Name: 服务名称，或服务ID。
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayServiceRateLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生网关限流插件(服务)
        :type Result: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CloudNativeAPIGatewayRateLimitDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayServicesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Limit: 列表数量
        :type Limit: int
        :param _Offset: 列表 offset
        :type Offset: int
        :param _Filters: 过滤条件，多个过滤条件之间是与的关系，支持 name,upstreamType
        :type Filters: list of ListFilter
        """
        self._GatewayId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ListFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayServicesResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongServices`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongServices()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewayUpstreamRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _ServiceName: 服务名字
        :type ServiceName: str
        """
        self._GatewayId = None
        self._ServiceName = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCloudNativeAPIGatewayUpstreamResponse(AbstractModel):
    """DescribeCloudNativeAPIGatewayUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongUpstreamList`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongUpstreamList()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeCloudNativeAPIGatewaysRequest(AbstractModel):
    """DescribeCloudNativeAPIGateways请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 请求过滤参数，支持按照实例名称、ID和标签键值（Name、GatewayId、Tag）筛选
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeCloudNativeAPIGatewaysResponse(AbstractModel):
    """DescribeCloudNativeAPIGateways返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生API网关实例列表响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.ListCloudNativeAPIGatewayResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ListCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeConfigFileGroupsRequest(AbstractModel):
    """DescribeConfigFileGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id
        :type InstanceId: str
        :param _Namespace: 根据命名空间过滤
        :type Namespace: str
        :param _Group: 根据配置文件组名过滤
        :type Group: str
        :param _FileName: 根据配置文件组名过滤
        :type FileName: str
        :param _Limit: 返回数量，默认为20，最大值为100。	
        :type Limit: int
        :param _Offset: 偏移量，默认为0。	
        :type Offset: int
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._FileName = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFileGroupsResponse(AbstractModel):
    """DescribeConfigFileGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 列表总数量
        :type TotalCount: int
        :param _ConfigFileGroups: 配置文件组列表
        :type ConfigFileGroups: list of ConfigFileGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigFileGroups = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigFileGroups(self):
        return self._ConfigFileGroups

    @ConfigFileGroups.setter
    def ConfigFileGroups(self, ConfigFileGroups):
        self._ConfigFileGroups = ConfigFileGroups

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigFileGroups") is not None:
            self._ConfigFileGroups = []
            for item in params.get("ConfigFileGroups"):
                obj = ConfigFileGroup()
                obj._deserialize(item)
                self._ConfigFileGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigFileReleaseHistoriesRequest(AbstractModel):
    """DescribeConfigFileReleaseHistories请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 组
        :type Group: str
        :param _Name: 名称
        :type Name: str
        :param _EndId: 发布历史记录id，用于分页优化，一般指定 EndId，就不用指定 Offset，否则分页可能不连续
        :type EndId: int
        :param _Limit: 返回数量，默认为20，最大值为100。	
        :type Limit: int
        :param _Offset: 偏移量，默认为0。	
        :type Offset: int
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._Name = None
        self._EndId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def EndId(self):
        return self._EndId

    @EndId.setter
    def EndId(self, EndId):
        self._EndId = EndId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Name = params.get("Name")
        self._EndId = params.get("EndId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFileReleaseHistoriesResponse(AbstractModel):
    """DescribeConfigFileReleaseHistories返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数据总数量
        :type TotalCount: int
        :param _ConfigFileReleaseHistories: 配置文件发布历史列表
        :type ConfigFileReleaseHistories: list of ConfigFileReleaseHistory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigFileReleaseHistories = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigFileReleaseHistories(self):
        return self._ConfigFileReleaseHistories

    @ConfigFileReleaseHistories.setter
    def ConfigFileReleaseHistories(self, ConfigFileReleaseHistories):
        self._ConfigFileReleaseHistories = ConfigFileReleaseHistories

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigFileReleaseHistories") is not None:
            self._ConfigFileReleaseHistories = []
            for item in params.get("ConfigFileReleaseHistories"):
                obj = ConfigFileReleaseHistory()
                obj._deserialize(item)
                self._ConfigFileReleaseHistories.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigFileReleaseRequest(AbstractModel):
    """DescribeConfigFileRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _Group: 配置分组名称
        :type Group: str
        :param _Name: 配置文件名称
        :type Name: str
        :param _ReleaseName: 配置文件发布名称
        :type ReleaseName: str
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._Name = None
        self._ReleaseName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ReleaseName(self):
        return self._ReleaseName

    @ReleaseName.setter
    def ReleaseName(self, ReleaseName):
        self._ReleaseName = ReleaseName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Name = params.get("Name")
        self._ReleaseName = params.get("ReleaseName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFileReleaseResponse(AbstractModel):
    """DescribeConfigFileRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigFileRelease: 配置文件发布详情
        :type ConfigFileRelease: :class:`tencentcloud.tse.v20201207.models.ConfigFileRelease`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigFileRelease = None
        self._RequestId = None

    @property
    def ConfigFileRelease(self):
        return self._ConfigFileRelease

    @ConfigFileRelease.setter
    def ConfigFileRelease(self, ConfigFileRelease):
        self._ConfigFileRelease = ConfigFileRelease

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConfigFileRelease") is not None:
            self._ConfigFileRelease = ConfigFileRelease()
            self._ConfigFileRelease._deserialize(params.get("ConfigFileRelease"))
        self._RequestId = params.get("RequestId")


class DescribeConfigFileReleaseVersionsRequest(AbstractModel):
    """DescribeConfigFileReleaseVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 配置分组
        :type Group: str
        :param _FileName: 文件名称
        :type FileName: str
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._FileName = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFileReleaseVersionsResponse(AbstractModel):
    """DescribeConfigFileReleaseVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReleaseVersions: 版本信息
        :type ReleaseVersions: list of ReleaseVersion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReleaseVersions = None
        self._RequestId = None

    @property
    def ReleaseVersions(self):
        return self._ReleaseVersions

    @ReleaseVersions.setter
    def ReleaseVersions(self, ReleaseVersions):
        self._ReleaseVersions = ReleaseVersions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ReleaseVersions") is not None:
            self._ReleaseVersions = []
            for item in params.get("ReleaseVersions"):
                obj = ReleaseVersion()
                obj._deserialize(item)
                self._ReleaseVersions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigFileReleasesRequest(AbstractModel):
    """DescribeConfigFileReleases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Limit: 条数
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 配置分组
        :type Group: str
        :param _FileName: 文件名称
        :type FileName: str
        :param _OnlyUse: 只保护处于使用状态
        :type OnlyUse: bool
        :param _ReleaseName: 发布名称
        :type ReleaseName: str
        :param _OrderField: 排序字段，mtime/version/name
，默认version
        :type OrderField: str
        :param _OrderDesc: 排序，asc/desc，默认 desc
        :type OrderDesc: str
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None
        self._Namespace = None
        self._Group = None
        self._FileName = None
        self._OnlyUse = None
        self._ReleaseName = None
        self._OrderField = None
        self._OrderDesc = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def OnlyUse(self):
        return self._OnlyUse

    @OnlyUse.setter
    def OnlyUse(self, OnlyUse):
        self._OnlyUse = OnlyUse

    @property
    def ReleaseName(self):
        return self._ReleaseName

    @ReleaseName.setter
    def ReleaseName(self, ReleaseName):
        self._ReleaseName = ReleaseName

    @property
    def OrderField(self):
        return self._OrderField

    @OrderField.setter
    def OrderField(self, OrderField):
        self._OrderField = OrderField

    @property
    def OrderDesc(self):
        return self._OrderDesc

    @OrderDesc.setter
    def OrderDesc(self, OrderDesc):
        self._OrderDesc = OrderDesc


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._FileName = params.get("FileName")
        self._OnlyUse = params.get("OnlyUse")
        self._ReleaseName = params.get("ReleaseName")
        self._OrderField = params.get("OrderField")
        self._OrderDesc = params.get("OrderDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFileReleasesResponse(AbstractModel):
    """DescribeConfigFileReleases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总条数
        :type TotalCount: int
        :param _Releases: 发布列表
        :type Releases: list of ConfigFileRelease
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Releases = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Releases(self):
        return self._Releases

    @Releases.setter
    def Releases(self, Releases):
        self._Releases = Releases

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Releases") is not None:
            self._Releases = []
            for item in params.get("Releases"):
                obj = ConfigFileRelease()
                obj._deserialize(item)
                self._Releases.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigFileRequest(AbstractModel):
    """DescribeConfigFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Group: 组
        :type Group: str
        :param _Name: 名称
        :type Name: str
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._Name = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFileResponse(AbstractModel):
    """DescribeConfigFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigFile: 配置文件
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigFile: :class:`tencentcloud.tse.v20201207.models.ConfigFile`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigFile = None
        self._RequestId = None

    @property
    def ConfigFile(self):
        return self._ConfigFile

    @ConfigFile.setter
    def ConfigFile(self, ConfigFile):
        self._ConfigFile = ConfigFile

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ConfigFile") is not None:
            self._ConfigFile = ConfigFile()
            self._ConfigFile._deserialize(params.get("ConfigFile"))
        self._RequestId = params.get("RequestId")


class DescribeConfigFilesByGroupRequest(AbstractModel):
    """DescribeConfigFilesByGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _Namespace: 命名空间名
        :type Namespace: str
        :param _Group: 组名
        :type Group: str
        :param _Limit: 返回数量，默认为20，最大值为100。	
        :type Limit: int
        :param _Offset: 偏移量，默认为0。	
        :type Offset: int
        """
        self._InstanceId = None
        self._Namespace = None
        self._Group = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Group = params.get("Group")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFilesByGroupResponse(AbstractModel):
    """DescribeConfigFilesByGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总数量
        :type TotalCount: int
        :param _ConfigFiles: 配置文件列表
        :type ConfigFiles: list of ConfigFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigFiles = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigFiles(self):
        return self._ConfigFiles

    @ConfigFiles.setter
    def ConfigFiles(self, ConfigFiles):
        self._ConfigFiles = ConfigFiles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigFiles") is not None:
            self._ConfigFiles = []
            for item in params.get("ConfigFiles"):
                obj = ConfigFile()
                obj._deserialize(item)
                self._ConfigFiles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConfigFilesRequest(AbstractModel):
    """DescribeConfigFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Namespace: 命名空间名称
        :type Namespace: str
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _Group: 组名
        :type Group: str
        :param _Name: 名称
        :type Name: str
        :param _Tags: 标签列表
        :type Tags: list of ConfigFileTag
        :param _Limit: 返回数量，默认为20，最大值为100。	
        :type Limit: int
        :param _Offset: 偏移量，默认为0。	
        :type Offset: int
        """
        self._Namespace = None
        self._InstanceId = None
        self._Group = None
        self._Name = None
        self._Tags = None
        self._Limit = None
        self._Offset = None

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Group(self):
        return self._Group

    @Group.setter
    def Group(self, Group):
        self._Group = Group

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Namespace = params.get("Namespace")
        self._InstanceId = params.get("InstanceId")
        self._Group = params.get("Group")
        self._Name = params.get("Name")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ConfigFileTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigFilesResponse(AbstractModel):
    """DescribeConfigFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 分页总数量
        :type TotalCount: int
        :param _ConfigFiles: 配置文件列表
        :type ConfigFiles: list of ConfigFile
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ConfigFiles = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ConfigFiles(self):
        return self._ConfigFiles

    @ConfigFiles.setter
    def ConfigFiles(self, ConfigFiles):
        self._ConfigFiles = ConfigFiles

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ConfigFiles") is not None:
            self._ConfigFiles = []
            for item in params.get("ConfigFiles"):
                obj = ConfigFile()
                obj._deserialize(item)
                self._ConfigFiles.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGatewayInstancePortResult(AbstractModel):
    """获取云原生API网关实例协议端口列表响应结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GatewayInstancePortList: 网关实例协议端口列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayInstancePortList: list of GatewayInstanceSchemeAndPorts
        """
        self._GatewayId = None
        self._GatewayInstancePortList = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GatewayInstancePortList(self):
        return self._GatewayInstancePortList

    @GatewayInstancePortList.setter
    def GatewayInstancePortList(self, GatewayInstancePortList):
        self._GatewayInstancePortList = GatewayInstancePortList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        if params.get("GatewayInstancePortList") is not None:
            self._GatewayInstancePortList = []
            for item in params.get("GatewayInstancePortList"):
                obj = GatewayInstanceSchemeAndPorts()
                obj._deserialize(item)
                self._GatewayInstancePortList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceAliasesRequest(AbstractModel):
    """DescribeGovernanceAliases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _Service: 服务别名所指向的服务名。
        :type Service: str
        :param _Namespace: 服务别名所指向的命名空间名。
        :type Namespace: str
        :param _Alias: 服务别名。
        :type Alias: str
        :param _AliasNamespace: 服务别名命名空间。
        :type AliasNamespace: str
        :param _Comment: 服务别名描述。
        :type Comment: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._InstanceId = None
        self._Service = None
        self._Namespace = None
        self._Alias = None
        self._AliasNamespace = None
        self._Comment = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def AliasNamespace(self):
        return self._AliasNamespace

    @AliasNamespace.setter
    def AliasNamespace(self, AliasNamespace):
        self._AliasNamespace = AliasNamespace

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

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
        self._InstanceId = params.get("InstanceId")
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Alias = params.get("Alias")
        self._AliasNamespace = params.get("AliasNamespace")
        self._Comment = params.get("Comment")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceAliasesResponse(AbstractModel):
    """DescribeGovernanceAliases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务别名总数量。
        :type TotalCount: int
        :param _Content: 服务别名列表。
        :type Content: list of GovernanceAlias
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = GovernanceAlias()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGovernanceInstancesRequest(AbstractModel):
    """DescribeGovernanceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Service: 实例所在的服务名。
        :type Service: str
        :param _Namespace: 实例所在命名空间名。
        :type Namespace: str
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _Host: 根据实例ip过滤，多个ip使用英文逗号分隔。
        :type Host: str
        :param _InstanceVersion: 根据实例版本过滤。
        :type InstanceVersion: str
        :param _Protocol: 根据实例协议过滤。
        :type Protocol: str
        :param _HealthStatus: 根据实例健康状态过滤。false：表示不健康，true：表示健康。
        :type HealthStatus: bool
        :param _Isolate: 根据实例隔离状态过滤。false：表示非隔离，true：表示隔离中。
        :type Isolate: bool
        :param _Metadatas: 根据元数据信息过滤。目前只支持一组元数据键值，若传了多个键值对，只会以第一个过滤。
        :type Metadatas: list of Metadata
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._Service = None
        self._Namespace = None
        self._InstanceId = None
        self._Host = None
        self._InstanceVersion = None
        self._Protocol = None
        self._HealthStatus = None
        self._Isolate = None
        self._Metadatas = None
        self._Offset = None
        self._Limit = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def Isolate(self):
        return self._Isolate

    @Isolate.setter
    def Isolate(self, Isolate):
        self._Isolate = Isolate

    @property
    def Metadatas(self):
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas

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
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._InstanceId = params.get("InstanceId")
        self._Host = params.get("Host")
        self._InstanceVersion = params.get("InstanceVersion")
        self._Protocol = params.get("Protocol")
        self._HealthStatus = params.get("HealthStatus")
        self._Isolate = params.get("Isolate")
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceInstancesResponse(AbstractModel):
    """DescribeGovernanceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务实例总数量。
        :type TotalCount: int
        :param _Content: 服务里实例列表。
        :type Content: list of GovernanceInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = GovernanceInstance()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGovernanceNamespacesRequest(AbstractModel):
    """DescribeGovernanceNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id
        :type InstanceId: str
        :param _Name: 根据命名空间名称过滤。
        :type Name: str
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self._InstanceId = None
        self._Name = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceNamespacesResponse(AbstractModel):
    """DescribeGovernanceNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 列表总数量。
        :type TotalCount: int
        :param _Content: 治理中心命名空间实例列表。
        :type Content: list of GovernanceNamespace
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = GovernanceNamespace()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGovernanceServiceContractVersionsRequest(AbstractModel):
    """DescribeGovernanceServiceContractVersions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例ID
        :type InstanceId: str
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Service: 服务名
        :type Service: str
        """
        self._InstanceId = None
        self._Namespace = None
        self._Service = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Namespace = params.get("Namespace")
        self._Service = params.get("Service")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceServiceContractVersionsResponse(AbstractModel):
    """DescribeGovernanceServiceContractVersions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GovernanceServiceContractVersions: 服务契约版本列表
        :type GovernanceServiceContractVersions: list of GovernanceServiceContractVersion
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GovernanceServiceContractVersions = None
        self._RequestId = None

    @property
    def GovernanceServiceContractVersions(self):
        return self._GovernanceServiceContractVersions

    @GovernanceServiceContractVersions.setter
    def GovernanceServiceContractVersions(self, GovernanceServiceContractVersions):
        self._GovernanceServiceContractVersions = GovernanceServiceContractVersions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("GovernanceServiceContractVersions") is not None:
            self._GovernanceServiceContractVersions = []
            for item in params.get("GovernanceServiceContractVersions"):
                obj = GovernanceServiceContractVersion()
                obj._deserialize(item)
                self._GovernanceServiceContractVersions.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGovernanceServiceContractsRequest(AbstractModel):
    """DescribeGovernanceServiceContracts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 北极星引擎实例ID
        :type InstanceId: str
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页条数
        :type Limit: int
        :param _Namespace: 命名空间
        :type Namespace: str
        :param _Service: 服务名
        :type Service: str
        :param _Name: 契约名称
        :type Name: str
        :param _ContractVersion: 契约版本
        :type ContractVersion: str
        :param _Protocol: 契约协议
        :type Protocol: str
        :param _Brief: 是否只展示基本信息
        :type Brief: bool
        """
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Namespace = None
        self._Service = None
        self._Name = None
        self._ContractVersion = None
        self._Protocol = None
        self._Brief = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ContractVersion(self):
        return self._ContractVersion

    @ContractVersion.setter
    def ContractVersion(self, ContractVersion):
        self._ContractVersion = ContractVersion

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Brief(self):
        return self._Brief

    @Brief.setter
    def Brief(self, Brief):
        self._Brief = Brief


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Namespace = params.get("Namespace")
        self._Service = params.get("Service")
        self._Name = params.get("Name")
        self._ContractVersion = params.get("ContractVersion")
        self._Protocol = params.get("Protocol")
        self._Brief = params.get("Brief")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceServiceContractsResponse(AbstractModel):
    """DescribeGovernanceServiceContracts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Size: 返回条数
        :type Size: int
        :param _ServiceContracts: 契约定义列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceContracts: list of GovernanceServiceContract
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Size = None
        self._ServiceContracts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Size(self):
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def ServiceContracts(self):
        return self._ServiceContracts

    @ServiceContracts.setter
    def ServiceContracts(self, ServiceContracts):
        self._ServiceContracts = ServiceContracts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Size = params.get("Size")
        if params.get("ServiceContracts") is not None:
            self._ServiceContracts = []
            for item in params.get("ServiceContracts"):
                obj = GovernanceServiceContract()
                obj._deserialize(item)
                self._ServiceContracts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeGovernanceServicesRequest(AbstractModel):
    """DescribeGovernanceServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 按照服务名过滤，精确匹配。
        :type Name: str
        :param _Namespace: 按照命名空间过滤，精确匹配。
        :type Namespace: str
        :param _Metadatas: 使用元数据过滤，目前只支持一组元组数，若传了多条，只会使用第一条元数据过滤。
        :type Metadatas: list of Metadata
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _InstanceId: tse 实例 id。
        :type InstanceId: str
        :param _Department: 服务所属部门。
        :type Department: str
        :param _Business: 服务所属业务。
        :type Business: str
        :param _Host: 服务中实例的ip，用来过滤服务。
        :type Host: str
        :param _OnlyExistHealthyInstance: 是否只查询存在健康实例的服务
        :type OnlyExistHealthyInstance: bool
        """
        self._Name = None
        self._Namespace = None
        self._Metadatas = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._Department = None
        self._Business = None
        self._Host = None
        self._OnlyExistHealthyInstance = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Metadatas(self):
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas

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

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def OnlyExistHealthyInstance(self):
        return self._OnlyExistHealthyInstance

    @OnlyExistHealthyInstance.setter
    def OnlyExistHealthyInstance(self, OnlyExistHealthyInstance):
        self._OnlyExistHealthyInstance = OnlyExistHealthyInstance


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Department = params.get("Department")
        self._Business = params.get("Business")
        self._Host = params.get("Host")
        self._OnlyExistHealthyInstance = params.get("OnlyExistHealthyInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGovernanceServicesResponse(AbstractModel):
    """DescribeGovernanceServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务数总量。
        :type TotalCount: int
        :param _Content: 服务信息详情。
        :type Content: list of GovernanceService
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = GovernanceService()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRegionInfo(AbstractModel):
    """实例地域信息描述

    """

    def __init__(self):
        r"""
        :param _EngineRegion: 引擎部署地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param _Replica: 引擎在该地域的副本数
注意：此字段可能返回 null，表示取不到有效值。
        :type Replica: int
        :param _SpecId: 引擎在该地域的规格id
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecId: str
        :param _IntranetVpcInfos: 客户端内网的网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetVpcInfos: list of VpcInfo
        :param _ConsoleIntranetVpcInfos: 控制台内网的网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleIntranetVpcInfos: list of VpcInfo
        :param _EnableClientInternet: 是否开公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableClientInternet: bool
        :param _LimiterIntranetVpcInfos: 限流客户端内网的网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type LimiterIntranetVpcInfos: list of VpcInfo
        :param _MainRegion: 是否为主地域，仅在服务治理中心多地域有效
注意：此字段可能返回 null，表示取不到有效值。
        :type MainRegion: bool
        :param _EKSClusterID: 该地域所在的EKS集群
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSClusterID: str
        """
        self._EngineRegion = None
        self._Replica = None
        self._SpecId = None
        self._IntranetVpcInfos = None
        self._ConsoleIntranetVpcInfos = None
        self._EnableClientInternet = None
        self._LimiterIntranetVpcInfos = None
        self._MainRegion = None
        self._EKSClusterID = None

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def IntranetVpcInfos(self):
        return self._IntranetVpcInfos

    @IntranetVpcInfos.setter
    def IntranetVpcInfos(self, IntranetVpcInfos):
        self._IntranetVpcInfos = IntranetVpcInfos

    @property
    def ConsoleIntranetVpcInfos(self):
        return self._ConsoleIntranetVpcInfos

    @ConsoleIntranetVpcInfos.setter
    def ConsoleIntranetVpcInfos(self, ConsoleIntranetVpcInfos):
        self._ConsoleIntranetVpcInfos = ConsoleIntranetVpcInfos

    @property
    def EnableClientInternet(self):
        return self._EnableClientInternet

    @EnableClientInternet.setter
    def EnableClientInternet(self, EnableClientInternet):
        self._EnableClientInternet = EnableClientInternet

    @property
    def LimiterIntranetVpcInfos(self):
        return self._LimiterIntranetVpcInfos

    @LimiterIntranetVpcInfos.setter
    def LimiterIntranetVpcInfos(self, LimiterIntranetVpcInfos):
        self._LimiterIntranetVpcInfos = LimiterIntranetVpcInfos

    @property
    def MainRegion(self):
        return self._MainRegion

    @MainRegion.setter
    def MainRegion(self, MainRegion):
        self._MainRegion = MainRegion

    @property
    def EKSClusterID(self):
        return self._EKSClusterID

    @EKSClusterID.setter
    def EKSClusterID(self, EKSClusterID):
        self._EKSClusterID = EKSClusterID


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        self._Replica = params.get("Replica")
        self._SpecId = params.get("SpecId")
        if params.get("IntranetVpcInfos") is not None:
            self._IntranetVpcInfos = []
            for item in params.get("IntranetVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._IntranetVpcInfos.append(obj)
        if params.get("ConsoleIntranetVpcInfos") is not None:
            self._ConsoleIntranetVpcInfos = []
            for item in params.get("ConsoleIntranetVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._ConsoleIntranetVpcInfos.append(obj)
        self._EnableClientInternet = params.get("EnableClientInternet")
        if params.get("LimiterIntranetVpcInfos") is not None:
            self._LimiterIntranetVpcInfos = []
            for item in params.get("LimiterIntranetVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._LimiterIntranetVpcInfos.append(obj)
        self._MainRegion = params.get("MainRegion")
        self._EKSClusterID = params.get("EKSClusterID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosReplicasRequest(AbstractModel):
    """DescribeNacosReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎实例ID
        :type InstanceId: str
        :param _Limit: 副本列表Limit
        :type Limit: int
        :param _Offset: 副本列表Offset
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosReplicasResponse(AbstractModel):
    """DescribeNacosReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Replicas: 引擎实例副本信息
        :type Replicas: list of NacosReplica
        :param _TotalCount: 副本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Replicas = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

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
        if params.get("Replicas") is not None:
            self._Replicas = []
            for item in params.get("Replicas"):
                obj = NacosReplica()
                obj._deserialize(item)
                self._Replicas.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNacosServerInterfacesRequest(AbstractModel):
    """DescribeNacosServerInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Limit: 返回的列表个数
        :type Limit: int
        :param _Offset: 返回的列表起始偏移量
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNacosServerInterfacesResponse(AbstractModel):
    """DescribeNacosServerInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 接口总个数
        :type TotalCount: int
        :param _Content: 接口列表
        :type Content: list of NacosServerInterface
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = NacosServerInterface()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNativeGatewayServerGroupsRequest(AbstractModel):
    """DescribeNativeGatewayServerGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _Offset: 翻页从第几个开始获取
        :type Offset: int
        :param _Limit: 翻页获取多少个
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._GatewayId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

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

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
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
        


class DescribeNativeGatewayServerGroupsResponse(AbstractModel):
    """DescribeNativeGatewayServerGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 分组列表信息
        :type Result: :class:`tencentcloud.tse.v20201207.models.NativeGatewayServerGroups`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = NativeGatewayServerGroups()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeOneCloudNativeAPIGatewayServiceRequest(AbstractModel):
    """DescribeOneCloudNativeAPIGatewayService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 服务名字，或服务ID
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOneCloudNativeAPIGatewayServiceResponse(AbstractModel):
    """DescribeOneCloudNativeAPIGatewayService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 无
        :type Result: :class:`tencentcloud.tse.v20201207.models.KongServiceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = KongServiceDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePublicAddressConfigRequest(AbstractModel):
    """DescribePublicAddressConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
        :type GatewayId: str
        :param _GroupId: 查询该分组的公网信息，不传则查询实例所有的公网负载均衡信息
        :type GroupId: str
        """
        self._GatewayId = None
        self._GroupId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicAddressConfigResponse(AbstractModel):
    """DescribePublicAddressConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 公网地址信息
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribePublicAddressConfigResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribePublicAddressConfigResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePublicAddressConfigResult(AbstractModel):
    """获取云原生api网关公网地址信息响应结果

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _ConfigList: 公网地址信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigList: list of PublicAddressConfig
        :param _TotalCount: 总个数	
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._GatewayId = None
        self._ConfigList = None
        self._TotalCount = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ConfigList(self):
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = PublicAddressConfig()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicNetworkRequest(AbstractModel):
    """DescribePublicNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 网关分组ID
        :type GroupId: str
        :param _NetworkId: 网络ID
        :type NetworkId: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkId(self):
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkId = params.get("NetworkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePublicNetworkResponse(AbstractModel):
    """DescribePublicNetwork返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 获取云原生API网关公网详情响应结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribePublicNetworkResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribePublicNetworkResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePublicNetworkResult(AbstractModel):
    """查询客户端公网信息

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _GroupId: 网关分组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _PublicNetwork: 客户端公网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PublicNetwork: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayConfig`
        """
        self._GatewayId = None
        self._GroupId = None
        self._PublicNetwork = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def PublicNetwork(self):
        return self._PublicNetwork

    @PublicNetwork.setter
    def PublicNetwork(self, PublicNetwork):
        self._PublicNetwork = PublicNetwork


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        if params.get("PublicNetwork") is not None:
            self._PublicNetwork = CloudNativeAPIGatewayConfig()
            self._PublicNetwork._deserialize(params.get("PublicNetwork"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstanceAccessAddressRequest(AbstractModel):
    """DescribeSREInstanceAccessAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 注册引擎实例Id
        :type InstanceId: str
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _Workload: 引擎其他组件名称（pushgateway、polaris-limiter）
        :type Workload: str
        :param _EngineRegion: 部署地域
        :type EngineRegion: str
        """
        self._InstanceId = None
        self._VpcId = None
        self._SubnetId = None
        self._Workload = None
        self._EngineRegion = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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

    @property
    def Workload(self):
        return self._Workload

    @Workload.setter
    def Workload(self, Workload):
        self._Workload = Workload

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Workload = params.get("Workload")
        self._EngineRegion = params.get("EngineRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstanceAccessAddressResponse(AbstractModel):
    """DescribeSREInstanceAccessAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IntranetAddress: 内网访问地址
        :type IntranetAddress: str
        :param _InternetAddress: 公网访问地址
        :type InternetAddress: str
        :param _EnvAddressInfos: apollo多环境公网ip
        :type EnvAddressInfos: list of EnvAddressInfo
        :param _ConsoleInternetAddress: 控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetAddress: str
        :param _ConsoleIntranetAddress: 控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleIntranetAddress: str
        :param _InternetBandWidth: 客户端公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetBandWidth: int
        :param _ConsoleInternetBandWidth: 控制台公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleInternetBandWidth: int
        :param _LimiterAddressInfos: 北极星限流server节点接入IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LimiterAddressInfos: list of PolarisLimiterAddress
        :param _CLBMultiRegion: InternetAddress 的公网 CLB 多可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CLBMultiRegion: :class:`tencentcloud.tse.v20201207.models.CLBMultiRegion`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IntranetAddress = None
        self._InternetAddress = None
        self._EnvAddressInfos = None
        self._ConsoleInternetAddress = None
        self._ConsoleIntranetAddress = None
        self._InternetBandWidth = None
        self._ConsoleInternetBandWidth = None
        self._LimiterAddressInfos = None
        self._CLBMultiRegion = None
        self._RequestId = None

    @property
    def IntranetAddress(self):
        return self._IntranetAddress

    @IntranetAddress.setter
    def IntranetAddress(self, IntranetAddress):
        self._IntranetAddress = IntranetAddress

    @property
    def InternetAddress(self):
        return self._InternetAddress

    @InternetAddress.setter
    def InternetAddress(self, InternetAddress):
        self._InternetAddress = InternetAddress

    @property
    def EnvAddressInfos(self):
        return self._EnvAddressInfos

    @EnvAddressInfos.setter
    def EnvAddressInfos(self, EnvAddressInfos):
        self._EnvAddressInfos = EnvAddressInfos

    @property
    def ConsoleInternetAddress(self):
        return self._ConsoleInternetAddress

    @ConsoleInternetAddress.setter
    def ConsoleInternetAddress(self, ConsoleInternetAddress):
        self._ConsoleInternetAddress = ConsoleInternetAddress

    @property
    def ConsoleIntranetAddress(self):
        return self._ConsoleIntranetAddress

    @ConsoleIntranetAddress.setter
    def ConsoleIntranetAddress(self, ConsoleIntranetAddress):
        self._ConsoleIntranetAddress = ConsoleIntranetAddress

    @property
    def InternetBandWidth(self):
        return self._InternetBandWidth

    @InternetBandWidth.setter
    def InternetBandWidth(self, InternetBandWidth):
        self._InternetBandWidth = InternetBandWidth

    @property
    def ConsoleInternetBandWidth(self):
        return self._ConsoleInternetBandWidth

    @ConsoleInternetBandWidth.setter
    def ConsoleInternetBandWidth(self, ConsoleInternetBandWidth):
        self._ConsoleInternetBandWidth = ConsoleInternetBandWidth

    @property
    def LimiterAddressInfos(self):
        return self._LimiterAddressInfos

    @LimiterAddressInfos.setter
    def LimiterAddressInfos(self, LimiterAddressInfos):
        self._LimiterAddressInfos = LimiterAddressInfos

    @property
    def CLBMultiRegion(self):
        return self._CLBMultiRegion

    @CLBMultiRegion.setter
    def CLBMultiRegion(self, CLBMultiRegion):
        self._CLBMultiRegion = CLBMultiRegion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IntranetAddress = params.get("IntranetAddress")
        self._InternetAddress = params.get("InternetAddress")
        if params.get("EnvAddressInfos") is not None:
            self._EnvAddressInfos = []
            for item in params.get("EnvAddressInfos"):
                obj = EnvAddressInfo()
                obj._deserialize(item)
                self._EnvAddressInfos.append(obj)
        self._ConsoleInternetAddress = params.get("ConsoleInternetAddress")
        self._ConsoleIntranetAddress = params.get("ConsoleIntranetAddress")
        self._InternetBandWidth = params.get("InternetBandWidth")
        self._ConsoleInternetBandWidth = params.get("ConsoleInternetBandWidth")
        if params.get("LimiterAddressInfos") is not None:
            self._LimiterAddressInfos = []
            for item in params.get("LimiterAddressInfos"):
                obj = PolarisLimiterAddress()
                obj._deserialize(item)
                self._LimiterAddressInfos.append(obj)
        if params.get("CLBMultiRegion") is not None:
            self._CLBMultiRegion = CLBMultiRegion()
            self._CLBMultiRegion._deserialize(params.get("CLBMultiRegion"))
        self._RequestId = params.get("RequestId")


class DescribeSREInstancesRequest(AbstractModel):
    """DescribeSREInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 请求过滤参数
        :type Filters: list of Filter
        :param _Limit: 翻页单页查询限制数量[0,1000], 默认值0
        :type Limit: int
        :param _Offset: 翻页单页偏移量，默认值0
        :type Offset: int
        :param _QueryType: 查询类型
        :type QueryType: str
        :param _QuerySource: 调用方来源
        :type QuerySource: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._QueryType = None
        self._QuerySource = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def QueryType(self):
        return self._QueryType

    @QueryType.setter
    def QueryType(self, QueryType):
        self._QueryType = QueryType

    @property
    def QuerySource(self):
        return self._QuerySource

    @QuerySource.setter
    def QuerySource(self, QuerySource):
        self._QuerySource = QuerySource


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._QueryType = params.get("QueryType")
        self._QuerySource = params.get("QuerySource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSREInstancesResponse(AbstractModel):
    """DescribeSREInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _Content: 实例记录
        :type Content: list of SREInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = SREInstance()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUpstreamHealthCheckConfigRequest(AbstractModel):
    """DescribeUpstreamHealthCheckConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 网关服务名称
        :type Name: str
        """
        self._GatewayId = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamHealthCheckConfigResponse(AbstractModel):
    """DescribeUpstreamHealthCheckConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.UpstreamHealthCheckConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UpstreamHealthCheckConfig()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWafDomainsRequest(AbstractModel):
    """DescribeWafDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        """
        self._GatewayId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafDomainsResponse(AbstractModel):
    """DescribeWafDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 已被 WAF 防护域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeWafDomainsResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeWafDomainsResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWafDomainsResult(AbstractModel):
    """获取WAF保护域名列表

    """

    def __init__(self):
        r"""
        :param _Domains: WAF防护域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        """
        self._Domains = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafProtectionRequest(AbstractModel):
    """DescribeWafProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Type:  防护资源的类型。
- Global  实例
- Service  服务
- Route  路由
- Object  对象
        :type Type: str
        :param _TypeList: 防护资源类型列表，支持查询多个类型（Global、Service、Route、Object）。为空时，默认查询Global类型。
        :type TypeList: list of str
        """
        self._GatewayId = None
        self._Type = None
        self._TypeList = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Type(self):
        warnings.warn("parameter `Type` is deprecated", DeprecationWarning) 

        return self._Type

    @Type.setter
    def Type(self, Type):
        warnings.warn("parameter `Type` is deprecated", DeprecationWarning) 

        self._Type = Type

    @property
    def TypeList(self):
        return self._TypeList

    @TypeList.setter
    def TypeList(self, TypeList):
        self._TypeList = TypeList


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Type = params.get("Type")
        self._TypeList = params.get("TypeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafProtectionResponse(AbstractModel):
    """DescribeWafProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 保护状态
        :type Result: :class:`tencentcloud.tse.v20201207.models.DescribeWafProtectionResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeWafProtectionResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeWafProtectionResult(AbstractModel):
    """获取WAF保护资源状态

    """

    def __init__(self):
        r"""
        :param _GlobalStatus: 全局防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalStatus: str
        :param _ServicesStatus: 服务防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ServicesStatus: list of ServiceWafStatus
        :param _RouteStatus: 路由防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteStatus: list of RouteWafStatus
        :param _ObjectStatus: 对象防护状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectStatus: str
        """
        self._GlobalStatus = None
        self._ServicesStatus = None
        self._RouteStatus = None
        self._ObjectStatus = None

    @property
    def GlobalStatus(self):
        return self._GlobalStatus

    @GlobalStatus.setter
    def GlobalStatus(self, GlobalStatus):
        self._GlobalStatus = GlobalStatus

    @property
    def ServicesStatus(self):
        return self._ServicesStatus

    @ServicesStatus.setter
    def ServicesStatus(self, ServicesStatus):
        self._ServicesStatus = ServicesStatus

    @property
    def RouteStatus(self):
        return self._RouteStatus

    @RouteStatus.setter
    def RouteStatus(self, RouteStatus):
        self._RouteStatus = RouteStatus

    @property
    def ObjectStatus(self):
        return self._ObjectStatus

    @ObjectStatus.setter
    def ObjectStatus(self, ObjectStatus):
        self._ObjectStatus = ObjectStatus


    def _deserialize(self, params):
        self._GlobalStatus = params.get("GlobalStatus")
        if params.get("ServicesStatus") is not None:
            self._ServicesStatus = []
            for item in params.get("ServicesStatus"):
                obj = ServiceWafStatus()
                obj._deserialize(item)
                self._ServicesStatus.append(obj)
        if params.get("RouteStatus") is not None:
            self._RouteStatus = []
            for item in params.get("RouteStatus"):
                obj = RouteWafStatus()
                obj._deserialize(item)
                self._RouteStatus.append(obj)
        self._ObjectStatus = params.get("ObjectStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperReplicasRequest(AbstractModel):
    """DescribeZookeeperReplicas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 注册引擎实例ID
        :type InstanceId: str
        :param _Limit: 副本列表Limit
        :type Limit: int
        :param _Offset: 副本列表Offset
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperReplicasResponse(AbstractModel):
    """DescribeZookeeperReplicas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Replicas: 注册引擎实例副本信息
        :type Replicas: list of ZookeeperReplica
        :param _TotalCount: 副本个数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Replicas = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Replicas(self):
        return self._Replicas

    @Replicas.setter
    def Replicas(self, Replicas):
        self._Replicas = Replicas

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
        if params.get("Replicas") is not None:
            self._Replicas = []
            for item in params.get("Replicas"):
                obj = ZookeeperReplica()
                obj._deserialize(item)
                self._Replicas.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZookeeperServerInterfacesRequest(AbstractModel):
    """DescribeZookeeperServerInterfaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Limit: 返回的列表个数
        :type Limit: int
        :param _Offset: 返回的列表起始偏移量
        :type Offset: int
        """
        self._InstanceId = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZookeeperServerInterfacesResponse(AbstractModel):
    """DescribeZookeeperServerInterfaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 接口总个数
        :type TotalCount: int
        :param _Content: 接口列表
        :type Content: list of ZookeeperServerInterface
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Content = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = ZookeeperServerInterface()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class EngineAdmin(AbstractModel):
    """引擎的初始管理账号，当前仅支持Apollo引擎

    """

    def __init__(self):
        r"""
        :param _Name: 控制台初始用户名
        :type Name: str
        :param _Password: 控制台初始密码
        :type Password: str
        :param _Token: 引擎接口的管理员 Token
        :type Token: str
        """
        self._Name = None
        self._Password = None
        self._Token = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Password = params.get("Password")
        self._Token = params.get("Token")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EngineRegionInfo(AbstractModel):
    """引擎地域配置详情

    """

    def __init__(self):
        r"""
        :param _EngineRegion: 引擎节点所在地域
        :type EngineRegion: str
        :param _Replica: 此地域节点分配数量
        :type Replica: int
        :param _VpcInfos: 集群网络信息
        :type VpcInfos: list of VpcInfo
        :param _MainRegion: Polaris: 是否为主地域
Zookeeper: 是否为Leader固定地域
        :type MainRegion: bool
        :param _SpecId: 引擎规格ID
        :type SpecId: str
        """
        self._EngineRegion = None
        self._Replica = None
        self._VpcInfos = None
        self._MainRegion = None
        self._SpecId = None

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def MainRegion(self):
        return self._MainRegion

    @MainRegion.setter
    def MainRegion(self, MainRegion):
        self._MainRegion = MainRegion

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        self._Replica = params.get("Replica")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        self._MainRegion = params.get("MainRegion")
        self._SpecId = params.get("SpecId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvAddressInfo(AbstractModel):
    """多环境网络信息

    """

    def __init__(self):
        r"""
        :param _EnvName: 环境名
        :type EnvName: str
        :param _EnableConfigInternet: 是否开启config公网
        :type EnableConfigInternet: bool
        :param _ConfigInternetServiceIp: config公网ip
        :type ConfigInternetServiceIp: str
        :param _ConfigIntranetAddress: config内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigIntranetAddress: str
        :param _EnableConfigIntranet: 是否开启config内网clb
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConfigIntranet: bool
        :param _InternetBandWidth: 客户端公网带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetBandWidth: int
        :param _CLBMultiRegion: 客户端公网CLB多可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CLBMultiRegion: :class:`tencentcloud.tse.v20201207.models.CLBMultiRegion`
        """
        self._EnvName = None
        self._EnableConfigInternet = None
        self._ConfigInternetServiceIp = None
        self._ConfigIntranetAddress = None
        self._EnableConfigIntranet = None
        self._InternetBandWidth = None
        self._CLBMultiRegion = None

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def EnableConfigInternet(self):
        return self._EnableConfigInternet

    @EnableConfigInternet.setter
    def EnableConfigInternet(self, EnableConfigInternet):
        self._EnableConfigInternet = EnableConfigInternet

    @property
    def ConfigInternetServiceIp(self):
        return self._ConfigInternetServiceIp

    @ConfigInternetServiceIp.setter
    def ConfigInternetServiceIp(self, ConfigInternetServiceIp):
        self._ConfigInternetServiceIp = ConfigInternetServiceIp

    @property
    def ConfigIntranetAddress(self):
        return self._ConfigIntranetAddress

    @ConfigIntranetAddress.setter
    def ConfigIntranetAddress(self, ConfigIntranetAddress):
        self._ConfigIntranetAddress = ConfigIntranetAddress

    @property
    def EnableConfigIntranet(self):
        return self._EnableConfigIntranet

    @EnableConfigIntranet.setter
    def EnableConfigIntranet(self, EnableConfigIntranet):
        self._EnableConfigIntranet = EnableConfigIntranet

    @property
    def InternetBandWidth(self):
        return self._InternetBandWidth

    @InternetBandWidth.setter
    def InternetBandWidth(self, InternetBandWidth):
        self._InternetBandWidth = InternetBandWidth

    @property
    def CLBMultiRegion(self):
        return self._CLBMultiRegion

    @CLBMultiRegion.setter
    def CLBMultiRegion(self, CLBMultiRegion):
        self._CLBMultiRegion = CLBMultiRegion


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        self._EnableConfigInternet = params.get("EnableConfigInternet")
        self._ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self._ConfigIntranetAddress = params.get("ConfigIntranetAddress")
        self._EnableConfigIntranet = params.get("EnableConfigIntranet")
        self._InternetBandWidth = params.get("InternetBandWidth")
        if params.get("CLBMultiRegion") is not None:
            self._CLBMultiRegion = CLBMultiRegion()
            self._CLBMultiRegion._deserialize(params.get("CLBMultiRegion"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvInfo(AbstractModel):
    """环境具体信息

    """

    def __init__(self):
        r"""
        :param _EnvName: 环境名称
        :type EnvName: str
        :param _VpcInfos: 环境对应的网络信息
        :type VpcInfos: list of VpcInfo
        :param _StorageCapacity: 云硬盘容量
        :type StorageCapacity: int
        :param _Status: 运行状态
        :type Status: str
        :param _AdminServiceIp: Admin service 访问地址
        :type AdminServiceIp: str
        :param _ConfigServiceIp: Config service访问地址
        :type ConfigServiceIp: str
        :param _EnableConfigInternet: 是否开启config-server公网
        :type EnableConfigInternet: bool
        :param _ConfigInternetServiceIp: config-server公网访问地址
        :type ConfigInternetServiceIp: str
        :param _SpecId: 规格ID
        :type SpecId: str
        :param _EnvReplica: 环境的节点数
        :type EnvReplica: int
        :param _RunningCount: 环境运行的节点数
        :type RunningCount: int
        :param _AliasEnvName: 环境别名
        :type AliasEnvName: str
        :param _EnvDesc: 环境描述
        :type EnvDesc: str
        :param _ClientBandWidth: 客户端带宽
        :type ClientBandWidth: int
        :param _EnableConfigIntranet: 客户端内网开关
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConfigIntranet: bool
        """
        self._EnvName = None
        self._VpcInfos = None
        self._StorageCapacity = None
        self._Status = None
        self._AdminServiceIp = None
        self._ConfigServiceIp = None
        self._EnableConfigInternet = None
        self._ConfigInternetServiceIp = None
        self._SpecId = None
        self._EnvReplica = None
        self._RunningCount = None
        self._AliasEnvName = None
        self._EnvDesc = None
        self._ClientBandWidth = None
        self._EnableConfigIntranet = None

    @property
    def EnvName(self):
        return self._EnvName

    @EnvName.setter
    def EnvName(self, EnvName):
        self._EnvName = EnvName

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AdminServiceIp(self):
        return self._AdminServiceIp

    @AdminServiceIp.setter
    def AdminServiceIp(self, AdminServiceIp):
        self._AdminServiceIp = AdminServiceIp

    @property
    def ConfigServiceIp(self):
        return self._ConfigServiceIp

    @ConfigServiceIp.setter
    def ConfigServiceIp(self, ConfigServiceIp):
        self._ConfigServiceIp = ConfigServiceIp

    @property
    def EnableConfigInternet(self):
        return self._EnableConfigInternet

    @EnableConfigInternet.setter
    def EnableConfigInternet(self, EnableConfigInternet):
        self._EnableConfigInternet = EnableConfigInternet

    @property
    def ConfigInternetServiceIp(self):
        return self._ConfigInternetServiceIp

    @ConfigInternetServiceIp.setter
    def ConfigInternetServiceIp(self, ConfigInternetServiceIp):
        self._ConfigInternetServiceIp = ConfigInternetServiceIp

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def EnvReplica(self):
        return self._EnvReplica

    @EnvReplica.setter
    def EnvReplica(self, EnvReplica):
        self._EnvReplica = EnvReplica

    @property
    def RunningCount(self):
        return self._RunningCount

    @RunningCount.setter
    def RunningCount(self, RunningCount):
        self._RunningCount = RunningCount

    @property
    def AliasEnvName(self):
        return self._AliasEnvName

    @AliasEnvName.setter
    def AliasEnvName(self, AliasEnvName):
        self._AliasEnvName = AliasEnvName

    @property
    def EnvDesc(self):
        return self._EnvDesc

    @EnvDesc.setter
    def EnvDesc(self, EnvDesc):
        self._EnvDesc = EnvDesc

    @property
    def ClientBandWidth(self):
        return self._ClientBandWidth

    @ClientBandWidth.setter
    def ClientBandWidth(self, ClientBandWidth):
        self._ClientBandWidth = ClientBandWidth

    @property
    def EnableConfigIntranet(self):
        return self._EnableConfigIntranet

    @EnableConfigIntranet.setter
    def EnableConfigIntranet(self, EnableConfigIntranet):
        self._EnableConfigIntranet = EnableConfigIntranet


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        self._StorageCapacity = params.get("StorageCapacity")
        self._Status = params.get("Status")
        self._AdminServiceIp = params.get("AdminServiceIp")
        self._ConfigServiceIp = params.get("ConfigServiceIp")
        self._EnableConfigInternet = params.get("EnableConfigInternet")
        self._ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self._SpecId = params.get("SpecId")
        self._EnvReplica = params.get("EnvReplica")
        self._RunningCount = params.get("RunningCount")
        self._AliasEnvName = params.get("AliasEnvName")
        self._EnvDesc = params.get("EnvDesc")
        self._ClientBandWidth = params.get("ClientBandWidth")
        self._EnableConfigIntranet = params.get("EnableConfigIntranet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExternalRedis(AbstractModel):
    """云原生网关限流插件外部redis配置

    """

    def __init__(self):
        r"""
        :param _RedisHost: redis ip
注意：此字段可能返回 null，表示取不到有效值。
        :type RedisHost: str
        :param _RedisPassword: redis密码
注意：此字段可能返回 null，表示取不到有效值。
        :type RedisPassword: str
        :param _RedisPort: redis端口
注意：此字段可能返回 null，表示取不到有效值。
        :type RedisPort: int
        :param _RedisTimeout: 超时时间  ms
注意：此字段可能返回 null，表示取不到有效值。
        :type RedisTimeout: int
        """
        self._RedisHost = None
        self._RedisPassword = None
        self._RedisPort = None
        self._RedisTimeout = None

    @property
    def RedisHost(self):
        return self._RedisHost

    @RedisHost.setter
    def RedisHost(self, RedisHost):
        self._RedisHost = RedisHost

    @property
    def RedisPassword(self):
        return self._RedisPassword

    @RedisPassword.setter
    def RedisPassword(self, RedisPassword):
        self._RedisPassword = RedisPassword

    @property
    def RedisPort(self):
        return self._RedisPort

    @RedisPort.setter
    def RedisPort(self, RedisPort):
        self._RedisPort = RedisPort

    @property
    def RedisTimeout(self):
        return self._RedisTimeout

    @RedisTimeout.setter
    def RedisTimeout(self, RedisTimeout):
        self._RedisTimeout = RedisTimeout


    def _deserialize(self, params):
        self._RedisHost = params.get("RedisHost")
        self._RedisPassword = params.get("RedisPassword")
        self._RedisPort = params.get("RedisPort")
        self._RedisTimeout = params.get("RedisTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤通用对象

    """

    def __init__(self):
        r"""
        :param _Name: 过滤参数名
        :type Name: str
        :param _Values: 过滤参数值
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
        


class GatewayInstanceSchemeAndPorts(AbstractModel):
    """网关实例协议端口列表

    """

    def __init__(self):
        r"""
        :param _Scheme: 端口协议，可选HTTP、HTTPS、TCP和UDP
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: str
        :param _PortList: 端口列表
注意：此字段可能返回 null，表示取不到有效值。
        :type PortList: list of int non-negative
        """
        self._Scheme = None
        self._PortList = None

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def PortList(self):
        return self._PortList

    @PortList.setter
    def PortList(self, PortList):
        self._PortList = PortList


    def _deserialize(self, params):
        self._Scheme = params.get("Scheme")
        self._PortList = params.get("PortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceAlias(AbstractModel):
    """服务别名结构信息

    """

    def __init__(self):
        r"""
        :param _Alias: 服务别名
        :type Alias: str
        :param _AliasNamespace: 服务别名命名空间
        :type AliasNamespace: str
        :param _Service: 服务别名指向的服务名
        :type Service: str
        :param _Namespace: 服务别名指向的服务命名空间
        :type Namespace: str
        :param _Comment: 服务别名的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreateTime: 服务别名创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 服务别名修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _Id: 服务别名ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Editable: 该服务别名是否可以编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type Editable: bool
        """
        self._Alias = None
        self._AliasNamespace = None
        self._Service = None
        self._Namespace = None
        self._Comment = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Id = None
        self._Editable = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def AliasNamespace(self):
        return self._AliasNamespace

    @AliasNamespace.setter
    def AliasNamespace(self, AliasNamespace):
        self._AliasNamespace = AliasNamespace

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Editable(self):
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._AliasNamespace = params.get("AliasNamespace")
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Comment = params.get("Comment")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Id = params.get("Id")
        self._Editable = params.get("Editable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceInstance(AbstractModel):
    """治理中心实例信息。

    """

    def __init__(self):
        r"""
        :param _Id: 实例id。
        :type Id: str
        :param _Service: 实例所在服务名。
        :type Service: str
        :param _Namespace: 实例所在命名空间名。
        :type Namespace: str
        :param _Host: 实例ip地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Port: 实例端口信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Protocol: 通信协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Version: 版本信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Weight: 负载均衡权重。
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _EnableHealthCheck: 是否开启健康检查。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableHealthCheck: bool
        :param _Healthy: 实例是否健康。
注意：此字段可能返回 null，表示取不到有效值。
        :type Healthy: bool
        :param _Isolate: 实例是否隔离。
注意：此字段可能返回 null，表示取不到有效值。
        :type Isolate: bool
        :param _CreateTime: 实例创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 实例修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _Metadatas: 元数据数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadatas: list of Metadata
        :param _Ttl: 上报心跳间隔。
注意：此字段可能返回 null，表示取不到有效值。
        :type Ttl: int
        :param _InstanceVersion: 版本信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceVersion: str
        :param _HealthStatus: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatus: str
        :param _Comment: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        """
        self._Id = None
        self._Service = None
        self._Namespace = None
        self._Host = None
        self._Port = None
        self._Protocol = None
        self._Version = None
        self._Weight = None
        self._EnableHealthCheck = None
        self._Healthy = None
        self._Isolate = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Metadatas = None
        self._Ttl = None
        self._InstanceVersion = None
        self._HealthStatus = None
        self._Comment = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def EnableHealthCheck(self):
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def Isolate(self):
        return self._Isolate

    @Isolate.setter
    def Isolate(self, Isolate):
        self._Isolate = Isolate

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Metadatas(self):
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._Version = params.get("Version")
        self._Weight = params.get("Weight")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._Healthy = params.get("Healthy")
        self._Isolate = params.get("Isolate")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        self._Ttl = params.get("Ttl")
        self._InstanceVersion = params.get("InstanceVersion")
        self._HealthStatus = params.get("HealthStatus")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceInstanceInput(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _Service: 实例所在服务名。
        :type Service: str
        :param _Namespace: 实例服务所在命名空间。
        :type Namespace: str
        :param _Weight: 实例负载均衡权重信息。不填默认为100。
        :type Weight: int
        :param _Healthy: 实例默认健康信息。不填默认为健康。
        :type Healthy: bool
        :param _Isolate: 实例隔离信息。不填默认为非隔离。
        :type Isolate: bool
        :param _Host: 实例ip。
        :type Host: str
        :param _Port: 实例监听端口。
        :type Port: int
        :param _Protocol: 实例使用协议。不填默认为空。
        :type Protocol: str
        :param _InstanceVersion: 实例版本。不填默认为空。
        :type InstanceVersion: str
        :param _EnableHealthCheck: 是否启用健康检查。不填默认不启用。
        :type EnableHealthCheck: bool
        :param _Ttl: 上报心跳时间间隔。若 EnableHealthCheck 为不启用，则此参数不生效；若 EnableHealthCheck 启用，此参数不填，则默认 ttl 为 5s。
        :type Ttl: int
        """
        self._Service = None
        self._Namespace = None
        self._Weight = None
        self._Healthy = None
        self._Isolate = None
        self._Host = None
        self._Port = None
        self._Protocol = None
        self._InstanceVersion = None
        self._EnableHealthCheck = None
        self._Ttl = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def Isolate(self):
        return self._Isolate

    @Isolate.setter
    def Isolate(self, Isolate):
        self._Isolate = Isolate

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def EnableHealthCheck(self):
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Weight = params.get("Weight")
        self._Healthy = params.get("Healthy")
        self._Isolate = params.get("Isolate")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._InstanceVersion = params.get("InstanceVersion")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._Ttl = params.get("Ttl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceInstanceUpdate(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param _Service: 实例所在服务名。
        :type Service: str
        :param _Namespace: 实例服务所在命名空间。
        :type Namespace: str
        :param _Weight: 实例负载均衡权重信息。不填默认为100。
        :type Weight: int
        :param _Healthy: 实例默认健康信息。不填默认为健康。
        :type Healthy: bool
        :param _Isolate: 实例隔离信息。不填默认为非隔离。
        :type Isolate: bool
        :param _Host: 实例ip。
        :type Host: str
        :param _Port: 实例监听端口。
        :type Port: int
        :param _Protocol: 实例使用协议。不填默认为空。
        :type Protocol: str
        :param _InstanceVersion: 实例版本。不填默认为空。
        :type InstanceVersion: str
        :param _EnableHealthCheck: 是否启用健康检查。不填默认不启用。
        :type EnableHealthCheck: bool
        :param _Ttl: 上报心跳时间间隔。若 EnableHealthCheck 为不启用，则此参数不生效；若 EnableHealthCheck 启用，此参数不填，则默认 ttl 为 5s。
        :type Ttl: int
        :param _Id: 治理中心服务实例id。
        :type Id: str
        :param _Metadatas: 元数据信息。
        :type Metadatas: list of Metadata
        """
        self._Service = None
        self._Namespace = None
        self._Weight = None
        self._Healthy = None
        self._Isolate = None
        self._Host = None
        self._Port = None
        self._Protocol = None
        self._InstanceVersion = None
        self._EnableHealthCheck = None
        self._Ttl = None
        self._Id = None
        self._Metadatas = None

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def Isolate(self):
        return self._Isolate

    @Isolate.setter
    def Isolate(self, Isolate):
        self._Isolate = Isolate

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InstanceVersion(self):
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def EnableHealthCheck(self):
        return self._EnableHealthCheck

    @EnableHealthCheck.setter
    def EnableHealthCheck(self, EnableHealthCheck):
        self._EnableHealthCheck = EnableHealthCheck

    @property
    def Ttl(self):
        return self._Ttl

    @Ttl.setter
    def Ttl(self, Ttl):
        self._Ttl = Ttl

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Metadatas(self):
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas


    def _deserialize(self, params):
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Weight = params.get("Weight")
        self._Healthy = params.get("Healthy")
        self._Isolate = params.get("Isolate")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._InstanceVersion = params.get("InstanceVersion")
        self._EnableHealthCheck = params.get("EnableHealthCheck")
        self._Ttl = params.get("Ttl")
        self._Id = params.get("Id")
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceInterfaceDescription(AbstractModel):
    """服务契约接口定义

    """

    def __init__(self):
        r"""
        :param _ID: 契约接口ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Method: 方法名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _Path: 路径/接口名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Content: 内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _Source: 创建来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Revision: 信息摘要
注意：此字段可能返回 null，表示取不到有效值。
        :type Revision: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _Name: 接口名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._ID = None
        self._Method = None
        self._Path = None
        self._Content = None
        self._Source = None
        self._Revision = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Name = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Revision(self):
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Method = params.get("Method")
        self._Path = params.get("Path")
        self._Content = params.get("Content")
        self._Source = params.get("Source")
        self._Revision = params.get("Revision")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceNamespace(AbstractModel):
    """治理中心命名空间

    """

    def __init__(self):
        r"""
        :param _Name: 命名空间名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Comment: 命名空间描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _TotalServiceCount: 命名空间下总服务数据量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalServiceCount: int
        :param _TotalHealthInstanceCount: 命名空间下总健康实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalHealthInstanceCount: int
        :param _TotalInstanceCount: 命名空间下总实例数量
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalInstanceCount: int
        :param _Id: 命名空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Editable: 是否可以编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type Editable: bool
        :param _UserIds: 可以操作此命名空间的用户ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIds: list of str
        :param _GroupIds: 可以操作此命名空间的用户组ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupIds: list of str
        :param _RemoveUserIds: 移除可以操作此命名空间的用户ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveUserIds: list of str
        :param _RemoveGroupIds: 移除可以操作此命名空间的用户组ID列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveGroupIds: list of str
        """
        self._Name = None
        self._Comment = None
        self._CreateTime = None
        self._ModifyTime = None
        self._TotalServiceCount = None
        self._TotalHealthInstanceCount = None
        self._TotalInstanceCount = None
        self._Id = None
        self._Editable = None
        self._UserIds = None
        self._GroupIds = None
        self._RemoveUserIds = None
        self._RemoveGroupIds = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def TotalServiceCount(self):
        return self._TotalServiceCount

    @TotalServiceCount.setter
    def TotalServiceCount(self, TotalServiceCount):
        self._TotalServiceCount = TotalServiceCount

    @property
    def TotalHealthInstanceCount(self):
        return self._TotalHealthInstanceCount

    @TotalHealthInstanceCount.setter
    def TotalHealthInstanceCount(self, TotalHealthInstanceCount):
        self._TotalHealthInstanceCount = TotalHealthInstanceCount

    @property
    def TotalInstanceCount(self):
        return self._TotalInstanceCount

    @TotalInstanceCount.setter
    def TotalInstanceCount(self, TotalInstanceCount):
        self._TotalInstanceCount = TotalInstanceCount

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Editable(self):
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RemoveUserIds(self):
        return self._RemoveUserIds

    @RemoveUserIds.setter
    def RemoveUserIds(self, RemoveUserIds):
        self._RemoveUserIds = RemoveUserIds

    @property
    def RemoveGroupIds(self):
        return self._RemoveGroupIds

    @RemoveGroupIds.setter
    def RemoveGroupIds(self, RemoveGroupIds):
        self._RemoveGroupIds = RemoveGroupIds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Comment = params.get("Comment")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._TotalServiceCount = params.get("TotalServiceCount")
        self._TotalHealthInstanceCount = params.get("TotalHealthInstanceCount")
        self._TotalInstanceCount = params.get("TotalInstanceCount")
        self._Id = params.get("Id")
        self._Editable = params.get("Editable")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._RemoveUserIds = params.get("RemoveUserIds")
        self._RemoveGroupIds = params.get("RemoveGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceNamespaceInput(AbstractModel):
    """治理中心命名空间输入参数

    """

    def __init__(self):
        r"""
        :param _Name: 命名空间名。
        :type Name: str
        :param _Comment: 描述信息。
        :type Comment: str
        :param _UserIds: 新增的可以操作此命名空间的用户ID列表
        :type UserIds: list of str
        :param _GroupIds: 新增的可以操作此命名空间的用户组ID列表
        :type GroupIds: list of str
        :param _RemoveUserIds: 移除可以操作此命名空间的用户ID列表
        :type RemoveUserIds: list of str
        :param _RemoveGroupIds: 移除可以操作此命名空间的用户组ID列表
        :type RemoveGroupIds: list of str
        """
        self._Name = None
        self._Comment = None
        self._UserIds = None
        self._GroupIds = None
        self._RemoveUserIds = None
        self._RemoveGroupIds = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RemoveUserIds(self):
        return self._RemoveUserIds

    @RemoveUserIds.setter
    def RemoveUserIds(self, RemoveUserIds):
        self._RemoveUserIds = RemoveUserIds

    @property
    def RemoveGroupIds(self):
        return self._RemoveGroupIds

    @RemoveGroupIds.setter
    def RemoveGroupIds(self, RemoveGroupIds):
        self._RemoveGroupIds = RemoveGroupIds


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Comment = params.get("Comment")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._RemoveUserIds = params.get("RemoveUserIds")
        self._RemoveGroupIds = params.get("RemoveGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceService(AbstractModel):
    """治理中心服务信息。

    """

    def __init__(self):
        r"""
        :param _Name: 服务名称。
        :type Name: str
        :param _Namespace: 命名空间名称。
        :type Namespace: str
        :param _Metadatas: 元数据信息数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadatas: list of Metadata
        :param _Comment: 描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _Department: 服务所属部门。
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: str
        :param _Business: 服务所属业务。
注意：此字段可能返回 null，表示取不到有效值。
        :type Business: str
        :param _HealthyInstanceCount: 健康服务实例数
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyInstanceCount: int
        :param _TotalInstanceCount: 服务实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalInstanceCount: int
        :param _Id: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Editable: 是否可以编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type Editable: bool
        :param _UserIds: 可以编辑该资源的用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserIds: list of str
        :param _GroupIds: 可以编辑该资源的用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupIds: list of str
        :param _RemoveUserIds: 移除可以编辑该资源的用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveUserIds: list of str
        :param _RemoveGroupIds: 移除可以编辑该资源的用户组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoveGroupIds: list of str
        :param _ExportTo: 该服务对哪些命名空间可见	
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportTo: list of str
        :param _Revision: 该服务信息摘要签名
注意：此字段可能返回 null，表示取不到有效值。
        :type Revision: str
        """
        self._Name = None
        self._Namespace = None
        self._Metadatas = None
        self._Comment = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Department = None
        self._Business = None
        self._HealthyInstanceCount = None
        self._TotalInstanceCount = None
        self._Id = None
        self._Editable = None
        self._UserIds = None
        self._GroupIds = None
        self._RemoveUserIds = None
        self._RemoveGroupIds = None
        self._ExportTo = None
        self._Revision = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Metadatas(self):
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def HealthyInstanceCount(self):
        return self._HealthyInstanceCount

    @HealthyInstanceCount.setter
    def HealthyInstanceCount(self, HealthyInstanceCount):
        self._HealthyInstanceCount = HealthyInstanceCount

    @property
    def TotalInstanceCount(self):
        return self._TotalInstanceCount

    @TotalInstanceCount.setter
    def TotalInstanceCount(self, TotalInstanceCount):
        self._TotalInstanceCount = TotalInstanceCount

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Editable(self):
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RemoveUserIds(self):
        return self._RemoveUserIds

    @RemoveUserIds.setter
    def RemoveUserIds(self, RemoveUserIds):
        self._RemoveUserIds = RemoveUserIds

    @property
    def RemoveGroupIds(self):
        return self._RemoveGroupIds

    @RemoveGroupIds.setter
    def RemoveGroupIds(self, RemoveGroupIds):
        self._RemoveGroupIds = RemoveGroupIds

    @property
    def ExportTo(self):
        return self._ExportTo

    @ExportTo.setter
    def ExportTo(self, ExportTo):
        self._ExportTo = ExportTo

    @property
    def Revision(self):
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        self._Comment = params.get("Comment")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        self._Department = params.get("Department")
        self._Business = params.get("Business")
        self._HealthyInstanceCount = params.get("HealthyInstanceCount")
        self._TotalInstanceCount = params.get("TotalInstanceCount")
        self._Id = params.get("Id")
        self._Editable = params.get("Editable")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._RemoveUserIds = params.get("RemoveUserIds")
        self._RemoveGroupIds = params.get("RemoveGroupIds")
        self._ExportTo = params.get("ExportTo")
        self._Revision = params.get("Revision")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceServiceContract(AbstractModel):
    """服务契约定义

    """

    def __init__(self):
        r"""
        :param _Name: 契约名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Namespace: 所属服务命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _ID: 契约ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Service: 所属服务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Service: str
        :param _Version: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Revision: 信息摘要
注意：此字段可能返回 null，表示取不到有效值。
        :type Revision: str
        :param _Content: 额外内容描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _Interfaces: 契约接口列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Interfaces: list of GovernanceInterfaceDescription
        """
        self._Name = None
        self._Namespace = None
        self._Protocol = None
        self._ID = None
        self._Service = None
        self._Version = None
        self._Revision = None
        self._Content = None
        self._CreateTime = None
        self._ModifyTime = None
        self._Interfaces = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Revision(self):
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Interfaces(self):
        return self._Interfaces

    @Interfaces.setter
    def Interfaces(self, Interfaces):
        self._Interfaces = Interfaces


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Protocol = params.get("Protocol")
        self._ID = params.get("ID")
        self._Service = params.get("Service")
        self._Version = params.get("Version")
        self._Revision = params.get("Revision")
        self._Content = params.get("Content")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("Interfaces") is not None:
            self._Interfaces = []
            for item in params.get("Interfaces"):
                obj = GovernanceInterfaceDescription()
                obj._deserialize(item)
                self._Interfaces.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceServiceContractVersion(AbstractModel):
    """服务契约版本信息

    """

    def __init__(self):
        r"""
        :param _Version: 契约版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _Name: 契约名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Key: 唯一名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        """
        self._Version = None
        self._Name = None
        self._Key = None

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Version = params.get("Version")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GovernanceServiceInput(AbstractModel):
    """治理中心服务入参

    """

    def __init__(self):
        r"""
        :param _Name: 服务名。
        :type Name: str
        :param _Namespace: 服务所属命名空间。
        :type Namespace: str
        :param _Comment: 服务描述信息。
        :type Comment: str
        :param _Metadatas: 服务元数据。
        :type Metadatas: list of Metadata
        :param _Department: 服务所属部门。
        :type Department: str
        :param _Business: 服务所属业务。
        :type Business: str
        :param _UserIds: 被添加进来可以操作此命名空间的用户ID列表
        :type UserIds: list of str
        :param _GroupIds: 被添加进来可以操作此命名空间的用户组ID列表
        :type GroupIds: list of str
        :param _RemoveUserIds: 从操作此命名空间的用户组ID列表被移除的ID列表
        :type RemoveUserIds: list of str
        :param _RemoveGroupIds: 从可以操作此命名空间的用户组ID列表中被移除的ID列表
        :type RemoveGroupIds: list of str
        :param _ExportTo: 该服务对哪些命名空间可见
        :type ExportTo: list of str
        """
        self._Name = None
        self._Namespace = None
        self._Comment = None
        self._Metadatas = None
        self._Department = None
        self._Business = None
        self._UserIds = None
        self._GroupIds = None
        self._RemoveUserIds = None
        self._RemoveGroupIds = None
        self._ExportTo = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def Metadatas(self):
        return self._Metadatas

    @Metadatas.setter
    def Metadatas(self, Metadatas):
        self._Metadatas = Metadatas

    @property
    def Department(self):
        return self._Department

    @Department.setter
    def Department(self, Department):
        self._Department = Department

    @property
    def Business(self):
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def UserIds(self):
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds

    @property
    def RemoveUserIds(self):
        return self._RemoveUserIds

    @RemoveUserIds.setter
    def RemoveUserIds(self, RemoveUserIds):
        self._RemoveUserIds = RemoveUserIds

    @property
    def RemoveGroupIds(self):
        return self._RemoveGroupIds

    @RemoveGroupIds.setter
    def RemoveGroupIds(self, RemoveGroupIds):
        self._RemoveGroupIds = RemoveGroupIds

    @property
    def ExportTo(self):
        return self._ExportTo

    @ExportTo.setter
    def ExportTo(self, ExportTo):
        self._ExportTo = ExportTo


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Namespace = params.get("Namespace")
        self._Comment = params.get("Comment")
        if params.get("Metadatas") is not None:
            self._Metadatas = []
            for item in params.get("Metadatas"):
                obj = Metadata()
                obj._deserialize(item)
                self._Metadatas.append(obj)
        self._Department = params.get("Department")
        self._Business = params.get("Business")
        self._UserIds = params.get("UserIds")
        self._GroupIds = params.get("GroupIds")
        self._RemoveUserIds = params.get("RemoveUserIds")
        self._RemoveGroupIds = params.get("RemoveGroupIds")
        self._ExportTo = params.get("ExportTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstancePort(AbstractModel):
    """实例监听端口信息

    """

    def __init__(self):
        r"""
        :param _HttpPort: 监听的 http 端口范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpPort: str
        :param _HttpsPort: 监听的 https 端口范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpsPort: str
        :param _TcpPort: 监听的 tcp 端口范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type TcpPort: str
        :param _UdpPort: 监听的 udp 端口范围。
注意：此字段可能返回 null，表示取不到有效值。
        :type UdpPort: str
        """
        self._HttpPort = None
        self._HttpsPort = None
        self._TcpPort = None
        self._UdpPort = None

    @property
    def HttpPort(self):
        return self._HttpPort

    @HttpPort.setter
    def HttpPort(self, HttpPort):
        self._HttpPort = HttpPort

    @property
    def HttpsPort(self):
        return self._HttpsPort

    @HttpsPort.setter
    def HttpsPort(self, HttpsPort):
        self._HttpsPort = HttpsPort

    @property
    def TcpPort(self):
        return self._TcpPort

    @TcpPort.setter
    def TcpPort(self, TcpPort):
        self._TcpPort = TcpPort

    @property
    def UdpPort(self):
        return self._UdpPort

    @UdpPort.setter
    def UdpPort(self, UdpPort):
        self._UdpPort = UdpPort


    def _deserialize(self, params):
        self._HttpPort = params.get("HttpPort")
        self._HttpsPort = params.get("HttpsPort")
        self._TcpPort = params.get("TcpPort")
        self._UdpPort = params.get("UdpPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTagInfo(AbstractModel):
    """引擎实例的标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InternetConfig(AbstractModel):
    """公网负载均衡配置

    """

    def __init__(self):
        r"""
        :param _InternetAddressVersion: 公网地址版本，可选："IPV4" | "IPV6" 。不填默认 IPV4 。
        :type InternetAddressVersion: str
        :param _InternetPayMode: 公网付费类型，当前仅可选："BANDWIDTH"。不填默认为 "BANDWIDTH"
        :type InternetPayMode: str
        :param _InternetMaxBandwidthOut: 公网带宽。
        :type InternetMaxBandwidthOut: int
        :param _Description: 负载均衡描述
        :type Description: str
        :param _SlaType: 负载均衡的规格类型，支持clb.c2.medium、clb.c3.small、clb.c3.medium、clb.c4.small、clb.c4.medium、clb.c4.large、clb.c4.xlarge，不传为共享型。
        :type SlaType: str
        :param _MultiZoneFlag: 负载均衡是否多可用区
        :type MultiZoneFlag: bool
        :param _MasterZoneId: 主可用区
        :type MasterZoneId: str
        :param _SlaveZoneId: 备可用区
        :type SlaveZoneId: str
        """
        self._InternetAddressVersion = None
        self._InternetPayMode = None
        self._InternetMaxBandwidthOut = None
        self._Description = None
        self._SlaType = None
        self._MultiZoneFlag = None
        self._MasterZoneId = None
        self._SlaveZoneId = None

    @property
    def InternetAddressVersion(self):
        return self._InternetAddressVersion

    @InternetAddressVersion.setter
    def InternetAddressVersion(self, InternetAddressVersion):
        self._InternetAddressVersion = InternetAddressVersion

    @property
    def InternetPayMode(self):
        return self._InternetPayMode

    @InternetPayMode.setter
    def InternetPayMode(self, InternetPayMode):
        self._InternetPayMode = InternetPayMode

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SlaType(self):
        return self._SlaType

    @SlaType.setter
    def SlaType(self, SlaType):
        self._SlaType = SlaType

    @property
    def MultiZoneFlag(self):
        return self._MultiZoneFlag

    @MultiZoneFlag.setter
    def MultiZoneFlag(self, MultiZoneFlag):
        self._MultiZoneFlag = MultiZoneFlag

    @property
    def MasterZoneId(self):
        return self._MasterZoneId

    @MasterZoneId.setter
    def MasterZoneId(self, MasterZoneId):
        self._MasterZoneId = MasterZoneId

    @property
    def SlaveZoneId(self):
        return self._SlaveZoneId

    @SlaveZoneId.setter
    def SlaveZoneId(self, SlaveZoneId):
        self._SlaveZoneId = SlaveZoneId


    def _deserialize(self, params):
        self._InternetAddressVersion = params.get("InternetAddressVersion")
        self._InternetPayMode = params.get("InternetPayMode")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._Description = params.get("Description")
        self._SlaType = params.get("SlaType")
        self._MultiZoneFlag = params.get("MultiZoneFlag")
        self._MasterZoneId = params.get("MasterZoneId")
        self._SlaveZoneId = params.get("SlaveZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KVMapping(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class KVPair(AbstractModel):
    """键值对

    """

    def __init__(self):
        r"""
        :param _Key: 键
        :type Key: str
        :param _Value: 值
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
        


class KeyValue(AbstractModel):
    """Key/Value结构

    """

    def __init__(self):
        r"""
        :param _Key: 条件的Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 条件的Value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class KongActiveHealthCheck(AbstractModel):
    """Kong网关主动健康检查配置

    """

    def __init__(self):
        r"""
        :param _HealthyInterval: 主动健康检查健康探测间隔，单位：秒，0表示不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyInterval: int
        :param _UnHealthyInterval: 主动健康检查异常探测间隔，单位：秒，0表示不开启
注意：此字段可能返回 null，表示取不到有效值。
        :type UnHealthyInterval: int
        :param _HttpPath: 在 GET HTTP 请求中使用的路径，以作为主动运行状况检查的探测器运行。默认： ”/”。
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpPath: str
        """
        self._HealthyInterval = None
        self._UnHealthyInterval = None
        self._HttpPath = None

    @property
    def HealthyInterval(self):
        return self._HealthyInterval

    @HealthyInterval.setter
    def HealthyInterval(self, HealthyInterval):
        self._HealthyInterval = HealthyInterval

    @property
    def UnHealthyInterval(self):
        return self._UnHealthyInterval

    @UnHealthyInterval.setter
    def UnHealthyInterval(self, UnHealthyInterval):
        self._UnHealthyInterval = UnHealthyInterval

    @property
    def HttpPath(self):
        return self._HttpPath

    @HttpPath.setter
    def HttpPath(self, HttpPath):
        self._HttpPath = HttpPath


    def _deserialize(self, params):
        self._HealthyInterval = params.get("HealthyInterval")
        self._UnHealthyInterval = params.get("UnHealthyInterval")
        self._HttpPath = params.get("HttpPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongCertificate(AbstractModel):
    """云原生网关证书

    """

    def __init__(self):
        r"""
        :param _Cert: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Cert: :class:`tencentcloud.tse.v20201207.models.KongCertificatesPreview`
        """
        self._Cert = None

    @property
    def Cert(self):
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert


    def _deserialize(self, params):
        if params.get("Cert") is not None:
            self._Cert = KongCertificatesPreview()
            self._Cert._deserialize(params.get("Cert"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongCertificatesList(AbstractModel):
    """kong证书列表

    """

    def __init__(self):
        r"""
        :param _Total: 证书列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _CertificatesList: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatesList: list of KongCertificatesPreview
        :param _Pages: 证书列表总页数
注意：此字段可能返回 null，表示取不到有效值。
        :type Pages: int
        """
        self._Total = None
        self._CertificatesList = None
        self._Pages = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CertificatesList(self):
        return self._CertificatesList

    @CertificatesList.setter
    def CertificatesList(self, CertificatesList):
        self._CertificatesList = CertificatesList

    @property
    def Pages(self):
        warnings.warn("parameter `Pages` is deprecated", DeprecationWarning) 

        return self._Pages

    @Pages.setter
    def Pages(self, Pages):
        warnings.warn("parameter `Pages` is deprecated", DeprecationWarning) 

        self._Pages = Pages


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CertificatesList") is not None:
            self._CertificatesList = []
            for item in params.get("CertificatesList"):
                obj = KongCertificatesPreview()
                obj._deserialize(item)
                self._CertificatesList.append(obj)
        self._Pages = params.get("Pages")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongCertificatesPreview(AbstractModel):
    """云原生网关证书预览信息

    """

    def __init__(self):
        r"""
        :param _Name: 证书名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Id: Id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _BindDomains: 绑定的域名
注意：此字段可能返回 null，表示取不到有效值。
        :type BindDomains: list of str
        :param _Status: 证书状态：expired(已过期)
                   active(生效中)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Crt: 证书pem格式
注意：此字段可能返回 null，表示取不到有效值。
        :type Crt: str
        :param _Key: 证书私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _ExpireTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _CreateTime: 证书上传时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _IssueTime: 证书签发时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IssueTime: str
        :param _CertSource: 证书来源：native(kong自定义证书)
                    ssl(ssl平台证书)
注意：此字段可能返回 null，表示取不到有效值。
        :type CertSource: str
        :param _CertId: ssl平台证书Id
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        """
        self._Name = None
        self._Id = None
        self._BindDomains = None
        self._Status = None
        self._Crt = None
        self._Key = None
        self._ExpireTime = None
        self._CreateTime = None
        self._IssueTime = None
        self._CertSource = None
        self._CertId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BindDomains(self):
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Crt(self):
        return self._Crt

    @Crt.setter
    def Crt(self, Crt):
        self._Crt = Crt

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IssueTime(self):
        return self._IssueTime

    @IssueTime.setter
    def IssueTime(self, IssueTime):
        self._IssueTime = IssueTime

    @property
    def CertSource(self):
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._BindDomains = params.get("BindDomains")
        self._Status = params.get("Status")
        self._Crt = params.get("Crt")
        self._Key = params.get("Key")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._IssueTime = params.get("IssueTime")
        self._CertSource = params.get("CertSource")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongPassiveHealthCheck(AbstractModel):
    """Kong网关被动健康检查配置

    """

    def __init__(self):
        r"""
        :param _Type: 后端target协议类型，被动健康检查支持http和tcp，主动健康检查支持http
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        """
        self._Type = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongRoutePreview(AbstractModel):
    """云原生网关路由信息

    """

    def __init__(self):
        r"""
        :param _ID: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Name: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Methods: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Methods: list of str
        :param _Paths: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Paths: list of str
        :param _Hosts: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Hosts: list of str
        :param _Protocols: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocols: list of str
        :param _PreserveHost: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type PreserveHost: bool
        :param _HttpsRedirectStatusCode: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpsRedirectStatusCode: int
        :param _StripPath: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type StripPath: bool
        :param _CreatedTime: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ForceHttps: 是否开启了强制HTTPS
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceHttps: bool
        :param _ServiceName: 服务名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ServiceID: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceID: str
        :param _DestinationPorts: 目的端口
注意：此字段可能返回 null，表示取不到有效值。
        :type DestinationPorts: list of int non-negative
        :param _Headers: 路由的Headers
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of KVMapping
        """
        self._ID = None
        self._Name = None
        self._Methods = None
        self._Paths = None
        self._Hosts = None
        self._Protocols = None
        self._PreserveHost = None
        self._HttpsRedirectStatusCode = None
        self._StripPath = None
        self._CreatedTime = None
        self._ForceHttps = None
        self._ServiceName = None
        self._ServiceID = None
        self._DestinationPorts = None
        self._Headers = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Methods(self):
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def PreserveHost(self):
        return self._PreserveHost

    @PreserveHost.setter
    def PreserveHost(self, PreserveHost):
        self._PreserveHost = PreserveHost

    @property
    def HttpsRedirectStatusCode(self):
        return self._HttpsRedirectStatusCode

    @HttpsRedirectStatusCode.setter
    def HttpsRedirectStatusCode(self, HttpsRedirectStatusCode):
        self._HttpsRedirectStatusCode = HttpsRedirectStatusCode

    @property
    def StripPath(self):
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ForceHttps(self):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        self._ForceHttps = ForceHttps

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceID(self):
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def DestinationPorts(self):
        return self._DestinationPorts

    @DestinationPorts.setter
    def DestinationPorts(self, DestinationPorts):
        self._DestinationPorts = DestinationPorts

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Methods = params.get("Methods")
        self._Paths = params.get("Paths")
        self._Hosts = params.get("Hosts")
        self._Protocols = params.get("Protocols")
        self._PreserveHost = params.get("PreserveHost")
        self._HttpsRedirectStatusCode = params.get("HttpsRedirectStatusCode")
        self._StripPath = params.get("StripPath")
        self._CreatedTime = params.get("CreatedTime")
        self._ForceHttps = params.get("ForceHttps")
        self._ServiceName = params.get("ServiceName")
        self._ServiceID = params.get("ServiceID")
        self._DestinationPorts = params.get("DestinationPorts")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServiceDetail(AbstractModel):
    """云原生网关服务详细信息

    """

    def __init__(self):
        r"""
        :param _ID: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Name: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Protocol: 后端协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Path: 后端路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Timeout: 后端延时，单位ms
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        :param _Retries: 重试次数
注意：此字段可能返回 null，表示取不到有效值。
        :type Retries: int
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _UpstreamInfo: 后端配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _UpstreamType: 后端类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamType: str
        :param _Editable: 是否可编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type Editable: bool
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self._ID = None
        self._Name = None
        self._Protocol = None
        self._Path = None
        self._Timeout = None
        self._Retries = None
        self._Tags = None
        self._UpstreamInfo = None
        self._UpstreamType = None
        self._Editable = None
        self._CreatedTime = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpstreamInfo(self):
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Editable(self):
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Path = params.get("Path")
        self._Timeout = params.get("Timeout")
        self._Retries = params.get("Retries")
        self._Tags = params.get("Tags")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._UpstreamType = params.get("UpstreamType")
        self._Editable = params.get("Editable")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServicePreview(AbstractModel):
    """云原生网关服务预览信息

    """

    def __init__(self):
        r"""
        :param _ID: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Name: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _UpstreamInfo: 后端配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _UpstreamType: 后端类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamType: str
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _Editable: 是否可编辑
注意：此字段可能返回 null，表示取不到有效值。
        :type Editable: bool
        :param _Path: 请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self._ID = None
        self._Name = None
        self._Tags = None
        self._UpstreamInfo = None
        self._UpstreamType = None
        self._CreatedTime = None
        self._Editable = None
        self._Path = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpstreamInfo(self):
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Editable(self):
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        self._Tags = params.get("Tags")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._UpstreamType = params.get("UpstreamType")
        self._CreatedTime = params.get("CreatedTime")
        self._Editable = params.get("Editable")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServiceRouteList(AbstractModel):
    """kong服务路由列表

    """

    def __init__(self):
        r"""
        :param _RouteList: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type RouteList: list of KongRoutePreview
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._RouteList = None
        self._TotalCount = None

    @property
    def RouteList(self):
        return self._RouteList

    @RouteList.setter
    def RouteList(self, RouteList):
        self._RouteList = RouteList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("RouteList") is not None:
            self._RouteList = []
            for item in params.get("RouteList"):
                obj = KongRoutePreview()
                obj._deserialize(item)
                self._RouteList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongServices(AbstractModel):
    """kong实例的服务列表

    """

    def __init__(self):
        r"""
        :param _ServiceList: kong实例的服务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceList: list of KongServicePreview
        :param _TotalCount: 列表总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        """
        self._ServiceList = None
        self._TotalCount = None

    @property
    def ServiceList(self):
        return self._ServiceList

    @ServiceList.setter
    def ServiceList(self, ServiceList):
        self._ServiceList = ServiceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ServiceList") is not None:
            self._ServiceList = []
            for item in params.get("ServiceList"):
                obj = KongServicePreview()
                obj._deserialize(item)
                self._ServiceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongTarget(AbstractModel):
    """Kong Upstream中的Target

    """

    def __init__(self):
        r"""
        :param _Host: Host
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Weight: 权重
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _Health: 健康状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Health: str
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _Source: Target的来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _CvmInstanceId: CVM实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceId: str
        :param _CvmInstanceName: CVM实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CvmInstanceName: str
        :param _Tags: target标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        """
        self._Host = None
        self._Port = None
        self._Weight = None
        self._Health = None
        self._CreatedTime = None
        self._Source = None
        self._CvmInstanceId = None
        self._CvmInstanceName = None
        self._Tags = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Health(self):
        return self._Health

    @Health.setter
    def Health(self, Health):
        self._Health = Health

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def CvmInstanceId(self):
        return self._CvmInstanceId

    @CvmInstanceId.setter
    def CvmInstanceId(self, CvmInstanceId):
        self._CvmInstanceId = CvmInstanceId

    @property
    def CvmInstanceName(self):
        return self._CvmInstanceName

    @CvmInstanceName.setter
    def CvmInstanceName(self, CvmInstanceName):
        self._CvmInstanceName = CvmInstanceName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._Health = params.get("Health")
        self._CreatedTime = params.get("CreatedTime")
        self._Source = params.get("Source")
        self._CvmInstanceId = params.get("CvmInstanceId")
        self._CvmInstanceName = params.get("CvmInstanceName")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongUpstreamInfo(AbstractModel):
    """服务的后端配置

    """

    def __init__(self):
        r"""
        :param _Host: IP或域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _SourceID: 服务来源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceID: str
        :param _Namespace: 命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _ServiceName: 服务（注册中心或Kubernetes中的服务）名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _Targets: 服务后端类型是IPList时提供
注意：此字段可能返回 null，表示取不到有效值。
        :type Targets: list of KongTarget
        :param _SourceType: 服务来源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _ScfType: SCF函数类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfType: str
        :param _ScfNamespace: SCF函数命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfNamespace: str
        :param _ScfLambdaName: SCF函数名
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfLambdaName: str
        :param _ScfLambdaQualifier: SCF函数版本
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfLambdaQualifier: str
        :param _SlowStart: 冷启动时间，单位秒
注意：此字段可能返回 null，表示取不到有效值。
        :type SlowStart: int
        :param _Algorithm: 负载均衡算法，默认为 round-robin，还支持 least-connections，consisten_hashing
注意：此字段可能返回 null，表示取不到有效值。
        :type Algorithm: str
        :param _AutoScalingGroupID: CVM弹性伸缩组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoScalingGroupID: str
        :param _AutoScalingCvmPort: CVM弹性伸缩组端口
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoScalingCvmPort: int
        :param _AutoScalingTatCmdStatus: CVM弹性伸缩组使用的CVM TAT命令状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoScalingTatCmdStatus: str
        :param _AutoScalingHookStatus: CVM弹性伸缩组生命周期挂钩状态
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoScalingHookStatus: str
        :param _SourceName: 服务来源的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceName: str
        :param _RealSourceType: 精确的服务来源类型，新建服务来源时候传入的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RealSourceType: str
        :param _HealthStatus: upstream健康状态HEALTHY（健康）, UNHEALTHY（异常）, HEALTHCHECKS_OFF（未开启）和NONE（不支持健康检查）
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthStatus: str
        :param _ScfCamAuthEnable: 云函数是否开启CAM鉴权，不填时默认为开启(true)
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfCamAuthEnable: bool
        :param _ScfIsBase64Encoded: 云函数是否开启Base64编码，默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfIsBase64Encoded: bool
        :param _ScfIsIntegratedResponse: 云函数是否开启响应集成，默认为false
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfIsIntegratedResponse: bool
        """
        self._Host = None
        self._Port = None
        self._SourceID = None
        self._Namespace = None
        self._ServiceName = None
        self._Targets = None
        self._SourceType = None
        self._ScfType = None
        self._ScfNamespace = None
        self._ScfLambdaName = None
        self._ScfLambdaQualifier = None
        self._SlowStart = None
        self._Algorithm = None
        self._AutoScalingGroupID = None
        self._AutoScalingCvmPort = None
        self._AutoScalingTatCmdStatus = None
        self._AutoScalingHookStatus = None
        self._SourceName = None
        self._RealSourceType = None
        self._HealthStatus = None
        self._ScfCamAuthEnable = None
        self._ScfIsBase64Encoded = None
        self._ScfIsIntegratedResponse = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def SourceID(self):
        return self._SourceID

    @SourceID.setter
    def SourceID(self, SourceID):
        self._SourceID = SourceID

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def ScfType(self):
        return self._ScfType

    @ScfType.setter
    def ScfType(self, ScfType):
        self._ScfType = ScfType

    @property
    def ScfNamespace(self):
        return self._ScfNamespace

    @ScfNamespace.setter
    def ScfNamespace(self, ScfNamespace):
        self._ScfNamespace = ScfNamespace

    @property
    def ScfLambdaName(self):
        return self._ScfLambdaName

    @ScfLambdaName.setter
    def ScfLambdaName(self, ScfLambdaName):
        self._ScfLambdaName = ScfLambdaName

    @property
    def ScfLambdaQualifier(self):
        return self._ScfLambdaQualifier

    @ScfLambdaQualifier.setter
    def ScfLambdaQualifier(self, ScfLambdaQualifier):
        self._ScfLambdaQualifier = ScfLambdaQualifier

    @property
    def SlowStart(self):
        return self._SlowStart

    @SlowStart.setter
    def SlowStart(self, SlowStart):
        self._SlowStart = SlowStart

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def AutoScalingGroupID(self):
        return self._AutoScalingGroupID

    @AutoScalingGroupID.setter
    def AutoScalingGroupID(self, AutoScalingGroupID):
        self._AutoScalingGroupID = AutoScalingGroupID

    @property
    def AutoScalingCvmPort(self):
        return self._AutoScalingCvmPort

    @AutoScalingCvmPort.setter
    def AutoScalingCvmPort(self, AutoScalingCvmPort):
        self._AutoScalingCvmPort = AutoScalingCvmPort

    @property
    def AutoScalingTatCmdStatus(self):
        return self._AutoScalingTatCmdStatus

    @AutoScalingTatCmdStatus.setter
    def AutoScalingTatCmdStatus(self, AutoScalingTatCmdStatus):
        self._AutoScalingTatCmdStatus = AutoScalingTatCmdStatus

    @property
    def AutoScalingHookStatus(self):
        return self._AutoScalingHookStatus

    @AutoScalingHookStatus.setter
    def AutoScalingHookStatus(self, AutoScalingHookStatus):
        self._AutoScalingHookStatus = AutoScalingHookStatus

    @property
    def SourceName(self):
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def RealSourceType(self):
        return self._RealSourceType

    @RealSourceType.setter
    def RealSourceType(self, RealSourceType):
        self._RealSourceType = RealSourceType

    @property
    def HealthStatus(self):
        return self._HealthStatus

    @HealthStatus.setter
    def HealthStatus(self, HealthStatus):
        self._HealthStatus = HealthStatus

    @property
    def ScfCamAuthEnable(self):
        return self._ScfCamAuthEnable

    @ScfCamAuthEnable.setter
    def ScfCamAuthEnable(self, ScfCamAuthEnable):
        self._ScfCamAuthEnable = ScfCamAuthEnable

    @property
    def ScfIsBase64Encoded(self):
        return self._ScfIsBase64Encoded

    @ScfIsBase64Encoded.setter
    def ScfIsBase64Encoded(self, ScfIsBase64Encoded):
        self._ScfIsBase64Encoded = ScfIsBase64Encoded

    @property
    def ScfIsIntegratedResponse(self):
        return self._ScfIsIntegratedResponse

    @ScfIsIntegratedResponse.setter
    def ScfIsIntegratedResponse(self, ScfIsIntegratedResponse):
        self._ScfIsIntegratedResponse = ScfIsIntegratedResponse


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._SourceID = params.get("SourceID")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = KongTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._SourceType = params.get("SourceType")
        self._ScfType = params.get("ScfType")
        self._ScfNamespace = params.get("ScfNamespace")
        self._ScfLambdaName = params.get("ScfLambdaName")
        self._ScfLambdaQualifier = params.get("ScfLambdaQualifier")
        self._SlowStart = params.get("SlowStart")
        self._Algorithm = params.get("Algorithm")
        self._AutoScalingGroupID = params.get("AutoScalingGroupID")
        self._AutoScalingCvmPort = params.get("AutoScalingCvmPort")
        self._AutoScalingTatCmdStatus = params.get("AutoScalingTatCmdStatus")
        self._AutoScalingHookStatus = params.get("AutoScalingHookStatus")
        self._SourceName = params.get("SourceName")
        self._RealSourceType = params.get("RealSourceType")
        self._HealthStatus = params.get("HealthStatus")
        self._ScfCamAuthEnable = params.get("ScfCamAuthEnable")
        self._ScfIsBase64Encoded = params.get("ScfIsBase64Encoded")
        self._ScfIsIntegratedResponse = params.get("ScfIsIntegratedResponse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongUpstreamList(AbstractModel):
    """kong后端upstream列表

    """

    def __init__(self):
        r"""
        :param _UpstreamList: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamList: list of KongUpstreamPreview
        """
        self._UpstreamList = None

    @property
    def UpstreamList(self):
        return self._UpstreamList

    @UpstreamList.setter
    def UpstreamList(self, UpstreamList):
        self._UpstreamList = UpstreamList


    def _deserialize(self, params):
        if params.get("UpstreamList") is not None:
            self._UpstreamList = []
            for item in params.get("UpstreamList"):
                obj = KongUpstreamPreview()
                obj._deserialize(item)
                self._UpstreamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KongUpstreamPreview(AbstractModel):
    """云原生网关Upstream信息

    """

    def __init__(self):
        r"""
        :param _ID: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ID: str
        :param _Name: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Target: 后端配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Target: list of KongTarget
        """
        self._ID = None
        self._Name = None
        self._Target = None

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target


    def _deserialize(self, params):
        self._ID = params.get("ID")
        self._Name = params.get("Name")
        if params.get("Target") is not None:
            self._Target = []
            for item in params.get("Target"):
                obj = KongTarget()
                obj._deserialize(item)
                self._Target.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LimitRule(AbstractModel):
    """参数限流的规则

    """

    def __init__(self):
        r"""
        :param _Filters: 请求匹配条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of RuleFilter
        :param _LimitBy: 参数限流依据组合
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitBy: list of KeyValue
        :param _QpsThresholds: 限流阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type QpsThresholds: list of QpsThreshold
        :param _AccurateQpsThresholds: 精确限流阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type AccurateQpsThresholds: list of AccurateQpsThreshold
        """
        self._Filters = None
        self._LimitBy = None
        self._QpsThresholds = None
        self._AccurateQpsThresholds = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def LimitBy(self):
        return self._LimitBy

    @LimitBy.setter
    def LimitBy(self, LimitBy):
        self._LimitBy = LimitBy

    @property
    def QpsThresholds(self):
        return self._QpsThresholds

    @QpsThresholds.setter
    def QpsThresholds(self, QpsThresholds):
        self._QpsThresholds = QpsThresholds

    @property
    def AccurateQpsThresholds(self):
        return self._AccurateQpsThresholds

    @AccurateQpsThresholds.setter
    def AccurateQpsThresholds(self, AccurateQpsThresholds):
        self._AccurateQpsThresholds = AccurateQpsThresholds


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RuleFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("LimitBy") is not None:
            self._LimitBy = []
            for item in params.get("LimitBy"):
                obj = KeyValue()
                obj._deserialize(item)
                self._LimitBy.append(obj)
        if params.get("QpsThresholds") is not None:
            self._QpsThresholds = []
            for item in params.get("QpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._QpsThresholds.append(obj)
        if params.get("AccurateQpsThresholds") is not None:
            self._AccurateQpsThresholds = []
            for item in params.get("AccurateQpsThresholds"):
                obj = AccurateQpsThreshold()
                obj._deserialize(item)
                self._AccurateQpsThresholds.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayResult(AbstractModel):
    """获取云原生API网关实例列表响应结果。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数。
        :type TotalCount: int
        :param _GatewayList: 云原生API网关实例列表。
        :type GatewayList: list of DescribeCloudNativeAPIGatewayResult
        """
        self._TotalCount = None
        self._GatewayList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GatewayList(self):
        return self._GatewayList

    @GatewayList.setter
    def GatewayList(self, GatewayList):
        self._GatewayList = GatewayList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GatewayList") is not None:
            self._GatewayList = []
            for item in params.get("GatewayList"):
                obj = DescribeCloudNativeAPIGatewayResult()
                obj._deserialize(item)
                self._GatewayList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayStrategyBindingGroupInfoResult(AbstractModel):
    """获取云原生API网关实例策略绑定网关分组列表响应结果。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _GroupInfos: 云原生API网关实例策略绑定网关分组列表
        :type GroupInfos: list of CloudNativeAPIGatewayStrategyBindingGroupInfo
        """
        self._TotalCount = None
        self._GroupInfos = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GroupInfos(self):
        return self._GroupInfos

    @GroupInfos.setter
    def GroupInfos(self, GroupInfos):
        self._GroupInfos = GroupInfos


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GroupInfos") is not None:
            self._GroupInfos = []
            for item in params.get("GroupInfos"):
                obj = CloudNativeAPIGatewayStrategyBindingGroupInfo()
                obj._deserialize(item)
                self._GroupInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCloudNativeAPIGatewayStrategyResult(AbstractModel):
    """获取云原生API网关实例策略响应结果。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数。
        :type TotalCount: int
        :param _StrategyList: 云原生API网关实例策略列表。
        :type StrategyList: list of CloudNativeAPIGatewayStrategy
        """
        self._TotalCount = None
        self._StrategyList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StrategyList(self):
        return self._StrategyList

    @StrategyList.setter
    def StrategyList(self, StrategyList):
        self._StrategyList = StrategyList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StrategyList") is not None:
            self._StrategyList = []
            for item in params.get("StrategyList"):
                obj = CloudNativeAPIGatewayStrategy()
                obj._deserialize(item)
                self._StrategyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListFilter(AbstractModel):
    """列表过滤条件，模糊匹配

    """

    def __init__(self):
        r"""
        :param _Key: 过滤字段
        :type Key: str
        :param _Value: 过滤值
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
        


class Metadata(AbstractModel):
    """元数据信息

    """

    def __init__(self):
        r"""
        :param _Key: 元数据键名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: 元数据键值。不填则默认为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
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
        


class ModifyAutoScalerResourceStrategyRequest(AbstractModel):
    """ModifyAutoScalerResourceStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        :param _StrategyName: 策略名称
        :type StrategyName: str
        :param _Description: 策略描述
        :type Description: str
        :param _Config: 指标伸缩配置
        :type Config: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyAutoScalerConfig`
        :param _CronScalerConfig: 定时伸缩配置
        :type CronScalerConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        :param _MaxReplicas: 最大节点数
        :type MaxReplicas: int
        :param _CronConfig: 指标伸缩配置
        :type CronConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategyCronScalerConfig`
        """
        self._GatewayId = None
        self._StrategyId = None
        self._StrategyName = None
        self._Description = None
        self._Config = None
        self._CronScalerConfig = None
        self._MaxReplicas = None
        self._CronConfig = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CronScalerConfig(self):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        return self._CronScalerConfig

    @CronScalerConfig.setter
    def CronScalerConfig(self, CronScalerConfig):
        warnings.warn("parameter `CronScalerConfig` is deprecated", DeprecationWarning) 

        self._CronScalerConfig = CronScalerConfig

    @property
    def MaxReplicas(self):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        return self._MaxReplicas

    @MaxReplicas.setter
    def MaxReplicas(self, MaxReplicas):
        warnings.warn("parameter `MaxReplicas` is deprecated", DeprecationWarning) 

        self._MaxReplicas = MaxReplicas

    @property
    def CronConfig(self):
        return self._CronConfig

    @CronConfig.setter
    def CronConfig(self, CronConfig):
        self._CronConfig = CronConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._Description = params.get("Description")
        if params.get("Config") is not None:
            self._Config = CloudNativeAPIGatewayStrategyAutoScalerConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("CronScalerConfig") is not None:
            self._CronScalerConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronScalerConfig._deserialize(params.get("CronScalerConfig"))
        self._MaxReplicas = params.get("MaxReplicas")
        if params.get("CronConfig") is not None:
            self._CronConfig = CloudNativeAPIGatewayStrategyCronScalerConfig()
            self._CronConfig._deserialize(params.get("CronConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAutoScalerResourceStrategyResponse(AbstractModel):
    """ModifyAutoScalerResourceStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyCloudNativeAPIGatewayCanaryRuleRequest(AbstractModel):
    """ModifyCloudNativeAPIGatewayCanaryRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关 ID
        :type GatewayId: str
        :param _ServiceId: 服务 ID
        :type ServiceId: str
        :param _Priority: 优先级，同一个服务的灰度规则优先级是唯一的
        :type Priority: int
        :param _CanaryRule: 灰度规则配置
        :type CanaryRule: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayCanaryRule`
        """
        self._GatewayId = None
        self._ServiceId = None
        self._Priority = None
        self._CanaryRule = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def CanaryRule(self):
        return self._CanaryRule

    @CanaryRule.setter
    def CanaryRule(self, CanaryRule):
        self._CanaryRule = CanaryRule


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceId = params.get("ServiceId")
        self._Priority = params.get("Priority")
        if params.get("CanaryRule") is not None:
            self._CanaryRule = CloudNativeAPIGatewayCanaryRule()
            self._CanaryRule._deserialize(params.get("CanaryRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayCanaryRuleResponse(AbstractModel):
    """ModifyCloudNativeAPIGatewayCanaryRule返回参数结构体

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


class ModifyCloudNativeAPIGatewayCertificateRequest(AbstractModel):
    """ModifyCloudNativeAPIGatewayCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Id: 证书id
        :type Id: str
        :param _Name: 证书名称，即将废弃
        :type Name: str
        :param _Key: 证书私钥，CertSource为native时必填。
        :type Key: str
        :param _Crt: 证书pem格式，CertSource为native时必填。
        :type Crt: str
        :param _BindDomains: 绑定的域名，即将废弃
        :type BindDomains: list of str
        :param _CertId: ssl平台证书 Id，CertSource为ssl时必填。
        :type CertId: str
        :param _CertSource: 证书来源
- ssl (ssl平台证书)，默认值
- native (kong自定义证书) 

        :type CertSource: str
        """
        self._GatewayId = None
        self._Id = None
        self._Name = None
        self._Key = None
        self._Crt = None
        self._BindDomains = None
        self._CertId = None
        self._CertSource = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        warnings.warn("parameter `Name` is deprecated", DeprecationWarning) 

        return self._Name

    @Name.setter
    def Name(self, Name):
        warnings.warn("parameter `Name` is deprecated", DeprecationWarning) 

        self._Name = Name

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Crt(self):
        return self._Crt

    @Crt.setter
    def Crt(self, Crt):
        self._Crt = Crt

    @property
    def BindDomains(self):
        warnings.warn("parameter `BindDomains` is deprecated", DeprecationWarning) 

        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        warnings.warn("parameter `BindDomains` is deprecated", DeprecationWarning) 

        self._BindDomains = BindDomains

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertSource(self):
        return self._CertSource

    @CertSource.setter
    def CertSource(self, CertSource):
        self._CertSource = CertSource


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Key = params.get("Key")
        self._Crt = params.get("Crt")
        self._BindDomains = params.get("BindDomains")
        self._CertId = params.get("CertId")
        self._CertSource = params.get("CertSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayCertificateResponse(AbstractModel):
    """ModifyCloudNativeAPIGatewayCertificate返回参数结构体

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


class ModifyCloudNativeAPIGatewayRequest(AbstractModel):
    """ModifyCloudNativeAPIGateway请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _Name: 云原生API网关名字, 最多支持60个字符。
        :type Name: str
        :param _Description: 云原生API网关描述信息, 最多支持120个字符。
        :type Description: str
        :param _EnableCls: 是否开启 CLS 日志。暂时取值只能是 true，即只能从关闭状态变成开启状态。
        :type EnableCls: bool
        :param _InternetPayMode: 公网计费模式。可选取值 BANDWIDTH | TRAFFIC ，表示按带宽和按流量计费。
        :type InternetPayMode: str
        """
        self._GatewayId = None
        self._Name = None
        self._Description = None
        self._EnableCls = None
        self._InternetPayMode = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnableCls(self):
        return self._EnableCls

    @EnableCls.setter
    def EnableCls(self, EnableCls):
        self._EnableCls = EnableCls

    @property
    def InternetPayMode(self):
        return self._InternetPayMode

    @InternetPayMode.setter
    def InternetPayMode(self, InternetPayMode):
        self._InternetPayMode = InternetPayMode


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._EnableCls = params.get("EnableCls")
        self._InternetPayMode = params.get("InternetPayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayResponse(AbstractModel):
    """ModifyCloudNativeAPIGateway返回参数结构体

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


class ModifyCloudNativeAPIGatewayRouteRateLimitRequest(AbstractModel):
    """ModifyCloudNativeAPIGatewayRouteRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Id: 路由id，或路由名称。
不支持“未命名”
        :type Id: str
        :param _LimitDetail: 限流配置
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Id = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def LimitDetail(self):
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayRouteRateLimitResponse(AbstractModel):
    """ModifyCloudNativeAPIGatewayRouteRateLimit返回参数结构体

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


class ModifyCloudNativeAPIGatewayRouteRequest(AbstractModel):
    """ModifyCloudNativeAPIGatewayRoute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _ServiceID: 所属服务的ID
        :type ServiceID: str
        :param _RouteID: 路由的ID，实例级别唯一
        :type RouteID: str
        :param _RouteName: 路由的名字，实例级别唯一，可以不提供
        :type RouteName: str
        :param _Methods: 路由的方法，其中方法可选值：
- GET
- POST
- DELETE
- PUT
- OPTIONS
- PATCH
- HEAD
- ANY
- TRACE
- COPY
- MOVE
- PROPFIND
- PROPPATCH
- MKCOL
- LOCK
- UNLOCK
        :type Methods: list of str
        :param _Hosts: 路由的域名
        :type Hosts: list of str
        :param _Paths: 路由的路径
        :type Paths: list of str
        :param _Protocols: 路由的协议，可选
- https
- http
        :type Protocols: list of str
        :param _PreserveHost: 转发到后端时是否保留Host
        :type PreserveHost: bool
        :param _HttpsRedirectStatusCode: https重定向状态码
        :type HttpsRedirectStatusCode: int
        :param _StripPath: 转发到后端时是否StripPath
        :type StripPath: bool
        :param _ForceHttps: 是否开启强制HTTPS
        :type ForceHttps: bool
        :param _DestinationPorts: 四层匹配的目的端口	
        :type DestinationPorts: list of int non-negative
        :param _Headers: 路由的Headers
        :type Headers: list of KVMapping
        """
        self._GatewayId = None
        self._ServiceID = None
        self._RouteID = None
        self._RouteName = None
        self._Methods = None
        self._Hosts = None
        self._Paths = None
        self._Protocols = None
        self._PreserveHost = None
        self._HttpsRedirectStatusCode = None
        self._StripPath = None
        self._ForceHttps = None
        self._DestinationPorts = None
        self._Headers = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceID(self):
        return self._ServiceID

    @ServiceID.setter
    def ServiceID(self, ServiceID):
        self._ServiceID = ServiceID

    @property
    def RouteID(self):
        return self._RouteID

    @RouteID.setter
    def RouteID(self, RouteID):
        self._RouteID = RouteID

    @property
    def RouteName(self):
        return self._RouteName

    @RouteName.setter
    def RouteName(self, RouteName):
        self._RouteName = RouteName

    @property
    def Methods(self):
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Protocols(self):
        return self._Protocols

    @Protocols.setter
    def Protocols(self, Protocols):
        self._Protocols = Protocols

    @property
    def PreserveHost(self):
        return self._PreserveHost

    @PreserveHost.setter
    def PreserveHost(self, PreserveHost):
        self._PreserveHost = PreserveHost

    @property
    def HttpsRedirectStatusCode(self):
        return self._HttpsRedirectStatusCode

    @HttpsRedirectStatusCode.setter
    def HttpsRedirectStatusCode(self, HttpsRedirectStatusCode):
        self._HttpsRedirectStatusCode = HttpsRedirectStatusCode

    @property
    def StripPath(self):
        return self._StripPath

    @StripPath.setter
    def StripPath(self, StripPath):
        self._StripPath = StripPath

    @property
    def ForceHttps(self):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
        warnings.warn("parameter `ForceHttps` is deprecated", DeprecationWarning) 

        self._ForceHttps = ForceHttps

    @property
    def DestinationPorts(self):
        return self._DestinationPorts

    @DestinationPorts.setter
    def DestinationPorts(self, DestinationPorts):
        self._DestinationPorts = DestinationPorts

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceID = params.get("ServiceID")
        self._RouteID = params.get("RouteID")
        self._RouteName = params.get("RouteName")
        self._Methods = params.get("Methods")
        self._Hosts = params.get("Hosts")
        self._Paths = params.get("Paths")
        self._Protocols = params.get("Protocols")
        self._PreserveHost = params.get("PreserveHost")
        self._HttpsRedirectStatusCode = params.get("HttpsRedirectStatusCode")
        self._StripPath = params.get("StripPath")
        self._ForceHttps = params.get("ForceHttps")
        self._DestinationPorts = params.get("DestinationPorts")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayRouteResponse(AbstractModel):
    """ModifyCloudNativeAPIGatewayRoute返回参数结构体

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


class ModifyCloudNativeAPIGatewayServiceRateLimitRequest(AbstractModel):
    """ModifyCloudNativeAPIGatewayServiceRateLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 服务名称，或服务ID
        :type Name: str
        :param _LimitDetail: 限流配置
        :type LimitDetail: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayRateLimitDetail`
        """
        self._GatewayId = None
        self._Name = None
        self._LimitDetail = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def LimitDetail(self):
        return self._LimitDetail

    @LimitDetail.setter
    def LimitDetail(self, LimitDetail):
        self._LimitDetail = LimitDetail


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("LimitDetail") is not None:
            self._LimitDetail = CloudNativeAPIGatewayRateLimitDetail()
            self._LimitDetail._deserialize(params.get("LimitDetail"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayServiceRateLimitResponse(AbstractModel):
    """ModifyCloudNativeAPIGatewayServiceRateLimit返回参数结构体

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


class ModifyCloudNativeAPIGatewayServiceRequest(AbstractModel):
    """ModifyCloudNativeAPIGatewayService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 服务名称
        :type Name: str
        :param _Protocol: 请求协议： 
- https 
- http 
- tcp 
- udp
        :type Protocol: str
        :param _Path: 请求路径
        :type Path: str
        :param _Timeout: 超时时间，单位ms
        :type Timeout: int
        :param _Retries: 重试次数
        :type Retries: int
        :param _UpstreamType: 服务类型: 
- Kubernetes 
- Registry
- IPList
- HostIP
- Scf	
        :type UpstreamType: str
        :param _UpstreamInfo: 服务配置
        :type UpstreamInfo: :class:`tencentcloud.tse.v20201207.models.KongUpstreamInfo`
        :param _ID: 服务ID
        :type ID: str
        """
        self._GatewayId = None
        self._Name = None
        self._Protocol = None
        self._Path = None
        self._Timeout = None
        self._Retries = None
        self._UpstreamType = None
        self._UpstreamInfo = None
        self._ID = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Timeout(self):
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def UpstreamInfo(self):
        return self._UpstreamInfo

    @UpstreamInfo.setter
    def UpstreamInfo(self, UpstreamInfo):
        self._UpstreamInfo = UpstreamInfo

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        self._Protocol = params.get("Protocol")
        self._Path = params.get("Path")
        self._Timeout = params.get("Timeout")
        self._Retries = params.get("Retries")
        self._UpstreamType = params.get("UpstreamType")
        if params.get("UpstreamInfo") is not None:
            self._UpstreamInfo = KongUpstreamInfo()
            self._UpstreamInfo._deserialize(params.get("UpstreamInfo"))
        self._ID = params.get("ID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCloudNativeAPIGatewayServiceResponse(AbstractModel):
    """ModifyCloudNativeAPIGatewayService返回参数结构体

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


class ModifyConfigFileGroupRequest(AbstractModel):
    """ModifyConfigFileGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id
        :type InstanceId: str
        :param _ConfigFileGroup: 配置文件组
        :type ConfigFileGroup: :class:`tencentcloud.tse.v20201207.models.ConfigFileGroup`
        """
        self._InstanceId = None
        self._ConfigFileGroup = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFileGroup(self):
        return self._ConfigFileGroup

    @ConfigFileGroup.setter
    def ConfigFileGroup(self, ConfigFileGroup):
        self._ConfigFileGroup = ConfigFileGroup


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFileGroup") is not None:
            self._ConfigFileGroup = ConfigFileGroup()
            self._ConfigFileGroup._deserialize(params.get("ConfigFileGroup"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigFileGroupResponse(AbstractModel):
    """ModifyConfigFileGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyConfigFilesRequest(AbstractModel):
    """ModifyConfigFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: ins-df344df5	
        :type InstanceId: str
        :param _ConfigFile: 配置文件列表
        :type ConfigFile: :class:`tencentcloud.tse.v20201207.models.ConfigFile`
        """
        self._InstanceId = None
        self._ConfigFile = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFile(self):
        return self._ConfigFile

    @ConfigFile.setter
    def ConfigFile(self, ConfigFile):
        self._ConfigFile = ConfigFile


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFile") is not None:
            self._ConfigFile = ConfigFile()
            self._ConfigFile._deserialize(params.get("ConfigFile"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigFilesResponse(AbstractModel):
    """ModifyConfigFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyConsoleNetworkRequest(AbstractModel):
    """ModifyConsoleNetwork请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _NetworkType: 网络类型：
- Open 公网
- Internal 内网（暂不支持）
        :type NetworkType: str
        :param _Operate: 开启Konga网络，不填时默认为Open
- Open，开启
- Close，关闭
        :type Operate: str
        :param _AccessControl: 访问控制策略
        :type AccessControl: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        self._GatewayId = None
        self._NetworkType = None
        self._Operate = None
        self._AccessControl = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def Operate(self):
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate

    @property
    def AccessControl(self):
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._NetworkType = params.get("NetworkType")
        self._Operate = params.get("Operate")
        if params.get("AccessControl") is not None:
            self._AccessControl = NetworkAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConsoleNetworkResponse(AbstractModel):
    """ModifyConsoleNetwork返回参数结构体

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


class ModifyGovernanceAliasRequest(AbstractModel):
    """ModifyGovernanceAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _Alias: 服务别名
        :type Alias: str
        :param _AliasNamespace: 服务别名命名空间
        :type AliasNamespace: str
        :param _Service: 服务别名所指向的服务名
        :type Service: str
        :param _Namespace: 服务别名所指向的命名空间
        :type Namespace: str
        :param _Comment: 服务别名描述
        :type Comment: str
        """
        self._InstanceId = None
        self._Alias = None
        self._AliasNamespace = None
        self._Service = None
        self._Namespace = None
        self._Comment = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def AliasNamespace(self):
        return self._AliasNamespace

    @AliasNamespace.setter
    def AliasNamespace(self, AliasNamespace):
        self._AliasNamespace = AliasNamespace

    @property
    def Service(self):
        return self._Service

    @Service.setter
    def Service(self, Service):
        self._Service = Service

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def Comment(self):
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Alias = params.get("Alias")
        self._AliasNamespace = params.get("AliasNamespace")
        self._Service = params.get("Service")
        self._Namespace = params.get("Namespace")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGovernanceAliasResponse(AbstractModel):
    """ModifyGovernanceAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyGovernanceInstancesRequest(AbstractModel):
    """ModifyGovernanceInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceInstances: 服务实例信息。
        :type GovernanceInstances: list of GovernanceInstanceUpdate
        """
        self._InstanceId = None
        self._GovernanceInstances = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceInstances(self):
        return self._GovernanceInstances

    @GovernanceInstances.setter
    def GovernanceInstances(self, GovernanceInstances):
        self._GovernanceInstances = GovernanceInstances


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceInstances") is not None:
            self._GovernanceInstances = []
            for item in params.get("GovernanceInstances"):
                obj = GovernanceInstanceUpdate()
                obj._deserialize(item)
                self._GovernanceInstances.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGovernanceInstancesResponse(AbstractModel):
    """ModifyGovernanceInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyGovernanceNamespacesRequest(AbstractModel):
    """ModifyGovernanceNamespaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse实例id。
        :type InstanceId: str
        :param _GovernanceNamespaces: 命名空间信息。
        :type GovernanceNamespaces: list of GovernanceNamespaceInput
        """
        self._InstanceId = None
        self._GovernanceNamespaces = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceNamespaces(self):
        return self._GovernanceNamespaces

    @GovernanceNamespaces.setter
    def GovernanceNamespaces(self, GovernanceNamespaces):
        self._GovernanceNamespaces = GovernanceNamespaces


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceNamespaces") is not None:
            self._GovernanceNamespaces = []
            for item in params.get("GovernanceNamespaces"):
                obj = GovernanceNamespaceInput()
                obj._deserialize(item)
                self._GovernanceNamespaces.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGovernanceNamespacesResponse(AbstractModel):
    """ModifyGovernanceNamespaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyGovernanceServicesRequest(AbstractModel):
    """ModifyGovernanceServices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: tse 实例 id。
        :type InstanceId: str
        :param _GovernanceServices: 服务信息。
        :type GovernanceServices: list of GovernanceServiceInput
        """
        self._InstanceId = None
        self._GovernanceServices = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def GovernanceServices(self):
        return self._GovernanceServices

    @GovernanceServices.setter
    def GovernanceServices(self, GovernanceServices):
        self._GovernanceServices = GovernanceServices


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("GovernanceServices") is not None:
            self._GovernanceServices = []
            for item in params.get("GovernanceServices"):
                obj = GovernanceServiceInput()
                obj._deserialize(item)
                self._GovernanceServices.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGovernanceServicesResponse(AbstractModel):
    """ModifyGovernanceServices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyNativeGatewayServerGroupRequest(AbstractModel):
    """ModifyNativeGatewayServerGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 网关分组 id
        :type GroupId: str
        :param _Name: 云原生API网关名字, 最多支持60个字符。
        :type Name: str
        :param _Description: 云原生API网关描述信息, 最多支持120个字符。
        :type Description: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._Name = None
        self._Description = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNativeGatewayServerGroupResponse(AbstractModel):
    """ModifyNativeGatewayServerGroup返回参数结构体

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


class ModifyNetworkAccessStrategyRequest(AbstractModel):
    """ModifyNetworkAccessStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 分组id
        :type GroupId: str
        :param _NetworkType: 网络类型： 
- Open 公网
- Internal 内网	（暂不支持）
        :type NetworkType: str
        :param _Vip: ip地址
        :type Vip: str
        :param _AccessControl: 访问控制策略
        :type AccessControl: :class:`tencentcloud.tse.v20201207.models.NetworkAccessControl`
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkType = None
        self._Vip = None
        self._AccessControl = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def AccessControl(self):
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkType = params.get("NetworkType")
        self._Vip = params.get("Vip")
        if params.get("AccessControl") is not None:
            self._AccessControl = NetworkAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkAccessStrategyResponse(AbstractModel):
    """ModifyNetworkAccessStrategy返回参数结构体

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


class ModifyNetworkBasicInfoRequest(AbstractModel):
    """ModifyNetworkBasicInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
        :type GatewayId: str
        :param _GroupId: 分组id
        :type GroupId: str
        :param _NetworkType: 网络类型：
- Open 公网ipv4
- Open-IPv6 公网ipv6
- Internal 内网
        :type NetworkType: str
        :param _Vip: ip地址
        :type Vip: str
        :param _InternetMaxBandwidthOut: 公网出流量带宽[1,2048]Mbps
        :type InternetMaxBandwidthOut: int
        :param _Description: 负载均衡描述
        :type Description: str
        """
        self._GatewayId = None
        self._GroupId = None
        self._NetworkType = None
        self._Vip = None
        self._InternetMaxBandwidthOut = None
        self._Description = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NetworkType(self):
        return self._NetworkType

    @NetworkType.setter
    def NetworkType(self, NetworkType):
        self._NetworkType = NetworkType

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        self._NetworkType = params.get("NetworkType")
        self._Vip = params.get("Vip")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkBasicInfoResponse(AbstractModel):
    """ModifyNetworkBasicInfo返回参数结构体

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


class ModifyUpstreamNodeStatusRequest(AbstractModel):
    """ModifyUpstreamNodeStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _Host: 访问IP地址或域名
        :type Host: str
        :param _Port: 访问端口
        :type Port: int
        :param _Status: HEALTHY或UNHEALTHY
        :type Status: str
        """
        self._GatewayId = None
        self._ServiceName = None
        self._Host = None
        self._Port = None
        self._Status = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._ServiceName = params.get("ServiceName")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUpstreamNodeStatusResponse(AbstractModel):
    """ModifyUpstreamNodeStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class NacosReplica(AbstractModel):
    """Nacos副本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Role: 角色
        :type Role: str
        :param _Status: 状态
        :type Status: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Zone: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _VpcId: VPC ID	
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        """
        self._Name = None
        self._Role = None
        self._Status = None
        self._SubnetId = None
        self._Zone = None
        self._ZoneId = None
        self._VpcId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NacosServerInterface(AbstractModel):
    """nacos服务端接口列表，用于云监控

    """

    def __init__(self):
        r"""
        :param _Interface: 接口名
注意：此字段可能返回 null，表示取不到有效值。
        :type Interface: str
        """
        self._Interface = None

    @property
    def Interface(self):
        return self._Interface

    @Interface.setter
    def Interface(self, Interface):
        self._Interface = Interface


    def _deserialize(self, params):
        self._Interface = params.get("Interface")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeGatewayServerGroup(AbstractModel):
    """云原生网关分组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 云原生网关分组唯一id
        :type GroupId: str
        :param _Name: 分组名
        :type Name: str
        :param _Description: 描述信息
        :type Description: str
        :param _NodeConfig: 节点规格、节点数信息
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        :param _Status: 网关分组状态。
        :type Status: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _IsFirstGroup: 是否是默认分组。
0：否。
1：是。
        :type IsFirstGroup: int
        :param _BindingStrategy: 关联策略信息
注意：此字段可能返回 null，表示取不到有效值。
        :type BindingStrategy: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayStrategy`
        :param _GatewayId: 网关实例 id
注意：此字段可能返回 null，表示取不到有效值。
        :type GatewayId: str
        :param _InternetMaxBandwidthOut: 带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        :param _SubnetIds: 子网id
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: str
        :param _DefaultWeight: 分组默认权重
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultWeight: int
        """
        self._GroupId = None
        self._Name = None
        self._Description = None
        self._NodeConfig = None
        self._Status = None
        self._CreateTime = None
        self._IsFirstGroup = None
        self._BindingStrategy = None
        self._GatewayId = None
        self._InternetMaxBandwidthOut = None
        self._ModifyTime = None
        self._SubnetIds = None
        self._DefaultWeight = None

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NodeConfig(self):
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def IsFirstGroup(self):
        return self._IsFirstGroup

    @IsFirstGroup.setter
    def IsFirstGroup(self, IsFirstGroup):
        self._IsFirstGroup = IsFirstGroup

    @property
    def BindingStrategy(self):
        return self._BindingStrategy

    @BindingStrategy.setter
    def BindingStrategy(self, BindingStrategy):
        self._BindingStrategy = BindingStrategy

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def ModifyTime(self):
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def DefaultWeight(self):
        return self._DefaultWeight

    @DefaultWeight.setter
    def DefaultWeight(self, DefaultWeight):
        self._DefaultWeight = DefaultWeight


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._IsFirstGroup = params.get("IsFirstGroup")
        if params.get("BindingStrategy") is not None:
            self._BindingStrategy = CloudNativeAPIGatewayStrategy()
            self._BindingStrategy._deserialize(params.get("BindingStrategy"))
        self._GatewayId = params.get("GatewayId")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._ModifyTime = params.get("ModifyTime")
        self._SubnetIds = params.get("SubnetIds")
        self._DefaultWeight = params.get("DefaultWeight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NativeGatewayServerGroups(AbstractModel):
    """网关分组列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _GatewayGroupList: 分组信息数组。
        :type GatewayGroupList: list of NativeGatewayServerGroup
        """
        self._TotalCount = None
        self._GatewayGroupList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def GatewayGroupList(self):
        return self._GatewayGroupList

    @GatewayGroupList.setter
    def GatewayGroupList(self, GatewayGroupList):
        self._GatewayGroupList = GatewayGroupList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("GatewayGroupList") is not None:
            self._GatewayGroupList = []
            for item in params.get("GatewayGroupList"):
                obj = NativeGatewayServerGroup()
                obj._deserialize(item)
                self._GatewayGroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAccessControl(AbstractModel):
    """网络访问策略

    """

    def __init__(self):
        r"""
        :param _Mode: 访问模式：Whitelist|Blacklist
        :type Mode: str
        :param _CidrWhiteList: 白名单列表
        :type CidrWhiteList: list of str
        :param _CidrBlackList: 黑名单列表
        :type CidrBlackList: list of str
        """
        self._Mode = None
        self._CidrWhiteList = None
        self._CidrBlackList = None

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def CidrWhiteList(self):
        return self._CidrWhiteList

    @CidrWhiteList.setter
    def CidrWhiteList(self, CidrWhiteList):
        self._CidrWhiteList = CidrWhiteList

    @property
    def CidrBlackList(self):
        return self._CidrBlackList

    @CidrBlackList.setter
    def CidrBlackList(self, CidrBlackList):
        self._CidrBlackList = CidrBlackList


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._CidrWhiteList = params.get("CidrWhiteList")
        self._CidrBlackList = params.get("CidrBlackList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWafProtectionRequest(AbstractModel):
    """OpenWafProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Type:  防护资源的类型。
- Global  实例
- Service  服务
- Route  路由
- Object  对象（接口暂不支持）
        :type Type: str
        :param _List: 当资源类型 Type 是 Service 或 Route 的时候，传入的服务或路由的列表
        :type List: list of str
        """
        self._GatewayId = None
        self._Type = None
        self._List = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Type = params.get("Type")
        self._List = params.get("List")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenWafProtectionResponse(AbstractModel):
    """OpenWafProtection返回参数结构体

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


class PolarisCLSTopicInfo(AbstractModel):
    """北极星日志主题信息

    """

    def __init__(self):
        r"""
        :param _LogSetId: 日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetId: str
        :param _LogSetName: 日志集名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetName: str
        :param _TopicId: 日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _TopicName: 日志主题名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicName: str
        """
        self._LogSetId = None
        self._LogSetName = None
        self._TopicId = None
        self._TopicName = None

    @property
    def LogSetId(self):
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogSetName(self):
        return self._LogSetName

    @LogSetName.setter
    def LogSetName(self, LogSetName):
        self._LogSetName = LogSetName

    @property
    def TopicId(self):
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName


    def _deserialize(self, params):
        self._LogSetId = params.get("LogSetId")
        self._LogSetName = params.get("LogSetName")
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolarisLimiterAddress(AbstractModel):
    """查询Limiter的接入地址

    """

    def __init__(self):
        r"""
        :param _IntranetAddress: VPC接入IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetAddress: str
        """
        self._IntranetAddress = None

    @property
    def IntranetAddress(self):
        return self._IntranetAddress

    @IntranetAddress.setter
    def IntranetAddress(self, IntranetAddress):
        self._IntranetAddress = IntranetAddress


    def _deserialize(self, params):
        self._IntranetAddress = params.get("IntranetAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicAddressConfig(AbstractModel):
    """公网地址信息

    """

    def __init__(self):
        r"""
        :param _Vip: 公网 ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param _InternetMaxBandwidthOut: 公网最大带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type InternetMaxBandwidthOut: int
        :param _GroupId: 公网所属分组 id
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param _GroupName: 公网所属分组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _NetworkId: 公网负载均衡 id
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkId: str
        """
        self._Vip = None
        self._InternetMaxBandwidthOut = None
        self._GroupId = None
        self._GroupName = None
        self._NetworkId = None

    @property
    def Vip(self):
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def NetworkId(self):
        return self._NetworkId

    @NetworkId.setter
    def NetworkId(self, NetworkId):
        self._NetworkId = NetworkId


    def _deserialize(self, params):
        self._Vip = params.get("Vip")
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._NetworkId = params.get("NetworkId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishConfigFilesRequest(AbstractModel):
    """PublishConfigFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _ConfigFileReleases: 配置文件发布
        :type ConfigFileReleases: :class:`tencentcloud.tse.v20201207.models.ConfigFileRelease`
        """
        self._InstanceId = None
        self._ConfigFileReleases = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConfigFileReleases(self):
        return self._ConfigFileReleases

    @ConfigFileReleases.setter
    def ConfigFileReleases(self, ConfigFileReleases):
        self._ConfigFileReleases = ConfigFileReleases


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConfigFileReleases") is not None:
            self._ConfigFileReleases = ConfigFileRelease()
            self._ConfigFileReleases._deserialize(params.get("ConfigFileReleases"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishConfigFilesResponse(AbstractModel):
    """PublishConfigFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 配置文件发布是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class QpsThreshold(AbstractModel):
    """云原生网关限流插件Qps阈值

    """

    def __init__(self):
        r"""
        :param _Unit: qps阈值控制维度,包含:second、minute、hour、day、month、year
        :type Unit: str
        :param _Max: 阈值
        :type Max: int
        """
        self._Unit = None
        self._Max = None

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Max(self):
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Unit = params.get("Unit")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RateLimitResponse(AbstractModel):
    """云原生网关限流插件自定义响应

    """

    def __init__(self):
        r"""
        :param _Body: 自定义响应体
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        :param _Headers: Headers
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of KVMapping
        :param _HttpStatus: http状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpStatus: int
        """
        self._Body = None
        self._Headers = None
        self._HttpStatus = None

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Headers(self):
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def HttpStatus(self):
        return self._HttpStatus

    @HttpStatus.setter
    def HttpStatus(self, HttpStatus):
        self._HttpStatus = HttpStatus


    def _deserialize(self, params):
        self._Body = params.get("Body")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = KVMapping()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._HttpStatus = params.get("HttpStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseVersion(AbstractModel):
    """配置发布版本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Active: 是否生效
注意：此字段可能返回 null，表示取不到有效值。
        :type Active: bool
        """
        self._Name = None
        self._Active = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Active(self):
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Active = params.get("Active")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackConfigFileReleasesRequest(AbstractModel):
    """RollbackConfigFileReleases请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: TSE实例id
        :type InstanceId: str
        :param _RollbackConfigFileReleases: 回滚发布
        :type RollbackConfigFileReleases: list of ConfigFileRelease
        """
        self._InstanceId = None
        self._RollbackConfigFileReleases = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RollbackConfigFileReleases(self):
        return self._RollbackConfigFileReleases

    @RollbackConfigFileReleases.setter
    def RollbackConfigFileReleases(self, RollbackConfigFileReleases):
        self._RollbackConfigFileReleases = RollbackConfigFileReleases


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("RollbackConfigFileReleases") is not None:
            self._RollbackConfigFileReleases = []
            for item in params.get("RollbackConfigFileReleases"):
                obj = ConfigFileRelease()
                obj._deserialize(item)
                self._RollbackConfigFileReleases.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackConfigFileReleasesResponse(AbstractModel):
    """RollbackConfigFileReleases返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 回滚结果
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class RouteWafStatus(AbstractModel):
    """路由 WAF 状态

    """

    def __init__(self):
        r"""
        :param _Name: 路由的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Id: 路由的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Status:  路由是否开启 WAF 防护
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _Methods: 方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Methods: list of str
        :param _Paths: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Paths: list of str
        :param _Hosts: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Hosts: list of str
        :param _ServiceName: 路由对应服务的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ServiceId: 路由对应服务的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        """
        self._Name = None
        self._Id = None
        self._Status = None
        self._Methods = None
        self._Paths = None
        self._Hosts = None
        self._ServiceName = None
        self._ServiceId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Methods(self):
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def Hosts(self):
        return self._Hosts

    @Hosts.setter
    def Hosts(self, Hosts):
        self._Hosts = Hosts

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Status = params.get("Status")
        self._Methods = params.get("Methods")
        self._Paths = params.get("Paths")
        self._Hosts = params.get("Hosts")
        self._ServiceName = params.get("ServiceName")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilter(AbstractModel):
    """限流规则的Filter

    """

    def __init__(self):
        r"""
        :param _Key: 限流条件的Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Values: 限流条件的Values
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SREInstance(AbstractModel):
    """微服务注册引擎实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 名称
        :type Name: str
        :param _Edition: 版本号
        :type Edition: str
        :param _Status: 状态, 枚举值:creating/create_fail/running/updating/update_fail/restarting/restart_fail/destroying/destroy_fail
        :type Status: str
        :param _SpecId: 规格ID
        :type SpecId: str
        :param _Replica: 副本数
        :type Replica: int
        :param _Type: 类型
        :type Type: str
        :param _VpcId: Vpc iD
        :type VpcId: str
        :param _SubnetIds: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetIds: list of str
        :param _EnableStorage: 是否开启持久化存储
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableStorage: bool
        :param _StorageType: 数据存储方式
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _StorageCapacity: 云硬盘容量
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageCapacity: int
        :param _Paymode: 计费方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Paymode: str
        :param _EKSClusterID: EKS集群的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSClusterID: str
        :param _CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _EnvInfos: 环境配置信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvInfos: list of EnvInfo
        :param _EngineRegion: 引擎所在的区域
注意：此字段可能返回 null，表示取不到有效值。
        :type EngineRegion: str
        :param _EnableInternet: 注册引擎是否开启公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableInternet: bool
        :param _VpcInfos: 私有网络列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcInfos: list of VpcInfo
        :param _ServiceGovernanceInfos: 服务治理相关信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceGovernanceInfos: list of ServiceGovernanceInfo
        :param _Tags: 实例的标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of KVPair
        :param _EnableConsoleInternet: 引擎实例是否开启控制台公网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleInternet: bool
        :param _EnableConsoleIntranet: 引擎实例是否开启控制台内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableConsoleIntranet: bool
        :param _ConfigInfoVisible: 引擎实例是否展示参数配置页面
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigInfoVisible: bool
        :param _ConsoleDefaultPwd: 引擎实例控制台默认密码
注意：此字段可能返回 null，表示取不到有效值。
        :type ConsoleDefaultPwd: str
        :param _TradeType: 交易付费类型，0后付费/1预付费
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeType: int
        :param _AutoRenewFlag: 自动续费标记：0表示默认状态(用户未设置，即初始状态)， 1表示自动续费，2表示明确不自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param _CurDeadline: 预付费到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        :param _IsolateTime: 隔离开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type IsolateTime: str
        :param _RegionInfos: 实例地域相关的描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionInfos: list of DescribeInstanceRegionInfo
        :param _EKSType: 所在EKS环境，分为common和yunti
注意：此字段可能返回 null，表示取不到有效值。
        :type EKSType: str
        :param _FeatureVersion: 引擎的产品版本
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureVersion: str
        :param _EnableClientIntranet: 引擎实例是否开启客户端内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableClientIntranet: bool
        :param _StorageOption: 存储额外配置选项
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageOption: list of StorageOption
        :param _ZookeeperRegionInfo: Zookeeper的额外环境数据信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ZookeeperRegionInfo: :class:`tencentcloud.tse.v20201207.models.ZookeeperRegionInfo`
        :param _DeployMode: 部署架构
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: str
        """
        self._InstanceId = None
        self._Name = None
        self._Edition = None
        self._Status = None
        self._SpecId = None
        self._Replica = None
        self._Type = None
        self._VpcId = None
        self._SubnetIds = None
        self._EnableStorage = None
        self._StorageType = None
        self._StorageCapacity = None
        self._Paymode = None
        self._EKSClusterID = None
        self._CreateTime = None
        self._EnvInfos = None
        self._EngineRegion = None
        self._EnableInternet = None
        self._VpcInfos = None
        self._ServiceGovernanceInfos = None
        self._Tags = None
        self._EnableConsoleInternet = None
        self._EnableConsoleIntranet = None
        self._ConfigInfoVisible = None
        self._ConsoleDefaultPwd = None
        self._TradeType = None
        self._AutoRenewFlag = None
        self._CurDeadline = None
        self._IsolateTime = None
        self._RegionInfos = None
        self._EKSType = None
        self._FeatureVersion = None
        self._EnableClientIntranet = None
        self._StorageOption = None
        self._ZookeeperRegionInfo = None
        self._DeployMode = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Edition(self):
        return self._Edition

    @Edition.setter
    def Edition(self, Edition):
        self._Edition = Edition

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SpecId(self):
        return self._SpecId

    @SpecId.setter
    def SpecId(self, SpecId):
        self._SpecId = SpecId

    @property
    def Replica(self):
        return self._Replica

    @Replica.setter
    def Replica(self, Replica):
        self._Replica = Replica

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetIds(self):
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def EnableStorage(self):
        return self._EnableStorage

    @EnableStorage.setter
    def EnableStorage(self, EnableStorage):
        self._EnableStorage = EnableStorage

    @property
    def StorageType(self):
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def StorageCapacity(self):
        return self._StorageCapacity

    @StorageCapacity.setter
    def StorageCapacity(self, StorageCapacity):
        self._StorageCapacity = StorageCapacity

    @property
    def Paymode(self):
        return self._Paymode

    @Paymode.setter
    def Paymode(self, Paymode):
        self._Paymode = Paymode

    @property
    def EKSClusterID(self):
        return self._EKSClusterID

    @EKSClusterID.setter
    def EKSClusterID(self, EKSClusterID):
        self._EKSClusterID = EKSClusterID

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnvInfos(self):
        return self._EnvInfos

    @EnvInfos.setter
    def EnvInfos(self, EnvInfos):
        self._EnvInfos = EnvInfos

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def EnableInternet(self):
        return self._EnableInternet

    @EnableInternet.setter
    def EnableInternet(self, EnableInternet):
        self._EnableInternet = EnableInternet

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def ServiceGovernanceInfos(self):
        return self._ServiceGovernanceInfos

    @ServiceGovernanceInfos.setter
    def ServiceGovernanceInfos(self, ServiceGovernanceInfos):
        self._ServiceGovernanceInfos = ServiceGovernanceInfos

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def EnableConsoleInternet(self):
        return self._EnableConsoleInternet

    @EnableConsoleInternet.setter
    def EnableConsoleInternet(self, EnableConsoleInternet):
        self._EnableConsoleInternet = EnableConsoleInternet

    @property
    def EnableConsoleIntranet(self):
        return self._EnableConsoleIntranet

    @EnableConsoleIntranet.setter
    def EnableConsoleIntranet(self, EnableConsoleIntranet):
        self._EnableConsoleIntranet = EnableConsoleIntranet

    @property
    def ConfigInfoVisible(self):
        return self._ConfigInfoVisible

    @ConfigInfoVisible.setter
    def ConfigInfoVisible(self, ConfigInfoVisible):
        self._ConfigInfoVisible = ConfigInfoVisible

    @property
    def ConsoleDefaultPwd(self):
        return self._ConsoleDefaultPwd

    @ConsoleDefaultPwd.setter
    def ConsoleDefaultPwd(self, ConsoleDefaultPwd):
        self._ConsoleDefaultPwd = ConsoleDefaultPwd

    @property
    def TradeType(self):
        return self._TradeType

    @TradeType.setter
    def TradeType(self, TradeType):
        self._TradeType = TradeType

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline

    @property
    def IsolateTime(self):
        return self._IsolateTime

    @IsolateTime.setter
    def IsolateTime(self, IsolateTime):
        self._IsolateTime = IsolateTime

    @property
    def RegionInfos(self):
        return self._RegionInfos

    @RegionInfos.setter
    def RegionInfos(self, RegionInfos):
        self._RegionInfos = RegionInfos

    @property
    def EKSType(self):
        return self._EKSType

    @EKSType.setter
    def EKSType(self, EKSType):
        self._EKSType = EKSType

    @property
    def FeatureVersion(self):
        return self._FeatureVersion

    @FeatureVersion.setter
    def FeatureVersion(self, FeatureVersion):
        self._FeatureVersion = FeatureVersion

    @property
    def EnableClientIntranet(self):
        return self._EnableClientIntranet

    @EnableClientIntranet.setter
    def EnableClientIntranet(self, EnableClientIntranet):
        self._EnableClientIntranet = EnableClientIntranet

    @property
    def StorageOption(self):
        return self._StorageOption

    @StorageOption.setter
    def StorageOption(self, StorageOption):
        self._StorageOption = StorageOption

    @property
    def ZookeeperRegionInfo(self):
        return self._ZookeeperRegionInfo

    @ZookeeperRegionInfo.setter
    def ZookeeperRegionInfo(self, ZookeeperRegionInfo):
        self._ZookeeperRegionInfo = ZookeeperRegionInfo

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Edition = params.get("Edition")
        self._Status = params.get("Status")
        self._SpecId = params.get("SpecId")
        self._Replica = params.get("Replica")
        self._Type = params.get("Type")
        self._VpcId = params.get("VpcId")
        self._SubnetIds = params.get("SubnetIds")
        self._EnableStorage = params.get("EnableStorage")
        self._StorageType = params.get("StorageType")
        self._StorageCapacity = params.get("StorageCapacity")
        self._Paymode = params.get("Paymode")
        self._EKSClusterID = params.get("EKSClusterID")
        self._CreateTime = params.get("CreateTime")
        if params.get("EnvInfos") is not None:
            self._EnvInfos = []
            for item in params.get("EnvInfos"):
                obj = EnvInfo()
                obj._deserialize(item)
                self._EnvInfos.append(obj)
        self._EngineRegion = params.get("EngineRegion")
        self._EnableInternet = params.get("EnableInternet")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        if params.get("ServiceGovernanceInfos") is not None:
            self._ServiceGovernanceInfos = []
            for item in params.get("ServiceGovernanceInfos"):
                obj = ServiceGovernanceInfo()
                obj._deserialize(item)
                self._ServiceGovernanceInfos.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = KVPair()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._EnableConsoleInternet = params.get("EnableConsoleInternet")
        self._EnableConsoleIntranet = params.get("EnableConsoleIntranet")
        self._ConfigInfoVisible = params.get("ConfigInfoVisible")
        self._ConsoleDefaultPwd = params.get("ConsoleDefaultPwd")
        self._TradeType = params.get("TradeType")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        self._IsolateTime = params.get("IsolateTime")
        if params.get("RegionInfos") is not None:
            self._RegionInfos = []
            for item in params.get("RegionInfos"):
                obj = DescribeInstanceRegionInfo()
                obj._deserialize(item)
                self._RegionInfos.append(obj)
        self._EKSType = params.get("EKSType")
        self._FeatureVersion = params.get("FeatureVersion")
        self._EnableClientIntranet = params.get("EnableClientIntranet")
        if params.get("StorageOption") is not None:
            self._StorageOption = []
            for item in params.get("StorageOption"):
                obj = StorageOption()
                obj._deserialize(item)
                self._StorageOption.append(obj)
        if params.get("ZookeeperRegionInfo") is not None:
            self._ZookeeperRegionInfo = ZookeeperRegionInfo()
            self._ZookeeperRegionInfo._deserialize(params.get("ZookeeperRegionInfo"))
        self._DeployMode = params.get("DeployMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceGovernanceInfo(AbstractModel):
    """服务治理相关的信息

    """

    def __init__(self):
        r"""
        :param _EngineRegion: 引擎所在的地域
        :type EngineRegion: str
        :param _BoundK8SInfos: 服务治理引擎绑定的kubernetes集群信息
        :type BoundK8SInfos: list of BoundK8SInfo
        :param _VpcInfos: 服务治理引擎绑定的网络信息
        :type VpcInfos: list of VpcInfo
        :param _AuthOpen: 当前实例鉴权是否开启
        :type AuthOpen: bool
        :param _Features: 该实例支持的功能，鉴权就是 Auth
        :type Features: list of str
        :param _MainPassword: 主账户名默认为 polaris，该值为主账户的默认密码
        :type MainPassword: str
        :param _PgwVpcInfos: 服务治理pushgateway引擎绑定的网络信息
        :type PgwVpcInfos: list of VpcInfo
        :param _LimiterVpcInfos: 服务治理限流server引擎绑定的网络信息
        :type LimiterVpcInfos: list of VpcInfo
        :param _CLSTopics: 引擎关联CLS日志主题信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CLSTopics: list of PolarisCLSTopicInfo
        """
        self._EngineRegion = None
        self._BoundK8SInfos = None
        self._VpcInfos = None
        self._AuthOpen = None
        self._Features = None
        self._MainPassword = None
        self._PgwVpcInfos = None
        self._LimiterVpcInfos = None
        self._CLSTopics = None

    @property
    def EngineRegion(self):
        return self._EngineRegion

    @EngineRegion.setter
    def EngineRegion(self, EngineRegion):
        self._EngineRegion = EngineRegion

    @property
    def BoundK8SInfos(self):
        return self._BoundK8SInfos

    @BoundK8SInfos.setter
    def BoundK8SInfos(self, BoundK8SInfos):
        self._BoundK8SInfos = BoundK8SInfos

    @property
    def VpcInfos(self):
        return self._VpcInfos

    @VpcInfos.setter
    def VpcInfos(self, VpcInfos):
        self._VpcInfos = VpcInfos

    @property
    def AuthOpen(self):
        return self._AuthOpen

    @AuthOpen.setter
    def AuthOpen(self, AuthOpen):
        self._AuthOpen = AuthOpen

    @property
    def Features(self):
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def MainPassword(self):
        return self._MainPassword

    @MainPassword.setter
    def MainPassword(self, MainPassword):
        self._MainPassword = MainPassword

    @property
    def PgwVpcInfos(self):
        return self._PgwVpcInfos

    @PgwVpcInfos.setter
    def PgwVpcInfos(self, PgwVpcInfos):
        self._PgwVpcInfos = PgwVpcInfos

    @property
    def LimiterVpcInfos(self):
        return self._LimiterVpcInfos

    @LimiterVpcInfos.setter
    def LimiterVpcInfos(self, LimiterVpcInfos):
        self._LimiterVpcInfos = LimiterVpcInfos

    @property
    def CLSTopics(self):
        return self._CLSTopics

    @CLSTopics.setter
    def CLSTopics(self, CLSTopics):
        self._CLSTopics = CLSTopics


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        if params.get("BoundK8SInfos") is not None:
            self._BoundK8SInfos = []
            for item in params.get("BoundK8SInfos"):
                obj = BoundK8SInfo()
                obj._deserialize(item)
                self._BoundK8SInfos.append(obj)
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
        self._AuthOpen = params.get("AuthOpen")
        self._Features = params.get("Features")
        self._MainPassword = params.get("MainPassword")
        if params.get("PgwVpcInfos") is not None:
            self._PgwVpcInfos = []
            for item in params.get("PgwVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._PgwVpcInfos.append(obj)
        if params.get("LimiterVpcInfos") is not None:
            self._LimiterVpcInfos = []
            for item in params.get("LimiterVpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._LimiterVpcInfos.append(obj)
        if params.get("CLSTopics") is not None:
            self._CLSTopics = []
            for item in params.get("CLSTopics"):
                obj = PolarisCLSTopicInfo()
                obj._deserialize(item)
                self._CLSTopics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceWafStatus(AbstractModel):
    """服务的 WAF 状态

    """

    def __init__(self):
        r"""
        :param _Name:  服务的名字
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Id: 服务的 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _Type: 服务的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Status:  服务是否开启 WAF 防护
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Name = None
        self._Id = None
        self._Type = None
        self._Status = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageOption(AbstractModel):
    """存储的额外选项

    """

    def __init__(self):
        r"""
        :param _Name: 存储对象，分为snap和txn两种
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Type: 存储类型，分为三类CLOUD_PREMIUM/CLOUD_SSD/CLOUD_SSD_PLUS，分别对应高性能云硬盘、SSD云硬盘、增强型SSD云硬盘
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Capacity: 存储容量，[50, 3200]的范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Capacity: int
        """
        self._Name = None
        self._Type = None
        self._Capacity = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Capacity(self):
        return self._Capacity

    @Capacity.setter
    def Capacity(self, Capacity):
        self._Capacity = Capacity


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Capacity = params.get("Capacity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoScalerResourceStrategyFromGroupsRequest(AbstractModel):
    """UnbindAutoScalerResourceStrategyFromGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        :param _GroupIds: 网关分组ID列表
        :type GroupIds: list of str
        """
        self._GatewayId = None
        self._StrategyId = None
        self._GroupIds = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GroupIds(self):
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._StrategyId = params.get("StrategyId")
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindAutoScalerResourceStrategyFromGroupsResponse(AbstractModel):
    """UnbindAutoScalerResourceStrategyFromGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateCloudNativeAPIGatewayCertificateInfoRequest(AbstractModel):
    """UpdateCloudNativeAPIGatewayCertificateInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Id: 证书id
        :type Id: str
        :param _BindDomains: 绑定的域名列表
        :type BindDomains: list of str
        :param _Name: 证书名称
        :type Name: str
        """
        self._GatewayId = None
        self._Id = None
        self._BindDomains = None
        self._Name = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BindDomains(self):
        return self._BindDomains

    @BindDomains.setter
    def BindDomains(self, BindDomains):
        self._BindDomains = BindDomains

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Id = params.get("Id")
        self._BindDomains = params.get("BindDomains")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewayCertificateInfoResponse(AbstractModel):
    """UpdateCloudNativeAPIGatewayCertificateInfo返回参数结构体

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


class UpdateCloudNativeAPIGatewayResult(AbstractModel):
    """更新云原生API网关响应结果。

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关ID。
        :type GatewayId: str
        :param _Status: 云原生网关状态。
        :type Status: str
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        """
        self._GatewayId = None
        self._Status = None
        self._TaskId = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewaySpecRequest(AbstractModel):
    """UpdateCloudNativeAPIGatewaySpec请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 云原生API网关实例ID。
只支持后付费实例
        :type GatewayId: str
        :param _GroupId: 网关分组id
        :type GroupId: str
        :param _NodeConfig: 网关分组节点规格配置。
        :type NodeConfig: :class:`tencentcloud.tse.v20201207.models.CloudNativeAPIGatewayNodeConfig`
        """
        self._GatewayId = None
        self._GroupId = None
        self._NodeConfig = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NodeConfig(self):
        return self._NodeConfig

    @NodeConfig.setter
    def NodeConfig(self, NodeConfig):
        self._NodeConfig = NodeConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._GroupId = params.get("GroupId")
        if params.get("NodeConfig") is not None:
            self._NodeConfig = CloudNativeAPIGatewayNodeConfig()
            self._NodeConfig._deserialize(params.get("NodeConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCloudNativeAPIGatewaySpecResponse(AbstractModel):
    """UpdateCloudNativeAPIGatewaySpec返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 更新云原生API网关实例规格的响应结果。
        :type Result: :class:`tencentcloud.tse.v20201207.models.UpdateCloudNativeAPIGatewayResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UpdateCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class UpdateEngineInternetAccessRequest(AbstractModel):
    """UpdateEngineInternetAccess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 引擎ID
        :type InstanceId: str
        :param _EngineType: 引擎类型
        :type EngineType: str
        :param _EnableClientInternetAccess: 是否开启客户端公网访问，true开 false关
        :type EnableClientInternetAccess: bool
        """
        self._InstanceId = None
        self._EngineType = None
        self._EnableClientInternetAccess = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def EngineType(self):
        return self._EngineType

    @EngineType.setter
    def EngineType(self, EngineType):
        self._EngineType = EngineType

    @property
    def EnableClientInternetAccess(self):
        return self._EnableClientInternetAccess

    @EnableClientInternetAccess.setter
    def EnableClientInternetAccess(self, EnableClientInternetAccess):
        self._EnableClientInternetAccess = EnableClientInternetAccess


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._EngineType = params.get("EngineType")
        self._EnableClientInternetAccess = params.get("EnableClientInternetAccess")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateEngineInternetAccessResponse(AbstractModel):
    """UpdateEngineInternetAccess返回参数结构体

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


class UpdateUpstreamHealthCheckConfigRequest(AbstractModel):
    """UpdateUpstreamHealthCheckConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _Name: 网关服务名称
        :type Name: str
        :param _HealthCheckConfig: 健康检查配置
        :type HealthCheckConfig: :class:`tencentcloud.tse.v20201207.models.UpstreamHealthCheckConfig`
        """
        self._GatewayId = None
        self._Name = None
        self._HealthCheckConfig = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def HealthCheckConfig(self):
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = UpstreamHealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUpstreamHealthCheckConfigResponse(AbstractModel):
    """UpdateUpstreamHealthCheckConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateUpstreamTargetsRequest(AbstractModel):
    """UpdateUpstreamTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关实例ID
        :type GatewayId: str
        :param _Name: 服务名称或ID
        :type Name: str
        :param _Targets: 实例列表
        :type Targets: list of KongTarget
        """
        self._GatewayId = None
        self._Name = None
        self._Targets = None

    @property
    def GatewayId(self):
        return self._GatewayId

    @GatewayId.setter
    def GatewayId(self, GatewayId):
        self._GatewayId = GatewayId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Targets(self):
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets


    def _deserialize(self, params):
        self._GatewayId = params.get("GatewayId")
        self._Name = params.get("Name")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = KongTarget()
                obj._deserialize(item)
                self._Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUpstreamTargetsResponse(AbstractModel):
    """UpdateUpstreamTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否更新成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpstreamHealthCheckConfig(AbstractModel):
    """云原生网关健康检查配置

    """

    def __init__(self):
        r"""
        :param _EnableActiveHealthCheck: 开启主动健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableActiveHealthCheck: bool
        :param _ActiveHealthCheck: 主动健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ActiveHealthCheck: :class:`tencentcloud.tse.v20201207.models.KongActiveHealthCheck`
        :param _EnablePassiveHealthCheck: 开启被动健康检查
注意：此字段可能返回 null，表示取不到有效值。
        :type EnablePassiveHealthCheck: bool
        :param _PassiveHealthCheck: 被动健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PassiveHealthCheck: :class:`tencentcloud.tse.v20201207.models.KongPassiveHealthCheck`
        :param _Successes: 连续健康阈值，单位：次
注意：此字段可能返回 null，表示取不到有效值。
        :type Successes: int
        :param _Failures: 连续异常阈值，单位：次	
注意：此字段可能返回 null，表示取不到有效值。
        :type Failures: int
        :param _Timeouts: 超时阈值，单位：次
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeouts: int
        :param _HealthyHttpStatuses: 健康HTTP状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyHttpStatuses: list of int non-negative
        :param _UnhealthyHttpStatuses: 异常HTTP状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type UnhealthyHttpStatuses: list of int non-negative
        :param _IgnoreZeroWeightNodes: 健康检查监控上报的数据屏蔽权重为0的节点
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreZeroWeightNodes: bool
        :param _ZeroWeightHeathCheck: 健康检查支持权重为0节点
注意：此字段可能返回 null，表示取不到有效值。
        :type ZeroWeightHeathCheck: bool
        """
        self._EnableActiveHealthCheck = None
        self._ActiveHealthCheck = None
        self._EnablePassiveHealthCheck = None
        self._PassiveHealthCheck = None
        self._Successes = None
        self._Failures = None
        self._Timeouts = None
        self._HealthyHttpStatuses = None
        self._UnhealthyHttpStatuses = None
        self._IgnoreZeroWeightNodes = None
        self._ZeroWeightHeathCheck = None

    @property
    def EnableActiveHealthCheck(self):
        return self._EnableActiveHealthCheck

    @EnableActiveHealthCheck.setter
    def EnableActiveHealthCheck(self, EnableActiveHealthCheck):
        self._EnableActiveHealthCheck = EnableActiveHealthCheck

    @property
    def ActiveHealthCheck(self):
        return self._ActiveHealthCheck

    @ActiveHealthCheck.setter
    def ActiveHealthCheck(self, ActiveHealthCheck):
        self._ActiveHealthCheck = ActiveHealthCheck

    @property
    def EnablePassiveHealthCheck(self):
        return self._EnablePassiveHealthCheck

    @EnablePassiveHealthCheck.setter
    def EnablePassiveHealthCheck(self, EnablePassiveHealthCheck):
        self._EnablePassiveHealthCheck = EnablePassiveHealthCheck

    @property
    def PassiveHealthCheck(self):
        return self._PassiveHealthCheck

    @PassiveHealthCheck.setter
    def PassiveHealthCheck(self, PassiveHealthCheck):
        self._PassiveHealthCheck = PassiveHealthCheck

    @property
    def Successes(self):
        return self._Successes

    @Successes.setter
    def Successes(self, Successes):
        self._Successes = Successes

    @property
    def Failures(self):
        return self._Failures

    @Failures.setter
    def Failures(self, Failures):
        self._Failures = Failures

    @property
    def Timeouts(self):
        return self._Timeouts

    @Timeouts.setter
    def Timeouts(self, Timeouts):
        self._Timeouts = Timeouts

    @property
    def HealthyHttpStatuses(self):
        return self._HealthyHttpStatuses

    @HealthyHttpStatuses.setter
    def HealthyHttpStatuses(self, HealthyHttpStatuses):
        self._HealthyHttpStatuses = HealthyHttpStatuses

    @property
    def UnhealthyHttpStatuses(self):
        return self._UnhealthyHttpStatuses

    @UnhealthyHttpStatuses.setter
    def UnhealthyHttpStatuses(self, UnhealthyHttpStatuses):
        self._UnhealthyHttpStatuses = UnhealthyHttpStatuses

    @property
    def IgnoreZeroWeightNodes(self):
        warnings.warn("parameter `IgnoreZeroWeightNodes` is deprecated", DeprecationWarning) 

        return self._IgnoreZeroWeightNodes

    @IgnoreZeroWeightNodes.setter
    def IgnoreZeroWeightNodes(self, IgnoreZeroWeightNodes):
        warnings.warn("parameter `IgnoreZeroWeightNodes` is deprecated", DeprecationWarning) 

        self._IgnoreZeroWeightNodes = IgnoreZeroWeightNodes

    @property
    def ZeroWeightHeathCheck(self):
        return self._ZeroWeightHeathCheck

    @ZeroWeightHeathCheck.setter
    def ZeroWeightHeathCheck(self, ZeroWeightHeathCheck):
        self._ZeroWeightHeathCheck = ZeroWeightHeathCheck


    def _deserialize(self, params):
        self._EnableActiveHealthCheck = params.get("EnableActiveHealthCheck")
        if params.get("ActiveHealthCheck") is not None:
            self._ActiveHealthCheck = KongActiveHealthCheck()
            self._ActiveHealthCheck._deserialize(params.get("ActiveHealthCheck"))
        self._EnablePassiveHealthCheck = params.get("EnablePassiveHealthCheck")
        if params.get("PassiveHealthCheck") is not None:
            self._PassiveHealthCheck = KongPassiveHealthCheck()
            self._PassiveHealthCheck._deserialize(params.get("PassiveHealthCheck"))
        self._Successes = params.get("Successes")
        self._Failures = params.get("Failures")
        self._Timeouts = params.get("Timeouts")
        self._HealthyHttpStatuses = params.get("HealthyHttpStatuses")
        self._UnhealthyHttpStatuses = params.get("UnhealthyHttpStatuses")
        self._IgnoreZeroWeightNodes = params.get("IgnoreZeroWeightNodes")
        self._ZeroWeightHeathCheck = params.get("ZeroWeightHeathCheck")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """私有网络信息

    """

    def __init__(self):
        r"""
        :param _VpcId: Vpc Id
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        :param _IntranetAddress: 内网访问地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetAddress: str
        :param _LbSubnetId: 负载均衡均衡接入点子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LbSubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None
        self._IntranetAddress = None
        self._LbSubnetId = None

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

    @property
    def IntranetAddress(self):
        return self._IntranetAddress

    @IntranetAddress.setter
    def IntranetAddress(self, IntranetAddress):
        self._IntranetAddress = IntranetAddress

    @property
    def LbSubnetId(self):
        return self._LbSubnetId

    @LbSubnetId.setter
    def LbSubnetId(self, LbSubnetId):
        self._LbSubnetId = LbSubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IntranetAddress = params.get("IntranetAddress")
        self._LbSubnetId = params.get("LbSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperRegionInfo(AbstractModel):
    """Zookeeper的地域额外信息记录

    """

    def __init__(self):
        r"""
        :param _DeployMode: 部署架构信息

- SingleRegion: 普通单地域
- MultiRegion: 普通多地域场景
- MasterSlave: 两地域，主备地域场景
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployMode: str
        :param _MainRegion: 主地域的额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MainRegion: :class:`tencentcloud.tse.v20201207.models.ZookeeperRegionMyIdInfo`
        :param _OtherRegions: 其他地域的额外信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OtherRegions: list of ZookeeperRegionMyIdInfo
        """
        self._DeployMode = None
        self._MainRegion = None
        self._OtherRegions = None

    @property
    def DeployMode(self):
        return self._DeployMode

    @DeployMode.setter
    def DeployMode(self, DeployMode):
        self._DeployMode = DeployMode

    @property
    def MainRegion(self):
        return self._MainRegion

    @MainRegion.setter
    def MainRegion(self, MainRegion):
        self._MainRegion = MainRegion

    @property
    def OtherRegions(self):
        return self._OtherRegions

    @OtherRegions.setter
    def OtherRegions(self, OtherRegions):
        self._OtherRegions = OtherRegions


    def _deserialize(self, params):
        self._DeployMode = params.get("DeployMode")
        if params.get("MainRegion") is not None:
            self._MainRegion = ZookeeperRegionMyIdInfo()
            self._MainRegion._deserialize(params.get("MainRegion"))
        if params.get("OtherRegions") is not None:
            self._OtherRegions = []
            for item in params.get("OtherRegions"):
                obj = ZookeeperRegionMyIdInfo()
                obj._deserialize(item)
                self._OtherRegions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperRegionMyIdInfo(AbstractModel):
    """Zookeeper的地域信息的 myid 信息记录

    """

    def __init__(self):
        r"""
        :param _Region: 地域信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _MyIdStart: myid 的起始号段
注意：此字段可能返回 null，表示取不到有效值。
        :type MyIdStart: int
        :param _MyIdEnd: myid 的结束号段
注意：此字段可能返回 null，表示取不到有效值。
        :type MyIdEnd: int
        """
        self._Region = None
        self._MyIdStart = None
        self._MyIdEnd = None

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def MyIdStart(self):
        return self._MyIdStart

    @MyIdStart.setter
    def MyIdStart(self, MyIdStart):
        self._MyIdStart = MyIdStart

    @property
    def MyIdEnd(self):
        return self._MyIdEnd

    @MyIdEnd.setter
    def MyIdEnd(self, MyIdEnd):
        self._MyIdEnd = MyIdEnd


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._MyIdStart = params.get("MyIdStart")
        self._MyIdEnd = params.get("MyIdEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperReplica(AbstractModel):
    """Zookeeper副本信息

    """

    def __init__(self):
        r"""
        :param _Name: 名称
        :type Name: str
        :param _Role: 角色
        :type Role: str
        :param _Status: 状态
        :type Status: str
        :param _SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Zone: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Zone: str
        :param _ZoneId: 可用区ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _AliasName: 别名
注意：此字段可能返回 null，表示取不到有效值。
        :type AliasName: str
        :param _VpcId: VPC ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        """
        self._Name = None
        self._Role = None
        self._Status = None
        self._SubnetId = None
        self._Zone = None
        self._ZoneId = None
        self._AliasName = None
        self._VpcId = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubnetId(self):
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def AliasName(self):
        return self._AliasName

    @AliasName.setter
    def AliasName(self, AliasName):
        self._AliasName = AliasName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._SubnetId = params.get("SubnetId")
        self._Zone = params.get("Zone")
        self._ZoneId = params.get("ZoneId")
        self._AliasName = params.get("AliasName")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZookeeperServerInterface(AbstractModel):
    """Zookeeper服务端接口列表，用于云监控

    """

    def __init__(self):
        r"""
        :param _Interface: 接口名
注意：此字段可能返回 null，表示取不到有效值。
        :type Interface: str
        """
        self._Interface = None

    @property
    def Interface(self):
        return self._Interface

    @Interface.setter
    def Interface(self, Interface):
        self._Interface = Interface


    def _deserialize(self, params):
        self._Interface = params.get("Interface")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        