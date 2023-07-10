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
        """
        self._BoundClusterId = None
        self._BoundClusterType = None
        self._SyncMode = None

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


    def _deserialize(self, params):
        self._BoundClusterId = params.get("BoundClusterId")
        self._BoundClusterType = params.get("BoundClusterType")
        self._SyncMode = params.get("SyncMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """
        self._Priority = None
        self._Enabled = None
        self._ConditionList = None
        self._BalancedServiceList = None
        self._ServiceId = None
        self._ServiceName = None

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
        """
        self._NodeId = None
        self._NodeIp = None
        self._ZoneId = None
        self._Zone = None
        self._GroupId = None
        self._GroupName = None
        self._Status = None

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


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeIp = params.get("NodeIp")
        self._ZoneId = params.get("ZoneId")
        self._Zone = params.get("Zone")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._Status = params.get("Status")
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
        :param _LimitBy: 限流依据
ip service consumer credential path header
        :type LimitBy: str
        :param _ResponseType: 响应策略
url请求转发
text 响应配置
default 直接返回

        :type ResponseType: str
        :param _HideClientHeaders: 是否隐藏限流客户端响应头
        :type HideClientHeaders: bool
        :param _IsDelay: 是否开启请求排队
        :type IsDelay: bool
        :param _Path: 需要进行流量控制的请求路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Header: 需要进行流量控制的请求头Key
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: str
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
        :param _LineUpTime: 排队时间
        :type LineUpTime: int
        """
        self._Enabled = None
        self._QpsThresholds = None
        self._LimitBy = None
        self._ResponseType = None
        self._HideClientHeaders = None
        self._IsDelay = None
        self._Path = None
        self._Header = None
        self._ExternalRedis = None
        self._Policy = None
        self._RateLimitResponse = None
        self._RateLimitResponseUrl = None
        self._LineUpTime = None

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
    def LimitBy(self):
        return self._LimitBy

    @LimitBy.setter
    def LimitBy(self, LimitBy):
        self._LimitBy = LimitBy

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
    def IsDelay(self):
        return self._IsDelay

    @IsDelay.setter
    def IsDelay(self, IsDelay):
        self._IsDelay = IsDelay

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
    def LineUpTime(self):
        return self._LineUpTime

    @LineUpTime.setter
    def LineUpTime(self, LineUpTime):
        self._LineUpTime = LineUpTime


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        if params.get("QpsThresholds") is not None:
            self._QpsThresholds = []
            for item in params.get("QpsThresholds"):
                obj = QpsThreshold()
                obj._deserialize(item)
                self._QpsThresholds.append(obj)
        self._LimitBy = params.get("LimitBy")
        self._ResponseType = params.get("ResponseType")
        self._HideClientHeaders = params.get("HideClientHeaders")
        self._IsDelay = params.get("IsDelay")
        self._Path = params.get("Path")
        self._Header = params.get("Header")
        if params.get("ExternalRedis") is not None:
            self._ExternalRedis = ExternalRedis()
            self._ExternalRedis._deserialize(params.get("ExternalRedis"))
        self._Policy = params.get("Policy")
        if params.get("RateLimitResponse") is not None:
            self._RateLimitResponse = RateLimitResponse()
            self._RateLimitResponse._deserialize(params.get("RateLimitResponse"))
        self._RateLimitResponseUrl = params.get("RateLimitResponseUrl")
        self._LineUpTime = params.get("LineUpTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _EngineAdmin: 引擎的初始帐号信息。可设置参数：
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
        :type EngineRegionInfos: list of EngineRegionInfo
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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


class DescribeCloudNativeAPIGatewayCanaryRulesRequest(AbstractModel):
    """DescribeCloudNativeAPIGatewayCanaryRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GatewayId: 网关ID
        :type GatewayId: str
        :param _ServiceId: 服务 ID
        :type ServiceId: str
        :param _Limit: 列表数量
        :type Limit: int
        :param _Offset: 列表offset
        :type Offset: int
        """
        self._GatewayId = None
        self._ServiceId = None
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _IntranetVpcInfos: 内网的网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntranetVpcInfos: list of VpcInfo
        :param _EnableClientInternet: 是否开公网
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableClientInternet: bool
        """
        self._EngineRegion = None
        self._Replica = None
        self._SpecId = None
        self._IntranetVpcInfos = None
        self._EnableClientInternet = None

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
    def EnableClientInternet(self):
        return self._EnableClientInternet

    @EnableClientInternet.setter
    def EnableClientInternet(self, EnableClientInternet):
        self._EnableClientInternet = EnableClientInternet


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
        self._EnableClientInternet = params.get("EnableClientInternet")
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
    """引擎的初始管理帐号

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
        """
        self._EngineRegion = None
        self._Replica = None
        self._VpcInfos = None

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


    def _deserialize(self, params):
        self._EngineRegion = params.get("EngineRegion")
        self._Replica = params.get("Replica")
        if params.get("VpcInfos") is not None:
            self._VpcInfos = []
            for item in params.get("VpcInfos"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcInfos.append(obj)
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
        """
        self._EnvName = None
        self._EnableConfigInternet = None
        self._ConfigInternetServiceIp = None
        self._ConfigIntranetAddress = None
        self._EnableConfigIntranet = None
        self._InternetBandWidth = None

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


    def _deserialize(self, params):
        self._EnvName = params.get("EnvName")
        self._EnableConfigInternet = params.get("EnableConfigInternet")
        self._ConfigInternetServiceIp = params.get("ConfigInternetServiceIp")
        self._ConfigIntranetAddress = params.get("ConfigIntranetAddress")
        self._EnableConfigIntranet = params.get("EnableConfigIntranet")
        self._InternetBandWidth = params.get("InternetBandWidth")
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
        :type Headers: :class:`tencentcloud.tse.v20201207.models.KVMapping`
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
        return self._ForceHttps

    @ForceHttps.setter
    def ForceHttps(self, ForceHttps):
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
            self._Headers = KVMapping()
            self._Headers._deserialize(params.get("Headers"))
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
        """
        self._ID = None
        self._Name = None
        self._Tags = None
        self._UpstreamInfo = None
        self._UpstreamType = None
        self._CreatedTime = None
        self._Editable = None

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
        :type Host: str
        :param _Port: 端口
        :type Port: int
        :param _Weight: 权重
        :type Weight: int
        :param _Health: 健康状态
        :type Health: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _Source: Target的来源
        :type Source: str
        """
        self._Host = None
        self._Port = None
        self._Weight = None
        self._Health = None
        self._CreatedTime = None
        self._Source = None

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


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._Health = params.get("Health")
        self._CreatedTime = params.get("CreatedTime")
        self._Source = params.get("Source")
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
        :type Host: str
        :param _Port: 端口
        :type Port: int
        :param _SourceID: 服务来源ID
        :type SourceID: str
        :param _Namespace: 名字空间
        :type Namespace: str
        :param _ServiceName: 服务（注册中心或Kubernetes中的服务）名字
        :type ServiceName: str
        :param _Targets: 服务后端类型是IPList时提供
        :type Targets: list of KongTarget
        :param _SourceType: 服务来源类型
        :type SourceType: str
        :param _ScfType: SCF函数类型
        :type ScfType: str
        :param _ScfNamespace: SCF函数命名空间
        :type ScfNamespace: str
        :param _ScfLambdaName: SCF函数名
        :type ScfLambdaName: str
        :param _ScfLambdaQualifier: SCF函数版本
        :type ScfLambdaQualifier: str
        :param _SlowStart: 冷启动时间，单位秒
        :type SlowStart: int
        :param _Algorithm: 负载均衡算法，默认为 round-robin，还支持 least-connections，consisten_hashing
        :type Algorithm: str
        :param _AutoScalingGroupID: CVM弹性伸缩组ID
        :type AutoScalingGroupID: str
        :param _AutoScalingCvmPort: CVM弹性伸缩组端口
        :type AutoScalingCvmPort: int
        :param _AutoScalingTatCmdStatus: CVM弹性伸缩组使用的CVM TAT命令状态
        :type AutoScalingTatCmdStatus: str
        :param _AutoScalingHookStatus: CVM弹性伸缩组生命周期挂钩状态
        :type AutoScalingHookStatus: str
        :param _SourceName: 服务来源的名字
        :type SourceName: str
        :param _RealSourceType: 精确的服务来源类型，新建服务来源时候传入的类型
        :type RealSourceType: str
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        :param _Headers: headrs
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
        """
        self._EngineRegion = None
        self._BoundK8SInfos = None
        self._VpcInfos = None
        self._AuthOpen = None
        self._Features = None
        self._MainPassword = None
        self._PgwVpcInfos = None
        self._LimiterVpcInfos = None

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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
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
        """
        self._VpcId = None
        self._SubnetId = None
        self._IntranetAddress = None

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


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._IntranetAddress = params.get("IntranetAddress")
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
        