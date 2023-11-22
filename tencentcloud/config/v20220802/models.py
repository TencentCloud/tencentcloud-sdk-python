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


class Annotation(AbstractModel):
    """合规详情

    """

    def __init__(self):
        r"""
        :param _Configuration: 资源当前实际配置。长度为0~256位字符，即资源不合规配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: str
        :param _DesiredValue: 资源期望配置。长度为0~256位字符，即资源合规配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredValue: str
        :param _Operator: 资源当前配置和期望配置之间的比较运算符。长度为0~16位字符，自定义规则上报评估结果此字段可能为空
        :type Operator: str
        :param _Property: 当前配置在资源属性结构体中的JSON路径。长度为0~256位字符，自定义规则上报评估结果此字段可能为空
        :type Property: str
        """
        self._Configuration = None
        self._DesiredValue = None
        self._Operator = None
        self._Property = None

    @property
    def Configuration(self):
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def DesiredValue(self):
        return self._DesiredValue

    @DesiredValue.setter
    def DesiredValue(self, DesiredValue):
        self._DesiredValue = DesiredValue

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Property(self):
        return self._Property

    @Property.setter
    def Property(self, Property):
        self._Property = Property


    def _deserialize(self, params):
        self._Configuration = params.get("Configuration")
        self._DesiredValue = params.get("DesiredValue")
        self._Operator = params.get("Operator")
        self._Property = params.get("Property")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigRule(AbstractModel):
    """规则详情

    """

    def __init__(self):
        r"""
        :param _Identifier: 规则标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Identifier: str
        :param _RuleName: 规则名
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _InputParameter: 规则参数
注意：此字段可能返回 null，表示取不到有效值。
        :type InputParameter: list of InputParameter
        :param _SourceCondition: 规则触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCondition: list of SourceConditionForManage
        :param _ResourceType: 规则支持的资源类型，规则仅对指定资源类型的资源生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: list of str
        :param _Labels: 规则所属标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param _RiskLevel: 规则风险等级
1:低风险
2:中风险
3:高风险
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param _ServiceFunction: 规则对应的函数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceFunction: str
        :param _CreateTime: 创建时间
格式：YYYY-MM-DD h:i:s
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Status: ACTIVE：启用
NO_ACTIVE：停止
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ComplianceResult: 合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
无法应用规则： 'NOT_APPLICABLE'
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceResult: str
        :param _Annotation: ["",""]
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        :param _ConfigRuleInvokedTime: 规则评估时间
格式：YYYY-MM-DD h:i:s

注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRuleInvokedTime: str
        :param _ConfigRuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRuleId: str
        :param _IdentifierType: CUSTOMIZE：自定义规则、
SYSTEM：托管规则
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentifierType: str
        :param _CompliancePackId: 合规包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CompliancePackId: str
        :param _TriggerType: 触发类型
ScheduledNotification：周期触发、
ConfigurationItemChangeNotification：变更触发
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: list of TriggerType
        :param _ManageInputParameter: 参数详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageInputParameter: list of InputParameterForManage
        :param _CompliancePackName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CompliancePackName: str
        :param _RegionsScope: 关联地域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionsScope: list of str
        :param _TagsScope: 关联标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope:  规则对指定资源ID无效，即不对该资源执行评估。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExcludeResourceIdsScope: list of str
        :param _AccountGroupId: 账号组ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupId: str
        :param _AccountGroupName: 账号组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupName: str
        :param _RuleOwnerId: 规则所属用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleOwnerId: int
        :param _ManageTriggerType: 预设规则支持的触发方式
ScheduledNotification：周期触发
ConfigurationItemChangeNotification：变更触发
        :type ManageTriggerType: list of str
        """
        self._Identifier = None
        self._RuleName = None
        self._InputParameter = None
        self._SourceCondition = None
        self._ResourceType = None
        self._Labels = None
        self._RiskLevel = None
        self._ServiceFunction = None
        self._CreateTime = None
        self._Description = None
        self._Status = None
        self._ComplianceResult = None
        self._Annotation = None
        self._ConfigRuleInvokedTime = None
        self._ConfigRuleId = None
        self._IdentifierType = None
        self._CompliancePackId = None
        self._TriggerType = None
        self._ManageInputParameter = None
        self._CompliancePackName = None
        self._RegionsScope = None
        self._TagsScope = None
        self._ExcludeResourceIdsScope = None
        self._AccountGroupId = None
        self._AccountGroupName = None
        self._RuleOwnerId = None
        self._ManageTriggerType = None

    @property
    def Identifier(self):
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def SourceCondition(self):
        return self._SourceCondition

    @SourceCondition.setter
    def SourceCondition(self, SourceCondition):
        self._SourceCondition = SourceCondition

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Labels(self):
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ServiceFunction(self):
        return self._ServiceFunction

    @ServiceFunction.setter
    def ServiceFunction(self, ServiceFunction):
        self._ServiceFunction = ServiceFunction

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ComplianceResult(self):
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def Annotation(self):
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation

    @property
    def ConfigRuleInvokedTime(self):
        return self._ConfigRuleInvokedTime

    @ConfigRuleInvokedTime.setter
    def ConfigRuleInvokedTime(self, ConfigRuleInvokedTime):
        self._ConfigRuleInvokedTime = ConfigRuleInvokedTime

    @property
    def ConfigRuleId(self):
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def IdentifierType(self):
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType

    @property
    def CompliancePackId(self):
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def TriggerType(self):
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def ManageInputParameter(self):
        return self._ManageInputParameter

    @ManageInputParameter.setter
    def ManageInputParameter(self, ManageInputParameter):
        self._ManageInputParameter = ManageInputParameter

    @property
    def CompliancePackName(self):
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RegionsScope(self):
        return self._RegionsScope

    @RegionsScope.setter
    def RegionsScope(self, RegionsScope):
        self._RegionsScope = RegionsScope

    @property
    def TagsScope(self):
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountGroupName(self):
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def RuleOwnerId(self):
        return self._RuleOwnerId

    @RuleOwnerId.setter
    def RuleOwnerId(self, RuleOwnerId):
        self._RuleOwnerId = RuleOwnerId

    @property
    def ManageTriggerType(self):
        return self._ManageTriggerType

    @ManageTriggerType.setter
    def ManageTriggerType(self, ManageTriggerType):
        self._ManageTriggerType = ManageTriggerType


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._RuleName = params.get("RuleName")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        if params.get("SourceCondition") is not None:
            self._SourceCondition = []
            for item in params.get("SourceCondition"):
                obj = SourceConditionForManage()
                obj._deserialize(item)
                self._SourceCondition.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._Labels = params.get("Labels")
        self._RiskLevel = params.get("RiskLevel")
        self._ServiceFunction = params.get("ServiceFunction")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._ComplianceResult = params.get("ComplianceResult")
        if params.get("Annotation") is not None:
            self._Annotation = Annotation()
            self._Annotation._deserialize(params.get("Annotation"))
        self._ConfigRuleInvokedTime = params.get("ConfigRuleInvokedTime")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._IdentifierType = params.get("IdentifierType")
        self._CompliancePackId = params.get("CompliancePackId")
        if params.get("TriggerType") is not None:
            self._TriggerType = []
            for item in params.get("TriggerType"):
                obj = TriggerType()
                obj._deserialize(item)
                self._TriggerType.append(obj)
        if params.get("ManageInputParameter") is not None:
            self._ManageInputParameter = []
            for item in params.get("ManageInputParameter"):
                obj = InputParameterForManage()
                obj._deserialize(item)
                self._ManageInputParameter.append(obj)
        self._CompliancePackName = params.get("CompliancePackName")
        self._RegionsScope = params.get("RegionsScope")
        if params.get("TagsScope") is not None:
            self._TagsScope = []
            for item in params.get("TagsScope"):
                obj = Tag()
                obj._deserialize(item)
                self._TagsScope.append(obj)
        self._ExcludeResourceIdsScope = params.get("ExcludeResourceIdsScope")
        self._AccountGroupId = params.get("AccountGroupId")
        self._AccountGroupName = params.get("AccountGroupName")
        self._RuleOwnerId = params.get("RuleOwnerId")
        self._ManageTriggerType = params.get("ManageTriggerType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputParameter(AbstractModel):
    """参数值

    """

    def __init__(self):
        r"""
        :param _ParameterKey: 参数名
        :type ParameterKey: str
        :param _Type: 参数类型。必填类型：Require，可选类型：Optional。
        :type Type: str
        :param _Value: 参数值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._ParameterKey = None
        self._Type = None
        self._Value = None

    @property
    def ParameterKey(self):
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

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


    def _deserialize(self, params):
        self._ParameterKey = params.get("ParameterKey")
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputParameterForManage(AbstractModel):
    """规则入参

    """

    def __init__(self):
        r"""
        :param _ValueType: 值类型。数值：Integer， 字符串：String
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueType: str
        :param _ParameterKey: 参数Key
注意：此字段可能返回 null，表示取不到有效值。
        :type ParameterKey: str
        :param _Type: 参数类型。必填类型：Require，可选类型：Optional。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _DefaultValue: 默认值
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._ValueType = None
        self._ParameterKey = None
        self._Type = None
        self._DefaultValue = None
        self._Description = None

    @property
    def ValueType(self):
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def ParameterKey(self):
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._ValueType = params.get("ValueType")
        self._ParameterKey = params.get("ParameterKey")
        self._Type = params.get("Type")
        self._DefaultValue = params.get("DefaultValue")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateConfigRulesRequest(AbstractModel):
    """ListAggregateConfigRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _OrderType: 排序类型, 倒序：desc，顺序：asc
        :type OrderType: str
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: list of int non-negative
        :param _State: 规则状态
        :type State: str
        :param _ComplianceResult: 评估结果
        :type ComplianceResult: list of str
        :param _RuleName: 规则名
        :type RuleName: str
        :param _RuleOwnerId: 规则所属账号ID
        :type RuleOwnerId: int
        """
        self._Limit = None
        self._Offset = None
        self._AccountGroupId = None
        self._OrderType = None
        self._RiskLevel = None
        self._State = None
        self._ComplianceResult = None
        self._RuleName = None
        self._RuleOwnerId = None

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
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleOwnerId(self):
        return self._RuleOwnerId

    @RuleOwnerId.setter
    def RuleOwnerId(self, RuleOwnerId):
        self._RuleOwnerId = RuleOwnerId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountGroupId = params.get("AccountGroupId")
        self._OrderType = params.get("OrderType")
        self._RiskLevel = params.get("RiskLevel")
        self._State = params.get("State")
        self._ComplianceResult = params.get("ComplianceResult")
        self._RuleName = params.get("RuleName")
        self._RuleOwnerId = params.get("RuleOwnerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateConfigRulesResponse(AbstractModel):
    """ListAggregateConfigRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 详情
        :type Items: list of ConfigRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListConfigRulesRequest(AbstractModel):
    """ListConfigRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _OrderType: 排序类型, 倒序：desc，顺序：asc
        :type OrderType: str
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: list of int non-negative
        :param _State: 规则状态
        :type State: str
        :param _ComplianceResult: 评估结果
        :type ComplianceResult: list of str
        :param _RuleName: 规则名
        :type RuleName: str
        """
        self._Limit = None
        self._Offset = None
        self._OrderType = None
        self._RiskLevel = None
        self._State = None
        self._ComplianceResult = None
        self._RuleName = None

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
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderType = params.get("OrderType")
        self._RiskLevel = params.get("RiskLevel")
        self._State = params.get("State")
        self._ComplianceResult = params.get("ComplianceResult")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConfigRulesResponse(AbstractModel):
    """ListConfigRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 详情
        :type Items: list of ConfigRule
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class SourceConditionForManage(AbstractModel):
    """管理端规则条件

    """

    def __init__(self):
        r"""
        :param _EmptyAs: 条件为空，合规：COMPLIANT，不合规：NON_COMPLIANT，无法应用：NOT_APPLICABLE
注意：此字段可能返回 null，表示取不到有效值。
        :type EmptyAs: str
        :param _SelectPath: 配置路径
注意：此字段可能返回 null，表示取不到有效值。
        :type SelectPath: str
        :param _Operator: 操作运算符
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Required: 是否必须
注意：此字段可能返回 null，表示取不到有效值。
        :type Required: bool
        :param _DesiredValue: 期望值
注意：此字段可能返回 null，表示取不到有效值。
        :type DesiredValue: str
        """
        self._EmptyAs = None
        self._SelectPath = None
        self._Operator = None
        self._Required = None
        self._DesiredValue = None

    @property
    def EmptyAs(self):
        return self._EmptyAs

    @EmptyAs.setter
    def EmptyAs(self, EmptyAs):
        self._EmptyAs = EmptyAs

    @property
    def SelectPath(self):
        return self._SelectPath

    @SelectPath.setter
    def SelectPath(self, SelectPath):
        self._SelectPath = SelectPath

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DesiredValue(self):
        return self._DesiredValue

    @DesiredValue.setter
    def DesiredValue(self, DesiredValue):
        self._DesiredValue = DesiredValue


    def _deserialize(self, params):
        self._EmptyAs = params.get("EmptyAs")
        self._SelectPath = params.get("SelectPath")
        self._Operator = params.get("Operator")
        self._Required = params.get("Required")
        self._DesiredValue = params.get("DesiredValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签key
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签value
注意：此字段可能返回 null，表示取不到有效值。
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
        


class TriggerType(AbstractModel):
    """规则支持触发类型

    """

    def __init__(self):
        r"""
        :param _MessageType: 触发类型
        :type MessageType: str
        :param _MaximumExecutionFrequency: 触发时间周期
注意：此字段可能返回 null，表示取不到有效值。
        :type MaximumExecutionFrequency: str
        """
        self._MessageType = None
        self._MaximumExecutionFrequency = None

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def MaximumExecutionFrequency(self):
        return self._MaximumExecutionFrequency

    @MaximumExecutionFrequency.setter
    def MaximumExecutionFrequency(self, MaximumExecutionFrequency):
        self._MaximumExecutionFrequency = MaximumExecutionFrequency


    def _deserialize(self, params):
        self._MessageType = params.get("MessageType")
        self._MaximumExecutionFrequency = params.get("MaximumExecutionFrequency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        