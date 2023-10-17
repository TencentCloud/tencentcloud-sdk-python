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
        :param _Type: 类型，Pods或Percent
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
        :param _StabilizationWindowSeconds: 稳定窗口时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StabilizationWindowSeconds: int
        :param _SelectPolicy: 选择策略依据
注意：此字段可能返回 null，表示取不到有效值。
        :type SelectPolicy: str
        :param _Policies: 扩容策略
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
        :param _SlaType: 负载均衡的规格类型，传 "SLA" 表示性能容量型，返回空为共享型
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaType: str
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
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _ResourceName: 指标资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _TargetType: 指标目标类型
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
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
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
        :param _TargetReplicas: 定时伸缩目标节点数
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetReplicas: int
        :param _Crontab: 定时伸缩cron表达式
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
            self._Result = CertificateInfo()
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
            self._Result = CreateCloudNativeAPIGatewayServerGroupResult()
            self._Result._deserialize(params.get("Result"))
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
            self._Result = ListCloudNativeAPIGatewayResult()
            self._Result._deserialize(params.get("Result"))
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
        :param _CLBMultiRegion: InternetAddress 的公网 CLB 多可用区信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CLBMultiRegion: :class:`tencentcloud.tse.v20201207.models.CLBMultiRegion`
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
        :param _MainRegion: 是否为主地域
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
        """
        self._HttpPort = None
        self._HttpsPort = None

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


    def _deserialize(self, params):
        self._HttpPort = params.get("HttpPort")
        self._HttpsPort = params.get("HttpsPort")
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
        :param _SlaType: 负载均衡的规格类型，传 "SLA" 表示性能容量型，不传为共享型。
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
        