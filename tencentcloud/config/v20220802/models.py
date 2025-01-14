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


class AggregateResourceInfo(AbstractModel):
    """资源列列表信息

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceRegion: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param _ResourceStatus: 资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: str
        :param _ResourceDelete: 是否删除 1:已删除 0:未删除
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceDelete: int
        :param _ResourceCreateTime: 资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCreateTime: str
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ResourceZone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceZone: str
        :param _ComplianceResult: 合规状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceResult: str
        :param _ResourceOwnerId: 资源所属用户ID
        :type ResourceOwnerId: int
        :param _ResourceOwnerName: 用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceOwnerName: str
        """
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ResourceStatus = None
        self._ResourceDelete = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._ResourceZone = None
        self._ComplianceResult = None
        self._ResourceOwnerId = None
        self._ResourceOwnerName = None

    @property
    def ResourceType(self):
        """资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceStatus(self):
        """资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceDelete(self):
        """是否删除 1:已删除 0:未删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceDelete

    @ResourceDelete.setter
    def ResourceDelete(self, ResourceDelete):
        self._ResourceDelete = ResourceDelete

    @property
    def ResourceCreateTime(self):
        """资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceZone(self):
        """可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def ComplianceResult(self):
        """合规状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def ResourceOwnerId(self):
        """资源所属用户ID
        :rtype: int
        """
        return self._ResourceOwnerId

    @ResourceOwnerId.setter
    def ResourceOwnerId(self, ResourceOwnerId):
        self._ResourceOwnerId = ResourceOwnerId

    @property
    def ResourceOwnerName(self):
        """用户昵称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceOwnerName

    @ResourceOwnerName.setter
    def ResourceOwnerName(self, ResourceOwnerName):
        self._ResourceOwnerName = ResourceOwnerName


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceStatus = params.get("ResourceStatus")
        self._ResourceDelete = params.get("ResourceDelete")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ResourceZone = params.get("ResourceZone")
        self._ComplianceResult = params.get("ComplianceResult")
        self._ResourceOwnerId = params.get("ResourceOwnerId")
        self._ResourceOwnerName = params.get("ResourceOwnerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """资源当前实际配置。长度为0~256位字符，即资源不合规配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def DesiredValue(self):
        """资源期望配置。长度为0~256位字符，即资源合规配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DesiredValue

    @DesiredValue.setter
    def DesiredValue(self, DesiredValue):
        self._DesiredValue = DesiredValue

    @property
    def Operator(self):
        """资源当前配置和期望配置之间的比较运算符。长度为0~16位字符，自定义规则上报评估结果此字段可能为空
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Property(self):
        """当前配置在资源属性结构体中的JSON路径。长度为0~256位字符，自定义规则上报评估结果此字段可能为空
        :rtype: str
        """
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
        :param _CompliancePackName: 合规包名称
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
        """规则标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def RuleName(self):
        """规则名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        """规则参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def SourceCondition(self):
        """规则触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SourceConditionForManage
        """
        return self._SourceCondition

    @SourceCondition.setter
    def SourceCondition(self, SourceCondition):
        self._SourceCondition = SourceCondition

    @property
    def ResourceType(self):
        """规则支持的资源类型，规则仅对指定资源类型的资源生效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Labels(self):
        """规则所属标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RiskLevel(self):
        """规则风险等级
1:低风险
2:中风险
3:高风险
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ServiceFunction(self):
        """规则对应的函数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceFunction

    @ServiceFunction.setter
    def ServiceFunction(self, ServiceFunction):
        self._ServiceFunction = ServiceFunction

    @property
    def CreateTime(self):
        """创建时间
格式：YYYY-MM-DD h:i:s
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        """规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        """ACTIVE：启用
NO_ACTIVE：停止
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ComplianceResult(self):
        """合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
无法应用规则： 'NOT_APPLICABLE'
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def Annotation(self):
        """["",""]
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation

    @property
    def ConfigRuleInvokedTime(self):
        """规则评估时间
格式：YYYY-MM-DD h:i:s

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigRuleInvokedTime

    @ConfigRuleInvokedTime.setter
    def ConfigRuleInvokedTime(self, ConfigRuleInvokedTime):
        self._ConfigRuleInvokedTime = ConfigRuleInvokedTime

    @property
    def ConfigRuleId(self):
        """规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def IdentifierType(self):
        """CUSTOMIZE：自定义规则、
SYSTEM：托管规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType

    @property
    def CompliancePackId(self):
        """合规包ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def TriggerType(self):
        """触发类型
ScheduledNotification：周期触发、
ConfigurationItemChangeNotification：变更触发
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def ManageInputParameter(self):
        """参数详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InputParameterForManage
        """
        return self._ManageInputParameter

    @ManageInputParameter.setter
    def ManageInputParameter(self, ManageInputParameter):
        self._ManageInputParameter = ManageInputParameter

    @property
    def CompliancePackName(self):
        """合规包名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RegionsScope(self):
        """关联地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RegionsScope

    @RegionsScope.setter
    def RegionsScope(self, RegionsScope):
        self._RegionsScope = RegionsScope

    @property
    def TagsScope(self):
        """关联标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        """ 规则对指定资源ID无效，即不对该资源执行评估。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope

    @property
    def AccountGroupId(self):
        """账号组ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountGroupName(self):
        """账号组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def RuleOwnerId(self):
        """规则所属用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RuleOwnerId

    @RuleOwnerId.setter
    def RuleOwnerId(self, RuleOwnerId):
        self._RuleOwnerId = RuleOwnerId

    @property
    def ManageTriggerType(self):
        """预设规则支持的触发方式
ScheduledNotification：周期触发
ConfigurationItemChangeNotification：变更触发
        :rtype: list of str
        """
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
        


class DescribeAggregateDiscoveredResourceRequest(AbstractModel):
    """DescribeAggregateDiscoveredResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _ResourceOwnerId: 资源所属用户ID
        :type ResourceOwnerId: int
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceRegion = None
        self._AccountGroupId = None
        self._ResourceOwnerId = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        """资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def AccountGroupId(self):
        """账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def ResourceOwnerId(self):
        """资源所属用户ID
        :rtype: int
        """
        return self._ResourceOwnerId

    @ResourceOwnerId.setter
    def ResourceOwnerId(self, ResourceOwnerId):
        self._ResourceOwnerId = ResourceOwnerId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._AccountGroupId = params.get("AccountGroupId")
        self._ResourceOwnerId = params.get("ResourceOwnerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggregateDiscoveredResourceResponse(AbstractModel):
    """DescribeAggregateDiscoveredResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ResourceName: 资源名
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _ResourceRegion: 资源地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param _ResourceZone: 资源可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceZone: str
        :param _Configuration: 资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: str
        :param _ResourceCreateTime: 资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCreateTime: str
        :param _Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _UpdateTime: 资源更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceRegion = None
        self._ResourceZone = None
        self._Configuration = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def ResourceId(self):
        """资源Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceRegion(self):
        """资源地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceZone(self):
        """资源可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def Configuration(self):
        """资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ResourceCreateTime(self):
        """资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpdateTime(self):
        """资源更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceZone = params.get("ResourceZone")
        self._Configuration = params.get("Configuration")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeDiscoveredResourceRequest(AbstractModel):
    """DescribeDiscoveredResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceRegion = None

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        """资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiscoveredResourceResponse(AbstractModel):
    """DescribeDiscoveredResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ResourceName: 资源名
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _ResourceRegion: 资源地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param _ResourceZone: 资源可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceZone: str
        :param _Configuration: 资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: str
        :param _ResourceCreateTime: 资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCreateTime: str
        :param _Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _UpdateTime: 资源更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceRegion = None
        self._ResourceZone = None
        self._Configuration = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def ResourceId(self):
        """资源Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        """资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceRegion(self):
        """资源地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceZone(self):
        """资源可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def Configuration(self):
        """资源配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ResourceCreateTime(self):
        """资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpdateTime(self):
        """资源更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceZone = params.get("ResourceZone")
        self._Configuration = params.get("Configuration")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class Evaluation(AbstractModel):
    """自定义规则评估结果

    """

    def __init__(self):
        r"""
        :param _ComplianceResourceId: 已评估资源ID。长度为0~256个字符
        :type ComplianceResourceId: str
        :param _ComplianceResourceType: 已评估资源类型。
支持:
QCS::CVM::Instance、 QCS::CBS::Disk、QCS::VPC::Vpc、QCS::VPC::Subnet、QCS::VPC::SecurityGroup、 QCS::CAM::User、QCS::CAM::Group、QCS::CAM::Policy、QCS::CAM::Role、QCS::COS::Bucket
        :type ComplianceResourceType: str
        :param _ComplianceRegion: 已评估资源地域。
长度为0~32个字符
        :type ComplianceRegion: str
        :param _ComplianceType: 合规类型。取值：
COMPLIANT：合规、
NON_COMPLIANT：不合规
        :type ComplianceType: str
        :param _Annotation: 不合规资源的补充信息。
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        self._ComplianceResourceId = None
        self._ComplianceResourceType = None
        self._ComplianceRegion = None
        self._ComplianceType = None
        self._Annotation = None

    @property
    def ComplianceResourceId(self):
        """已评估资源ID。长度为0~256个字符
        :rtype: str
        """
        return self._ComplianceResourceId

    @ComplianceResourceId.setter
    def ComplianceResourceId(self, ComplianceResourceId):
        self._ComplianceResourceId = ComplianceResourceId

    @property
    def ComplianceResourceType(self):
        """已评估资源类型。
支持:
QCS::CVM::Instance、 QCS::CBS::Disk、QCS::VPC::Vpc、QCS::VPC::Subnet、QCS::VPC::SecurityGroup、 QCS::CAM::User、QCS::CAM::Group、QCS::CAM::Policy、QCS::CAM::Role、QCS::COS::Bucket
        :rtype: str
        """
        return self._ComplianceResourceType

    @ComplianceResourceType.setter
    def ComplianceResourceType(self, ComplianceResourceType):
        self._ComplianceResourceType = ComplianceResourceType

    @property
    def ComplianceRegion(self):
        """已评估资源地域。
长度为0~32个字符
        :rtype: str
        """
        return self._ComplianceRegion

    @ComplianceRegion.setter
    def ComplianceRegion(self, ComplianceRegion):
        self._ComplianceRegion = ComplianceRegion

    @property
    def ComplianceType(self):
        """合规类型。取值：
COMPLIANT：合规、
NON_COMPLIANT：不合规
        :rtype: str
        """
        return self._ComplianceType

    @ComplianceType.setter
    def ComplianceType(self, ComplianceType):
        self._ComplianceType = ComplianceType

    @property
    def Annotation(self):
        """不合规资源的补充信息。
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation


    def _deserialize(self, params):
        self._ComplianceResourceId = params.get("ComplianceResourceId")
        self._ComplianceResourceType = params.get("ComplianceResourceType")
        self._ComplianceRegion = params.get("ComplianceRegion")
        self._ComplianceType = params.get("ComplianceType")
        if params.get("Annotation") is not None:
            self._Annotation = Annotation()
            self._Annotation._deserialize(params.get("Annotation"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """资源列表筛选

    """

    def __init__(self):
        r"""
        :param _Name: 查询字段名称 资源名称：resourceName  资源ID：resourceId 资源类型：resourceType 资源地域：resourceRegion    删除状态：resourceDelete 0未删除，1已删除  resourceRegionAndZone地域/可用区
        :type Name: str
        :param _Values: 查询字段值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """查询字段名称 资源名称：resourceName  资源ID：resourceId 资源类型：resourceType 资源地域：resourceRegion    删除状态：resourceDelete 0未删除，1已删除  resourceRegionAndZone地域/可用区
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """查询字段值
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
        """参数名
        :rtype: str
        """
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        """参数类型。必填类型：Require，可选类型：Optional。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """参数值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """值类型。数值：Integer， 字符串：String
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def ParameterKey(self):
        """参数Key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        """参数类型。必填类型：Require，可选类型：Optional。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        """默认值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Description(self):
        """描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """每页限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountGroupId(self):
        """账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def OrderType(self):
        """排序类型, 倒序：desc，顺序：asc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        """风险等级
1：高风险。
2：中风险。
3：低风险。
        :rtype: list of int non-negative
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        """规则状态
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        """评估结果
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        """规则名
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleOwnerId(self):
        """规则所属账号ID
        :rtype: int
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        """详情
        :rtype: list of ConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class ListAggregateDiscoveredResourcesRequest(AbstractModel):
    """ListAggregateDiscoveredResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxResults: 每页显示数量
        :type MaxResults: int
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _Filters: resourceName：资源名  resourceId ：资源ID resourceType：资源类型
        :type Filters: list of Filter
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _NextToken: 下一页token
        :type NextToken: str
        :param _OrderType: 排序方式 asc、desc
        :type OrderType: str
        """
        self._MaxResults = None
        self._AccountGroupId = None
        self._Filters = None
        self._Tags = None
        self._NextToken = None
        self._OrderType = None

    @property
    def MaxResults(self):
        """每页显示数量
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def AccountGroupId(self):
        """账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def Filters(self):
        """resourceName：资源名  resourceId ：资源ID resourceType：资源类型
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextToken(self):
        """下一页token
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OrderType(self):
        """排序方式 asc、desc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        self._AccountGroupId = params.get("AccountGroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NextToken = params.get("NextToken")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateDiscoveredResourcesResponse(AbstractModel):
    """ListAggregateDiscoveredResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 详情
        :type Items: list of AggregateResourceInfo
        :param _NextToken: 下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._NextToken = None
        self._RequestId = None

    @property
    def Items(self):
        """详情
        :rtype: list of AggregateResourceInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextToken(self):
        """下一页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AggregateResourceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class ListConfigRulesRequest(AbstractModel):
    """ListConfigRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页数量。
取值范围：1~200
        :type Limit: int
        :param _Offset: 偏移量。
取值范围：最小值为0
        :type Offset: int
        :param _OrderType: 排序类型(规则名称)。
倒序：desc，
顺序：asc
        :type OrderType: str
        :param _RiskLevel: 风险等级。
1：高风险，
2：中风险，
3：低风险。
        :type RiskLevel: list of int non-negative
        :param _State: 规则状态。
ACTIVE：启用
UN_ACTIVE：停用

        :type State: str
        :param _ComplianceResult: 评估结果。
COMPLIANT：合规
NON_COMPLIANT：不合规
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
        """每页数量。
取值范围：1~200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量。
取值范围：最小值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderType(self):
        """排序类型(规则名称)。
倒序：desc，
顺序：asc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        """风险等级。
1：高风险，
2：中风险，
3：低风险。
        :rtype: list of int non-negative
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        """规则状态。
ACTIVE：启用
UN_ACTIVE：停用

        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        """评估结果。
COMPLIANT：合规
NON_COMPLIANT：不合规
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        """规则名
        :rtype: str
        """
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        """详情
        :rtype: list of ConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class ListDiscoveredResourcesRequest(AbstractModel):
    """ListDiscoveredResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxResults: 每页显示数量
        :type MaxResults: int
        :param _Filters: resourceName：资源名  resourceId ：资源ID
        :type Filters: list of Filter
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _NextToken: 下一页token
        :type NextToken: str
        :param _OrderType: 排序方式 asc、desc
        :type OrderType: str
        """
        self._MaxResults = None
        self._Filters = None
        self._Tags = None
        self._NextToken = None
        self._OrderType = None

    @property
    def MaxResults(self):
        """每页显示数量
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Filters(self):
        """resourceName：资源名  resourceId ：资源ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextToken(self):
        """下一页token
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OrderType(self):
        """排序方式 asc、desc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NextToken = params.get("NextToken")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDiscoveredResourcesResponse(AbstractModel):
    """ListDiscoveredResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 详情
        :type Items: list of ResourceListInfo
        :param _NextToken: 下一页
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._NextToken = None
        self._RequestId = None

    @property
    def Items(self):
        """详情
        :rtype: list of ResourceListInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextToken(self):
        """下一页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceListInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class PutEvaluationsRequest(AbstractModel):
    """PutEvaluations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultToken: 回调令牌。从自定义规则所选的scf云函数入参中取参数ResultToken值
<a href="https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E" target="_blank">云函数入参说明</a>
        :type ResultToken: str
        :param _Evaluations: 自定义规则评估结果信息。
        :type Evaluations: list of Evaluation
        """
        self._ResultToken = None
        self._Evaluations = None

    @property
    def ResultToken(self):
        """回调令牌。从自定义规则所选的scf云函数入参中取参数ResultToken值
<a href="https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E" target="_blank">云函数入参说明</a>
        :rtype: str
        """
        return self._ResultToken

    @ResultToken.setter
    def ResultToken(self, ResultToken):
        self._ResultToken = ResultToken

    @property
    def Evaluations(self):
        """自定义规则评估结果信息。
        :rtype: list of Evaluation
        """
        return self._Evaluations

    @Evaluations.setter
    def Evaluations(self, Evaluations):
        self._Evaluations = Evaluations


    def _deserialize(self, params):
        self._ResultToken = params.get("ResultToken")
        if params.get("Evaluations") is not None:
            self._Evaluations = []
            for item in params.get("Evaluations"):
                obj = Evaluation()
                obj._deserialize(item)
                self._Evaluations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutEvaluationsResponse(AbstractModel):
    """PutEvaluations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ResourceListInfo(AbstractModel):
    """资源列列表信息

    """

    def __init__(self):
        r"""
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _ResourceRegion: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param _ResourceStatus: 资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceStatus: str
        :param _ResourceDelete: 1 :已删除 2：未删除
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceDelete: int
        :param _ResourceCreateTime: 资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceCreateTime: str
        :param _Tags: 标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _ResourceZone: 可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceZone: str
        :param _ComplianceResult: 合规状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceResult: str
        """
        self._ResourceType = None
        self._ResourceName = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ResourceStatus = None
        self._ResourceDelete = None
        self._ResourceCreateTime = None
        self._Tags = None
        self._ResourceZone = None
        self._ComplianceResult = None

    @property
    def ResourceType(self):
        """资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        """资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        """资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceStatus(self):
        """资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceDelete(self):
        """1 :已删除 2：未删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceDelete

    @ResourceDelete.setter
    def ResourceDelete(self, ResourceDelete):
        self._ResourceDelete = ResourceDelete

    @property
    def ResourceCreateTime(self):
        """资源创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        """标签信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceZone(self):
        """可用区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def ComplianceResult(self):
        """合规状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._ResourceName = params.get("ResourceName")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceStatus = params.get("ResourceStatus")
        self._ResourceDelete = params.get("ResourceDelete")
        self._ResourceCreateTime = params.get("ResourceCreateTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ResourceZone = params.get("ResourceZone")
        self._ComplianceResult = params.get("ComplianceResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """条件为空，合规：COMPLIANT，不合规：NON_COMPLIANT，无法应用：NOT_APPLICABLE
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EmptyAs

    @EmptyAs.setter
    def EmptyAs(self, EmptyAs):
        self._EmptyAs = EmptyAs

    @property
    def SelectPath(self):
        """配置路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SelectPath

    @SelectPath.setter
    def SelectPath(self, SelectPath):
        self._SelectPath = SelectPath

    @property
    def Operator(self):
        """操作运算符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Required(self):
        """是否必须
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DesiredValue(self):
        """期望值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """标签key
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签value
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        """触发类型
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def MaximumExecutionFrequency(self):
        """触发时间周期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        