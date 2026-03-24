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


class AddAggregateCompliancePackRequest(AbstractModel):
    r"""AddAggregateCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigRules: <p>合规包规则</p>
        :type ConfigRules: list of CompliancePackRule
        :param _RiskLevel: <p>风险等级<br>1：高风险。<br>2：中风险。<br>3：低风险。</p>
        :type RiskLevel: int
        :param _CompliancePackName: <p>合规包名称</p>
        :type CompliancePackName: str
        :param _AccountGroupId: <p>账号组ID</p>
        :type AccountGroupId: str
        :param _Description: <p>描述</p>
        :type Description: str
        """
        self._ConfigRules = None
        self._RiskLevel = None
        self._CompliancePackName = None
        self._AccountGroupId = None
        self._Description = None

    @property
    def ConfigRules(self):
        r"""<p>合规包规则</p>
        :rtype: list of CompliancePackRule
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

    @property
    def RiskLevel(self):
        r"""<p>风险等级<br>1：高风险。<br>2：中风险。<br>3：低风险。</p>
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CompliancePackName(self):
        r"""<p>合规包名称</p>
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def AccountGroupId(self):
        r"""<p>账号组ID</p>
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def Description(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = CompliancePackRule()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._RiskLevel = params.get("RiskLevel")
        self._CompliancePackName = params.get("CompliancePackName")
        self._AccountGroupId = params.get("AccountGroupId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAggregateCompliancePackResponse(AbstractModel):
    r"""AddAggregateCompliancePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: <p>合规包Id</p>
        :type CompliancePackId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompliancePackId = None
        self._RequestId = None

    @property
    def CompliancePackId(self):
        r"""<p>合规包Id</p>
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

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
        self._CompliancePackId = params.get("CompliancePackId")
        self._RequestId = params.get("RequestId")


class AddAggregateConfigRuleRequest(AbstractModel):
    r"""AddAggregateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Identifier: 规则模板标识，预设规则模板为Identifier, 自定义规则为云函数arn（region:functionName）
        :type Identifier: str
        :param _IdentifierType: 规则模板类型，SYSTEM, CUSTOMIZE
        :type IdentifierType: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _ResourceType: 规则支持的资源
        :type ResourceType: list of str
        :param _TriggerType: 触发类型，最多支持两种
        :type TriggerType: list of TriggerType
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: int
        :param _AccountGroupId: 账号组Id
        :type AccountGroupId: str
        :param _InputParameter: 入参
        :type InputParameter: list of InputParameter
        :param _Description: 描述
        :type Description: str
        :param _RegionScope: 关联地域
        :type RegionScope: list of str
        :param _TagsScope: 关联标签
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope: 排除的资源ID
        :type ExcludeResourceIdsScope: list of str
        """
        self._Identifier = None
        self._IdentifierType = None
        self._RuleName = None
        self._ResourceType = None
        self._TriggerType = None
        self._RiskLevel = None
        self._AccountGroupId = None
        self._InputParameter = None
        self._Description = None
        self._RegionScope = None
        self._TagsScope = None
        self._ExcludeResourceIdsScope = None

    @property
    def Identifier(self):
        r"""规则模板标识，预设规则模板为Identifier, 自定义规则为云函数arn（region:functionName）
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def IdentifierType(self):
        r"""规则模板类型，SYSTEM, CUSTOMIZE
        :rtype: str
        """
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def ResourceType(self):
        r"""规则支持的资源
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def TriggerType(self):
        r"""触发类型，最多支持两种
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def RiskLevel(self):
        r"""风险等级
1：高风险。
2：中风险。
3：低风险。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def AccountGroupId(self):
        r"""账号组Id
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def InputParameter(self):
        r"""入参
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RegionScope(self):
        r"""关联地域
        :rtype: list of str
        """
        return self._RegionScope

    @RegionScope.setter
    def RegionScope(self, RegionScope):
        self._RegionScope = RegionScope

    @property
    def TagsScope(self):
        r"""关联标签
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        r"""排除的资源ID
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._IdentifierType = params.get("IdentifierType")
        self._RuleName = params.get("RuleName")
        self._ResourceType = params.get("ResourceType")
        if params.get("TriggerType") is not None:
            self._TriggerType = []
            for item in params.get("TriggerType"):
                obj = TriggerType()
                obj._deserialize(item)
                self._TriggerType.append(obj)
        self._RiskLevel = params.get("RiskLevel")
        self._AccountGroupId = params.get("AccountGroupId")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        self._Description = params.get("Description")
        self._RegionScope = params.get("RegionScope")
        if params.get("TagsScope") is not None:
            self._TagsScope = []
            for item in params.get("TagsScope"):
                obj = Tag()
                obj._deserialize(item)
                self._TagsScope.append(obj)
        self._ExcludeResourceIdsScope = params.get("ExcludeResourceIdsScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddAggregateConfigRuleResponse(AbstractModel):
    r"""AddAggregateConfigRule返回参数结构体

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


class AddCompliancePackRequest(AbstractModel):
    r"""AddCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigRules: <p>合规包规则</p>
        :type ConfigRules: list of CompliancePackRule
        :param _RiskLevel: <p>风险等级<br>1：高风险。<br>2：中风险。<br>3：低风险。</p>
        :type RiskLevel: int
        :param _CompliancePackName: <p>合规包名称</p>
        :type CompliancePackName: str
        :param _Description: <p>描述</p>
        :type Description: str
        """
        self._ConfigRules = None
        self._RiskLevel = None
        self._CompliancePackName = None
        self._Description = None

    @property
    def ConfigRules(self):
        r"""<p>合规包规则</p>
        :rtype: list of CompliancePackRule
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

    @property
    def RiskLevel(self):
        r"""<p>风险等级<br>1：高风险。<br>2：中风险。<br>3：低风险。</p>
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CompliancePackName(self):
        r"""<p>合规包名称</p>
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def Description(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = CompliancePackRule()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._RiskLevel = params.get("RiskLevel")
        self._CompliancePackName = params.get("CompliancePackName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCompliancePackResponse(AbstractModel):
    r"""AddCompliancePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: <p>合规包Id</p>
        :type CompliancePackId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompliancePackId = None
        self._RequestId = None

    @property
    def CompliancePackId(self):
        r"""<p>合规包Id</p>
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

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
        self._CompliancePackId = params.get("CompliancePackId")
        self._RequestId = params.get("RequestId")


class AddConfigRuleRequest(AbstractModel):
    r"""AddConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Identifier: 规则模板标识，预设规则模板为Identifier, 自定义规则为云函数arn（region:functionName）
        :type Identifier: str
        :param _IdentifierType: 规则模板类型，SYSTEM, CUSTOMIZE
        :type IdentifierType: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _ResourceType: 规则支持的资源
        :type ResourceType: list of str
        :param _TriggerType: 触发类型，最多支持两种
        :type TriggerType: list of TriggerType
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: int
        :param _InputParameter: 入参
        :type InputParameter: list of InputParameter
        :param _Description: 规则描述。长度范围0~1024字符
        :type Description: str
        :param _RegionsScope: 规则评估地域范围，规则仅对指定地域中的资源生效。
支持的地域范围config:ListResourceRegions返回的地域
        :type RegionsScope: list of str
        :param _TagsScope: 规则评估标签范围，规则仅对绑定指定标签的资源生效。
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope: 规则对指定资源ID无效，即不对该资源执行评估。
        :type ExcludeResourceIdsScope: list of str
        """
        self._Identifier = None
        self._IdentifierType = None
        self._RuleName = None
        self._ResourceType = None
        self._TriggerType = None
        self._RiskLevel = None
        self._InputParameter = None
        self._Description = None
        self._RegionsScope = None
        self._TagsScope = None
        self._ExcludeResourceIdsScope = None

    @property
    def Identifier(self):
        r"""规则模板标识，预设规则模板为Identifier, 自定义规则为云函数arn（region:functionName）
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def IdentifierType(self):
        r"""规则模板类型，SYSTEM, CUSTOMIZE
        :rtype: str
        """
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def ResourceType(self):
        r"""规则支持的资源
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def TriggerType(self):
        r"""触发类型，最多支持两种
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def RiskLevel(self):
        r"""风险等级
1：高风险。
2：中风险。
3：低风险。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def InputParameter(self):
        r"""入参
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def Description(self):
        r"""规则描述。长度范围0~1024字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RegionsScope(self):
        r"""规则评估地域范围，规则仅对指定地域中的资源生效。
支持的地域范围config:ListResourceRegions返回的地域
        :rtype: list of str
        """
        return self._RegionsScope

    @RegionsScope.setter
    def RegionsScope(self, RegionsScope):
        self._RegionsScope = RegionsScope

    @property
    def TagsScope(self):
        r"""规则评估标签范围，规则仅对绑定指定标签的资源生效。
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        r"""规则对指定资源ID无效，即不对该资源执行评估。
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._IdentifierType = params.get("IdentifierType")
        self._RuleName = params.get("RuleName")
        self._ResourceType = params.get("ResourceType")
        if params.get("TriggerType") is not None:
            self._TriggerType = []
            for item in params.get("TriggerType"):
                obj = TriggerType()
                obj._deserialize(item)
                self._TriggerType.append(obj)
        self._RiskLevel = params.get("RiskLevel")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        self._Description = params.get("Description")
        self._RegionsScope = params.get("RegionsScope")
        if params.get("TagsScope") is not None:
            self._TagsScope = []
            for item in params.get("TagsScope"):
                obj = Tag()
                obj._deserialize(item)
                self._TagsScope.append(obj)
        self._ExcludeResourceIdsScope = params.get("ExcludeResourceIdsScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddConfigRuleResponse(AbstractModel):
    r"""AddConfigRule返回参数结构体

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


class AggregateEvaluationResult(AbstractModel):
    r"""评估结果

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _ResourceName: 资源名称
        :type ResourceName: str
        :param _ConfigRuleId: 规则id
        :type ConfigRuleId: str
        :param _ConfigRuleName: 规则名称
        :type ConfigRuleName: str
        :param _CompliancePackId: 合规包id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompliancePackId: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _Annotation: 评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        :param _ComplianceType: 合规类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceType: str
        :param _InvokingEventMessageType: 规则发起类型
        :type InvokingEventMessageType: str
        :param _ConfigRuleInvokedTime: 评估发起时间
        :type ConfigRuleInvokedTime: str
        :param _ResultRecordedTime: 评估实际时间
        :type ResultRecordedTime: str
        :param _ResourceOwnerId: 资源所属用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceOwnerId: int
        :param _ResourceOwnerName: 资源所属用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceOwnerName: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceRegion = None
        self._ResourceName = None
        self._ConfigRuleId = None
        self._ConfigRuleName = None
        self._CompliancePackId = None
        self._RiskLevel = None
        self._Annotation = None
        self._ComplianceType = None
        self._InvokingEventMessageType = None
        self._ConfigRuleInvokedTime = None
        self._ResultRecordedTime = None
        self._ResourceOwnerId = None
        self._ResourceOwnerName = None

    @property
    def ResourceId(self):
        r"""资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        r"""资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceName(self):
        r"""资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ConfigRuleId(self):
        r"""规则id
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def ConfigRuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._ConfigRuleName

    @ConfigRuleName.setter
    def ConfigRuleName(self, ConfigRuleName):
        self._ConfigRuleName = ConfigRuleName

    @property
    def CompliancePackId(self):
        r"""合规包id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def Annotation(self):
        r"""评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation

    @property
    def ComplianceType(self):
        r"""合规类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceType

    @ComplianceType.setter
    def ComplianceType(self, ComplianceType):
        self._ComplianceType = ComplianceType

    @property
    def InvokingEventMessageType(self):
        r"""规则发起类型
        :rtype: str
        """
        return self._InvokingEventMessageType

    @InvokingEventMessageType.setter
    def InvokingEventMessageType(self, InvokingEventMessageType):
        self._InvokingEventMessageType = InvokingEventMessageType

    @property
    def ConfigRuleInvokedTime(self):
        r"""评估发起时间
        :rtype: str
        """
        return self._ConfigRuleInvokedTime

    @ConfigRuleInvokedTime.setter
    def ConfigRuleInvokedTime(self, ConfigRuleInvokedTime):
        self._ConfigRuleInvokedTime = ConfigRuleInvokedTime

    @property
    def ResultRecordedTime(self):
        r"""评估实际时间
        :rtype: str
        """
        return self._ResultRecordedTime

    @ResultRecordedTime.setter
    def ResultRecordedTime(self, ResultRecordedTime):
        self._ResultRecordedTime = ResultRecordedTime

    @property
    def ResourceOwnerId(self):
        r"""资源所属用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ResourceOwnerId

    @ResourceOwnerId.setter
    def ResourceOwnerId(self, ResourceOwnerId):
        self._ResourceOwnerId = ResourceOwnerId

    @property
    def ResourceOwnerName(self):
        r"""资源所属用户名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceOwnerName

    @ResourceOwnerName.setter
    def ResourceOwnerName(self, ResourceOwnerName):
        self._ResourceOwnerName = ResourceOwnerName


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceName = params.get("ResourceName")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._ConfigRuleName = params.get("ConfigRuleName")
        self._CompliancePackId = params.get("CompliancePackId")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("Annotation") is not None:
            self._Annotation = Annotation()
            self._Annotation._deserialize(params.get("Annotation"))
        self._ComplianceType = params.get("ComplianceType")
        self._InvokingEventMessageType = params.get("InvokingEventMessageType")
        self._ConfigRuleInvokedTime = params.get("ConfigRuleInvokedTime")
        self._ResultRecordedTime = params.get("ResultRecordedTime")
        self._ResourceOwnerId = params.get("ResourceOwnerId")
        self._ResourceOwnerName = params.get("ResourceOwnerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AggregateResourceInfo(AbstractModel):
    r"""资源列列表信息

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
        :type ResourceRegion: str
        :param _ResourceStatus: 资源状态
        :type ResourceStatus: str
        :param _ResourceDelete: 是否删除 1:已删除 0:未删除
        :type ResourceDelete: int
        :param _ResourceCreateTime: 资源创建时间
        :type ResourceCreateTime: str
        :param _Tags: 标签信息
        :type Tags: list of Tag
        :param _ResourceZone: 可用区
        :type ResourceZone: str
        :param _ComplianceResult: 合规状态
        :type ComplianceResult: str
        :param _ResourceOwnerId: 资源所属用户ID
        :type ResourceOwnerId: int
        :param _ResourceOwnerName: 用户昵称
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
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        r"""资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        r"""地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceStatus(self):
        r"""资源状态
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceDelete(self):
        r"""是否删除 1:已删除 0:未删除
        :rtype: int
        """
        return self._ResourceDelete

    @ResourceDelete.setter
    def ResourceDelete(self, ResourceDelete):
        self._ResourceDelete = ResourceDelete

    @property
    def ResourceCreateTime(self):
        r"""资源创建时间
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        r"""标签信息
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceZone(self):
        r"""可用区
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def ComplianceResult(self):
        r"""合规状态
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def ResourceOwnerId(self):
        r"""资源所属用户ID
        :rtype: int
        """
        return self._ResourceOwnerId

    @ResourceOwnerId.setter
    def ResourceOwnerId(self, ResourceOwnerId):
        self._ResourceOwnerId = ResourceOwnerId

    @property
    def ResourceOwnerName(self):
        r"""用户昵称
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
        


class Aggregator(AbstractModel):
    r"""用户组列表信息

    """

    def __init__(self):
        r"""
        :param _Name: 账号组名称
        :type Name: str
        :param _Description: 账号组描述
        :type Description: str
        :param _OwnerUin: 创建者用户ID
        :type OwnerUin: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _AccountCount: 账号组成员数量
        :type AccountCount: int
        :param _Type: RD:全局账号组
        :type Type: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _AggregatorStatus: 账号组状态
        :type AggregatorStatus: int
        :param _MemberName: 账号组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        """
        self._Name = None
        self._Description = None
        self._OwnerUin = None
        self._CreateTime = None
        self._AccountCount = None
        self._Type = None
        self._AccountGroupId = None
        self._AggregatorStatus = None
        self._MemberName = None

    @property
    def Name(self):
        r"""账号组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""账号组描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OwnerUin(self):
        r"""创建者用户ID
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

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
    def AccountCount(self):
        r"""账号组成员数量
        :rtype: int
        """
        return self._AccountCount

    @AccountCount.setter
    def AccountCount(self, AccountCount):
        self._AccountCount = AccountCount

    @property
    def Type(self):
        r"""RD:全局账号组
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AggregatorStatus(self):
        r"""账号组状态
        :rtype: int
        """
        return self._AggregatorStatus

    @AggregatorStatus.setter
    def AggregatorStatus(self, AggregatorStatus):
        self._AggregatorStatus = AggregatorStatus

    @property
    def MemberName(self):
        r"""账号组名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._OwnerUin = params.get("OwnerUin")
        self._CreateTime = params.get("CreateTime")
        self._AccountCount = params.get("AccountCount")
        self._Type = params.get("Type")
        self._AccountGroupId = params.get("AccountGroupId")
        self._AggregatorStatus = params.get("AggregatorStatus")
        self._MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AggregatorAccount(AbstractModel):
    r"""成员信息

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员ID
        :type MemberUin: int
        :param _MemberName: 成员名称
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        """
        self._MemberUin = None
        self._MemberName = None

    @property
    def MemberUin(self):
        r"""成员ID
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""成员名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Annotation(AbstractModel):
    r"""合规详情

    """

    def __init__(self):
        r"""
        :param _Configuration: 资源当前实际配置。长度为0~256位字符，即资源不合规配置
        :type Configuration: str
        :param _DesiredValue: 资源期望配置。长度为0~256位字符，即资源合规配置
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
        r"""资源当前实际配置。长度为0~256位字符，即资源不合规配置
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def DesiredValue(self):
        r"""资源期望配置。长度为0~256位字符，即资源合规配置
        :rtype: str
        """
        return self._DesiredValue

    @DesiredValue.setter
    def DesiredValue(self, DesiredValue):
        self._DesiredValue = DesiredValue

    @property
    def Operator(self):
        r"""资源当前配置和期望配置之间的比较运算符。长度为0~16位字符，自定义规则上报评估结果此字段可能为空
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Property(self):
        r"""当前配置在资源属性结构体中的JSON路径。长度为0~256位字符，自定义规则上报评估结果此字段可能为空
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
        


class CloseAggregateConfigRuleRequest(AbstractModel):
    r"""CloseAggregateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AccountGroupId: 账号组Id
        :type AccountGroupId: str
        """
        self._RuleId = None
        self._AccountGroupId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccountGroupId(self):
        r"""账号组Id
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAggregateConfigRuleResponse(AbstractModel):
    r"""CloseAggregateConfigRule返回参数结构体

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


class CloseConfigRecorderRequest(AbstractModel):
    r"""CloseConfigRecorder请求参数结构体

    """


class CloseConfigRecorderResponse(AbstractModel):
    r"""CloseConfigRecorder返回参数结构体

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


class CloseConfigRuleRequest(AbstractModel):
    r"""CloseConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseConfigRuleResponse(AbstractModel):
    r"""CloseConfigRule返回参数结构体

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


class ComplianceConfigRule(AbstractModel):
    r"""合规包规则信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param _Status: 规则状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ConfigRuleId: 规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRuleId: str
        :param _ComplianceResult: 评估结果
合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceResult: str
        :param _Labels: 关键字
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of str
        :param _InputParameter: 入参
注意：此字段可能返回 null，表示取不到有效值。
        :type InputParameter: list of InputParameter
        :param _SourceCondition: 参数格式
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCondition: list of SourceConditionForManage
        :param _Identifier: 规则标识
注意：此字段可能返回 null，表示取不到有效值。
        :type Identifier: str
        :param _CreateByType: 创建方式 user、compliancePack、system
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateByType: str
        :param _Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ManageInputParameter: 参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ManageInputParameter: list of InputParameterForManage
        """
        self._RuleName = None
        self._RiskLevel = None
        self._Status = None
        self._ConfigRuleId = None
        self._ComplianceResult = None
        self._Labels = None
        self._InputParameter = None
        self._SourceCondition = None
        self._Identifier = None
        self._CreateByType = None
        self._Description = None
        self._ManageInputParameter = None

    @property
    def RuleName(self):
        r"""规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RiskLevel(self):
        r"""风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def Status(self):
        r"""规则状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ConfigRuleId(self):
        r"""规则ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def ComplianceResult(self):
        r"""评估结果
合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def Labels(self):
        r"""关键字
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def InputParameter(self):
        r"""入参
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def SourceCondition(self):
        r"""参数格式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SourceConditionForManage
        """
        return self._SourceCondition

    @SourceCondition.setter
    def SourceCondition(self, SourceCondition):
        self._SourceCondition = SourceCondition

    @property
    def Identifier(self):
        r"""规则标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def CreateByType(self):
        r"""创建方式 user、compliancePack、system
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateByType

    @CreateByType.setter
    def CreateByType(self, CreateByType):
        self._CreateByType = CreateByType

    @property
    def Description(self):
        r"""规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ManageInputParameter(self):
        r"""参数描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InputParameterForManage
        """
        return self._ManageInputParameter

    @ManageInputParameter.setter
    def ManageInputParameter(self, ManageInputParameter):
        self._ManageInputParameter = ManageInputParameter


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._RiskLevel = params.get("RiskLevel")
        self._Status = params.get("Status")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._ComplianceResult = params.get("ComplianceResult")
        self._Labels = params.get("Labels")
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
        self._Identifier = params.get("Identifier")
        self._CreateByType = params.get("CreateByType")
        self._Description = params.get("Description")
        if params.get("ManageInputParameter") is not None:
            self._ManageInputParameter = []
            for item in params.get("ManageInputParameter"):
                obj = InputParameterForManage()
                obj._deserialize(item)
                self._ManageInputParameter.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePackRule(AbstractModel):
    r"""合规包规则信息

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _InputParameter: 入参
        :type InputParameter: list of InputParameter
        :param _Identifier: 规则身份标识
        :type Identifier: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ManagedRuleIdentifier: 预设规则身份标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagedRuleIdentifier: str
        :param _ConfigRuleId: 规则ID
        :type ConfigRuleId: str
        :param _CompliancePackId: 合规包ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CompliancePackId: str
        """
        self._RuleName = None
        self._RiskLevel = None
        self._InputParameter = None
        self._Identifier = None
        self._Description = None
        self._ManagedRuleIdentifier = None
        self._ConfigRuleId = None
        self._CompliancePackId = None

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def InputParameter(self):
        r"""入参
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def Identifier(self):
        r"""规则身份标识
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ManagedRuleIdentifier(self):
        r"""预设规则身份标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ManagedRuleIdentifier

    @ManagedRuleIdentifier.setter
    def ManagedRuleIdentifier(self, ManagedRuleIdentifier):
        self._ManagedRuleIdentifier = ManagedRuleIdentifier

    @property
    def ConfigRuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def CompliancePackId(self):
        r"""合规包ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        self._Identifier = params.get("Identifier")
        self._Description = params.get("Description")
        self._ManagedRuleIdentifier = params.get("ManagedRuleIdentifier")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePackRuleForManage(AbstractModel):
    r"""管理端系统合规包规则

    """

    def __init__(self):
        r"""
        :param _Identifier: <p>规则唯一身份标识</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Identifier: str
        :param _RuleName: <p>规则名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleName: str
        :param _Description: <p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RiskLevel: <p>风险等级</p><p>1：高风险 2：中风险  3：低风险</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param _CreateTime: <p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _CompliancePackRules: <p>合规包规则</p>
        :type CompliancePackRules: list of CompliancePackRules
        :param _Control: <p>规则编号信息</p>
        :type Control: list of Control
        :param _ResourceTypes: <p>资源类型</p>
        :type ResourceTypes: list of str
        """
        self._Identifier = None
        self._RuleName = None
        self._Description = None
        self._RiskLevel = None
        self._CreateTime = None
        self._UpdateTime = None
        self._CompliancePackRules = None
        self._Control = None
        self._ResourceTypes = None

    @property
    def Identifier(self):
        r"""<p>规则唯一身份标识</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def RuleName(self):
        r"""<p>规则名称</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Description(self):
        r"""<p>描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RiskLevel(self):
        r"""<p>风险等级</p><p>1：高风险 2：中风险  3：低风险</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CompliancePackRules(self):
        r"""<p>合规包规则</p>
        :rtype: list of CompliancePackRules
        """
        return self._CompliancePackRules

    @CompliancePackRules.setter
    def CompliancePackRules(self, CompliancePackRules):
        self._CompliancePackRules = CompliancePackRules

    @property
    def Control(self):
        r"""<p>规则编号信息</p>
        :rtype: list of Control
        """
        return self._Control

    @Control.setter
    def Control(self, Control):
        self._Control = Control

    @property
    def ResourceTypes(self):
        r"""<p>资源类型</p>
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._RuleName = params.get("RuleName")
        self._Description = params.get("Description")
        self._RiskLevel = params.get("RiskLevel")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("CompliancePackRules") is not None:
            self._CompliancePackRules = []
            for item in params.get("CompliancePackRules"):
                obj = CompliancePackRules()
                obj._deserialize(item)
                self._CompliancePackRules.append(obj)
        if params.get("Control") is not None:
            self._Control = []
            for item in params.get("Control"):
                obj = Control()
                obj._deserialize(item)
                self._Control.append(obj)
        self._ResourceTypes = params.get("ResourceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompliancePackRules(AbstractModel):
    r"""合规包规则信息

    """

    def __init__(self):
        r"""
        :param _Identifier: <p>规则标识</p>
        :type Identifier: str
        :param _Control: <p>规则编号信息</p>
        :type Control: list of Control
        :param _ResourceTypes: <p>资源类型</p>
        :type ResourceTypes: list of str
        """
        self._Identifier = None
        self._Control = None
        self._ResourceTypes = None

    @property
    def Identifier(self):
        r"""<p>规则标识</p>
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def Control(self):
        r"""<p>规则编号信息</p>
        :rtype: list of Control
        """
        return self._Control

    @Control.setter
    def Control(self, Control):
        self._Control = Control

    @property
    def ResourceTypes(self):
        r"""<p>资源类型</p>
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        if params.get("Control") is not None:
            self._Control = []
            for item in params.get("Control"):
                obj = Control()
                obj._deserialize(item)
                self._Control.append(obj)
        self._ResourceTypes = params.get("ResourceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigCompliancePack(AbstractModel):
    r"""用户合规包信息

    """

    def __init__(self):
        r"""
        :param _Status: 合规包状态
        :type Status: str
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _ComplianceResult: 评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceResult: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _NoCompliantNames: 不合规规则名
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCompliantNames: list of str
        :param _RuleCount: 合规包规则数
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCount: int
        """
        self._Status = None
        self._CompliancePackId = None
        self._Description = None
        self._CompliancePackName = None
        self._RiskLevel = None
        self._ComplianceResult = None
        self._CreateTime = None
        self._NoCompliantNames = None
        self._RuleCount = None

    @property
    def Status(self):
        r"""合规包状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ComplianceResult(self):
        r"""评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

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
    def NoCompliantNames(self):
        r"""不合规规则名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._NoCompliantNames

    @NoCompliantNames.setter
    def NoCompliantNames(self, NoCompliantNames):
        self._NoCompliantNames = NoCompliantNames

    @property
    def RuleCount(self):
        r"""合规包规则数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RuleCount

    @RuleCount.setter
    def RuleCount(self, RuleCount):
        self._RuleCount = RuleCount


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CompliancePackId = params.get("CompliancePackId")
        self._Description = params.get("Description")
        self._CompliancePackName = params.get("CompliancePackName")
        self._RiskLevel = params.get("RiskLevel")
        self._ComplianceResult = params.get("ComplianceResult")
        self._CreateTime = params.get("CreateTime")
        self._NoCompliantNames = params.get("NoCompliantNames")
        self._RuleCount = params.get("RuleCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigResource(AbstractModel):
    r"""资源类型信息

    """

    def __init__(self):
        r"""
        :param _Product: 产品
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _ProductName: 产品名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ResourceTypeName: 资源类型名
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTypeName: str
        """
        self._Product = None
        self._ProductName = None
        self._ResourceType = None
        self._ResourceTypeName = None

    @property
    def Product(self):
        r"""产品
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProductName(self):
        r"""产品名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ResourceType(self):
        r"""资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceTypeName(self):
        r"""资源类型名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceTypeName

    @ResourceTypeName.setter
    def ResourceTypeName(self, ResourceTypeName):
        self._ResourceTypeName = ResourceTypeName


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProductName = params.get("ProductName")
        self._ResourceType = params.get("ResourceType")
        self._ResourceTypeName = params.get("ResourceTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConfigRule(AbstractModel):
    r"""规则详情

    """

    def __init__(self):
        r"""
        :param _Identifier: 规则标识
        :type Identifier: str
        :param _RuleName: 规则名
        :type RuleName: str
        :param _InputParameter: 规则参数
        :type InputParameter: list of InputParameter
        :param _SourceCondition: 规则触发条件
        :type SourceCondition: list of SourceConditionForManage
        :param _ResourceType: 规则支持的资源类型，规则仅对指定资源类型的资源生效。
        :type ResourceType: list of str
        :param _Labels: 规则所属标签
        :type Labels: list of str
        :param _RiskLevel: 规则风险等级
1:低风险
2:中风险
3:高风险
        :type RiskLevel: int
        :param _ServiceFunction: 规则对应的函数
        :type ServiceFunction: str
        :param _CreateTime: 创建时间
格式：YYYY-MM-DD h:i:s
        :type CreateTime: str
        :param _Description: 规则描述
        :type Description: str
        :param _Status: ACTIVE：启用
NO_ACTIVE：停止
        :type Status: str
        :param _ComplianceResult: 合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
无法应用规则： 'NOT_APPLICABLE'
        :type ComplianceResult: str
        :param _Annotation: ["",""]
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        :param _ConfigRuleInvokedTime: 规则评估时间
格式：YYYY-MM-DD h:i:s

        :type ConfigRuleInvokedTime: str
        :param _ConfigRuleId: 规则ID
        :type ConfigRuleId: str
        :param _IdentifierType: CUSTOMIZE：自定义规则、
SYSTEM：托管规则
        :type IdentifierType: str
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _TriggerType: 触发类型
ScheduledNotification：周期触发、
ConfigurationItemChangeNotification：变更触发
        :type TriggerType: list of TriggerType
        :param _ManageInputParameter: 参数详情
        :type ManageInputParameter: list of InputParameterForManage
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _RegionsScope: 关联地域
        :type RegionsScope: list of str
        :param _TagsScope: 关联标签
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope:  规则对指定资源ID无效，即不对该资源执行评估。
        :type ExcludeResourceIdsScope: list of str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _AccountGroupName: 账号组名称
        :type AccountGroupName: str
        :param _RuleOwnerId: 规则所属用户ID
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
        r"""规则标识
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def RuleName(self):
        r"""规则名
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        r"""规则参数
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def SourceCondition(self):
        r"""规则触发条件
        :rtype: list of SourceConditionForManage
        """
        return self._SourceCondition

    @SourceCondition.setter
    def SourceCondition(self, SourceCondition):
        self._SourceCondition = SourceCondition

    @property
    def ResourceType(self):
        r"""规则支持的资源类型，规则仅对指定资源类型的资源生效。
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Labels(self):
        r"""规则所属标签
        :rtype: list of str
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels

    @property
    def RiskLevel(self):
        r"""规则风险等级
1:低风险
2:中风险
3:高风险
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ServiceFunction(self):
        r"""规则对应的函数
        :rtype: str
        """
        return self._ServiceFunction

    @ServiceFunction.setter
    def ServiceFunction(self, ServiceFunction):
        self._ServiceFunction = ServiceFunction

    @property
    def CreateTime(self):
        r"""创建时间
格式：YYYY-MM-DD h:i:s
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""ACTIVE：启用
NO_ACTIVE：停止
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ComplianceResult(self):
        r"""合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
无法应用规则： 'NOT_APPLICABLE'
        :rtype: str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def Annotation(self):
        r"""["",""]
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation

    @property
    def ConfigRuleInvokedTime(self):
        r"""规则评估时间
格式：YYYY-MM-DD h:i:s

        :rtype: str
        """
        return self._ConfigRuleInvokedTime

    @ConfigRuleInvokedTime.setter
    def ConfigRuleInvokedTime(self, ConfigRuleInvokedTime):
        self._ConfigRuleInvokedTime = ConfigRuleInvokedTime

    @property
    def ConfigRuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def IdentifierType(self):
        r"""CUSTOMIZE：自定义规则、
SYSTEM：托管规则
        :rtype: str
        """
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def TriggerType(self):
        r"""触发类型
ScheduledNotification：周期触发、
ConfigurationItemChangeNotification：变更触发
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def ManageInputParameter(self):
        r"""参数详情
        :rtype: list of InputParameterForManage
        """
        return self._ManageInputParameter

    @ManageInputParameter.setter
    def ManageInputParameter(self, ManageInputParameter):
        self._ManageInputParameter = ManageInputParameter

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RegionsScope(self):
        r"""关联地域
        :rtype: list of str
        """
        return self._RegionsScope

    @RegionsScope.setter
    def RegionsScope(self, RegionsScope):
        self._RegionsScope = RegionsScope

    @property
    def TagsScope(self):
        r"""关联标签
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        r""" 规则对指定资源ID无效，即不对该资源执行评估。
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def AccountGroupName(self):
        r"""账号组名称
        :rtype: str
        """
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def RuleOwnerId(self):
        r"""规则所属用户ID
        :rtype: int
        """
        return self._RuleOwnerId

    @RuleOwnerId.setter
    def RuleOwnerId(self, RuleOwnerId):
        self._RuleOwnerId = RuleOwnerId

    @property
    def ManageTriggerType(self):
        r"""预设规则支持的触发方式
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
        


class Control(AbstractModel):
    r"""规则编号信息

    """

    def __init__(self):
        r"""
        :param _Id: <p>规则编号</p>
        :type Id: str
        :param _Description: <p>编号描述</p>
        :type Description: str
        """
        self._Id = None
        self._Description = None

    @property
    def Id(self):
        r"""<p>规则编号</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        r"""<p>编号描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAggregatorRequest(AbstractModel):
    r"""CreateAggregator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>账号组名称</p>
        :type Name: str
        :param _Description: <p>账号组描述</p>
        :type Description: str
        :param _Type: <p>账号组类型 </p><p>枚举值：</p><ul><li>RD： 全局账号组</li><li>CUSTOM： 自定义账号组</li></ul>
        :type Type: str
        :param _AggregatorAccounts: <p>账号组成员信息列表，最多100个</p>
        :type AggregatorAccounts: list of AggregatorAccount
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._AggregatorAccounts = None

    @property
    def Name(self):
        r"""<p>账号组名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>账号组描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        r"""<p>账号组类型 </p><p>枚举值：</p><ul><li>RD： 全局账号组</li><li>CUSTOM： 自定义账号组</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AggregatorAccounts(self):
        r"""<p>账号组成员信息列表，最多100个</p>
        :rtype: list of AggregatorAccount
        """
        return self._AggregatorAccounts

    @AggregatorAccounts.setter
    def AggregatorAccounts(self, AggregatorAccounts):
        self._AggregatorAccounts = AggregatorAccounts


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        if params.get("AggregatorAccounts") is not None:
            self._AggregatorAccounts = []
            for item in params.get("AggregatorAccounts"):
                obj = AggregatorAccount()
                obj._deserialize(item)
                self._AggregatorAccounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAggregatorResponse(AbstractModel):
    r"""CreateAggregator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: <p>账号组Id</p>
        :type AccountGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountGroupId = None
        self._RequestId = None

    @property
    def AccountGroupId(self):
        r"""<p>账号组Id</p>
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

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
        self._AccountGroupId = params.get("AccountGroupId")
        self._RequestId = params.get("RequestId")


class CreateRemediationRequest(AbstractModel):
    r"""CreateRemediation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: <p>规则 ID</p>
        :type RuleId: str
        :param _RemediationType: <p>修正类型取值：   SCF：云函数（自定义修正）。</p>
        :type RemediationType: str
        :param _RemediationTemplateId: <p>修正模板 ID</p>
        :type RemediationTemplateId: str
        :param _InvokeType: <p>修正执行方式。<br>取值：   MANUAL_EXECUTION：手动执行</p>
        :type InvokeType: str
        :param _SourceType: <p>执行修正的模板来源<br>CUSTOM：自定义模板。</p>
        :type SourceType: str
        """
        self._RuleId = None
        self._RemediationType = None
        self._RemediationTemplateId = None
        self._InvokeType = None
        self._SourceType = None

    @property
    def RuleId(self):
        r"""<p>规则 ID</p>
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RemediationType(self):
        r"""<p>修正类型取值：   SCF：云函数（自定义修正）。</p>
        :rtype: str
        """
        return self._RemediationType

    @RemediationType.setter
    def RemediationType(self, RemediationType):
        self._RemediationType = RemediationType

    @property
    def RemediationTemplateId(self):
        r"""<p>修正模板 ID</p>
        :rtype: str
        """
        return self._RemediationTemplateId

    @RemediationTemplateId.setter
    def RemediationTemplateId(self, RemediationTemplateId):
        self._RemediationTemplateId = RemediationTemplateId

    @property
    def InvokeType(self):
        r"""<p>修正执行方式。<br>取值：   MANUAL_EXECUTION：手动执行</p>
        :rtype: str
        """
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def SourceType(self):
        r"""<p>执行修正的模板来源<br>CUSTOM：自定义模板。</p>
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._RemediationType = params.get("RemediationType")
        self._RemediationTemplateId = params.get("RemediationTemplateId")
        self._InvokeType = params.get("InvokeType")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRemediationResponse(AbstractModel):
    r"""CreateRemediation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RemediationId: <p>修正设置Id</p>
        :type RemediationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RemediationId = None
        self._RequestId = None

    @property
    def RemediationId(self):
        r"""<p>修正设置Id</p>
        :rtype: str
        """
        return self._RemediationId

    @RemediationId.setter
    def RemediationId(self, RemediationId):
        self._RemediationId = RemediationId

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
        self._RemediationId = params.get("RemediationId")
        self._RequestId = params.get("RequestId")


class DeleteAggregateCompliancePackRequest(AbstractModel):
    r"""DeleteAggregateCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        """
        self._CompliancePackId = None
        self._AccountGroupId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAggregateCompliancePackResponse(AbstractModel):
    r"""DeleteAggregateCompliancePack返回参数结构体

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


class DeleteAggregateConfigRuleRequest(AbstractModel):
    r"""DeleteAggregateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        """
        self._RuleId = None
        self._AccountGroupId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAggregateConfigRuleResponse(AbstractModel):
    r"""DeleteAggregateConfigRule返回参数结构体

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


class DeleteCompliancePackRequest(AbstractModel):
    r"""DeleteCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        """
        self._CompliancePackId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCompliancePackResponse(AbstractModel):
    r"""DeleteCompliancePack返回参数结构体

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


class DeleteConfigRuleRequest(AbstractModel):
    r"""DeleteConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConfigRuleResponse(AbstractModel):
    r"""DeleteConfigRule返回参数结构体

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


class DeleteRemediationsRequest(AbstractModel):
    r"""DeleteRemediations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RemediationIds: 修正设置ID
        :type RemediationIds: list of str
        """
        self._RemediationIds = None

    @property
    def RemediationIds(self):
        r"""修正设置ID
        :rtype: list of str
        """
        return self._RemediationIds

    @RemediationIds.setter
    def RemediationIds(self, RemediationIds):
        self._RemediationIds = RemediationIds


    def _deserialize(self, params):
        self._RemediationIds = params.get("RemediationIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRemediationsResponse(AbstractModel):
    r"""DeleteRemediations返回参数结构体

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


class DescribeAggregateCompliancePackRequest(AbstractModel):
    r"""DescribeAggregateCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        """
        self._AccountGroupId = None
        self._CompliancePackId = None

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggregateCompliancePackResponse(AbstractModel):
    r"""DescribeAggregateCompliancePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _ConfigRules: 合规包规则
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRules: list of ComplianceConfigRule
        :param _CompliancePackId: 合规包id
        :type CompliancePackId: str
        :param _Status: 合规包状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompliancePackName = None
        self._Description = None
        self._CreateTime = None
        self._RiskLevel = None
        self._ConfigRules = None
        self._CompliancePackId = None
        self._Status = None
        self._RequestId = None

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ConfigRules(self):
        r"""合规包规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ComplianceConfigRule
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

    @property
    def CompliancePackId(self):
        r"""合规包id
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def Status(self):
        r"""合规包状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._CompliancePackName = params.get("CompliancePackName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = ComplianceConfigRule()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._CompliancePackId = params.get("CompliancePackId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeAggregateConfigDeliverRequest(AbstractModel):
    r"""DescribeAggregateConfigDeliver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        """
        self._AccountGroupId = None

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggregateConfigDeliverResponse(AbstractModel):
    r"""DescribeAggregateConfigDeliver返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeliverName: 投递名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverName: str
        :param _TargetArn: 资源六段式
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetArn: str
        :param _Status: 投递状态 DeliverStatus：0 关闭  1 开启
        :type Status: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _DeliverPrefix: 日志前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverPrefix: str
        :param _DeliverType: 投递类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverType: str
        :param _DeliverUin: 支持跨账号投递的成员账号uin，只能是委派管理员。默认为0，即投递到管理员账号下
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverUin: int
        :param _DeliverContentType: 1：配置变更 2： 资源列表 3：全部
        :type DeliverContentType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeliverName = None
        self._TargetArn = None
        self._Status = None
        self._CreateTime = None
        self._DeliverPrefix = None
        self._DeliverType = None
        self._DeliverUin = None
        self._DeliverContentType = None
        self._RequestId = None

    @property
    def DeliverName(self):
        r"""投递名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverName

    @DeliverName.setter
    def DeliverName(self, DeliverName):
        self._DeliverName = DeliverName

    @property
    def TargetArn(self):
        r"""资源六段式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetArn

    @TargetArn.setter
    def TargetArn(self, TargetArn):
        self._TargetArn = TargetArn

    @property
    def Status(self):
        r"""投递状态 DeliverStatus：0 关闭  1 开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeliverPrefix(self):
        r"""日志前缀
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverPrefix

    @DeliverPrefix.setter
    def DeliverPrefix(self, DeliverPrefix):
        self._DeliverPrefix = DeliverPrefix

    @property
    def DeliverType(self):
        r"""投递类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverType

    @DeliverType.setter
    def DeliverType(self, DeliverType):
        self._DeliverType = DeliverType

    @property
    def DeliverUin(self):
        r"""支持跨账号投递的成员账号uin，只能是委派管理员。默认为0，即投递到管理员账号下
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DeliverUin

    @DeliverUin.setter
    def DeliverUin(self, DeliverUin):
        self._DeliverUin = DeliverUin

    @property
    def DeliverContentType(self):
        r"""1：配置变更 2： 资源列表 3：全部
        :rtype: int
        """
        return self._DeliverContentType

    @DeliverContentType.setter
    def DeliverContentType(self, DeliverContentType):
        self._DeliverContentType = DeliverContentType

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
        self._DeliverName = params.get("DeliverName")
        self._TargetArn = params.get("TargetArn")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._DeliverPrefix = params.get("DeliverPrefix")
        self._DeliverType = params.get("DeliverType")
        self._DeliverUin = params.get("DeliverUin")
        self._DeliverContentType = params.get("DeliverContentType")
        self._RequestId = params.get("RequestId")


class DescribeAggregateConfigRuleRequest(AbstractModel):
    r"""DescribeAggregateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AccountGroupId: 账号组
        :type AccountGroupId: str
        """
        self._RuleId = None
        self._AccountGroupId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccountGroupId(self):
        r"""账号组
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggregateConfigRuleResponse(AbstractModel):
    r"""DescribeAggregateConfigRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigRule: 规则详情
        :type ConfigRule: :class:`tencentcloud.config.v20220802.models.ConfigRule`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigRule = None
        self._RequestId = None

    @property
    def ConfigRule(self):
        r"""规则详情
        :rtype: :class:`tencentcloud.config.v20220802.models.ConfigRule`
        """
        return self._ConfigRule

    @ConfigRule.setter
    def ConfigRule(self, ConfigRule):
        self._ConfigRule = ConfigRule

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
        if params.get("ConfigRule") is not None:
            self._ConfigRule = ConfigRule()
            self._ConfigRule._deserialize(params.get("ConfigRule"))
        self._RequestId = params.get("RequestId")


class DescribeAggregateDiscoveredResourceRequest(AbstractModel):
    r"""DescribeAggregateDiscoveredResource请求参数结构体

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
        r"""资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        r"""资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def ResourceOwnerId(self):
        r"""资源所属用户ID
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
    r"""DescribeAggregateDiscoveredResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceName: 资源名
        :type ResourceName: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _ResourceZone: 资源可用区
        :type ResourceZone: str
        :param _Configuration: 资源配置
        :type Configuration: str
        :param _ResourceCreateTime: 资源创建时间
        :type ResourceCreateTime: str
        :param _Tags: 资源标签
        :type Tags: list of Tag
        :param _UpdateTime: 资源更新时间
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
        r"""资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""资源名
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceRegion(self):
        r"""资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceZone(self):
        r"""资源可用区
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def Configuration(self):
        r"""资源配置
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ResourceCreateTime(self):
        r"""资源创建时间
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        r"""资源标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpdateTime(self):
        r"""资源更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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


class DescribeAggregatorRequest(AbstractModel):
    r"""DescribeAggregator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountGroupId: <p>账号组ID</p>
        :type AccountGroupId: str
        :param _OwnerUin: <p>账号组创建者ID</p>
        :type OwnerUin: int
        """
        self._AccountGroupId = None
        self._OwnerUin = None

    @property
    def AccountGroupId(self):
        r"""<p>账号组ID</p>
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def OwnerUin(self):
        r"""<p>账号组创建者ID</p>
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin


    def _deserialize(self, params):
        self._AccountGroupId = params.get("AccountGroupId")
        self._OwnerUin = params.get("OwnerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAggregatorResponse(AbstractModel):
    r"""DescribeAggregator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>账号组名称</p>
        :type Name: str
        :param _Description: <p>账号组描述</p>
        :type Description: str
        :param _Type: <p>账号组类型</p>
        :type Type: str
        :param _AggregatorAccounts: <p>成员信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AggregatorAccounts: list of AggregatorAccount
        :param _AggregatorStatus: <p>创建状态</p>
        :type AggregatorStatus: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._AggregatorAccounts = None
        self._AggregatorStatus = None
        self._RequestId = None

    @property
    def Name(self):
        r"""<p>账号组名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>账号组描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        r"""<p>账号组类型</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AggregatorAccounts(self):
        r"""<p>成员信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AggregatorAccount
        """
        return self._AggregatorAccounts

    @AggregatorAccounts.setter
    def AggregatorAccounts(self, AggregatorAccounts):
        self._AggregatorAccounts = AggregatorAccounts

    @property
    def AggregatorStatus(self):
        r"""<p>创建状态</p>
        :rtype: int
        """
        return self._AggregatorStatus

    @AggregatorStatus.setter
    def AggregatorStatus(self, AggregatorStatus):
        self._AggregatorStatus = AggregatorStatus

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
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        if params.get("AggregatorAccounts") is not None:
            self._AggregatorAccounts = []
            for item in params.get("AggregatorAccounts"):
                obj = AggregatorAccount()
                obj._deserialize(item)
                self._AggregatorAccounts.append(obj)
        self._AggregatorStatus = params.get("AggregatorStatus")
        self._RequestId = params.get("RequestId")


class DescribeCompliancePackRequest(AbstractModel):
    r"""DescribeCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        """
        self._CompliancePackId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompliancePackResponse(AbstractModel):
    r"""DescribeCompliancePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _ConfigRules: 合规包规则
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRules: list of ComplianceConfigRule
        :param _CompliancePackId: 合规包id
        :type CompliancePackId: str
        :param _Status: 合规包状态
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompliancePackName = None
        self._Description = None
        self._CreateTime = None
        self._RiskLevel = None
        self._ConfigRules = None
        self._CompliancePackId = None
        self._Status = None
        self._RequestId = None

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ConfigRules(self):
        r"""合规包规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ComplianceConfigRule
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

    @property
    def CompliancePackId(self):
        r"""合规包id
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def Status(self):
        r"""合规包状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._CompliancePackName = params.get("CompliancePackName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = ComplianceConfigRule()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._CompliancePackId = params.get("CompliancePackId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeConfigDeliverRequest(AbstractModel):
    r"""DescribeConfigDeliver请求参数结构体

    """


class DescribeConfigDeliverResponse(AbstractModel):
    r"""DescribeConfigDeliver返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeliverName: 投递名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverName: str
        :param _TargetArn: 资源六段式
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetArn: str
        :param _Status: 投递状态 DeliverStatus：0 关闭  1 开启
        :type Status: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _DeliverPrefix: 日志前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverPrefix: str
        :param _DeliverType: 投递类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeliverType: str
        :param _DeliverContentType: 1：配置变更   2： 资源列表 3：全部
        :type DeliverContentType: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeliverName = None
        self._TargetArn = None
        self._Status = None
        self._CreateTime = None
        self._DeliverPrefix = None
        self._DeliverType = None
        self._DeliverContentType = None
        self._RequestId = None

    @property
    def DeliverName(self):
        r"""投递名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverName

    @DeliverName.setter
    def DeliverName(self, DeliverName):
        self._DeliverName = DeliverName

    @property
    def TargetArn(self):
        r"""资源六段式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetArn

    @TargetArn.setter
    def TargetArn(self, TargetArn):
        self._TargetArn = TargetArn

    @property
    def Status(self):
        r"""投递状态 DeliverStatus：0 关闭  1 开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeliverPrefix(self):
        r"""日志前缀
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverPrefix

    @DeliverPrefix.setter
    def DeliverPrefix(self, DeliverPrefix):
        self._DeliverPrefix = DeliverPrefix

    @property
    def DeliverType(self):
        r"""投递类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeliverType

    @DeliverType.setter
    def DeliverType(self, DeliverType):
        self._DeliverType = DeliverType

    @property
    def DeliverContentType(self):
        r"""1：配置变更   2： 资源列表 3：全部
        :rtype: int
        """
        return self._DeliverContentType

    @DeliverContentType.setter
    def DeliverContentType(self, DeliverContentType):
        self._DeliverContentType = DeliverContentType

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
        self._DeliverName = params.get("DeliverName")
        self._TargetArn = params.get("TargetArn")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._DeliverPrefix = params.get("DeliverPrefix")
        self._DeliverType = params.get("DeliverType")
        self._DeliverContentType = params.get("DeliverContentType")
        self._RequestId = params.get("RequestId")


class DescribeConfigRecorderRequest(AbstractModel):
    r"""DescribeConfigRecorder请求参数结构体

    """


class DescribeConfigRecorderResponse(AbstractModel):
    r"""DescribeConfigRecorder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 用户监控资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of UserConfigResource
        :param _Status: 0 关闭1 打开
        :type Status: int
        :param _TriggerCount: 当日快照次数
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerCount: int
        :param _OpenCount: 当日打开监控次数
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenCount: int
        :param _UpdateCount: 当日修改监控范围次数
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateCount: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Status = None
        self._TriggerCount = None
        self._OpenCount = None
        self._UpdateCount = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def Items(self):
        r"""用户监控资源列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UserConfigResource
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Status(self):
        r"""0 关闭1 打开
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TriggerCount(self):
        r"""当日快照次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TriggerCount

    @TriggerCount.setter
    def TriggerCount(self, TriggerCount):
        self._TriggerCount = TriggerCount

    @property
    def OpenCount(self):
        r"""当日打开监控次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OpenCount

    @OpenCount.setter
    def OpenCount(self, OpenCount):
        self._OpenCount = OpenCount

    @property
    def UpdateCount(self):
        r"""当日修改监控范围次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateCount

    @UpdateCount.setter
    def UpdateCount(self, UpdateCount):
        self._UpdateCount = UpdateCount

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = UserConfigResource()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Status = params.get("Status")
        self._TriggerCount = params.get("TriggerCount")
        self._OpenCount = params.get("OpenCount")
        self._UpdateCount = params.get("UpdateCount")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")


class DescribeConfigRuleRequest(AbstractModel):
    r"""DescribeConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConfigRuleResponse(AbstractModel):
    r"""DescribeConfigRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigRule: 规则详情
        :type ConfigRule: :class:`tencentcloud.config.v20220802.models.ConfigRule`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConfigRule = None
        self._RequestId = None

    @property
    def ConfigRule(self):
        r"""规则详情
        :rtype: :class:`tencentcloud.config.v20220802.models.ConfigRule`
        """
        return self._ConfigRule

    @ConfigRule.setter
    def ConfigRule(self, ConfigRule):
        self._ConfigRule = ConfigRule

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
        if params.get("ConfigRule") is not None:
            self._ConfigRule = ConfigRule()
            self._ConfigRule._deserialize(params.get("ConfigRule"))
        self._RequestId = params.get("RequestId")


class DescribeDiscoveredResourceRequest(AbstractModel):
    r"""DescribeDiscoveredResource请求参数结构体

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
        r"""资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        r"""资源地域
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
    r"""DescribeDiscoveredResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源Id
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _ResourceName: 资源名
        :type ResourceName: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _ResourceZone: 资源可用区
        :type ResourceZone: str
        :param _Configuration: 资源配置
        :type Configuration: str
        :param _ResourceCreateTime: 资源创建时间
        :type ResourceCreateTime: str
        :param _Tags: 资源标签
        :type Tags: list of Tag
        :param _UpdateTime: 资源更新时间
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
        r"""资源Id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""资源名
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceRegion(self):
        r"""资源地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceZone(self):
        r"""资源可用区
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def Configuration(self):
        r"""资源配置
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def ResourceCreateTime(self):
        r"""资源创建时间
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        r"""资源标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UpdateTime(self):
        r"""资源更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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


class DescribeSystemCompliancePackRequest(AbstractModel):
    r"""DescribeSystemCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        """
        self._CompliancePackId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSystemCompliancePackResponse(AbstractModel):
    r"""DescribeSystemCompliancePack返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _Description: 合规包描述
        :type Description: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _ConfigRules: 合规包规则列表
        :type ConfigRules: list of CompliancePackRuleForManage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CompliancePackId = None
        self._CompliancePackName = None
        self._Description = None
        self._RiskLevel = None
        self._ConfigRules = None
        self._RequestId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def Description(self):
        r"""合规包描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ConfigRules(self):
        r"""合规包规则列表
        :rtype: list of CompliancePackRuleForManage
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

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
        self._CompliancePackId = params.get("CompliancePackId")
        self._CompliancePackName = params.get("CompliancePackName")
        self._Description = params.get("Description")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = CompliancePackRuleForManage()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSystemRuleRequest(AbstractModel):
    r"""DescribeSystemRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Identifier: 规则唯一标识
        :type Identifier: str
        """
        self._Identifier = None

    @property
    def Identifier(self):
        r"""规则唯一标识
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSystemRuleResponse(AbstractModel):
    r"""DescribeSystemRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SystemConfigRule: 详情
        :type SystemConfigRule: :class:`tencentcloud.config.v20220802.models.SystemConfigRule`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SystemConfigRule = None
        self._RequestId = None

    @property
    def SystemConfigRule(self):
        r"""详情
        :rtype: :class:`tencentcloud.config.v20220802.models.SystemConfigRule`
        """
        return self._SystemConfigRule

    @SystemConfigRule.setter
    def SystemConfigRule(self, SystemConfigRule):
        self._SystemConfigRule = SystemConfigRule

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
        if params.get("SystemConfigRule") is not None:
            self._SystemConfigRule = SystemConfigRule()
            self._SystemConfigRule._deserialize(params.get("SystemConfigRule"))
        self._RequestId = params.get("RequestId")


class DetachAggregateConfigRuleToCompliancePackRequest(AbstractModel):
    r"""DetachAggregateConfigRuleToCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _ConfigRuleId: 规则ID
        :type ConfigRuleId: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        """
        self._CompliancePackId = None
        self._ConfigRuleId = None
        self._AccountGroupId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def ConfigRuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachAggregateConfigRuleToCompliancePackResponse(AbstractModel):
    r"""DetachAggregateConfigRuleToCompliancePack返回参数结构体

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


class DetachConfigRuleToCompliancePackRequest(AbstractModel):
    r"""DetachConfigRuleToCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _ConfigRuleId: 规则ID
        :type ConfigRuleId: str
        """
        self._CompliancePackId = None
        self._ConfigRuleId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def ConfigRuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        self._ConfigRuleId = params.get("ConfigRuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachConfigRuleToCompliancePackResponse(AbstractModel):
    r"""DetachConfigRuleToCompliancePack返回参数结构体

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


class Evaluation(AbstractModel):
    r"""自定义规则评估结果

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
        r"""已评估资源ID。长度为0~256个字符
        :rtype: str
        """
        return self._ComplianceResourceId

    @ComplianceResourceId.setter
    def ComplianceResourceId(self, ComplianceResourceId):
        self._ComplianceResourceId = ComplianceResourceId

    @property
    def ComplianceResourceType(self):
        r"""已评估资源类型。
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
        r"""已评估资源地域。
长度为0~32个字符
        :rtype: str
        """
        return self._ComplianceRegion

    @ComplianceRegion.setter
    def ComplianceRegion(self, ComplianceRegion):
        self._ComplianceRegion = ComplianceRegion

    @property
    def ComplianceType(self):
        r"""合规类型。取值：
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
        r"""不合规资源的补充信息。
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
        


class EvaluationResult(AbstractModel):
    r"""评估结果

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ResourceRegion: 资源地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param _ResourceName: 资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceName: str
        :param _ConfigRuleId: 规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRuleId: str
        :param _ConfigRuleName: 规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRuleName: str
        :param _CompliancePackId: 合规包id
注意：此字段可能返回 null，表示取不到有效值。
        :type CompliancePackId: str
        :param _RiskLevel: 风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param _Annotation: 评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Annotation: :class:`tencentcloud.config.v20220802.models.Annotation`
        :param _ComplianceType: 合规类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ComplianceType: str
        :param _InvokingEventMessageType: 规则发起类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InvokingEventMessageType: str
        :param _ConfigRuleInvokedTime: 评估发起时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRuleInvokedTime: str
        :param _ResultRecordedTime: 评估实际时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultRecordedTime: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._ResourceRegion = None
        self._ResourceName = None
        self._ConfigRuleId = None
        self._ConfigRuleName = None
        self._CompliancePackId = None
        self._RiskLevel = None
        self._Annotation = None
        self._ComplianceType = None
        self._InvokingEventMessageType = None
        self._ConfigRuleInvokedTime = None
        self._ResultRecordedTime = None

    @property
    def ResourceId(self):
        r"""资源id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceRegion(self):
        r"""资源地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceName(self):
        r"""资源名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ConfigRuleId(self):
        r"""规则id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def ConfigRuleName(self):
        r"""规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigRuleName

    @ConfigRuleName.setter
    def ConfigRuleName(self, ConfigRuleName):
        self._ConfigRuleName = ConfigRuleName

    @property
    def CompliancePackId(self):
        r"""合规包id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def RiskLevel(self):
        r"""风险等级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def Annotation(self):
        r"""评估结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.config.v20220802.models.Annotation`
        """
        return self._Annotation

    @Annotation.setter
    def Annotation(self, Annotation):
        self._Annotation = Annotation

    @property
    def ComplianceType(self):
        r"""合规类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ComplianceType

    @ComplianceType.setter
    def ComplianceType(self, ComplianceType):
        self._ComplianceType = ComplianceType

    @property
    def InvokingEventMessageType(self):
        r"""规则发起类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InvokingEventMessageType

    @InvokingEventMessageType.setter
    def InvokingEventMessageType(self, InvokingEventMessageType):
        self._InvokingEventMessageType = InvokingEventMessageType

    @property
    def ConfigRuleInvokedTime(self):
        r"""评估发起时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigRuleInvokedTime

    @ConfigRuleInvokedTime.setter
    def ConfigRuleInvokedTime(self, ConfigRuleInvokedTime):
        self._ConfigRuleInvokedTime = ConfigRuleInvokedTime

    @property
    def ResultRecordedTime(self):
        r"""评估实际时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultRecordedTime

    @ResultRecordedTime.setter
    def ResultRecordedTime(self, ResultRecordedTime):
        self._ResultRecordedTime = ResultRecordedTime


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceName = params.get("ResourceName")
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._ConfigRuleName = params.get("ConfigRuleName")
        self._CompliancePackId = params.get("CompliancePackId")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("Annotation") is not None:
            self._Annotation = Annotation()
            self._Annotation._deserialize(params.get("Annotation"))
        self._ComplianceType = params.get("ComplianceType")
        self._InvokingEventMessageType = params.get("InvokingEventMessageType")
        self._ConfigRuleInvokedTime = params.get("ConfigRuleInvokedTime")
        self._ResultRecordedTime = params.get("ResultRecordedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""资源列表筛选

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
        r"""查询字段名称 资源名称：resourceName  资源ID：resourceId 资源类型：resourceType 资源地域：resourceRegion    删除状态：resourceDelete 0未删除，1已删除  resourceRegionAndZone地域/可用区
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""查询字段值
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
    r"""参数值

    """

    def __init__(self):
        r"""
        :param _ParameterKey: 参数名
        :type ParameterKey: str
        :param _Type: 参数类型。必填类型：Require，可选类型：Optional。
        :type Type: str
        :param _Value: 参数值
        :type Value: str
        """
        self._ParameterKey = None
        self._Type = None
        self._Value = None

    @property
    def ParameterKey(self):
        r"""参数名
        :rtype: str
        """
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        r"""参数类型。必填类型：Require，可选类型：Optional。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""参数值
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
    r"""规则入参

    """

    def __init__(self):
        r"""
        :param _ValueType: 值类型。数值：Integer， 字符串：String
        :type ValueType: str
        :param _ParameterKey: 参数Key
        :type ParameterKey: str
        :param _Type: 参数类型。必填类型：Require，可选类型：Optional。
        :type Type: str
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        :param _Description: 描述
        :type Description: str
        """
        self._ValueType = None
        self._ParameterKey = None
        self._Type = None
        self._DefaultValue = None
        self._Description = None

    @property
    def ValueType(self):
        r"""值类型。数值：Integer， 字符串：String
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType

    @property
    def ParameterKey(self):
        r"""参数Key
        :rtype: str
        """
        return self._ParameterKey

    @ParameterKey.setter
    def ParameterKey(self, ParameterKey):
        self._ParameterKey = ParameterKey

    @property
    def Type(self):
        r"""参数类型。必填类型：Require，可选类型：Optional。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        r"""默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Description(self):
        r"""描述
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
        


class ListAggregateCompliancePacksRequest(AbstractModel):
    r"""ListAggregateCompliancePacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: list of int non-negative
        :param _Status: 合规包状态 ACTIVE、NO_ACTIVE
        :type Status: str
        :param _ComplianceResult: 评估状态合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
        :type ComplianceResult: list of str
        :param _OrderType: 排序类型, 倒序：desc，顺序：asc
        :type OrderType: str
        """
        self._Limit = None
        self._Offset = None
        self._AccountGroupId = None
        self._CompliancePackName = None
        self._RiskLevel = None
        self._Status = None
        self._ComplianceResult = None
        self._OrderType = None

    @property
    def Limit(self):
        r"""数量
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

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RiskLevel(self):
        r"""风险等级
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
    def Status(self):
        r"""合规包状态 ACTIVE、NO_ACTIVE
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ComplianceResult(self):
        r"""评估状态合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def OrderType(self):
        r"""排序类型, 倒序：desc，顺序：asc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountGroupId = params.get("AccountGroupId")
        self._CompliancePackName = params.get("CompliancePackName")
        self._RiskLevel = params.get("RiskLevel")
        self._Status = params.get("Status")
        self._ComplianceResult = params.get("ComplianceResult")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateCompliancePacksResponse(AbstractModel):
    r"""ListAggregateCompliancePacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 详情
        :type Items: list of ConfigCompliancePack
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
        :rtype: list of ConfigCompliancePack
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigCompliancePack()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListAggregateConfigRuleEvaluationResultsRequest(AbstractModel):
    r"""ListAggregateConfigRuleEvaluationResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigRuleId: <p>规则ID</p>
        :type ConfigRuleId: str
        :param _Limit: <p>偏移量</p>
        :type Limit: int
        :param _Offset: <p>当前页</p>
        :type Offset: int
        :param _AccountGroupId: <p>账号组ID</p>
        :type AccountGroupId: str
        :param _ResourceType: <p>类型</p>
        :type ResourceType: list of str
        :param _ComplianceType: <p>评估结果 COMPLIANT：合规   NON_COMPLIANT：不合规</p>
        :type ComplianceType: list of str
        :param _ResourceOwnerId: <p>资源所属用户ID</p>
        :type ResourceOwnerId: int
        :param _ResourceOwnerIds: <p>筛选的资源拥有者uin集合</p>
        :type ResourceOwnerIds: list of int non-negative
        """
        self._ConfigRuleId = None
        self._Limit = None
        self._Offset = None
        self._AccountGroupId = None
        self._ResourceType = None
        self._ComplianceType = None
        self._ResourceOwnerId = None
        self._ResourceOwnerIds = None

    @property
    def ConfigRuleId(self):
        r"""<p>规则ID</p>
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def Limit(self):
        r"""<p>偏移量</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>当前页</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountGroupId(self):
        r"""<p>账号组ID</p>
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def ResourceType(self):
        r"""<p>类型</p>
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ComplianceType(self):
        r"""<p>评估结果 COMPLIANT：合规   NON_COMPLIANT：不合规</p>
        :rtype: list of str
        """
        return self._ComplianceType

    @ComplianceType.setter
    def ComplianceType(self, ComplianceType):
        self._ComplianceType = ComplianceType

    @property
    def ResourceOwnerId(self):
        r"""<p>资源所属用户ID</p>
        :rtype: int
        """
        return self._ResourceOwnerId

    @ResourceOwnerId.setter
    def ResourceOwnerId(self, ResourceOwnerId):
        self._ResourceOwnerId = ResourceOwnerId

    @property
    def ResourceOwnerIds(self):
        r"""<p>筛选的资源拥有者uin集合</p>
        :rtype: list of int non-negative
        """
        return self._ResourceOwnerIds

    @ResourceOwnerIds.setter
    def ResourceOwnerIds(self, ResourceOwnerIds):
        self._ResourceOwnerIds = ResourceOwnerIds


    def _deserialize(self, params):
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._AccountGroupId = params.get("AccountGroupId")
        self._ResourceType = params.get("ResourceType")
        self._ComplianceType = params.get("ComplianceType")
        self._ResourceOwnerId = params.get("ResourceOwnerId")
        self._ResourceOwnerIds = params.get("ResourceOwnerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregateConfigRuleEvaluationResultsResponse(AbstractModel):
    r"""ListAggregateConfigRuleEvaluationResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: <p>总数</p>
        :type Total: int
        :param _Items: <p>详情</p>
        :type Items: list of AggregateEvaluationResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""<p>详情</p>
        :rtype: list of AggregateEvaluationResult
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AggregateEvaluationResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListAggregateConfigRulesRequest(AbstractModel):
    r"""ListAggregateConfigRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: <p>每页限制</p>
        :type Limit: int
        :param _Offset: <p>偏移量</p>
        :type Offset: int
        :param _AccountGroupId: <p>账号组ID</p>
        :type AccountGroupId: str
        :param _OrderType: <p>排序类型, 倒序：desc，顺序：asc</p>
        :type OrderType: str
        :param _RiskLevel: <p>风险等级<br>1：高风险。<br>2：中风险。<br>3：低风险。</p>
        :type RiskLevel: list of int non-negative
        :param _State: <p>规则状态</p>
        :type State: str
        :param _ComplianceResult: <p>评估结果</p>
        :type ComplianceResult: list of str
        :param _RuleName: <p>规则名</p>
        :type RuleName: str
        :param _RuleOwnerId: <p>规则所属账号ID</p>
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
        r"""<p>每页限制</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def AccountGroupId(self):
        r"""<p>账号组ID</p>
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def OrderType(self):
        r"""<p>排序类型, 倒序：desc，顺序：asc</p>
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def RiskLevel(self):
        r"""<p>风险等级<br>1：高风险。<br>2：中风险。<br>3：低风险。</p>
        :rtype: list of int non-negative
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def State(self):
        r"""<p>规则状态</p>
        :rtype: str
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def ComplianceResult(self):
        r"""<p>评估结果</p>
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def RuleName(self):
        r"""<p>规则名</p>
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def RuleOwnerId(self):
        r"""<p>规则所属账号ID</p>
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
    r"""ListAggregateConfigRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: <p>总数</p>
        :type Total: int
        :param _Items: <p>详情</p>
        :type Items: list of ConfigRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""<p>详情</p>
        :rtype: list of ConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListAggregateDiscoveredResourcesRequest(AbstractModel):
    r"""ListAggregateDiscoveredResources请求参数结构体

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
        r"""每页显示数量
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def Filters(self):
        r"""resourceName：资源名  resourceId ：资源ID resourceType：资源类型
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextToken(self):
        r"""下一页token
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OrderType(self):
        r"""排序方式 asc、desc
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
    r"""ListAggregateDiscoveredResources返回参数结构体

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
        r"""详情
        :rtype: list of AggregateResourceInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextToken(self):
        r"""下一页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AggregateResourceInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class ListAggregatorsRequest(AbstractModel):
    r"""ListAggregators请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页显示数量
        :type Limit: int
        :param _Offset: 起始
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        r"""每页显示数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""起始
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAggregatorsResponse(AbstractModel):
    r"""ListAggregators返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 账号组列表
        :type Items: list of Aggregator
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""账号组列表
        :rtype: list of Aggregator
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Aggregator()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListCompliancePacksRequest(AbstractModel):
    r"""ListCompliancePacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 数量
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: list of int non-negative
        :param _Status: 合规包状态 ACTIVE、NO_ACTIVE
        :type Status: str
        :param _ComplianceResult: 评估状态合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
        :type ComplianceResult: list of str
        :param _OrderType: 排序类型, 倒序：desc，顺序：asc
        :type OrderType: str
        """
        self._Limit = None
        self._Offset = None
        self._CompliancePackName = None
        self._RiskLevel = None
        self._Status = None
        self._ComplianceResult = None
        self._OrderType = None

    @property
    def Limit(self):
        r"""数量
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

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RiskLevel(self):
        r"""风险等级
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
    def Status(self):
        r"""合规包状态 ACTIVE、NO_ACTIVE
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ComplianceResult(self):
        r"""评估状态合规： 'COMPLIANT'
不合规： 'NON_COMPLIANT'
        :rtype: list of str
        """
        return self._ComplianceResult

    @ComplianceResult.setter
    def ComplianceResult(self, ComplianceResult):
        self._ComplianceResult = ComplianceResult

    @property
    def OrderType(self):
        r"""排序类型, 倒序：desc，顺序：asc
        :rtype: str
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._CompliancePackName = params.get("CompliancePackName")
        self._RiskLevel = params.get("RiskLevel")
        self._Status = params.get("Status")
        self._ComplianceResult = params.get("ComplianceResult")
        self._OrderType = params.get("OrderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListCompliancePacksResponse(AbstractModel):
    r"""ListCompliancePacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 详情
        :type Items: list of ConfigCompliancePack
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
        :rtype: list of ConfigCompliancePack
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigCompliancePack()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListConfigRuleEvaluationResultsRequest(AbstractModel):
    r"""ListConfigRuleEvaluationResults请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConfigRuleId: 规则ID
        :type ConfigRuleId: str
        :param _Limit: 偏移量
        :type Limit: int
        :param _Offset: 当前页
        :type Offset: int
        :param _ResourceType: 类型
        :type ResourceType: list of str
        :param _ComplianceType: 评估结果 COMPLIANT：合规   NON_COMPLIANT：不合规
        :type ComplianceType: list of str
        """
        self._ConfigRuleId = None
        self._Limit = None
        self._Offset = None
        self._ResourceType = None
        self._ComplianceType = None

    @property
    def ConfigRuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._ConfigRuleId

    @ConfigRuleId.setter
    def ConfigRuleId(self, ConfigRuleId):
        self._ConfigRuleId = ConfigRuleId

    @property
    def Limit(self):
        r"""偏移量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""当前页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ResourceType(self):
        r"""类型
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ComplianceType(self):
        r"""评估结果 COMPLIANT：合规   NON_COMPLIANT：不合规
        :rtype: list of str
        """
        return self._ComplianceType

    @ComplianceType.setter
    def ComplianceType(self, ComplianceType):
        self._ComplianceType = ComplianceType


    def _deserialize(self, params):
        self._ConfigRuleId = params.get("ConfigRuleId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ResourceType = params.get("ResourceType")
        self._ComplianceType = params.get("ComplianceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListConfigRuleEvaluationResultsResponse(AbstractModel):
    r"""ListConfigRuleEvaluationResults返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 详情
        :type Items: list of EvaluationResult
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
        :rtype: list of EvaluationResult
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = EvaluationResult()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListConfigRulesRequest(AbstractModel):
    r"""ListConfigRules请求参数结构体

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
        r"""每页数量。
取值范围：1~200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量。
取值范围：最小值为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderType(self):
        r"""排序类型(规则名称)。
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
        r"""风险等级。
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
        r"""规则状态。
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
        r"""评估结果。
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
        r"""规则名
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
    r"""ListConfigRules返回参数结构体

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
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
        :rtype: list of ConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListDiscoveredResourcesRequest(AbstractModel):
    r"""ListDiscoveredResources请求参数结构体

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
        r"""每页显示数量
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Filters(self):
        r"""resourceName：资源名  resourceId ：资源ID
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Tags(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NextToken(self):
        r"""下一页token
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def OrderType(self):
        r"""排序方式 asc、desc
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
    r"""ListDiscoveredResources返回参数结构体

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
        r"""详情
        :rtype: list of ResourceListInfo
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def NextToken(self):
        r"""下一页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceListInfo()
                obj._deserialize(item)
                self._Items.append(obj)
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class ListRemediationExecutionsRequest(AbstractModel):
    r"""ListRemediationExecutions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        :param _Limit: 分页条数。默认20， 取值1~200
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _ExecutionStatus: 修正状态 1：运行中 2：成功 3：失败
        :type ExecutionStatus: int
        """
        self._RuleId = None
        self._Limit = None
        self._Offset = None
        self._ExecutionStatus = None

    @property
    def RuleId(self):
        r"""规则 ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Limit(self):
        r"""分页条数。默认20， 取值1~200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ExecutionStatus(self):
        r"""修正状态 1：运行中 2：成功 3：失败
        :rtype: int
        """
        return self._ExecutionStatus

    @ExecutionStatus.setter
    def ExecutionStatus(self, ExecutionStatus):
        self._ExecutionStatus = ExecutionStatus


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ExecutionStatus = params.get("ExecutionStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRemediationExecutionsResponse(AbstractModel):
    r"""ListRemediationExecutions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _RemediationExecutions: 修复记录
        :type RemediationExecutions: list of RemediationExecutions
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RemediationExecutions = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RemediationExecutions(self):
        r"""修复记录
        :rtype: list of RemediationExecutions
        """
        return self._RemediationExecutions

    @RemediationExecutions.setter
    def RemediationExecutions(self, RemediationExecutions):
        self._RemediationExecutions = RemediationExecutions

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
        self._Total = params.get("Total")
        if params.get("RemediationExecutions") is not None:
            self._RemediationExecutions = []
            for item in params.get("RemediationExecutions"):
                obj = RemediationExecutions()
                obj._deserialize(item)
                self._RemediationExecutions.append(obj)
        self._RequestId = params.get("RequestId")


class ListRemediationsRequest(AbstractModel):
    r"""ListRemediations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页条数。默认20， 取值1~200
        :type Limit: int
        :param _RuleIds: 规则ID
        :type RuleIds: list of str
        """
        self._Limit = None
        self._RuleIds = None

    @property
    def Limit(self):
        r"""分页条数。默认20， 取值1~200
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def RuleIds(self):
        r"""规则ID
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRemediationsResponse(AbstractModel):
    r"""ListRemediations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Remediations: 修正设置
        :type Remediations: list of Remediation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Remediations = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Remediations(self):
        r"""修正设置
        :rtype: list of Remediation
        """
        return self._Remediations

    @Remediations.setter
    def Remediations(self, Remediations):
        self._Remediations = Remediations

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
        self._Total = params.get("Total")
        if params.get("Remediations") is not None:
            self._Remediations = []
            for item in params.get("Remediations"):
                obj = Remediation()
                obj._deserialize(item)
                self._Remediations.append(obj)
        self._RequestId = params.get("RequestId")


class ListResourceTypesRequest(AbstractModel):
    r"""ListResourceTypes请求参数结构体

    """


class ListResourceTypesResponse(AbstractModel):
    r"""ListResourceTypes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 详情
        :type Items: list of ConfigResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        r"""详情
        :rtype: list of ConfigResource
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ConfigResource()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListSystemCompliancePacksRequest(AbstractModel):
    r"""ListSystemCompliancePacks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        r"""每页限制
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
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSystemCompliancePacksResponse(AbstractModel):
    r"""ListSystemCompliancePacks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _Items: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of SystemCompliancePack
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SystemCompliancePack
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SystemCompliancePack()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListSystemRulesRequest(AbstractModel):
    r"""ListSystemRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页数量
        :type Limit: int
        :param _Offset: 当前页
        :type Offset: int
        :param _Keyword: 搜索关键字。支持标识/名称/标签/描述搜索
        :type Keyword: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        """
        self._Limit = None
        self._Offset = None
        self._Keyword = None
        self._RiskLevel = None

    @property
    def Limit(self):
        r"""每页数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""当前页
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Keyword(self):
        r"""搜索关键字。支持标识/名称/标签/描述搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Keyword = params.get("Keyword")
        self._RiskLevel = params.get("RiskLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSystemRulesResponse(AbstractModel):
    r"""ListSystemRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Items: 详情
        :type Items: list of SystemConfigRule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
        :rtype: list of SystemConfigRule
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = SystemConfigRule()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class OpenAggregateConfigRuleRequest(AbstractModel):
    r"""OpenAggregateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        """
        self._RuleId = None
        self._AccountGroupId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAggregateConfigRuleResponse(AbstractModel):
    r"""OpenAggregateConfigRule返回参数结构体

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


class OpenConfigRecorderRequest(AbstractModel):
    r"""OpenConfigRecorder请求参数结构体

    """


class OpenConfigRecorderResponse(AbstractModel):
    r"""OpenConfigRecorder返回参数结构体

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


class OpenConfigRuleRequest(AbstractModel):
    r"""OpenConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenConfigRuleResponse(AbstractModel):
    r"""OpenConfigRule返回参数结构体

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


class PutEvaluationsRequest(AbstractModel):
    r"""PutEvaluations请求参数结构体

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
        r"""回调令牌。从自定义规则所选的scf云函数入参中取参数ResultToken值
<a href="https://cloud.tencent.com/document/product/583/9210#.E5.87.BD.E6.95.B0.E5.85.A5.E5.8F.82.3Ca-id.3D.22input.22.3E.3C.2Fa.3E" target="_blank">云函数入参说明</a>
        :rtype: str
        """
        return self._ResultToken

    @ResultToken.setter
    def ResultToken(self, ResultToken):
        self._ResultToken = ResultToken

    @property
    def Evaluations(self):
        r"""自定义规则评估结果信息。
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
    r"""PutEvaluations返回参数结构体

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


class Remediation(AbstractModel):
    r"""修复设置

    """

    def __init__(self):
        r"""
        :param _RemediationTemplateId: 修正模板 ID。
        :type RemediationTemplateId: str
        :param _RemediationId: 修正设置 ID。
        :type RemediationId: str
        :param _RemediationSourceType: 执行修正的模板来源
        :type RemediationSourceType: str
        :param _RemediationType: 修正类型。取值：
SCF：函数计算（自定义修正）。
        :type RemediationType: str
        :param _OwnerUin: 账号ID
        :type OwnerUin: str
        :param _InvokeType: 修正执行方式。取值：
MANUAL_EXECUTION：手动执行。
        :type InvokeType: str
        :param _RuleId: 规则 ID。
        :type RuleId: str
        """
        self._RemediationTemplateId = None
        self._RemediationId = None
        self._RemediationSourceType = None
        self._RemediationType = None
        self._OwnerUin = None
        self._InvokeType = None
        self._RuleId = None

    @property
    def RemediationTemplateId(self):
        r"""修正模板 ID。
        :rtype: str
        """
        return self._RemediationTemplateId

    @RemediationTemplateId.setter
    def RemediationTemplateId(self, RemediationTemplateId):
        self._RemediationTemplateId = RemediationTemplateId

    @property
    def RemediationId(self):
        r"""修正设置 ID。
        :rtype: str
        """
        return self._RemediationId

    @RemediationId.setter
    def RemediationId(self, RemediationId):
        self._RemediationId = RemediationId

    @property
    def RemediationSourceType(self):
        r"""执行修正的模板来源
        :rtype: str
        """
        return self._RemediationSourceType

    @RemediationSourceType.setter
    def RemediationSourceType(self, RemediationSourceType):
        self._RemediationSourceType = RemediationSourceType

    @property
    def RemediationType(self):
        r"""修正类型。取值：
SCF：函数计算（自定义修正）。
        :rtype: str
        """
        return self._RemediationType

    @RemediationType.setter
    def RemediationType(self, RemediationType):
        self._RemediationType = RemediationType

    @property
    def OwnerUin(self):
        r"""账号ID
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def InvokeType(self):
        r"""修正执行方式。取值：
MANUAL_EXECUTION：手动执行。
        :rtype: str
        """
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def RuleId(self):
        r"""规则 ID。
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RemediationTemplateId = params.get("RemediationTemplateId")
        self._RemediationId = params.get("RemediationId")
        self._RemediationSourceType = params.get("RemediationSourceType")
        self._RemediationType = params.get("RemediationType")
        self._OwnerUin = params.get("OwnerUin")
        self._InvokeType = params.get("InvokeType")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemediationExecutions(AbstractModel):
    r"""修正记录

    """

    def __init__(self):
        r"""
        :param _ExecutionStatus: 修正状态 1：运行中 2：成功 3：失败
        :type ExecutionStatus: int
        :param _ExecutionResourceType: 资源类型
        :type ExecutionResourceType: str
        :param _ExecutionCreateDate: 修复时间
        :type ExecutionCreateDate: str
        :param _ExecutionStatusMessage: 错误信息
        :type ExecutionStatusMessage: str
        :param _ExecutionResourceIds: 资源ID
        :type ExecutionResourceIds: str
        """
        self._ExecutionStatus = None
        self._ExecutionResourceType = None
        self._ExecutionCreateDate = None
        self._ExecutionStatusMessage = None
        self._ExecutionResourceIds = None

    @property
    def ExecutionStatus(self):
        r"""修正状态 1：运行中 2：成功 3：失败
        :rtype: int
        """
        return self._ExecutionStatus

    @ExecutionStatus.setter
    def ExecutionStatus(self, ExecutionStatus):
        self._ExecutionStatus = ExecutionStatus

    @property
    def ExecutionResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ExecutionResourceType

    @ExecutionResourceType.setter
    def ExecutionResourceType(self, ExecutionResourceType):
        self._ExecutionResourceType = ExecutionResourceType

    @property
    def ExecutionCreateDate(self):
        r"""修复时间
        :rtype: str
        """
        return self._ExecutionCreateDate

    @ExecutionCreateDate.setter
    def ExecutionCreateDate(self, ExecutionCreateDate):
        self._ExecutionCreateDate = ExecutionCreateDate

    @property
    def ExecutionStatusMessage(self):
        r"""错误信息
        :rtype: str
        """
        return self._ExecutionStatusMessage

    @ExecutionStatusMessage.setter
    def ExecutionStatusMessage(self, ExecutionStatusMessage):
        self._ExecutionStatusMessage = ExecutionStatusMessage

    @property
    def ExecutionResourceIds(self):
        r"""资源ID
        :rtype: str
        """
        return self._ExecutionResourceIds

    @ExecutionResourceIds.setter
    def ExecutionResourceIds(self, ExecutionResourceIds):
        self._ExecutionResourceIds = ExecutionResourceIds


    def _deserialize(self, params):
        self._ExecutionStatus = params.get("ExecutionStatus")
        self._ExecutionResourceType = params.get("ExecutionResourceType")
        self._ExecutionCreateDate = params.get("ExecutionCreateDate")
        self._ExecutionStatusMessage = params.get("ExecutionStatusMessage")
        self._ExecutionResourceIds = params.get("ExecutionResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceListInfo(AbstractModel):
    r"""资源列列表信息

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
        :type ResourceRegion: str
        :param _ResourceStatus: 资源状态
        :type ResourceStatus: str
        :param _ResourceDelete: 1 :已删除 2：未删除
        :type ResourceDelete: int
        :param _ResourceCreateTime: 资源创建时间
        :type ResourceCreateTime: str
        :param _Tags: 标签信息
        :type Tags: list of Tag
        :param _ResourceZone: 可用区
        :type ResourceZone: str
        :param _ComplianceResult: 合规状态
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
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceName(self):
        r"""资源名称
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceId(self):
        r"""资源ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        r"""地域
        :rtype: str
        """
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceStatus(self):
        r"""资源状态
        :rtype: str
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus

    @property
    def ResourceDelete(self):
        r"""1 :已删除 2：未删除
        :rtype: int
        """
        return self._ResourceDelete

    @ResourceDelete.setter
    def ResourceDelete(self, ResourceDelete):
        self._ResourceDelete = ResourceDelete

    @property
    def ResourceCreateTime(self):
        r"""资源创建时间
        :rtype: str
        """
        return self._ResourceCreateTime

    @ResourceCreateTime.setter
    def ResourceCreateTime(self, ResourceCreateTime):
        self._ResourceCreateTime = ResourceCreateTime

    @property
    def Tags(self):
        r"""标签信息
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceZone(self):
        r"""可用区
        :rtype: str
        """
        return self._ResourceZone

    @ResourceZone.setter
    def ResourceZone(self, ResourceZone):
        self._ResourceZone = ResourceZone

    @property
    def ComplianceResult(self):
        r"""合规状态
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
    r"""管理端规则条件

    """

    def __init__(self):
        r"""
        :param _EmptyAs: 条件为空，合规：COMPLIANT，不合规：NON_COMPLIANT，无法应用：NOT_APPLICABLE
        :type EmptyAs: str
        :param _SelectPath: 配置路径
        :type SelectPath: str
        :param _Operator: 操作运算符
        :type Operator: str
        :param _Required: 是否必须
        :type Required: bool
        :param _DesiredValue: 期望值
        :type DesiredValue: str
        """
        self._EmptyAs = None
        self._SelectPath = None
        self._Operator = None
        self._Required = None
        self._DesiredValue = None

    @property
    def EmptyAs(self):
        r"""条件为空，合规：COMPLIANT，不合规：NON_COMPLIANT，无法应用：NOT_APPLICABLE
        :rtype: str
        """
        return self._EmptyAs

    @EmptyAs.setter
    def EmptyAs(self, EmptyAs):
        self._EmptyAs = EmptyAs

    @property
    def SelectPath(self):
        r"""配置路径
        :rtype: str
        """
        return self._SelectPath

    @SelectPath.setter
    def SelectPath(self, SelectPath):
        self._SelectPath = SelectPath

    @property
    def Operator(self):
        r"""操作运算符
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Required(self):
        r"""是否必须
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def DesiredValue(self):
        r"""期望值
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
        


class StartAggregateConfigRuleEvaluationRequest(AbstractModel):
    r"""StartAggregateConfigRuleEvaluation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerType: 手动触发：MANUAL  周期触发：SCHEDULE
        :type TriggerType: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        """
        self._TriggerType = None
        self._AccountGroupId = None
        self._RuleId = None
        self._CompliancePackId = None

    @property
    def TriggerType(self):
        r"""手动触发：MANUAL  周期触发：SCHEDULE
        :rtype: str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._TriggerType = params.get("TriggerType")
        self._AccountGroupId = params.get("AccountGroupId")
        self._RuleId = params.get("RuleId")
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartAggregateConfigRuleEvaluationResponse(AbstractModel):
    r"""StartAggregateConfigRuleEvaluation返回参数结构体

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


class StartConfigRuleEvaluationRequest(AbstractModel):
    r"""StartConfigRuleEvaluation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        """
        self._RuleId = None
        self._CompliancePackId = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._CompliancePackId = params.get("CompliancePackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartConfigRuleEvaluationResponse(AbstractModel):
    r"""StartConfigRuleEvaluation返回参数结构体

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


class StartRemediationRequest(AbstractModel):
    r"""StartRemediation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则 ID
        :type RuleId: str
        """
        self._RuleId = None

    @property
    def RuleId(self):
        r"""规则 ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartRemediationResponse(AbstractModel):
    r"""StartRemediation返回参数结构体

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


class SystemCompliancePack(AbstractModel):
    r"""系统合规包信息

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _CompliancePackName: 名称
        :type CompliancePackName: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _RiskLevel: 合规包风险等级1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: int
        :param _ConfigRules: 合规包规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigRules: list of CompliancePackRuleForManage
        """
        self._CompliancePackId = None
        self._CompliancePackName = None
        self._Description = None
        self._RiskLevel = None
        self._ConfigRules = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def CompliancePackName(self):
        r"""名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RiskLevel(self):
        r"""合规包风险等级1：高风险。
2：中风险。
3：低风险。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ConfigRules(self):
        r"""合规包规则信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CompliancePackRuleForManage
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        self._CompliancePackName = params.get("CompliancePackName")
        self._Description = params.get("Description")
        self._RiskLevel = params.get("RiskLevel")
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = CompliancePackRuleForManage()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemConfigRule(AbstractModel):
    r"""管理端规则详情

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
        :type InputParameter: list of InputParameterForManage
        :param _SourceCondition: 规则触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceCondition: list of SourceConditionForManage
        :param _ResourceType: 支持的资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: list of str
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: list of str
        :param _RiskLevel: 风险等级，1，2，3
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskLevel: int
        :param _ServiceFunction: 对应的函数
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceFunction: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _TriggerType: 触发类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TriggerType: list of str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ReferenceCount: 使用次数
注意：此字段可能返回 null，表示取不到有效值。
        :type ReferenceCount: int
        :param _IdentifierType: 规则类型
        :type IdentifierType: str
        """
        self._Identifier = None
        self._RuleName = None
        self._InputParameter = None
        self._SourceCondition = None
        self._ResourceType = None
        self._Label = None
        self._RiskLevel = None
        self._ServiceFunction = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TriggerType = None
        self._Description = None
        self._ReferenceCount = None
        self._IdentifierType = None

    @property
    def Identifier(self):
        r"""规则标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Identifier

    @Identifier.setter
    def Identifier(self, Identifier):
        self._Identifier = Identifier

    @property
    def RuleName(self):
        r"""规则名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        r"""规则参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of InputParameterForManage
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def SourceCondition(self):
        r"""规则触发条件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SourceConditionForManage
        """
        return self._SourceCondition

    @SourceCondition.setter
    def SourceCondition(self, SourceCondition):
        self._SourceCondition = SourceCondition

    @property
    def ResourceType(self):
        r"""支持的资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Label(self):
        r"""标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def RiskLevel(self):
        r"""风险等级，1，2，3
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def ServiceFunction(self):
        r"""对应的函数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceFunction

    @ServiceFunction.setter
    def ServiceFunction(self, ServiceFunction):
        self._ServiceFunction = ServiceFunction

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TriggerType(self):
        r"""触发类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ReferenceCount(self):
        r"""使用次数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReferenceCount

    @ReferenceCount.setter
    def ReferenceCount(self, ReferenceCount):
        self._ReferenceCount = ReferenceCount

    @property
    def IdentifierType(self):
        r"""规则类型
        :rtype: str
        """
        return self._IdentifierType

    @IdentifierType.setter
    def IdentifierType(self, IdentifierType):
        self._IdentifierType = IdentifierType


    def _deserialize(self, params):
        self._Identifier = params.get("Identifier")
        self._RuleName = params.get("RuleName")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameterForManage()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        if params.get("SourceCondition") is not None:
            self._SourceCondition = []
            for item in params.get("SourceCondition"):
                obj = SourceConditionForManage()
                obj._deserialize(item)
                self._SourceCondition.append(obj)
        self._ResourceType = params.get("ResourceType")
        self._Label = params.get("Label")
        self._RiskLevel = params.get("RiskLevel")
        self._ServiceFunction = params.get("ServiceFunction")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TriggerType = params.get("TriggerType")
        self._Description = params.get("Description")
        self._ReferenceCount = params.get("ReferenceCount")
        self._IdentifierType = params.get("IdentifierType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签key
        :type TagKey: str
        :param _TagValue: 标签value
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签key
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签value
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
    r"""规则支持触发类型

    """

    def __init__(self):
        r"""
        :param _MessageType: 触发类型
        :type MessageType: str
        :param _MaximumExecutionFrequency: 触发时间周期
        :type MaximumExecutionFrequency: str
        """
        self._MessageType = None
        self._MaximumExecutionFrequency = None

    @property
    def MessageType(self):
        r"""触发类型
        :rtype: str
        """
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType

    @property
    def MaximumExecutionFrequency(self):
        r"""触发时间周期
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
        


class UpdateAggregateCompliancePackRequest(AbstractModel):
    r"""UpdateAggregateCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _ConfigRules: 合规包规则
        :type ConfigRules: list of CompliancePackRule
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _Description: 描述
        :type Description: str
        """
        self._CompliancePackName = None
        self._RiskLevel = None
        self._CompliancePackId = None
        self._ConfigRules = None
        self._AccountGroupId = None
        self._Description = None

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def ConfigRules(self):
        r"""合规包规则
        :rtype: list of CompliancePackRule
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._CompliancePackName = params.get("CompliancePackName")
        self._RiskLevel = params.get("RiskLevel")
        self._CompliancePackId = params.get("CompliancePackId")
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = CompliancePackRule()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._AccountGroupId = params.get("AccountGroupId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAggregateCompliancePackResponse(AbstractModel):
    r"""UpdateAggregateCompliancePack返回参数结构体

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


class UpdateAggregateCompliancePackStatusRequest(AbstractModel):
    r"""UpdateAggregateCompliancePackStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _Status: ACTIVE：启用
UN_ACTIVE ：停用
        :type Status: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        """
        self._CompliancePackId = None
        self._Status = None
        self._AccountGroupId = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def Status(self):
        r"""ACTIVE：启用
UN_ACTIVE ：停用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        self._Status = params.get("Status")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAggregateCompliancePackStatusResponse(AbstractModel):
    r"""UpdateAggregateCompliancePackStatus返回参数结构体

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


class UpdateAggregateConfigDeliverRequest(AbstractModel):
    r"""UpdateAggregateConfigDeliver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0 关闭  1 开启
        :type Status: int
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _DeliverName: 投递服务名称
        :type DeliverName: str
        :param _TargetArn: 资源六段式  
COS：qcs::cos:$region:$account:prefix/$appid/$BucketName
CLS:
qcs::cls:$region:$account:cls/topicId
        :type TargetArn: str
        :param _DeliverPrefix: 资源前缀
        :type DeliverPrefix: str
        :param _DeliverType: 投递类型  COS CLS
        :type DeliverType: str
        :param _DeliverUin: 支持跨账号投递的成员账号uin，只能是委派管理员。默认为0，即投递到管理员账号下
        :type DeliverUin: int
        :param _DeliverContentType: 1：配置变更 2： 资源列表 3：全选
        :type DeliverContentType: int
        """
        self._Status = None
        self._AccountGroupId = None
        self._DeliverName = None
        self._TargetArn = None
        self._DeliverPrefix = None
        self._DeliverType = None
        self._DeliverUin = None
        self._DeliverContentType = None

    @property
    def Status(self):
        r"""0 关闭  1 开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def DeliverName(self):
        r"""投递服务名称
        :rtype: str
        """
        return self._DeliverName

    @DeliverName.setter
    def DeliverName(self, DeliverName):
        self._DeliverName = DeliverName

    @property
    def TargetArn(self):
        r"""资源六段式  
COS：qcs::cos:$region:$account:prefix/$appid/$BucketName
CLS:
qcs::cls:$region:$account:cls/topicId
        :rtype: str
        """
        return self._TargetArn

    @TargetArn.setter
    def TargetArn(self, TargetArn):
        self._TargetArn = TargetArn

    @property
    def DeliverPrefix(self):
        r"""资源前缀
        :rtype: str
        """
        return self._DeliverPrefix

    @DeliverPrefix.setter
    def DeliverPrefix(self, DeliverPrefix):
        self._DeliverPrefix = DeliverPrefix

    @property
    def DeliverType(self):
        r"""投递类型  COS CLS
        :rtype: str
        """
        return self._DeliverType

    @DeliverType.setter
    def DeliverType(self, DeliverType):
        self._DeliverType = DeliverType

    @property
    def DeliverUin(self):
        r"""支持跨账号投递的成员账号uin，只能是委派管理员。默认为0，即投递到管理员账号下
        :rtype: int
        """
        return self._DeliverUin

    @DeliverUin.setter
    def DeliverUin(self, DeliverUin):
        self._DeliverUin = DeliverUin

    @property
    def DeliverContentType(self):
        r"""1：配置变更 2： 资源列表 3：全选
        :rtype: int
        """
        return self._DeliverContentType

    @DeliverContentType.setter
    def DeliverContentType(self, DeliverContentType):
        self._DeliverContentType = DeliverContentType


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._AccountGroupId = params.get("AccountGroupId")
        self._DeliverName = params.get("DeliverName")
        self._TargetArn = params.get("TargetArn")
        self._DeliverPrefix = params.get("DeliverPrefix")
        self._DeliverType = params.get("DeliverType")
        self._DeliverUin = params.get("DeliverUin")
        self._DeliverContentType = params.get("DeliverContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAggregateConfigDeliverResponse(AbstractModel):
    r"""UpdateAggregateConfigDeliver返回参数结构体

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


class UpdateAggregateConfigRuleRequest(AbstractModel):
    r"""UpdateAggregateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerType: 触发类型，最多支持两种
        :type TriggerType: list of TriggerType
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: int
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _AccountGroupId: 账号组ID
        :type AccountGroupId: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _InputParameter: 入参
        :type InputParameter: list of InputParameter
        :param _Description: 描述
        :type Description: str
        :param _RegionScope: 关联地域
        :type RegionScope: list of str
        :param _TagsScope: 关联标签
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope: 排除的资源ID
        :type ExcludeResourceIdsScope: list of str
        """
        self._TriggerType = None
        self._RiskLevel = None
        self._RuleId = None
        self._AccountGroupId = None
        self._RuleName = None
        self._InputParameter = None
        self._Description = None
        self._RegionScope = None
        self._TagsScope = None
        self._ExcludeResourceIdsScope = None

    @property
    def TriggerType(self):
        r"""触发类型，最多支持两种
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def RiskLevel(self):
        r"""风险等级
1：高风险。
2：中风险。
3：低风险。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def AccountGroupId(self):
        r"""账号组ID
        :rtype: str
        """
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        r"""入参
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RegionScope(self):
        r"""关联地域
        :rtype: list of str
        """
        return self._RegionScope

    @RegionScope.setter
    def RegionScope(self, RegionScope):
        self._RegionScope = RegionScope

    @property
    def TagsScope(self):
        r"""关联标签
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        r"""排除的资源ID
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope


    def _deserialize(self, params):
        if params.get("TriggerType") is not None:
            self._TriggerType = []
            for item in params.get("TriggerType"):
                obj = TriggerType()
                obj._deserialize(item)
                self._TriggerType.append(obj)
        self._RiskLevel = params.get("RiskLevel")
        self._RuleId = params.get("RuleId")
        self._AccountGroupId = params.get("AccountGroupId")
        self._RuleName = params.get("RuleName")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        self._Description = params.get("Description")
        self._RegionScope = params.get("RegionScope")
        if params.get("TagsScope") is not None:
            self._TagsScope = []
            for item in params.get("TagsScope"):
                obj = Tag()
                obj._deserialize(item)
                self._TagsScope.append(obj)
        self._ExcludeResourceIdsScope = params.get("ExcludeResourceIdsScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAggregateConfigRuleResponse(AbstractModel):
    r"""UpdateAggregateConfigRule返回参数结构体

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


class UpdateCompliancePackRequest(AbstractModel):
    r"""UpdateCompliancePack请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackName: 合规包名称
        :type CompliancePackName: str
        :param _RiskLevel: 风险等级
        :type RiskLevel: int
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _ConfigRules: 合规包规则
        :type ConfigRules: list of CompliancePackRule
        :param _Description: 描述
        :type Description: str
        """
        self._CompliancePackName = None
        self._RiskLevel = None
        self._CompliancePackId = None
        self._ConfigRules = None
        self._Description = None

    @property
    def CompliancePackName(self):
        r"""合规包名称
        :rtype: str
        """
        return self._CompliancePackName

    @CompliancePackName.setter
    def CompliancePackName(self, CompliancePackName):
        self._CompliancePackName = CompliancePackName

    @property
    def RiskLevel(self):
        r"""风险等级
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def ConfigRules(self):
        r"""合规包规则
        :rtype: list of CompliancePackRule
        """
        return self._ConfigRules

    @ConfigRules.setter
    def ConfigRules(self, ConfigRules):
        self._ConfigRules = ConfigRules

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._CompliancePackName = params.get("CompliancePackName")
        self._RiskLevel = params.get("RiskLevel")
        self._CompliancePackId = params.get("CompliancePackId")
        if params.get("ConfigRules") is not None:
            self._ConfigRules = []
            for item in params.get("ConfigRules"):
                obj = CompliancePackRule()
                obj._deserialize(item)
                self._ConfigRules.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCompliancePackResponse(AbstractModel):
    r"""UpdateCompliancePack返回参数结构体

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


class UpdateCompliancePackStatusRequest(AbstractModel):
    r"""UpdateCompliancePackStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompliancePackId: 合规包ID
        :type CompliancePackId: str
        :param _Status: ACTIVE：启用
UN_ACTIVE ：停用
        :type Status: str
        """
        self._CompliancePackId = None
        self._Status = None

    @property
    def CompliancePackId(self):
        r"""合规包ID
        :rtype: str
        """
        return self._CompliancePackId

    @CompliancePackId.setter
    def CompliancePackId(self, CompliancePackId):
        self._CompliancePackId = CompliancePackId

    @property
    def Status(self):
        r"""ACTIVE：启用
UN_ACTIVE ：停用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CompliancePackId = params.get("CompliancePackId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCompliancePackStatusResponse(AbstractModel):
    r"""UpdateCompliancePackStatus返回参数结构体

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


class UpdateConfigDeliverRequest(AbstractModel):
    r"""UpdateConfigDeliver请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 0 关闭  1 开启
        :type Status: int
        :param _DeliverName: 投递服务名称
        :type DeliverName: str
        :param _TargetArn: 资源六段式  
COS：qcs::cos:$region:$account:prefix/$appid/$BucketName
CLS:
qcs::cls:$region:$account:cls/topicId
        :type TargetArn: str
        :param _DeliverPrefix: clonfig_fix
        :type DeliverPrefix: str
        :param _DeliverType: 投递类型
        :type DeliverType: str
        :param _DeliverContentType: 1：配置变更 2： 资源列表 3：全选
        :type DeliverContentType: int
        """
        self._Status = None
        self._DeliverName = None
        self._TargetArn = None
        self._DeliverPrefix = None
        self._DeliverType = None
        self._DeliverContentType = None

    @property
    def Status(self):
        r"""0 关闭  1 开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeliverName(self):
        r"""投递服务名称
        :rtype: str
        """
        return self._DeliverName

    @DeliverName.setter
    def DeliverName(self, DeliverName):
        self._DeliverName = DeliverName

    @property
    def TargetArn(self):
        r"""资源六段式  
COS：qcs::cos:$region:$account:prefix/$appid/$BucketName
CLS:
qcs::cls:$region:$account:cls/topicId
        :rtype: str
        """
        return self._TargetArn

    @TargetArn.setter
    def TargetArn(self, TargetArn):
        self._TargetArn = TargetArn

    @property
    def DeliverPrefix(self):
        r"""clonfig_fix
        :rtype: str
        """
        return self._DeliverPrefix

    @DeliverPrefix.setter
    def DeliverPrefix(self, DeliverPrefix):
        self._DeliverPrefix = DeliverPrefix

    @property
    def DeliverType(self):
        r"""投递类型
        :rtype: str
        """
        return self._DeliverType

    @DeliverType.setter
    def DeliverType(self, DeliverType):
        self._DeliverType = DeliverType

    @property
    def DeliverContentType(self):
        r"""1：配置变更 2： 资源列表 3：全选
        :rtype: int
        """
        return self._DeliverContentType

    @DeliverContentType.setter
    def DeliverContentType(self, DeliverContentType):
        self._DeliverContentType = DeliverContentType


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._DeliverName = params.get("DeliverName")
        self._TargetArn = params.get("TargetArn")
        self._DeliverPrefix = params.get("DeliverPrefix")
        self._DeliverType = params.get("DeliverType")
        self._DeliverContentType = params.get("DeliverContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConfigDeliverResponse(AbstractModel):
    r"""UpdateConfigDeliver返回参数结构体

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


class UpdateConfigRecorderRequest(AbstractModel):
    r"""UpdateConfigRecorder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceTypes: 资源类型列表
        :type ResourceTypes: list of str
        """
        self._ResourceTypes = None

    @property
    def ResourceTypes(self):
        r"""资源类型列表
        :rtype: list of str
        """
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes


    def _deserialize(self, params):
        self._ResourceTypes = params.get("ResourceTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConfigRecorderResponse(AbstractModel):
    r"""UpdateConfigRecorder返回参数结构体

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


class UpdateConfigRuleRequest(AbstractModel):
    r"""UpdateConfigRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerType: 触发类型，最多支持两种
        :type TriggerType: list of TriggerType
        :param _RiskLevel: 风险等级
1：高风险。
2：中风险。
3：低风险。
        :type RiskLevel: int
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _InputParameter: 入参
        :type InputParameter: list of InputParameter
        :param _Description: 描述
        :type Description: str
        :param _RegionsScope: 规则评估地域范围，规则仅对指定地域中的资源生效。
支持的地域范围config:ListResourceRegions返回的地域
        :type RegionsScope: list of str
        :param _TagsScope: 规则评估标签范围，规则仅对绑定指定标签的资源生效。
        :type TagsScope: list of Tag
        :param _ExcludeResourceIdsScope: 规则对指定资源ID无效，即不对该资源执行评估。
        :type ExcludeResourceIdsScope: list of str
        """
        self._TriggerType = None
        self._RiskLevel = None
        self._RuleId = None
        self._RuleName = None
        self._InputParameter = None
        self._Description = None
        self._RegionsScope = None
        self._TagsScope = None
        self._ExcludeResourceIdsScope = None

    @property
    def TriggerType(self):
        r"""触发类型，最多支持两种
        :rtype: list of TriggerType
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def RiskLevel(self):
        r"""风险等级
1：高风险。
2：中风险。
3：低风险。
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def InputParameter(self):
        r"""入参
        :rtype: list of InputParameter
        """
        return self._InputParameter

    @InputParameter.setter
    def InputParameter(self, InputParameter):
        self._InputParameter = InputParameter

    @property
    def Description(self):
        r"""描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def RegionsScope(self):
        r"""规则评估地域范围，规则仅对指定地域中的资源生效。
支持的地域范围config:ListResourceRegions返回的地域
        :rtype: list of str
        """
        return self._RegionsScope

    @RegionsScope.setter
    def RegionsScope(self, RegionsScope):
        self._RegionsScope = RegionsScope

    @property
    def TagsScope(self):
        r"""规则评估标签范围，规则仅对绑定指定标签的资源生效。
        :rtype: list of Tag
        """
        return self._TagsScope

    @TagsScope.setter
    def TagsScope(self, TagsScope):
        self._TagsScope = TagsScope

    @property
    def ExcludeResourceIdsScope(self):
        r"""规则对指定资源ID无效，即不对该资源执行评估。
        :rtype: list of str
        """
        return self._ExcludeResourceIdsScope

    @ExcludeResourceIdsScope.setter
    def ExcludeResourceIdsScope(self, ExcludeResourceIdsScope):
        self._ExcludeResourceIdsScope = ExcludeResourceIdsScope


    def _deserialize(self, params):
        if params.get("TriggerType") is not None:
            self._TriggerType = []
            for item in params.get("TriggerType"):
                obj = TriggerType()
                obj._deserialize(item)
                self._TriggerType.append(obj)
        self._RiskLevel = params.get("RiskLevel")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        if params.get("InputParameter") is not None:
            self._InputParameter = []
            for item in params.get("InputParameter"):
                obj = InputParameter()
                obj._deserialize(item)
                self._InputParameter.append(obj)
        self._Description = params.get("Description")
        self._RegionsScope = params.get("RegionsScope")
        if params.get("TagsScope") is not None:
            self._TagsScope = []
            for item in params.get("TagsScope"):
                obj = Tag()
                obj._deserialize(item)
                self._TagsScope.append(obj)
        self._ExcludeResourceIdsScope = params.get("ExcludeResourceIdsScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateConfigRuleResponse(AbstractModel):
    r"""UpdateConfigRule返回参数结构体

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


class UpdateRemediationRequest(AbstractModel):
    r"""UpdateRemediation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RemediationId: 修正设置 ID
        :type RemediationId: str
        :param _RemediationType: 修正类型。取值： SCF：函数计算（自定义修正）。
        :type RemediationType: str
        :param _RemediationTemplateId: 修正模板 ID
        :type RemediationTemplateId: str
        :param _InvokeType: 修正执行方式。取值：  NON_EXECUTION：不执行。  AUTO_EXECUTION：自动执行。  MANUAL_EXECUTION：手动执行。  NOT_CONFIG：未设置。
        :type InvokeType: str
        :param _SourceType: 执行修正来源
        :type SourceType: str
        """
        self._RemediationId = None
        self._RemediationType = None
        self._RemediationTemplateId = None
        self._InvokeType = None
        self._SourceType = None

    @property
    def RemediationId(self):
        r"""修正设置 ID
        :rtype: str
        """
        return self._RemediationId

    @RemediationId.setter
    def RemediationId(self, RemediationId):
        self._RemediationId = RemediationId

    @property
    def RemediationType(self):
        r"""修正类型。取值： SCF：函数计算（自定义修正）。
        :rtype: str
        """
        return self._RemediationType

    @RemediationType.setter
    def RemediationType(self, RemediationType):
        self._RemediationType = RemediationType

    @property
    def RemediationTemplateId(self):
        r"""修正模板 ID
        :rtype: str
        """
        return self._RemediationTemplateId

    @RemediationTemplateId.setter
    def RemediationTemplateId(self, RemediationTemplateId):
        self._RemediationTemplateId = RemediationTemplateId

    @property
    def InvokeType(self):
        r"""修正执行方式。取值：  NON_EXECUTION：不执行。  AUTO_EXECUTION：自动执行。  MANUAL_EXECUTION：手动执行。  NOT_CONFIG：未设置。
        :rtype: str
        """
        return self._InvokeType

    @InvokeType.setter
    def InvokeType(self, InvokeType):
        self._InvokeType = InvokeType

    @property
    def SourceType(self):
        r"""执行修正来源
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType


    def _deserialize(self, params):
        self._RemediationId = params.get("RemediationId")
        self._RemediationType = params.get("RemediationType")
        self._RemediationTemplateId = params.get("RemediationTemplateId")
        self._InvokeType = params.get("InvokeType")
        self._SourceType = params.get("SourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRemediationResponse(AbstractModel):
    r"""UpdateRemediation返回参数结构体

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


class UserConfigResource(AbstractModel):
    r"""资源类型

    """

    def __init__(self):
        r"""
        :param _Product: 产品
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _ProductName: 产品名
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _ResourceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _ResourceTypeName: 资源类型名
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTypeName: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._Product = None
        self._ProductName = None
        self._ResourceType = None
        self._ResourceTypeName = None
        self._UpdateTime = None

    @property
    def Product(self):
        r"""产品
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProductName(self):
        r"""产品名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ResourceType(self):
        r"""资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def ResourceTypeName(self):
        r"""资源类型名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceTypeName

    @ResourceTypeName.setter
    def ResourceTypeName(self, ResourceTypeName):
        self._ResourceTypeName = ResourceTypeName

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProductName = params.get("ProductName")
        self._ResourceType = params.get("ResourceType")
        self._ResourceTypeName = params.get("ResourceTypeName")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        