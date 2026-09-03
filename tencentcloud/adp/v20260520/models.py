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


class AICallConfig(AbstractModel):
    r"""智能通话配置

    """

    def __init__(self):
        r"""
        :param _DigitalHuman: 数智人配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DigitalHuman: :class:`tencentcloud.adp.v20260520.models.DigitalHumanConfig`
        :param _EnableDigitalHuman: 启用数智人
        :type EnableDigitalHuman: bool
        :param _EnableVoiceCall: 启用语音通话
        :type EnableVoiceCall: bool
        :param _EnableVoiceInteract: 启用语音互动功能
        :type EnableVoiceInteract: bool
        :param _Voice: 音色配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Voice: :class:`tencentcloud.adp.v20260520.models.VoiceConfig`
        """
        self._DigitalHuman = None
        self._EnableDigitalHuman = None
        self._EnableVoiceCall = None
        self._EnableVoiceInteract = None
        self._Voice = None

    @property
    def DigitalHuman(self):
        r"""数智人配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.DigitalHumanConfig`
        """
        return self._DigitalHuman

    @DigitalHuman.setter
    def DigitalHuman(self, DigitalHuman):
        self._DigitalHuman = DigitalHuman

    @property
    def EnableDigitalHuman(self):
        r"""启用数智人
        :rtype: bool
        """
        return self._EnableDigitalHuman

    @EnableDigitalHuman.setter
    def EnableDigitalHuman(self, EnableDigitalHuman):
        self._EnableDigitalHuman = EnableDigitalHuman

    @property
    def EnableVoiceCall(self):
        r"""启用语音通话
        :rtype: bool
        """
        return self._EnableVoiceCall

    @EnableVoiceCall.setter
    def EnableVoiceCall(self, EnableVoiceCall):
        self._EnableVoiceCall = EnableVoiceCall

    @property
    def EnableVoiceInteract(self):
        r"""启用语音互动功能
        :rtype: bool
        """
        return self._EnableVoiceInteract

    @EnableVoiceInteract.setter
    def EnableVoiceInteract(self, EnableVoiceInteract):
        self._EnableVoiceInteract = EnableVoiceInteract

    @property
    def Voice(self):
        r"""音色配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.VoiceConfig`
        """
        return self._Voice

    @Voice.setter
    def Voice(self, Voice):
        self._Voice = Voice


    def _deserialize(self, params):
        if params.get("DigitalHuman") is not None:
            self._DigitalHuman = DigitalHumanConfig()
            self._DigitalHuman._deserialize(params.get("DigitalHuman"))
        self._EnableDigitalHuman = params.get("EnableDigitalHuman")
        self._EnableVoiceCall = params.get("EnableVoiceCall")
        self._EnableVoiceInteract = params.get("EnableVoiceInteract")
        if params.get("Voice") is not None:
            self._Voice = VoiceConfig()
            self._Voice._deserialize(params.get("Voice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AIOptimizeModel(AbstractModel):
    r"""AI一键优化模型配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountInfo(AbstractModel):
    r"""员工信息

    """

    def __init__(self):
        r"""
        :param _AccountUin: <p>员工子账号id</p>
        :type AccountUin: str
        :param _NickName: <p>员工昵称</p>
        :type NickName: str
        :param _Avatar: <p>员工头像</p>
        :type Avatar: str
        """
        self._AccountUin = None
        self._NickName = None
        self._Avatar = None

    @property
    def AccountUin(self):
        r"""<p>员工子账号id</p>
        :rtype: str
        """
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def NickName(self):
        r"""<p>员工昵称</p>
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Avatar(self):
        r"""<p>员工头像</p>
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar


    def _deserialize(self, params):
        self._AccountUin = params.get("AccountUin")
        self._NickName = params.get("NickName")
        self._Avatar = params.get("Avatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentAdvancedConfig(AbstractModel):
    r"""Agent高级设置

    """

    def __init__(self):
        r"""
        :param _MaxReasoningRound: <p>最大推理轮数</p>
        :type MaxReasoningRound: int
        """
        self._MaxReasoningRound = None

    @property
    def MaxReasoningRound(self):
        r"""<p>最大推理轮数</p>
        :rtype: int
        """
        return self._MaxReasoningRound

    @MaxReasoningRound.setter
    def MaxReasoningRound(self, MaxReasoningRound):
        self._MaxReasoningRound = MaxReasoningRound


    def _deserialize(self, params):
        self._MaxReasoningRound = params.get("MaxReasoningRound")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentCollaborationConfig(AbstractModel):
    r"""[数据结构定义] Agent协同配置

    """

    def __init__(self):
        r"""
        :param _AgentCollaborationMode: 协同方式。枚举值: 1:自由转交：Agent之间可自由传递任务, 2:工作流编排：基于预定义流程的协同, 3:Plan-and-Execute：规划与执行分离的协同模式
        :type AgentCollaborationMode: int
        :param _WorkflowId: 工作流Id
        :type WorkflowId: str
        :param _WorkflowName: 工作流名称
        :type WorkflowName: str
        """
        self._AgentCollaborationMode = None
        self._WorkflowId = None
        self._WorkflowName = None

    @property
    def AgentCollaborationMode(self):
        r"""协同方式。枚举值: 1:自由转交：Agent之间可自由传递任务, 2:工作流编排：基于预定义流程的协同, 3:Plan-and-Execute：规划与执行分离的协同模式
        :rtype: int
        """
        return self._AgentCollaborationMode

    @AgentCollaborationMode.setter
    def AgentCollaborationMode(self, AgentCollaborationMode):
        self._AgentCollaborationMode = AgentCollaborationMode

    @property
    def WorkflowId(self):
        r"""工作流Id
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""工作流名称
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName


    def _deserialize(self, params):
        self._AgentCollaborationMode = params.get("AgentCollaborationMode")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentDetail(AbstractModel):
    r"""Agent 详情

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent ID</p>
        :type AgentId: str
        :param _Profile: <p>Agent基本配置</p>
        :type Profile: :class:`tencentcloud.adp.v20260520.models.AgentProfile`
        :param _Instructions: <p>系统提示词</p>
        :type Instructions: str
        :param _Model: <p>模型信息</p>
        :type Model: :class:`tencentcloud.adp.v20260520.models.AgentModelConfig`
        :param _ToolList: <p>工具详情</p>
        :type ToolList: list of AgentTool
        :param _PluginList: <p>插件配置</p>
        :type PluginList: list of AgentPlugin
        :param _SkillList: <p>技能详情</p>
        :type SkillList: list of AgentSkill
        :param _AdvancedConfig: <p>高级配置</p>
        :type AdvancedConfig: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        :param _ExternalToolList: <p>调用方执行的 Function Tool 列表</p><p>入参限制：仅在 C 端用户态 Agent 场景可用，B 端配置态 Agent 忽略该字段与</p>
        :type ExternalToolList: list of AgentExternalToolConfig
        """
        self._AgentId = None
        self._Profile = None
        self._Instructions = None
        self._Model = None
        self._ToolList = None
        self._PluginList = None
        self._SkillList = None
        self._AdvancedConfig = None
        self._ExternalToolList = None

    @property
    def AgentId(self):
        r"""<p>Agent ID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Profile(self):
        r"""<p>Agent基本配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Instructions(self):
        r"""<p>系统提示词</p>
        :rtype: str
        """
        return self._Instructions

    @Instructions.setter
    def Instructions(self, Instructions):
        self._Instructions = Instructions

    @property
    def Model(self):
        r"""<p>模型信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentModelConfig`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def ToolList(self):
        r"""<p>工具详情</p>
        :rtype: list of AgentTool
        """
        return self._ToolList

    @ToolList.setter
    def ToolList(self, ToolList):
        self._ToolList = ToolList

    @property
    def PluginList(self):
        r"""<p>插件配置</p>
        :rtype: list of AgentPlugin
        """
        return self._PluginList

    @PluginList.setter
    def PluginList(self, PluginList):
        self._PluginList = PluginList

    @property
    def SkillList(self):
        r"""<p>技能详情</p>
        :rtype: list of AgentSkill
        """
        return self._SkillList

    @SkillList.setter
    def SkillList(self, SkillList):
        self._SkillList = SkillList

    @property
    def AdvancedConfig(self):
        r"""<p>高级配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig

    @property
    def ExternalToolList(self):
        r"""<p>调用方执行的 Function Tool 列表</p><p>入参限制：仅在 C 端用户态 Agent 场景可用，B 端配置态 Agent 忽略该字段与</p>
        :rtype: list of AgentExternalToolConfig
        """
        return self._ExternalToolList

    @ExternalToolList.setter
    def ExternalToolList(self, ExternalToolList):
        self._ExternalToolList = ExternalToolList


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        if params.get("Profile") is not None:
            self._Profile = AgentProfile()
            self._Profile._deserialize(params.get("Profile"))
        self._Instructions = params.get("Instructions")
        if params.get("Model") is not None:
            self._Model = AgentModelConfig()
            self._Model._deserialize(params.get("Model"))
        if params.get("ToolList") is not None:
            self._ToolList = []
            for item in params.get("ToolList"):
                obj = AgentTool()
                obj._deserialize(item)
                self._ToolList.append(obj)
        if params.get("PluginList") is not None:
            self._PluginList = []
            for item in params.get("PluginList"):
                obj = AgentPlugin()
                obj._deserialize(item)
                self._PluginList.append(obj)
        if params.get("SkillList") is not None:
            self._SkillList = []
            for item in params.get("SkillList"):
                obj = AgentSkill()
                obj._deserialize(item)
                self._SkillList.append(obj)
        if params.get("AdvancedConfig") is not None:
            self._AdvancedConfig = AgentAdvancedConfig()
            self._AdvancedConfig._deserialize(params.get("AdvancedConfig"))
        if params.get("ExternalToolList") is not None:
            self._ExternalToolList = []
            for item in params.get("ExternalToolList"):
                obj = AgentExternalToolConfig()
                obj._deserialize(item)
                self._ExternalToolList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentExternalToolConfig(AbstractModel):
    r"""调用方执行的 Function Tool 配置

    """

    def __init__(self):
        r"""
        :param _Type: <p>工具类型</p><p>入参限制：目前仅支持 &quot;function&quot;</p>
        :type Type: str
        :param _Name: <p>工具名称</p>
        :type Name: str
        :param _Description: <p>工具描述</p>
        :type Description: str
        :param _Parameters: <p>工具入参定义</p>
        :type Parameters: list of RequestParam
        """
        self._Type = None
        self._Name = None
        self._Description = None
        self._Parameters = None

    @property
    def Type(self):
        r"""<p>工具类型</p><p>入参限制：目前仅支持 &quot;function&quot;</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""<p>工具名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>工具描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Parameters(self):
        r"""<p>工具入参定义</p>
        :rtype: list of RequestParam
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentInput(AbstractModel):
    r"""Agent输入值，支持直接赋值和引用

    """

    def __init__(self):
        r"""
        :param _InputType: <p>输入来源类型：0 用户输入，3 自定义变量（API参数）</p>
        :type InputType: int
        :param _UserInputValue: <p>用户手写输入</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInputValue: :class:`tencentcloud.adp.v20260520.models.AgentUserInputValue`
        :param _SystemVariable: <p>系统参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SystemVariable: :class:`tencentcloud.adp.v20260520.models.AgentSystemVariable`
        :param _CustomVariableId: <p>自定义变量（API参数）</p>
        :type CustomVariableId: str
        :param _EnvVariableId: <p>环境变量参数</p>
        :type EnvVariableId: str
        :param _AppVariableId: <p>应用变量参数</p>
        :type AppVariableId: str
        """
        self._InputType = None
        self._UserInputValue = None
        self._SystemVariable = None
        self._CustomVariableId = None
        self._EnvVariableId = None
        self._AppVariableId = None

    @property
    def InputType(self):
        r"""<p>输入来源类型：0 用户输入，3 自定义变量（API参数）</p>
        :rtype: int
        """
        return self._InputType

    @InputType.setter
    def InputType(self, InputType):
        self._InputType = InputType

    @property
    def UserInputValue(self):
        r"""<p>用户手写输入</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentUserInputValue`
        """
        return self._UserInputValue

    @UserInputValue.setter
    def UserInputValue(self, UserInputValue):
        self._UserInputValue = UserInputValue

    @property
    def SystemVariable(self):
        r"""<p>系统参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentSystemVariable`
        """
        return self._SystemVariable

    @SystemVariable.setter
    def SystemVariable(self, SystemVariable):
        self._SystemVariable = SystemVariable

    @property
    def CustomVariableId(self):
        r"""<p>自定义变量（API参数）</p>
        :rtype: str
        """
        return self._CustomVariableId

    @CustomVariableId.setter
    def CustomVariableId(self, CustomVariableId):
        self._CustomVariableId = CustomVariableId

    @property
    def EnvVariableId(self):
        r"""<p>环境变量参数</p>
        :rtype: str
        """
        return self._EnvVariableId

    @EnvVariableId.setter
    def EnvVariableId(self, EnvVariableId):
        self._EnvVariableId = EnvVariableId

    @property
    def AppVariableId(self):
        r"""<p>应用变量参数</p>
        :rtype: str
        """
        return self._AppVariableId

    @AppVariableId.setter
    def AppVariableId(self, AppVariableId):
        self._AppVariableId = AppVariableId


    def _deserialize(self, params):
        self._InputType = params.get("InputType")
        if params.get("UserInputValue") is not None:
            self._UserInputValue = AgentUserInputValue()
            self._UserInputValue._deserialize(params.get("UserInputValue"))
        if params.get("SystemVariable") is not None:
            self._SystemVariable = AgentSystemVariable()
            self._SystemVariable._deserialize(params.get("SystemVariable"))
        self._CustomVariableId = params.get("CustomVariableId")
        self._EnvVariableId = params.get("EnvVariableId")
        self._AppVariableId = params.get("AppVariableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentModelConfig(AbstractModel):
    r"""Agent 配置里面的模型定义

    """

    def __init__(self):
        r"""
        :param _ModelId: <p>模型唯一id</p>
        :type ModelId: str
        :param _Alias: <p>模型别名</p>
        :type Alias: str
        :param _ContextWordsLimit: <p>模型上下文长度字符限制</p>
        :type ContextWordsLimit: int
        :param _InstructionsWordsLimit: <p>指令长度字符限制</p>
        :type InstructionsWordsLimit: int
        :param _ModelParameters: <p>模型参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelParameters: :class:`tencentcloud.adp.v20260520.models.ModelParams`
        """
        self._ModelId = None
        self._Alias = None
        self._ContextWordsLimit = None
        self._InstructionsWordsLimit = None
        self._ModelParameters = None

    @property
    def ModelId(self):
        r"""<p>模型唯一id</p>
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def Alias(self):
        r"""<p>模型别名</p>
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def ContextWordsLimit(self):
        r"""<p>模型上下文长度字符限制</p>
        :rtype: int
        """
        return self._ContextWordsLimit

    @ContextWordsLimit.setter
    def ContextWordsLimit(self, ContextWordsLimit):
        self._ContextWordsLimit = ContextWordsLimit

    @property
    def InstructionsWordsLimit(self):
        r"""<p>指令长度字符限制</p>
        :rtype: int
        """
        return self._InstructionsWordsLimit

    @InstructionsWordsLimit.setter
    def InstructionsWordsLimit(self, InstructionsWordsLimit):
        self._InstructionsWordsLimit = InstructionsWordsLimit

    @property
    def ModelParameters(self):
        r"""<p>模型参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelParams`
        """
        return self._ModelParameters

    @ModelParameters.setter
    def ModelParameters(self, ModelParameters):
        self._ModelParameters = ModelParameters


    def _deserialize(self, params):
        self._ModelId = params.get("ModelId")
        self._Alias = params.get("Alias")
        self._ContextWordsLimit = params.get("ContextWordsLimit")
        self._InstructionsWordsLimit = params.get("InstructionsWordsLimit")
        if params.get("ModelParameters") is not None:
            self._ModelParameters = ModelParams()
            self._ModelParameters._deserialize(params.get("ModelParameters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPlugin(AbstractModel):
    r"""Agent 的插件信息

    """

    def __init__(self):
        r"""
        :param _Config: <p>插件基本配置</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.AgentPluginConfig`
        :param _Name: <p>插件名称</p>
        :type Name: str
        :param _IconUrl: <p>插件图标url</p>
        :type IconUrl: str
        :param _Description: <p>插件描述</p>
        :type Description: str
        :param _PluginClass: <p>插件产品分类</p><p>枚举值：</p><ul><li>0： 普通插件</li><li>1： 连接器类插件</li></ul>
        :type PluginClass: int
        :param _Status: <p>插件状态</p><p>枚举值：</p><ul><li>0： 未知</li><li>1： 可用</li><li>2： 不可用</li></ul>
        :type Status: int
        :param _AuthConfigStatus: <p>插件鉴权配置状态</p><p>枚举值：</p><ul><li>0： 不需要授权</li><li>1： 未配置</li><li>2： 已配置</li></ul>
        :type AuthConfigStatus: int
        """
        self._Config = None
        self._Name = None
        self._IconUrl = None
        self._Description = None
        self._PluginClass = None
        self._Status = None
        self._AuthConfigStatus = None

    @property
    def Config(self):
        r"""<p>插件基本配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentPluginConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Name(self):
        r"""<p>插件名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IconUrl(self):
        r"""<p>插件图标url</p>
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Description(self):
        r"""<p>插件描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PluginClass(self):
        r"""<p>插件产品分类</p><p>枚举值：</p><ul><li>0： 普通插件</li><li>1： 连接器类插件</li></ul>
        :rtype: int
        """
        return self._PluginClass

    @PluginClass.setter
    def PluginClass(self, PluginClass):
        self._PluginClass = PluginClass

    @property
    def Status(self):
        r"""<p>插件状态</p><p>枚举值：</p><ul><li>0： 未知</li><li>1： 可用</li><li>2： 不可用</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def AuthConfigStatus(self):
        r"""<p>插件鉴权配置状态</p><p>枚举值：</p><ul><li>0： 不需要授权</li><li>1： 未配置</li><li>2： 已配置</li></ul>
        :rtype: int
        """
        return self._AuthConfigStatus

    @AuthConfigStatus.setter
    def AuthConfigStatus(self, AuthConfigStatus):
        self._AuthConfigStatus = AuthConfigStatus


    def _deserialize(self, params):
        if params.get("Config") is not None:
            self._Config = AgentPluginConfig()
            self._Config._deserialize(params.get("Config"))
        self._Name = params.get("Name")
        self._IconUrl = params.get("IconUrl")
        self._Description = params.get("Description")
        self._PluginClass = params.get("PluginClass")
        self._Status = params.get("Status")
        self._AuthConfigStatus = params.get("AuthConfigStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPluginConfig(AbstractModel):
    r"""Agent 的插件基本配置

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _HeaderParameterList: <p>插件 Header 参数</p>
        :type HeaderParameterList: list of AgentPluginParameter
        :param _QueryParameterList: <p>插件 Query 参数</p>
        :type QueryParameterList: list of AgentPluginParameter
        :param _EnableCamRoleAuth: <p>是否使用CAM一键授权，仅 auth_type=2时生效</p>
        :type EnableCamRoleAuth: bool
        :param _AuthType: <p>授权类型</p><p>枚举值：</p><ul><li>0： 无鉴权</li><li>1： API Key</li><li>2： CAM授权</li><li>3： OAuth2.0授权</li></ul>
        :type AuthType: int
        :param _OAuthConsent: <p>OAuth 授权同意模式；0-开发者授权；1-使用者授权（仅在auth_type=3时生效）</p>
        :type OAuthConsent: int
        """
        self._PluginId = None
        self._HeaderParameterList = None
        self._QueryParameterList = None
        self._EnableCamRoleAuth = None
        self._AuthType = None
        self._OAuthConsent = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def HeaderParameterList(self):
        r"""<p>插件 Header 参数</p>
        :rtype: list of AgentPluginParameter
        """
        return self._HeaderParameterList

    @HeaderParameterList.setter
    def HeaderParameterList(self, HeaderParameterList):
        self._HeaderParameterList = HeaderParameterList

    @property
    def QueryParameterList(self):
        r"""<p>插件 Query 参数</p>
        :rtype: list of AgentPluginParameter
        """
        return self._QueryParameterList

    @QueryParameterList.setter
    def QueryParameterList(self, QueryParameterList):
        self._QueryParameterList = QueryParameterList

    @property
    def EnableCamRoleAuth(self):
        r"""<p>是否使用CAM一键授权，仅 auth_type=2时生效</p>
        :rtype: bool
        """
        return self._EnableCamRoleAuth

    @EnableCamRoleAuth.setter
    def EnableCamRoleAuth(self, EnableCamRoleAuth):
        self._EnableCamRoleAuth = EnableCamRoleAuth

    @property
    def AuthType(self):
        r"""<p>授权类型</p><p>枚举值：</p><ul><li>0： 无鉴权</li><li>1： API Key</li><li>2： CAM授权</li><li>3： OAuth2.0授权</li></ul>
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def OAuthConsent(self):
        r"""<p>OAuth 授权同意模式；0-开发者授权；1-使用者授权（仅在auth_type=3时生效）</p>
        :rtype: int
        """
        return self._OAuthConsent

    @OAuthConsent.setter
    def OAuthConsent(self, OAuthConsent):
        self._OAuthConsent = OAuthConsent


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        if params.get("HeaderParameterList") is not None:
            self._HeaderParameterList = []
            for item in params.get("HeaderParameterList"):
                obj = AgentPluginParameter()
                obj._deserialize(item)
                self._HeaderParameterList.append(obj)
        if params.get("QueryParameterList") is not None:
            self._QueryParameterList = []
            for item in params.get("QueryParameterList"):
                obj = AgentPluginParameter()
                obj._deserialize(item)
                self._QueryParameterList.append(obj)
        self._EnableCamRoleAuth = params.get("EnableCamRoleAuth")
        self._AuthType = params.get("AuthType")
        self._OAuthConsent = params.get("OAuthConsent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentPluginParameter(AbstractModel):
    r"""Agent 插件参数配置

    """

    def __init__(self):
        r"""
        :param _Name: <p>参数名称</p>
        :type Name: str
        :param _IsRequired: <p>是否必填</p>
        :type IsRequired: bool
        :param _Input: <p>输入的值</p>
        :type Input: :class:`tencentcloud.adp.v20260520.models.AgentInput`
        """
        self._Name = None
        self._IsRequired = None
        self._Input = None

    @property
    def Name(self):
        r"""<p>参数名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IsRequired(self):
        r"""<p>是否必填</p>
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def Input(self):
        r"""<p>输入的值</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IsRequired = params.get("IsRequired")
        if params.get("Input") is not None:
            self._Input = AgentInput()
            self._Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentProfile(AbstractModel):
    r"""Agent 基本配置

    """

    def __init__(self):
        r"""
        :param _Name: <p>Agent名称</p>
        :type Name: str
        :param _IconUrl: <p>图标URL</p>
        :type IconUrl: str
        :param _Role: <p>Agent 角色：0=主 / 1=子</p>
        :type Role: int
        :param _Description: <p>Agent 描述</p>
        :type Description: str
        :param _AppName: <p>应用名称</p>
        :type AppName: str
        :param _Developer: <p>开发者</p>
        :type Developer: str
        :param _ParentAgentId: <p>主AgentId，只读，不可通过修改接口进行变更</p>
        :type ParentAgentId: str
        """
        self._Name = None
        self._IconUrl = None
        self._Role = None
        self._Description = None
        self._AppName = None
        self._Developer = None
        self._ParentAgentId = None

    @property
    def Name(self):
        r"""<p>Agent名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IconUrl(self):
        r"""<p>图标URL</p>
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Role(self):
        r"""<p>Agent 角色：0=主 / 1=子</p>
        :rtype: int
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Description(self):
        r"""<p>Agent 描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def AppName(self):
        r"""<p>应用名称</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def Developer(self):
        r"""<p>开发者</p>
        :rtype: str
        """
        return self._Developer

    @Developer.setter
    def Developer(self, Developer):
        self._Developer = Developer

    @property
    def ParentAgentId(self):
        r"""<p>主AgentId，只读，不可通过修改接口进行变更</p>
        :rtype: str
        """
        return self._ParentAgentId

    @ParentAgentId.setter
    def ParentAgentId(self, ParentAgentId):
        self._ParentAgentId = ParentAgentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IconUrl = params.get("IconUrl")
        self._Role = params.get("Role")
        self._Description = params.get("Description")
        self._AppName = params.get("AppName")
        self._Developer = params.get("Developer")
        self._ParentAgentId = params.get("ParentAgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentRelease(AbstractModel):
    r"""Agent发布项目详情

    """

    def __init__(self):
        r"""
        :param _ItemName: <p>名称</p>
        :type ItemName: str
        :param _UpdateTime: <p>更新时间, unix 秒时间戳 (s)</p>
        :type UpdateTime: str
        :param _ActionDescription: <p>动作描述</p>
        :type ActionDescription: str
        :param _ReleaseMessage: <p>变更为 测试</p>
        :type ReleaseMessage: str
        """
        self._ItemName = None
        self._UpdateTime = None
        self._ActionDescription = None
        self._ReleaseMessage = None

    @property
    def ItemName(self):
        r"""<p>名称</p>
        :rtype: str
        """
        return self._ItemName

    @ItemName.setter
    def ItemName(self, ItemName):
        self._ItemName = ItemName

    @property
    def UpdateTime(self):
        r"""<p>更新时间, unix 秒时间戳 (s)</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ActionDescription(self):
        r"""<p>动作描述</p>
        :rtype: str
        """
        return self._ActionDescription

    @ActionDescription.setter
    def ActionDescription(self, ActionDescription):
        self._ActionDescription = ActionDescription

    @property
    def ReleaseMessage(self):
        r"""<p>变更为 测试</p>
        :rtype: str
        """
        return self._ReleaseMessage

    @ReleaseMessage.setter
    def ReleaseMessage(self, ReleaseMessage):
        self._ReleaseMessage = ReleaseMessage


    def _deserialize(self, params):
        self._ItemName = params.get("ItemName")
        self._UpdateTime = params.get("UpdateTime")
        self._ActionDescription = params.get("ActionDescription")
        self._ReleaseMessage = params.get("ReleaseMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentReleasePreview(AbstractModel):
    r"""Agent 发布预览信息

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>AgentID</p>
        :type AgentId: str
        :param _Name: <p>Agent名称</p>
        :type Name: str
        :param _UpdateTime: <p>更新时间, unix 秒时间戳 (s)</p>
        :type UpdateTime: str
        :param _Action: <p>状态, 状态值：1:新增, 2:修改, 3:删除</p>
        :type Action: int
        :param _ActionDescription: <p>动作描述</p>
        :type ActionDescription: str
        :param _Message: <p>发布消息</p>
        :type Message: str
        :param _ReleaseList: <p>发布详情</p>
        :type ReleaseList: list of AgentRelease
        """
        self._AgentId = None
        self._Name = None
        self._UpdateTime = None
        self._Action = None
        self._ActionDescription = None
        self._Message = None
        self._ReleaseList = None

    @property
    def AgentId(self):
        r"""<p>AgentID</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Name(self):
        r"""<p>Agent名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UpdateTime(self):
        r"""<p>更新时间, unix 秒时间戳 (s)</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Action(self):
        r"""<p>状态, 状态值：1:新增, 2:修改, 3:删除</p>
        :rtype: int
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ActionDescription(self):
        r"""<p>动作描述</p>
        :rtype: str
        """
        return self._ActionDescription

    @ActionDescription.setter
    def ActionDescription(self, ActionDescription):
        self._ActionDescription = ActionDescription

    @property
    def Message(self):
        r"""<p>发布消息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ReleaseList(self):
        r"""<p>发布详情</p>
        :rtype: list of AgentRelease
        """
        return self._ReleaseList

    @ReleaseList.setter
    def ReleaseList(self, ReleaseList):
        self._ReleaseList = ReleaseList


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        self._Name = params.get("Name")
        self._UpdateTime = params.get("UpdateTime")
        self._Action = params.get("Action")
        self._ActionDescription = params.get("ActionDescription")
        self._Message = params.get("Message")
        if params.get("ReleaseList") is not None:
            self._ReleaseList = []
            for item in params.get("ReleaseList"):
                obj = AgentRelease()
                obj._deserialize(item)
                self._ReleaseList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentSkill(AbstractModel):
    r"""Agent 技能详情

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>skillId</p>
        :type SkillId: str
        :param _Name: <p>skill名称</p>
        :type Name: str
        :param _Description: <p>技能描述</p>
        :type Description: str
        :param _DisplayName: <p>skill展示名称</p>
        :type DisplayName: str
        :param _DisplayDescription: <p>技能展示描述</p>
        :type DisplayDescription: str
        :param _IconUrl: <p>skill图标url</p>
        :type IconUrl: str
        :param _SourceType: <p>Skill来源</p>
        :type SourceType: int
        :param _CurrentVersion: <p>Skill版本</p>
        :type CurrentVersion: str
        """
        self._SkillId = None
        self._Name = None
        self._Description = None
        self._DisplayName = None
        self._DisplayDescription = None
        self._IconUrl = None
        self._SourceType = None
        self._CurrentVersion = None

    @property
    def SkillId(self):
        r"""<p>skillId</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def Name(self):
        r"""<p>skill名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>技能描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DisplayName(self):
        r"""<p>skill展示名称</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def DisplayDescription(self):
        r"""<p>技能展示描述</p>
        :rtype: str
        """
        return self._DisplayDescription

    @DisplayDescription.setter
    def DisplayDescription(self, DisplayDescription):
        self._DisplayDescription = DisplayDescription

    @property
    def IconUrl(self):
        r"""<p>skill图标url</p>
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def SourceType(self):
        r"""<p>Skill来源</p>
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def CurrentVersion(self):
        r"""<p>Skill版本</p>
        :rtype: str
        """
        return self._CurrentVersion

    @CurrentVersion.setter
    def CurrentVersion(self, CurrentVersion):
        self._CurrentVersion = CurrentVersion


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._DisplayName = params.get("DisplayName")
        self._DisplayDescription = params.get("DisplayDescription")
        self._IconUrl = params.get("IconUrl")
        self._SourceType = params.get("SourceType")
        self._CurrentVersion = params.get("CurrentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentSkillConfig(AbstractModel):
    r"""Agent 技能入参

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>技能ID</p>
        :type SkillId: str
        """
        self._SkillId = None

    @property
    def SkillId(self):
        r"""<p>技能ID</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentSpec(AbstractModel):
    r"""Agent 可编辑配置

    """

    def __init__(self):
        r"""
        :param _Profile: <p>Agent基本配置</p>
        :type Profile: :class:`tencentcloud.adp.v20260520.models.AgentProfile`
        :param _Instructions: <p>系统提示词</p>
        :type Instructions: str
        :param _Model: <p>主模型配置</p>
        :type Model: :class:`tencentcloud.adp.v20260520.models.AgentModelConfig`
        :param _ToolList: <p>工具信息</p>
        :type ToolList: list of AgentToolConfig
        :param _PluginList: <p>插件信息</p>
        :type PluginList: list of AgentPluginConfig
        :param _SkillList: <p>技能信息</p>
        :type SkillList: list of AgentSkillConfig
        :param _AdvancedConfig: <p>高级设置</p>
        :type AdvancedConfig: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        :param _ExternalToolList: <p>调用方执行的 Function Tool 列表</p><p>入参限制：仅在 C 端用户态 Agent 场景可用，B 端配置态 Agent  忽略该字段与</p>
        :type ExternalToolList: list of AgentExternalToolConfig
        """
        self._Profile = None
        self._Instructions = None
        self._Model = None
        self._ToolList = None
        self._PluginList = None
        self._SkillList = None
        self._AdvancedConfig = None
        self._ExternalToolList = None

    @property
    def Profile(self):
        r"""<p>Agent基本配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Instructions(self):
        r"""<p>系统提示词</p>
        :rtype: str
        """
        return self._Instructions

    @Instructions.setter
    def Instructions(self, Instructions):
        self._Instructions = Instructions

    @property
    def Model(self):
        r"""<p>主模型配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentModelConfig`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def ToolList(self):
        r"""<p>工具信息</p>
        :rtype: list of AgentToolConfig
        """
        return self._ToolList

    @ToolList.setter
    def ToolList(self, ToolList):
        self._ToolList = ToolList

    @property
    def PluginList(self):
        r"""<p>插件信息</p>
        :rtype: list of AgentPluginConfig
        """
        return self._PluginList

    @PluginList.setter
    def PluginList(self, PluginList):
        self._PluginList = PluginList

    @property
    def SkillList(self):
        r"""<p>技能信息</p>
        :rtype: list of AgentSkillConfig
        """
        return self._SkillList

    @SkillList.setter
    def SkillList(self, SkillList):
        self._SkillList = SkillList

    @property
    def AdvancedConfig(self):
        r"""<p>高级设置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig

    @property
    def ExternalToolList(self):
        r"""<p>调用方执行的 Function Tool 列表</p><p>入参限制：仅在 C 端用户态 Agent 场景可用，B 端配置态 Agent  忽略该字段与</p>
        :rtype: list of AgentExternalToolConfig
        """
        return self._ExternalToolList

    @ExternalToolList.setter
    def ExternalToolList(self, ExternalToolList):
        self._ExternalToolList = ExternalToolList


    def _deserialize(self, params):
        if params.get("Profile") is not None:
            self._Profile = AgentProfile()
            self._Profile._deserialize(params.get("Profile"))
        self._Instructions = params.get("Instructions")
        if params.get("Model") is not None:
            self._Model = AgentModelConfig()
            self._Model._deserialize(params.get("Model"))
        if params.get("ToolList") is not None:
            self._ToolList = []
            for item in params.get("ToolList"):
                obj = AgentToolConfig()
                obj._deserialize(item)
                self._ToolList.append(obj)
        if params.get("PluginList") is not None:
            self._PluginList = []
            for item in params.get("PluginList"):
                obj = AgentPluginConfig()
                obj._deserialize(item)
                self._PluginList.append(obj)
        if params.get("SkillList") is not None:
            self._SkillList = []
            for item in params.get("SkillList"):
                obj = AgentSkillConfig()
                obj._deserialize(item)
                self._SkillList.append(obj)
        if params.get("AdvancedConfig") is not None:
            self._AdvancedConfig = AgentAdvancedConfig()
            self._AdvancedConfig._deserialize(params.get("AdvancedConfig"))
        if params.get("ExternalToolList") is not None:
            self._ExternalToolList = []
            for item in params.get("ExternalToolList"):
                obj = AgentExternalToolConfig()
                obj._deserialize(item)
                self._ExternalToolList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentSummary(AbstractModel):
    r"""Agent摘要信息

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>AgentId</p>
        :type AgentId: str
        :param _Profile: <p>Agent 身份画像</p>
        :type Profile: :class:`tencentcloud.adp.v20260520.models.AgentProfile`
        :param _AdvancedConfig: <p>高级设置;scope=0 时返回</p>
        :type AdvancedConfig: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        """
        self._AgentId = None
        self._Profile = None
        self._AdvancedConfig = None

    @property
    def AgentId(self):
        r"""<p>AgentId</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Profile(self):
        r"""<p>Agent 身份画像</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def AdvancedConfig(self):
        r"""<p>高级设置;scope=0 时返回</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


    def _deserialize(self, params):
        self._AgentId = params.get("AgentId")
        if params.get("Profile") is not None:
            self._Profile = AgentProfile()
            self._Profile._deserialize(params.get("Profile"))
        if params.get("AdvancedConfig") is not None:
            self._AdvancedConfig = AgentAdvancedConfig()
            self._AdvancedConfig._deserialize(params.get("AdvancedConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentSystemVariable(AbstractModel):
    r"""系统参数

    """

    def __init__(self):
        r"""
        :param _Name: <p>系统参数名</p>
        :type Name: str
        :param _DialogHistoryLimit: <p>对话历史轮数的配置；如果Input是系统变量中的“对话历史”时才使用；</p>
        :type DialogHistoryLimit: int
        """
        self._Name = None
        self._DialogHistoryLimit = None

    @property
    def Name(self):
        r"""<p>系统参数名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DialogHistoryLimit(self):
        r"""<p>对话历史轮数的配置；如果Input是系统变量中的“对话历史”时才使用；</p>
        :rtype: int
        """
        return self._DialogHistoryLimit

    @DialogHistoryLimit.setter
    def DialogHistoryLimit(self, DialogHistoryLimit):
        self._DialogHistoryLimit = DialogHistoryLimit


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._DialogHistoryLimit = params.get("DialogHistoryLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentTool(AbstractModel):
    r"""Agent 工具详情

    """

    def __init__(self):
        r"""
        :param _Config: <p>工具配置字段</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.AgentToolBasicConfig`
        :param _Name: <p>工具名称</p>
        :type Name: str
        :param _Status: <p>工具状态</p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li><li>3： 已失效</li></ul>
        :type Status: int
        :param _StreamMode: <p>调用方式</p><p>枚举值：</p><ul><li>0： 非流式</li><li>1： 流式</li></ul>
        :type StreamMode: int
        :param _ToolAccessMode: <p>工具访问模式</p><p>枚举值：</p><ul><li>0： 未指定</li><li>1： 只读</li><li>2： 写/删除</li></ul>
        :type ToolAccessMode: int
        """
        self._Config = None
        self._Name = None
        self._Status = None
        self._StreamMode = None
        self._ToolAccessMode = None

    @property
    def Config(self):
        r"""<p>工具配置字段</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentToolBasicConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Name(self):
        r"""<p>工具名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Status(self):
        r"""<p>工具状态</p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li><li>3： 已失效</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StreamMode(self):
        r"""<p>调用方式</p><p>枚举值：</p><ul><li>0： 非流式</li><li>1： 流式</li></ul>
        :rtype: int
        """
        return self._StreamMode

    @StreamMode.setter
    def StreamMode(self, StreamMode):
        self._StreamMode = StreamMode

    @property
    def ToolAccessMode(self):
        r"""<p>工具访问模式</p><p>枚举值：</p><ul><li>0： 未指定</li><li>1： 只读</li><li>2： 写/删除</li></ul>
        :rtype: int
        """
        return self._ToolAccessMode

    @ToolAccessMode.setter
    def ToolAccessMode(self, ToolAccessMode):
        self._ToolAccessMode = ToolAccessMode


    def _deserialize(self, params):
        if params.get("Config") is not None:
            self._Config = AgentToolBasicConfig()
            self._Config._deserialize(params.get("Config"))
        self._Name = params.get("Name")
        self._Status = params.get("Status")
        self._StreamMode = params.get("StreamMode")
        self._ToolAccessMode = params.get("ToolAccessMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentToolBasicConfig(AbstractModel):
    r"""Agent的工具基础配置

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _ToolId: <p>工具id</p>
        :type ToolId: str
        :param _Description: <p>描述</p>
        :type Description: str
        :param _InputList: <p>工具输入参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InputList: list of AgentToolInputParameter
        :param _OutputList: <p>工具输出参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputList: list of AgentToolOutputParameter
        :param _HeaderParameterList: <p>工具Header参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderParameterList: list of AgentPluginParameter
        :param _QueryParameterList: <p>工具Query参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryParameterList: list of AgentPluginParameter
        :param _ToolSource: <p>工具来源: 0-来自插件，1-来自工作流</p>
        :type ToolSource: int
        :param _IsDisabled: <p>是否禁用</p>
        :type IsDisabled: bool
        """
        self._PluginId = None
        self._ToolId = None
        self._Description = None
        self._InputList = None
        self._OutputList = None
        self._HeaderParameterList = None
        self._QueryParameterList = None
        self._ToolSource = None
        self._IsDisabled = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ToolId(self):
        r"""<p>工具id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def Description(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InputList(self):
        r"""<p>工具输入参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentToolInputParameter
        """
        return self._InputList

    @InputList.setter
    def InputList(self, InputList):
        self._InputList = InputList

    @property
    def OutputList(self):
        r"""<p>工具输出参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentToolOutputParameter
        """
        return self._OutputList

    @OutputList.setter
    def OutputList(self, OutputList):
        self._OutputList = OutputList

    @property
    def HeaderParameterList(self):
        r"""<p>工具Header参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentPluginParameter
        """
        return self._HeaderParameterList

    @HeaderParameterList.setter
    def HeaderParameterList(self, HeaderParameterList):
        self._HeaderParameterList = HeaderParameterList

    @property
    def QueryParameterList(self):
        r"""<p>工具Query参数列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentPluginParameter
        """
        return self._QueryParameterList

    @QueryParameterList.setter
    def QueryParameterList(self, QueryParameterList):
        self._QueryParameterList = QueryParameterList

    @property
    def ToolSource(self):
        r"""<p>工具来源: 0-来自插件，1-来自工作流</p>
        :rtype: int
        """
        return self._ToolSource

    @ToolSource.setter
    def ToolSource(self, ToolSource):
        self._ToolSource = ToolSource

    @property
    def IsDisabled(self):
        r"""<p>是否禁用</p>
        :rtype: bool
        """
        return self._IsDisabled

    @IsDisabled.setter
    def IsDisabled(self, IsDisabled):
        self._IsDisabled = IsDisabled


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._ToolId = params.get("ToolId")
        self._Description = params.get("Description")
        if params.get("InputList") is not None:
            self._InputList = []
            for item in params.get("InputList"):
                obj = AgentToolInputParameter()
                obj._deserialize(item)
                self._InputList.append(obj)
        if params.get("OutputList") is not None:
            self._OutputList = []
            for item in params.get("OutputList"):
                obj = AgentToolOutputParameter()
                obj._deserialize(item)
                self._OutputList.append(obj)
        if params.get("HeaderParameterList") is not None:
            self._HeaderParameterList = []
            for item in params.get("HeaderParameterList"):
                obj = AgentPluginParameter()
                obj._deserialize(item)
                self._HeaderParameterList.append(obj)
        if params.get("QueryParameterList") is not None:
            self._QueryParameterList = []
            for item in params.get("QueryParameterList"):
                obj = AgentPluginParameter()
                obj._deserialize(item)
                self._QueryParameterList.append(obj)
        self._ToolSource = params.get("ToolSource")
        self._IsDisabled = params.get("IsDisabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentToolConfig(AbstractModel):
    r"""Agent 工具入参

    """

    def __init__(self):
        r"""
        :param _Config: <p>工具配置</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.AgentToolBasicConfig`
        """
        self._Config = None

    @property
    def Config(self):
        r"""<p>工具配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentToolBasicConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        if params.get("Config") is not None:
            self._Config = AgentToolBasicConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentToolInputParameter(AbstractModel):
    r"""Agent 工具输入参数定义

    """

    def __init__(self):
        r"""
        :param _Name: <p>工具名称</p>
        :type Name: str
        :param _Description: <p>工具描述</p>
        :type Description: str
        :param _Type: <p>工具参数类型</p><p>枚举值：</p><ul><li>0： STRING</li><li>1： INT</li><li>2： FLOAT</li><li>3： BOOL</li><li>4： OBJECT</li><li>5： ARRAY_STRING</li><li>6： ARRAY_INT</li><li>7： ARRAY_FLOAT</li><li>8： ARRAY_BOOL</li><li>9： ARRAY_OBJECT</li><li>20： ARRAY_ARRAY</li><li>99： NULL</li></ul>
        :type Type: int
        :param _IsRequired: <p>是否必填</p>
        :type IsRequired: bool
        :param _SubParameterList: <p>子参数，仅 OBJECT 或 ARRAY&lt;&gt; 类型时使用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SubParameterList: list of AgentToolInputParameter
        :param _IsHidden: <p>模式下是否对模型隐藏</p>
        :type IsHidden: bool
        :param _OneOfList: <p>OneOf类型的参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OneOfList: list of AgentToolInputParameter
        :param _AnyOfList: <p>AnyOf类型的参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AnyOfList: list of AgentToolInputParameter
        :param _Input: <p>参数取值来源</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Input: :class:`tencentcloud.adp.v20260520.models.AgentInput`
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._IsRequired = None
        self._SubParameterList = None
        self._IsHidden = None
        self._OneOfList = None
        self._AnyOfList = None
        self._Input = None

    @property
    def Name(self):
        r"""<p>工具名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>工具描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        r"""<p>工具参数类型</p><p>枚举值：</p><ul><li>0： STRING</li><li>1： INT</li><li>2： FLOAT</li><li>3： BOOL</li><li>4： OBJECT</li><li>5： ARRAY_STRING</li><li>6： ARRAY_INT</li><li>7： ARRAY_FLOAT</li><li>8： ARRAY_BOOL</li><li>9： ARRAY_OBJECT</li><li>20： ARRAY_ARRAY</li><li>99： NULL</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def IsRequired(self):
        r"""<p>是否必填</p>
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def SubParameterList(self):
        r"""<p>子参数，仅 OBJECT 或 ARRAY&lt;&gt; 类型时使用</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentToolInputParameter
        """
        return self._SubParameterList

    @SubParameterList.setter
    def SubParameterList(self, SubParameterList):
        self._SubParameterList = SubParameterList

    @property
    def IsHidden(self):
        r"""<p>模式下是否对模型隐藏</p>
        :rtype: bool
        """
        return self._IsHidden

    @IsHidden.setter
    def IsHidden(self, IsHidden):
        self._IsHidden = IsHidden

    @property
    def OneOfList(self):
        r"""<p>OneOf类型的参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentToolInputParameter
        """
        return self._OneOfList

    @OneOfList.setter
    def OneOfList(self, OneOfList):
        self._OneOfList = OneOfList

    @property
    def AnyOfList(self):
        r"""<p>AnyOf类型的参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AgentToolInputParameter
        """
        return self._AnyOfList

    @AnyOfList.setter
    def AnyOfList(self, AnyOfList):
        self._AnyOfList = AnyOfList

    @property
    def Input(self):
        r"""<p>参数取值来源</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentInput`
        """
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        self._IsRequired = params.get("IsRequired")
        if params.get("SubParameterList") is not None:
            self._SubParameterList = []
            for item in params.get("SubParameterList"):
                obj = AgentToolInputParameter()
                obj._deserialize(item)
                self._SubParameterList.append(obj)
        self._IsHidden = params.get("IsHidden")
        if params.get("OneOfList") is not None:
            self._OneOfList = []
            for item in params.get("OneOfList"):
                obj = AgentToolInputParameter()
                obj._deserialize(item)
                self._OneOfList.append(obj)
        if params.get("AnyOfList") is not None:
            self._AnyOfList = []
            for item in params.get("AnyOfList"):
                obj = AgentToolInputParameter()
                obj._deserialize(item)
                self._AnyOfList.append(obj)
        if params.get("Input") is not None:
            self._Input = AgentInput()
            self._Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentToolOutputParameter(AbstractModel):
    r"""Agent 工具输出参数

    """

    def __init__(self):
        r"""
        :param _Name: <p>参数名称</p>
        :type Name: str
        :param _Description: <p>变量描述</p>
        :type Description: str
        :param _Type: <p>参数类型</p><p>枚举值：</p><ul><li>0： STRING</li><li>1： INT</li><li>2： FLOAT</li><li>3： BOOL</li><li>4： OBJECT</li><li>5： ARRAY_STRING</li><li>6： ARRAY_INT</li><li>7： ARRAY_FLOAT</li><li>8： ARRAY_BOOL</li><li>9： ARRAY_OBJECT</li><li>20： ARRAY_ARRAY</li><li>99： NULL</li></ul>
        :type Type: int
        :param _SubParameterList: <p>子参数，仅 OBJECT 或 ARRAY_OBJECT 类型时使用</p>
        :type SubParameterList: list of AgentToolOutputParameter
        :param _RenderMode: <p>解析方式</p>
        :type RenderMode: int
        """
        self._Name = None
        self._Description = None
        self._Type = None
        self._SubParameterList = None
        self._RenderMode = None

    @property
    def Name(self):
        r"""<p>参数名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>变量描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Type(self):
        r"""<p>参数类型</p><p>枚举值：</p><ul><li>0： STRING</li><li>1： INT</li><li>2： FLOAT</li><li>3： BOOL</li><li>4： OBJECT</li><li>5： ARRAY_STRING</li><li>6： ARRAY_INT</li><li>7： ARRAY_FLOAT</li><li>8： ARRAY_BOOL</li><li>9： ARRAY_OBJECT</li><li>20： ARRAY_ARRAY</li><li>99： NULL</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SubParameterList(self):
        r"""<p>子参数，仅 OBJECT 或 ARRAY_OBJECT 类型时使用</p>
        :rtype: list of AgentToolOutputParameter
        """
        return self._SubParameterList

    @SubParameterList.setter
    def SubParameterList(self, SubParameterList):
        self._SubParameterList = SubParameterList

    @property
    def RenderMode(self):
        r"""<p>解析方式</p>
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Type = params.get("Type")
        if params.get("SubParameterList") is not None:
            self._SubParameterList = []
            for item in params.get("SubParameterList"):
                obj = AgentToolOutputParameter()
                obj._deserialize(item)
                self._SubParameterList.append(obj)
        self._RenderMode = params.get("RenderMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentUserInputValue(AbstractModel):
    r"""用户输入值

    """

    def __init__(self):
        r"""
        :param _ValueList: <p>用户输入参数值</p>
        :type ValueList: list of str
        """
        self._ValueList = None

    @property
    def ValueList(self):
        r"""<p>用户输入参数值</p>
        :rtype: list of str
        """
        return self._ValueList

    @ValueList.setter
    def ValueList(self, ValueList):
        self._ValueList = ValueList


    def _deserialize(self, params):
        self._ValueList = params.get("ValueList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKeyAuthConfig(AbstractModel):
    r"""ApiKey鉴权配置

    """

    def __init__(self):
        r"""
        :param _KeyLocation: 密钥位置 HEADER/QUERY

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | Header鉴权 |
| 1 | Query鉴权 |
        :type KeyLocation: int
        :param _KeyParamName: 密钥参数名
        :type KeyParamName: str
        :param _KeyParamValue: 密钥参数值
        :type KeyParamValue: str
        """
        self._KeyLocation = None
        self._KeyParamName = None
        self._KeyParamValue = None

    @property
    def KeyLocation(self):
        r"""密钥位置 HEADER/QUERY

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | Header鉴权 |
| 1 | Query鉴权 |
        :rtype: int
        """
        return self._KeyLocation

    @KeyLocation.setter
    def KeyLocation(self, KeyLocation):
        self._KeyLocation = KeyLocation

    @property
    def KeyParamName(self):
        r"""密钥参数名
        :rtype: str
        """
        return self._KeyParamName

    @KeyParamName.setter
    def KeyParamName(self, KeyParamName):
        self._KeyParamName = KeyParamName

    @property
    def KeyParamValue(self):
        r"""密钥参数值
        :rtype: str
        """
        return self._KeyParamValue

    @KeyParamValue.setter
    def KeyParamValue(self, KeyParamValue):
        self._KeyParamValue = KeyParamValue


    def _deserialize(self, params):
        self._KeyLocation = params.get("KeyLocation")
        self._KeyParamName = params.get("KeyParamName")
        self._KeyParamValue = params.get("KeyParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiPluginConfig(AbstractModel):
    r"""API插件配置

    """

    def __init__(self):
        r"""
        :param _AuthConfig: 授权配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthConfig: :class:`tencentcloud.adp.v20260520.models.AuthConfig`
        """
        self._AuthConfig = None

    @property
    def AuthConfig(self):
        r"""授权配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AuthConfig`
        """
        return self._AuthConfig

    @AuthConfig.setter
    def AuthConfig(self, AuthConfig):
        self._AuthConfig = AuthConfig


    def _deserialize(self, params):
        if params.get("AuthConfig") is not None:
            self._AuthConfig = AuthConfig()
            self._AuthConfig._deserialize(params.get("AuthConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiToolConfig(AbstractModel):
    r"""ApiToolConfig

    """

    def __init__(self):
        r"""
        :param _Body: <p>请求体参数</p>
        :type Body: list of RequestParam
        :param _Example: <p>示例</p>
        :type Example: :class:`tencentcloud.adp.v20260520.models.ToolExample`
        :param _ExternalApiUrl: <p>API插件外部调用地址</p>
        :type ExternalApiUrl: str
        :param _Header: <p>Header</p>
        :type Header: list of RequestParam
        :param _Method: <p>请求方式</p>
        :type Method: str
        :param _Outputs: <p>输出</p>
        :type Outputs: list of ResponseParam
        :param _Query: <p>查询参数</p>
        :type Query: list of RequestParam
        :param _StreamMode: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>STREAM_MODE_UNARY</td><td>0</td><td>非流式</td></tr><tr><td>STREAM_MODE_STREAMING</td><td>1</td><td>流式</td></tr></tbody></table>
        :type StreamMode: int
        :param _Url: <p>地址</p>
        :type Url: str
        """
        self._Body = None
        self._Example = None
        self._ExternalApiUrl = None
        self._Header = None
        self._Method = None
        self._Outputs = None
        self._Query = None
        self._StreamMode = None
        self._Url = None

    @property
    def Body(self):
        r"""<p>请求体参数</p>
        :rtype: list of RequestParam
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Example(self):
        r"""<p>示例</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ToolExample`
        """
        return self._Example

    @Example.setter
    def Example(self, Example):
        self._Example = Example

    @property
    def ExternalApiUrl(self):
        r"""<p>API插件外部调用地址</p>
        :rtype: str
        """
        return self._ExternalApiUrl

    @ExternalApiUrl.setter
    def ExternalApiUrl(self, ExternalApiUrl):
        self._ExternalApiUrl = ExternalApiUrl

    @property
    def Header(self):
        r"""<p>Header</p>
        :rtype: list of RequestParam
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Method(self):
        r"""<p>请求方式</p>
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Outputs(self):
        r"""<p>输出</p>
        :rtype: list of ResponseParam
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def Query(self):
        r"""<p>查询参数</p>
        :rtype: list of RequestParam
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def StreamMode(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>STREAM_MODE_UNARY</td><td>0</td><td>非流式</td></tr><tr><td>STREAM_MODE_STREAMING</td><td>1</td><td>流式</td></tr></tbody></table>
        :rtype: int
        """
        return self._StreamMode

    @StreamMode.setter
    def StreamMode(self, StreamMode):
        self._StreamMode = StreamMode

    @property
    def Url(self):
        r"""<p>地址</p>
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        if params.get("Body") is not None:
            self._Body = []
            for item in params.get("Body"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Body.append(obj)
        if params.get("Example") is not None:
            self._Example = ToolExample()
            self._Example._deserialize(params.get("Example"))
        self._ExternalApiUrl = params.get("ExternalApiUrl")
        if params.get("Header") is not None:
            self._Header = []
            for item in params.get("Header"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Header.append(obj)
        self._Method = params.get("Method")
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = ResponseParam()
                obj._deserialize(item)
                self._Outputs.append(obj)
        if params.get("Query") is not None:
            self._Query = []
            for item in params.get("Query"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Query.append(obj)
        self._StreamMode = params.get("StreamMode")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class App(AbstractModel):
    r"""App 应用完整信息

    """

    def __init__(self):
        r"""
        :param _AuxiliaryInfo: <p>辅助信息(子状态/审批/申诉/搜索资源/特殊状态等)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryInfo: :class:`tencentcloud.adp.v20260520.models.AppAuxiliaryInfo`
        :param _Config: <p>配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        :param _Metadata: <p>元数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.adp.v20260520.models.AppMetadata`
        :param _SecretInfo: <p>应用密钥信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretInfo: :class:`tencentcloud.adp.v20260520.models.AppSecretInfo`
        :param _ShareUrlInfo: <p>分享链接信息(含访问控制)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareUrlInfo: :class:`tencentcloud.adp.v20260520.models.AppShareURLInfo`
        :param _Status: <p>状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.adp.v20260520.models.AppStatusInfo`
        :param _SharedKbList: <p>应用引用的共享知识库列表</p>
        :type SharedKbList: list of AppSharedKbInfo
        :param _CorpShareConfig: <p>企业共享配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpShareConfig: :class:`tencentcloud.adp.v20260520.models.CorpShareConfig`
        """
        self._AuxiliaryInfo = None
        self._Config = None
        self._Metadata = None
        self._SecretInfo = None
        self._ShareUrlInfo = None
        self._Status = None
        self._SharedKbList = None
        self._CorpShareConfig = None

    @property
    def AuxiliaryInfo(self):
        r"""<p>辅助信息(子状态/审批/申诉/搜索资源/特殊状态等)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppAuxiliaryInfo`
        """
        return self._AuxiliaryInfo

    @AuxiliaryInfo.setter
    def AuxiliaryInfo(self, AuxiliaryInfo):
        self._AuxiliaryInfo = AuxiliaryInfo

    @property
    def Config(self):
        r"""<p>配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Metadata(self):
        r"""<p>元数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def SecretInfo(self):
        r"""<p>应用密钥信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppSecretInfo`
        """
        return self._SecretInfo

    @SecretInfo.setter
    def SecretInfo(self, SecretInfo):
        self._SecretInfo = SecretInfo

    @property
    def ShareUrlInfo(self):
        r"""<p>分享链接信息(含访问控制)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppShareURLInfo`
        """
        return self._ShareUrlInfo

    @ShareUrlInfo.setter
    def ShareUrlInfo(self, ShareUrlInfo):
        self._ShareUrlInfo = ShareUrlInfo

    @property
    def Status(self):
        r"""<p>状态</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppStatusInfo`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SharedKbList(self):
        r"""<p>应用引用的共享知识库列表</p>
        :rtype: list of AppSharedKbInfo
        """
        return self._SharedKbList

    @SharedKbList.setter
    def SharedKbList(self, SharedKbList):
        self._SharedKbList = SharedKbList

    @property
    def CorpShareConfig(self):
        r"""<p>企业共享配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.CorpShareConfig`
        """
        return self._CorpShareConfig

    @CorpShareConfig.setter
    def CorpShareConfig(self, CorpShareConfig):
        self._CorpShareConfig = CorpShareConfig


    def _deserialize(self, params):
        if params.get("AuxiliaryInfo") is not None:
            self._AuxiliaryInfo = AppAuxiliaryInfo()
            self._AuxiliaryInfo._deserialize(params.get("AuxiliaryInfo"))
        if params.get("Config") is not None:
            self._Config = AppConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("Metadata") is not None:
            self._Metadata = AppMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        if params.get("SecretInfo") is not None:
            self._SecretInfo = AppSecretInfo()
            self._SecretInfo._deserialize(params.get("SecretInfo"))
        if params.get("ShareUrlInfo") is not None:
            self._ShareUrlInfo = AppShareURLInfo()
            self._ShareUrlInfo._deserialize(params.get("ShareUrlInfo"))
        if params.get("Status") is not None:
            self._Status = AppStatusInfo()
            self._Status._deserialize(params.get("Status"))
        if params.get("SharedKbList") is not None:
            self._SharedKbList = []
            for item in params.get("SharedKbList"):
                obj = AppSharedKbInfo()
                obj._deserialize(item)
                self._SharedKbList.append(obj)
        if params.get("CorpShareConfig") is not None:
            self._CorpShareConfig = CorpShareConfig()
            self._CorpShareConfig._deserialize(params.get("CorpShareConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAdvancedConf(AbstractModel):
    r"""应用高级配置

    """

    def __init__(self):
        r"""
        :param _EnableContextRewrite: <p>是否开启上下文改写</p>
        :type EnableContextRewrite: bool
        :param _EnableImageTextRetrieval: <p>是否开启图文检索</p>
        :type EnableImageTextRetrieval: bool
        :param _ReplyFlexibility: <p>回复灵活度</p>
        :type ReplyFlexibility: int
        :param _DialogCustomConfig: <p>对话端自定义配置(所有模式共用,允许对话中动态修改配置)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogCustomConfig: :class:`tencentcloud.adp.v20260520.models.DialogCustomConfig`
        :param _IntentAchievement: <p>意图达成优先级</p>
        :type IntentAchievement: list of IntentAchievementInfo
        """
        self._EnableContextRewrite = None
        self._EnableImageTextRetrieval = None
        self._ReplyFlexibility = None
        self._DialogCustomConfig = None
        self._IntentAchievement = None

    @property
    def EnableContextRewrite(self):
        r"""<p>是否开启上下文改写</p>
        :rtype: bool
        """
        return self._EnableContextRewrite

    @EnableContextRewrite.setter
    def EnableContextRewrite(self, EnableContextRewrite):
        self._EnableContextRewrite = EnableContextRewrite

    @property
    def EnableImageTextRetrieval(self):
        r"""<p>是否开启图文检索</p>
        :rtype: bool
        """
        return self._EnableImageTextRetrieval

    @EnableImageTextRetrieval.setter
    def EnableImageTextRetrieval(self, EnableImageTextRetrieval):
        self._EnableImageTextRetrieval = EnableImageTextRetrieval

    @property
    def ReplyFlexibility(self):
        r"""<p>回复灵活度</p>
        :rtype: int
        """
        return self._ReplyFlexibility

    @ReplyFlexibility.setter
    def ReplyFlexibility(self, ReplyFlexibility):
        self._ReplyFlexibility = ReplyFlexibility

    @property
    def DialogCustomConfig(self):
        r"""<p>对话端自定义配置(所有模式共用,允许对话中动态修改配置)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.DialogCustomConfig`
        """
        return self._DialogCustomConfig

    @DialogCustomConfig.setter
    def DialogCustomConfig(self, DialogCustomConfig):
        self._DialogCustomConfig = DialogCustomConfig

    @property
    def IntentAchievement(self):
        r"""<p>意图达成优先级</p>
        :rtype: list of IntentAchievementInfo
        """
        return self._IntentAchievement

    @IntentAchievement.setter
    def IntentAchievement(self, IntentAchievement):
        self._IntentAchievement = IntentAchievement


    def _deserialize(self, params):
        self._EnableContextRewrite = params.get("EnableContextRewrite")
        self._EnableImageTextRetrieval = params.get("EnableImageTextRetrieval")
        self._ReplyFlexibility = params.get("ReplyFlexibility")
        if params.get("DialogCustomConfig") is not None:
            self._DialogCustomConfig = DialogCustomConfig()
            self._DialogCustomConfig._deserialize(params.get("DialogCustomConfig"))
        if params.get("IntentAchievement") is not None:
            self._IntentAchievement = []
            for item in params.get("IntentAchievement"):
                obj = IntentAchievementInfo()
                obj._deserialize(item)
                self._IntentAchievement.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAppeal(AbstractModel):
    r"""应用申诉信息(用户不可修改)

    """

    def __init__(self):
        r"""
        :param _AppealingStatus: 申诉中的配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type AppealingStatus: :class:`tencentcloud.adp.v20260520.models.AppealingStatus`
        """
        self._AppealingStatus = None

    @property
    def AppealingStatus(self):
        r"""申诉中的配置项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppealingStatus`
        """
        return self._AppealingStatus

    @AppealingStatus.setter
    def AppealingStatus(self, AppealingStatus):
        self._AppealingStatus = AppealingStatus


    def _deserialize(self, params):
        if params.get("AppealingStatus") is not None:
            self._AppealingStatus = AppealingStatus()
            self._AppealingStatus._deserialize(params.get("AppealingStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppAuxiliaryInfo(AbstractModel):
    r"""应用辅助信息 - 包含各类辅助状态和扩展信息(用户不可修改)

    """

    def __init__(self):
        r"""
        :param _Appeal: 申诉信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Appeal: :class:`tencentcloud.adp.v20260520.models.AppAppeal`
        :param _SearchResourceStatus: 搜索资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchResourceStatus: :class:`tencentcloud.adp.v20260520.models.SearchResourceStatusInfo`
        :param _SpecialStatusInfo: 特殊状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialStatusInfo: :class:`tencentcloud.adp.v20260520.models.SpecialStatusInfo`
        :param _SubStatus: 子状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatus: :class:`tencentcloud.adp.v20260520.models.AppSubStatusInfo`
        """
        self._Appeal = None
        self._SearchResourceStatus = None
        self._SpecialStatusInfo = None
        self._SubStatus = None

    @property
    def Appeal(self):
        r"""申诉信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppAppeal`
        """
        return self._Appeal

    @Appeal.setter
    def Appeal(self, Appeal):
        self._Appeal = Appeal

    @property
    def SearchResourceStatus(self):
        r"""搜索资源状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SearchResourceStatusInfo`
        """
        return self._SearchResourceStatus

    @SearchResourceStatus.setter
    def SearchResourceStatus(self, SearchResourceStatus):
        self._SearchResourceStatus = SearchResourceStatus

    @property
    def SpecialStatusInfo(self):
        r"""特殊状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SpecialStatusInfo`
        """
        return self._SpecialStatusInfo

    @SpecialStatusInfo.setter
    def SpecialStatusInfo(self, SpecialStatusInfo):
        self._SpecialStatusInfo = SpecialStatusInfo

    @property
    def SubStatus(self):
        r"""子状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppSubStatusInfo`
        """
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus


    def _deserialize(self, params):
        if params.get("Appeal") is not None:
            self._Appeal = AppAppeal()
            self._Appeal._deserialize(params.get("Appeal"))
        if params.get("SearchResourceStatus") is not None:
            self._SearchResourceStatus = SearchResourceStatusInfo()
            self._SearchResourceStatus._deserialize(params.get("SearchResourceStatus"))
        if params.get("SpecialStatusInfo") is not None:
            self._SpecialStatusInfo = SpecialStatusInfo()
            self._SpecialStatusInfo._deserialize(params.get("SpecialStatusInfo"))
        if params.get("SubStatus") is not None:
            self._SubStatus = AppSubStatusInfo()
            self._SubStatus._deserialize(params.get("SubStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppConfig(AbstractModel):
    r"""应用配置 - 用户可修改的所有配置

    """

    def __init__(self):
        r"""
        :param _Experience: 体验配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Experience: :class:`tencentcloud.adp.v20260520.models.AppExperienceConfig`
        :param _Greeting: 欢迎语配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Greeting: :class:`tencentcloud.adp.v20260520.models.AppGreetingConfig`
        :param _Memory: 记忆配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: :class:`tencentcloud.adp.v20260520.models.AppMemoryConfig`
        :param _Mode: 模式相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: :class:`tencentcloud.adp.v20260520.models.AppModeConfig`
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.AppModelConfig`
        :param _WebSearch: 联网搜索配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSearch: :class:`tencentcloud.adp.v20260520.models.AppWebSearchConfig`
        :param _Workflow: 工作流配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Workflow: :class:`tencentcloud.adp.v20260520.models.AppWorkflowConfig`
        """
        self._Experience = None
        self._Greeting = None
        self._Memory = None
        self._Mode = None
        self._Model = None
        self._WebSearch = None
        self._Workflow = None

    @property
    def Experience(self):
        r"""体验配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppExperienceConfig`
        """
        return self._Experience

    @Experience.setter
    def Experience(self, Experience):
        self._Experience = Experience

    @property
    def Greeting(self):
        r"""欢迎语配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppGreetingConfig`
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting

    @property
    def Memory(self):
        r"""记忆配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppMemoryConfig`
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Mode(self):
        r"""模式相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppModeConfig`
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppModelConfig`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def WebSearch(self):
        r"""联网搜索配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppWebSearchConfig`
        """
        return self._WebSearch

    @WebSearch.setter
    def WebSearch(self, WebSearch):
        self._WebSearch = WebSearch

    @property
    def Workflow(self):
        r"""工作流配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppWorkflowConfig`
        """
        return self._Workflow

    @Workflow.setter
    def Workflow(self, Workflow):
        self._Workflow = Workflow


    def _deserialize(self, params):
        if params.get("Experience") is not None:
            self._Experience = AppExperienceConfig()
            self._Experience._deserialize(params.get("Experience"))
        if params.get("Greeting") is not None:
            self._Greeting = AppGreetingConfig()
            self._Greeting._deserialize(params.get("Greeting"))
        if params.get("Memory") is not None:
            self._Memory = AppMemoryConfig()
            self._Memory._deserialize(params.get("Memory"))
        if params.get("Mode") is not None:
            self._Mode = AppModeConfig()
            self._Mode._deserialize(params.get("Mode"))
        if params.get("Model") is not None:
            self._Model = AppModelConfig()
            self._Model._deserialize(params.get("Model"))
        if params.get("WebSearch") is not None:
            self._WebSearch = AppWebSearchConfig()
            self._WebSearch._deserialize(params.get("WebSearch"))
        if params.get("Workflow") is not None:
            self._Workflow = AppWorkflowConfig()
            self._Workflow._deserialize(params.get("Workflow"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppExperienceConfig(AbstractModel):
    r"""体验配置

    """

    def __init__(self):
        r"""
        :param _Advanced: 高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Advanced: :class:`tencentcloud.adp.v20260520.models.AppAdvancedConf`
        :param _Conversation: 对话体验配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Conversation: :class:`tencentcloud.adp.v20260520.models.ConversationExperience`
        :param _Role: 角色配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: :class:`tencentcloud.adp.v20260520.models.RoleConfig`
        """
        self._Advanced = None
        self._Conversation = None
        self._Role = None

    @property
    def Advanced(self):
        r"""高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppAdvancedConf`
        """
        return self._Advanced

    @Advanced.setter
    def Advanced(self, Advanced):
        self._Advanced = Advanced

    @property
    def Conversation(self):
        r"""对话体验配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationExperience`
        """
        return self._Conversation

    @Conversation.setter
    def Conversation(self, Conversation):
        self._Conversation = Conversation

    @property
    def Role(self):
        r"""角色配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.RoleConfig`
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role


    def _deserialize(self, params):
        if params.get("Advanced") is not None:
            self._Advanced = AppAdvancedConf()
            self._Advanced._deserialize(params.get("Advanced"))
        if params.get("Conversation") is not None:
            self._Conversation = ConversationExperience()
            self._Conversation._deserialize(params.get("Conversation"))
        if params.get("Role") is not None:
            self._Role = RoleConfig()
            self._Role._deserialize(params.get("Role"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppGreetingConfig(AbstractModel):
    r"""欢迎语配置

    """

    def __init__(self):
        r"""
        :param _Greeting: <p>欢迎语内容</p>
        :type Greeting: str
        :param _OpeningQuestionList: <p>开场问题列表</p>
        :type OpeningQuestionList: list of str
        """
        self._Greeting = None
        self._OpeningQuestionList = None

    @property
    def Greeting(self):
        r"""<p>欢迎语内容</p>
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting

    @property
    def OpeningQuestionList(self):
        r"""<p>开场问题列表</p>
        :rtype: list of str
        """
        return self._OpeningQuestionList

    @OpeningQuestionList.setter
    def OpeningQuestionList(self, OpeningQuestionList):
        self._OpeningQuestionList = OpeningQuestionList


    def _deserialize(self, params):
        self._Greeting = params.get("Greeting")
        self._OpeningQuestionList = params.get("OpeningQuestionList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppMemoryConfig(AbstractModel):
    r"""记忆配置

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启长记忆
        :type Enabled: bool
        :param _LongMemoryDay: 长记忆时长
        :type LongMemoryDay: int
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        :param _PromptContent: prompt内容
        :type PromptContent: str
        :param _PromptMode: 提示词模式。枚举值: 1:自定义
        :type PromptMode: int
        """
        self._Enabled = None
        self._LongMemoryDay = None
        self._Model = None
        self._PromptContent = None
        self._PromptMode = None

    @property
    def Enabled(self):
        r"""是否开启长记忆
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def LongMemoryDay(self):
        r"""长记忆时长
        :rtype: int
        """
        return self._LongMemoryDay

    @LongMemoryDay.setter
    def LongMemoryDay(self, LongMemoryDay):
        self._LongMemoryDay = LongMemoryDay

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def PromptContent(self):
        r"""prompt内容
        :rtype: str
        """
        return self._PromptContent

    @PromptContent.setter
    def PromptContent(self, PromptContent):
        self._PromptContent = PromptContent

    @property
    def PromptMode(self):
        r"""提示词模式。枚举值: 1:自定义
        :rtype: int
        """
        return self._PromptMode

    @PromptMode.setter
    def PromptMode(self, PromptMode):
        self._PromptMode = PromptMode


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._LongMemoryDay = params.get("LongMemoryDay")
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        self._PromptContent = params.get("PromptContent")
        self._PromptMode = params.get("PromptMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppMetadata(AbstractModel):
    r"""应用元数据 - 基础标识和描述信息

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _AppMode: 应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :type AppMode: int
        :param _Avatar: 应用头像
        :type Avatar: str
        :param _CreateTime: 创建时间 (Unix时间戳,秒级)
        :type CreateTime: str
        :param _Description: 应用描述
        :type Description: str
        :param _Name: 应用名称
        :type Name: str
        :param _SpaceId: 空间ID
        :type SpaceId: str
        :param _UpdateTime: 更新时间 (Unix时间戳,秒级)
        :type UpdateTime: str
        """
        self._AppId = None
        self._AppMode = None
        self._Avatar = None
        self._CreateTime = None
        self._Description = None
        self._Name = None
        self._SpaceId = None
        self._UpdateTime = None

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppMode(self):
        r"""应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :rtype: int
        """
        return self._AppMode

    @AppMode.setter
    def AppMode(self, AppMode):
        self._AppMode = AppMode

    @property
    def Avatar(self):
        r"""应用头像
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def CreateTime(self):
        r"""创建时间 (Unix时间戳,秒级)
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

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
    def Name(self):
        r"""应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SpaceId(self):
        r"""空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UpdateTime(self):
        r"""更新时间 (Unix时间戳,秒级)
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppMode = params.get("AppMode")
        self._Avatar = params.get("Avatar")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._SpaceId = params.get("SpaceId")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppModeConfig(AbstractModel):
    r"""模式配置 - 包含不同模式的独有配置

    """

    def __init__(self):
        r"""
        :param _MultiAgentConfig: 多智能体配置(Agent模式)
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiAgentConfig: :class:`tencentcloud.adp.v20260520.models.MultiAgentConfig`
        :param _SingleWorkflowConfig: 单工作流配置(单工作流模式)
注意：此字段可能返回 null，表示取不到有效值。
        :type SingleWorkflowConfig: :class:`tencentcloud.adp.v20260520.models.SingleWorkflowConfig`
        :param _ClawAgentConfig: ClawAgent配置(ClawAgent模式)
注意：此字段可能返回 null，表示取不到有效值。
        :type ClawAgentConfig: :class:`tencentcloud.adp.v20260520.models.ClawAgentConfig`
        """
        self._MultiAgentConfig = None
        self._SingleWorkflowConfig = None
        self._ClawAgentConfig = None

    @property
    def MultiAgentConfig(self):
        r"""多智能体配置(Agent模式)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.MultiAgentConfig`
        """
        return self._MultiAgentConfig

    @MultiAgentConfig.setter
    def MultiAgentConfig(self, MultiAgentConfig):
        self._MultiAgentConfig = MultiAgentConfig

    @property
    def SingleWorkflowConfig(self):
        r"""单工作流配置(单工作流模式)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SingleWorkflowConfig`
        """
        return self._SingleWorkflowConfig

    @SingleWorkflowConfig.setter
    def SingleWorkflowConfig(self, SingleWorkflowConfig):
        self._SingleWorkflowConfig = SingleWorkflowConfig

    @property
    def ClawAgentConfig(self):
        r"""ClawAgent配置(ClawAgent模式)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ClawAgentConfig`
        """
        return self._ClawAgentConfig

    @ClawAgentConfig.setter
    def ClawAgentConfig(self, ClawAgentConfig):
        self._ClawAgentConfig = ClawAgentConfig


    def _deserialize(self, params):
        if params.get("MultiAgentConfig") is not None:
            self._MultiAgentConfig = MultiAgentConfig()
            self._MultiAgentConfig._deserialize(params.get("MultiAgentConfig"))
        if params.get("SingleWorkflowConfig") is not None:
            self._SingleWorkflowConfig = SingleWorkflowConfig()
            self._SingleWorkflowConfig._deserialize(params.get("SingleWorkflowConfig"))
        if params.get("ClawAgentConfig") is not None:
            self._ClawAgentConfig = ClawAgentConfig()
            self._ClawAgentConfig._deserialize(params.get("ClawAgentConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppModelConfig(AbstractModel):
    r"""模型配置

    """

    def __init__(self):
        r"""
        :param _AiOptimizeModel: AI一键优化模型
注意：此字段可能返回 null，表示取不到有效值。
        :type AiOptimizeModel: :class:`tencentcloud.adp.v20260520.models.AIOptimizeModel`
        :param _FileParseModel: 实时文件解析模型
注意：此字段可能返回 null，表示取不到有效值。
        :type FileParseModel: :class:`tencentcloud.adp.v20260520.models.FileParseModel`
        :param _GenerateModel: 生成模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type GenerateModel: :class:`tencentcloud.adp.v20260520.models.GenerateModel`
        :param _MultiModalQaModel: 多模态问答模型
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiModalQaModel: :class:`tencentcloud.adp.v20260520.models.MultiModalQAModel`
        :param _MultiModalUnderstandingModel: 多模态理解模型
注意：此字段可能返回 null，表示取不到有效值。
        :type MultiModalUnderstandingModel: :class:`tencentcloud.adp.v20260520.models.MultiModalUnderstandingModel`
        :param _PromptRewriteModel: Prompt改写模型
注意：此字段可能返回 null，表示取不到有效值。
        :type PromptRewriteModel: :class:`tencentcloud.adp.v20260520.models.PromptRewriteModel`
        :param _ThinkModel: 思考模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ThinkModel: :class:`tencentcloud.adp.v20260520.models.ThinkModel`
        """
        self._AiOptimizeModel = None
        self._FileParseModel = None
        self._GenerateModel = None
        self._MultiModalQaModel = None
        self._MultiModalUnderstandingModel = None
        self._PromptRewriteModel = None
        self._ThinkModel = None

    @property
    def AiOptimizeModel(self):
        r"""AI一键优化模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AIOptimizeModel`
        """
        return self._AiOptimizeModel

    @AiOptimizeModel.setter
    def AiOptimizeModel(self, AiOptimizeModel):
        self._AiOptimizeModel = AiOptimizeModel

    @property
    def FileParseModel(self):
        r"""实时文件解析模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.FileParseModel`
        """
        return self._FileParseModel

    @FileParseModel.setter
    def FileParseModel(self, FileParseModel):
        self._FileParseModel = FileParseModel

    @property
    def GenerateModel(self):
        r"""生成模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.GenerateModel`
        """
        return self._GenerateModel

    @GenerateModel.setter
    def GenerateModel(self, GenerateModel):
        self._GenerateModel = GenerateModel

    @property
    def MultiModalQaModel(self):
        r"""多模态问答模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.MultiModalQAModel`
        """
        return self._MultiModalQaModel

    @MultiModalQaModel.setter
    def MultiModalQaModel(self, MultiModalQaModel):
        self._MultiModalQaModel = MultiModalQaModel

    @property
    def MultiModalUnderstandingModel(self):
        r"""多模态理解模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.MultiModalUnderstandingModel`
        """
        return self._MultiModalUnderstandingModel

    @MultiModalUnderstandingModel.setter
    def MultiModalUnderstandingModel(self, MultiModalUnderstandingModel):
        self._MultiModalUnderstandingModel = MultiModalUnderstandingModel

    @property
    def PromptRewriteModel(self):
        r"""Prompt改写模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.PromptRewriteModel`
        """
        return self._PromptRewriteModel

    @PromptRewriteModel.setter
    def PromptRewriteModel(self, PromptRewriteModel):
        self._PromptRewriteModel = PromptRewriteModel

    @property
    def ThinkModel(self):
        r"""思考模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ThinkModel`
        """
        return self._ThinkModel

    @ThinkModel.setter
    def ThinkModel(self, ThinkModel):
        self._ThinkModel = ThinkModel


    def _deserialize(self, params):
        if params.get("AiOptimizeModel") is not None:
            self._AiOptimizeModel = AIOptimizeModel()
            self._AiOptimizeModel._deserialize(params.get("AiOptimizeModel"))
        if params.get("FileParseModel") is not None:
            self._FileParseModel = FileParseModel()
            self._FileParseModel._deserialize(params.get("FileParseModel"))
        if params.get("GenerateModel") is not None:
            self._GenerateModel = GenerateModel()
            self._GenerateModel._deserialize(params.get("GenerateModel"))
        if params.get("MultiModalQaModel") is not None:
            self._MultiModalQaModel = MultiModalQAModel()
            self._MultiModalQaModel._deserialize(params.get("MultiModalQaModel"))
        if params.get("MultiModalUnderstandingModel") is not None:
            self._MultiModalUnderstandingModel = MultiModalUnderstandingModel()
            self._MultiModalUnderstandingModel._deserialize(params.get("MultiModalUnderstandingModel"))
        if params.get("PromptRewriteModel") is not None:
            self._PromptRewriteModel = PromptRewriteModel()
            self._PromptRewriteModel._deserialize(params.get("PromptRewriteModel"))
        if params.get("ThinkModel") is not None:
            self._ThinkModel = ThinkModel()
            self._ThinkModel._deserialize(params.get("ThinkModel"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppOperation(AbstractModel):
    r"""应用操作信息

    """

    def __init__(self):
        r"""
        :param _Creator: 创建人
        :type Creator: str
        :param _CreatorUin: 创建人UIN
        :type CreatorUin: str
        :param _CreatorUserAccount: 创建人账号(私有化场景使用)
        :type CreatorUserAccount: str
        :param _UpdateTime: 修改时间 (Unix时间戳,秒级)
        :type UpdateTime: str
        :param _Updater: 最后修改人
        :type Updater: str
        :param _UpdaterUin: 修改人UIN
        :type UpdaterUin: str
        """
        self._Creator = None
        self._CreatorUin = None
        self._CreatorUserAccount = None
        self._UpdateTime = None
        self._Updater = None
        self._UpdaterUin = None

    @property
    def Creator(self):
        r"""创建人
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatorUin(self):
        r"""创建人UIN
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CreatorUserAccount(self):
        r"""创建人账号(私有化场景使用)
        :rtype: str
        """
        return self._CreatorUserAccount

    @CreatorUserAccount.setter
    def CreatorUserAccount(self, CreatorUserAccount):
        self._CreatorUserAccount = CreatorUserAccount

    @property
    def UpdateTime(self):
        r"""修改时间 (Unix时间戳,秒级)
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Updater(self):
        r"""最后修改人
        :rtype: str
        """
        return self._Updater

    @Updater.setter
    def Updater(self, Updater):
        self._Updater = Updater

    @property
    def UpdaterUin(self):
        r"""修改人UIN
        :rtype: str
        """
        return self._UpdaterUin

    @UpdaterUin.setter
    def UpdaterUin(self, UpdaterUin):
        self._UpdaterUin = UpdaterUin


    def _deserialize(self, params):
        self._Creator = params.get("Creator")
        self._CreatorUin = params.get("CreatorUin")
        self._CreatorUserAccount = params.get("CreatorUserAccount")
        self._UpdateTime = params.get("UpdateTime")
        self._Updater = params.get("Updater")
        self._UpdaterUin = params.get("UpdaterUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppPluginConfig(AbstractModel):
    r"""应用插件配置信息

    """

    def __init__(self):
        r"""
        :param _AppId: 基于发布应用创建插件的应用ID
        :type AppId: str
        """
        self._AppId = None

    @property
    def AppId(self):
        r"""基于发布应用创建插件的应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSecretInfo(AbstractModel):
    r"""应用密钥信息

    """

    def __init__(self):
        r"""
        :param _AppKey: 应用密钥
        :type AppKey: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._AppKey = None
        self._CreateTime = None

    @property
    def AppKey(self):
        r"""应用密钥
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._AppKey = params.get("AppKey")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppShareAccessControl(AbstractModel):
    r"""AppShareAccessControl

    """

    def __init__(self):
        r"""
        :param _AccessType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_SHARE_ACCESS_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>APP_SHARE_ACCESS_TYPE_PUBLIC</td><td>1</td><td>公开访问(所有用户都可访问)</td></tr><tr><td>APP_SHARE_ACCESS_TYPE_INTERNAL</td><td>2</td><td>内部访问(仅企业用户可访问)</td></tr><tr><td>APP_SHARE_ACCESS_TYPE_ACCOUNT_WHITELIST</td><td>3</td><td>账号白名单(指定UIN/手机/邮箱/IP可访问)</td></tr></tbody></table>
        :type AccessType: int
        :param _Enabled: <p>是否开启访问控制</p><p>枚举值：</p><ul><li>true： 启用</li><li>false： 禁用</li></ul>
        :type Enabled: bool
        :param _Whitelist: <p>白名单信息</p>
        :type Whitelist: list of AppShareWhitelistItem
        """
        self._AccessType = None
        self._Enabled = None
        self._Whitelist = None

    @property
    def AccessType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_SHARE_ACCESS_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>APP_SHARE_ACCESS_TYPE_PUBLIC</td><td>1</td><td>公开访问(所有用户都可访问)</td></tr><tr><td>APP_SHARE_ACCESS_TYPE_INTERNAL</td><td>2</td><td>内部访问(仅企业用户可访问)</td></tr><tr><td>APP_SHARE_ACCESS_TYPE_ACCOUNT_WHITELIST</td><td>3</td><td>账号白名单(指定UIN/手机/邮箱/IP可访问)</td></tr></tbody></table>
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Enabled(self):
        r"""<p>是否开启访问控制</p><p>枚举值：</p><ul><li>true： 启用</li><li>false： 禁用</li></ul>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Whitelist(self):
        r"""<p>白名单信息</p>
        :rtype: list of AppShareWhitelistItem
        """
        return self._Whitelist

    @Whitelist.setter
    def Whitelist(self, Whitelist):
        self._Whitelist = Whitelist


    def _deserialize(self, params):
        self._AccessType = params.get("AccessType")
        self._Enabled = params.get("Enabled")
        if params.get("Whitelist") is not None:
            self._Whitelist = []
            for item in params.get("Whitelist"):
                obj = AppShareWhitelistItem()
                obj._deserialize(item)
                self._Whitelist.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppShareURLInfo(AbstractModel):
    r"""分享链接信息(详情查询返回，用户不可修改部分；access_control 用户可修改部分由 ModifyApp 承载)

    """

    def __init__(self):
        r"""
        :param _AccessControl: 当前生效的访问控制配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessControl: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        :param _ShareUrl: 分享URL
        :type ShareUrl: str
        """
        self._AccessControl = None
        self._ShareUrl = None

    @property
    def AccessControl(self):
        r"""当前生效的访问控制配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        """
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def ShareUrl(self):
        r"""分享URL
        :rtype: str
        """
        return self._ShareUrl

    @ShareUrl.setter
    def ShareUrl(self, ShareUrl):
        self._ShareUrl = ShareUrl


    def _deserialize(self, params):
        if params.get("AccessControl") is not None:
            self._AccessControl = AppShareAccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        self._ShareUrl = params.get("ShareUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppShareWhitelistItem(AbstractModel):
    r"""AppShareWhitelistItem

    """

    def __init__(self):
        r"""
        :param _Type: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_UIN</td><td>1</td><td>UIN账号</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_PHONE</td><td>2</td><td>手机号码</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_EMAIL</td><td>3</td><td>邮箱地址</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_IP</td><td>4</td><td>IP地址</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_RTX</td><td>5</td><td>RTX账号</td></tr></tbody></table>
        :type Type: int
        :param _Values: <p>白名单数组信息</p><p>参数格式：白名单值</p>
        :type Values: list of str
        """
        self._Type = None
        self._Values = None

    @property
    def Type(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_UIN</td><td>1</td><td>UIN账号</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_PHONE</td><td>2</td><td>手机号码</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_EMAIL</td><td>3</td><td>邮箱地址</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_IP</td><td>4</td><td>IP地址</td></tr><tr><td>APP_SHARE_WHITELIST_TYPE_RTX</td><td>5</td><td>RTX账号</td></tr></tbody></table>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        r"""<p>白名单数组信息</p><p>参数格式：白名单值</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSharedKbInfo(AbstractModel):
    r"""应用引用的共享知识库简要信息(查询时仅返回ID和名称)

    """

    def __init__(self):
        r"""
        :param _KbId: 共享知识库ID
        :type KbId: str
        :param _KbName: 共享知识库名称
        :type KbName: str
        """
        self._KbId = None
        self._KbName = None

    @property
    def KbId(self):
        r"""共享知识库ID
        :rtype: str
        """
        return self._KbId

    @KbId.setter
    def KbId(self, KbId):
        self._KbId = KbId

    @property
    def KbName(self):
        r"""共享知识库名称
        :rtype: str
        """
        return self._KbName

    @KbName.setter
    def KbName(self, KbName):
        self._KbName = KbName


    def _deserialize(self, params):
        self._KbId = params.get("KbId")
        self._KbName = params.get("KbName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppStatusInfo(AbstractModel):
    r"""应用状态信息 - 运行时状态信息(用户不可修改)

    """

    def __init__(self):
        r"""
        :param _Status: <p>应用状态</p><p>枚举值：</p><ul><li>1： 未上线</li><li>2： 运行中</li><li>3： 停用</li><li>4： 导入中</li></ul>
        :type Status: int
        :param _StatusDescription: <p>状态描述</p>
        :type StatusDescription: str
        """
        self._Status = None
        self._StatusDescription = None

    @property
    def Status(self):
        r"""<p>应用状态</p><p>枚举值：</p><ul><li>1： 未上线</li><li>2： 运行中</li><li>3： 停用</li><li>4： 导入中</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDescription(self):
        r"""<p>状态描述</p>
        :rtype: str
        """
        return self._StatusDescription

    @StatusDescription.setter
    def StatusDescription(self, StatusDescription):
        self._StatusDescription = StatusDescription


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._StatusDescription = params.get("StatusDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSubStatusInfo(AbstractModel):
    r"""应用子状态信息

    """

    def __init__(self):
        r"""
        :param _ApprovalId: 审批记录ID (当sub_status_list包含PUBLISH_APPROVING时有效)
        :type ApprovalId: str
        :param _SubStatusList: 应用子状态列表 (可能同时处于多个子状态)
        :type SubStatusList: list of int
        """
        self._ApprovalId = None
        self._SubStatusList = None

    @property
    def ApprovalId(self):
        r"""审批记录ID (当sub_status_list包含PUBLISH_APPROVING时有效)
        :rtype: str
        """
        return self._ApprovalId

    @ApprovalId.setter
    def ApprovalId(self, ApprovalId):
        self._ApprovalId = ApprovalId

    @property
    def SubStatusList(self):
        r"""应用子状态列表 (可能同时处于多个子状态)
        :rtype: list of int
        """
        return self._SubStatusList

    @SubStatusList.setter
    def SubStatusList(self, SubStatusList):
        self._SubStatusList = SubStatusList


    def _deserialize(self, params):
        self._ApprovalId = params.get("ApprovalId")
        self._SubStatusList = params.get("SubStatusList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppSummary(AbstractModel):
    r"""应用摘要 - 列表查询返回的应用信息

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _AppMode: 应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :type AppMode: int
        :param _Avatar: 应用头像
        :type Avatar: str
        :param _Name: 应用名称
        :type Name: str
        :param _OperationInfo: 操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OperationInfo: :class:`tencentcloud.adp.v20260520.models.AppOperation`
        :param _Status: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.adp.v20260520.models.AppStatusInfo`
        :param _SubStatus: 子状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubStatus: :class:`tencentcloud.adp.v20260520.models.AppSubStatusInfo`
        :param _PermissionIdList: 资源操作权限
        :type PermissionIdList: list of str
        """
        self._AppId = None
        self._AppMode = None
        self._Avatar = None
        self._Name = None
        self._OperationInfo = None
        self._Status = None
        self._SubStatus = None
        self._PermissionIdList = None

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppMode(self):
        r"""应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :rtype: int
        """
        return self._AppMode

    @AppMode.setter
    def AppMode(self, AppMode):
        self._AppMode = AppMode

    @property
    def Avatar(self):
        r"""应用头像
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Name(self):
        r"""应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OperationInfo(self):
        r"""操作信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppOperation`
        """
        return self._OperationInfo

    @OperationInfo.setter
    def OperationInfo(self, OperationInfo):
        self._OperationInfo = OperationInfo

    @property
    def Status(self):
        r"""状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppStatusInfo`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SubStatus(self):
        r"""子状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppSubStatusInfo`
        """
        return self._SubStatus

    @SubStatus.setter
    def SubStatus(self, SubStatus):
        self._SubStatus = SubStatus

    @property
    def PermissionIdList(self):
        r"""资源操作权限
        :rtype: list of str
        """
        return self._PermissionIdList

    @PermissionIdList.setter
    def PermissionIdList(self, PermissionIdList):
        self._PermissionIdList = PermissionIdList


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppMode = params.get("AppMode")
        self._Avatar = params.get("Avatar")
        self._Name = params.get("Name")
        if params.get("OperationInfo") is not None:
            self._OperationInfo = AppOperation()
            self._OperationInfo._deserialize(params.get("OperationInfo"))
        if params.get("Status") is not None:
            self._Status = AppStatusInfo()
            self._Status._deserialize(params.get("Status"))
        if params.get("SubStatus") is not None:
            self._SubStatus = AppSubStatusInfo()
            self._SubStatus._deserialize(params.get("SubStatus"))
        self._PermissionIdList = params.get("PermissionIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppToolConfig(AbstractModel):
    r"""AppToolConfig

    """

    def __init__(self):
        r"""
        :param _Inputs: <p>输入参数</p>
        :type Inputs: list of RequestParam
        :param _Outputs: <p>输出参数</p>
        :type Outputs: list of ResponseParam
        """
        self._Inputs = None
        self._Outputs = None

    @property
    def Inputs(self):
        r"""<p>输入参数</p>
        :rtype: list of RequestParam
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Outputs(self):
        r"""<p>输出参数</p>
        :rtype: list of ResponseParam
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs


    def _deserialize(self, params):
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Inputs.append(obj)
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = ResponseParam()
                obj._deserialize(item)
                self._Outputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTrigger(AbstractModel):
    r"""AppTrigger

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _ExecuteConfig: <p>执行配置</p>
        :type ExecuteConfig: :class:`tencentcloud.adp.v20260520.models.ExecuteConfig`
        :param _ExecuteType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_PROMPT</td><td>1</td><td>指令执行</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_WORKFLOW</td><td>2</td><td>工作流执行</td></tr></tbody></table>
        :type ExecuteType: int
        :param _FailedCount: <p>失败次数</p>
        :type FailedCount: str
        :param _PushConfig: <p>推送渠道配置</p>
        :type PushConfig: :class:`tencentcloud.adp.v20260520.models.TimerPushConfig`
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _Status: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_STATUS_ENABLED</td><td>1</td><td>启用</td></tr><tr><td>APP_TRIGGER_STATUS_PAUSED</td><td>2</td><td>暂停</td></tr><tr><td>APP_TRIGGER_STATUS_DELETED</td><td>3</td><td>已删除</td></tr></tbody></table>
        :type Status: int
        :param _SuccessCount: <p>成功次数</p>
        :type SuccessCount: str
        :param _TriggerConfig: <p>触发器配置</p>
        :type TriggerConfig: :class:`tencentcloud.adp.v20260520.models.TriggerConfig`
        :param _TriggerId: <p>触发器ID</p>
        :type TriggerId: str
        :param _TriggerName: <p>触发器名称</p>
        :type TriggerName: str
        :param _TriggerStatus: <p>触发器状态</p>
        :type TriggerStatus: :class:`tencentcloud.adp.v20260520.models.TriggerStatus`
        :param _TriggerType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr></tbody></table>
        :type TriggerType: int
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._ExecuteConfig = None
        self._ExecuteType = None
        self._FailedCount = None
        self._PushConfig = None
        self._Scope = None
        self._Status = None
        self._SuccessCount = None
        self._TriggerConfig = None
        self._TriggerId = None
        self._TriggerName = None
        self._TriggerStatus = None
        self._TriggerType = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ExecuteConfig(self):
        r"""<p>执行配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ExecuteConfig`
        """
        return self._ExecuteConfig

    @ExecuteConfig.setter
    def ExecuteConfig(self, ExecuteConfig):
        self._ExecuteConfig = ExecuteConfig

    @property
    def ExecuteType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_PROMPT</td><td>1</td><td>指令执行</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_WORKFLOW</td><td>2</td><td>工作流执行</td></tr></tbody></table>
        :rtype: int
        """
        return self._ExecuteType

    @ExecuteType.setter
    def ExecuteType(self, ExecuteType):
        self._ExecuteType = ExecuteType

    @property
    def FailedCount(self):
        r"""<p>失败次数</p>
        :rtype: str
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount

    @property
    def PushConfig(self):
        r"""<p>推送渠道配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimerPushConfig`
        """
        return self._PushConfig

    @PushConfig.setter
    def PushConfig(self, PushConfig):
        self._PushConfig = PushConfig

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Status(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_STATUS_ENABLED</td><td>1</td><td>启用</td></tr><tr><td>APP_TRIGGER_STATUS_PAUSED</td><td>2</td><td>暂停</td></tr><tr><td>APP_TRIGGER_STATUS_DELETED</td><td>3</td><td>已删除</td></tr></tbody></table>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuccessCount(self):
        r"""<p>成功次数</p>
        :rtype: str
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def TriggerConfig(self):
        r"""<p>触发器配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TriggerConfig`
        """
        return self._TriggerConfig

    @TriggerConfig.setter
    def TriggerConfig(self, TriggerConfig):
        self._TriggerConfig = TriggerConfig

    @property
    def TriggerId(self):
        r"""<p>触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def TriggerName(self):
        r"""<p>触发器名称</p>
        :rtype: str
        """
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def TriggerStatus(self):
        r"""<p>触发器状态</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TriggerStatus`
        """
        return self._TriggerStatus

    @TriggerStatus.setter
    def TriggerStatus(self, TriggerStatus):
        self._TriggerStatus = TriggerStatus

    @property
    def TriggerType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr></tbody></table>
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("ExecuteConfig") is not None:
            self._ExecuteConfig = ExecuteConfig()
            self._ExecuteConfig._deserialize(params.get("ExecuteConfig"))
        self._ExecuteType = params.get("ExecuteType")
        self._FailedCount = params.get("FailedCount")
        if params.get("PushConfig") is not None:
            self._PushConfig = TimerPushConfig()
            self._PushConfig._deserialize(params.get("PushConfig"))
        self._Scope = params.get("Scope")
        self._Status = params.get("Status")
        self._SuccessCount = params.get("SuccessCount")
        if params.get("TriggerConfig") is not None:
            self._TriggerConfig = TriggerConfig()
            self._TriggerConfig._deserialize(params.get("TriggerConfig"))
        self._TriggerId = params.get("TriggerId")
        self._TriggerName = params.get("TriggerName")
        if params.get("TriggerStatus") is not None:
            self._TriggerStatus = TriggerStatus()
            self._TriggerStatus._deserialize(params.get("TriggerStatus"))
        self._TriggerType = params.get("TriggerType")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerInstance(AbstractModel):
    r"""AppTriggerInstance

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用id</p>
        :type AppId: str
        :param _ConversationId: <p>会话id</p>
        :type ConversationId: str
        :param _CreatedAt: <p>触发器创建时间</p>
        :type CreatedAt: str
        :param _FinishedAt: <p>结束时间</p>
        :type FinishedAt: str
        :param _InstanceId: <p>触发器运行实例id</p>
        :type InstanceId: str
        :param _RequestId: <p>请求ID</p>
        :type RequestId: str
        :param _ResultCode: <p>结果码</p>
        :type ResultCode: str
        :param _ResultSummary: <p>结果摘要</p>
        :type ResultSummary: str
        :param _RunId: <p>单次对话id</p>
        :type RunId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _Source: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_INSTANCE_SOURCE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_INSTANCE_SOURCE_APP_TRIGGER</td><td>1</td><td>来源于应用触发器</td></tr></tbody></table>
        :type Source: int
        :param _StartedAt: <p>触发器开始执行时间</p>
        :type StartedAt: str
        :param _Status: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TIMER_RUN_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>TIMER_RUN_STATUS_PENDING</td><td>1</td><td>等待执行</td></tr><tr><td>TIMER_RUN_STATUS_RUNNING</td><td>2</td><td>执行中</td></tr><tr><td>TIMER_RUN_STATUS_RETRY_WAIT</td><td>3</td><td>等待重试</td></tr><tr><td>TIMER_RUN_STATUS_SUCCESS</td><td>4</td><td>成功</td></tr><tr><td>TIMER_RUN_STATUS_DEAD</td><td>5</td><td>失败终态 (重试耗尽 / 不可重试)</td></tr><tr><td>TIMER_RUN_STATUS_CANCELLED</td><td>6</td><td>被任务暂停/删除/修改取消</td></tr></tbody></table>
        :type Status: int
        :param _TraceId: <p>TraceId，用于日志记录</p>
        :type TraceId: str
        :param _TriggerId: <p>触发器id</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        :param _WorkflowRunId: <p>工作流运行ID</p>
        :type WorkflowRunId: str
        """
        self._AppId = None
        self._ConversationId = None
        self._CreatedAt = None
        self._FinishedAt = None
        self._InstanceId = None
        self._RequestId = None
        self._ResultCode = None
        self._ResultSummary = None
        self._RunId = None
        self._Scope = None
        self._Source = None
        self._StartedAt = None
        self._Status = None
        self._TraceId = None
        self._TriggerId = None
        self._UserId = None
        self._WorkflowRunId = None

    @property
    def AppId(self):
        r"""<p>应用id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ConversationId(self):
        r"""<p>会话id</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def CreatedAt(self):
        r"""<p>触发器创建时间</p>
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def FinishedAt(self):
        r"""<p>结束时间</p>
        :rtype: str
        """
        return self._FinishedAt

    @FinishedAt.setter
    def FinishedAt(self, FinishedAt):
        self._FinishedAt = FinishedAt

    @property
    def InstanceId(self):
        r"""<p>触发器运行实例id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RequestId(self):
        r"""<p>请求ID</p>
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def ResultCode(self):
        r"""<p>结果码</p>
        :rtype: str
        """
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultSummary(self):
        r"""<p>结果摘要</p>
        :rtype: str
        """
        return self._ResultSummary

    @ResultSummary.setter
    def ResultSummary(self, ResultSummary):
        self._ResultSummary = ResultSummary

    @property
    def RunId(self):
        r"""<p>单次对话id</p>
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Source(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_INSTANCE_SOURCE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_INSTANCE_SOURCE_APP_TRIGGER</td><td>1</td><td>来源于应用触发器</td></tr></tbody></table>
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def StartedAt(self):
        r"""<p>触发器开始执行时间</p>
        :rtype: str
        """
        return self._StartedAt

    @StartedAt.setter
    def StartedAt(self, StartedAt):
        self._StartedAt = StartedAt

    @property
    def Status(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TIMER_RUN_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>TIMER_RUN_STATUS_PENDING</td><td>1</td><td>等待执行</td></tr><tr><td>TIMER_RUN_STATUS_RUNNING</td><td>2</td><td>执行中</td></tr><tr><td>TIMER_RUN_STATUS_RETRY_WAIT</td><td>3</td><td>等待重试</td></tr><tr><td>TIMER_RUN_STATUS_SUCCESS</td><td>4</td><td>成功</td></tr><tr><td>TIMER_RUN_STATUS_DEAD</td><td>5</td><td>失败终态 (重试耗尽 / 不可重试)</td></tr><tr><td>TIMER_RUN_STATUS_CANCELLED</td><td>6</td><td>被任务暂停/删除/修改取消</td></tr></tbody></table>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TraceId(self):
        r"""<p>TraceId，用于日志记录</p>
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def TriggerId(self):
        r"""<p>触发器id</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行ID</p>
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ConversationId = params.get("ConversationId")
        self._CreatedAt = params.get("CreatedAt")
        self._FinishedAt = params.get("FinishedAt")
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")
        self._ResultCode = params.get("ResultCode")
        self._ResultSummary = params.get("ResultSummary")
        self._RunId = params.get("RunId")
        self._Scope = params.get("Scope")
        self._Source = params.get("Source")
        self._StartedAt = params.get("StartedAt")
        self._Status = params.get("Status")
        self._TraceId = params.get("TraceId")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerParamBinding(AbstractModel):
    r"""AppTriggerParamBinding

    """

    def __init__(self):
        r"""
        :param _ParamName: <p>参数名字</p>
        :type ParamName: str
        :param _ParamType: <p>参数类型</p><p>枚举值：</p><ul><li>0： 字符串</li><li>1： 整数</li><li>2： 浮点数</li><li>4： 对象</li><li>5： 字符串数组</li><li>6： 整数数组</li><li>7： 浮点数数组</li><li>8： 布尔值数组</li><li>3： 布尔值</li><li>9： 对象数组</li><li>10： 文件</li><li>11： 文档</li><li>12： 图片</li><li>13： 音频</li><li>14： 视频</li><li>15： 文件数组</li><li>16： 文档数组</li><li>17： 图片数组</li><li>18： 音频数组</li><li>19： 视频数组</li><li>20： 数组嵌套</li><li>22： 密钥</li><li>99： 空值</li><li>100： 未指定类型，用于OneOf和AnyOf场景</li></ul>
        :type ParamType: int
        :param _Value: <p>参数值</p>
        :type Value: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingValue`
        """
        self._ParamName = None
        self._ParamType = None
        self._Value = None

    @property
    def ParamName(self):
        r"""<p>参数名字</p>
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        r"""<p>参数类型</p><p>枚举值：</p><ul><li>0： 字符串</li><li>1： 整数</li><li>2： 浮点数</li><li>4： 对象</li><li>5： 字符串数组</li><li>6： 整数数组</li><li>7： 浮点数数组</li><li>8： 布尔值数组</li><li>3： 布尔值</li><li>9： 对象数组</li><li>10： 文件</li><li>11： 文档</li><li>12： 图片</li><li>13： 音频</li><li>14： 视频</li><li>15： 文件数组</li><li>16： 文档数组</li><li>17： 图片数组</li><li>18： 音频数组</li><li>19： 视频数组</li><li>20： 数组嵌套</li><li>22： 密钥</li><li>99： 空值</li><li>100： 未指定类型，用于OneOf和AnyOf场景</li></ul>
        :rtype: int
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Value(self):
        r"""<p>参数值</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingValue`
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamType = params.get("ParamType")
        if params.get("Value") is not None:
            self._Value = AppTriggerParamBindingValue()
            self._Value._deserialize(params.get("Value"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerParamBindingConfig(AbstractModel):
    r"""AppTriggerParamBindingConfig

    """

    def __init__(self):
        r"""
        :param _ParamList: <p>绑定参数列表</p>
        :type ParamList: list of AppTriggerParamBinding
        """
        self._ParamList = None

    @property
    def ParamList(self):
        r"""<p>绑定参数列表</p>
        :rtype: list of AppTriggerParamBinding
        """
        return self._ParamList

    @ParamList.setter
    def ParamList(self, ParamList):
        self._ParamList = ParamList


    def _deserialize(self, params):
        if params.get("ParamList") is not None:
            self._ParamList = []
            for item in params.get("ParamList"):
                obj = AppTriggerParamBinding()
                obj._deserialize(item)
                self._ParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerParamBindingValue(AbstractModel):
    r"""AppTriggerParamBindingValue

    """

    def __init__(self):
        r"""
        :param _ParamValue: <p>参数值</p>
        :type ParamValue: str
        :param _VariableName: <p>应用变量名</p>
        :type VariableName: str
        """
        self._ParamValue = None
        self._VariableName = None

    @property
    def ParamValue(self):
        r"""<p>参数值</p>
        :rtype: str
        """
        return self._ParamValue

    @ParamValue.setter
    def ParamValue(self, ParamValue):
        self._ParamValue = ParamValue

    @property
    def VariableName(self):
        r"""<p>应用变量名</p>
        :rtype: str
        """
        return self._VariableName

    @VariableName.setter
    def VariableName(self, VariableName):
        self._VariableName = VariableName


    def _deserialize(self, params):
        self._ParamValue = params.get("ParamValue")
        self._VariableName = params.get("VariableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerParamSchema(AbstractModel):
    r"""AppTriggerParamSchema

    """

    def __init__(self):
        r"""
        :param _ParamName: <p>参数名</p>
        :type ParamName: str
        :param _ParamType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>PARAM_TYPE_STRING</td><td>0</td><td>字符串</td></tr><tr><td>PARAM_TYPE_INT</td><td>1</td><td>整数</td></tr><tr><td>PARAM_TYPE_FLOAT</td><td>2</td><td>浮点数</td></tr><tr><td>PARAM_TYPE_BOOL</td><td>3</td><td>布尔值</td></tr><tr><td>PARAM_TYPE_OBJECT</td><td>4</td><td>对象</td></tr><tr><td>PARAM_TYPE_ARRAY_STRING</td><td>5</td><td>字符串数组</td></tr><tr><td>PARAM_TYPE_ARRAY_INT</td><td>6</td><td>整数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_FLOAT</td><td>7</td><td>浮点数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_BOOL</td><td>8</td><td>布尔值数组</td></tr><tr><td>PARAM_TYPE_ARRAY_OBJECT</td><td>9</td><td>对象数组</td></tr><tr><td>PARAM_TYPE_ARRAY_ARRAY</td><td>20</td><td>数组嵌套</td></tr><tr><td>PARAM_TYPE_NULL</td><td>99</td><td>空值</td></tr><tr><td>PARAM_TYPE_UNSPECIFIED</td><td>100</td><td>未指定类型，用于OneOf和AnyOf场景</td></tr></tbody></table>
        :type ParamType: int
        :param _Required: <p>是否必选</p>
        :type Required: bool
        :param _SubParamList: <p>子参数列表</p>
        :type SubParamList: list of AppTriggerParamSchema
        """
        self._ParamName = None
        self._ParamType = None
        self._Required = None
        self._SubParamList = None

    @property
    def ParamName(self):
        r"""<p>参数名</p>
        :rtype: str
        """
        return self._ParamName

    @ParamName.setter
    def ParamName(self, ParamName):
        self._ParamName = ParamName

    @property
    def ParamType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>PARAM_TYPE_STRING</td><td>0</td><td>字符串</td></tr><tr><td>PARAM_TYPE_INT</td><td>1</td><td>整数</td></tr><tr><td>PARAM_TYPE_FLOAT</td><td>2</td><td>浮点数</td></tr><tr><td>PARAM_TYPE_BOOL</td><td>3</td><td>布尔值</td></tr><tr><td>PARAM_TYPE_OBJECT</td><td>4</td><td>对象</td></tr><tr><td>PARAM_TYPE_ARRAY_STRING</td><td>5</td><td>字符串数组</td></tr><tr><td>PARAM_TYPE_ARRAY_INT</td><td>6</td><td>整数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_FLOAT</td><td>7</td><td>浮点数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_BOOL</td><td>8</td><td>布尔值数组</td></tr><tr><td>PARAM_TYPE_ARRAY_OBJECT</td><td>9</td><td>对象数组</td></tr><tr><td>PARAM_TYPE_ARRAY_ARRAY</td><td>20</td><td>数组嵌套</td></tr><tr><td>PARAM_TYPE_NULL</td><td>99</td><td>空值</td></tr><tr><td>PARAM_TYPE_UNSPECIFIED</td><td>100</td><td>未指定类型，用于OneOf和AnyOf场景</td></tr></tbody></table>
        :rtype: int
        """
        return self._ParamType

    @ParamType.setter
    def ParamType(self, ParamType):
        self._ParamType = ParamType

    @property
    def Required(self):
        r"""<p>是否必选</p>
        :rtype: bool
        """
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def SubParamList(self):
        r"""<p>子参数列表</p>
        :rtype: list of AppTriggerParamSchema
        """
        return self._SubParamList

    @SubParamList.setter
    def SubParamList(self, SubParamList):
        self._SubParamList = SubParamList


    def _deserialize(self, params):
        self._ParamName = params.get("ParamName")
        self._ParamType = params.get("ParamType")
        self._Required = params.get("Required")
        if params.get("SubParamList") is not None:
            self._SubParamList = []
            for item in params.get("SubParamList"):
                obj = AppTriggerParamSchema()
                obj._deserialize(item)
                self._SubParamList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerPromptExecuteConfig(AbstractModel):
    r"""AppTriggerPromptExecuteConfig

    """

    def __init__(self):
        r"""
        :param _ExecutePrompt: <p>触发器执行提示词</p>
        :type ExecutePrompt: str
        :param _ParamBindingsApi: <p>api参数绑定</p>
        :type ParamBindingsApi: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingConfig`
        """
        self._ExecutePrompt = None
        self._ParamBindingsApi = None

    @property
    def ExecutePrompt(self):
        r"""<p>触发器执行提示词</p>
        :rtype: str
        """
        return self._ExecutePrompt

    @ExecutePrompt.setter
    def ExecutePrompt(self, ExecutePrompt):
        self._ExecutePrompt = ExecutePrompt

    @property
    def ParamBindingsApi(self):
        r"""<p>api参数绑定</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingConfig`
        """
        return self._ParamBindingsApi

    @ParamBindingsApi.setter
    def ParamBindingsApi(self, ParamBindingsApi):
        self._ParamBindingsApi = ParamBindingsApi


    def _deserialize(self, params):
        self._ExecutePrompt = params.get("ExecutePrompt")
        if params.get("ParamBindingsApi") is not None:
            self._ParamBindingsApi = AppTriggerParamBindingConfig()
            self._ParamBindingsApi._deserialize(params.get("ParamBindingsApi"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerRunLog(AbstractModel):
    r"""AppTriggerRunLog

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话id</p>
        :type ConversationId: str
        :param _DurationMs: <p>执行时间</p>
        :type DurationMs: str
        :param _EndTime: <p>结束时间</p><p>参数格式：YYYY-MM-DD hh:mm:ss</p>
        :type EndTime: str
        :param _FireType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_MANUAL_RUN</td><td>3</td><td>手动立即执行</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_TEST_RUN</td><td>4</td><td>测试执行</td></tr></tbody></table>
        :type FireType: int
        :param _InstanceId: <p>触发实例id</p>
        :type InstanceId: str
        :param _PushStatus: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_NONE</td><td>1</td><td>未配置推送</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_WAITING</td><td>2</td><td>等待推送</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_SUCCESS</td><td>3</td><td>推送成功</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_FAILED</td><td>4</td><td>推送失败</td></tr></tbody></table>
        :type PushStatus: int
        :param _ResultCode: <p>结果码</p>
        :type ResultCode: str
        :param _ResultSummary: <p>结果概要</p>
        :type ResultSummary: str
        :param _RunId: <p>单次对话id</p>
        :type RunId: str
        :param _ScheduledFireTime: <p>触发时间</p><p>参数格式：YYYY:MM:DD hh:mm:ss</p>
        :type ScheduledFireTime: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _StartTime: <p>开始执行时间</p><p>参数格式：YYYY:MM:DD hh:mm:ss</p>
        :type StartTime: str
        :param _Status: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TIMER_RUN_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>TIMER_RUN_STATUS_PENDING</td><td>1</td><td>等待执行</td></tr><tr><td>TIMER_RUN_STATUS_RUNNING</td><td>2</td><td>执行中</td></tr><tr><td>TIMER_RUN_STATUS_RETRY_WAIT</td><td>3</td><td>等待重试</td></tr><tr><td>TIMER_RUN_STATUS_SUCCESS</td><td>4</td><td>成功</td></tr><tr><td>TIMER_RUN_STATUS_DEAD</td><td>5</td><td>失败终态 (重试耗尽 / 不可重试)</td></tr><tr><td>TIMER_RUN_STATUS_CANCELLED</td><td>6</td><td>被任务暂停/删除/修改取消</td></tr></tbody></table>
        :type Status: int
        :param _TriggerId: <p>触发器id</p>
        :type TriggerId: str
        :param _Unread: <p>是否已读</p>
        :type Unread: bool
        :param _UserId: <p>访客Id</p>
        :type UserId: str
        :param _WorkflowRunId: <p>工作流运行id</p>
        :type WorkflowRunId: str
        """
        self._ConversationId = None
        self._DurationMs = None
        self._EndTime = None
        self._FireType = None
        self._InstanceId = None
        self._PushStatus = None
        self._ResultCode = None
        self._ResultSummary = None
        self._RunId = None
        self._ScheduledFireTime = None
        self._Scope = None
        self._StartTime = None
        self._Status = None
        self._TriggerId = None
        self._Unread = None
        self._UserId = None
        self._WorkflowRunId = None

    @property
    def ConversationId(self):
        r"""<p>会话id</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def DurationMs(self):
        r"""<p>执行时间</p>
        :rtype: str
        """
        return self._DurationMs

    @DurationMs.setter
    def DurationMs(self, DurationMs):
        self._DurationMs = DurationMs

    @property
    def EndTime(self):
        r"""<p>结束时间</p><p>参数格式：YYYY-MM-DD hh:mm:ss</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def FireType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_MANUAL_RUN</td><td>3</td><td>手动立即执行</td></tr><tr><td>APP_TRIGGER_FIRE_TYPE_TEST_RUN</td><td>4</td><td>测试执行</td></tr></tbody></table>
        :rtype: int
        """
        return self._FireType

    @FireType.setter
    def FireType(self, FireType):
        self._FireType = FireType

    @property
    def InstanceId(self):
        r"""<p>触发实例id</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PushStatus(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_NONE</td><td>1</td><td>未配置推送</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_WAITING</td><td>2</td><td>等待推送</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_SUCCESS</td><td>3</td><td>推送成功</td></tr><tr><td>TIMER_RUN_PUSH_STATUS_FAILED</td><td>4</td><td>推送失败</td></tr></tbody></table>
        :rtype: int
        """
        return self._PushStatus

    @PushStatus.setter
    def PushStatus(self, PushStatus):
        self._PushStatus = PushStatus

    @property
    def ResultCode(self):
        r"""<p>结果码</p>
        :rtype: str
        """
        return self._ResultCode

    @ResultCode.setter
    def ResultCode(self, ResultCode):
        self._ResultCode = ResultCode

    @property
    def ResultSummary(self):
        r"""<p>结果概要</p>
        :rtype: str
        """
        return self._ResultSummary

    @ResultSummary.setter
    def ResultSummary(self, ResultSummary):
        self._ResultSummary = ResultSummary

    @property
    def RunId(self):
        r"""<p>单次对话id</p>
        :rtype: str
        """
        return self._RunId

    @RunId.setter
    def RunId(self, RunId):
        self._RunId = RunId

    @property
    def ScheduledFireTime(self):
        r"""<p>触发时间</p><p>参数格式：YYYY:MM:DD hh:mm:ss</p>
        :rtype: str
        """
        return self._ScheduledFireTime

    @ScheduledFireTime.setter
    def ScheduledFireTime(self, ScheduledFireTime):
        self._ScheduledFireTime = ScheduledFireTime

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def StartTime(self):
        r"""<p>开始执行时间</p><p>参数格式：YYYY:MM:DD hh:mm:ss</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def Status(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TIMER_RUN_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>TIMER_RUN_STATUS_PENDING</td><td>1</td><td>等待执行</td></tr><tr><td>TIMER_RUN_STATUS_RUNNING</td><td>2</td><td>执行中</td></tr><tr><td>TIMER_RUN_STATUS_RETRY_WAIT</td><td>3</td><td>等待重试</td></tr><tr><td>TIMER_RUN_STATUS_SUCCESS</td><td>4</td><td>成功</td></tr><tr><td>TIMER_RUN_STATUS_DEAD</td><td>5</td><td>失败终态 (重试耗尽 / 不可重试)</td></tr><tr><td>TIMER_RUN_STATUS_CANCELLED</td><td>6</td><td>被任务暂停/删除/修改取消</td></tr></tbody></table>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TriggerId(self):
        r"""<p>触发器id</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def Unread(self):
        r"""<p>是否已读</p>
        :rtype: bool
        """
        return self._Unread

    @Unread.setter
    def Unread(self, Unread):
        self._Unread = Unread

    @property
    def UserId(self):
        r"""<p>访客Id</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def WorkflowRunId(self):
        r"""<p>工作流运行id</p>
        :rtype: str
        """
        return self._WorkflowRunId

    @WorkflowRunId.setter
    def WorkflowRunId(self, WorkflowRunId):
        self._WorkflowRunId = WorkflowRunId


    def _deserialize(self, params):
        self._ConversationId = params.get("ConversationId")
        self._DurationMs = params.get("DurationMs")
        self._EndTime = params.get("EndTime")
        self._FireType = params.get("FireType")
        self._InstanceId = params.get("InstanceId")
        self._PushStatus = params.get("PushStatus")
        self._ResultCode = params.get("ResultCode")
        self._ResultSummary = params.get("ResultSummary")
        self._RunId = params.get("RunId")
        self._ScheduledFireTime = params.get("ScheduledFireTime")
        self._Scope = params.get("Scope")
        self._StartTime = params.get("StartTime")
        self._Status = params.get("Status")
        self._TriggerId = params.get("TriggerId")
        self._Unread = params.get("Unread")
        self._UserId = params.get("UserId")
        self._WorkflowRunId = params.get("WorkflowRunId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerScheduleConfig(AbstractModel):
    r"""AppTriggerScheduleConfig

    """

    def __init__(self):
        r"""
        :param _Schedule: <p>触发器定时配置</p>
        :type Schedule: :class:`tencentcloud.adp.v20260520.models.TimerScheduleConfig`
        """
        self._Schedule = None

    @property
    def Schedule(self):
        r"""<p>触发器定时配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimerScheduleConfig`
        """
        return self._Schedule

    @Schedule.setter
    def Schedule(self, Schedule):
        self._Schedule = Schedule


    def _deserialize(self, params):
        if params.get("Schedule") is not None:
            self._Schedule = TimerScheduleConfig()
            self._Schedule._deserialize(params.get("Schedule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerScheduleStatus(AbstractModel):
    r"""AppTriggerScheduleStatus

    """

    def __init__(self):
        r"""
        :param _LastFireTime: <p>最近一次触发时间</p><p>参数格式：格式为YYYY-MM-DD hh:mm:ss</p>
        :type LastFireTime: str
        :param _NextFireTime: <p>下一次触发时间</p><p>参数格式：格式为YYYY-MM-DD hh:mm:ss</p>
        :type NextFireTime: str
        :param _PolicySummary: <p>触发方式</p>
        :type PolicySummary: str
        """
        self._LastFireTime = None
        self._NextFireTime = None
        self._PolicySummary = None

    @property
    def LastFireTime(self):
        r"""<p>最近一次触发时间</p><p>参数格式：格式为YYYY-MM-DD hh:mm:ss</p>
        :rtype: str
        """
        return self._LastFireTime

    @LastFireTime.setter
    def LastFireTime(self, LastFireTime):
        self._LastFireTime = LastFireTime

    @property
    def NextFireTime(self):
        r"""<p>下一次触发时间</p><p>参数格式：格式为YYYY-MM-DD hh:mm:ss</p>
        :rtype: str
        """
        return self._NextFireTime

    @NextFireTime.setter
    def NextFireTime(self, NextFireTime):
        self._NextFireTime = NextFireTime

    @property
    def PolicySummary(self):
        r"""<p>触发方式</p>
        :rtype: str
        """
        return self._PolicySummary

    @PolicySummary.setter
    def PolicySummary(self, PolicySummary):
        self._PolicySummary = PolicySummary


    def _deserialize(self, params):
        self._LastFireTime = params.get("LastFireTime")
        self._NextFireTime = params.get("NextFireTime")
        self._PolicySummary = params.get("PolicySummary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerSummary(AbstractModel):
    r"""AppTriggerSummary

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _ExecuteType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_PROMPT</td><td>1</td><td>指令执行</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_WORKFLOW</td><td>2</td><td>工作流执行</td></tr></tbody></table>
        :type ExecuteType: int
        :param _FailedCount: <p>失败次数</p>
        :type FailedCount: str
        :param _LastSessionId: <p>最近一次会话id</p>
        :type LastSessionId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table><p>取值范围：[0, 2]</p>
        :type Scope: int
        :param _Status: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_STATUS_ENABLED</td><td>1</td><td>启用</td></tr><tr><td>APP_TRIGGER_STATUS_PAUSED</td><td>2</td><td>暂停</td></tr><tr><td>APP_TRIGGER_STATUS_DELETED</td><td>3</td><td>已删除</td></tr></tbody></table>
        :type Status: int
        :param _SuccessCount: <p>成功次数</p>
        :type SuccessCount: str
        :param _TriggerId: <p>触发器id</p>
        :type TriggerId: str
        :param _TriggerName: <p>触发器名称</p>
        :type TriggerName: str
        :param _TriggerStatus: <p>触发器执行状态</p>
        :type TriggerStatus: :class:`tencentcloud.adp.v20260520.models.TriggerStatus`
        :param _TriggerType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr></tbody></table>
        :type TriggerType: int
        :param _UnreadRunLogCount: <p>未读日志的数量</p>
        :type UnreadRunLogCount: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._ExecuteType = None
        self._FailedCount = None
        self._LastSessionId = None
        self._Scope = None
        self._Status = None
        self._SuccessCount = None
        self._TriggerId = None
        self._TriggerName = None
        self._TriggerStatus = None
        self._TriggerType = None
        self._UnreadRunLogCount = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ExecuteType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_PROMPT</td><td>1</td><td>指令执行</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_WORKFLOW</td><td>2</td><td>工作流执行</td></tr></tbody></table>
        :rtype: int
        """
        return self._ExecuteType

    @ExecuteType.setter
    def ExecuteType(self, ExecuteType):
        self._ExecuteType = ExecuteType

    @property
    def FailedCount(self):
        r"""<p>失败次数</p>
        :rtype: str
        """
        return self._FailedCount

    @FailedCount.setter
    def FailedCount(self, FailedCount):
        self._FailedCount = FailedCount

    @property
    def LastSessionId(self):
        r"""<p>最近一次会话id</p>
        :rtype: str
        """
        return self._LastSessionId

    @LastSessionId.setter
    def LastSessionId(self, LastSessionId):
        self._LastSessionId = LastSessionId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table><p>取值范围：[0, 2]</p>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Status(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_STATUS_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_STATUS_ENABLED</td><td>1</td><td>启用</td></tr><tr><td>APP_TRIGGER_STATUS_PAUSED</td><td>2</td><td>暂停</td></tr><tr><td>APP_TRIGGER_STATUS_DELETED</td><td>3</td><td>已删除</td></tr></tbody></table>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SuccessCount(self):
        r"""<p>成功次数</p>
        :rtype: str
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def TriggerId(self):
        r"""<p>触发器id</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def TriggerName(self):
        r"""<p>触发器名称</p>
        :rtype: str
        """
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def TriggerStatus(self):
        r"""<p>触发器执行状态</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TriggerStatus`
        """
        return self._TriggerStatus

    @TriggerStatus.setter
    def TriggerStatus(self, TriggerStatus):
        self._TriggerStatus = TriggerStatus

    @property
    def TriggerType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr></tbody></table>
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def UnreadRunLogCount(self):
        r"""<p>未读日志的数量</p>
        :rtype: str
        """
        return self._UnreadRunLogCount

    @UnreadRunLogCount.setter
    def UnreadRunLogCount(self, UnreadRunLogCount):
        self._UnreadRunLogCount = UnreadRunLogCount

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ExecuteType = params.get("ExecuteType")
        self._FailedCount = params.get("FailedCount")
        self._LastSessionId = params.get("LastSessionId")
        self._Scope = params.get("Scope")
        self._Status = params.get("Status")
        self._SuccessCount = params.get("SuccessCount")
        self._TriggerId = params.get("TriggerId")
        self._TriggerName = params.get("TriggerName")
        if params.get("TriggerStatus") is not None:
            self._TriggerStatus = TriggerStatus()
            self._TriggerStatus._deserialize(params.get("TriggerStatus"))
        self._TriggerType = params.get("TriggerType")
        self._UnreadRunLogCount = params.get("UnreadRunLogCount")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerWebhookConfig(AbstractModel):
    r"""AppTriggerWebhookConfig

    """

    def __init__(self):
        r"""
        :param _ParamSchemaConfig: <p>触发器webhook参数配置</p>
        :type ParamSchemaConfig: :class:`tencentcloud.adp.v20260520.models.AppTriggerWebhookParamSchemaConfig`
        :param _WebhookKey: <p>webhook的key</p>
        :type WebhookKey: str
        :param _WebhookToken: <p>webhook的密钥</p>
        :type WebhookToken: str
        :param _WebhookUrl: <p>webhook的地址</p>
        :type WebhookUrl: str
        """
        self._ParamSchemaConfig = None
        self._WebhookKey = None
        self._WebhookToken = None
        self._WebhookUrl = None

    @property
    def ParamSchemaConfig(self):
        r"""<p>触发器webhook参数配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerWebhookParamSchemaConfig`
        """
        return self._ParamSchemaConfig

    @ParamSchemaConfig.setter
    def ParamSchemaConfig(self, ParamSchemaConfig):
        self._ParamSchemaConfig = ParamSchemaConfig

    @property
    def WebhookKey(self):
        r"""<p>webhook的key</p>
        :rtype: str
        """
        return self._WebhookKey

    @WebhookKey.setter
    def WebhookKey(self, WebhookKey):
        self._WebhookKey = WebhookKey

    @property
    def WebhookToken(self):
        r"""<p>webhook的密钥</p>
        :rtype: str
        """
        return self._WebhookToken

    @WebhookToken.setter
    def WebhookToken(self, WebhookToken):
        self._WebhookToken = WebhookToken

    @property
    def WebhookUrl(self):
        r"""<p>webhook的地址</p>
        :rtype: str
        """
        return self._WebhookUrl

    @WebhookUrl.setter
    def WebhookUrl(self, WebhookUrl):
        self._WebhookUrl = WebhookUrl


    def _deserialize(self, params):
        if params.get("ParamSchemaConfig") is not None:
            self._ParamSchemaConfig = AppTriggerWebhookParamSchemaConfig()
            self._ParamSchemaConfig._deserialize(params.get("ParamSchemaConfig"))
        self._WebhookKey = params.get("WebhookKey")
        self._WebhookToken = params.get("WebhookToken")
        self._WebhookUrl = params.get("WebhookUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerWebhookParamSchemaConfig(AbstractModel):
    r"""AppTriggerWebhookParamSchemaConfig

    """

    def __init__(self):
        r"""
        :param _SchemaList: <p>触发器API参数列表</p>
        :type SchemaList: list of AppTriggerParamSchema
        """
        self._SchemaList = None

    @property
    def SchemaList(self):
        r"""<p>触发器API参数列表</p>
        :rtype: list of AppTriggerParamSchema
        """
        return self._SchemaList

    @SchemaList.setter
    def SchemaList(self, SchemaList):
        self._SchemaList = SchemaList


    def _deserialize(self, params):
        if params.get("SchemaList") is not None:
            self._SchemaList = []
            for item in params.get("SchemaList"):
                obj = AppTriggerParamSchema()
                obj._deserialize(item)
                self._SchemaList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerWebhookStatus(AbstractModel):
    r"""AppTriggerWebhookStatus

    """

    def __init__(self):
        r"""
        :param _WebhookUrl: <p>推送Webbook地址</p>
        :type WebhookUrl: str
        """
        self._WebhookUrl = None

    @property
    def WebhookUrl(self):
        r"""<p>推送Webbook地址</p>
        :rtype: str
        """
        return self._WebhookUrl

    @WebhookUrl.setter
    def WebhookUrl(self, WebhookUrl):
        self._WebhookUrl = WebhookUrl


    def _deserialize(self, params):
        self._WebhookUrl = params.get("WebhookUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppTriggerWorkflowExecuteConfig(AbstractModel):
    r"""AppTriggerWorkflowExecuteConfig

    """

    def __init__(self):
        r"""
        :param _ParamBindingsApi: <p>工作流API参数绑定</p>
        :type ParamBindingsApi: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingConfig`
        :param _ParamBindingsWorkflow: <p>工作流参数绑定</p>
        :type ParamBindingsWorkflow: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingConfig`
        :param _WorkflowId: <p>工作流ID</p>
        :type WorkflowId: str
        :param _WorkflowName: <p>工作流名字</p>
        :type WorkflowName: str
        """
        self._ParamBindingsApi = None
        self._ParamBindingsWorkflow = None
        self._WorkflowId = None
        self._WorkflowName = None

    @property
    def ParamBindingsApi(self):
        r"""<p>工作流API参数绑定</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingConfig`
        """
        return self._ParamBindingsApi

    @ParamBindingsApi.setter
    def ParamBindingsApi(self, ParamBindingsApi):
        self._ParamBindingsApi = ParamBindingsApi

    @property
    def ParamBindingsWorkflow(self):
        r"""<p>工作流参数绑定</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerParamBindingConfig`
        """
        return self._ParamBindingsWorkflow

    @ParamBindingsWorkflow.setter
    def ParamBindingsWorkflow(self, ParamBindingsWorkflow):
        self._ParamBindingsWorkflow = ParamBindingsWorkflow

    @property
    def WorkflowId(self):
        r"""<p>工作流ID</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""<p>工作流名字</p>
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName


    def _deserialize(self, params):
        if params.get("ParamBindingsApi") is not None:
            self._ParamBindingsApi = AppTriggerParamBindingConfig()
            self._ParamBindingsApi._deserialize(params.get("ParamBindingsApi"))
        if params.get("ParamBindingsWorkflow") is not None:
            self._ParamBindingsWorkflow = AppTriggerParamBindingConfig()
            self._ParamBindingsWorkflow._deserialize(params.get("ParamBindingsWorkflow"))
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppWebSearchConfig(AbstractModel):
    r"""联网搜索配置(国际版使用)

    """

    def __init__(self):
        r"""
        :param _ApiKey: API密钥
        :type ApiKey: str
        :param _Enabled: 是否开启
        :type Enabled: bool
        :param _Provider: 服务提供商
        :type Provider: str
        :param _TopN: 返回结果数量
        :type TopN: int
        """
        self._ApiKey = None
        self._Enabled = None
        self._Provider = None
        self._TopN = None

    @property
    def ApiKey(self):
        r"""API密钥
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Enabled(self):
        r"""是否开启
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Provider(self):
        r"""服务提供商
        :rtype: str
        """
        return self._Provider

    @Provider.setter
    def Provider(self, Provider):
        self._Provider = Provider

    @property
    def TopN(self):
        r"""返回结果数量
        :rtype: int
        """
        return self._TopN

    @TopN.setter
    def TopN(self, TopN):
        self._TopN = TopN


    def _deserialize(self, params):
        self._ApiKey = params.get("ApiKey")
        self._Enabled = params.get("Enabled")
        self._Provider = params.get("Provider")
        self._TopN = params.get("TopN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppWorkflowConfig(AbstractModel):
    r"""工作流配置

    """

    def __init__(self):
        r"""
        :param _EnablePDL: 是否使用PDL
        :type EnablePDL: bool
        """
        self._EnablePDL = None

    @property
    def EnablePDL(self):
        r"""是否使用PDL
        :rtype: bool
        """
        return self._EnablePDL

    @EnablePDL.setter
    def EnablePDL(self, EnablePDL):
        self._EnablePDL = EnablePDL


    def _deserialize(self, params):
        self._EnablePDL = params.get("EnablePDL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppealingStatus(AbstractModel):
    r"""申诉中的配置 - 记录各配置项是否在申诉中

    """

    def __init__(self):
        r"""
        :param _AvatarInAppeal: 头像是否在申诉中
        :type AvatarInAppeal: bool
        :param _FallbackReplyInAppeal: 兜底回复语是否在申诉中
        :type FallbackReplyInAppeal: bool
        :param _GreetingInAppeal: 欢迎语是否在申诉中
        :type GreetingInAppeal: bool
        :param _NameInAppeal: 应用名称是否在申诉中
        :type NameInAppeal: bool
        :param _RoleInAppeal: 角色描述是否在申诉中
        :type RoleInAppeal: bool
        """
        self._AvatarInAppeal = None
        self._FallbackReplyInAppeal = None
        self._GreetingInAppeal = None
        self._NameInAppeal = None
        self._RoleInAppeal = None

    @property
    def AvatarInAppeal(self):
        r"""头像是否在申诉中
        :rtype: bool
        """
        return self._AvatarInAppeal

    @AvatarInAppeal.setter
    def AvatarInAppeal(self, AvatarInAppeal):
        self._AvatarInAppeal = AvatarInAppeal

    @property
    def FallbackReplyInAppeal(self):
        r"""兜底回复语是否在申诉中
        :rtype: bool
        """
        return self._FallbackReplyInAppeal

    @FallbackReplyInAppeal.setter
    def FallbackReplyInAppeal(self, FallbackReplyInAppeal):
        self._FallbackReplyInAppeal = FallbackReplyInAppeal

    @property
    def GreetingInAppeal(self):
        r"""欢迎语是否在申诉中
        :rtype: bool
        """
        return self._GreetingInAppeal

    @GreetingInAppeal.setter
    def GreetingInAppeal(self, GreetingInAppeal):
        self._GreetingInAppeal = GreetingInAppeal

    @property
    def NameInAppeal(self):
        r"""应用名称是否在申诉中
        :rtype: bool
        """
        return self._NameInAppeal

    @NameInAppeal.setter
    def NameInAppeal(self, NameInAppeal):
        self._NameInAppeal = NameInAppeal

    @property
    def RoleInAppeal(self):
        r"""角色描述是否在申诉中
        :rtype: bool
        """
        return self._RoleInAppeal

    @RoleInAppeal.setter
    def RoleInAppeal(self, RoleInAppeal):
        self._RoleInAppeal = RoleInAppeal


    def _deserialize(self, params):
        self._AvatarInAppeal = params.get("AvatarInAppeal")
        self._FallbackReplyInAppeal = params.get("FallbackReplyInAppeal")
        self._GreetingInAppeal = params.get("GreetingInAppeal")
        self._NameInAppeal = params.get("NameInAppeal")
        self._RoleInAppeal = params.get("RoleInAppeal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    r"""操作日志

    """

    def __init__(self):
        r"""
        :param _AccountInfo: <p>员工信息</p>
        :type AccountInfo: :class:`tencentcloud.adp.v20260520.models.AccountInfo`
        :param _AppId: <p>应用业务id</p>
        :type AppId: str
        :param _AppName: <p>应用名称</p><p>操作日志触发时的名称</p>
        :type AppName: str
        :param _OperateTime: <p>操作时间</p><p>参数格式：秒时间戳</p>
        :type OperateTime: str
        :param _Action: <p>操作类型</p>
        :type Action: str
        :param _Biz: <p>操作对象</p>
        :type Biz: str
        :param _Content: <p>操作内容</p>
        :type Content: str
        :param _UniqueId: <p>操作唯一ID</p>
        :type UniqueId: str
        """
        self._AccountInfo = None
        self._AppId = None
        self._AppName = None
        self._OperateTime = None
        self._Action = None
        self._Biz = None
        self._Content = None
        self._UniqueId = None

    @property
    def AccountInfo(self):
        r"""<p>员工信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AccountInfo`
        """
        return self._AccountInfo

    @AccountInfo.setter
    def AccountInfo(self, AccountInfo):
        self._AccountInfo = AccountInfo

    @property
    def AppId(self):
        r"""<p>应用业务id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppName(self):
        r"""<p>应用名称</p><p>操作日志触发时的名称</p>
        :rtype: str
        """
        return self._AppName

    @AppName.setter
    def AppName(self, AppName):
        self._AppName = AppName

    @property
    def OperateTime(self):
        r"""<p>操作时间</p><p>参数格式：秒时间戳</p>
        :rtype: str
        """
        return self._OperateTime

    @OperateTime.setter
    def OperateTime(self, OperateTime):
        self._OperateTime = OperateTime

    @property
    def Action(self):
        r"""<p>操作类型</p>
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Biz(self):
        r"""<p>操作对象</p>
        :rtype: str
        """
        return self._Biz

    @Biz.setter
    def Biz(self, Biz):
        self._Biz = Biz

    @property
    def Content(self):
        r"""<p>操作内容</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def UniqueId(self):
        r"""<p>操作唯一ID</p>
        :rtype: str
        """
        return self._UniqueId

    @UniqueId.setter
    def UniqueId(self, UniqueId):
        self._UniqueId = UniqueId


    def _deserialize(self, params):
        if params.get("AccountInfo") is not None:
            self._AccountInfo = AccountInfo()
            self._AccountInfo._deserialize(params.get("AccountInfo"))
        self._AppId = params.get("AppId")
        self._AppName = params.get("AppName")
        self._OperateTime = params.get("OperateTime")
        self._Action = params.get("Action")
        self._Biz = params.get("Biz")
        self._Content = params.get("Content")
        self._UniqueId = params.get("UniqueId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogMetaField(AbstractModel):
    r"""操作日志元数据

    """

    def __init__(self):
        r"""
        :param _Key: <p>操作日志元数据key</p>
        :type Key: str
        :param _Name: <p>操作日志元数据Name</p>
        :type Name: str
        """
        self._Key = None
        self._Name = None

    @property
    def Key(self):
        r"""<p>操作日志元数据key</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        r"""<p>操作日志元数据Name</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthConfig(AbstractModel):
    r"""插件授权配置

    """

    def __init__(self):
        r"""
        :param _AuthType: <p>授权方式。</p><p>枚举值：</p><ul><li>0：无鉴权</li><li>1：API Key 鉴权</li><li>2：CAM 授权</li><li>3：OAuth 2.0 授权</li></ul>
        :type AuthType: int
        :param _ApiKeyAuthConfig: API Key授权配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiKeyAuthConfig: :class:`tencentcloud.adp.v20260520.models.ApiKeyAuthConfig`
        :param _CamAuthConfig: CAM授权配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CamAuthConfig: :class:`tencentcloud.adp.v20260520.models.CamAuthConfig`
        :param _OAuthConfig: OAuth2.0授权配置
注意：此字段可能返回 null，表示取不到有效值。
        :type OAuthConfig: :class:`tencentcloud.adp.v20260520.models.OAuthConfig`
        """
        self._AuthType = None
        self._ApiKeyAuthConfig = None
        self._CamAuthConfig = None
        self._OAuthConfig = None

    @property
    def AuthType(self):
        r"""<p>授权方式。</p><p>枚举值：</p><ul><li>0：无鉴权</li><li>1：API Key 鉴权</li><li>2：CAM 授权</li><li>3：OAuth 2.0 授权</li></ul>
        :rtype: int
        """
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiKeyAuthConfig(self):
        r"""API Key授权配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ApiKeyAuthConfig`
        """
        return self._ApiKeyAuthConfig

    @ApiKeyAuthConfig.setter
    def ApiKeyAuthConfig(self, ApiKeyAuthConfig):
        self._ApiKeyAuthConfig = ApiKeyAuthConfig

    @property
    def CamAuthConfig(self):
        r"""CAM授权配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.CamAuthConfig`
        """
        return self._CamAuthConfig

    @CamAuthConfig.setter
    def CamAuthConfig(self, CamAuthConfig):
        self._CamAuthConfig = CamAuthConfig

    @property
    def OAuthConfig(self):
        r"""OAuth2.0授权配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.OAuthConfig`
        """
        return self._OAuthConfig

    @OAuthConfig.setter
    def OAuthConfig(self, OAuthConfig):
        self._OAuthConfig = OAuthConfig


    def _deserialize(self, params):
        self._AuthType = params.get("AuthType")
        if params.get("ApiKeyAuthConfig") is not None:
            self._ApiKeyAuthConfig = ApiKeyAuthConfig()
            self._ApiKeyAuthConfig._deserialize(params.get("ApiKeyAuthConfig"))
        if params.get("CamAuthConfig") is not None:
            self._CamAuthConfig = CamAuthConfig()
            self._CamAuthConfig._deserialize(params.get("CamAuthConfig"))
        if params.get("OAuthConfig") is not None:
            self._OAuthConfig = OAuthConfig()
            self._OAuthConfig._deserialize(params.get("OAuthConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackgroundImage(AbstractModel):
    r"""BackgroundImage 背景图片配置

    """

    def __init__(self):
        r"""
        :param _Brightness: 亮度值
        :type Brightness: int
        :param _LandscapeImageUrl: 横图(pc)
        :type LandscapeImageUrl: str
        :param _OriginalImageUrl: 原始图
        :type OriginalImageUrl: str
        :param _PortraitImageUrl: 长图(手机)
        :type PortraitImageUrl: str
        :param _ThemeColor: 主题色
        :type ThemeColor: str
        """
        self._Brightness = None
        self._LandscapeImageUrl = None
        self._OriginalImageUrl = None
        self._PortraitImageUrl = None
        self._ThemeColor = None

    @property
    def Brightness(self):
        r"""亮度值
        :rtype: int
        """
        return self._Brightness

    @Brightness.setter
    def Brightness(self, Brightness):
        self._Brightness = Brightness

    @property
    def LandscapeImageUrl(self):
        r"""横图(pc)
        :rtype: str
        """
        return self._LandscapeImageUrl

    @LandscapeImageUrl.setter
    def LandscapeImageUrl(self, LandscapeImageUrl):
        self._LandscapeImageUrl = LandscapeImageUrl

    @property
    def OriginalImageUrl(self):
        r"""原始图
        :rtype: str
        """
        return self._OriginalImageUrl

    @OriginalImageUrl.setter
    def OriginalImageUrl(self, OriginalImageUrl):
        self._OriginalImageUrl = OriginalImageUrl

    @property
    def PortraitImageUrl(self):
        r"""长图(手机)
        :rtype: str
        """
        return self._PortraitImageUrl

    @PortraitImageUrl.setter
    def PortraitImageUrl(self, PortraitImageUrl):
        self._PortraitImageUrl = PortraitImageUrl

    @property
    def ThemeColor(self):
        r"""主题色
        :rtype: str
        """
        return self._ThemeColor

    @ThemeColor.setter
    def ThemeColor(self, ThemeColor):
        self._ThemeColor = ThemeColor


    def _deserialize(self, params):
        self._Brightness = params.get("Brightness")
        self._LandscapeImageUrl = params.get("LandscapeImageUrl")
        self._OriginalImageUrl = params.get("OriginalImageUrl")
        self._PortraitImageUrl = params.get("PortraitImageUrl")
        self._ThemeColor = params.get("ThemeColor")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BasicBilling(AbstractModel):
    r"""BasicBilling

    """

    def __init__(self):
        r"""
        :param _BillingUnit: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>UNKNOW</td><td>0</td><td></td></tr><tr><td>TOKEN</td><td>1</td><td>按token</td></tr><tr><td>PAGE_COUNT</td><td>2</td><td>按页数</td></tr><tr><td>TIMES</td><td>3</td><td>按次数</td></tr><tr><td>TIMES_THOUSAND</td><td>4</td><td>按千次数</td></tr><tr><td>SECOND</td><td>5</td><td>按时长</td></tr><tr><td>CHARACTER</td><td>6</td><td>按字符数</td></tr><tr><td>CHARACTER_THOUSAND</td><td>7</td><td>按千字符数</td></tr><tr><td>SHEET</td><td>8</td><td>按张</td></tr><tr><td>NUMBER</td><td>9</td><td>按个数</td></tr></tbody></table>
        :type BillingUnit: int
        :param _CashPrice: <p>现金价格</p><p>单位：元</p>
        :type CashPrice: float
        :param _PuPrice: <p>PU价格</p><p>单位：pu</p>
        :type PuPrice: float
        """
        self._BillingUnit = None
        self._CashPrice = None
        self._PuPrice = None

    @property
    def BillingUnit(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>UNKNOW</td><td>0</td><td></td></tr><tr><td>TOKEN</td><td>1</td><td>按token</td></tr><tr><td>PAGE_COUNT</td><td>2</td><td>按页数</td></tr><tr><td>TIMES</td><td>3</td><td>按次数</td></tr><tr><td>TIMES_THOUSAND</td><td>4</td><td>按千次数</td></tr><tr><td>SECOND</td><td>5</td><td>按时长</td></tr><tr><td>CHARACTER</td><td>6</td><td>按字符数</td></tr><tr><td>CHARACTER_THOUSAND</td><td>7</td><td>按千字符数</td></tr><tr><td>SHEET</td><td>8</td><td>按张</td></tr><tr><td>NUMBER</td><td>9</td><td>按个数</td></tr></tbody></table>
        :rtype: int
        """
        return self._BillingUnit

    @BillingUnit.setter
    def BillingUnit(self, BillingUnit):
        self._BillingUnit = BillingUnit

    @property
    def CashPrice(self):
        r"""<p>现金价格</p><p>单位：元</p>
        :rtype: float
        """
        return self._CashPrice

    @CashPrice.setter
    def CashPrice(self, CashPrice):
        self._CashPrice = CashPrice

    @property
    def PuPrice(self):
        r"""<p>PU价格</p><p>单位：pu</p>
        :rtype: float
        """
        return self._PuPrice

    @PuPrice.setter
    def PuPrice(self, PuPrice):
        self._PuPrice = PuPrice


    def _deserialize(self, params):
        self._BillingUnit = params.get("BillingUnit")
        self._CashPrice = params.get("CashPrice")
        self._PuPrice = params.get("PuPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingAttribute(AbstractModel):
    r"""BillingAttribute

    """

    def __init__(self):
        r"""
        :param _Name: <p>属性名称</p>
        :type Name: str
        :param _Value: <p>属性值</p>
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""<p>属性名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""<p>属性值</p>
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
        


class CallSource(AbstractModel):
    r"""调用来源

    """

    def __init__(self):
        r"""
        :param _SubjectId: <p>调用主体 ID，含义由 subject_type 决定（如 app_id、kb_id 等）</p>
        :type SubjectId: str
        :param _SubjectName: <p>调用主体名称</p>
        :type SubjectName: str
        :param _SubjectType: <p>调用主体类型：APP/KB/WIDGET/OPEN_CLAW/KB_RECALL_TEST/WORKBENCH/MODEL_API</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>METRIC_SOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>METRIC_SOURCE_TYPE_APP</td><td>1</td><td>应用开发</td></tr><tr><td>METRIC_SOURCE_TYPE_KB</td><td>2</td><td>知识库</td></tr><tr><td>METRIC_SOURCE_TYPE_WIDGET</td><td>3</td><td>Widget</td></tr><tr><td>METRIC_SOURCE_TYPE_OPEN_CLAW</td><td>4</td><td>ClawPro</td></tr><tr><td>METRIC_SOURCE_TYPE_KB_RECALL_TEST</td><td>5</td><td>知识库召回测试</td></tr><tr><td>METRIC_SOURCE_TYPE_WORKBENCH</td><td>6</td><td>智能工作台</td></tr><tr><td>METRIC_SOURCE_TYPE_MODEL_API</td><td>7</td><td>模型 API 调用</td></tr></tbody></table>
        :type SubjectType: int
        """
        self._SubjectId = None
        self._SubjectName = None
        self._SubjectType = None

    @property
    def SubjectId(self):
        r"""<p>调用主体 ID，含义由 subject_type 决定（如 app_id、kb_id 等）</p>
        :rtype: str
        """
        return self._SubjectId

    @SubjectId.setter
    def SubjectId(self, SubjectId):
        self._SubjectId = SubjectId

    @property
    def SubjectName(self):
        r"""<p>调用主体名称</p>
        :rtype: str
        """
        return self._SubjectName

    @SubjectName.setter
    def SubjectName(self, SubjectName):
        self._SubjectName = SubjectName

    @property
    def SubjectType(self):
        r"""<p>调用主体类型：APP/KB/WIDGET/OPEN_CLAW/KB_RECALL_TEST/WORKBENCH/MODEL_API</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>METRIC_SOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>METRIC_SOURCE_TYPE_APP</td><td>1</td><td>应用开发</td></tr><tr><td>METRIC_SOURCE_TYPE_KB</td><td>2</td><td>知识库</td></tr><tr><td>METRIC_SOURCE_TYPE_WIDGET</td><td>3</td><td>Widget</td></tr><tr><td>METRIC_SOURCE_TYPE_OPEN_CLAW</td><td>4</td><td>ClawPro</td></tr><tr><td>METRIC_SOURCE_TYPE_KB_RECALL_TEST</td><td>5</td><td>知识库召回测试</td></tr><tr><td>METRIC_SOURCE_TYPE_WORKBENCH</td><td>6</td><td>智能工作台</td></tr><tr><td>METRIC_SOURCE_TYPE_MODEL_API</td><td>7</td><td>模型 API 调用</td></tr></tbody></table>
        :rtype: int
        """
        return self._SubjectType

    @SubjectType.setter
    def SubjectType(self, SubjectType):
        self._SubjectType = SubjectType


    def _deserialize(self, params):
        self._SubjectId = params.get("SubjectId")
        self._SubjectName = params.get("SubjectName")
        self._SubjectType = params.get("SubjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CamAuthConfig(AbstractModel):
    r"""CAM授权信息

    """

    def __init__(self):
        r"""
        :param _RoleName: 角色名称
        :type RoleName: str
        :param _KeyLocation: 密钥位置 HEADER/QUERY

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 头鉴权 |
| 1 | 请求信息鉴权 |
        :type KeyLocation: int
        :param _SecretIdName: SecretId字段名称
        :type SecretIdName: str
        :param _SecretKeyName: SecretKey字段名称
        :type SecretKeyName: str
        """
        self._RoleName = None
        self._KeyLocation = None
        self._SecretIdName = None
        self._SecretKeyName = None

    @property
    def RoleName(self):
        r"""角色名称
        :rtype: str
        """
        return self._RoleName

    @RoleName.setter
    def RoleName(self, RoleName):
        self._RoleName = RoleName

    @property
    def KeyLocation(self):
        r"""密钥位置 HEADER/QUERY

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 头鉴权 |
| 1 | 请求信息鉴权 |
        :rtype: int
        """
        return self._KeyLocation

    @KeyLocation.setter
    def KeyLocation(self, KeyLocation):
        self._KeyLocation = KeyLocation

    @property
    def SecretIdName(self):
        r"""SecretId字段名称
        :rtype: str
        """
        return self._SecretIdName

    @SecretIdName.setter
    def SecretIdName(self, SecretIdName):
        self._SecretIdName = SecretIdName

    @property
    def SecretKeyName(self):
        r"""SecretKey字段名称
        :rtype: str
        """
        return self._SecretKeyName

    @SecretKeyName.setter
    def SecretKeyName(self, SecretKeyName):
        self._SecretKeyName = SecretKeyName


    def _deserialize(self, params):
        self._RoleName = params.get("RoleName")
        self._KeyLocation = params.get("KeyLocation")
        self._SecretIdName = params.get("SecretIdName")
        self._SecretKeyName = params.get("SecretKeyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CategoryPermission(AbstractModel):
    r"""CategoryPermission

    """

    def __init__(self):
        r"""
        :param _CanAdd: <p>当前用户是否可新增子分类</p>
        :type CanAdd: bool
        :param _CanDelete: <p>当前用户是否可删除该分类</p>
        :type CanDelete: bool
        :param _CanEdit: <p>当前用户是否可编辑该分类</p>
        :type CanEdit: bool
        """
        self._CanAdd = None
        self._CanDelete = None
        self._CanEdit = None

    @property
    def CanAdd(self):
        r"""<p>当前用户是否可新增子分类</p>
        :rtype: bool
        """
        return self._CanAdd

    @CanAdd.setter
    def CanAdd(self, CanAdd):
        self._CanAdd = CanAdd

    @property
    def CanDelete(self):
        r"""<p>当前用户是否可删除该分类</p>
        :rtype: bool
        """
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def CanEdit(self):
        r"""<p>当前用户是否可编辑该分类</p>
        :rtype: bool
        """
        return self._CanEdit

    @CanEdit.setter
    def CanEdit(self, CanEdit):
        self._CanEdit = CanEdit


    def _deserialize(self, params):
        self._CanAdd = params.get("CanAdd")
        self._CanDelete = params.get("CanDelete")
        self._CanEdit = params.get("CanEdit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClawAgentAgentTeamConfig(AbstractModel):
    r"""ClawAgent Agent团队协作配置

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>是否开启Agent团队协作</p>
        :type Enabled: bool
        :param _PromptContent: <p>prompt内容</p>
        :type PromptContent: str
        """
        self._Enabled = None
        self._PromptContent = None

    @property
    def Enabled(self):
        r"""<p>是否开启Agent团队协作</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def PromptContent(self):
        r"""<p>prompt内容</p>
        :rtype: str
        """
        return self._PromptContent

    @PromptContent.setter
    def PromptContent(self, PromptContent):
        self._PromptContent = PromptContent


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._PromptContent = params.get("PromptContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClawAgentConfig(AbstractModel):
    r"""ClawAgent配置

    """

    def __init__(self):
        r"""
        :param _AgentTeamConfig: Agent团队协作配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentTeamConfig: :class:`tencentcloud.adp.v20260520.models.ClawAgentAgentTeamConfig`
        :param _LongMemoryConfig: 长期记忆配置
注意：此字段可能返回 null，表示取不到有效值。
        :type LongMemoryConfig: :class:`tencentcloud.adp.v20260520.models.ClawAgentLongMemoryConfig`
        """
        self._AgentTeamConfig = None
        self._LongMemoryConfig = None

    @property
    def AgentTeamConfig(self):
        r"""Agent团队协作配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ClawAgentAgentTeamConfig`
        """
        return self._AgentTeamConfig

    @AgentTeamConfig.setter
    def AgentTeamConfig(self, AgentTeamConfig):
        self._AgentTeamConfig = AgentTeamConfig

    @property
    def LongMemoryConfig(self):
        r"""长期记忆配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ClawAgentLongMemoryConfig`
        """
        return self._LongMemoryConfig

    @LongMemoryConfig.setter
    def LongMemoryConfig(self, LongMemoryConfig):
        self._LongMemoryConfig = LongMemoryConfig


    def _deserialize(self, params):
        if params.get("AgentTeamConfig") is not None:
            self._AgentTeamConfig = ClawAgentAgentTeamConfig()
            self._AgentTeamConfig._deserialize(params.get("AgentTeamConfig"))
        if params.get("LongMemoryConfig") is not None:
            self._LongMemoryConfig = ClawAgentLongMemoryConfig()
            self._LongMemoryConfig._deserialize(params.get("LongMemoryConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClawAgentLongMemoryConfig(AbstractModel):
    r"""ClawAgent长期记忆配置

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>是否开启长期记忆</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>是否开启长期记忆</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CodeToolConfig(AbstractModel):
    r"""CodeToolConfig

    """

    def __init__(self):
        r"""
        :param _Code: <p>代码</p>
        :type Code: str
        :param _Example: <p>示例</p>
        :type Example: :class:`tencentcloud.adp.v20260520.models.ToolExample`
        :param _Inputs: <p>输入参数</p>
        :type Inputs: list of RequestParam
        :param _Outputs: <p>输出参数</p>
        :type Outputs: list of ResponseParam
        """
        self._Code = None
        self._Example = None
        self._Inputs = None
        self._Outputs = None

    @property
    def Code(self):
        r"""<p>代码</p>
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Example(self):
        r"""<p>示例</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ToolExample`
        """
        return self._Example

    @Example.setter
    def Example(self, Example):
        self._Example = Example

    @property
    def Inputs(self):
        r"""<p>输入参数</p>
        :rtype: list of RequestParam
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Outputs(self):
        r"""<p>输出参数</p>
        :rtype: list of ResponseParam
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs


    def _deserialize(self, params):
        self._Code = params.get("Code")
        if params.get("Example") is not None:
            self._Example = ToolExample()
            self._Example._deserialize(params.get("Example"))
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Inputs.append(obj)
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = ResponseParam()
                obj._deserialize(item)
                self._Outputs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplexBilling(AbstractModel):
    r"""ComplexBilling

    """

    def __init__(self):
        r"""
        :param _ComplexList: <p>复合计费列表</p>
        :type ComplexList: list of ComplexBillingItem
        """
        self._ComplexList = None

    @property
    def ComplexList(self):
        r"""<p>复合计费列表</p>
        :rtype: list of ComplexBillingItem
        """
        return self._ComplexList

    @ComplexList.setter
    def ComplexList(self, ComplexList):
        self._ComplexList = ComplexList


    def _deserialize(self, params):
        if params.get("ComplexList") is not None:
            self._ComplexList = []
            for item in params.get("ComplexList"):
                obj = ComplexBillingItem()
                obj._deserialize(item)
                self._ComplexList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComplexBillingItem(AbstractModel):
    r"""ComplexBillingItem

    """

    def __init__(self):
        r"""
        :param _BillingAttributeList: <p>复合计费维度信息</p>
        :type BillingAttributeList: list of BillingAttribute
        :param _BillingUnit: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>UNKNOW</td><td>0</td><td></td></tr><tr><td>TOKEN</td><td>1</td><td>按token</td></tr><tr><td>PAGE_COUNT</td><td>2</td><td>按页数</td></tr><tr><td>TIMES</td><td>3</td><td>按次数</td></tr><tr><td>TIMES_THOUSAND</td><td>4</td><td>按千次数</td></tr><tr><td>SECOND</td><td>5</td><td>按时长</td></tr><tr><td>CHARACTER</td><td>6</td><td>按字符数</td></tr><tr><td>CHARACTER_THOUSAND</td><td>7</td><td>按千字符数</td></tr><tr><td>SHEET</td><td>8</td><td>按张</td></tr><tr><td>NUMBER</td><td>9</td><td>按个数</td></tr></tbody></table>
        :type BillingUnit: int
        :param _CashPrice: <p>现金价格</p><p>单位：元</p>
        :type CashPrice: float
        :param _PuPrice: <p>pu价格</p><p>单位：pu</p>
        :type PuPrice: float
        """
        self._BillingAttributeList = None
        self._BillingUnit = None
        self._CashPrice = None
        self._PuPrice = None

    @property
    def BillingAttributeList(self):
        r"""<p>复合计费维度信息</p>
        :rtype: list of BillingAttribute
        """
        return self._BillingAttributeList

    @BillingAttributeList.setter
    def BillingAttributeList(self, BillingAttributeList):
        self._BillingAttributeList = BillingAttributeList

    @property
    def BillingUnit(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>UNKNOW</td><td>0</td><td></td></tr><tr><td>TOKEN</td><td>1</td><td>按token</td></tr><tr><td>PAGE_COUNT</td><td>2</td><td>按页数</td></tr><tr><td>TIMES</td><td>3</td><td>按次数</td></tr><tr><td>TIMES_THOUSAND</td><td>4</td><td>按千次数</td></tr><tr><td>SECOND</td><td>5</td><td>按时长</td></tr><tr><td>CHARACTER</td><td>6</td><td>按字符数</td></tr><tr><td>CHARACTER_THOUSAND</td><td>7</td><td>按千字符数</td></tr><tr><td>SHEET</td><td>8</td><td>按张</td></tr><tr><td>NUMBER</td><td>9</td><td>按个数</td></tr></tbody></table>
        :rtype: int
        """
        return self._BillingUnit

    @BillingUnit.setter
    def BillingUnit(self, BillingUnit):
        self._BillingUnit = BillingUnit

    @property
    def CashPrice(self):
        r"""<p>现金价格</p><p>单位：元</p>
        :rtype: float
        """
        return self._CashPrice

    @CashPrice.setter
    def CashPrice(self, CashPrice):
        self._CashPrice = CashPrice

    @property
    def PuPrice(self):
        r"""<p>pu价格</p><p>单位：pu</p>
        :rtype: float
        """
        return self._PuPrice

    @PuPrice.setter
    def PuPrice(self, PuPrice):
        self._PuPrice = PuPrice


    def _deserialize(self, params):
        if params.get("BillingAttributeList") is not None:
            self._BillingAttributeList = []
            for item in params.get("BillingAttributeList"):
                obj = BillingAttribute()
                obj._deserialize(item)
                self._BillingAttributeList.append(obj)
        self._BillingUnit = params.get("BillingUnit")
        self._CashPrice = params.get("CashPrice")
        self._PuPrice = params.get("PuPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConcurrencyLimitDetail(AbstractModel):
    r"""并发超限明细

    """

    def __init__(self):
        r"""
        :param _CallSource: <p>调用来源（subject_type 决定 subject_id/subject_name 的含义，如 APP 时 subject_id=app_id、subject_name=app_name）</p>
        :type CallSource: :class:`tencentcloud.adp.v20260520.models.CallSource`
        :param _EventTime: <p>超限发生时间（Unix秒）</p>
        :type EventTime: str
        :param _ModelName: <p>模型名称</p>
        :type ModelName: str
        :param _RequestQuery: <p>请求内容（用户请求的原始查询文本）</p>
        :type RequestQuery: str
        :param _SpaceId: <p>空间 ID</p>
        :type SpaceId: str
        """
        self._CallSource = None
        self._EventTime = None
        self._ModelName = None
        self._RequestQuery = None
        self._SpaceId = None

    @property
    def CallSource(self):
        r"""<p>调用来源（subject_type 决定 subject_id/subject_name 的含义，如 APP 时 subject_id=app_id、subject_name=app_name）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.CallSource`
        """
        return self._CallSource

    @CallSource.setter
    def CallSource(self, CallSource):
        self._CallSource = CallSource

    @property
    def EventTime(self):
        r"""<p>超限发生时间（Unix秒）</p>
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def ModelName(self):
        r"""<p>模型名称</p>
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def RequestQuery(self):
        r"""<p>请求内容（用户请求的原始查询文本）</p>
        :rtype: str
        """
        return self._RequestQuery

    @RequestQuery.setter
    def RequestQuery(self, RequestQuery):
        self._RequestQuery = RequestQuery

    @property
    def SpaceId(self):
        r"""<p>空间 ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        if params.get("CallSource") is not None:
            self._CallSource = CallSource()
            self._CallSource._deserialize(params.get("CallSource"))
        self._EventTime = params.get("EventTime")
        self._ModelName = params.get("ModelName")
        self._RequestQuery = params.get("RequestQuery")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionClassification(AbstractModel):
    r"""消耗分类

    """

    def __init__(self):
        r"""
        :param _ConsumptionScene: <p>消耗场景（如推理/训练/评测等）</p>
        :type ConsumptionScene: str
        :param _ConsumptionTarget: <p>消耗目标（如具体模型名/插件名/平台功能名）</p>
        :type ConsumptionTarget: str
        :param _ConsumptionType: <p>消耗类型，取值集合由业务方定义（如 model/plugin/platform 等）</p>
        :type ConsumptionType: str
        :param _PackageName: <p>套餐包名称</p>
        :type PackageName: str
        """
        self._ConsumptionScene = None
        self._ConsumptionTarget = None
        self._ConsumptionType = None
        self._PackageName = None

    @property
    def ConsumptionScene(self):
        r"""<p>消耗场景（如推理/训练/评测等）</p>
        :rtype: str
        """
        return self._ConsumptionScene

    @ConsumptionScene.setter
    def ConsumptionScene(self, ConsumptionScene):
        self._ConsumptionScene = ConsumptionScene

    @property
    def ConsumptionTarget(self):
        r"""<p>消耗目标（如具体模型名/插件名/平台功能名）</p>
        :rtype: str
        """
        return self._ConsumptionTarget

    @ConsumptionTarget.setter
    def ConsumptionTarget(self, ConsumptionTarget):
        self._ConsumptionTarget = ConsumptionTarget

    @property
    def ConsumptionType(self):
        r"""<p>消耗类型，取值集合由业务方定义（如 model/plugin/platform 等）</p>
        :rtype: str
        """
        return self._ConsumptionType

    @ConsumptionType.setter
    def ConsumptionType(self, ConsumptionType):
        self._ConsumptionType = ConsumptionType

    @property
    def PackageName(self):
        r"""<p>套餐包名称</p>
        :rtype: str
        """
        return self._PackageName

    @PackageName.setter
    def PackageName(self, PackageName):
        self._PackageName = PackageName


    def _deserialize(self, params):
        self._ConsumptionScene = params.get("ConsumptionScene")
        self._ConsumptionTarget = params.get("ConsumptionTarget")
        self._ConsumptionType = params.get("ConsumptionType")
        self._PackageName = params.get("PackageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionDetail(AbstractModel):
    r"""资源消耗明细

    """

    def __init__(self):
        r"""
        :param _Classification: <p>消耗分类（类型/目标/场景/套餐包）</p>
        :type Classification: :class:`tencentcloud.adp.v20260520.models.ConsumptionClassification`
        :param _EventTime: <p>消耗发生时间，Unix 秒</p>
        :type EventTime: str
        :param _MetricSourceType: <p>用量来源类型</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>METRIC_SOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>METRIC_SOURCE_TYPE_APP</td><td>1</td><td>应用开发</td></tr><tr><td>METRIC_SOURCE_TYPE_KB</td><td>2</td><td>知识库</td></tr><tr><td>METRIC_SOURCE_TYPE_WIDGET</td><td>3</td><td>Widget</td></tr><tr><td>METRIC_SOURCE_TYPE_OPEN_CLAW</td><td>4</td><td>ClawPro</td></tr><tr><td>METRIC_SOURCE_TYPE_KB_RECALL_TEST</td><td>5</td><td>知识库召回测试</td></tr><tr><td>METRIC_SOURCE_TYPE_WORKBENCH</td><td>6</td><td>智能工作台</td></tr><tr><td>METRIC_SOURCE_TYPE_MODEL_API</td><td>7</td><td>模型 API 调用</td></tr></tbody></table>
        :type MetricSourceType: int
        :param _Name: <p>名称</p>
        :type Name: str
        :param _SpaceName: <p>空间名称</p>
        :type SpaceName: str
        :param _Usage: <p>消耗用量（数值/单位/PU 消耗）</p>
        :type Usage: :class:`tencentcloud.adp.v20260520.models.ConsumptionUsage`
        :param _UserName: <p>用户名称</p>
        :type UserName: str
        """
        self._Classification = None
        self._EventTime = None
        self._MetricSourceType = None
        self._Name = None
        self._SpaceName = None
        self._Usage = None
        self._UserName = None

    @property
    def Classification(self):
        r"""<p>消耗分类（类型/目标/场景/套餐包）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConsumptionClassification`
        """
        return self._Classification

    @Classification.setter
    def Classification(self, Classification):
        self._Classification = Classification

    @property
    def EventTime(self):
        r"""<p>消耗发生时间，Unix 秒</p>
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def MetricSourceType(self):
        r"""<p>用量来源类型</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>METRIC_SOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>METRIC_SOURCE_TYPE_APP</td><td>1</td><td>应用开发</td></tr><tr><td>METRIC_SOURCE_TYPE_KB</td><td>2</td><td>知识库</td></tr><tr><td>METRIC_SOURCE_TYPE_WIDGET</td><td>3</td><td>Widget</td></tr><tr><td>METRIC_SOURCE_TYPE_OPEN_CLAW</td><td>4</td><td>ClawPro</td></tr><tr><td>METRIC_SOURCE_TYPE_KB_RECALL_TEST</td><td>5</td><td>知识库召回测试</td></tr><tr><td>METRIC_SOURCE_TYPE_WORKBENCH</td><td>6</td><td>智能工作台</td></tr><tr><td>METRIC_SOURCE_TYPE_MODEL_API</td><td>7</td><td>模型 API 调用</td></tr></tbody></table>
        :rtype: int
        """
        return self._MetricSourceType

    @MetricSourceType.setter
    def MetricSourceType(self, MetricSourceType):
        self._MetricSourceType = MetricSourceType

    @property
    def Name(self):
        r"""<p>名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SpaceName(self):
        r"""<p>空间名称</p>
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def Usage(self):
        r"""<p>消耗用量（数值/单位/PU 消耗）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConsumptionUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def UserName(self):
        r"""<p>用户名称</p>
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName


    def _deserialize(self, params):
        if params.get("Classification") is not None:
            self._Classification = ConsumptionClassification()
            self._Classification._deserialize(params.get("Classification"))
        self._EventTime = params.get("EventTime")
        self._MetricSourceType = params.get("MetricSourceType")
        self._Name = params.get("Name")
        self._SpaceName = params.get("SpaceName")
        if params.get("Usage") is not None:
            self._Usage = ConsumptionUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConsumptionUsage(AbstractModel):
    r"""消耗用量

    """

    def __init__(self):
        r"""
        :param _ConsumptionPU: <p>消耗PU</p>
        :type ConsumptionPU: float
        :param _Usage: <p>用量数值</p>
        :type Usage: float
        :param _UsageUnit: <p>用量单位，枚举值 DosageUnit</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>DOSAGE_UNIT_TOKEN</td><td>0</td><td>token（默认）</td></tr><tr><td>DOSAGE_UNIT_PAGE_COUNT</td><td>1</td><td>page_count（页数）</td></tr><tr><td>DOSAGE_UNIT_TIMES</td><td>2</td><td>times（次数）</td></tr><tr><td>DOSAGE_UNIT_SECOND</td><td>3</td><td>second（秒）</td></tr><tr><td>DOSAGE_UNIT_ITEM</td><td>4</td><td>item（条）</td></tr><tr><td>DOSAGE_UNIT_SHEET</td><td>5</td><td>sheet（张）</td></tr><tr><td>DOSAGE_UNIT_CHARACTER</td><td>6</td><td>character（字符）</td></tr><tr><td>DOSAGE_UNIT_GB</td><td>7</td><td>GB</td></tr><tr><td>DOSAGE_UNIT_NUMBER</td><td>8</td><td>number（个数）</td></tr><tr><td>DOSAGE_UNIT_MILL_SECOND</td><td>9</td><td>mill_second（毫秒）</td></tr></tbody></table>
        :type UsageUnit: int
        """
        self._ConsumptionPU = None
        self._Usage = None
        self._UsageUnit = None

    @property
    def ConsumptionPU(self):
        r"""<p>消耗PU</p>
        :rtype: float
        """
        return self._ConsumptionPU

    @ConsumptionPU.setter
    def ConsumptionPU(self, ConsumptionPU):
        self._ConsumptionPU = ConsumptionPU

    @property
    def Usage(self):
        r"""<p>用量数值</p>
        :rtype: float
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def UsageUnit(self):
        r"""<p>用量单位，枚举值 DosageUnit</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>DOSAGE_UNIT_TOKEN</td><td>0</td><td>token（默认）</td></tr><tr><td>DOSAGE_UNIT_PAGE_COUNT</td><td>1</td><td>page_count（页数）</td></tr><tr><td>DOSAGE_UNIT_TIMES</td><td>2</td><td>times（次数）</td></tr><tr><td>DOSAGE_UNIT_SECOND</td><td>3</td><td>second（秒）</td></tr><tr><td>DOSAGE_UNIT_ITEM</td><td>4</td><td>item（条）</td></tr><tr><td>DOSAGE_UNIT_SHEET</td><td>5</td><td>sheet（张）</td></tr><tr><td>DOSAGE_UNIT_CHARACTER</td><td>6</td><td>character（字符）</td></tr><tr><td>DOSAGE_UNIT_GB</td><td>7</td><td>GB</td></tr><tr><td>DOSAGE_UNIT_NUMBER</td><td>8</td><td>number（个数）</td></tr><tr><td>DOSAGE_UNIT_MILL_SECOND</td><td>9</td><td>mill_second（毫秒）</td></tr></tbody></table>
        :rtype: int
        """
        return self._UsageUnit

    @UsageUnit.setter
    def UsageUnit(self, UsageUnit):
        self._UsageUnit = UsageUnit


    def _deserialize(self, params):
        self._ConsumptionPU = params.get("ConsumptionPU")
        self._Usage = params.get("Usage")
        self._UsageUnit = params.get("UsageUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Conversation(AbstractModel):
    r"""Conversation 会话信息

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _UpdateTime: <p>更新时间</p>
        :type UpdateTime: str
        :param _Title: <p>会话标题</p>
        :type Title: str
        :param _AgentId: <p>会话使用的用户端 AgentId</p>
        :type AgentId: str
        """
        self._AppId = None
        self._ConversationId = None
        self._CreateTime = None
        self._Type = None
        self._UpdateTime = None
        self._Title = None
        self._AgentId = None

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Title(self):
        r"""<p>会话标题</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def AgentId(self):
        r"""<p>会话使用的用户端 AgentId</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ConversationId = params.get("ConversationId")
        self._CreateTime = params.get("CreateTime")
        self._Type = params.get("Type")
        self._UpdateTime = params.get("UpdateTime")
        self._Title = params.get("Title")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationAgentTask(AbstractModel):
    r"""AgentTask 智能体任务信息

    """

    def __init__(self):
        r"""
        :param _Content: <p>任务内容</p>
        :type Content: str
        :param _Index: <p>任务序号</p>
        :type Index: str
        :param _Status: <p>任务状态，pending:待执行，processing:处理中，success:已完成，failed:处理失败，stop:已取消</p>
        :type Status: str
        """
        self._Content = None
        self._Index = None
        self._Status = None

    @property
    def Content(self):
        r"""<p>任务内容</p>
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Index(self):
        r"""<p>任务序号</p>
        :rtype: str
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Status(self):
        r"""<p>任务状态，pending:待执行，processing:处理中，success:已完成，failed:处理失败，stop:已取消</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._Index = params.get("Index")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationContent(AbstractModel):
    r"""Content 消息内容信息

    """

    def __init__(self):
        r"""
        :param _Text: <p>文本内容</p>
        :type Text: str
        :param _Type: <p>内容类型, text：文本,image：图片,file：文件,custom_variables：自定义输入参数信息,widget_action：widget动作信息</p>
        :type Type: str
        :param _CustomParamList: <p>自定义参数数据</p>
        :type CustomParamList: list of str
        :param _CustomParams: <p>自定义参数数据</p>
        :type CustomParams: list of str
        :param _CustomVariablesData: <p>自定义变量数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomVariablesData: str
        :param _EnterpriseCharts: <p>企业表单</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseCharts: str
        :param _OptionCardList: <p>选项卡列表</p>
        :type OptionCardList: list of str
        :param _OptionCards: <p>选项卡列表</p>
        :type OptionCards: list of str
        :param _OptionMode: <p>选项卡模式 枚举值: 0-OPTION_MODE_SINGLE(单选), 1-OPTION_MODE_MULTI(多选)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OptionMode: int
        :param _QuoteInfoList: <p>引用角标信息列表</p>
        :type QuoteInfoList: list of ConversationQuoteInfo
        :param _QuoteInfos: <p>引用角标信息列表</p>
        :type QuoteInfos: list of ConversationQuoteInfo
        :param _ReferenceList: <p>参考来源列表</p>
        :type ReferenceList: list of ConversationReference
        :param _References: <p>参考来源列表</p>
        :type References: list of ConversationReference
        :param _RelatedRecordId: <p>关联记录 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RelatedRecordId: str
        :param _TaskList: <p>智能体任务列表</p>
        :type TaskList: list of ConversationAgentTask
        :param _Tasks: <p>智能体任务列表</p>
        :type Tasks: list of ConversationAgentTask
        :param _WorkflowInput: <p>工作流输入参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkflowInput: str
        :param _McpApp: <p>MCP-APP调用信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type McpApp: :class:`tencentcloud.adp.v20260520.models.ConversationMcpApp`
        """
        self._Text = None
        self._Type = None
        self._CustomParamList = None
        self._CustomParams = None
        self._CustomVariablesData = None
        self._EnterpriseCharts = None
        self._OptionCardList = None
        self._OptionCards = None
        self._OptionMode = None
        self._QuoteInfoList = None
        self._QuoteInfos = None
        self._ReferenceList = None
        self._References = None
        self._RelatedRecordId = None
        self._TaskList = None
        self._Tasks = None
        self._WorkflowInput = None
        self._McpApp = None

    @property
    def Text(self):
        r"""<p>文本内容</p>
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Type(self):
        r"""<p>内容类型, text：文本,image：图片,file：文件,custom_variables：自定义输入参数信息,widget_action：widget动作信息</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CustomParamList(self):
        r"""<p>自定义参数数据</p>
        :rtype: list of str
        """
        return self._CustomParamList

    @CustomParamList.setter
    def CustomParamList(self, CustomParamList):
        self._CustomParamList = CustomParamList

    @property
    def CustomParams(self):
        r"""<p>自定义参数数据</p>
        :rtype: list of str
        """
        return self._CustomParams

    @CustomParams.setter
    def CustomParams(self, CustomParams):
        self._CustomParams = CustomParams

    @property
    def CustomVariablesData(self):
        r"""<p>自定义变量数据</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomVariablesData

    @CustomVariablesData.setter
    def CustomVariablesData(self, CustomVariablesData):
        self._CustomVariablesData = CustomVariablesData

    @property
    def EnterpriseCharts(self):
        r"""<p>企业表单</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EnterpriseCharts

    @EnterpriseCharts.setter
    def EnterpriseCharts(self, EnterpriseCharts):
        self._EnterpriseCharts = EnterpriseCharts

    @property
    def OptionCardList(self):
        r"""<p>选项卡列表</p>
        :rtype: list of str
        """
        return self._OptionCardList

    @OptionCardList.setter
    def OptionCardList(self, OptionCardList):
        self._OptionCardList = OptionCardList

    @property
    def OptionCards(self):
        r"""<p>选项卡列表</p>
        :rtype: list of str
        """
        return self._OptionCards

    @OptionCards.setter
    def OptionCards(self, OptionCards):
        self._OptionCards = OptionCards

    @property
    def OptionMode(self):
        r"""<p>选项卡模式 枚举值: 0-OPTION_MODE_SINGLE(单选), 1-OPTION_MODE_MULTI(多选)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OptionMode

    @OptionMode.setter
    def OptionMode(self, OptionMode):
        self._OptionMode = OptionMode

    @property
    def QuoteInfoList(self):
        r"""<p>引用角标信息列表</p>
        :rtype: list of ConversationQuoteInfo
        """
        return self._QuoteInfoList

    @QuoteInfoList.setter
    def QuoteInfoList(self, QuoteInfoList):
        self._QuoteInfoList = QuoteInfoList

    @property
    def QuoteInfos(self):
        r"""<p>引用角标信息列表</p>
        :rtype: list of ConversationQuoteInfo
        """
        return self._QuoteInfos

    @QuoteInfos.setter
    def QuoteInfos(self, QuoteInfos):
        self._QuoteInfos = QuoteInfos

    @property
    def ReferenceList(self):
        r"""<p>参考来源列表</p>
        :rtype: list of ConversationReference
        """
        return self._ReferenceList

    @ReferenceList.setter
    def ReferenceList(self, ReferenceList):
        self._ReferenceList = ReferenceList

    @property
    def References(self):
        r"""<p>参考来源列表</p>
        :rtype: list of ConversationReference
        """
        return self._References

    @References.setter
    def References(self, References):
        self._References = References

    @property
    def RelatedRecordId(self):
        r"""<p>关联记录 ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RelatedRecordId

    @RelatedRecordId.setter
    def RelatedRecordId(self, RelatedRecordId):
        self._RelatedRecordId = RelatedRecordId

    @property
    def TaskList(self):
        r"""<p>智能体任务列表</p>
        :rtype: list of ConversationAgentTask
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def Tasks(self):
        r"""<p>智能体任务列表</p>
        :rtype: list of ConversationAgentTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

    @property
    def WorkflowInput(self):
        r"""<p>工作流输入参数</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WorkflowInput

    @WorkflowInput.setter
    def WorkflowInput(self, WorkflowInput):
        self._WorkflowInput = WorkflowInput

    @property
    def McpApp(self):
        r"""<p>MCP-APP调用信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationMcpApp`
        """
        return self._McpApp

    @McpApp.setter
    def McpApp(self, McpApp):
        self._McpApp = McpApp


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Type = params.get("Type")
        self._CustomParamList = params.get("CustomParamList")
        self._CustomParams = params.get("CustomParams")
        self._CustomVariablesData = params.get("CustomVariablesData")
        self._EnterpriseCharts = params.get("EnterpriseCharts")
        self._OptionCardList = params.get("OptionCardList")
        self._OptionCards = params.get("OptionCards")
        self._OptionMode = params.get("OptionMode")
        if params.get("QuoteInfoList") is not None:
            self._QuoteInfoList = []
            for item in params.get("QuoteInfoList"):
                obj = ConversationQuoteInfo()
                obj._deserialize(item)
                self._QuoteInfoList.append(obj)
        if params.get("QuoteInfos") is not None:
            self._QuoteInfos = []
            for item in params.get("QuoteInfos"):
                obj = ConversationQuoteInfo()
                obj._deserialize(item)
                self._QuoteInfos.append(obj)
        if params.get("ReferenceList") is not None:
            self._ReferenceList = []
            for item in params.get("ReferenceList"):
                obj = ConversationReference()
                obj._deserialize(item)
                self._ReferenceList.append(obj)
        if params.get("References") is not None:
            self._References = []
            for item in params.get("References"):
                obj = ConversationReference()
                obj._deserialize(item)
                self._References.append(obj)
        self._RelatedRecordId = params.get("RelatedRecordId")
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = ConversationAgentTask()
                obj._deserialize(item)
                self._TaskList.append(obj)
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = ConversationAgentTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._WorkflowInput = params.get("WorkflowInput")
        if params.get("McpApp") is not None:
            self._McpApp = ConversationMcpApp()
            self._McpApp._deserialize(params.get("McpApp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationExperience(AbstractModel):
    r"""对话体验配置

    """

    def __init__(self):
        r"""
        :param _AiCall: AI通话配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AiCall: :class:`tencentcloud.adp.v20260520.models.AICallConfig`
        :param _BackgroundImage: 背景图片配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BackgroundImage: :class:`tencentcloud.adp.v20260520.models.BackgroundImage`
        :param _EnableFallbackReply: 兜底回复开关
        :type EnableFallbackReply: bool
        :param _EnableRecommended: 是否使用推荐问
        :type EnableRecommended: bool
        :param _EnableWebSearch: 是否使用联网搜索
        :type EnableWebSearch: bool
        :param _FallbackReply: 兜底回复语
        :type FallbackReply: str
        :param _InputBoxConfig: 输入框配置
注意：此字段可能返回 null，表示取不到有效值。
        :type InputBoxConfig: :class:`tencentcloud.adp.v20260520.models.InputBoxConfig`
        :param _Method: 输出方式。枚举值: 1:流式, 2:非流式
        :type Method: int
        :param _RecommendPromptMode: 推荐问生成prompt模式。枚举值: 1:仅结合知识库输出推荐问的prompt
        :type RecommendPromptMode: int
        """
        self._AiCall = None
        self._BackgroundImage = None
        self._EnableFallbackReply = None
        self._EnableRecommended = None
        self._EnableWebSearch = None
        self._FallbackReply = None
        self._InputBoxConfig = None
        self._Method = None
        self._RecommendPromptMode = None

    @property
    def AiCall(self):
        r"""AI通话配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AICallConfig`
        """
        return self._AiCall

    @AiCall.setter
    def AiCall(self, AiCall):
        self._AiCall = AiCall

    @property
    def BackgroundImage(self):
        r"""背景图片配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.BackgroundImage`
        """
        return self._BackgroundImage

    @BackgroundImage.setter
    def BackgroundImage(self, BackgroundImage):
        self._BackgroundImage = BackgroundImage

    @property
    def EnableFallbackReply(self):
        r"""兜底回复开关
        :rtype: bool
        """
        return self._EnableFallbackReply

    @EnableFallbackReply.setter
    def EnableFallbackReply(self, EnableFallbackReply):
        self._EnableFallbackReply = EnableFallbackReply

    @property
    def EnableRecommended(self):
        r"""是否使用推荐问
        :rtype: bool
        """
        return self._EnableRecommended

    @EnableRecommended.setter
    def EnableRecommended(self, EnableRecommended):
        self._EnableRecommended = EnableRecommended

    @property
    def EnableWebSearch(self):
        r"""是否使用联网搜索
        :rtype: bool
        """
        return self._EnableWebSearch

    @EnableWebSearch.setter
    def EnableWebSearch(self, EnableWebSearch):
        self._EnableWebSearch = EnableWebSearch

    @property
    def FallbackReply(self):
        r"""兜底回复语
        :rtype: str
        """
        return self._FallbackReply

    @FallbackReply.setter
    def FallbackReply(self, FallbackReply):
        self._FallbackReply = FallbackReply

    @property
    def InputBoxConfig(self):
        r"""输入框配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.InputBoxConfig`
        """
        return self._InputBoxConfig

    @InputBoxConfig.setter
    def InputBoxConfig(self, InputBoxConfig):
        self._InputBoxConfig = InputBoxConfig

    @property
    def Method(self):
        r"""输出方式。枚举值: 1:流式, 2:非流式
        :rtype: int
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def RecommendPromptMode(self):
        r"""推荐问生成prompt模式。枚举值: 1:仅结合知识库输出推荐问的prompt
        :rtype: int
        """
        return self._RecommendPromptMode

    @RecommendPromptMode.setter
    def RecommendPromptMode(self, RecommendPromptMode):
        self._RecommendPromptMode = RecommendPromptMode


    def _deserialize(self, params):
        if params.get("AiCall") is not None:
            self._AiCall = AICallConfig()
            self._AiCall._deserialize(params.get("AiCall"))
        if params.get("BackgroundImage") is not None:
            self._BackgroundImage = BackgroundImage()
            self._BackgroundImage._deserialize(params.get("BackgroundImage"))
        self._EnableFallbackReply = params.get("EnableFallbackReply")
        self._EnableRecommended = params.get("EnableRecommended")
        self._EnableWebSearch = params.get("EnableWebSearch")
        self._FallbackReply = params.get("FallbackReply")
        if params.get("InputBoxConfig") is not None:
            self._InputBoxConfig = InputBoxConfig()
            self._InputBoxConfig._deserialize(params.get("InputBoxConfig"))
        self._Method = params.get("Method")
        self._RecommendPromptMode = params.get("RecommendPromptMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationMcpApp(AbstractModel):
    r"""MCP App 内容，供历史会话重建可交互 App

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>能力边界：一次请求只能读该 plugin 的资源</p>
        :type PluginId: str
        :param _ResourceUri: <p>ui:// 资源，前端据此调 ReadMCPResource 拉 HTML</p>
        :type ResourceUri: str
        :param _ThreadId: <p>agent-exec 侧 thread</p>
        :type ThreadId: str
        :param _ToolResult: <p>JSON：完整 CallToolResult 原文，供历史会话重建时重放</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolResult: str
        """
        self._PluginId = None
        self._ResourceUri = None
        self._ThreadId = None
        self._ToolResult = None

    @property
    def PluginId(self):
        r"""<p>能力边界：一次请求只能读该 plugin 的资源</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ResourceUri(self):
        r"""<p>ui:// 资源，前端据此调 ReadMCPResource 拉 HTML</p>
        :rtype: str
        """
        return self._ResourceUri

    @ResourceUri.setter
    def ResourceUri(self, ResourceUri):
        self._ResourceUri = ResourceUri

    @property
    def ThreadId(self):
        r"""<p>agent-exec 侧 thread</p>
        :rtype: str
        """
        return self._ThreadId

    @ThreadId.setter
    def ThreadId(self, ThreadId):
        self._ThreadId = ThreadId

    @property
    def ToolResult(self):
        r"""<p>JSON：完整 CallToolResult 原文，供历史会话重建时重放</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ToolResult

    @ToolResult.setter
    def ToolResult(self, ToolResult):
        self._ToolResult = ToolResult


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._ResourceUri = params.get("ResourceUri")
        self._ThreadId = params.get("ThreadId")
        self._ToolResult = params.get("ToolResult")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationMessage(AbstractModel):
    r"""Message 消息信息

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _Icon: <p>消息图标</p>
        :type Icon: str
        :param _MessageId: <p>消息 ID</p>
        :type MessageId: str
        :param _Name: <p>消息名称</p>
        :type Name: str
        :param _RecordId: <p>记录 ID</p>
        :type RecordId: str
        :param _Role: <p>消息角色</p>
        :type Role: str
        :param _Status: <p>消息状态，pending:待执行，processing:处理中，success:已完成，failed:处理失败，stop:已取消</p>
        :type Status: str
        :param _StatusDesc: <p>状态描述</p>
        :type StatusDesc: str
        :param _Title: <p>消息标题</p>
        :type Title: str
        :param _ContentList: <p>消息内容列表</p>
        :type ContentList: list of ConversationContent
        :param _Contents: <p>消息内容列表</p>
        :type Contents: list of ConversationContent
        :param _Type: <p>类型</p>
        :type Type: str
        """
        self._ConversationId = None
        self._Icon = None
        self._MessageId = None
        self._Name = None
        self._RecordId = None
        self._Role = None
        self._Status = None
        self._StatusDesc = None
        self._Title = None
        self._ContentList = None
        self._Contents = None
        self._Type = None

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def Icon(self):
        r"""<p>消息图标</p>
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def MessageId(self):
        r"""<p>消息 ID</p>
        :rtype: str
        """
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def Name(self):
        r"""<p>消息名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RecordId(self):
        r"""<p>记录 ID</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Role(self):
        r"""<p>消息角色</p>
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Status(self):
        r"""<p>消息状态，pending:待执行，processing:处理中，success:已完成，failed:处理失败，stop:已取消</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDesc(self):
        r"""<p>状态描述</p>
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc

    @property
    def Title(self):
        r"""<p>消息标题</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def ContentList(self):
        r"""<p>消息内容列表</p>
        :rtype: list of ConversationContent
        """
        return self._ContentList

    @ContentList.setter
    def ContentList(self, ContentList):
        self._ContentList = ContentList

    @property
    def Contents(self):
        r"""<p>消息内容列表</p>
        :rtype: list of ConversationContent
        """
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def Type(self):
        r"""<p>类型</p>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._ConversationId = params.get("ConversationId")
        self._Icon = params.get("Icon")
        self._MessageId = params.get("MessageId")
        self._Name = params.get("Name")
        self._RecordId = params.get("RecordId")
        self._Role = params.get("Role")
        self._Status = params.get("Status")
        self._StatusDesc = params.get("StatusDesc")
        self._Title = params.get("Title")
        if params.get("ContentList") is not None:
            self._ContentList = []
            for item in params.get("ContentList"):
                obj = ConversationContent()
                obj._deserialize(item)
                self._ContentList.append(obj)
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = ConversationContent()
                obj._deserialize(item)
                self._Contents.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationQuoteInfo(AbstractModel):
    r"""QuoteInfo 参考来源索引信息

    """

    def __init__(self):
        r"""
        :param _Index: <p>参考来源的索引值</p>
        :type Index: int
        :param _Position: <p>参考来源位置</p>
        :type Position: int
        """
        self._Index = None
        self._Position = None

    @property
    def Index(self):
        r"""<p>参考来源的索引值</p>
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Position(self):
        r"""<p>参考来源位置</p>
        :rtype: int
        """
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Position = params.get("Position")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationRecordErrorInfo(AbstractModel):
    r"""单次对话失败信息

    """

    def __init__(self):
        r"""
        :param _Code: <p>对话失败错误码</p>
        :type Code: str
        :param _Message: <p>对话失败错误信息</p>
        :type Message: str
        """
        self._Code = None
        self._Message = None

    @property
    def Code(self):
        r"""<p>对话失败错误码</p>
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        r"""<p>对话失败错误信息</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationRecordSummary(AbstractModel):
    r"""单次对话记录统计信息

    """

    def __init__(self):
        r"""
        :param _RecordId: <p>回复记录 ID，对应 messages 中回复消息的 record_id</p>
        :type RecordId: str
        :param _RelatedRecordId: <p>用户提问记录 ID，对应 messages 中用户消息的 record_id</p>
        :type RelatedRecordId: str
        :param _TimeUsage: <p>单次对话耗时信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeUsage: :class:`tencentcloud.adp.v20260520.models.ConversationRecordTimeUsage`
        :param _TokenUsage: <p>单次对话 token 消耗信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenUsage: :class:`tencentcloud.adp.v20260520.models.ConversationRecordTokenUsage`
        :param _ErrorInfo: <p>单次对话失败信息；成功时为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorInfo: :class:`tencentcloud.adp.v20260520.models.ConversationRecordErrorInfo`
        :param _Status: <p>单次员工助理对话当前状态</p><p>枚举值：</p><ul><li>pending： 待处理</li><li>processing： 处理中</li><li>success： 成功</li><li>failed： 失败</li><li>stop： 停止</li></ul>
        :type Status: str
        """
        self._RecordId = None
        self._RelatedRecordId = None
        self._TimeUsage = None
        self._TokenUsage = None
        self._ErrorInfo = None
        self._Status = None

    @property
    def RecordId(self):
        r"""<p>回复记录 ID，对应 messages 中回复消息的 record_id</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RelatedRecordId(self):
        r"""<p>用户提问记录 ID，对应 messages 中用户消息的 record_id</p>
        :rtype: str
        """
        return self._RelatedRecordId

    @RelatedRecordId.setter
    def RelatedRecordId(self, RelatedRecordId):
        self._RelatedRecordId = RelatedRecordId

    @property
    def TimeUsage(self):
        r"""<p>单次对话耗时信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationRecordTimeUsage`
        """
        return self._TimeUsage

    @TimeUsage.setter
    def TimeUsage(self, TimeUsage):
        self._TimeUsage = TimeUsage

    @property
    def TokenUsage(self):
        r"""<p>单次对话 token 消耗信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationRecordTokenUsage`
        """
        return self._TokenUsage

    @TokenUsage.setter
    def TokenUsage(self, TokenUsage):
        self._TokenUsage = TokenUsage

    @property
    def ErrorInfo(self):
        r"""<p>单次对话失败信息；成功时为空</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationRecordErrorInfo`
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def Status(self):
        r"""<p>单次员工助理对话当前状态</p><p>枚举值：</p><ul><li>pending： 待处理</li><li>processing： 处理中</li><li>success： 成功</li><li>failed： 失败</li><li>stop： 停止</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RelatedRecordId = params.get("RelatedRecordId")
        if params.get("TimeUsage") is not None:
            self._TimeUsage = ConversationRecordTimeUsage()
            self._TimeUsage._deserialize(params.get("TimeUsage"))
        if params.get("TokenUsage") is not None:
            self._TokenUsage = ConversationRecordTokenUsage()
            self._TokenUsage._deserialize(params.get("TokenUsage"))
        if params.get("ErrorInfo") is not None:
            self._ErrorInfo = ConversationRecordErrorInfo()
            self._ErrorInfo._deserialize(params.get("ErrorInfo"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationRecordTimeUsage(AbstractModel):
    r"""单次对话耗时信息

    """

    def __init__(self):
        r"""
        :param _Elapsed: <p>单次对话总耗时，单位毫秒</p>
        :type Elapsed: str
        :param _FirstTokenCost: <p>首 token 耗时，单位毫秒</p>
        :type FirstTokenCost: str
        :param _TotalCost: <p>模型推理总耗时，单位毫秒</p>
        :type TotalCost: str
        """
        self._Elapsed = None
        self._FirstTokenCost = None
        self._TotalCost = None

    @property
    def Elapsed(self):
        r"""<p>单次对话总耗时，单位毫秒</p>
        :rtype: str
        """
        return self._Elapsed

    @Elapsed.setter
    def Elapsed(self, Elapsed):
        self._Elapsed = Elapsed

    @property
    def FirstTokenCost(self):
        r"""<p>首 token 耗时，单位毫秒</p>
        :rtype: str
        """
        return self._FirstTokenCost

    @FirstTokenCost.setter
    def FirstTokenCost(self, FirstTokenCost):
        self._FirstTokenCost = FirstTokenCost

    @property
    def TotalCost(self):
        r"""<p>模型推理总耗时，单位毫秒</p>
        :rtype: str
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost


    def _deserialize(self, params):
        self._Elapsed = params.get("Elapsed")
        self._FirstTokenCost = params.get("FirstTokenCost")
        self._TotalCost = params.get("TotalCost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationRecordTokenUsage(AbstractModel):
    r"""单次对话 token 消耗信息

    """

    def __init__(self):
        r"""
        :param _InputTokens: <p>输入 token 总数</p>
        :type InputTokens: str
        :param _OutputTokens: <p>输出 token 总数</p>
        :type OutputTokens: str
        :param _TotalTokens: <p>消耗 token 总数</p>
        :type TotalTokens: str
        :param _CachedTokens: <p>缓存命中 token 总数</p>
        :type CachedTokens: str
        :param _ReasoningTokens: <p>推理 token 总数</p>
        :type ReasoningTokens: str
        """
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None
        self._CachedTokens = None
        self._ReasoningTokens = None

    @property
    def InputTokens(self):
        r"""<p>输入 token 总数</p>
        :rtype: str
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        r"""<p>输出 token 总数</p>
        :rtype: str
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        r"""<p>消耗 token 总数</p>
        :rtype: str
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def CachedTokens(self):
        r"""<p>缓存命中 token 总数</p>
        :rtype: str
        """
        return self._CachedTokens

    @CachedTokens.setter
    def CachedTokens(self, CachedTokens):
        self._CachedTokens = CachedTokens

    @property
    def ReasoningTokens(self):
        r"""<p>推理 token 总数</p>
        :rtype: str
        """
        return self._ReasoningTokens

    @ReasoningTokens.setter
    def ReasoningTokens(self, ReasoningTokens):
        self._ReasoningTokens = ReasoningTokens


    def _deserialize(self, params):
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        self._CachedTokens = params.get("CachedTokens")
        self._ReasoningTokens = params.get("ReasoningTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationReference(AbstractModel):
    r"""Reference 参考来源信息

    """

    def __init__(self):
        r"""
        :param _Index: <p>参考来源索引</p>
        :type Index: int
        :param _Name: <p>参考来源名称</p>
        :type Name: str
        :param _Type: <p>参考来源类型 枚举值: 0-APP_REFERENCE_TYPE_UNSPECIFIED(未指定), 1-APP_REFERENCE_TYPE_QA(问答), 2-APP_REFERENCE_TYPE_SEGMENT(分片), 3-APP_REFERENCE_TYPE_DOC(文档), 4-APP_REFERENCE_TYPE_WEB_SEARCH(Web 搜索), 5-APP_REFERENCE_TYPE_GRAPH_RAG(GraphRAG)</p>
        :type Type: int
        """
        self._Index = None
        self._Name = None
        self._Type = None

    @property
    def Index(self):
        r"""<p>参考来源索引</p>
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        r"""<p>参考来源名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>参考来源类型 枚举值: 0-APP_REFERENCE_TYPE_UNSPECIFIED(未指定), 1-APP_REFERENCE_TYPE_QA(问答), 2-APP_REFERENCE_TYPE_SEGMENT(分片), 3-APP_REFERENCE_TYPE_DOC(文档), 4-APP_REFERENCE_TYPE_WEB_SEARCH(Web 搜索), 5-APP_REFERENCE_TYPE_GRAPH_RAG(GraphRAG)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationResetInfo(AbstractModel):
    r"""会话重置信息

    """

    def __init__(self):
        r"""
        :param _ResetTime: <p>最近一次重置的毫秒级时间戳</p>
        :type ResetTime: str
        :param _ResetThroughRecordId: <p>最近一次重置边界；该记录及更早的记录不再作为对话上下文</p>
        :type ResetThroughRecordId: str
        """
        self._ResetTime = None
        self._ResetThroughRecordId = None

    @property
    def ResetTime(self):
        r"""<p>最近一次重置的毫秒级时间戳</p>
        :rtype: str
        """
        return self._ResetTime

    @ResetTime.setter
    def ResetTime(self, ResetTime):
        self._ResetTime = ResetTime

    @property
    def ResetThroughRecordId(self):
        r"""<p>最近一次重置边界；该记录及更早的记录不再作为对话上下文</p>
        :rtype: str
        """
        return self._ResetThroughRecordId

    @ResetThroughRecordId.setter
    def ResetThroughRecordId(self, ResetThroughRecordId):
        self._ResetThroughRecordId = ResetThroughRecordId


    def _deserialize(self, params):
        self._ResetTime = params.get("ResetTime")
        self._ResetThroughRecordId = params.get("ResetThroughRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConversationWorkspace(AbstractModel):
    r"""Workspace 工作空间信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: <p>工作空间 ID</p>
        :type WorkspaceId: str
        :param _StorageType: <p>存储类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        """
        self._WorkspaceId = None
        self._StorageType = None

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def StorageType(self):
        r"""<p>存储类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._StorageType = params.get("StorageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAgentFromAppRequest(AbstractModel):
    r"""CopyAgentFromApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用Id</p>
        :type AppId: str
        :param _TargetAppId: <p>目标应用ID，kind=0时需传入</p>
        :type TargetAppId: str
        :param _Kind: <p>Agent 类型，区分 B 端配置态 Agent 与 C 端用户态 Agent</p><p>枚举值：</p><ul><li>0：  配置端Agent </li><li>1：  用户态 Agent</li></ul>
        :type Kind: int
        """
        self._AppId = None
        self._TargetAppId = None
        self._Kind = None

    @property
    def AppId(self):
        r"""<p>应用Id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def TargetAppId(self):
        r"""<p>目标应用ID，kind=0时需传入</p>
        :rtype: str
        """
        return self._TargetAppId

    @TargetAppId.setter
    def TargetAppId(self, TargetAppId):
        self._TargetAppId = TargetAppId

    @property
    def Kind(self):
        r"""<p>Agent 类型，区分 B 端配置态 Agent 与 C 端用户态 Agent</p><p>枚举值：</p><ul><li>0：  配置端Agent </li><li>1：  用户态 Agent</li></ul>
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._TargetAppId = params.get("TargetAppId")
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAgentFromAppResponse(AbstractModel):
    r"""CopyAgentFromApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ParentAgentId: <p>主 Agent Id</p>
        :type ParentAgentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ParentAgentId = None
        self._RequestId = None

    @property
    def ParentAgentId(self):
        r"""<p>主 Agent Id</p>
        :rtype: str
        """
        return self._ParentAgentId

    @ParentAgentId.setter
    def ParentAgentId(self, ParentAgentId):
        self._ParentAgentId = ParentAgentId

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
        self._ParentAgentId = params.get("ParentAgentId")
        self._RequestId = params.get("RequestId")


class CopyAppRequest(AbstractModel):
    r"""CopyApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _TargetSpaceId: target_space_id
        :type TargetSpaceId: str
        """
        self._AppId = None
        self._TargetSpaceId = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def TargetSpaceId(self):
        r"""target_space_id
        :rtype: str
        """
        return self._TargetSpaceId

    @TargetSpaceId.setter
    def TargetSpaceId(self, TargetSpaceId):
        self._TargetSpaceId = TargetSpaceId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._TargetSpaceId = params.get("TargetSpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CopyAppResponse(AbstractModel):
    r"""CopyApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NewAppId: new_app_id
        :type NewAppId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NewAppId = None
        self._RequestId = None

    @property
    def NewAppId(self):
        r"""new_app_id
        :rtype: str
        """
        return self._NewAppId

    @NewAppId.setter
    def NewAppId(self, NewAppId):
        self._NewAppId = NewAppId

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
        self._NewAppId = params.get("NewAppId")
        self._RequestId = params.get("RequestId")


class CorpShareConfig(AbstractModel):
    r"""CorpShareConfig

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>企业共享开关</p>
        :type Enabled: bool
        :param _ShareScope: <p>共享范围类型，1：企业全员，2：指定账户，3：指定空间</p>
        :type ShareScope: int
        :param _TagIdList: <p>企业共享应用标签</p>
        :type TagIdList: list of str
        :param _ShareScopeList: <p>共享范围信息(用户时StrId为uin,Name为用户名称;空间时StrId为空间ID,Name为空间名称)</p>
        :type ShareScopeList: list of Identity
        """
        self._Enabled = None
        self._ShareScope = None
        self._TagIdList = None
        self._ShareScopeList = None

    @property
    def Enabled(self):
        r"""<p>企业共享开关</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def ShareScope(self):
        r"""<p>共享范围类型，1：企业全员，2：指定账户，3：指定空间</p>
        :rtype: int
        """
        return self._ShareScope

    @ShareScope.setter
    def ShareScope(self, ShareScope):
        self._ShareScope = ShareScope

    @property
    def TagIdList(self):
        r"""<p>企业共享应用标签</p>
        :rtype: list of str
        """
        return self._TagIdList

    @TagIdList.setter
    def TagIdList(self, TagIdList):
        self._TagIdList = TagIdList

    @property
    def ShareScopeList(self):
        r"""<p>共享范围信息(用户时StrId为uin,Name为用户名称;空间时StrId为空间ID,Name为空间名称)</p>
        :rtype: list of Identity
        """
        return self._ShareScopeList

    @ShareScopeList.setter
    def ShareScopeList(self, ShareScopeList):
        self._ShareScopeList = ShareScopeList


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._ShareScope = params.get("ShareScope")
        self._TagIdList = params.get("TagIdList")
        if params.get("ShareScopeList") is not None:
            self._ShareScopeList = []
            for item in params.get("ShareScopeList"):
                obj = Identity()
                obj._deserialize(item)
                self._ShareScopeList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentRequest(AbstractModel):
    r"""CreateAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用Id</p>
        :type AppId: str
        :param _Agent: <p>Agent 配置</p>
        :type Agent: :class:`tencentcloud.adp.v20260520.models.AgentSpec`
        :param _Kind: <p>Agent 类型，区分 B 端配置态 Agent 与 C 端用户态 Agent</p><p>枚举值：</p><ul><li>0： 配置端Agent</li><li>1： 用户态 Agent</li></ul>
        :type Kind: int
        """
        self._AppId = None
        self._Agent = None
        self._Kind = None

    @property
    def AppId(self):
        r"""<p>应用Id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Agent(self):
        r"""<p>Agent 配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentSpec`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def Kind(self):
        r"""<p>Agent 类型，区分 B 端配置态 Agent 与 C 端用户态 Agent</p><p>枚举值：</p><ul><li>0： 配置端Agent</li><li>1： 用户态 Agent</li></ul>
        :rtype: int
        """
        return self._Kind

    @Kind.setter
    def Kind(self, Kind):
        self._Kind = Kind


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("Agent") is not None:
            self._Agent = AgentSpec()
            self._Agent._deserialize(params.get("Agent"))
        self._Kind = params.get("Kind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAgentResponse(AbstractModel):
    r"""CreateAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AgentId: <p>Agent Id</p>
        :type AgentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AgentId = None
        self._RequestId = None

    @property
    def AgentId(self):
        r"""<p>Agent Id</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

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
        self._AgentId = params.get("AgentId")
        self._RequestId = params.get("RequestId")


class CreateAppRequest(AbstractModel):
    r"""CreateApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间ID
        :type SpaceId: str
        :param _AppMode: 应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :type AppMode: int
        :param _Avatar: 应用头像
        :type Avatar: str
        :param _Description: 应用描述
        :type Description: str
        :param _Name: 应用名称
        :type Name: str
        """
        self._SpaceId = None
        self._AppMode = None
        self._Avatar = None
        self._Description = None
        self._Name = None

    @property
    def SpaceId(self):
        r"""空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def AppMode(self):
        r"""应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :rtype: int
        """
        return self._AppMode

    @AppMode.setter
    def AppMode(self, AppMode):
        self._AppMode = AppMode

    @property
    def Avatar(self):
        r"""应用头像
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

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
    def Name(self):
        r"""应用名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._AppMode = params.get("AppMode")
        self._Avatar = params.get("Avatar")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppResponse(AbstractModel):
    r"""CreateApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

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
        self._AppId = params.get("AppId")
        self._RequestId = params.get("RequestId")


class CreateAppTriggerRequest(AbstractModel):
    r"""CreateAppTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _ExecuteConfig: <p>应用触发器执行配置</p>
        :type ExecuteConfig: :class:`tencentcloud.adp.v20260520.models.ExecuteConfig`
        :param _ExecuteType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_PROMPT</td><td>1</td><td>指令执行</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_WORKFLOW</td><td>2</td><td>工作流执行</td></tr></tbody></table>
        :type ExecuteType: int
        :param _PushConfig: <p>第三方推送配置</p>
        :type PushConfig: :class:`tencentcloud.adp.v20260520.models.TimerPushConfig`
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerConfig: <p>触发器配置</p>
        :type TriggerConfig: :class:`tencentcloud.adp.v20260520.models.TriggerConfig`
        :param _TriggerName: <p>触发器名字</p>
        :type TriggerName: str
        :param _TriggerType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr></tbody></table>
        :type TriggerType: int
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._ExecuteConfig = None
        self._ExecuteType = None
        self._PushConfig = None
        self._Scope = None
        self._TriggerConfig = None
        self._TriggerName = None
        self._TriggerType = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ExecuteConfig(self):
        r"""<p>应用触发器执行配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ExecuteConfig`
        """
        return self._ExecuteConfig

    @ExecuteConfig.setter
    def ExecuteConfig(self, ExecuteConfig):
        self._ExecuteConfig = ExecuteConfig

    @property
    def ExecuteType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_PROMPT</td><td>1</td><td>指令执行</td></tr><tr><td>APP_TRIGGER_EXECUTE_TYPE_WORKFLOW</td><td>2</td><td>工作流执行</td></tr></tbody></table>
        :rtype: int
        """
        return self._ExecuteType

    @ExecuteType.setter
    def ExecuteType(self, ExecuteType):
        self._ExecuteType = ExecuteType

    @property
    def PushConfig(self):
        r"""<p>第三方推送配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimerPushConfig`
        """
        return self._PushConfig

    @PushConfig.setter
    def PushConfig(self, PushConfig):
        self._PushConfig = PushConfig

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerConfig(self):
        r"""<p>触发器配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TriggerConfig`
        """
        return self._TriggerConfig

    @TriggerConfig.setter
    def TriggerConfig(self, TriggerConfig):
        self._TriggerConfig = TriggerConfig

    @property
    def TriggerName(self):
        r"""<p>触发器名字</p>
        :rtype: str
        """
        return self._TriggerName

    @TriggerName.setter
    def TriggerName(self, TriggerName):
        self._TriggerName = TriggerName

    @property
    def TriggerType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_TYPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_TYPE_SCHEDULED</td><td>1</td><td>定时触发</td></tr><tr><td>APP_TRIGGER_TYPE_WEBHOOK</td><td>2</td><td>Webhook 触发</td></tr></tbody></table>
        :rtype: int
        """
        return self._TriggerType

    @TriggerType.setter
    def TriggerType(self, TriggerType):
        self._TriggerType = TriggerType

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("ExecuteConfig") is not None:
            self._ExecuteConfig = ExecuteConfig()
            self._ExecuteConfig._deserialize(params.get("ExecuteConfig"))
        self._ExecuteType = params.get("ExecuteType")
        if params.get("PushConfig") is not None:
            self._PushConfig = TimerPushConfig()
            self._PushConfig._deserialize(params.get("PushConfig"))
        self._Scope = params.get("Scope")
        if params.get("TriggerConfig") is not None:
            self._TriggerConfig = TriggerConfig()
            self._TriggerConfig._deserialize(params.get("TriggerConfig"))
        self._TriggerName = params.get("TriggerName")
        self._TriggerType = params.get("TriggerType")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAppTriggerResponse(AbstractModel):
    r"""CreateAppTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TriggerId: <p>应用触发器ID</p>
        :type TriggerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TriggerId = None
        self._RequestId = None

    @property
    def TriggerId(self):
        r"""<p>应用触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

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
        self._TriggerId = params.get("TriggerId")
        self._RequestId = params.get("RequestId")


class CreateConversationRequest(AbstractModel):
    r"""CreateConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>登录用户子账号(集成商模式必填)</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>登录用户主账号(集成商模式必填)</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        :param _AgentId: <p>用户端 AgnetId，当Claw模式开启了“允许在对话中动态修改配置”时可用</p>
        :type AgentId: str
        """
        self._Type = None
        self._AppId = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None
        self._UserId = None
        self._AgentId = None

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>登录用户子账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>登录用户主账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AgentId(self):
        r"""<p>用户端 AgnetId，当Claw模式开启了“允许在对话中动态修改配置”时可用</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppId = params.get("AppId")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConversationResponse(AbstractModel):
    r"""CreateConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConversationId = None
        self._RequestId = None

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

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
        self._ConversationId = params.get("ConversationId")
        self._RequestId = params.get("RequestId")


class CreateMsgRecordCategoryRequest(AbstractModel):
    r"""CreateMsgRecordCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>分类名称</p>
        :type Name: str
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _ParentId: <p>父分类业务 ID，0 表示一级分类（未分类）</p>
        :type ParentId: str
        """
        self._Name = None
        self._AppId = None
        self._ParentId = None

    @property
    def Name(self):
        r"""<p>分类名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ParentId(self):
        r"""<p>父分类业务 ID，0 表示一级分类（未分类）</p>
        :rtype: str
        """
        return self._ParentId

    @ParentId.setter
    def ParentId(self, ParentId):
        self._ParentId = ParentId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._ParentId = params.get("ParentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMsgRecordCategoryResponse(AbstractModel):
    r"""CreateMsgRecordCategory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryId: <p>新建分类的业务 ID</p>
        :type CategoryId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryId = None
        self._RequestId = None

    @property
    def CategoryId(self):
        r"""<p>新建分类的业务 ID</p>
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

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
        self._CategoryId = params.get("CategoryId")
        self._RequestId = params.get("RequestId")


class CreatePluginRequest(AbstractModel):
    r"""CreatePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Profile: <p>插件基础资料</p>
        :type Profile: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        :param _Config: <p>插件类型配置</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        :param _SpaceId: <p>当前空间id</p>
        :type SpaceId: str
        :param _ToolList: <p>插件的工具列表</p>
        :type ToolList: list of Tool
        :param _LoginUin: <p>登录用户主账号(集成商模式必填)</p>
        :type LoginUin: str
        :param _LoginSubAccountUin: <p>登录用户子账号(集成商模式必填)</p>
        :type LoginSubAccountUin: str
        """
        self._Profile = None
        self._Config = None
        self._SpaceId = None
        self._ToolList = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def Profile(self):
        r"""<p>插件基础资料</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Config(self):
        r"""<p>插件类型配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def SpaceId(self):
        r"""<p>当前空间id</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def ToolList(self):
        r"""<p>插件的工具列表</p>
        :rtype: list of Tool
        """
        return self._ToolList

    @ToolList.setter
    def ToolList(self, ToolList):
        self._ToolList = ToolList

    @property
    def LoginUin(self):
        r"""<p>登录用户主账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""<p>登录用户子账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        if params.get("Profile") is not None:
            self._Profile = PluginProfile()
            self._Profile._deserialize(params.get("Profile"))
        if params.get("Config") is not None:
            self._Config = PluginConfig()
            self._Config._deserialize(params.get("Config"))
        self._SpaceId = params.get("SpaceId")
        if params.get("ToolList") is not None:
            self._ToolList = []
            for item in params.get("ToolList"):
                obj = Tool()
                obj._deserialize(item)
                self._ToolList.append(obj)
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePluginResponse(AbstractModel):
    r"""CreatePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PluginId = None
        self._RequestId = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

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
        self._PluginId = params.get("PluginId")
        self._RequestId = params.get("RequestId")


class CreateReleaseRequest(AbstractModel):
    r"""CreateRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _AppShareAccessControl: <p>应用分享访问控制配置</p>
        :type AppShareAccessControl: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        :param _ChannelIdList: <p>渠道ID列表</p>
        :type ChannelIdList: list of str
        :param _CorpShareConfig: <p>企业共享配置</p>
        :type CorpShareConfig: :class:`tencentcloud.adp.v20260520.models.CorpShareConfig`
        :param _Description: <p>发布描述</p>
        :type Description: str
        :param _IsDevToRelease: <p>将默认知识库中，仅调试生效的知识批量变更为&quot;调试/发布都生效&quot;</p>
        :type IsDevToRelease: bool
        :param _IsPublishAsTemplate: <p>是否同步发布为应用模板</p>
        :type IsPublishAsTemplate: bool
        """
        self._AppId = None
        self._AppShareAccessControl = None
        self._ChannelIdList = None
        self._CorpShareConfig = None
        self._Description = None
        self._IsDevToRelease = None
        self._IsPublishAsTemplate = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppShareAccessControl(self):
        r"""<p>应用分享访问控制配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        """
        return self._AppShareAccessControl

    @AppShareAccessControl.setter
    def AppShareAccessControl(self, AppShareAccessControl):
        self._AppShareAccessControl = AppShareAccessControl

    @property
    def ChannelIdList(self):
        r"""<p>渠道ID列表</p>
        :rtype: list of str
        """
        return self._ChannelIdList

    @ChannelIdList.setter
    def ChannelIdList(self, ChannelIdList):
        self._ChannelIdList = ChannelIdList

    @property
    def CorpShareConfig(self):
        r"""<p>企业共享配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.CorpShareConfig`
        """
        return self._CorpShareConfig

    @CorpShareConfig.setter
    def CorpShareConfig(self, CorpShareConfig):
        self._CorpShareConfig = CorpShareConfig

    @property
    def Description(self):
        r"""<p>发布描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsDevToRelease(self):
        r"""<p>将默认知识库中，仅调试生效的知识批量变更为&quot;调试/发布都生效&quot;</p>
        :rtype: bool
        """
        return self._IsDevToRelease

    @IsDevToRelease.setter
    def IsDevToRelease(self, IsDevToRelease):
        self._IsDevToRelease = IsDevToRelease

    @property
    def IsPublishAsTemplate(self):
        r"""<p>是否同步发布为应用模板</p>
        :rtype: bool
        """
        return self._IsPublishAsTemplate

    @IsPublishAsTemplate.setter
    def IsPublishAsTemplate(self, IsPublishAsTemplate):
        self._IsPublishAsTemplate = IsPublishAsTemplate


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("AppShareAccessControl") is not None:
            self._AppShareAccessControl = AppShareAccessControl()
            self._AppShareAccessControl._deserialize(params.get("AppShareAccessControl"))
        self._ChannelIdList = params.get("ChannelIdList")
        if params.get("CorpShareConfig") is not None:
            self._CorpShareConfig = CorpShareConfig()
            self._CorpShareConfig._deserialize(params.get("CorpShareConfig"))
        self._Description = params.get("Description")
        self._IsDevToRelease = params.get("IsDevToRelease")
        self._IsPublishAsTemplate = params.get("IsPublishAsTemplate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReleaseResponse(AbstractModel):
    r"""CreateRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NeedApproval: <p>need_approval</p>
        :type NeedApproval: bool
        :param _ReleaseId: <p>release_id</p>
        :type ReleaseId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NeedApproval = None
        self._ReleaseId = None
        self._RequestId = None

    @property
    def NeedApproval(self):
        r"""<p>need_approval</p>
        :rtype: bool
        """
        return self._NeedApproval

    @NeedApproval.setter
    def NeedApproval(self, NeedApproval):
        self._NeedApproval = NeedApproval

    @property
    def ReleaseId(self):
        r"""<p>release_id</p>
        :rtype: str
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId

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
        self._NeedApproval = params.get("NeedApproval")
        self._ReleaseId = params.get("ReleaseId")
        self._RequestId = params.get("RequestId")


class CreateSkillRequest(AbstractModel):
    r"""CreateSkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CreateType: <p>Skill 创建方式，必填；仅允许</p><p>枚举值：</p><ul><li>1： FILE_UPLOAD（文件上传）</li><li>3： AIGC（AIGC生成）</li></ul>
        :type CreateType: int
        :param _FileUrl: <p>skill包文件地址（zip）；FILE_UPLOAD / AIGC 均必填</p>
        :type FileUrl: str
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        :param _DisplayDescription: <p>skill展示描述</p>
        :type DisplayDescription: str
        :param _DisplayName: <p>skill展示名称</p>
        :type DisplayName: str
        :param _IconUrl: <p>图标地址</p>
        :type IconUrl: str
        :param _Name: <p>skill业务唯一标识名（同企业下唯一）；未传时从skill包解析</p>
        :type Name: str
        :param _SkillVersion: <p>版本号</p>
        :type SkillVersion: str
        :param _UpdateDescription: <p>版本变更说明</p>
        :type UpdateDescription: str
        """
        self._CreateType = None
        self._FileUrl = None
        self._SpaceId = None
        self._DisplayDescription = None
        self._DisplayName = None
        self._IconUrl = None
        self._Name = None
        self._SkillVersion = None
        self._UpdateDescription = None

    @property
    def CreateType(self):
        r"""<p>Skill 创建方式，必填；仅允许</p><p>枚举值：</p><ul><li>1： FILE_UPLOAD（文件上传）</li><li>3： AIGC（AIGC生成）</li></ul>
        :rtype: int
        """
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType

    @property
    def FileUrl(self):
        r"""<p>skill包文件地址（zip）；FILE_UPLOAD / AIGC 均必填</p>
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def DisplayDescription(self):
        r"""<p>skill展示描述</p>
        :rtype: str
        """
        return self._DisplayDescription

    @DisplayDescription.setter
    def DisplayDescription(self, DisplayDescription):
        self._DisplayDescription = DisplayDescription

    @property
    def DisplayName(self):
        r"""<p>skill展示名称</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def IconUrl(self):
        r"""<p>图标地址</p>
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Name(self):
        r"""<p>skill业务唯一标识名（同企业下唯一）；未传时从skill包解析</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkillVersion(self):
        r"""<p>版本号</p>
        :rtype: str
        """
        return self._SkillVersion

    @SkillVersion.setter
    def SkillVersion(self, SkillVersion):
        self._SkillVersion = SkillVersion

    @property
    def UpdateDescription(self):
        r"""<p>版本变更说明</p>
        :rtype: str
        """
        return self._UpdateDescription

    @UpdateDescription.setter
    def UpdateDescription(self, UpdateDescription):
        self._UpdateDescription = UpdateDescription


    def _deserialize(self, params):
        self._CreateType = params.get("CreateType")
        self._FileUrl = params.get("FileUrl")
        self._SpaceId = params.get("SpaceId")
        self._DisplayDescription = params.get("DisplayDescription")
        self._DisplayName = params.get("DisplayName")
        self._IconUrl = params.get("IconUrl")
        self._Name = params.get("Name")
        self._SkillVersion = params.get("SkillVersion")
        self._UpdateDescription = params.get("UpdateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSkillResponse(AbstractModel):
    r"""CreateSkill返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>创建成功后的skillID</p>
        :type SkillId: str
        :param _VersionId: <p>创建成功后的版本ID</p>
        :type VersionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SkillId = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SkillId(self):
        r"""<p>创建成功后的skillID</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def VersionId(self):
        r"""<p>创建成功后的版本ID</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

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
        self._SkillId = params.get("SkillId")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class CreateSkillShareRequest(AbstractModel):
    r"""CreateSkillShare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyRemark: <p>必填，申请备注（弹窗&quot;申请备注&quot;）</p>
        :type ApplyRemark: str
        :param _SkillId: <p>必填，原skill_id</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID，必填</p>
        :type SpaceId: str
        :param _VersionId: <p>必填，被共享的版本id（必须高于已共享版本）</p>
        :type VersionId: str
        """
        self._ApplyRemark = None
        self._SkillId = None
        self._SpaceId = None
        self._VersionId = None

    @property
    def ApplyRemark(self):
        r"""<p>必填，申请备注（弹窗&quot;申请备注&quot;）</p>
        :rtype: str
        """
        return self._ApplyRemark

    @ApplyRemark.setter
    def ApplyRemark(self, ApplyRemark):
        self._ApplyRemark = ApplyRemark

    @property
    def SkillId(self):
        r"""<p>必填，原skill_id</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID，必填</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def VersionId(self):
        r"""<p>必填，被共享的版本id（必须高于已共享版本）</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._ApplyRemark = params.get("ApplyRemark")
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSkillShareResponse(AbstractModel):
    r"""CreateSkillShare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NeedApproval: <p>是否走了审批流（false表示无需审批已直接创建共享任务）</p>
        :type NeedApproval: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NeedApproval = None
        self._RequestId = None

    @property
    def NeedApproval(self):
        r"""<p>是否走了审批流（false表示无需审批已直接创建共享任务）</p>
        :rtype: bool
        """
        return self._NeedApproval

    @NeedApproval.setter
    def NeedApproval(self, NeedApproval):
        self._NeedApproval = NeedApproval

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
        self._NeedApproval = params.get("NeedApproval")
        self._RequestId = params.get("RequestId")


class CreateSpaceRequest(AbstractModel):
    r"""CreateSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 工作空间名称,长度最大30个字符
        :type Name: str
        :param _Description: 空间描述，长度最大150个字符
        :type Description: str
        """
        self._Name = None
        self._Description = None

    @property
    def Name(self):
        r"""工作空间名称,长度最大30个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""空间描述，长度最大150个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSpaceResponse(AbstractModel):
    r"""CreateSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SpaceId = None
        self._RequestId = None

    @property
    def SpaceId(self):
        r"""空间id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

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
        self._SpaceId = params.get("SpaceId")
        self._RequestId = params.get("RequestId")


class CreateVariableRequest(AbstractModel):
    r"""CreateVariable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _Variable: 变量信息
        :type Variable: :class:`tencentcloud.adp.v20260520.models.Variable`
        """
        self._AppId = None
        self._Variable = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Variable(self):
        r"""变量信息
        :rtype: :class:`tencentcloud.adp.v20260520.models.Variable`
        """
        return self._Variable

    @Variable.setter
    def Variable(self, Variable):
        self._Variable = Variable


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("Variable") is not None:
            self._Variable = Variable()
            self._Variable._deserialize(params.get("Variable"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVariableResponse(AbstractModel):
    r"""CreateVariable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VariableId: variable_id
        :type VariableId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VariableId = None
        self._RequestId = None

    @property
    def VariableId(self):
        r"""variable_id
        :rtype: str
        """
        return self._VariableId

    @VariableId.setter
    def VariableId(self, VariableId):
        self._VariableId = VariableId

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
        self._VariableId = params.get("VariableId")
        self._RequestId = params.get("RequestId")


class CreateWebSocketTokenRequest(AbstractModel):
    r"""CreateWebSocketToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>子用户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>主用户Uin</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        """
        self._Type = None
        self._AppId = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None
        self._UserId = None

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>子用户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>主用户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppId = params.get("AppId")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebSocketTokenResponse(AbstractModel):
    r"""CreateWebSocketToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Token: <p>WebSocket Token</p>
        :type Token: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._Token = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Token(self):
        r"""<p>WebSocket Token</p>
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

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
        self._AppId = params.get("AppId")
        self._Token = params.get("Token")
        self._RequestId = params.get("RequestId")


class CreateWorkspaceCredentialRequest(AbstractModel):
    r"""CreateWorkspaceCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _WorkspaceId: <p>工作空间 ID</p>
        :type WorkspaceId: str
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>子用户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>主用户Uin</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        """
        self._Type = None
        self._WorkspaceId = None
        self._AppId = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None
        self._UserId = None

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>子用户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>主用户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._WorkspaceId = params.get("WorkspaceId")
        self._AppId = params.get("AppId")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceCredentialResponse(AbstractModel):
    r"""CreateWorkspaceCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StorageType: <p>存储类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageType: str
        :param _WorkspaceId: <p>工作空间 ID</p>
        :type WorkspaceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StorageType = None
        self._WorkspaceId = None
        self._RequestId = None

    @property
    def StorageType(self):
        r"""<p>存储类型</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StorageType

    @StorageType.setter
    def StorageType(self, StorageType):
        self._StorageType = StorageType

    @property
    def WorkspaceId(self):
        r"""<p>工作空间 ID</p>
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

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
        self._StorageType = params.get("StorageType")
        self._WorkspaceId = params.get("WorkspaceId")
        self._RequestId = params.get("RequestId")


class CronSchedule(AbstractModel):
    r"""CronSchedule

    """

    def __init__(self):
        r"""
        :param _Expression: cron表达式
        :type Expression: str
        """
        self._Expression = None

    @property
    def Expression(self):
        r"""cron表达式
        :rtype: str
        """
        return self._Expression

    @Expression.setter
    def Expression(self, Expression):
        self._Expression = Expression


    def _deserialize(self, params):
        self._Expression = params.get("Expression")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DailySchedule(AbstractModel):
    r"""DailySchedule

    """

    def __init__(self):
        r"""
        :param _TimeOfDay: 时间
        :type TimeOfDay: str
        """
        self._TimeOfDay = None

    @property
    def TimeOfDay(self):
        r"""时间
        :rtype: str
        """
        return self._TimeOfDay

    @TimeOfDay.setter
    def TimeOfDay(self, TimeOfDay):
        self._TimeOfDay = TimeOfDay


    def _deserialize(self, params):
        self._TimeOfDay = params.get("TimeOfDay")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentRequest(AbstractModel):
    r"""DeleteAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用Id</p>
        :type AppId: str
        :param _AgentId: <p>待删除AgentId</p>
        :type AgentId: str
        :param _CollaborationMode: 协作模式；0-Claw模式；1-Multi-Agent模式
        :type CollaborationMode: int
        """
        self._AppId = None
        self._AgentId = None
        self._CollaborationMode = None

    @property
    def AppId(self):
        r"""<p>应用Id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AgentId(self):
        r"""<p>待删除AgentId</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def CollaborationMode(self):
        r"""协作模式；0-Claw模式；1-Multi-Agent模式
        :rtype: int
        """
        return self._CollaborationMode

    @CollaborationMode.setter
    def CollaborationMode(self, CollaborationMode):
        self._CollaborationMode = CollaborationMode


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AgentId = params.get("AgentId")
        self._CollaborationMode = params.get("CollaborationMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAgentResponse(AbstractModel):
    r"""DeleteAgent返回参数结构体

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


class DeleteAppRequest(AbstractModel):
    r"""DeleteApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>app_id</p>
        :type AppId: str
        :param _Reason: <p>删除原因(非必填,审批时展示)</p>
        :type Reason: str
        """
        self._AppId = None
        self._Reason = None

    @property
    def AppId(self):
        r"""<p>app_id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Reason(self):
        r"""<p>删除原因(非必填,审批时展示)</p>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppResponse(AbstractModel):
    r"""DeleteApp返回参数结构体

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


class DeleteAppTriggerRequest(AbstractModel):
    r"""DeleteAppTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerId: <p>触发器ID</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._Scope = None
        self._TriggerId = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerId(self):
        r"""<p>触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Scope = params.get("Scope")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppTriggerResponse(AbstractModel):
    r"""DeleteAppTrigger返回参数结构体

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


class DeleteConversationRequest(AbstractModel):
    r"""DeleteConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>子用户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>主用户Uin</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        """
        self._ConversationId = None
        self._Type = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>子用户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>主用户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode


    def _deserialize(self, params):
        self._ConversationId = params.get("ConversationId")
        self._Type = params.get("Type")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteConversationResponse(AbstractModel):
    r"""DeleteConversation返回参数结构体

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


class DeleteMsgRecordCategoryRequest(AbstractModel):
    r"""DeleteMsgRecordCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _CategoryId: <p>待删除的分类业务 ID</p>
        :type CategoryId: str
        """
        self._AppId = None
        self._CategoryId = None

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CategoryId(self):
        r"""<p>待删除的分类业务 ID</p>
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._CategoryId = params.get("CategoryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMsgRecordCategoryResponse(AbstractModel):
    r"""DeleteMsgRecordCategory返回参数结构体

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


class DeletePluginRequest(AbstractModel):
    r"""DeletePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _LoginUin: <p>登录用户主账号(集成商模式必填)</p>
        :type LoginUin: str
        :param _LoginSubAccountUin: <p>登录用户子账号(集成商模式必填)</p>
        :type LoginSubAccountUin: str
        """
        self._PluginId = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def LoginUin(self):
        r"""<p>登录用户主账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""<p>登录用户子账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePluginResponse(AbstractModel):
    r"""DeletePlugin返回参数结构体

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


class DeleteSkillRequest(AbstractModel):
    r"""DeleteSkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>Skill ID，必填</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID，必填</p>
        :type SpaceId: str
        """
        self._SkillId = None
        self._SpaceId = None

    @property
    def SkillId(self):
        r"""<p>Skill ID，必填</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID，必填</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSkillResponse(AbstractModel):
    r"""DeleteSkill返回参数结构体

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


class DeleteSkillShareRequest(AbstractModel):
    r"""DeleteSkillShare请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyRemark: <p>申请备注，必填（弹窗&quot;申请备注&quot;）</p>
        :type ApplyRemark: str
        :param _SkillId: <p>原 Skill ID，必填（前端无须感知 _shared 后缀）</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID，必填</p>
        :type SpaceId: str
        :param _VersionId: <p>原版本 ID，必填（与 CreateSkillShare 上架时传的同一 version_id）</p>
        :type VersionId: str
        """
        self._ApplyRemark = None
        self._SkillId = None
        self._SpaceId = None
        self._VersionId = None

    @property
    def ApplyRemark(self):
        r"""<p>申请备注，必填（弹窗&quot;申请备注&quot;）</p>
        :rtype: str
        """
        return self._ApplyRemark

    @ApplyRemark.setter
    def ApplyRemark(self, ApplyRemark):
        self._ApplyRemark = ApplyRemark

    @property
    def SkillId(self):
        r"""<p>原 Skill ID，必填（前端无须感知 _shared 后缀）</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID，必填</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def VersionId(self):
        r"""<p>原版本 ID，必填（与 CreateSkillShare 上架时传的同一 version_id）</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._ApplyRemark = params.get("ApplyRemark")
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSkillShareResponse(AbstractModel):
    r"""DeleteSkillShare返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NeedApproval: <p>是否走审批流（false 表示无需审批已直接执行下架）</p>
        :type NeedApproval: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NeedApproval = None
        self._RequestId = None

    @property
    def NeedApproval(self):
        r"""<p>是否走审批流（false 表示无需审批已直接执行下架）</p>
        :rtype: bool
        """
        return self._NeedApproval

    @NeedApproval.setter
    def NeedApproval(self, NeedApproval):
        self._NeedApproval = NeedApproval

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
        self._NeedApproval = params.get("NeedApproval")
        self._RequestId = params.get("RequestId")


class DeleteSpaceRequest(AbstractModel):
    r"""DeleteSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间id
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        r"""空间id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSpaceResponse(AbstractModel):
    r"""DeleteSpace返回参数结构体

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


class DeleteVariableRequest(AbstractModel):
    r"""DeleteVariable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _VariableId: variable_id
        :type VariableId: str
        :param _ModuleType: module_type。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :type ModuleType: int
        """
        self._AppId = None
        self._VariableId = None
        self._ModuleType = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def VariableId(self):
        r"""variable_id
        :rtype: str
        """
        return self._VariableId

    @VariableId.setter
    def VariableId(self, VariableId):
        self._VariableId = VariableId

    @property
    def ModuleType(self):
        r"""module_type。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :rtype: int
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._VariableId = params.get("VariableId")
        self._ModuleType = params.get("ModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVariableResponse(AbstractModel):
    r"""DeleteVariable返回参数结构体

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


class DescribeAccountListRequest(AbstractModel):
    r"""DescribeAccountList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageNumber: <p>页码</p><p>从0开始</p>
        :type PageNumber: int
        :param _PageSize: <p>分页数量</p><p>取值范围：[1, 100]</p><p>单位：个</p><p>最大100</p>
        :type PageSize: int
        :param _FilterList: <p>参数过滤</p><p>支持SpaceId,NIckName 过滤查询</p>
        :type FilterList: list of Filter
        """
        self._PageNumber = None
        self._PageSize = None
        self._FilterList = None

    @property
    def PageNumber(self):
        r"""<p>页码</p><p>从0开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>分页数量</p><p>取值范围：[1, 100]</p><p>单位：个</p><p>最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FilterList(self):
        r"""<p>参数过滤</p><p>支持SpaceId,NIckName 过滤查询</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountListResponse(AbstractModel):
    r"""DescribeAccountList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
        :type TotalCount: str
        :param _AccountList: <p>员工列表</p>
        :type AccountList: list of AccountInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountList(self):
        r"""<p>员工列表</p>
        :rtype: list of AccountInfo
        """
        return self._AccountList

    @AccountList.setter
    def AccountList(self, AccountList):
        self._AccountList = AccountList

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
        if params.get("AccountList") is not None:
            self._AccountList = []
            for item in params.get("AccountList"):
                obj = AccountInfo()
                obj._deserialize(item)
                self._AccountList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAgentDetailRequest(AbstractModel):
    r"""DescribeAgentDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用Id</p>
        :type AppId: str
        :param _AgentId: <p>AgentId</p>
        :type AgentId: str
        """
        self._AppId = None
        self._AgentId = None

    @property
    def AppId(self):
        r"""<p>应用Id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AgentId(self):
        r"""<p>AgentId</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentDetailResponse(AbstractModel):
    r"""DescribeAgentDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Agent: <p>Agent信息</p>
        :type Agent: :class:`tencentcloud.adp.v20260520.models.AgentDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Agent = None
        self._RequestId = None

    @property
    def Agent(self):
        r"""<p>Agent信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentDetail`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

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
        if params.get("Agent") is not None:
            self._Agent = AgentDetail()
            self._Agent._deserialize(params.get("Agent"))
        self._RequestId = params.get("RequestId")


class DescribeAgentReleasePreviewListRequest(AbstractModel):
    r"""DescribeAgentReleasePreviewList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用Id</p>
        :type AppId: str
        :param _PageNumber: <p>页码</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量在1到200之间</p>
        :type PageSize: int
        :param _Query: <p>查询关键字, 用于模糊匹配标题</p>
        :type Query: str
        :param _FilterList: <p>过滤条件</p><p>入参限制：支持 StartTime、EndTime、ActionList、ReleaseStatusList</p>
        :type FilterList: list of Filter
        """
        self._AppId = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._FilterList = None

    @property
    def AppId(self):
        r"""<p>应用Id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PageNumber(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量在1到200之间</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""<p>查询关键字, 用于模糊匹配标题</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def FilterList(self):
        r"""<p>过滤条件</p><p>入参限制：支持 StartTime、EndTime、ActionList、ReleaseStatusList</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentReleasePreviewListResponse(AbstractModel):
    r"""DescribeAgentReleasePreviewList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReleaseList: <p>发布预览列表</p>
        :type ReleaseList: list of AgentReleasePreview
        :param _TotalCount: <p>总数</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReleaseList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ReleaseList(self):
        r"""<p>发布预览列表</p>
        :rtype: list of AgentReleasePreview
        """
        return self._ReleaseList

    @ReleaseList.setter
    def ReleaseList(self, ReleaseList):
        self._ReleaseList = ReleaseList

    @property
    def TotalCount(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ReleaseList") is not None:
            self._ReleaseList = []
            for item in params.get("ReleaseList"):
                obj = AgentReleasePreview()
                obj._deserialize(item)
                self._ReleaseList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAgentSummaryListRequest(AbstractModel):
    r"""DescribeAgentSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Scope: <p>查询范围；0-单应用查询；1-跨应用查询</p>
        :type Scope: int
        :param _AppId: <p>应用Id，Scope=0 时为目标应用ID（必填）；scope=1 时无需填写</p>
        :type AppId: str
        :param _FilterList: <p>过滤条件（name: "SearchWord", "SpaceId", "AgentSource", "AppId"）</p>
        :type FilterList: list of Filter
        :param _PageSize: <p>每页数目</p>
        :type PageSize: int
        :param _PageNumber: <p>页码</p>
        :type PageNumber: int
        """
        self._Scope = None
        self._AppId = None
        self._FilterList = None
        self._PageSize = None
        self._PageNumber = None

    @property
    def Scope(self):
        r"""<p>查询范围；0-单应用查询；1-跨应用查询</p>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def AppId(self):
        r"""<p>应用Id，Scope=0 时为目标应用ID（必填）；scope=1 时无需填写</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FilterList(self):
        r"""<p>过滤条件（name: "SearchWord", "SpaceId", "AgentSource", "AppId"）</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageSize(self):
        r"""<p>每页数目</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNumber(self):
        r"""<p>页码</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._Scope = params.get("Scope")
        self._AppId = params.get("AppId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageSize = params.get("PageSize")
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAgentSummaryListResponse(AbstractModel):
    r"""DescribeAgentSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总数</p>
        :type TotalCount: int
        :param _AgentList: <p>Agent摘要信息</p>
        :type AgentList: list of AgentSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AgentList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AgentList(self):
        r"""<p>Agent摘要信息</p>
        :rtype: list of AgentSummary
        """
        return self._AgentList

    @AgentList.setter
    def AgentList(self, AgentList):
        self._AgentList = AgentList

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
        if params.get("AgentList") is not None:
            self._AgentList = []
            for item in params.get("AgentList"):
                obj = AgentSummary()
                obj._deserialize(item)
                self._AgentList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAppRequest(AbstractModel):
    r"""DescribeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Domain: <p>应用域: ADP_DOMAIN_DEV(1)=开发域, ADP_DOMAIN_PROD(2)=发布域。枚举值: 1:开发域, 2:生产域</p>
        :type Domain: int
        :param _FieldMask: <p>字段掩码，指定需要返回的字段(Paths为空则返回所有字段)。Paths枚举值：AppConfig(应用配置), SecretInfo(应用密钥信息), ShareUrlInfo(分享链接信息), SpecialStatusInfo(特殊状态信息), SearchResourceStatus(搜索资源状态), SharedKbList(应用引用的共享知识库列表),CorpShareConfig(企业共享配置)</p>
        :type FieldMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        :param _StatusType: <p>特殊状态类型(当FieldMask包含SpecialStatusInfo时必填)。枚举值: 1:回滚状态, 2:首次导入状态</p>
        :type StatusType: int
        """
        self._AppId = None
        self._Domain = None
        self._FieldMask = None
        self._StatusType = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        r"""<p>应用域: ADP_DOMAIN_DEV(1)=开发域, ADP_DOMAIN_PROD(2)=发布域。枚举值: 1:开发域, 2:生产域</p>
        :rtype: int
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def FieldMask(self):
        r"""<p>字段掩码，指定需要返回的字段(Paths为空则返回所有字段)。Paths枚举值：AppConfig(应用配置), SecretInfo(应用密钥信息), ShareUrlInfo(分享链接信息), SpecialStatusInfo(特殊状态信息), SearchResourceStatus(搜索资源状态), SharedKbList(应用引用的共享知识库列表),CorpShareConfig(企业共享配置)</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._FieldMask

    @FieldMask.setter
    def FieldMask(self, FieldMask):
        self._FieldMask = FieldMask

    @property
    def StatusType(self):
        r"""<p>特殊状态类型(当FieldMask包含SpecialStatusInfo时必填)。枚举值: 1:回滚状态, 2:首次导入状态</p>
        :rtype: int
        """
        return self._StatusType

    @StatusType.setter
    def StatusType(self, StatusType):
        self._StatusType = StatusType


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        if params.get("FieldMask") is not None:
            self._FieldMask = FieldMask()
            self._FieldMask._deserialize(params.get("FieldMask"))
        self._StatusType = params.get("StatusType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppResponse(AbstractModel):
    r"""DescribeApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _App: <p>应用详情</p>
        :type App: :class:`tencentcloud.adp.v20260520.models.App`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._App = None
        self._RequestId = None

    @property
    def App(self):
        r"""<p>应用详情</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.App`
        """
        return self._App

    @App.setter
    def App(self, App):
        self._App = App

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
        if params.get("App") is not None:
            self._App = App()
            self._App._deserialize(params.get("App"))
        self._RequestId = params.get("RequestId")


class DescribeAppSummaryListRequest(AbstractModel):
    r"""DescribeAppSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间ID(必填)
        :type SpaceId: str
        :param _FilterList: 过滤条件(多个Filter之间为AND关系,同一Filter的多个Values为OR关系): - AppStatus: 应用状态,枚举值,精确匹配(APP_STATUS_OFFLINE=1/APP_STATUS_RUNNING=2/APP_STATUS_DISABLED=3) - AppMode: 应用模式,枚举值,精确匹配(APP_MODE_STANDARD=1/APP_MODE_AGENT=2/APP_MODE_SINGLE_WORKFLOW=3/APP_MODE_CLAW_AGENT=4)
        :type FilterList: list of Filter
        :param _PageNumber: 页码(从0开始)
        :type PageNumber: int
        :param _PageSize: 每页数量(最大值:100)
        :type PageSize: int
        :param _Query: 模糊查询
        :type Query: str
        """
        self._SpaceId = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def SpaceId(self):
        r"""空间ID(必填)
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FilterList(self):
        r"""过滤条件(多个Filter之间为AND关系,同一Filter的多个Values为OR关系): - AppStatus: 应用状态,枚举值,精确匹配(APP_STATUS_OFFLINE=1/APP_STATUS_RUNNING=2/APP_STATUS_DISABLED=3) - AppMode: 应用模式,枚举值,精确匹配(APP_MODE_STANDARD=1/APP_MODE_AGENT=2/APP_MODE_SINGLE_WORKFLOW=3/APP_MODE_CLAW_AGENT=4)
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""页码(从0开始)
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量(最大值:100)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""模糊查询
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppSummaryListResponse(AbstractModel):
    r"""DescribeAppSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppSummaryList: 应用摘要列表
        :type AppSummaryList: list of AppSummary
        :param _TotalCount: total_count
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppSummaryList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AppSummaryList(self):
        r"""应用摘要列表
        :rtype: list of AppSummary
        """
        return self._AppSummaryList

    @AppSummaryList.setter
    def AppSummaryList(self, AppSummaryList):
        self._AppSummaryList = AppSummaryList

    @property
    def TotalCount(self):
        r"""total_count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("AppSummaryList") is not None:
            self._AppSummaryList = []
            for item in params.get("AppSummaryList"):
                obj = AppSummary()
                obj._deserialize(item)
                self._AppSummaryList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAppTriggerInstanceRequest(AbstractModel):
    r"""DescribeAppTriggerInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _InstanceId: <p>触发器运行实例ID</p>
        :type InstanceId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._InstanceId = None
        self._Scope = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def InstanceId(self):
        r"""<p>触发器运行实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._InstanceId = params.get("InstanceId")
        self._Scope = params.get("Scope")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppTriggerInstanceResponse(AbstractModel):
    r"""DescribeAppTriggerInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instance: <p>应用触发器实例</p>
        :type Instance: :class:`tencentcloud.adp.v20260520.models.AppTriggerInstance`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instance = None
        self._RequestId = None

    @property
    def Instance(self):
        r"""<p>应用触发器实例</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerInstance`
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

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
        if params.get("Instance") is not None:
            self._Instance = AppTriggerInstance()
            self._Instance._deserialize(params.get("Instance"))
        self._RequestId = params.get("RequestId")


class DescribeAppTriggerRequest(AbstractModel):
    r"""DescribeAppTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerId: <p>应用触发器ID</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._Scope = None
        self._TriggerId = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerId(self):
        r"""<p>应用触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Scope = params.get("Scope")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppTriggerResponse(AbstractModel):
    r"""DescribeAppTrigger返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Trigger: <p>应用触发器信息</p>
        :type Trigger: :class:`tencentcloud.adp.v20260520.models.AppTrigger`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Trigger = None
        self._RequestId = None

    @property
    def Trigger(self):
        r"""<p>应用触发器信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTrigger`
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

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
        if params.get("Trigger") is not None:
            self._Trigger = AppTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._RequestId = params.get("RequestId")


class DescribeAppTriggerRunLogListRequest(AbstractModel):
    r"""DescribeAppTriggerRunLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _FilterList: <p>过滤参数</p>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码</p><p>取值范围：[1, 1000000]</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数据量</p><p>取值范围：[1, 100]</p>
        :type PageSize: int
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerId: <p>应用触发器ID</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None
        self._Scope = None
        self._TriggerId = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FilterList(self):
        r"""<p>过滤参数</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码</p><p>取值范围：[1, 1000000]</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数据量</p><p>取值范围：[1, 100]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerId(self):
        r"""<p>应用触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Scope = params.get("Scope")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppTriggerRunLogListResponse(AbstractModel):
    r"""DescribeAppTriggerRunLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RunLogList: <p>日志列表</p>
        :type RunLogList: list of AppTriggerRunLog
        :param _TotalCount: <p>日志列表数量</p>
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RunLogList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RunLogList(self):
        r"""<p>日志列表</p>
        :rtype: list of AppTriggerRunLog
        """
        return self._RunLogList

    @RunLogList.setter
    def RunLogList(self, RunLogList):
        self._RunLogList = RunLogList

    @property
    def TotalCount(self):
        r"""<p>日志列表数量</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("RunLogList") is not None:
            self._RunLogList = []
            for item in params.get("RunLogList"):
                obj = AppTriggerRunLog()
                obj._deserialize(item)
                self._RunLogList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeAppTriggerSummaryListRequest(AbstractModel):
    r"""DescribeAppTriggerSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _FilterList: <p>参数过滤列表</p>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码</p><p>取值范围：[1, 1000000]</p>
        :type PageNumber: int
        :param _PageSize: <p>每页大小</p><p>取值范围：[1, 100]</p>
        :type PageSize: int
        :param _Query: <p>模糊查询字符串</p>
        :type Query: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._Scope = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FilterList(self):
        r"""<p>参数过滤列表</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码</p><p>取值范围：[1, 1000000]</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页大小</p><p>取值范围：[1, 100]</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""<p>模糊查询字符串</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._Scope = params.get("Scope")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppTriggerSummaryListResponse(AbstractModel):
    r"""DescribeAppTriggerSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>应用触发器数量</p>
        :type TotalCount: str
        :param _TriggerList: <p>应用触发器列表</p>
        :type TriggerList: list of AppTriggerSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TriggerList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>应用触发器数量</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TriggerList(self):
        r"""<p>应用触发器列表</p>
        :rtype: list of AppTriggerSummary
        """
        return self._TriggerList

    @TriggerList.setter
    def TriggerList(self, TriggerList):
        self._TriggerList = TriggerList

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
        if params.get("TriggerList") is not None:
            self._TriggerList = []
            for item in params.get("TriggerList"):
                obj = AppTriggerSummary()
                obj._deserialize(item)
                self._TriggerList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogListRequest(AbstractModel):
    r"""DescribeAuditLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>空间id</p>
        :type SpaceId: str
        :param _Limit: <p>每页数量</p><p>取值范围：[1, 100]</p>
        :type Limit: int
        :param _SearchAfter: <p>es查询起始位置</p><p>对应接口返回SearchAfter</p>
        :type SearchAfter: list of str
        :param _FilterList: <p>参数过滤</p><p>支持 Action,BizObject,Content<br>支持SpaceId,AccountUin,AppId(最多100个)<br>支持startTime,endTime(秒时间戳)</p>
        :type FilterList: list of Filter
        """
        self._SpaceId = None
        self._Limit = None
        self._SearchAfter = None
        self._FilterList = None

    @property
    def SpaceId(self):
        r"""<p>空间id</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Limit(self):
        r"""<p>每页数量</p><p>取值范围：[1, 100]</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchAfter(self):
        r"""<p>es查询起始位置</p><p>对应接口返回SearchAfter</p>
        :rtype: list of str
        """
        return self._SearchAfter

    @SearchAfter.setter
    def SearchAfter(self, SearchAfter):
        self._SearchAfter = SearchAfter

    @property
    def FilterList(self):
        r"""<p>参数过滤</p><p>支持 Action,BizObject,Content<br>支持SpaceId,AccountUin,AppId(最多100个)<br>支持startTime,endTime(秒时间戳)</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Limit = params.get("Limit")
        self._SearchAfter = params.get("SearchAfter")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogListResponse(AbstractModel):
    r"""DescribeAuditLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditLogList: <p>操作日志列表</p>
        :type AuditLogList: list of AuditLog
        :param _SearchAfter: <p>es查询起始位置</p><p>用于入参查询下一页</p>
        :type SearchAfter: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuditLogList = None
        self._SearchAfter = None
        self._RequestId = None

    @property
    def AuditLogList(self):
        r"""<p>操作日志列表</p>
        :rtype: list of AuditLog
        """
        return self._AuditLogList

    @AuditLogList.setter
    def AuditLogList(self, AuditLogList):
        self._AuditLogList = AuditLogList

    @property
    def SearchAfter(self):
        r"""<p>es查询起始位置</p><p>用于入参查询下一页</p>
        :rtype: list of str
        """
        return self._SearchAfter

    @SearchAfter.setter
    def SearchAfter(self, SearchAfter):
        self._SearchAfter = SearchAfter

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
        if params.get("AuditLogList") is not None:
            self._AuditLogList = []
            for item in params.get("AuditLogList"):
                obj = AuditLog()
                obj._deserialize(item)
                self._AuditLogList.append(obj)
        self._SearchAfter = params.get("SearchAfter")
        self._RequestId = params.get("RequestId")


class DescribeAuditLogMetaRequest(AbstractModel):
    r"""DescribeAuditLogMeta请求参数结构体

    """


class DescribeAuditLogMetaResponse(AbstractModel):
    r"""DescribeAuditLogMeta返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Actions: <p>操作类型列表</p>
        :type Actions: list of AuditLogMetaField
        :param _BizObjects: <p>操作对象列表</p>
        :type BizObjects: list of AuditLogMetaField
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Actions = None
        self._BizObjects = None
        self._RequestId = None

    @property
    def Actions(self):
        r"""<p>操作类型列表</p>
        :rtype: list of AuditLogMetaField
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def BizObjects(self):
        r"""<p>操作对象列表</p>
        :rtype: list of AuditLogMetaField
        """
        return self._BizObjects

    @BizObjects.setter
    def BizObjects(self, BizObjects):
        self._BizObjects = BizObjects

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
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = AuditLogMetaField()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("BizObjects") is not None:
            self._BizObjects = []
            for item in params.get("BizObjects"):
                obj = AuditLogMetaField()
                obj._deserialize(item)
                self._BizObjects.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeConcurrencyLimitDetailListRequest(AbstractModel):
    r"""DescribeConcurrencyLimitDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRange: <p>查询时间范围（Unix 秒）</p>
        :type TimeRange: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        :param _ViewScope: <p>视图范围：企业视图 / 空间视图/ 应用视图</p>
        :type ViewScope: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        :param _FilterList: <p>扩展过滤。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：concurrency_type（qpm_tpm/dedicated，默认 qpm_tpm）、model_name（必填）、space_id、app_id/resource_id/source_id（应用ID，多选）、metric_source_type（METRIC_SOURCE_TYPE_* 枚举名或整数）</p>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码，从 0 开始</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量，最大 100</p>
        :type PageSize: int
        """
        self._TimeRange = None
        self._ViewScope = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TimeRange(self):
        r"""<p>查询时间范围（Unix 秒）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def ViewScope(self):
        r"""<p>视图范围：企业视图 / 空间视图/ 应用视图</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        """
        return self._ViewScope

    @ViewScope.setter
    def ViewScope(self, ViewScope):
        self._ViewScope = ViewScope

    @property
    def FilterList(self):
        r"""<p>扩展过滤。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：concurrency_type（qpm_tpm/dedicated，默认 qpm_tpm）、model_name（必填）、space_id、app_id/resource_id/source_id（应用ID，多选）、metric_source_type（METRIC_SOURCE_TYPE_* 枚举名或整数）</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码，从 0 开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量，最大 100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("TimeRange") is not None:
            self._TimeRange = TimeRange()
            self._TimeRange._deserialize(params.get("TimeRange"))
        if params.get("ViewScope") is not None:
            self._ViewScope = ViewScope()
            self._ViewScope._deserialize(params.get("ViewScope"))
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConcurrencyLimitDetailListResponse(AbstractModel):
    r"""DescribeConcurrencyLimitDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConcurrencyLimitDetailList: <p>并发超限明细列表</p>
        :type ConcurrencyLimitDetailList: list of ConcurrencyLimitDetail
        :param _TotalCount: <p>总记录数，用于前端分页</p>
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConcurrencyLimitDetailList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConcurrencyLimitDetailList(self):
        r"""<p>并发超限明细列表</p>
        :rtype: list of ConcurrencyLimitDetail
        """
        return self._ConcurrencyLimitDetailList

    @ConcurrencyLimitDetailList.setter
    def ConcurrencyLimitDetailList(self, ConcurrencyLimitDetailList):
        self._ConcurrencyLimitDetailList = ConcurrencyLimitDetailList

    @property
    def TotalCount(self):
        r"""<p>总记录数，用于前端分页</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ConcurrencyLimitDetailList") is not None:
            self._ConcurrencyLimitDetailList = []
            for item in params.get("ConcurrencyLimitDetailList"):
                obj = ConcurrencyLimitDetail()
                obj._deserialize(item)
                self._ConcurrencyLimitDetailList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConsumptionDetailListRequest(AbstractModel):
    r"""DescribeConsumptionDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRange: <p>查询时间范围（Unix 秒）</p>
        :type TimeRange: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        :param _ViewScope: <p>视图范围：企业视图 / 空间视图</p>
        :type ViewScope: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        :param _FilterList: <p>扩展过滤。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：metric_source_type（METRIC_SOURCE_TYPE_* 或整数）、source_ids（多选来源ID）、resource_id/source_id（单选来源ID，source_ids 未传时生效）、space_id、user_id</p>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码，从 0 开始</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量，最大 100</p>
        :type PageSize: int
        """
        self._TimeRange = None
        self._ViewScope = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def TimeRange(self):
        r"""<p>查询时间范围（Unix 秒）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def ViewScope(self):
        r"""<p>视图范围：企业视图 / 空间视图</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        """
        return self._ViewScope

    @ViewScope.setter
    def ViewScope(self, ViewScope):
        self._ViewScope = ViewScope

    @property
    def FilterList(self):
        r"""<p>扩展过滤。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：metric_source_type（METRIC_SOURCE_TYPE_* 或整数）、source_ids（多选来源ID）、resource_id/source_id（单选来源ID，source_ids 未传时生效）、space_id、user_id</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码，从 0 开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量，最大 100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        if params.get("TimeRange") is not None:
            self._TimeRange = TimeRange()
            self._TimeRange._deserialize(params.get("TimeRange"))
        if params.get("ViewScope") is not None:
            self._ViewScope = ViewScope()
            self._ViewScope._deserialize(params.get("ViewScope"))
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConsumptionDetailListResponse(AbstractModel):
    r"""DescribeConsumptionDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConsumptionDetailList: <p>资源消耗明细列表</p>
        :type ConsumptionDetailList: list of ConsumptionDetail
        :param _TotalCount: <p>总记录数，用于前端分页</p>
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConsumptionDetailList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConsumptionDetailList(self):
        r"""<p>资源消耗明细列表</p>
        :rtype: list of ConsumptionDetail
        """
        return self._ConsumptionDetailList

    @ConsumptionDetailList.setter
    def ConsumptionDetailList(self, ConsumptionDetailList):
        self._ConsumptionDetailList = ConsumptionDetailList

    @property
    def TotalCount(self):
        r"""<p>总记录数，用于前端分页</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ConsumptionDetailList") is not None:
            self._ConsumptionDetailList = []
            for item in params.get("ConsumptionDetailList"):
                obj = ConsumptionDetail()
                obj._deserialize(item)
                self._ConsumptionDetailList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConversationListRequest(AbstractModel):
    r"""DescribeConversationList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: <p>会话类型，传 CONVERSATION_TYPE_UNSPECIFIED 表示全部 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _Keyword: <p>关键词</p>
        :type Keyword: str
        :param _Limit: <p>限制数目（整型），配合Offset使用</p>
        :type Limit: int
        :param _LoginSubAccountUin: <p>子账户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>主账户Uin</p>
        :type LoginUin: str
        :param _Offset: <p>偏移量（整型），配合Limit使用，从0开始</p>
        :type Offset: int
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        :param _AgentId: <p>用户端 AgentId，当需要查询基于用户端 AgentId 创建的会话时使用</p>
        :type AgentId: str
        """
        self._Type = None
        self._AppId = None
        self._AppKey = None
        self._Keyword = None
        self._Limit = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._Offset = None
        self._ShareCode = None
        self._UserId = None
        self._AgentId = None

    @property
    def Type(self):
        r"""<p>会话类型，传 CONVERSATION_TYPE_UNSPECIFIED 表示全部 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def Keyword(self):
        r"""<p>关键词</p>
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Limit(self):
        r"""<p>限制数目（整型），配合Offset使用</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LoginSubAccountUin(self):
        r"""<p>子账户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>主账户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def Offset(self):
        r"""<p>偏移量（整型），配合Limit使用，从0开始</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AgentId(self):
        r"""<p>用户端 AgentId，当需要查询基于用户端 AgentId 创建的会话时使用</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppId = params.get("AppId")
        self._AppKey = params.get("AppKey")
        self._Keyword = params.get("Keyword")
        self._Limit = params.get("Limit")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._Offset = params.get("Offset")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConversationListResponse(AbstractModel):
    r"""DescribeConversationList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConversationList: <p>会话列表</p>
        :type ConversationList: list of Conversation
        :param _Conversations: <p>会话列表</p>
        :type Conversations: list of Conversation
        :param _TotalCount: <p>总数</p>
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConversationList = None
        self._Conversations = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConversationList(self):
        r"""<p>会话列表</p>
        :rtype: list of Conversation
        """
        return self._ConversationList

    @ConversationList.setter
    def ConversationList(self, ConversationList):
        self._ConversationList = ConversationList

    @property
    def Conversations(self):
        r"""<p>会话列表</p>
        :rtype: list of Conversation
        """
        return self._Conversations

    @Conversations.setter
    def Conversations(self, Conversations):
        self._Conversations = Conversations

    @property
    def TotalCount(self):
        r"""<p>总数</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ConversationList") is not None:
            self._ConversationList = []
            for item in params.get("ConversationList"):
                obj = Conversation()
                obj._deserialize(item)
                self._ConversationList.append(obj)
        if params.get("Conversations") is not None:
            self._Conversations = []
            for item in params.get("Conversations"):
                obj = Conversation()
                obj._deserialize(item)
                self._Conversations.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeConversationMessageListRequest(AbstractModel):
    r"""DescribeConversationMessageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _Limit: <p>返回记录总数量，默认 10，最大 50。向前或向后查询时，不包含record_id指定记录的消息，查询方向中心向前后查询时，包含record_id指定的记录消息，返回记录数量为前后各limit / 2条，向上取整</p>
        :type Limit: int
        :param _LoginSubAccountUin: <p>子用户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>主用户Uin</p>
        :type LoginUin: str
        :param _RecordId: <p>查询锚点记录 ID</p>
        :type RecordId: str
        :param _RecordQueryDirection: <p>相对于 record_id 的查询方向 枚举值: 0-RECORD_QUERY_DIRECTION_UNSPECIFIED(未指定，兼容旧逻辑，默认向前查询), 1-RECORD_QUERY_DIRECTION_BACKWARD(从 record_id 向前查询更早的消息), 2-RECORD_QUERY_DIRECTION_FORWARD(从 record_id 向后查询更新的消息), 3-RECORD_QUERY_DIRECTION_BIDIRECTIONAL(以 record_id 为中心，同时向前后查询)</p>
        :type RecordQueryDirection: int
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        """
        self._ConversationId = None
        self._Type = None
        self._AppKey = None
        self._Limit = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._RecordId = None
        self._RecordQueryDirection = None
        self._ShareCode = None
        self._UserId = None

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def Limit(self):
        r"""<p>返回记录总数量，默认 10，最大 50。向前或向后查询时，不包含record_id指定记录的消息，查询方向中心向前后查询时，包含record_id指定的记录消息，返回记录数量为前后各limit / 2条，向上取整</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def LoginSubAccountUin(self):
        r"""<p>子用户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>主用户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def RecordId(self):
        r"""<p>查询锚点记录 ID</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordQueryDirection(self):
        r"""<p>相对于 record_id 的查询方向 枚举值: 0-RECORD_QUERY_DIRECTION_UNSPECIFIED(未指定，兼容旧逻辑，默认向前查询), 1-RECORD_QUERY_DIRECTION_BACKWARD(从 record_id 向前查询更早的消息), 2-RECORD_QUERY_DIRECTION_FORWARD(从 record_id 向后查询更新的消息), 3-RECORD_QUERY_DIRECTION_BIDIRECTIONAL(以 record_id 为中心，同时向前后查询)</p>
        :rtype: int
        """
        return self._RecordQueryDirection

    @RecordQueryDirection.setter
    def RecordQueryDirection(self, RecordQueryDirection):
        self._RecordQueryDirection = RecordQueryDirection

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ConversationId = params.get("ConversationId")
        self._Type = params.get("Type")
        self._AppKey = params.get("AppKey")
        self._Limit = params.get("Limit")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._RecordId = params.get("RecordId")
        self._RecordQueryDirection = params.get("RecordQueryDirection")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConversationMessageListResponse(AbstractModel):
    r"""DescribeConversationMessageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FirstRecordId: <p>第一个记录 ID</p>
        :type FirstRecordId: str
        :param _HasMoreAfter: <p>更新消息方向是否还有更多</p>
        :type HasMoreAfter: bool
        :param _HasMoreBefore: <p>更早消息方向是否还有更多</p>
        :type HasMoreBefore: bool
        :param _LastRecordId: <p>最后一个记录 ID</p>
        :type LastRecordId: str
        :param _MessageList: <p>消息列表</p>
        :type MessageList: list of ConversationMessage
        :param _Messages: <p>消息列表</p>
        :type Messages: list of ConversationMessage
        :param _RecordSummaryList: <p>单次对话记录统计列表，与 message_list 通过 record_id / related_record_id 关联</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordSummaryList: list of ConversationRecordSummary
        :param _ResetInfo: <p>最近一次重置信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResetInfo: :class:`tencentcloud.adp.v20260520.models.ConversationResetInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FirstRecordId = None
        self._HasMoreAfter = None
        self._HasMoreBefore = None
        self._LastRecordId = None
        self._MessageList = None
        self._Messages = None
        self._RecordSummaryList = None
        self._ResetInfo = None
        self._RequestId = None

    @property
    def FirstRecordId(self):
        r"""<p>第一个记录 ID</p>
        :rtype: str
        """
        return self._FirstRecordId

    @FirstRecordId.setter
    def FirstRecordId(self, FirstRecordId):
        self._FirstRecordId = FirstRecordId

    @property
    def HasMoreAfter(self):
        r"""<p>更新消息方向是否还有更多</p>
        :rtype: bool
        """
        return self._HasMoreAfter

    @HasMoreAfter.setter
    def HasMoreAfter(self, HasMoreAfter):
        self._HasMoreAfter = HasMoreAfter

    @property
    def HasMoreBefore(self):
        r"""<p>更早消息方向是否还有更多</p>
        :rtype: bool
        """
        return self._HasMoreBefore

    @HasMoreBefore.setter
    def HasMoreBefore(self, HasMoreBefore):
        self._HasMoreBefore = HasMoreBefore

    @property
    def LastRecordId(self):
        r"""<p>最后一个记录 ID</p>
        :rtype: str
        """
        return self._LastRecordId

    @LastRecordId.setter
    def LastRecordId(self, LastRecordId):
        self._LastRecordId = LastRecordId

    @property
    def MessageList(self):
        r"""<p>消息列表</p>
        :rtype: list of ConversationMessage
        """
        return self._MessageList

    @MessageList.setter
    def MessageList(self, MessageList):
        self._MessageList = MessageList

    @property
    def Messages(self):
        warnings.warn("parameter `Messages` is deprecated", DeprecationWarning) 

        r"""<p>消息列表</p>
        :rtype: list of ConversationMessage
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        warnings.warn("parameter `Messages` is deprecated", DeprecationWarning) 

        self._Messages = Messages

    @property
    def RecordSummaryList(self):
        r"""<p>单次对话记录统计列表，与 message_list 通过 record_id / related_record_id 关联</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ConversationRecordSummary
        """
        return self._RecordSummaryList

    @RecordSummaryList.setter
    def RecordSummaryList(self, RecordSummaryList):
        self._RecordSummaryList = RecordSummaryList

    @property
    def ResetInfo(self):
        r"""<p>最近一次重置信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationResetInfo`
        """
        return self._ResetInfo

    @ResetInfo.setter
    def ResetInfo(self, ResetInfo):
        self._ResetInfo = ResetInfo

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
        self._FirstRecordId = params.get("FirstRecordId")
        self._HasMoreAfter = params.get("HasMoreAfter")
        self._HasMoreBefore = params.get("HasMoreBefore")
        self._LastRecordId = params.get("LastRecordId")
        if params.get("MessageList") is not None:
            self._MessageList = []
            for item in params.get("MessageList"):
                obj = ConversationMessage()
                obj._deserialize(item)
                self._MessageList.append(obj)
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = ConversationMessage()
                obj._deserialize(item)
                self._Messages.append(obj)
        if params.get("RecordSummaryList") is not None:
            self._RecordSummaryList = []
            for item in params.get("RecordSummaryList"):
                obj = ConversationRecordSummary()
                obj._deserialize(item)
                self._RecordSummaryList.append(obj)
        if params.get("ResetInfo") is not None:
            self._ResetInfo = ConversationResetInfo()
            self._ResetInfo._deserialize(params.get("ResetInfo"))
        self._RequestId = params.get("RequestId")


class DescribeConversationRequest(AbstractModel):
    r"""DescribeConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>主用户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>子用户Uin</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        """
        self._ConversationId = None
        self._Type = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None
        self._UserId = None

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>主用户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>子用户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ConversationId = params.get("ConversationId")
        self._Type = params.get("Type")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeConversationResponse(AbstractModel):
    r"""DescribeConversation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _CreateTime: <p>创建时间</p>
        :type CreateTime: str
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _UpdateTime: <p>更新时间</p>
        :type UpdateTime: str
        :param _Workspace: <p>工作空间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Workspace: :class:`tencentcloud.adp.v20260520.models.ConversationWorkspace`
        :param _Title: <p>会话标题</p>
        :type Title: str
        :param _AgentId: <p>会话使用的用户端 AgentId</p>
        :type AgentId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._ConversationId = None
        self._CreateTime = None
        self._Type = None
        self._UpdateTime = None
        self._Workspace = None
        self._Title = None
        self._AgentId = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def CreateTime(self):
        r"""<p>创建时间</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UpdateTime(self):
        r"""<p>更新时间</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Workspace(self):
        r"""<p>工作空间</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ConversationWorkspace`
        """
        return self._Workspace

    @Workspace.setter
    def Workspace(self, Workspace):
        self._Workspace = Workspace

    @property
    def Title(self):
        r"""<p>会话标题</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def AgentId(self):
        r"""<p>会话使用的用户端 AgentId</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

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
        self._AppId = params.get("AppId")
        self._ConversationId = params.get("ConversationId")
        self._CreateTime = params.get("CreateTime")
        self._Type = params.get("Type")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Workspace") is not None:
            self._Workspace = ConversationWorkspace()
            self._Workspace._deserialize(params.get("Workspace"))
        self._Title = params.get("Title")
        self._AgentId = params.get("AgentId")
        self._RequestId = params.get("RequestId")


class DescribeLatestReleaseRequest(AbstractModel):
    r"""DescribeLatestRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        """
        self._AppId = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLatestReleaseResponse(AbstractModel):
    r"""DescribeLatestRelease返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsChanged: 是否有发布变更
        :type IsChanged: bool
        :param _ReleaseSummary: 发布信息
        :type ReleaseSummary: :class:`tencentcloud.adp.v20260520.models.ReleaseSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsChanged = None
        self._ReleaseSummary = None
        self._RequestId = None

    @property
    def IsChanged(self):
        r"""是否有发布变更
        :rtype: bool
        """
        return self._IsChanged

    @IsChanged.setter
    def IsChanged(self, IsChanged):
        self._IsChanged = IsChanged

    @property
    def ReleaseSummary(self):
        r"""发布信息
        :rtype: :class:`tencentcloud.adp.v20260520.models.ReleaseSummary`
        """
        return self._ReleaseSummary

    @ReleaseSummary.setter
    def ReleaseSummary(self, ReleaseSummary):
        self._ReleaseSummary = ReleaseSummary

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
        self._IsChanged = params.get("IsChanged")
        if params.get("ReleaseSummary") is not None:
            self._ReleaseSummary = ReleaseSummary()
            self._ReleaseSummary._deserialize(params.get("ReleaseSummary"))
        self._RequestId = params.get("RequestId")


class DescribeMetricOverviewListRequest(AbstractModel):
    r"""DescribeMetricOverviewList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: <p>看板域，必填，决定返回哪个域的 KPI 数据</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>RESOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>RESOURCE_TYPE_MODEL</td><td>1</td><td>模型用量</td></tr><tr><td>RESOURCE_TYPE_PLUGIN</td><td>2</td><td>插件用量</td></tr><tr><td>RESOURCE_TYPE_PLATFORM</td><td>3</td><td>平台功能用量</td></tr><tr><td>RESOURCE_TYPE_MODEL_CONCURRENCY</td><td>4</td><td>模型并发超限</td></tr><tr><td>RESOURCE_TYPE_KB_CAPACITY</td><td>5</td><td>知识库容量</td></tr><tr><td>RESOURCE_TYPE_USAGE_SUMMARY</td><td>6</td><td>用量汇总</td></tr><tr><td>RESOURCE_TYPE_RESOURCE_CONSUME</td><td>7</td><td>资源消耗（计费明细）</td></tr></tbody></table>
        :type ResourceType: int
        :param _TimeRange: <p>查询时间范围（Unix 秒）</p>
        :type TimeRange: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        :param _ViewScope: <p>视图范围：企业视图 / 空间视图</p>
        :type ViewScope: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        :param _FilterList: <p>扩展过滤（resource_type=MODEL）。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：model_name（模型名）、user_id（用户ID）、space_id（空间ID）、resource_id/source_id（来源ID）、metric_source_type（METRIC_SOURCE_TYPE_* 枚举名或整数）</p>
        :type FilterList: list of Filter
        """
        self._ResourceType = None
        self._TimeRange = None
        self._ViewScope = None
        self._FilterList = None

    @property
    def ResourceType(self):
        r"""<p>看板域，必填，决定返回哪个域的 KPI 数据</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>RESOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>RESOURCE_TYPE_MODEL</td><td>1</td><td>模型用量</td></tr><tr><td>RESOURCE_TYPE_PLUGIN</td><td>2</td><td>插件用量</td></tr><tr><td>RESOURCE_TYPE_PLATFORM</td><td>3</td><td>平台功能用量</td></tr><tr><td>RESOURCE_TYPE_MODEL_CONCURRENCY</td><td>4</td><td>模型并发超限</td></tr><tr><td>RESOURCE_TYPE_KB_CAPACITY</td><td>5</td><td>知识库容量</td></tr><tr><td>RESOURCE_TYPE_USAGE_SUMMARY</td><td>6</td><td>用量汇总</td></tr><tr><td>RESOURCE_TYPE_RESOURCE_CONSUME</td><td>7</td><td>资源消耗（计费明细）</td></tr></tbody></table>
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def TimeRange(self):
        r"""<p>查询时间范围（Unix 秒）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def ViewScope(self):
        r"""<p>视图范围：企业视图 / 空间视图</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        """
        return self._ViewScope

    @ViewScope.setter
    def ViewScope(self, ViewScope):
        self._ViewScope = ViewScope

    @property
    def FilterList(self):
        r"""<p>扩展过滤（resource_type=MODEL）。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：model_name（模型名）、user_id（用户ID）、space_id（空间ID）、resource_id/source_id（来源ID）、metric_source_type（METRIC_SOURCE_TYPE_* 枚举名或整数）</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("TimeRange") is not None:
            self._TimeRange = TimeRange()
            self._TimeRange._deserialize(params.get("TimeRange"))
        if params.get("ViewScope") is not None:
            self._ViewScope = ViewScope()
            self._ViewScope._deserialize(params.get("ViewScope"))
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMetricOverviewListResponse(AbstractModel):
    r"""DescribeMetricOverviewList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MetricList: <p>所有域 Overview 统一出参：KPI 卡片列表，key 字符串标识指标，客户端按 resource_type 解析；key 白名单参考 platform.common.v2.MetricOverview 注释</p>
        :type MetricList: list of MetricOverview
        :param _TotalCount: <p>总记录数，等于 MetricList 长度，仅为列表接口一致性预留</p>
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MetricList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def MetricList(self):
        r"""<p>所有域 Overview 统一出参：KPI 卡片列表，key 字符串标识指标，客户端按 resource_type 解析；key 白名单参考 platform.common.v2.MetricOverview 注释</p>
        :rtype: list of MetricOverview
        """
        return self._MetricList

    @MetricList.setter
    def MetricList(self, MetricList):
        self._MetricList = MetricList

    @property
    def TotalCount(self):
        r"""<p>总记录数，等于 MetricList 长度，仅为列表接口一致性预留</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("MetricList") is not None:
            self._MetricList = []
            for item in params.get("MetricList"):
                obj = MetricOverview()
                obj._deserialize(item)
                self._MetricList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeModelListRequest(AbstractModel):
    r"""DescribeModelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelScene: <p>模型场景。0-不区分场景, 1-标准生成, 2-标准思考, 3-Agent思考, 4-多模态理解, 5-多模态问答, 6-改写, 7-长期记忆, 8-自然语言转SQL, 9-AI优化, 10-实时文件解析, 11-文件解析, 12-GraphRAG, 13-OpenClaw, 14-多模态Embedding, 15-Rerank, 16-文本Embedding, 17-Widget, 18-Claw模式, 19-工作流代码生成, 20-工作流大模型节点, 21-工作流节点专用向量化, 22-工作流参数提取, 23-工作流大模型知识问答, 24-工作流标签提取, 25-工作流意图识别, 26-工作流选项卡, 27-工作流逻辑判断, 28-文档生成问答, 29-知识库Schema</p><p>枚举值：</p><ul><li>0： 不区分场景</li><li>1： 标准生成</li><li>2： 标准思考</li><li>3： Agent思考</li><li>4： 多模态理解</li><li>5： 多模态问答</li><li>6： 改写</li><li>7： 长期记忆</li><li>8： 自然语言转SQL</li><li>9： AI优化</li><li>10： 实时文件解析</li><li>11： 文件解析</li><li>12： GraphRAG</li><li>13： OpenClaw</li><li>14： 多模态Embedding</li><li>15： Rerank</li><li>16： 文本Embedding</li><li>17： Widget</li><li>18： Claw模式</li><li>19： 工作流代码生成</li><li>20： 工作流大模型节点</li><li>21： 工作流节点专用向量化</li><li>22： 工作流参数提取</li><li>23： 工作流大模型知识问答</li><li>24： 工作流标签提取</li><li>25： 工作流意图识别</li><li>26： 工作流选项卡</li><li>27： 工作流逻辑判断</li><li>28： 文档生成问答</li><li>29： 知识库Schema</li></ul>
        :type ModelScene: int
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        :param _Query: <p>关键词模糊搜索</p>
        :type Query: str
        :param _PageNumber: <p>页码。从0开始</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量，默认20，最大100</p>
        :type PageSize: int
        :param _FilterList: <p>过滤条件(多个 Filter 之间为 AND, 同一 Filter 多 Values 为 OR)<br>DeveloperName： 模型作者名称<br>ProviderName： 模型提供商名称<br>ProviderType：模型提供商类型</p>
        :type FilterList: list of Filter
        """
        self._ModelScene = None
        self._SpaceId = None
        self._Query = None
        self._PageNumber = None
        self._PageSize = None
        self._FilterList = None

    @property
    def ModelScene(self):
        r"""<p>模型场景。0-不区分场景, 1-标准生成, 2-标准思考, 3-Agent思考, 4-多模态理解, 5-多模态问答, 6-改写, 7-长期记忆, 8-自然语言转SQL, 9-AI优化, 10-实时文件解析, 11-文件解析, 12-GraphRAG, 13-OpenClaw, 14-多模态Embedding, 15-Rerank, 16-文本Embedding, 17-Widget, 18-Claw模式, 19-工作流代码生成, 20-工作流大模型节点, 21-工作流节点专用向量化, 22-工作流参数提取, 23-工作流大模型知识问答, 24-工作流标签提取, 25-工作流意图识别, 26-工作流选项卡, 27-工作流逻辑判断, 28-文档生成问答, 29-知识库Schema</p><p>枚举值：</p><ul><li>0： 不区分场景</li><li>1： 标准生成</li><li>2： 标准思考</li><li>3： Agent思考</li><li>4： 多模态理解</li><li>5： 多模态问答</li><li>6： 改写</li><li>7： 长期记忆</li><li>8： 自然语言转SQL</li><li>9： AI优化</li><li>10： 实时文件解析</li><li>11： 文件解析</li><li>12： GraphRAG</li><li>13： OpenClaw</li><li>14： 多模态Embedding</li><li>15： Rerank</li><li>16： 文本Embedding</li><li>17： Widget</li><li>18： Claw模式</li><li>19： 工作流代码生成</li><li>20： 工作流大模型节点</li><li>21： 工作流节点专用向量化</li><li>22： 工作流参数提取</li><li>23： 工作流大模型知识问答</li><li>24： 工作流标签提取</li><li>25： 工作流意图识别</li><li>26： 工作流选项卡</li><li>27： 工作流逻辑判断</li><li>28： 文档生成问答</li><li>29： 知识库Schema</li></ul>
        :rtype: int
        """
        return self._ModelScene

    @ModelScene.setter
    def ModelScene(self, ModelScene):
        self._ModelScene = ModelScene

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Query(self):
        r"""<p>关键词模糊搜索</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def PageNumber(self):
        r"""<p>页码。从0开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量，默认20，最大100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def FilterList(self):
        r"""<p>过滤条件(多个 Filter 之间为 AND, 同一 Filter 多 Values 为 OR)<br>DeveloperName： 模型作者名称<br>ProviderName： 模型提供商名称<br>ProviderType：模型提供商类型</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList


    def _deserialize(self, params):
        self._ModelScene = params.get("ModelScene")
        self._SpaceId = params.get("SpaceId")
        self._Query = params.get("Query")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModelListResponse(AbstractModel):
    r"""DescribeModelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ModelList: <p>模型列表</p>
        :type ModelList: list of Model
        :param _TotalCount: <p>模型总数</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ModelList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ModelList(self):
        r"""<p>模型列表</p>
        :rtype: list of Model
        """
        return self._ModelList

    @ModelList.setter
    def ModelList(self, ModelList):
        self._ModelList = ModelList

    @property
    def TotalCount(self):
        r"""<p>模型总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ModelList") is not None:
            self._ModelList = []
            for item in params.get("ModelList"):
                obj = Model()
                obj._deserialize(item)
                self._ModelList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeMsgRecordCategoryListRequest(AbstractModel):
    r"""DescribeMsgRecordCategoryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        """
        self._AppId = None

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMsgRecordCategoryListResponse(AbstractModel):
    r"""DescribeMsgRecordCategoryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryList: <p>消息记录分类树列表</p>
        :type CategoryList: list of MsgRecordCategory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryList = None
        self._RequestId = None

    @property
    def CategoryList(self):
        r"""<p>消息记录分类树列表</p>
        :rtype: list of MsgRecordCategory
        """
        return self._CategoryList

    @CategoryList.setter
    def CategoryList(self, CategoryList):
        self._CategoryList = CategoryList

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
        if params.get("CategoryList") is not None:
            self._CategoryList = []
            for item in params.get("CategoryList"):
                obj = MsgRecordCategory()
                obj._deserialize(item)
                self._CategoryList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMsgRecordListRequest(AbstractModel):
    r"""DescribeMsgRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _FilterList: <ul><li><strong>ChannelType</strong> :   0-表示全部 2-体验页面（腾讯云）3-调试页面（腾讯云）4-体验页面（手机号）5-对话端API接入 6-应用评测 7-调试API&#39; 10000-微信服务号 10001-微信订阅号 10002-企微应用 10004-微信客服 10005-微信小程序 10006-腾讯元器 10007-应用宝 10009-企微智能机器人 10014-企微智能机器人 10011-LINE 10012-Telegram 10013-钉钉机器人 10016-飞书机器人 30000-定时任务 30001-触发器 </li><li><strong>FeedbackType</strong> :   反馈类型，-1-表示全部 0-未评价 1-点赞 2-点踩 </li><li><strong>QueryType</strong> :    检索类型（按平台约定取值）, SessionId-sessionID Question-问题  Answer-回复 Intent-意图 User-用户 </li><li><strong>Query</strong> : 对应QueryType输入的过滤条件 </li><li><strong>CategoryId</strong> :  分类ID </li><li><strong>ReplyMethod</strong> :  回复类型 0-全部回复类型  1-拒答问题回复 2-问答直接回复 3-审核失败回复 4-知识润色回复 6-工作流回复 8-图片理解回复 9-搜索引擎回复 10-大模型直接回复 11-兜底回复 </li><li><strong>StartTime</strong> : 开始时间，秒级时间戳 </li><li><strong>EndTime</strong>:  结束时间，秒级时间戳 </li><li><strong>Cursor</strong> : 游标信息，上一页取响应 PrevCursor，下一页取响应 NextCursor  </li><li><strong>Direction</strong> : 方向，next 下一页，prev 上一页</li><li><strong>CallResult</strong> : 调用结果：0 全部 / 1 成功 / 2 失败 / 3 用户取消 &lt;</li><li><strong>FailReason</strong> : 失败原因 0-全部  1-审核失败 2-达到QPM上限 3-达到TPM上限 4-达到并发上限  5-系统异常 </li><li><strong>Intent</strong> :  意图</li></ul>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码，从 0 开始；不传时按 0 处理</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量，最大 100；不传或传 0 时按默认分页大小处理</p>
        :type PageSize: int
        :param _Sort: <p>排序条件，只支持按 CreateTime 排序</p>
        :type Sort: :class:`tencentcloud.adp.v20260520.models.Sort`
        """
        self._AppId = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None
        self._Sort = None

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FilterList(self):
        r"""<ul><li><strong>ChannelType</strong> :   0-表示全部 2-体验页面（腾讯云）3-调试页面（腾讯云）4-体验页面（手机号）5-对话端API接入 6-应用评测 7-调试API&#39; 10000-微信服务号 10001-微信订阅号 10002-企微应用 10004-微信客服 10005-微信小程序 10006-腾讯元器 10007-应用宝 10009-企微智能机器人 10014-企微智能机器人 10011-LINE 10012-Telegram 10013-钉钉机器人 10016-飞书机器人 30000-定时任务 30001-触发器 </li><li><strong>FeedbackType</strong> :   反馈类型，-1-表示全部 0-未评价 1-点赞 2-点踩 </li><li><strong>QueryType</strong> :    检索类型（按平台约定取值）, SessionId-sessionID Question-问题  Answer-回复 Intent-意图 User-用户 </li><li><strong>Query</strong> : 对应QueryType输入的过滤条件 </li><li><strong>CategoryId</strong> :  分类ID </li><li><strong>ReplyMethod</strong> :  回复类型 0-全部回复类型  1-拒答问题回复 2-问答直接回复 3-审核失败回复 4-知识润色回复 6-工作流回复 8-图片理解回复 9-搜索引擎回复 10-大模型直接回复 11-兜底回复 </li><li><strong>StartTime</strong> : 开始时间，秒级时间戳 </li><li><strong>EndTime</strong>:  结束时间，秒级时间戳 </li><li><strong>Cursor</strong> : 游标信息，上一页取响应 PrevCursor，下一页取响应 NextCursor  </li><li><strong>Direction</strong> : 方向，next 下一页，prev 上一页</li><li><strong>CallResult</strong> : 调用结果：0 全部 / 1 成功 / 2 失败 / 3 用户取消 &lt;</li><li><strong>FailReason</strong> : 失败原因 0-全部  1-审核失败 2-达到QPM上限 3-达到TPM上限 4-达到并发上限  5-系统异常 </li><li><strong>Intent</strong> :  意图</li></ul>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码，从 0 开始；不传时按 0 处理</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量，最大 100；不传或传 0 时按默认分页大小处理</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Sort(self):
        r"""<p>排序条件，只支持按 CreateTime 排序</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMsgRecordListResponse(AbstractModel):
    r"""DescribeMsgRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HasMore: <p>是否有更多页</p>
        :type HasMore: bool
        :param _MsgRecordList: <p>消息记录列表</p>
        :type MsgRecordList: list of MsgRecord
        :param _NextCursor: <p>下一页游标信息</p>
        :type NextCursor: str
        :param _PrevCursor: <p>上一页游标信息</p>
        :type PrevCursor: str
        :param _TotalCount: <p>符合条件的总记录数，用于前端分页显示</p>
        :type TotalCount: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HasMore = None
        self._MsgRecordList = None
        self._NextCursor = None
        self._PrevCursor = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HasMore(self):
        r"""<p>是否有更多页</p>
        :rtype: bool
        """
        return self._HasMore

    @HasMore.setter
    def HasMore(self, HasMore):
        self._HasMore = HasMore

    @property
    def MsgRecordList(self):
        r"""<p>消息记录列表</p>
        :rtype: list of MsgRecord
        """
        return self._MsgRecordList

    @MsgRecordList.setter
    def MsgRecordList(self, MsgRecordList):
        self._MsgRecordList = MsgRecordList

    @property
    def NextCursor(self):
        r"""<p>下一页游标信息</p>
        :rtype: str
        """
        return self._NextCursor

    @NextCursor.setter
    def NextCursor(self, NextCursor):
        self._NextCursor = NextCursor

    @property
    def PrevCursor(self):
        r"""<p>上一页游标信息</p>
        :rtype: str
        """
        return self._PrevCursor

    @PrevCursor.setter
    def PrevCursor(self, PrevCursor):
        self._PrevCursor = PrevCursor

    @property
    def TotalCount(self):
        r"""<p>符合条件的总记录数，用于前端分页显示</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._HasMore = params.get("HasMore")
        if params.get("MsgRecordList") is not None:
            self._MsgRecordList = []
            for item in params.get("MsgRecordList"):
                obj = MsgRecord()
                obj._deserialize(item)
                self._MsgRecordList.append(obj)
        self._NextCursor = params.get("NextCursor")
        self._PrevCursor = params.get("PrevCursor")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePluginRequest(AbstractModel):
    r"""DescribePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _SpaceId: <p>当前空间id</p>
        :type SpaceId: str
        :param _FieldMask: <p>获取指定字段</p>
        :type FieldMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        :param _Module: <p>插件展示场景。不传或取 0 时不限定场景。</p><p>枚举值：</p><ul><li>0：不限定场景</li><li>1：Agent 模式</li><li>2：工作流</li><li>3：智能工作台</li></ul>
        :type Module: int
        """
        self._PluginId = None
        self._SpaceId = None
        self._FieldMask = None
        self._Module = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def SpaceId(self):
        r"""<p>当前空间id</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FieldMask(self):
        r"""<p>获取指定字段</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._FieldMask

    @FieldMask.setter
    def FieldMask(self, FieldMask):
        self._FieldMask = FieldMask

    @property
    def Module(self):
        r"""<p>插件展示场景。不传或取 0 时不限定场景。</p><p>枚举值：</p><ul><li>0：不限定场景</li><li>1：Agent 模式</li><li>2：工作流</li><li>3：智能工作台</li></ul>
        :rtype: int
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._SpaceId = params.get("SpaceId")
        if params.get("FieldMask") is not None:
            self._FieldMask = FieldMask()
            self._FieldMask._deserialize(params.get("FieldMask"))
        self._Module = params.get("Module")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginResponse(AbstractModel):
    r"""DescribePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plugin: <p>插件详情</p>
        :type Plugin: :class:`tencentcloud.adp.v20260520.models.Plugin`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plugin = None
        self._RequestId = None

    @property
    def Plugin(self):
        r"""<p>插件详情</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.Plugin`
        """
        return self._Plugin

    @Plugin.setter
    def Plugin(self, Plugin):
        self._Plugin = Plugin

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
        if params.get("Plugin") is not None:
            self._Plugin = Plugin()
            self._Plugin._deserialize(params.get("Plugin"))
        self._RequestId = params.get("RequestId")


class DescribePluginSummaryListRequest(AbstractModel):
    r"""DescribePluginSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间ID，查询空间内的插件列表时使用
        :type SpaceId: str
        :param _FilterList: 过滤条件列表 支持：PluginKind、CategoryKey、PluginSource、PluginId、PluginClass、BillingType
        :type FilterList: list of Filter
        :param _IsFavoriteOnly: <p>是否只返回已收藏插件。取 true 时，仅返回当前用户已收藏的插件；取 false 或不传时不按收藏状态过滤。</p>
        :type IsFavoriteOnly: bool
        :param _Module: <p>插件展示场景。不传或取 0 时不限定场景。</p><p>枚举值：</p><ul><li>0：不限定场景</li><li>1：Agent 模式</li><li>2：工作流</li><li>3：智能工作台</li></ul>
        :type Module: int
        :param _PageNumber: 页码 从0开始
        :type PageNumber: int
        :param _PageSize: 每页大小
        :type PageSize: int
        :param _Query: 查询内容 模糊匹配：插件名称/插件描述/工具名称/工具描述
        :type Query: str
        :param _SortType: <p>排序方式。</p><p>枚举值：</p><ul><li>0：未指定，默认排序</li><li>1：按相关性排序</li><li>2：按更新时间排序</li><li>3：默认排序</li><li>4：按热度排序</li></ul>
        :type SortType: int
        """
        self._SpaceId = None
        self._FilterList = None
        self._IsFavoriteOnly = None
        self._Module = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None
        self._SortType = None

    @property
    def SpaceId(self):
        r"""空间ID，查询空间内的插件列表时使用
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FilterList(self):
        r"""过滤条件列表 支持：PluginKind、CategoryKey、PluginSource、PluginId、PluginClass、BillingType
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def IsFavoriteOnly(self):
        r"""<p>是否只返回已收藏插件。取 true 时，仅返回当前用户已收藏的插件；取 false 或不传时不按收藏状态过滤。</p>
        :rtype: bool
        """
        return self._IsFavoriteOnly

    @IsFavoriteOnly.setter
    def IsFavoriteOnly(self, IsFavoriteOnly):
        self._IsFavoriteOnly = IsFavoriteOnly

    @property
    def Module(self):
        r"""<p>插件展示场景。不传或取 0 时不限定场景。</p><p>枚举值：</p><ul><li>0：不限定场景</li><li>1：Agent 模式</li><li>2：工作流</li><li>3：智能工作台</li></ul>
        :rtype: int
        """
        return self._Module

    @Module.setter
    def Module(self, Module):
        self._Module = Module

    @property
    def PageNumber(self):
        r"""页码 从0开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询内容 模糊匹配：插件名称/插件描述/工具名称/工具描述
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def SortType(self):
        r"""<p>排序方式。</p><p>枚举值：</p><ul><li>0：未指定，默认排序</li><li>1：按相关性排序</li><li>2：按更新时间排序</li><li>3：默认排序</li><li>4：按热度排序</li></ul>
        :rtype: int
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._IsFavoriteOnly = params.get("IsFavoriteOnly")
        self._Module = params.get("Module")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        self._SortType = params.get("SortType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginSummaryListResponse(AbstractModel):
    r"""DescribePluginSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginList: plugin_list
        :type PluginList: list of PluginSummary
        :param _TotalCount: total_count
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PluginList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PluginList(self):
        r"""plugin_list
        :rtype: list of PluginSummary
        """
        return self._PluginList

    @PluginList.setter
    def PluginList(self, PluginList):
        self._PluginList = PluginList

    @property
    def TotalCount(self):
        r"""total_count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("PluginList") is not None:
            self._PluginList = []
            for item in params.get("PluginList"):
                obj = PluginSummary()
                obj._deserialize(item)
                self._PluginList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeReleaseListRequest(AbstractModel):
    r"""DescribeReleaseList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _PageNumber: 页码(从0开始)
        :type PageNumber: int
        :param _PageSize: 每页数量(最大值:100)
        :type PageSize: int
        """
        self._AppId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def PageNumber(self):
        r"""页码(从0开始)
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量(最大值:100)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseListResponse(AbstractModel):
    r"""DescribeReleaseList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReleaseList: release_list
        :type ReleaseList: list of ReleaseRecord
        :param _TotalCount: total_count
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReleaseList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ReleaseList(self):
        r"""release_list
        :rtype: list of ReleaseRecord
        """
        return self._ReleaseList

    @ReleaseList.setter
    def ReleaseList(self, ReleaseList):
        self._ReleaseList = ReleaseList

    @property
    def TotalCount(self):
        r"""total_count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("ReleaseList") is not None:
            self._ReleaseList = []
            for item in params.get("ReleaseList"):
                obj = ReleaseRecord()
                obj._deserialize(item)
                self._ReleaseList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeReleaseSummaryRequest(AbstractModel):
    r"""DescribeReleaseSummary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _ReleaseId: release_id
        :type ReleaseId: str
        """
        self._AppId = None
        self._ReleaseId = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ReleaseId(self):
        r"""release_id
        :rtype: str
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ReleaseId = params.get("ReleaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReleaseSummaryResponse(AbstractModel):
    r"""DescribeReleaseSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReleaseSummary: 发布信息
        :type ReleaseSummary: :class:`tencentcloud.adp.v20260520.models.ReleaseSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReleaseSummary = None
        self._RequestId = None

    @property
    def ReleaseSummary(self):
        r"""发布信息
        :rtype: :class:`tencentcloud.adp.v20260520.models.ReleaseSummary`
        """
        return self._ReleaseSummary

    @ReleaseSummary.setter
    def ReleaseSummary(self, ReleaseSummary):
        self._ReleaseSummary = ReleaseSummary

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
        if params.get("ReleaseSummary") is not None:
            self._ReleaseSummary = ReleaseSummary()
            self._ReleaseSummary._deserialize(params.get("ReleaseSummary"))
        self._RequestId = params.get("RequestId")


class DescribeSkillCategoryListRequest(AbstractModel):
    r"""DescribeSkillCategoryList请求参数结构体

    """


class DescribeSkillCategoryListResponse(AbstractModel):
    r"""DescribeSkillCategoryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CategoryList: Skill 分类列表
        :type CategoryList: list of SkillCategory
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CategoryList = None
        self._RequestId = None

    @property
    def CategoryList(self):
        r"""Skill 分类列表
        :rtype: list of SkillCategory
        """
        return self._CategoryList

    @CategoryList.setter
    def CategoryList(self, CategoryList):
        self._CategoryList = CategoryList

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
        if params.get("CategoryList") is not None:
            self._CategoryList = []
            for item in params.get("CategoryList"):
                obj = SkillCategory()
                obj._deserialize(item)
                self._CategoryList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSkillDetailRequest(AbstractModel):
    r"""DescribeSkillDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: skillID
        :type SkillId: str
        :param _SpaceId: 空间ID
        :type SpaceId: str
        :param _VersionFilterList: 版本过滤条件(多个Filter之间为AND关系,同一Filter的多个Values为OR关系): - Perspective: 视角枚举,字符串单值,Values 长度必须为 1,多值视为非法;仅作用于详情返回的 version_list 裁剪,不决定接口本身可见性;不传默认 USER (USER=使用者视角,version_list 仅返回已上线版本 / EDITOR=编辑者视角,version_list 返回全部存活版本 / ALL=全量视角,同 EDITOR)
        :type VersionFilterList: list of Filter
        """
        self._SkillId = None
        self._SpaceId = None
        self._VersionFilterList = None

    @property
    def SkillId(self):
        r"""skillID
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""空间ID
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def VersionFilterList(self):
        r"""版本过滤条件(多个Filter之间为AND关系,同一Filter的多个Values为OR关系): - Perspective: 视角枚举,字符串单值,Values 长度必须为 1,多值视为非法;仅作用于详情返回的 version_list 裁剪,不决定接口本身可见性;不传默认 USER (USER=使用者视角,version_list 仅返回已上线版本 / EDITOR=编辑者视角,version_list 返回全部存活版本 / ALL=全量视角,同 EDITOR)
        :rtype: list of Filter
        """
        return self._VersionFilterList

    @VersionFilterList.setter
    def VersionFilterList(self, VersionFilterList):
        self._VersionFilterList = VersionFilterList


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        if params.get("VersionFilterList") is not None:
            self._VersionFilterList = []
            for item in params.get("VersionFilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._VersionFilterList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillDetailResponse(AbstractModel):
    r"""DescribeSkillDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillDetail: skill详情
        :type SkillDetail: :class:`tencentcloud.adp.v20260520.models.SkillDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SkillDetail = None
        self._RequestId = None

    @property
    def SkillDetail(self):
        r"""skill详情
        :rtype: :class:`tencentcloud.adp.v20260520.models.SkillDetail`
        """
        return self._SkillDetail

    @SkillDetail.setter
    def SkillDetail(self, SkillDetail):
        self._SkillDetail = SkillDetail

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
        if params.get("SkillDetail") is not None:
            self._SkillDetail = SkillDetail()
            self._SkillDetail._deserialize(params.get("SkillDetail"))
        self._RequestId = params.get("RequestId")


class DescribeSkillReferenceListRequest(AbstractModel):
    r"""DescribeSkillReferenceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>Skill ID，必填</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID，必填</p>
        :type SpaceId: str
        """
        self._SkillId = None
        self._SpaceId = None

    @property
    def SkillId(self):
        r"""<p>Skill ID，必填</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID，必填</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillReferenceListResponse(AbstractModel):
    r"""DescribeSkillReferenceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReferenceList: <p>按 SkillRefType 分组的引用汇总：某类型 total_count = 0 时不入组（不返回空占位） 本期同时落 OPENCLAW / AGENT / CORP_ASSISTANT 三路</p>
        :type ReferenceList: list of SkillReferenceGroup
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReferenceList = None
        self._RequestId = None

    @property
    def ReferenceList(self):
        r"""<p>按 SkillRefType 分组的引用汇总：某类型 total_count = 0 时不入组（不返回空占位） 本期同时落 OPENCLAW / AGENT / CORP_ASSISTANT 三路</p>
        :rtype: list of SkillReferenceGroup
        """
        return self._ReferenceList

    @ReferenceList.setter
    def ReferenceList(self, ReferenceList):
        self._ReferenceList = ReferenceList

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
        if params.get("ReferenceList") is not None:
            self._ReferenceList = []
            for item in params.get("ReferenceList"):
                obj = SkillReferenceGroup()
                obj._deserialize(item)
                self._ReferenceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSkillSummaryListRequest(AbstractModel):
    r"""DescribeSkillSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间ID，必填
        :type SpaceId: str
        :param _FavoriteOnly: 仅查询当前用户收藏的 Skill
        :type FavoriteOnly: bool
        :param _FilterList:    过滤条件(多个Filter之间为AND关系,同一Filter的多个Values为OR关系):
   - SkillIdList: Skill ID列表,字符串数组,精确匹配
   - ProviderType: Skill 提供方类型,枚举值数组,精确匹配
     (SKILL_PROVIDER_TYPE_OFFICIAL=1/SKILL_PROVIDER_TYPE_THIRD_PARTY=2/SKILL_PROVIDER_TYPE_CUSTOM=3/SKILL_PROVIDER_TYPE_CUSTOM_SHARED=4)
   - CategoryKey: 分类标识,字符串数组,精确匹配
   - AnalysisStatus: 安全检测状态,枚举值数组,精确匹配
     (SKILL_ANALYSIS_PENDING=0/SKILL_ANALYSIS_RUNNING=1/SKILL_ANALYSIS_AVAILABLE=2/SKILL_ANALYSIS_UNAVAILABLE=3/SKILL_ANALYSIS_FAILED=4)
   - RiskLevel: 风险等级,枚举值数组,精确匹配
     (SKILL_RISK_NONE=0/SKILL_RISK_LOW=1/SKILL_RISK_MEDIUM=2/SKILL_RISK_HIGH=3)
- SkillStatus: Skill 维度发布状态,枚举值数组,精确匹配,多值之间 OR;仅在 Perspective=EDITOR/ALL 时有实际意义
(SKILL_STATUS_INITIALIZED=0/SKILL_STATUS_AUDITING=1/SKILL_STATUS_PENDING_RELEASE=2/SKILL_STATUS_RELEASED=3)
   - ShareStatus: 共享状态,枚举值数组,精确匹配,仅在ProviderType包含SKILL_PROVIDER_TYPE_CUSTOM/SKILL_PROVIDER_TYPE_CUSTOM_SHARED时生效
     (SHARE_STATUS_UNSHARED=0/SHARE_STATUS_SHARED=1/SHARE_STATUS_APPROVING=2)
   - Perspective: 视角枚举,字符串单值,Values 长度必须为 1,多值视为非法;仅在 ProviderType=SKILL_PROVIDER_TYPE_CUSTOM 时生效;不传默认 USER
     (USER=使用者视角,仅返回仅有使用权限的 Skill / EDITOR=编辑者视角,仅返回有编辑权限的 Skill / ALL=全量视角,返回有任一权限位的 Skill)
  - Creator: 创建者过滤,字符串单值,Values 长度必须为 1,多值视为非法;仅在 ProviderType=SKILL_PROVIDER_TYPE_CUSTOM 时生效
   当前仅支持占位符 "$self",表示仅返回当前调用者创建的 Skill
   后续如需扩展为指定身份,再在此处追加约定
        :type FilterList: list of Filter
        :param _PageNumber: 页码，从 0 开始
        :type PageNumber: int
        :param _PageSize: 每页数量，最大值 100
        :type PageSize: int
        :param _Query: 名称/展示名称模糊搜索
        :type Query: str
        """
        self._SpaceId = None
        self._FavoriteOnly = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def SpaceId(self):
        r"""空间ID，必填
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FavoriteOnly(self):
        r"""仅查询当前用户收藏的 Skill
        :rtype: bool
        """
        return self._FavoriteOnly

    @FavoriteOnly.setter
    def FavoriteOnly(self, FavoriteOnly):
        self._FavoriteOnly = FavoriteOnly

    @property
    def FilterList(self):
        r"""   过滤条件(多个Filter之间为AND关系,同一Filter的多个Values为OR关系):
   - SkillIdList: Skill ID列表,字符串数组,精确匹配
   - ProviderType: Skill 提供方类型,枚举值数组,精确匹配
     (SKILL_PROVIDER_TYPE_OFFICIAL=1/SKILL_PROVIDER_TYPE_THIRD_PARTY=2/SKILL_PROVIDER_TYPE_CUSTOM=3/SKILL_PROVIDER_TYPE_CUSTOM_SHARED=4)
   - CategoryKey: 分类标识,字符串数组,精确匹配
   - AnalysisStatus: 安全检测状态,枚举值数组,精确匹配
     (SKILL_ANALYSIS_PENDING=0/SKILL_ANALYSIS_RUNNING=1/SKILL_ANALYSIS_AVAILABLE=2/SKILL_ANALYSIS_UNAVAILABLE=3/SKILL_ANALYSIS_FAILED=4)
   - RiskLevel: 风险等级,枚举值数组,精确匹配
     (SKILL_RISK_NONE=0/SKILL_RISK_LOW=1/SKILL_RISK_MEDIUM=2/SKILL_RISK_HIGH=3)
- SkillStatus: Skill 维度发布状态,枚举值数组,精确匹配,多值之间 OR;仅在 Perspective=EDITOR/ALL 时有实际意义
(SKILL_STATUS_INITIALIZED=0/SKILL_STATUS_AUDITING=1/SKILL_STATUS_PENDING_RELEASE=2/SKILL_STATUS_RELEASED=3)
   - ShareStatus: 共享状态,枚举值数组,精确匹配,仅在ProviderType包含SKILL_PROVIDER_TYPE_CUSTOM/SKILL_PROVIDER_TYPE_CUSTOM_SHARED时生效
     (SHARE_STATUS_UNSHARED=0/SHARE_STATUS_SHARED=1/SHARE_STATUS_APPROVING=2)
   - Perspective: 视角枚举,字符串单值,Values 长度必须为 1,多值视为非法;仅在 ProviderType=SKILL_PROVIDER_TYPE_CUSTOM 时生效;不传默认 USER
     (USER=使用者视角,仅返回仅有使用权限的 Skill / EDITOR=编辑者视角,仅返回有编辑权限的 Skill / ALL=全量视角,返回有任一权限位的 Skill)
  - Creator: 创建者过滤,字符串单值,Values 长度必须为 1,多值视为非法;仅在 ProviderType=SKILL_PROVIDER_TYPE_CUSTOM 时生效
   当前仅支持占位符 "$self",表示仅返回当前调用者创建的 Skill
   后续如需扩展为指定身份,再在此处追加约定
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""页码，从 0 开始
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量，最大值 100
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""名称/展示名称模糊搜索
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._FavoriteOnly = params.get("FavoriteOnly")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSkillSummaryListResponse(AbstractModel):
    r"""DescribeSkillSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillSummaryList: Skill 摘要列表
        :type SkillSummaryList: list of SkillSummary
        :param _TotalCount: 总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SkillSummaryList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SkillSummaryList(self):
        r"""Skill 摘要列表
        :rtype: list of SkillSummary
        """
        return self._SkillSummaryList

    @SkillSummaryList.setter
    def SkillSummaryList(self, SkillSummaryList):
        self._SkillSummaryList = SkillSummaryList

    @property
    def TotalCount(self):
        r"""总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("SkillSummaryList") is not None:
            self._SkillSummaryList = []
            for item in params.get("SkillSummaryList"):
                obj = SkillSummary()
                obj._deserialize(item)
                self._SkillSummaryList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSpaceListRequest(AbstractModel):
    r"""DescribeSpaceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 支持空间名称模糊搜索
        :type Query: str
        """
        self._Query = None

    @property
    def Query(self):
        r"""支持空间名称模糊搜索
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSpaceListResponse(AbstractModel):
    r"""DescribeSpaceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: str
        :param _SpaceList: 空间列表
        :type SpaceList: list of Space
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SpaceList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SpaceList(self):
        r"""空间列表
        :rtype: list of Space
        """
        return self._SpaceList

    @SpaceList.setter
    def SpaceList(self, SpaceList):
        self._SpaceList = SpaceList

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
        if params.get("SpaceList") is not None:
            self._SpaceList = []
            for item in params.get("SpaceList"):
                obj = Space()
                obj._deserialize(item)
                self._SpaceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSystemVariableListRequest(AbstractModel):
    r"""DescribeSystemVariableList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        """
        self._AppId = None

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSystemVariableListResponse(AbstractModel):
    r"""DescribeSystemVariableList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SystemVariableList: system_variable_list
        :type SystemVariableList: list of SystemVariable
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SystemVariableList = None
        self._RequestId = None

    @property
    def SystemVariableList(self):
        r"""system_variable_list
        :rtype: list of SystemVariable
        """
        return self._SystemVariableList

    @SystemVariableList.setter
    def SystemVariableList(self, SystemVariableList):
        self._SystemVariableList = SystemVariableList

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
        if params.get("SystemVariableList") is not None:
            self._SystemVariableList = []
            for item in params.get("SystemVariableList"):
                obj = SystemVariable()
                obj._deserialize(item)
                self._SystemVariableList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsageDetailListRequest(AbstractModel):
    r"""DescribeUsageDetailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: <p>资源类型，限定为 RESOURCE_TYPE_MODEL / RESOURCE_TYPE_PLUGIN</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>RESOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>RESOURCE_TYPE_MODEL</td><td>1</td><td>模型用量</td></tr><tr><td>RESOURCE_TYPE_PLUGIN</td><td>2</td><td>插件用量</td></tr><tr><td>RESOURCE_TYPE_PLATFORM</td><td>3</td><td>平台功能用量</td></tr><tr><td>RESOURCE_TYPE_MODEL_CONCURRENCY</td><td>4</td><td>模型并发超限</td></tr><tr><td>RESOURCE_TYPE_KB_CAPACITY</td><td>5</td><td>知识库容量</td></tr><tr><td>RESOURCE_TYPE_USAGE_SUMMARY</td><td>6</td><td>用量汇总</td></tr><tr><td>RESOURCE_TYPE_RESOURCE_CONSUME</td><td>7</td><td>资源消耗（计费明细）</td></tr></tbody></table>
        :type ResourceType: int
        :param _TimeRange: <p>查询时间范围（Unix 秒）</p>
        :type TimeRange: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        :param _ViewScope: <p>视图范围：企业视图 / 空间视图 / 应用视图</p>
        :type ViewScope: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        :param _FilterList: <p>扩展过滤（resource_type=MODEL）。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：model_name、user_id、space_id、resource_id/source_id、metric_source_type（METRIC_SOURCE_TYPE_* 或整数）、call_type（调用类型）</p>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码，从 0 开始</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量，最大 100</p>
        :type PageSize: int
        """
        self._ResourceType = None
        self._TimeRange = None
        self._ViewScope = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ResourceType(self):
        r"""<p>资源类型，限定为 RESOURCE_TYPE_MODEL / RESOURCE_TYPE_PLUGIN</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>RESOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>RESOURCE_TYPE_MODEL</td><td>1</td><td>模型用量</td></tr><tr><td>RESOURCE_TYPE_PLUGIN</td><td>2</td><td>插件用量</td></tr><tr><td>RESOURCE_TYPE_PLATFORM</td><td>3</td><td>平台功能用量</td></tr><tr><td>RESOURCE_TYPE_MODEL_CONCURRENCY</td><td>4</td><td>模型并发超限</td></tr><tr><td>RESOURCE_TYPE_KB_CAPACITY</td><td>5</td><td>知识库容量</td></tr><tr><td>RESOURCE_TYPE_USAGE_SUMMARY</td><td>6</td><td>用量汇总</td></tr><tr><td>RESOURCE_TYPE_RESOURCE_CONSUME</td><td>7</td><td>资源消耗（计费明细）</td></tr></tbody></table>
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def TimeRange(self):
        r"""<p>查询时间范围（Unix 秒）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def ViewScope(self):
        r"""<p>视图范围：企业视图 / 空间视图 / 应用视图</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        """
        return self._ViewScope

    @ViewScope.setter
    def ViewScope(self, ViewScope):
        self._ViewScope = ViewScope

    @property
    def FilterList(self):
        r"""<p>扩展过滤（resource_type=MODEL）。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：model_name、user_id、space_id、resource_id/source_id、metric_source_type（METRIC_SOURCE_TYPE_* 或整数）、call_type（调用类型）</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码，从 0 开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量，最大 100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("TimeRange") is not None:
            self._TimeRange = TimeRange()
            self._TimeRange._deserialize(params.get("TimeRange"))
        if params.get("ViewScope") is not None:
            self._ViewScope = ViewScope()
            self._ViewScope._deserialize(params.get("ViewScope"))
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageDetailListResponse(AbstractModel):
    r"""DescribeUsageDetailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总记录数，用于前端分页</p>
        :type TotalCount: str
        :param _UsageDetailList: <p>资源调用时序明细列表</p>
        :type UsageDetailList: list of UsageDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UsageDetailList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总记录数，用于前端分页</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UsageDetailList(self):
        r"""<p>资源调用时序明细列表</p>
        :rtype: list of UsageDetail
        """
        return self._UsageDetailList

    @UsageDetailList.setter
    def UsageDetailList(self, UsageDetailList):
        self._UsageDetailList = UsageDetailList

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
        if params.get("UsageDetailList") is not None:
            self._UsageDetailList = []
            for item in params.get("UsageDetailList"):
                obj = UsageDetail()
                obj._deserialize(item)
                self._UsageDetailList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeUsageSummaryListRequest(AbstractModel):
    r"""DescribeUsageSummaryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceType: <p>资源类型，限定为 MODEL / PLUGIN / PLATFORM</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>RESOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>RESOURCE_TYPE_MODEL</td><td>1</td><td>模型用量</td></tr><tr><td>RESOURCE_TYPE_PLUGIN</td><td>2</td><td>插件用量</td></tr><tr><td>RESOURCE_TYPE_PLATFORM</td><td>3</td><td>平台功能用量</td></tr><tr><td>RESOURCE_TYPE_MODEL_CONCURRENCY</td><td>4</td><td>模型并发超限</td></tr><tr><td>RESOURCE_TYPE_KB_CAPACITY</td><td>5</td><td>知识库容量</td></tr><tr><td>RESOURCE_TYPE_USAGE_SUMMARY</td><td>6</td><td>用量汇总</td></tr><tr><td>RESOURCE_TYPE_RESOURCE_CONSUME</td><td>7</td><td>资源消耗（计费明细）</td></tr></tbody></table>
        :type ResourceType: int
        :param _TimeRange: <p>查询时间范围（Unix 秒）</p>
        :type TimeRange: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        :param _ViewScope: <p>视图范围：企业视图 / 空间视图 / 应用视图</p>
        :type ViewScope: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        :param _FilterList: <p>扩展过滤（resource_type=MODEL）。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：model_name（模型名）、user_id（用户ID）、space_id（空间ID）、resource_id/source_id（来源ID）、metric_source_type（METRIC_SOURCE_TYPE_* 枚举名或整数）</p>
        :type FilterList: list of Filter
        :param _PageNumber: <p>页码，从 0 开始</p>
        :type PageNumber: int
        :param _PageSize: <p>每页数量，最大 100</p>
        :type PageSize: int
        """
        self._ResourceType = None
        self._TimeRange = None
        self._ViewScope = None
        self._FilterList = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def ResourceType(self):
        r"""<p>资源类型，限定为 MODEL / PLUGIN / PLATFORM</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>RESOURCE_TYPE_UNSPECIFIED</td><td>0</td><td></td></tr><tr><td>RESOURCE_TYPE_MODEL</td><td>1</td><td>模型用量</td></tr><tr><td>RESOURCE_TYPE_PLUGIN</td><td>2</td><td>插件用量</td></tr><tr><td>RESOURCE_TYPE_PLATFORM</td><td>3</td><td>平台功能用量</td></tr><tr><td>RESOURCE_TYPE_MODEL_CONCURRENCY</td><td>4</td><td>模型并发超限</td></tr><tr><td>RESOURCE_TYPE_KB_CAPACITY</td><td>5</td><td>知识库容量</td></tr><tr><td>RESOURCE_TYPE_USAGE_SUMMARY</td><td>6</td><td>用量汇总</td></tr><tr><td>RESOURCE_TYPE_RESOURCE_CONSUME</td><td>7</td><td>资源消耗（计费明细）</td></tr></tbody></table>
        :rtype: int
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def TimeRange(self):
        r"""<p>查询时间范围（Unix 秒）</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.TimeRange`
        """
        return self._TimeRange

    @TimeRange.setter
    def TimeRange(self, TimeRange):
        self._TimeRange = TimeRange

    @property
    def ViewScope(self):
        r"""<p>视图范围：企业视图 / 空间视图 / 应用视图</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ViewScope`
        """
        return self._ViewScope

    @ViewScope.setter
    def ViewScope(self, ViewScope):
        self._ViewScope = ViewScope

    @property
    def FilterList(self):
        r"""<p>扩展过滤（resource_type=MODEL）。Filter 组合规则：多项 AND，同项 value_list OR。支持 Name：model_name（模型名）、user_id（用户ID）、space_id（空间ID）、resource_id/source_id（来源ID）、metric_source_type（METRIC_SOURCE_TYPE_* 枚举名或整数）</p>
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def PageNumber(self):
        r"""<p>页码，从 0 开始</p>
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""<p>每页数量，最大 100</p>
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("TimeRange") is not None:
            self._TimeRange = TimeRange()
            self._TimeRange._deserialize(params.get("TimeRange"))
        if params.get("ViewScope") is not None:
            self._ViewScope = ViewScope()
            self._ViewScope._deserialize(params.get("ViewScope"))
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageSummaryListResponse(AbstractModel):
    r"""DescribeUsageSummaryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>总记录数，用于前端分页</p>
        :type TotalCount: str
        :param _UsageSummaryList: <p>资源用量聚合明细列表</p>
        :type UsageSummaryList: list of UsageSummary
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._UsageSummaryList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>总记录数，用于前端分页</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UsageSummaryList(self):
        r"""<p>资源用量聚合明细列表</p>
        :rtype: list of UsageSummary
        """
        return self._UsageSummaryList

    @UsageSummaryList.setter
    def UsageSummaryList(self, UsageSummaryList):
        self._UsageSummaryList = UsageSummaryList

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
        if params.get("UsageSummaryList") is not None:
            self._UsageSummaryList = []
            for item in params.get("UsageSummaryList"):
                obj = UsageSummary()
                obj._deserialize(item)
                self._UsageSummaryList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVariableListRequest(AbstractModel):
    r"""DescribeVariableList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _FilterList: 过滤条件(支持: VariableIdList-变量ID列表, VariableType-变量类型)
        :type FilterList: list of Filter
        :param _ModuleType: 模块类型。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :type ModuleType: int
        :param _NeedInternalVariable: 是否需要内部变量
        :type NeedInternalVariable: bool
        :param _PageNumber: 页码(从0开始)
        :type PageNumber: int
        :param _PageSize: 每页数量(最大值:100)
        :type PageSize: int
        :param _Query: 查询关键词
        :type Query: str
        """
        self._AppId = None
        self._FilterList = None
        self._ModuleType = None
        self._NeedInternalVariable = None
        self._PageNumber = None
        self._PageSize = None
        self._Query = None

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def FilterList(self):
        r"""过滤条件(支持: VariableIdList-变量ID列表, VariableType-变量类型)
        :rtype: list of Filter
        """
        return self._FilterList

    @FilterList.setter
    def FilterList(self, FilterList):
        self._FilterList = FilterList

    @property
    def ModuleType(self):
        r"""模块类型。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :rtype: int
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType

    @property
    def NeedInternalVariable(self):
        r"""是否需要内部变量
        :rtype: bool
        """
        return self._NeedInternalVariable

    @NeedInternalVariable.setter
    def NeedInternalVariable(self, NeedInternalVariable):
        self._NeedInternalVariable = NeedInternalVariable

    @property
    def PageNumber(self):
        r"""页码(从0开始)
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        r"""每页数量(最大值:100)
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Query(self):
        r"""查询关键词
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("FilterList") is not None:
            self._FilterList = []
            for item in params.get("FilterList"):
                obj = Filter()
                obj._deserialize(item)
                self._FilterList.append(obj)
        self._ModuleType = params.get("ModuleType")
        self._NeedInternalVariable = params.get("NeedInternalVariable")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVariableListResponse(AbstractModel):
    r"""DescribeVariableList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: total_count
        :type TotalCount: int
        :param _VariableList: variable_list
        :type VariableList: list of Variable
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VariableList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""total_count
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VariableList(self):
        r"""variable_list
        :rtype: list of Variable
        """
        return self._VariableList

    @VariableList.setter
    def VariableList(self, VariableList):
        self._VariableList = VariableList

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
        if params.get("VariableList") is not None:
            self._VariableList = []
            for item in params.get("VariableList"):
                obj = Variable()
                obj._deserialize(item)
                self._VariableList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVariableRequest(AbstractModel):
    r"""DescribeVariable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _VariableId: variable_id
        :type VariableId: str
        :param _ModuleType: module_type。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :type ModuleType: int
        """
        self._AppId = None
        self._VariableId = None
        self._ModuleType = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def VariableId(self):
        r"""variable_id
        :rtype: str
        """
        return self._VariableId

    @VariableId.setter
    def VariableId(self, VariableId):
        self._VariableId = VariableId

    @property
    def ModuleType(self):
        r"""module_type。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :rtype: int
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._VariableId = params.get("VariableId")
        self._ModuleType = params.get("ModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVariableResponse(AbstractModel):
    r"""DescribeVariable返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Variable: 变量信息
        :type Variable: :class:`tencentcloud.adp.v20260520.models.Variable`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Variable = None
        self._RequestId = None

    @property
    def Variable(self):
        r"""变量信息
        :rtype: :class:`tencentcloud.adp.v20260520.models.Variable`
        """
        return self._Variable

    @Variable.setter
    def Variable(self, Variable):
        self._Variable = Variable

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
        if params.get("Variable") is not None:
            self._Variable = Variable()
            self._Variable._deserialize(params.get("Variable"))
        self._RequestId = params.get("RequestId")


class DialogCustomConfig(AbstractModel):
    r"""对话端自定义配置(所有模式共用,允许对话中动态修改配置)

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>是否开启对话端动态修改配置</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>是否开启对话端动态修改配置</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DigitalHumanConfig(AbstractModel):
    r"""数智人配置

    """

    def __init__(self):
        r"""
        :param _AssetKey: 数智人形象资产id
        :type AssetKey: str
        :param _Avatar: 数智人图片
        :type Avatar: str
        :param _Name: 数智人形象名称
        :type Name: str
        :param _PreviewUrl: 数智人预览地址
        :type PreviewUrl: str
        """
        self._AssetKey = None
        self._Avatar = None
        self._Name = None
        self._PreviewUrl = None

    @property
    def AssetKey(self):
        r"""数智人形象资产id
        :rtype: str
        """
        return self._AssetKey

    @AssetKey.setter
    def AssetKey(self, AssetKey):
        self._AssetKey = AssetKey

    @property
    def Avatar(self):
        r"""数智人图片
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Name(self):
        r"""数智人形象名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PreviewUrl(self):
        r"""数智人预览地址
        :rtype: str
        """
        return self._PreviewUrl

    @PreviewUrl.setter
    def PreviewUrl(self, PreviewUrl):
        self._PreviewUrl = PreviewUrl


    def _deserialize(self, params):
        self._AssetKey = params.get("AssetKey")
        self._Avatar = params.get("Avatar")
        self._Name = params.get("Name")
        self._PreviewUrl = params.get("PreviewUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplexBilling(AbstractModel):
    r"""DuplexBilling

    """

    def __init__(self):
        r"""
        :param _BillingUnit: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>UNKNOW</td><td>0</td><td></td></tr><tr><td>TOKEN</td><td>1</td><td>按token</td></tr><tr><td>PAGE_COUNT</td><td>2</td><td>按页数</td></tr><tr><td>TIMES</td><td>3</td><td>按次数</td></tr><tr><td>TIMES_THOUSAND</td><td>4</td><td>按千次数</td></tr><tr><td>SECOND</td><td>5</td><td>按时长</td></tr><tr><td>CHARACTER</td><td>6</td><td>按字符数</td></tr><tr><td>CHARACTER_THOUSAND</td><td>7</td><td>按千字符数</td></tr><tr><td>SHEET</td><td>8</td><td>按张</td></tr><tr><td>NUMBER</td><td>9</td><td>按个数</td></tr></tbody></table>
        :type BillingUnit: int
        :param _InputCashPrice: <p>输入现金价格</p><p>单位：元</p>
        :type InputCashPrice: float
        :param _InputPuPrice: <p>输入pu价格</p><p>单位：pu</p>
        :type InputPuPrice: float
        :param _OutputCashPrice: <p>输出现金价格</p><p>单位：元</p>
        :type OutputCashPrice: float
        :param _OutputPuPrice: <p>输出pu价格</p><p>单位：pu</p>
        :type OutputPuPrice: float
        """
        self._BillingUnit = None
        self._InputCashPrice = None
        self._InputPuPrice = None
        self._OutputCashPrice = None
        self._OutputPuPrice = None

    @property
    def BillingUnit(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>UNKNOW</td><td>0</td><td></td></tr><tr><td>TOKEN</td><td>1</td><td>按token</td></tr><tr><td>PAGE_COUNT</td><td>2</td><td>按页数</td></tr><tr><td>TIMES</td><td>3</td><td>按次数</td></tr><tr><td>TIMES_THOUSAND</td><td>4</td><td>按千次数</td></tr><tr><td>SECOND</td><td>5</td><td>按时长</td></tr><tr><td>CHARACTER</td><td>6</td><td>按字符数</td></tr><tr><td>CHARACTER_THOUSAND</td><td>7</td><td>按千字符数</td></tr><tr><td>SHEET</td><td>8</td><td>按张</td></tr><tr><td>NUMBER</td><td>9</td><td>按个数</td></tr></tbody></table>
        :rtype: int
        """
        return self._BillingUnit

    @BillingUnit.setter
    def BillingUnit(self, BillingUnit):
        self._BillingUnit = BillingUnit

    @property
    def InputCashPrice(self):
        r"""<p>输入现金价格</p><p>单位：元</p>
        :rtype: float
        """
        return self._InputCashPrice

    @InputCashPrice.setter
    def InputCashPrice(self, InputCashPrice):
        self._InputCashPrice = InputCashPrice

    @property
    def InputPuPrice(self):
        r"""<p>输入pu价格</p><p>单位：pu</p>
        :rtype: float
        """
        return self._InputPuPrice

    @InputPuPrice.setter
    def InputPuPrice(self, InputPuPrice):
        self._InputPuPrice = InputPuPrice

    @property
    def OutputCashPrice(self):
        r"""<p>输出现金价格</p><p>单位：元</p>
        :rtype: float
        """
        return self._OutputCashPrice

    @OutputCashPrice.setter
    def OutputCashPrice(self, OutputCashPrice):
        self._OutputCashPrice = OutputCashPrice

    @property
    def OutputPuPrice(self):
        r"""<p>输出pu价格</p><p>单位：pu</p>
        :rtype: float
        """
        return self._OutputPuPrice

    @OutputPuPrice.setter
    def OutputPuPrice(self, OutputPuPrice):
        self._OutputPuPrice = OutputPuPrice


    def _deserialize(self, params):
        self._BillingUnit = params.get("BillingUnit")
        self._InputCashPrice = params.get("InputCashPrice")
        self._InputPuPrice = params.get("InputPuPrice")
        self._OutputCashPrice = params.get("OutputCashPrice")
        self._OutputPuPrice = params.get("OutputPuPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExecuteConfig(AbstractModel):
    r"""ExecuteConfig

    """

    def __init__(self):
        r"""
        :param _PromptConfig: <p>Prompt配置</p>
        :type PromptConfig: :class:`tencentcloud.adp.v20260520.models.AppTriggerPromptExecuteConfig`
        :param _WorkflowConfig: <p>工作流配置</p>
        :type WorkflowConfig: :class:`tencentcloud.adp.v20260520.models.AppTriggerWorkflowExecuteConfig`
        """
        self._PromptConfig = None
        self._WorkflowConfig = None

    @property
    def PromptConfig(self):
        r"""<p>Prompt配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerPromptExecuteConfig`
        """
        return self._PromptConfig

    @PromptConfig.setter
    def PromptConfig(self, PromptConfig):
        self._PromptConfig = PromptConfig

    @property
    def WorkflowConfig(self):
        r"""<p>工作流配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerWorkflowExecuteConfig`
        """
        return self._WorkflowConfig

    @WorkflowConfig.setter
    def WorkflowConfig(self, WorkflowConfig):
        self._WorkflowConfig = WorkflowConfig


    def _deserialize(self, params):
        if params.get("PromptConfig") is not None:
            self._PromptConfig = AppTriggerPromptExecuteConfig()
            self._PromptConfig._deserialize(params.get("PromptConfig"))
        if params.get("WorkflowConfig") is not None:
            self._WorkflowConfig = AppTriggerWorkflowExecuteConfig()
            self._WorkflowConfig._deserialize(params.get("WorkflowConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FavoritePluginRequest(AbstractModel):
    r"""FavoritePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _SpaceId: <p>当前空间id</p>
        :type SpaceId: str
        """
        self._PluginId = None
        self._SpaceId = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def SpaceId(self):
        r"""<p>当前空间id</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FavoritePluginResponse(AbstractModel):
    r"""FavoritePlugin返回参数结构体

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


class FavoriteSkillRequest(AbstractModel):
    r"""FavoriteSkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>SkillId</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        """
        self._SkillId = None
        self._SpaceId = None

    @property
    def SkillId(self):
        r"""<p>SkillId</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FavoriteSkillResponse(AbstractModel):
    r"""FavoriteSkill返回参数结构体

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


class FieldMask(AbstractModel):
    r"""FieldMask

    """

    def __init__(self):
        r"""
        :param _Paths: <p>参数名称</p><p>参数格式：需要获取的指定字段路径</p>
        :type Paths: list of str
        """
        self._Paths = None

    @property
    def Paths(self):
        r"""<p>参数名称</p><p>参数格式：需要获取的指定字段路径</p>
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths


    def _deserialize(self, params):
        self._Paths = params.get("Paths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileParseModel(AbstractModel):
    r"""文档解析模型参数

    """

    def __init__(self):
        r"""
        :param _Alias: 模型别名
        :type Alias: str
        :param _Description: 模型描述
        :type Description: str
        :param _EnhancementMode: 增强模式
        :type EnhancementMode: str
        :param _ModelId: 模型唯一ID
        :type ModelId: str
        :param _ModelProviderType: 模型类型
        :type ModelProviderType: str
        :param _EnableFormulaEnhancement: 是否启用公式增强
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableFormulaEnhancement: bool
        :param _EnableLLMEnhancement: 是否启用 LLM 增强
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableLLMEnhancement: bool
        :param _OutputHtmlTable: 是否输出 HTML 表格
注意：此字段可能返回 null，表示取不到有效值。
        :type OutputHtmlTable: bool
        :param _SupportedFileList: 支持的文件类型列表
        :type SupportedFileList: list of SupportedFileType
        """
        self._Alias = None
        self._Description = None
        self._EnhancementMode = None
        self._ModelId = None
        self._ModelProviderType = None
        self._EnableFormulaEnhancement = None
        self._EnableLLMEnhancement = None
        self._OutputHtmlTable = None
        self._SupportedFileList = None

    @property
    def Alias(self):
        r"""模型别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Description(self):
        r"""模型描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EnhancementMode(self):
        r"""增强模式
        :rtype: str
        """
        return self._EnhancementMode

    @EnhancementMode.setter
    def EnhancementMode(self, EnhancementMode):
        self._EnhancementMode = EnhancementMode

    @property
    def ModelId(self):
        r"""模型唯一ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelProviderType(self):
        r"""模型类型
        :rtype: str
        """
        return self._ModelProviderType

    @ModelProviderType.setter
    def ModelProviderType(self, ModelProviderType):
        self._ModelProviderType = ModelProviderType

    @property
    def EnableFormulaEnhancement(self):
        r"""是否启用公式增强
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableFormulaEnhancement

    @EnableFormulaEnhancement.setter
    def EnableFormulaEnhancement(self, EnableFormulaEnhancement):
        self._EnableFormulaEnhancement = EnableFormulaEnhancement

    @property
    def EnableLLMEnhancement(self):
        r"""是否启用 LLM 增强
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._EnableLLMEnhancement

    @EnableLLMEnhancement.setter
    def EnableLLMEnhancement(self, EnableLLMEnhancement):
        self._EnableLLMEnhancement = EnableLLMEnhancement

    @property
    def OutputHtmlTable(self):
        r"""是否输出 HTML 表格
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._OutputHtmlTable

    @OutputHtmlTable.setter
    def OutputHtmlTable(self, OutputHtmlTable):
        self._OutputHtmlTable = OutputHtmlTable

    @property
    def SupportedFileList(self):
        r"""支持的文件类型列表
        :rtype: list of SupportedFileType
        """
        return self._SupportedFileList

    @SupportedFileList.setter
    def SupportedFileList(self, SupportedFileList):
        self._SupportedFileList = SupportedFileList


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Description = params.get("Description")
        self._EnhancementMode = params.get("EnhancementMode")
        self._ModelId = params.get("ModelId")
        self._ModelProviderType = params.get("ModelProviderType")
        self._EnableFormulaEnhancement = params.get("EnableFormulaEnhancement")
        self._EnableLLMEnhancement = params.get("EnableLLMEnhancement")
        self._OutputHtmlTable = params.get("OutputHtmlTable")
        if params.get("SupportedFileList") is not None:
            self._SupportedFileList = []
            for item in params.get("SupportedFileList"):
                obj = SupportedFileType()
                obj._deserialize(item)
                self._SupportedFileList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""列表通用过滤条件（多个 Filter 之间为 AND 关系，同一 Filter 的多个 value_list 为 OR 关系）

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名
        :type Name: str
        :param _Operator: 操作符，默认 IN（向后兼容）<table><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>FILTER_OPERATOR_IN</td><td>0</td><td>属于 value_list（默认值，向后兼容；value_list 不可为空）</td></tr><tr><td>FILTER_OPERATOR_NOT_IN</td><td>1</td><td>不属于 value_list（value_list 不可为空）</td></tr></table>
        :type Operator: int
        :param _ValueList: 过滤值数组
        :type ValueList: list of str
        """
        self._Name = None
        self._Operator = None
        self._ValueList = None

    @property
    def Name(self):
        r"""过滤字段名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        r"""操作符，默认 IN（向后兼容）<table><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>FILTER_OPERATOR_IN</td><td>0</td><td>属于 value_list（默认值，向后兼容；value_list 不可为空）</td></tr><tr><td>FILTER_OPERATOR_NOT_IN</td><td>1</td><td>不属于 value_list（value_list 不可为空）</td></tr></table>
        :rtype: int
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def ValueList(self):
        r"""过滤值数组
        :rtype: list of str
        """
        return self._ValueList

    @ValueList.setter
    def ValueList(self, ValueList):
        self._ValueList = ValueList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        self._ValueList = params.get("ValueList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateModel(AbstractModel):
    r"""生成模型配置

    """

    def __init__(self):
        r"""
        :param _Model: 生成模型
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""生成模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Identity(AbstractModel):
    r"""通用身份信息（支持数字 ID 与字符串 ID 两种形态）

    """

    def __init__(self):
        r"""
        :param _Description: <p>描述</p>
        :type Description: str
        :param _Id: <p>数字 ID</p>
        :type Id: str
        :param _Name: <p>名称</p>
        :type Name: str
        :param _StrId: <p>字符串 ID</p>
        :type StrId: str
        """
        self._Description = None
        self._Id = None
        self._Name = None
        self._StrId = None

    @property
    def Description(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Id(self):
        r"""<p>数字 ID</p>
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""<p>名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StrId(self):
        r"""<p>字符串 ID</p>
        :rtype: str
        """
        return self._StrId

    @StrId.setter
    def StrId(self, StrId):
        self._StrId = StrId


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._StrId = params.get("StrId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputBoxConfig(AbstractModel):
    r"""输入框配置

    """

    def __init__(self):
        r"""
        :param _InputBoxButtons: 输入框按钮，1：上传图片、2：上传文档，3：腾讯文档，4：联网搜索
        :type InputBoxButtons: list of int
        """
        self._InputBoxButtons = None

    @property
    def InputBoxButtons(self):
        r"""输入框按钮，1：上传图片、2：上传文档，3：腾讯文档，4：联网搜索
        :rtype: list of int
        """
        return self._InputBoxButtons

    @InputBoxButtons.setter
    def InputBoxButtons(self, InputBoxButtons):
        self._InputBoxButtons = InputBoxButtons


    def _deserialize(self, params):
        self._InputBoxButtons = params.get("InputBoxButtons")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntentAchievementInfo(AbstractModel):
    r"""意图达成信息

    """

    def __init__(self):
        r"""
        :param _Description: 描述
        :type Description: str
        :param _Name: 名称
        :type Name: str
        """
        self._Description = None
        self._Name = None

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
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntervalSchedule(AbstractModel):
    r"""IntervalSchedule

    """

    def __init__(self):
        r"""
        :param _StartAt: 开始时间
        :type StartAt: str
        :param _Unit: 
枚举值:
| 枚举值 | uint |
| --- | --- |
| INTERVAL_UNIT_UNSPECIFIED | 0 |
| INTERVAL_UNIT_HOUR | 1 |
| INTERVAL_UNIT_DAY | 2 |
        :type Unit: int
        :param _Value: 值
        :type Value: int
        """
        self._StartAt = None
        self._Unit = None
        self._Value = None

    @property
    def StartAt(self):
        r"""开始时间
        :rtype: str
        """
        return self._StartAt

    @StartAt.setter
    def StartAt(self, StartAt):
        self._StartAt = StartAt

    @property
    def Unit(self):
        r"""
枚举值:
| 枚举值 | uint |
| --- | --- |
| INTERVAL_UNIT_UNSPECIFIED | 0 |
| INTERVAL_UNIT_HOUR | 1 |
| INTERVAL_UNIT_DAY | 2 |
        :rtype: int
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        r"""值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._StartAt = params.get("StartAt")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MCPPluginConfig(AbstractModel):
    r"""MCP插件配置信息

    """

    def __init__(self):
        r"""
        :param _ExternalMCPServerUrl: <p>MCP插件外部访问地址</p>
        :type ExternalMCPServerUrl: str
        :param _MCPServerUrl: <p>MCP server地址</p>
        :type MCPServerUrl: str
        :param _MCPTransport: <p>MCP传输类型: SSE/Streamable<br>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 | SSE + HTTP 模式 |<br>| 1 | Streamable HTTP 模式 |</p>
        :type MCPTransport: int
        :param _PluginHeader: <p>MCP插件的header参数</p>
        :type PluginHeader: list of PluginParam
        :param _PluginQuery: <p>MCP插件的query参数</p>
        :type PluginQuery: list of PluginParam
        :param _SSEReadTimeout: <p>SSE长连接超时时间，单位秒</p>
        :type SSEReadTimeout: int
        :param _Timeout: <p>请求超时时间，单位秒</p>
        :type Timeout: int
        :param _AuthConfig: <p>授权信息</p>
        :type AuthConfig: :class:`tencentcloud.adp.v20260520.models.AuthConfig`
        :param _SupportsApps: <p>是否支持交互界面（MCP Apps），插件级标签，默认false</p>
        :type SupportsApps: bool
        """
        self._ExternalMCPServerUrl = None
        self._MCPServerUrl = None
        self._MCPTransport = None
        self._PluginHeader = None
        self._PluginQuery = None
        self._SSEReadTimeout = None
        self._Timeout = None
        self._AuthConfig = None
        self._SupportsApps = None

    @property
    def ExternalMCPServerUrl(self):
        r"""<p>MCP插件外部访问地址</p>
        :rtype: str
        """
        return self._ExternalMCPServerUrl

    @ExternalMCPServerUrl.setter
    def ExternalMCPServerUrl(self, ExternalMCPServerUrl):
        self._ExternalMCPServerUrl = ExternalMCPServerUrl

    @property
    def MCPServerUrl(self):
        r"""<p>MCP server地址</p>
        :rtype: str
        """
        return self._MCPServerUrl

    @MCPServerUrl.setter
    def MCPServerUrl(self, MCPServerUrl):
        self._MCPServerUrl = MCPServerUrl

    @property
    def MCPTransport(self):
        r"""<p>MCP传输类型: SSE/Streamable<br>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 | SSE + HTTP 模式 |<br>| 1 | Streamable HTTP 模式 |</p>
        :rtype: int
        """
        return self._MCPTransport

    @MCPTransport.setter
    def MCPTransport(self, MCPTransport):
        self._MCPTransport = MCPTransport

    @property
    def PluginHeader(self):
        r"""<p>MCP插件的header参数</p>
        :rtype: list of PluginParam
        """
        return self._PluginHeader

    @PluginHeader.setter
    def PluginHeader(self, PluginHeader):
        self._PluginHeader = PluginHeader

    @property
    def PluginQuery(self):
        r"""<p>MCP插件的query参数</p>
        :rtype: list of PluginParam
        """
        return self._PluginQuery

    @PluginQuery.setter
    def PluginQuery(self, PluginQuery):
        self._PluginQuery = PluginQuery

    @property
    def SSEReadTimeout(self):
        r"""<p>SSE长连接超时时间，单位秒</p>
        :rtype: int
        """
        return self._SSEReadTimeout

    @SSEReadTimeout.setter
    def SSEReadTimeout(self, SSEReadTimeout):
        self._SSEReadTimeout = SSEReadTimeout

    @property
    def Timeout(self):
        r"""<p>请求超时时间，单位秒</p>
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def AuthConfig(self):
        r"""<p>授权信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AuthConfig`
        """
        return self._AuthConfig

    @AuthConfig.setter
    def AuthConfig(self, AuthConfig):
        self._AuthConfig = AuthConfig

    @property
    def SupportsApps(self):
        r"""<p>是否支持交互界面（MCP Apps），插件级标签，默认false</p>
        :rtype: bool
        """
        return self._SupportsApps

    @SupportsApps.setter
    def SupportsApps(self, SupportsApps):
        self._SupportsApps = SupportsApps


    def _deserialize(self, params):
        self._ExternalMCPServerUrl = params.get("ExternalMCPServerUrl")
        self._MCPServerUrl = params.get("MCPServerUrl")
        self._MCPTransport = params.get("MCPTransport")
        if params.get("PluginHeader") is not None:
            self._PluginHeader = []
            for item in params.get("PluginHeader"):
                obj = PluginParam()
                obj._deserialize(item)
                self._PluginHeader.append(obj)
        if params.get("PluginQuery") is not None:
            self._PluginQuery = []
            for item in params.get("PluginQuery"):
                obj = PluginParam()
                obj._deserialize(item)
                self._PluginQuery.append(obj)
        self._SSEReadTimeout = params.get("SSEReadTimeout")
        self._Timeout = params.get("Timeout")
        if params.get("AuthConfig") is not None:
            self._AuthConfig = AuthConfig()
            self._AuthConfig._deserialize(params.get("AuthConfig"))
        self._SupportsApps = params.get("SupportsApps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MCPToolConfig(AbstractModel):
    r"""MCPToolConfig

    """

    def __init__(self):
        r"""
        :param _Inputs: <p>输入参数</p>
        :type Inputs: list of RequestParam
        :param _Outputs: <p>输出参数</p>
        :type Outputs: list of ResponseParam
        :param _Meta: <p>工具meta信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Meta: :class:`tencentcloud.adp.v20260520.models.MCPToolMeta`
        :param _SupportsApps: <p>是否支持交互界面（MCP Apps），插件级标签  默认值：false</p>
        :type SupportsApps: bool
        """
        self._Inputs = None
        self._Outputs = None
        self._Meta = None
        self._SupportsApps = None

    @property
    def Inputs(self):
        r"""<p>输入参数</p>
        :rtype: list of RequestParam
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs

    @property
    def Outputs(self):
        r"""<p>输出参数</p>
        :rtype: list of ResponseParam
        """
        return self._Outputs

    @Outputs.setter
    def Outputs(self, Outputs):
        self._Outputs = Outputs

    @property
    def Meta(self):
        r"""<p>工具meta信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.MCPToolMeta`
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta

    @property
    def SupportsApps(self):
        r"""<p>是否支持交互界面（MCP Apps），插件级标签  默认值：false</p>
        :rtype: bool
        """
        return self._SupportsApps

    @SupportsApps.setter
    def SupportsApps(self, SupportsApps):
        self._SupportsApps = SupportsApps


    def _deserialize(self, params):
        if params.get("Inputs") is not None:
            self._Inputs = []
            for item in params.get("Inputs"):
                obj = RequestParam()
                obj._deserialize(item)
                self._Inputs.append(obj)
        if params.get("Outputs") is not None:
            self._Outputs = []
            for item in params.get("Outputs"):
                obj = ResponseParam()
                obj._deserialize(item)
                self._Outputs.append(obj)
        if params.get("Meta") is not None:
            self._Meta = MCPToolMeta()
            self._Meta._deserialize(params.get("Meta"))
        self._SupportsApps = params.get("SupportsApps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MCPToolMeta(AbstractModel):
    r"""对应 MCP 协议工具 _meta，承载 MCP Apps 工具的 UI 元信息（本期仅消费 resourceUri）

    """

    def __init__(self):
        r"""
        :param _Ui: <p>工具的 UI 扩展元信息，对应 MCP 协议的 _meta.ui，声明工具关联的交互式界面资源（ResourceUri）及调用方可见性（Visibility）。仅当工具支持 MCP Apps 或声明了可见性时返回；纯文本工具该字段为空。详见 MCPToolUIMeta 结构定义。</p>
        :type Ui: :class:`tencentcloud.adp.v20260520.models.MCPToolUIMeta`
        """
        self._Ui = None

    @property
    def Ui(self):
        r"""<p>工具的 UI 扩展元信息，对应 MCP 协议的 _meta.ui，声明工具关联的交互式界面资源（ResourceUri）及调用方可见性（Visibility）。仅当工具支持 MCP Apps 或声明了可见性时返回；纯文本工具该字段为空。详见 MCPToolUIMeta 结构定义。</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.MCPToolUIMeta`
        """
        return self._Ui

    @Ui.setter
    def Ui(self, Ui):
        self._Ui = Ui


    def _deserialize(self, params):
        if params.get("Ui") is not None:
            self._Ui = MCPToolUIMeta()
            self._Ui._deserialize(params.get("Ui"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MCPToolUIMeta(AbstractModel):
    r"""对应 MCP 协议 _meta.ui，定义 MCP Apps 工具的交互界面元信息（本期仅消费 resourceUri，visibility）

    """

    def __init__(self):
        r"""
        :param _ResourceUri: <p>关联的 UI 资源 URI，ui:// scheme，格式为 ui://&lt;插件标识&gt;/&lt;资源名&gt;-&lt;版本&gt;。该字段是 MCP Apps 交互式界面的入口，非空时表示工具支持 Apps（&quot;文本 + 交互式界面&quot;展示），为空则为纯文本工具。由工具同步结果自动识别填充，不支持手工编辑。</p>
        :type ResourceUri: str
        :param _Visibility: <p>工具的调用方可见性声明，取值范围：model（模型可调用）、app（应用界面可调用），可多选，如 [&quot;model&quot;,&quot;app&quot;]。与 ResourceUri 相互独立（SEP-1865），可单独存在，例如纯后端 app-only 工具为 [&quot;app&quot;]。当 ResourceUri 非空且本字段缺省时，按规范归一化为 [&quot;model&quot;,&quot;app&quot;]；存量非 Apps 工具保持为空。</p><p>枚举值：</p><ul><li>model： 支持model</li><li>app： 支持app</li></ul>
        :type Visibility: list of str
        """
        self._ResourceUri = None
        self._Visibility = None

    @property
    def ResourceUri(self):
        r"""<p>关联的 UI 资源 URI，ui:// scheme，格式为 ui://&lt;插件标识&gt;/&lt;资源名&gt;-&lt;版本&gt;。该字段是 MCP Apps 交互式界面的入口，非空时表示工具支持 Apps（&quot;文本 + 交互式界面&quot;展示），为空则为纯文本工具。由工具同步结果自动识别填充，不支持手工编辑。</p>
        :rtype: str
        """
        return self._ResourceUri

    @ResourceUri.setter
    def ResourceUri(self, ResourceUri):
        self._ResourceUri = ResourceUri

    @property
    def Visibility(self):
        r"""<p>工具的调用方可见性声明，取值范围：model（模型可调用）、app（应用界面可调用），可多选，如 [&quot;model&quot;,&quot;app&quot;]。与 ResourceUri 相互独立（SEP-1865），可单独存在，例如纯后端 app-only 工具为 [&quot;app&quot;]。当 ResourceUri 非空且本字段缺省时，按规范归一化为 [&quot;model&quot;,&quot;app&quot;]；存量非 Apps 工具保持为空。</p><p>枚举值：</p><ul><li>model： 支持model</li><li>app： 支持app</li></ul>
        :rtype: list of str
        """
        return self._Visibility

    @Visibility.setter
    def Visibility(self, Visibility):
        self._Visibility = Visibility


    def _deserialize(self, params):
        self._ResourceUri = params.get("ResourceUri")
        self._Visibility = params.get("Visibility")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManualOnlySchedule(AbstractModel):
    r"""ManualOnlySchedule

    """

    def __init__(self):
        r"""
        :param _Enabled: 启用
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""启用
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricOverview(AbstractModel):
    r"""总览 KPI 卡片指标项

    """

    def __init__(self):
        r"""
        :param _Key: <p>指标键，取值参考 MetricOverview 注释中的 key 白名单</p>
        :type Key: str
        :param _Mom: <p>环比百分比，无环比时填 0</p>
        :type Mom: float
        :param _Unit: <p>指标单位，枚举值 DosageUnit；key 与 unit 的对应关系参考 MetricOverview 注释白名单</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>DOSAGE_UNIT_TOKEN</td><td>0</td><td>token（默认）</td></tr><tr><td>DOSAGE_UNIT_PAGE_COUNT</td><td>1</td><td>page_count（页数）</td></tr><tr><td>DOSAGE_UNIT_TIMES</td><td>2</td><td>times（次数）</td></tr><tr><td>DOSAGE_UNIT_SECOND</td><td>3</td><td>second（秒）</td></tr><tr><td>DOSAGE_UNIT_ITEM</td><td>4</td><td>item（条）</td></tr><tr><td>DOSAGE_UNIT_SHEET</td><td>5</td><td>sheet（张）</td></tr><tr><td>DOSAGE_UNIT_CHARACTER</td><td>6</td><td>character（字符）</td></tr><tr><td>DOSAGE_UNIT_GB</td><td>7</td><td>GB</td></tr><tr><td>DOSAGE_UNIT_NUMBER</td><td>8</td><td>number（个数）</td></tr><tr><td>DOSAGE_UNIT_MILL_SECOND</td><td>9</td><td>mill_second（毫秒）</td></tr></tbody></table>
        :type Unit: int
        :param _Value: <p>指标数值</p>
        :type Value: float
        """
        self._Key = None
        self._Mom = None
        self._Unit = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>指标键，取值参考 MetricOverview 注释中的 key 白名单</p>
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Mom(self):
        r"""<p>环比百分比，无环比时填 0</p>
        :rtype: float
        """
        return self._Mom

    @Mom.setter
    def Mom(self, Mom):
        self._Mom = Mom

    @property
    def Unit(self):
        r"""<p>指标单位，枚举值 DosageUnit；key 与 unit 的对应关系参考 MetricOverview 注释白名单</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>DOSAGE_UNIT_TOKEN</td><td>0</td><td>token（默认）</td></tr><tr><td>DOSAGE_UNIT_PAGE_COUNT</td><td>1</td><td>page_count（页数）</td></tr><tr><td>DOSAGE_UNIT_TIMES</td><td>2</td><td>times（次数）</td></tr><tr><td>DOSAGE_UNIT_SECOND</td><td>3</td><td>second（秒）</td></tr><tr><td>DOSAGE_UNIT_ITEM</td><td>4</td><td>item（条）</td></tr><tr><td>DOSAGE_UNIT_SHEET</td><td>5</td><td>sheet（张）</td></tr><tr><td>DOSAGE_UNIT_CHARACTER</td><td>6</td><td>character（字符）</td></tr><tr><td>DOSAGE_UNIT_GB</td><td>7</td><td>GB</td></tr><tr><td>DOSAGE_UNIT_NUMBER</td><td>8</td><td>number（个数）</td></tr><tr><td>DOSAGE_UNIT_MILL_SECOND</td><td>9</td><td>mill_second（毫秒）</td></tr></tbody></table>
        :rtype: int
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        r"""<p>指标数值</p>
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Mom = params.get("Mom")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Model(AbstractModel):
    r"""模型完整信息

    """

    def __init__(self):
        r"""
        :param _BadgeList: <p>模型徽章列表</p>
        :type BadgeList: list of ModelBadge
        :param _LimitInfo: <p>模型限制信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LimitInfo: :class:`tencentcloud.adp.v20260520.models.ModelLimit`
        :param _ModelBasic: <p>模型基本信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelBasic: :class:`tencentcloud.adp.v20260520.models.ModelBasic`
        :param _ParameterList: <p>模型超参配置</p>
        :type ParameterList: list of ModelParameter
        :param _PropertyList: <p>模型属性配置</p>
        :type PropertyList: list of ModelProperty
        :param _ProviderInfo: <p>模型提供商信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ProviderInfo: :class:`tencentcloud.adp.v20260520.models.ModelProviderBasic`
        :param _StatusInfo: <p>模型状态信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInfo: :class:`tencentcloud.adp.v20260520.models.ModelStatus`
        :param _TagList: <p>模型标签列表</p>
        :type TagList: list of str
        :param _DeveloperInfo: <p>模型作者信息</p>
        :type DeveloperInfo: :class:`tencentcloud.adp.v20260520.models.ModelDeveloperBasic`
        """
        self._BadgeList = None
        self._LimitInfo = None
        self._ModelBasic = None
        self._ParameterList = None
        self._PropertyList = None
        self._ProviderInfo = None
        self._StatusInfo = None
        self._TagList = None
        self._DeveloperInfo = None

    @property
    def BadgeList(self):
        r"""<p>模型徽章列表</p>
        :rtype: list of ModelBadge
        """
        return self._BadgeList

    @BadgeList.setter
    def BadgeList(self, BadgeList):
        self._BadgeList = BadgeList

    @property
    def LimitInfo(self):
        r"""<p>模型限制信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelLimit`
        """
        return self._LimitInfo

    @LimitInfo.setter
    def LimitInfo(self, LimitInfo):
        self._LimitInfo = LimitInfo

    @property
    def ModelBasic(self):
        r"""<p>模型基本信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelBasic`
        """
        return self._ModelBasic

    @ModelBasic.setter
    def ModelBasic(self, ModelBasic):
        self._ModelBasic = ModelBasic

    @property
    def ParameterList(self):
        r"""<p>模型超参配置</p>
        :rtype: list of ModelParameter
        """
        return self._ParameterList

    @ParameterList.setter
    def ParameterList(self, ParameterList):
        self._ParameterList = ParameterList

    @property
    def PropertyList(self):
        r"""<p>模型属性配置</p>
        :rtype: list of ModelProperty
        """
        return self._PropertyList

    @PropertyList.setter
    def PropertyList(self, PropertyList):
        self._PropertyList = PropertyList

    @property
    def ProviderInfo(self):
        r"""<p>模型提供商信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelProviderBasic`
        """
        return self._ProviderInfo

    @ProviderInfo.setter
    def ProviderInfo(self, ProviderInfo):
        self._ProviderInfo = ProviderInfo

    @property
    def StatusInfo(self):
        r"""<p>模型状态信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelStatus`
        """
        return self._StatusInfo

    @StatusInfo.setter
    def StatusInfo(self, StatusInfo):
        self._StatusInfo = StatusInfo

    @property
    def TagList(self):
        r"""<p>模型标签列表</p>
        :rtype: list of str
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def DeveloperInfo(self):
        r"""<p>模型作者信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDeveloperBasic`
        """
        return self._DeveloperInfo

    @DeveloperInfo.setter
    def DeveloperInfo(self, DeveloperInfo):
        self._DeveloperInfo = DeveloperInfo


    def _deserialize(self, params):
        if params.get("BadgeList") is not None:
            self._BadgeList = []
            for item in params.get("BadgeList"):
                obj = ModelBadge()
                obj._deserialize(item)
                self._BadgeList.append(obj)
        if params.get("LimitInfo") is not None:
            self._LimitInfo = ModelLimit()
            self._LimitInfo._deserialize(params.get("LimitInfo"))
        if params.get("ModelBasic") is not None:
            self._ModelBasic = ModelBasic()
            self._ModelBasic._deserialize(params.get("ModelBasic"))
        if params.get("ParameterList") is not None:
            self._ParameterList = []
            for item in params.get("ParameterList"):
                obj = ModelParameter()
                obj._deserialize(item)
                self._ParameterList.append(obj)
        if params.get("PropertyList") is not None:
            self._PropertyList = []
            for item in params.get("PropertyList"):
                obj = ModelProperty()
                obj._deserialize(item)
                self._PropertyList.append(obj)
        if params.get("ProviderInfo") is not None:
            self._ProviderInfo = ModelProviderBasic()
            self._ProviderInfo._deserialize(params.get("ProviderInfo"))
        if params.get("StatusInfo") is not None:
            self._StatusInfo = ModelStatus()
            self._StatusInfo._deserialize(params.get("StatusInfo"))
        self._TagList = params.get("TagList")
        if params.get("DeveloperInfo") is not None:
            self._DeveloperInfo = ModelDeveloperBasic()
            self._DeveloperInfo._deserialize(params.get("DeveloperInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelBadge(AbstractModel):
    r"""模型徽章

    """

    def __init__(self):
        r"""
        :param _Text: 展示文案
        :type Text: str
        :param _Theme: 样式主题。1-信息（蓝色）, 2-成功（绿色）, 3-警告（橙色）, 4-危险（红色）
        :type Theme: int
        :param _Tips: tooltip文案，为空则不展示
        :type Tips: str
        :param _Type: 徽章类型。1-限时免费, 2-即将下线, 3-新模型, 4-热门
        :type Type: int
        """
        self._Text = None
        self._Theme = None
        self._Tips = None
        self._Type = None

    @property
    def Text(self):
        r"""展示文案
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Theme(self):
        r"""样式主题。1-信息（蓝色）, 2-成功（绿色）, 3-警告（橙色）, 4-危险（红色）
        :rtype: int
        """
        return self._Theme

    @Theme.setter
    def Theme(self, Theme):
        self._Theme = Theme

    @property
    def Tips(self):
        r"""tooltip文案，为空则不展示
        :rtype: str
        """
        return self._Tips

    @Tips.setter
    def Tips(self, Tips):
        self._Tips = Tips

    @property
    def Type(self):
        r"""徽章类型。1-限时免费, 2-即将下线, 3-新模型, 4-热门
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Theme = params.get("Theme")
        self._Tips = params.get("Tips")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelBasic(AbstractModel):
    r"""模型基本信息

    """

    def __init__(self):
        r"""
        :param _Description: 模型描述
        :type Description: str
        :param _IconUrl: 模型图标地址
        :type IconUrl: str
        :param _ModelId: 模型ID
        :type ModelId: str
        :param _ModelType: 模型类型。1-LLM模型, 2-Rerank模型, 3-Embedding模型, 4-文档解析模型
        :type ModelType: int
        :param _Name: 模型名称
        :type Name: str
        """
        self._Description = None
        self._IconUrl = None
        self._ModelId = None
        self._ModelType = None
        self._Name = None

    @property
    def Description(self):
        r"""模型描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IconUrl(self):
        r"""模型图标地址
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

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
    def ModelType(self):
        r"""模型类型。1-LLM模型, 2-Rerank模型, 3-Embedding模型, 4-文档解析模型
        :rtype: int
        """
        return self._ModelType

    @ModelType.setter
    def ModelType(self, ModelType):
        self._ModelType = ModelType

    @property
    def Name(self):
        r"""模型名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._IconUrl = params.get("IconUrl")
        self._ModelId = params.get("ModelId")
        self._ModelType = params.get("ModelType")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelDetailInfo(AbstractModel):
    r"""模型详细信息

    """

    def __init__(self):
        r"""
        :param _Alias: 模型别名
        :type Alias: str
        :param _HistoryLimit: 历史对话条数限制
        :type HistoryLimit: int
        :param _ModelId: 模型唯一 ID
        :type ModelId: str
        :param _ModelParams: 模型参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ModelParams: :class:`tencentcloud.adp.v20260520.models.ModelParams`
        """
        self._Alias = None
        self._HistoryLimit = None
        self._ModelId = None
        self._ModelParams = None

    @property
    def Alias(self):
        r"""模型别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def HistoryLimit(self):
        r"""历史对话条数限制
        :rtype: int
        """
        return self._HistoryLimit

    @HistoryLimit.setter
    def HistoryLimit(self, HistoryLimit):
        self._HistoryLimit = HistoryLimit

    @property
    def ModelId(self):
        r"""模型唯一 ID
        :rtype: str
        """
        return self._ModelId

    @ModelId.setter
    def ModelId(self, ModelId):
        self._ModelId = ModelId

    @property
    def ModelParams(self):
        r"""模型参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelParams`
        """
        return self._ModelParams

    @ModelParams.setter
    def ModelParams(self, ModelParams):
        self._ModelParams = ModelParams


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._HistoryLimit = params.get("HistoryLimit")
        self._ModelId = params.get("ModelId")
        if params.get("ModelParams") is not None:
            self._ModelParams = ModelParams()
            self._ModelParams._deserialize(params.get("ModelParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelDeveloperBasic(AbstractModel):
    r"""模型作者信息

    """

    def __init__(self):
        r"""
        :param _Name: <p>作者标识</p>
        :type Name: str
        :param _Alias: <p>作者显示名称</p>
        :type Alias: str
        """
        self._Name = None
        self._Alias = None

    @property
    def Name(self):
        r"""<p>作者标识</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Alias(self):
        r"""<p>作者显示名称</p>
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelLimit(AbstractModel):
    r"""模型限制信息

    """

    def __init__(self):
        r"""
        :param _ContextLengthDescription: 模型上下文长度展示文案（如 "128K"、"1000K"）
        :type ContextLengthDescription: str
        :param _InputLengthLimit: 模型对话框输入长度字符数限制
        :type InputLengthLimit: int
        :param _PromptLengthLimit: 模型提示词长度字符数限制
        :type PromptLengthLimit: int
        """
        self._ContextLengthDescription = None
        self._InputLengthLimit = None
        self._PromptLengthLimit = None

    @property
    def ContextLengthDescription(self):
        r"""模型上下文长度展示文案（如 "128K"、"1000K"）
        :rtype: str
        """
        return self._ContextLengthDescription

    @ContextLengthDescription.setter
    def ContextLengthDescription(self, ContextLengthDescription):
        self._ContextLengthDescription = ContextLengthDescription

    @property
    def InputLengthLimit(self):
        r"""模型对话框输入长度字符数限制
        :rtype: int
        """
        return self._InputLengthLimit

    @InputLengthLimit.setter
    def InputLengthLimit(self, InputLengthLimit):
        self._InputLengthLimit = InputLengthLimit

    @property
    def PromptLengthLimit(self):
        r"""模型提示词长度字符数限制
        :rtype: int
        """
        return self._PromptLengthLimit

    @PromptLengthLimit.setter
    def PromptLengthLimit(self, PromptLengthLimit):
        self._PromptLengthLimit = PromptLengthLimit


    def _deserialize(self, params):
        self._ContextLengthDescription = params.get("ContextLengthDescription")
        self._InputLengthLimit = params.get("InputLengthLimit")
        self._PromptLengthLimit = params.get("PromptLengthLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelParameter(AbstractModel):
    r"""模型超参

    """

    def __init__(self):
        r"""
        :param _DefaultValue: <p>默认值</p>
        :type DefaultValue: str
        :param _EnumValueList: <p>可选值列表</p>
        :type EnumValueList: list of str
        :param _MaxValue: <p>最大值（仅数值类型有效）</p>
        :type MaxValue: float
        :param _MinValue: <p>最小值（仅数值类型有效）</p>
        :type MinValue: float
        :param _Name: <p>超参名称</p>
        :type Name: str
        :param _Type: <p>超参类型。1-浮点数, 2-整数, 3-字符串</p>
        :type Type: int
        """
        self._DefaultValue = None
        self._EnumValueList = None
        self._MaxValue = None
        self._MinValue = None
        self._Name = None
        self._Type = None

    @property
    def DefaultValue(self):
        r"""<p>默认值</p>
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def EnumValueList(self):
        r"""<p>可选值列表</p>
        :rtype: list of str
        """
        return self._EnumValueList

    @EnumValueList.setter
    def EnumValueList(self, EnumValueList):
        self._EnumValueList = EnumValueList

    @property
    def MaxValue(self):
        r"""<p>最大值（仅数值类型有效）</p>
        :rtype: float
        """
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def MinValue(self):
        r"""<p>最小值（仅数值类型有效）</p>
        :rtype: float
        """
        return self._MinValue

    @MinValue.setter
    def MinValue(self, MinValue):
        self._MinValue = MinValue

    @property
    def Name(self):
        r"""<p>超参名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>超参类型。1-浮点数, 2-整数, 3-字符串</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._DefaultValue = params.get("DefaultValue")
        self._EnumValueList = params.get("EnumValueList")
        self._MaxValue = params.get("MaxValue")
        self._MinValue = params.get("MinValue")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelParams(AbstractModel):
    r"""模型参数

    """

    def __init__(self):
        r"""
        :param _DeepThinking: 是否开启深度思考
        :type DeepThinking: str
        :param _FrequencyPenalty: 频率惩罚
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyPenalty: float
        :param _MaxTokens: 最大输出长度
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxTokens: int
        :param _PresencePenalty: 存在惩罚
注意：此字段可能返回 null，表示取不到有效值。
        :type PresencePenalty: float
        :param _ReasoningEffort: 深度思考效果
        :type ReasoningEffort: str
        :param _RepetitionPenalty: 重复惩罚
注意：此字段可能返回 null，表示取不到有效值。
        :type RepetitionPenalty: float
        :param _ReplyFormat: 输出格式（text、json_object）
        :type ReplyFormat: str
        :param _Seed: seed 随机种子
注意：此字段可能返回 null，表示取不到有效值。
        :type Seed: int
        :param _StopSequenceList: 停止序列
        :type StopSequenceList: list of str
        :param _Temperature: 温度
注意：此字段可能返回 null，表示取不到有效值。
        :type Temperature: float
        :param _TopP: top_p
注意：此字段可能返回 null，表示取不到有效值。
        :type TopP: float
        """
        self._DeepThinking = None
        self._FrequencyPenalty = None
        self._MaxTokens = None
        self._PresencePenalty = None
        self._ReasoningEffort = None
        self._RepetitionPenalty = None
        self._ReplyFormat = None
        self._Seed = None
        self._StopSequenceList = None
        self._Temperature = None
        self._TopP = None

    @property
    def DeepThinking(self):
        r"""是否开启深度思考
        :rtype: str
        """
        return self._DeepThinking

    @DeepThinking.setter
    def DeepThinking(self, DeepThinking):
        self._DeepThinking = DeepThinking

    @property
    def FrequencyPenalty(self):
        r"""频率惩罚
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._FrequencyPenalty

    @FrequencyPenalty.setter
    def FrequencyPenalty(self, FrequencyPenalty):
        self._FrequencyPenalty = FrequencyPenalty

    @property
    def MaxTokens(self):
        r"""最大输出长度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def PresencePenalty(self):
        r"""存在惩罚
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._PresencePenalty

    @PresencePenalty.setter
    def PresencePenalty(self, PresencePenalty):
        self._PresencePenalty = PresencePenalty

    @property
    def ReasoningEffort(self):
        r"""深度思考效果
        :rtype: str
        """
        return self._ReasoningEffort

    @ReasoningEffort.setter
    def ReasoningEffort(self, ReasoningEffort):
        self._ReasoningEffort = ReasoningEffort

    @property
    def RepetitionPenalty(self):
        r"""重复惩罚
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._RepetitionPenalty

    @RepetitionPenalty.setter
    def RepetitionPenalty(self, RepetitionPenalty):
        self._RepetitionPenalty = RepetitionPenalty

    @property
    def ReplyFormat(self):
        r"""输出格式（text、json_object）
        :rtype: str
        """
        return self._ReplyFormat

    @ReplyFormat.setter
    def ReplyFormat(self, ReplyFormat):
        self._ReplyFormat = ReplyFormat

    @property
    def Seed(self):
        r"""seed 随机种子
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def StopSequenceList(self):
        r"""停止序列
        :rtype: list of str
        """
        return self._StopSequenceList

    @StopSequenceList.setter
    def StopSequenceList(self, StopSequenceList):
        self._StopSequenceList = StopSequenceList

    @property
    def Temperature(self):
        r"""温度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def TopP(self):
        r"""top_p
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP


    def _deserialize(self, params):
        self._DeepThinking = params.get("DeepThinking")
        self._FrequencyPenalty = params.get("FrequencyPenalty")
        self._MaxTokens = params.get("MaxTokens")
        self._PresencePenalty = params.get("PresencePenalty")
        self._ReasoningEffort = params.get("ReasoningEffort")
        self._RepetitionPenalty = params.get("RepetitionPenalty")
        self._ReplyFormat = params.get("ReplyFormat")
        self._Seed = params.get("Seed")
        self._StopSequenceList = params.get("StopSequenceList")
        self._Temperature = params.get("Temperature")
        self._TopP = params.get("TopP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelProperty(AbstractModel):
    r"""模型属性

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称
        :type Name: str
        :param _Value: 属性值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""属性名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""属性值
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
        


class ModelProviderBasic(AbstractModel):
    r"""模型提供商基本信息

    """

    def __init__(self):
        r"""
        :param _Alias: 模型提供商别名
        :type Alias: str
        :param _Name: 模型提供商名称
        :type Name: str
        :param _ProviderType: 模型提供商类型。1-自有提供商, 2-自定义模型提供商, 3-第三方模型提供商
        :type ProviderType: int
        """
        self._Alias = None
        self._Name = None
        self._ProviderType = None

    @property
    def Alias(self):
        r"""模型提供商别名
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Name(self):
        r"""模型提供商名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProviderType(self):
        r"""模型提供商类型。1-自有提供商, 2-自定义模型提供商, 3-第三方模型提供商
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Name = params.get("Name")
        self._ProviderType = params.get("ProviderType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelStatus(AbstractModel):
    r"""模型状态信息

    """

    def __init__(self):
        r"""
        :param _Concurrency: 专属并发数
        :type Concurrency: int
        :param _IsExclusive: 是否专属并发
        :type IsExclusive: bool
        :param _ResourceStatus: 资源状态。1-资源可用, 2-资源已用尽
        :type ResourceStatus: int
        """
        self._Concurrency = None
        self._IsExclusive = None
        self._ResourceStatus = None

    @property
    def Concurrency(self):
        r"""专属并发数
        :rtype: int
        """
        return self._Concurrency

    @Concurrency.setter
    def Concurrency(self, Concurrency):
        self._Concurrency = Concurrency

    @property
    def IsExclusive(self):
        r"""是否专属并发
        :rtype: bool
        """
        return self._IsExclusive

    @IsExclusive.setter
    def IsExclusive(self, IsExclusive):
        self._IsExclusive = IsExclusive

    @property
    def ResourceStatus(self):
        r"""资源状态。1-资源可用, 2-资源已用尽
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus


    def _deserialize(self, params):
        self._Concurrency = params.get("Concurrency")
        self._IsExclusive = params.get("IsExclusive")
        self._ResourceStatus = params.get("ResourceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelUsageDetail(AbstractModel):
    r"""模型调用明细

    """

    def __init__(self):
        r"""
        :param _CallType: <p>调用类型，来源于计费 scene_billing（与 filter.call_type 对应）</p>
        :type CallType: str
        :param _IsDefaultKB: <p>是否默认知识库</p>
        :type IsDefaultKB: bool
        :param _ModelName: <p>模型名称</p>
        :type ModelName: str
        :param _ResourceConsumptionList: <p>MODEL 域单次调用的消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*/cache_*），label 为空表示 total_tokens；unit=PAGE_COUNT 表示模型消耗页数</p>
        :type ResourceConsumptionList: list of ResourceConsumption
        :param _ConsumptionPU: <p>本次调用消耗 PU 量</p>
        :type ConsumptionPU: float
        """
        self._CallType = None
        self._IsDefaultKB = None
        self._ModelName = None
        self._ResourceConsumptionList = None
        self._ConsumptionPU = None

    @property
    def CallType(self):
        r"""<p>调用类型，来源于计费 scene_billing（与 filter.call_type 对应）</p>
        :rtype: str
        """
        return self._CallType

    @CallType.setter
    def CallType(self, CallType):
        self._CallType = CallType

    @property
    def IsDefaultKB(self):
        r"""<p>是否默认知识库</p>
        :rtype: bool
        """
        return self._IsDefaultKB

    @IsDefaultKB.setter
    def IsDefaultKB(self, IsDefaultKB):
        self._IsDefaultKB = IsDefaultKB

    @property
    def ModelName(self):
        r"""<p>模型名称</p>
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ResourceConsumptionList(self):
        r"""<p>MODEL 域单次调用的消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*/cache_*），label 为空表示 total_tokens；unit=PAGE_COUNT 表示模型消耗页数</p>
        :rtype: list of ResourceConsumption
        """
        return self._ResourceConsumptionList

    @ResourceConsumptionList.setter
    def ResourceConsumptionList(self, ResourceConsumptionList):
        self._ResourceConsumptionList = ResourceConsumptionList

    @property
    def ConsumptionPU(self):
        r"""<p>本次调用消耗 PU 量</p>
        :rtype: float
        """
        return self._ConsumptionPU

    @ConsumptionPU.setter
    def ConsumptionPU(self, ConsumptionPU):
        self._ConsumptionPU = ConsumptionPU


    def _deserialize(self, params):
        self._CallType = params.get("CallType")
        self._IsDefaultKB = params.get("IsDefaultKB")
        self._ModelName = params.get("ModelName")
        if params.get("ResourceConsumptionList") is not None:
            self._ResourceConsumptionList = []
            for item in params.get("ResourceConsumptionList"):
                obj = ResourceConsumption()
                obj._deserialize(item)
                self._ResourceConsumptionList.append(obj)
        self._ConsumptionPU = params.get("ConsumptionPU")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModelUsageSummary(AbstractModel):
    r"""模型资源用量聚合明细（MODEL 域专属）

    """

    def __init__(self):
        r"""
        :param _CallCount: <p>调用次数（业务调用维度的顶层计数）</p>
        :type CallCount: float
        :param _IsDefaultKB: <p>是否默认知识库</p>
        :type IsDefaultKB: bool
        :param _ModelName: <p>模型名称，标识使用的 AI 模型</p>
        :type ModelName: str
        :param _ResourceConsumptionList: <p>MODEL 域消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*/cache_*），label 为空表示 total_tokens；unit=PAGE_COUNT 表示模型消耗页数</p>
        :type ResourceConsumptionList: list of ResourceConsumption
        :param _ConsumptionPU: <p>模型消耗 PU 总量（聚合维度内的 PU 消耗之和）</p>
        :type ConsumptionPU: float
        """
        self._CallCount = None
        self._IsDefaultKB = None
        self._ModelName = None
        self._ResourceConsumptionList = None
        self._ConsumptionPU = None

    @property
    def CallCount(self):
        r"""<p>调用次数（业务调用维度的顶层计数）</p>
        :rtype: float
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def IsDefaultKB(self):
        r"""<p>是否默认知识库</p>
        :rtype: bool
        """
        return self._IsDefaultKB

    @IsDefaultKB.setter
    def IsDefaultKB(self, IsDefaultKB):
        self._IsDefaultKB = IsDefaultKB

    @property
    def ModelName(self):
        r"""<p>模型名称，标识使用的 AI 模型</p>
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ResourceConsumptionList(self):
        r"""<p>MODEL 域消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*/cache_*），label 为空表示 total_tokens；unit=PAGE_COUNT 表示模型消耗页数</p>
        :rtype: list of ResourceConsumption
        """
        return self._ResourceConsumptionList

    @ResourceConsumptionList.setter
    def ResourceConsumptionList(self, ResourceConsumptionList):
        self._ResourceConsumptionList = ResourceConsumptionList

    @property
    def ConsumptionPU(self):
        r"""<p>模型消耗 PU 总量（聚合维度内的 PU 消耗之和）</p>
        :rtype: float
        """
        return self._ConsumptionPU

    @ConsumptionPU.setter
    def ConsumptionPU(self, ConsumptionPU):
        self._ConsumptionPU = ConsumptionPU


    def _deserialize(self, params):
        self._CallCount = params.get("CallCount")
        self._IsDefaultKB = params.get("IsDefaultKB")
        self._ModelName = params.get("ModelName")
        if params.get("ResourceConsumptionList") is not None:
            self._ResourceConsumptionList = []
            for item in params.get("ResourceConsumptionList"):
                obj = ResourceConsumption()
                obj._deserialize(item)
                self._ResourceConsumptionList.append(obj)
        self._ConsumptionPU = params.get("ConsumptionPU")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentRequest(AbstractModel):
    r"""ModifyAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用Id</p>
        :type AppId: str
        :param _AgentId: <p>Agent Id</p>
        :type AgentId: str
        :param _Agent: <p>修改后的Agent的信息</p>
        :type Agent: :class:`tencentcloud.adp.v20260520.models.AgentSpec`
        :param _UpdateMask: <p>需要更新的字段路径，如 ["Profile.Name", "Profile.IconUrl", "Instructions", "Model", "ToolList", "PluginList", "SkillList", "AdvancedConfig"]</p>
        :type UpdateMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        self._AppId = None
        self._AgentId = None
        self._Agent = None
        self._UpdateMask = None

    @property
    def AppId(self):
        r"""<p>应用Id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AgentId(self):
        r"""<p>Agent Id</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        self._AgentId = AgentId

    @property
    def Agent(self):
        r"""<p>修改后的Agent的信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentSpec`
        """
        return self._Agent

    @Agent.setter
    def Agent(self, Agent):
        self._Agent = Agent

    @property
    def UpdateMask(self):
        r"""<p>需要更新的字段路径，如 ["Profile.Name", "Profile.IconUrl", "Instructions", "Model", "ToolList", "PluginList", "SkillList", "AdvancedConfig"]</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._UpdateMask

    @UpdateMask.setter
    def UpdateMask(self, UpdateMask):
        self._UpdateMask = UpdateMask


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AgentId = params.get("AgentId")
        if params.get("Agent") is not None:
            self._Agent = AgentSpec()
            self._Agent._deserialize(params.get("Agent"))
        if params.get("UpdateMask") is not None:
            self._UpdateMask = FieldMask()
            self._UpdateMask._deserialize(params.get("UpdateMask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAgentResponse(AbstractModel):
    r"""ModifyAgent返回参数结构体

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


class ModifyAppRequest(AbstractModel):
    r"""ModifyApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _AppMode: <p>应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式</p>
        :type AppMode: int
        :param _Avatar: <p>应用头像</p>
        :type Avatar: str
        :param _Config: <p>应用配置</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        :param _Description: <p>应用描述</p>
        :type Description: str
        :param _Name: <p>应用名称</p>
        :type Name: str
        :param _SharedKbIdList: <p>引用的共享知识库ID列表(全量覆盖)</p>
        :type SharedKbIdList: list of str
        :param _UpdateMask: <p>字段掩码，指定需要更新的字段(Paths为空则不更新任何字段)。Paths枚举值：<br>【顶层】Name, Avatar, Description, AppMode, SharedKbIdList<br>【Greeting】Config.Greeting, Config.Greeting.Greeting, Config.Greeting.OpeningQuestionList<br>【Model】Config.Model, Config.Model.ThinkModel, Config.Model.GenerateModel, Config.Model.AiOptimizeModel, Config.Model.FileParseModel, Config.Model.PromptRewriteModel, Config.Model.MultiModalQaModel, Config.Model.MultiModalUnderstandingModel<br>【WebSearch】Config.WebSearch<br>【Memory】Config.Memory, Config.Memory.Enabled, Config.Memory.LongMemoryDay, Config.Memory.Model, Config.Memory.PromptMode, Config.Memory.PromptContent<br>【Mode】Config.Mode, Config.Mode.MultiAgentConfig, Config.Mode.SingleWorkflowConfig, Config.Mode.ClawAgentConfig<br>【Mode.ClawAgentConfig】Config.Mode.ClawAgentConfig.LongMemoryConfig, Config.Mode.ClawAgentConfig.AgentTeamConfig<br>【Experience】Config.Experience, Config.Experience.Conversation, Config.Experience.Role, Config.Experience.Advanced<br>【Experience.Conversation】Config.Experience.Conversation.AiCall, Config.Experience.Conversation.BackgroundImage, Config.Experience.Conversation.Method, Config.Experience.Conversation.FallbackReply, Config.Experience.Conversation.Recommended, Config.Experience.Conversation.InputBoxConfig, Config.Experience.Conversation.WebSearch<br>【Experience.Conversation.AiCall】Config.Experience.Conversation.AiCall.VoiceInteract, Config.Experience.Conversation.AiCall.VoiceCall, Config.Experience.Conversation.AiCall.DigitalHuman<br>【Experience.Advanced】Config.Experience.Advanced.ContextRewrite, Config.Experience.Advanced.ImageTextRetrieval, Config.Experience.Advanced.IntentAchievement, Config.Experience.Advanced.ReplyFlexibility, Config.Experience.Advanced.DialogCustomConfig</p>
        :type UpdateMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        self._AppId = None
        self._AppMode = None
        self._Avatar = None
        self._Config = None
        self._Description = None
        self._Name = None
        self._SharedKbIdList = None
        self._UpdateMask = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppMode(self):
        r"""<p>应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式</p>
        :rtype: int
        """
        return self._AppMode

    @AppMode.setter
    def AppMode(self, AppMode):
        self._AppMode = AppMode

    @property
    def Avatar(self):
        r"""<p>应用头像</p>
        :rtype: str
        """
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Config(self):
        r"""<p>应用配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Description(self):
        r"""<p>应用描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""<p>应用名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SharedKbIdList(self):
        r"""<p>引用的共享知识库ID列表(全量覆盖)</p>
        :rtype: list of str
        """
        return self._SharedKbIdList

    @SharedKbIdList.setter
    def SharedKbIdList(self, SharedKbIdList):
        self._SharedKbIdList = SharedKbIdList

    @property
    def UpdateMask(self):
        r"""<p>字段掩码，指定需要更新的字段(Paths为空则不更新任何字段)。Paths枚举值：<br>【顶层】Name, Avatar, Description, AppMode, SharedKbIdList<br>【Greeting】Config.Greeting, Config.Greeting.Greeting, Config.Greeting.OpeningQuestionList<br>【Model】Config.Model, Config.Model.ThinkModel, Config.Model.GenerateModel, Config.Model.AiOptimizeModel, Config.Model.FileParseModel, Config.Model.PromptRewriteModel, Config.Model.MultiModalQaModel, Config.Model.MultiModalUnderstandingModel<br>【WebSearch】Config.WebSearch<br>【Memory】Config.Memory, Config.Memory.Enabled, Config.Memory.LongMemoryDay, Config.Memory.Model, Config.Memory.PromptMode, Config.Memory.PromptContent<br>【Mode】Config.Mode, Config.Mode.MultiAgentConfig, Config.Mode.SingleWorkflowConfig, Config.Mode.ClawAgentConfig<br>【Mode.ClawAgentConfig】Config.Mode.ClawAgentConfig.LongMemoryConfig, Config.Mode.ClawAgentConfig.AgentTeamConfig<br>【Experience】Config.Experience, Config.Experience.Conversation, Config.Experience.Role, Config.Experience.Advanced<br>【Experience.Conversation】Config.Experience.Conversation.AiCall, Config.Experience.Conversation.BackgroundImage, Config.Experience.Conversation.Method, Config.Experience.Conversation.FallbackReply, Config.Experience.Conversation.Recommended, Config.Experience.Conversation.InputBoxConfig, Config.Experience.Conversation.WebSearch<br>【Experience.Conversation.AiCall】Config.Experience.Conversation.AiCall.VoiceInteract, Config.Experience.Conversation.AiCall.VoiceCall, Config.Experience.Conversation.AiCall.DigitalHuman<br>【Experience.Advanced】Config.Experience.Advanced.ContextRewrite, Config.Experience.Advanced.ImageTextRetrieval, Config.Experience.Advanced.IntentAchievement, Config.Experience.Advanced.ReplyFlexibility, Config.Experience.Advanced.DialogCustomConfig</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._UpdateMask

    @UpdateMask.setter
    def UpdateMask(self, UpdateMask):
        self._UpdateMask = UpdateMask


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._AppMode = params.get("AppMode")
        self._Avatar = params.get("Avatar")
        if params.get("Config") is not None:
            self._Config = AppConfig()
            self._Config._deserialize(params.get("Config"))
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._SharedKbIdList = params.get("SharedKbIdList")
        if params.get("UpdateMask") is not None:
            self._UpdateMask = FieldMask()
            self._UpdateMask._deserialize(params.get("UpdateMask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppResponse(AbstractModel):
    r"""ModifyApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>app_id</p>
        :type AppId: str
        :param _UpdateTime: <p>更新时间 (Unix时间戳,秒级)</p>
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def AppId(self):
        r"""<p>app_id</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def UpdateTime(self):
        r"""<p>更新时间 (Unix时间戳,秒级)</p>
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
        self._AppId = params.get("AppId")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ModifyAppTriggerRequest(AbstractModel):
    r"""ModifyAppTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _Trigger: <p>触发器信息</p>
        :type Trigger: :class:`tencentcloud.adp.v20260520.models.AppTrigger`
        :param _TriggerId: <p>触发器唯一ID</p>
        :type TriggerId: str
        :param _UpdateMask: <p>修改字段</p>
        :type UpdateMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._Scope = None
        self._Trigger = None
        self._TriggerId = None
        self._UpdateMask = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Trigger(self):
        r"""<p>触发器信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTrigger`
        """
        return self._Trigger

    @Trigger.setter
    def Trigger(self, Trigger):
        self._Trigger = Trigger

    @property
    def TriggerId(self):
        r"""<p>触发器唯一ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UpdateMask(self):
        r"""<p>修改字段</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._UpdateMask

    @UpdateMask.setter
    def UpdateMask(self, UpdateMask):
        self._UpdateMask = UpdateMask

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Scope = params.get("Scope")
        if params.get("Trigger") is not None:
            self._Trigger = AppTrigger()
            self._Trigger._deserialize(params.get("Trigger"))
        self._TriggerId = params.get("TriggerId")
        if params.get("UpdateMask") is not None:
            self._UpdateMask = FieldMask()
            self._UpdateMask._deserialize(params.get("UpdateMask"))
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAppTriggerResponse(AbstractModel):
    r"""ModifyAppTrigger返回参数结构体

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


class ModifyConversationRequest(AbstractModel):
    r"""ModifyConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>登录用户子账号(集成商模式必填)</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>登录用户主账号(集成商模式必填)</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        :param _ConversationId: 会话ID
        :type ConversationId: str
        :param _Title: 会话标题
        :type Title: str
        """
        self._Type = None
        self._AppId = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None
        self._UserId = None
        self._ConversationId = None
        self._Title = None

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>登录用户子账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>登录用户主账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ConversationId(self):
        r"""会话ID
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def Title(self):
        r"""会话标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._AppId = params.get("AppId")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        self._ConversationId = params.get("ConversationId")
        self._Title = params.get("Title")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConversationResponse(AbstractModel):
    r"""ModifyConversation返回参数结构体

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


class ModifyMsgRecordCategoryRequest(AbstractModel):
    r"""ModifyMsgRecordCategory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用 ID</p>
        :type AppId: str
        :param _CategoryId: <p>待修改的分类业务 ID</p>
        :type CategoryId: str
        :param _Name: <p>修改后的分类名称</p>
        :type Name: str
        """
        self._AppId = None
        self._CategoryId = None
        self._Name = None

    @property
    def AppId(self):
        r"""<p>应用 ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CategoryId(self):
        r"""<p>待修改的分类业务 ID</p>
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def Name(self):
        r"""<p>修改后的分类名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._CategoryId = params.get("CategoryId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMsgRecordCategoryResponse(AbstractModel):
    r"""ModifyMsgRecordCategory返回参数结构体

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


class ModifyPluginRequest(AbstractModel):
    r"""ModifyPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _PluginVersion: <p>插件版本号</p>
        :type PluginVersion: int
        :param _Profile: <p>插件基础资料</p>
        :type Profile: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        :param _Config: <p>插件类型配置</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        :param _UpdateMask: <p>指定需要更新的字段，避免全量覆盖</p>
        :type UpdateMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        :param _ToolList: <p>插件的工具列表，mcp插件不传</p>
        :type ToolList: list of Tool
        :param _LoginUin: <p>登录用户主账号(集成商模式必填)</p>
        :type LoginUin: str
        :param _LoginSubAccountUin: <p>登录用户子账号(集成商模式必填)</p>
        :type LoginSubAccountUin: str
        """
        self._PluginId = None
        self._PluginVersion = None
        self._Profile = None
        self._Config = None
        self._UpdateMask = None
        self._ToolList = None
        self._LoginUin = None
        self._LoginSubAccountUin = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginVersion(self):
        r"""<p>插件版本号</p>
        :rtype: int
        """
        return self._PluginVersion

    @PluginVersion.setter
    def PluginVersion(self, PluginVersion):
        self._PluginVersion = PluginVersion

    @property
    def Profile(self):
        r"""<p>插件基础资料</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Config(self):
        r"""<p>插件类型配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def UpdateMask(self):
        r"""<p>指定需要更新的字段，避免全量覆盖</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._UpdateMask

    @UpdateMask.setter
    def UpdateMask(self, UpdateMask):
        self._UpdateMask = UpdateMask

    @property
    def ToolList(self):
        r"""<p>插件的工具列表，mcp插件不传</p>
        :rtype: list of Tool
        """
        return self._ToolList

    @ToolList.setter
    def ToolList(self, ToolList):
        self._ToolList = ToolList

    @property
    def LoginUin(self):
        r"""<p>登录用户主账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def LoginSubAccountUin(self):
        r"""<p>登录用户子账号(集成商模式必填)</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginVersion = params.get("PluginVersion")
        if params.get("Profile") is not None:
            self._Profile = PluginProfile()
            self._Profile._deserialize(params.get("Profile"))
        if params.get("Config") is not None:
            self._Config = PluginConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("UpdateMask") is not None:
            self._UpdateMask = FieldMask()
            self._UpdateMask._deserialize(params.get("UpdateMask"))
        if params.get("ToolList") is not None:
            self._ToolList = []
            for item in params.get("ToolList"):
                obj = Tool()
                obj._deserialize(item)
                self._ToolList.append(obj)
        self._LoginUin = params.get("LoginUin")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPluginResponse(AbstractModel):
    r"""ModifyPlugin返回参数结构体

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


class ModifySkillRequest(AbstractModel):
    r"""ModifySkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>SkillId</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        :param _DisplayDescription: <p>skill描述</p>
        :type DisplayDescription: str
        :param _DisplayName: <p>skill名称</p>
        :type DisplayName: str
        :param _FileUrl: <p>skill包文件地址（zip）；传入则触发新版本生成，需与SkillVersion、UpdateDescription配套传入</p>
        :type FileUrl: str
        :param _IconUrl: <p>图标地址</p>
        :type IconUrl: str
        :param _SkillVersion: <p>skill版本号（与FileUrl配套传入）</p>
        :type SkillVersion: str
        :param _UpdateDescription: <p>版本变更说明（与FileUrl配套传入）</p>
        :type UpdateDescription: str
        """
        self._SkillId = None
        self._SpaceId = None
        self._DisplayDescription = None
        self._DisplayName = None
        self._FileUrl = None
        self._IconUrl = None
        self._SkillVersion = None
        self._UpdateDescription = None

    @property
    def SkillId(self):
        r"""<p>SkillId</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def DisplayDescription(self):
        r"""<p>skill描述</p>
        :rtype: str
        """
        return self._DisplayDescription

    @DisplayDescription.setter
    def DisplayDescription(self, DisplayDescription):
        self._DisplayDescription = DisplayDescription

    @property
    def DisplayName(self):
        r"""<p>skill名称</p>
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def FileUrl(self):
        r"""<p>skill包文件地址（zip）；传入则触发新版本生成，需与SkillVersion、UpdateDescription配套传入</p>
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def IconUrl(self):
        r"""<p>图标地址</p>
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def SkillVersion(self):
        r"""<p>skill版本号（与FileUrl配套传入）</p>
        :rtype: str
        """
        return self._SkillVersion

    @SkillVersion.setter
    def SkillVersion(self, SkillVersion):
        self._SkillVersion = SkillVersion

    @property
    def UpdateDescription(self):
        r"""<p>版本变更说明（与FileUrl配套传入）</p>
        :rtype: str
        """
        return self._UpdateDescription

    @UpdateDescription.setter
    def UpdateDescription(self, UpdateDescription):
        self._UpdateDescription = UpdateDescription


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        self._DisplayDescription = params.get("DisplayDescription")
        self._DisplayName = params.get("DisplayName")
        self._FileUrl = params.get("FileUrl")
        self._IconUrl = params.get("IconUrl")
        self._SkillVersion = params.get("SkillVersion")
        self._UpdateDescription = params.get("UpdateDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySkillResponse(AbstractModel):
    r"""ModifySkill返回参数结构体

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


class ModifySpaceRequest(AbstractModel):
    r"""ModifySpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 工作空间名称,长度最大30个字符
        :type Name: str
        :param _Description: 空间描述，长度最大150个字符
        :type Description: str
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _FieldMask: 指定需要更新的字段，支持Name和Description
        :type FieldMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        self._Name = None
        self._Description = None
        self._SpaceId = None
        self._FieldMask = None

    @property
    def Name(self):
        r"""工作空间名称,长度最大30个字符
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""空间描述，长度最大150个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SpaceId(self):
        r"""空间id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def FieldMask(self):
        r"""指定需要更新的字段，支持Name和Description
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._FieldMask

    @FieldMask.setter
    def FieldMask(self, FieldMask):
        self._FieldMask = FieldMask


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._SpaceId = params.get("SpaceId")
        if params.get("FieldMask") is not None:
            self._FieldMask = FieldMask()
            self._FieldMask._deserialize(params.get("FieldMask"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySpaceResponse(AbstractModel):
    r"""ModifySpace返回参数结构体

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


class ModifyVariableRequest(AbstractModel):
    r"""ModifyVariable请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _Variable: 变量信息
        :type Variable: :class:`tencentcloud.adp.v20260520.models.Variable`
        """
        self._AppId = None
        self._Variable = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Variable(self):
        r"""变量信息
        :rtype: :class:`tencentcloud.adp.v20260520.models.Variable`
        """
        return self._Variable

    @Variable.setter
    def Variable(self, Variable):
        self._Variable = Variable


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        if params.get("Variable") is not None:
            self._Variable = Variable()
            self._Variable._deserialize(params.get("Variable"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVariableResponse(AbstractModel):
    r"""ModifyVariable返回参数结构体

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


class MsgRecord(AbstractModel):
    r"""MsgRecord

    """

    def __init__(self):
        r"""
        :param _Answer: 答案
        :type Answer: str
        :param _AppId: 应用ID
        :type AppId: str
        :param _CategoryId: 分类ID
        :type CategoryId: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _Intent: 意图
        :type Intent: str
        :param _IntentCategory: 意图分类
        :type IntentCategory: str
        :param _IsSmart: 是否是智能分类
        :type IsSmart: bool
        :param _Question: 问题
        :type Question: str
        :param _RecordId: 记录ID
        :type RecordId: str
        :param _ReplyMethod: 表示消息的回复方式，枚举 ReplyMethod：0=未指定, 1=大模型直接回复, 2=保守回复, 3=拒答, 4=敏感回复, 5=问答对优先回复, 6=欢迎语, 7=并发超限, 8=全局干预知识, 9=任务流程过程回复, 10=任务流程答案, 11=搜索引擎, 12=知识润色, 13=图片理解, 14=实时文档, 15=澄清确认, 16=工作流回复, 17=工作流结束, 18=智能体回复, 19=多意图, 20=中断, 21=智能体计划预览, 22=智能体计划结果, 23=智能体结构化输出。
        :type ReplyMethod: int
        :param _Result: 返回结果
        :type Result: :class:`tencentcloud.adp.v20260520.models.MsgRecordResult`
        :param _Score: 分数
        :type Score: int
        :param _SessionId: 会话ID
        :type SessionId: str
        :param _Source: 来源
        :type Source: :class:`tencentcloud.adp.v20260520.models.MsgRecordSource`
        :param _TraceId: trace_id
        :type TraceId: str
        """
        self._Answer = None
        self._AppId = None
        self._CategoryId = None
        self._CreateTime = None
        self._Intent = None
        self._IntentCategory = None
        self._IsSmart = None
        self._Question = None
        self._RecordId = None
        self._ReplyMethod = None
        self._Result = None
        self._Score = None
        self._SessionId = None
        self._Source = None
        self._TraceId = None

    @property
    def Answer(self):
        r"""答案
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CategoryId(self):
        r"""分类ID
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

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
    def Intent(self):
        r"""意图
        :rtype: str
        """
        return self._Intent

    @Intent.setter
    def Intent(self, Intent):
        self._Intent = Intent

    @property
    def IntentCategory(self):
        r"""意图分类
        :rtype: str
        """
        return self._IntentCategory

    @IntentCategory.setter
    def IntentCategory(self, IntentCategory):
        self._IntentCategory = IntentCategory

    @property
    def IsSmart(self):
        r"""是否是智能分类
        :rtype: bool
        """
        return self._IsSmart

    @IsSmart.setter
    def IsSmart(self, IsSmart):
        self._IsSmart = IsSmart

    @property
    def Question(self):
        r"""问题
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def RecordId(self):
        r"""记录ID
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ReplyMethod(self):
        r"""表示消息的回复方式，枚举 ReplyMethod：0=未指定, 1=大模型直接回复, 2=保守回复, 3=拒答, 4=敏感回复, 5=问答对优先回复, 6=欢迎语, 7=并发超限, 8=全局干预知识, 9=任务流程过程回复, 10=任务流程答案, 11=搜索引擎, 12=知识润色, 13=图片理解, 14=实时文档, 15=澄清确认, 16=工作流回复, 17=工作流结束, 18=智能体回复, 19=多意图, 20=中断, 21=智能体计划预览, 22=智能体计划结果, 23=智能体结构化输出。
        :rtype: int
        """
        return self._ReplyMethod

    @ReplyMethod.setter
    def ReplyMethod(self, ReplyMethod):
        self._ReplyMethod = ReplyMethod

    @property
    def Result(self):
        r"""返回结果
        :rtype: :class:`tencentcloud.adp.v20260520.models.MsgRecordResult`
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Score(self):
        r"""分数
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def SessionId(self):
        r"""会话ID
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Source(self):
        r"""来源
        :rtype: :class:`tencentcloud.adp.v20260520.models.MsgRecordSource`
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def TraceId(self):
        r"""trace_id
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId


    def _deserialize(self, params):
        self._Answer = params.get("Answer")
        self._AppId = params.get("AppId")
        self._CategoryId = params.get("CategoryId")
        self._CreateTime = params.get("CreateTime")
        self._Intent = params.get("Intent")
        self._IntentCategory = params.get("IntentCategory")
        self._IsSmart = params.get("IsSmart")
        self._Question = params.get("Question")
        self._RecordId = params.get("RecordId")
        self._ReplyMethod = params.get("ReplyMethod")
        if params.get("Result") is not None:
            self._Result = MsgRecordResult()
            self._Result._deserialize(params.get("Result"))
        self._Score = params.get("Score")
        self._SessionId = params.get("SessionId")
        if params.get("Source") is not None:
            self._Source = MsgRecordSource()
            self._Source._deserialize(params.get("Source"))
        self._TraceId = params.get("TraceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecordCategory(AbstractModel):
    r"""MsgRecordCategory

    """

    def __init__(self):
        r"""
        :param _CategoryId: <p>分类的业务 ID</p>
        :type CategoryId: str
        :param _Children: <p>子分类列表，树形嵌套</p>
        :type Children: list of MsgRecordCategory
        :param _Name: <p>分类名称</p>
        :type Name: str
        :param _Permission: <p>当前用户对该分类的操作权限</p>
        :type Permission: :class:`tencentcloud.adp.v20260520.models.CategoryPermission`
        :param _TotalCount: <p>该分类下消息记录的数量</p>
        :type TotalCount: str
        """
        self._CategoryId = None
        self._Children = None
        self._Name = None
        self._Permission = None
        self._TotalCount = None

    @property
    def CategoryId(self):
        r"""<p>分类的业务 ID</p>
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def Children(self):
        r"""<p>子分类列表，树形嵌套</p>
        :rtype: list of MsgRecordCategory
        """
        return self._Children

    @Children.setter
    def Children(self, Children):
        self._Children = Children

    @property
    def Name(self):
        r"""<p>分类名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Permission(self):
        r"""<p>当前用户对该分类的操作权限</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.CategoryPermission`
        """
        return self._Permission

    @Permission.setter
    def Permission(self, Permission):
        self._Permission = Permission

    @property
    def TotalCount(self):
        r"""<p>该分类下消息记录的数量</p>
        :rtype: str
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        if params.get("Children") is not None:
            self._Children = []
            for item in params.get("Children"):
                obj = MsgRecordCategory()
                obj._deserialize(item)
                self._Children.append(obj)
        self._Name = params.get("Name")
        if params.get("Permission") is not None:
            self._Permission = CategoryPermission()
            self._Permission._deserialize(params.get("Permission"))
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecordResult(AbstractModel):
    r"""MsgRecordResult

    """

    def __init__(self):
        r"""
        :param _CallResult: 表示该条消息的调用结果：0=CALL_RESULT_UNKNOWN（全部/未知）, 1=CALL_RESULT_SUCCESS（成功）, 2=CALL_RESULT_FAILED（失败）；fail_reason（string）为调用失败时的失败原因描述。
        :type CallResult: int
        :param _CustomerVariable: 自定义变量，json字符串
        :type CustomerVariable: str
        :param _FailReason: 失败原因
        :type FailReason: str
        :param _FirstTokenLatency: 首token耗时
        :type FirstTokenLatency: int
        :param _InputToken: 输入token数
        :type InputToken: int
        :param _OutputToken: 输出token数
        :type OutputToken: int
        :param _TotalToken: 总token数
        :type TotalToken: int
        :param _TotalTokenLatency: 总token耗时
        :type TotalTokenLatency: int
        """
        self._CallResult = None
        self._CustomerVariable = None
        self._FailReason = None
        self._FirstTokenLatency = None
        self._InputToken = None
        self._OutputToken = None
        self._TotalToken = None
        self._TotalTokenLatency = None

    @property
    def CallResult(self):
        r"""表示该条消息的调用结果：0=CALL_RESULT_UNKNOWN（全部/未知）, 1=CALL_RESULT_SUCCESS（成功）, 2=CALL_RESULT_FAILED（失败）；fail_reason（string）为调用失败时的失败原因描述。
        :rtype: int
        """
        return self._CallResult

    @CallResult.setter
    def CallResult(self, CallResult):
        self._CallResult = CallResult

    @property
    def CustomerVariable(self):
        r"""自定义变量，json字符串
        :rtype: str
        """
        return self._CustomerVariable

    @CustomerVariable.setter
    def CustomerVariable(self, CustomerVariable):
        self._CustomerVariable = CustomerVariable

    @property
    def FailReason(self):
        r"""失败原因
        :rtype: str
        """
        return self._FailReason

    @FailReason.setter
    def FailReason(self, FailReason):
        self._FailReason = FailReason

    @property
    def FirstTokenLatency(self):
        r"""首token耗时
        :rtype: int
        """
        return self._FirstTokenLatency

    @FirstTokenLatency.setter
    def FirstTokenLatency(self, FirstTokenLatency):
        self._FirstTokenLatency = FirstTokenLatency

    @property
    def InputToken(self):
        r"""输入token数
        :rtype: int
        """
        return self._InputToken

    @InputToken.setter
    def InputToken(self, InputToken):
        self._InputToken = InputToken

    @property
    def OutputToken(self):
        r"""输出token数
        :rtype: int
        """
        return self._OutputToken

    @OutputToken.setter
    def OutputToken(self, OutputToken):
        self._OutputToken = OutputToken

    @property
    def TotalToken(self):
        r"""总token数
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        self._TotalToken = TotalToken

    @property
    def TotalTokenLatency(self):
        r"""总token耗时
        :rtype: int
        """
        return self._TotalTokenLatency

    @TotalTokenLatency.setter
    def TotalTokenLatency(self, TotalTokenLatency):
        self._TotalTokenLatency = TotalTokenLatency


    def _deserialize(self, params):
        self._CallResult = params.get("CallResult")
        self._CustomerVariable = params.get("CustomerVariable")
        self._FailReason = params.get("FailReason")
        self._FirstTokenLatency = params.get("FirstTokenLatency")
        self._InputToken = params.get("InputToken")
        self._OutputToken = params.get("OutputToken")
        self._TotalToken = params.get("TotalToken")
        self._TotalTokenLatency = params.get("TotalTokenLatency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MsgRecordSource(AbstractModel):
    r"""MsgRecordSource

    """

    def __init__(self):
        r"""
        :param _ChannelType: 对话消息的接入渠道类型：0=未指定, 1=坐席, 2=体验页面(腾讯云), 3=评测端对话, 4=体验页面(手机号), 5=对话端API接入, 6=评测任务对话, 10=工作流调试, 10000=微信公众号, 10001=微信服务号, 10002=企微应用, 10003=网页组件, 10004=微信客服, 10005=微信小程序, 10006=元器, 10007=应用宝, 10008=元宝, 10009=企微智能机器人, 10010=元器API, 10011=LINE, 10012=Telegram, 10100=电脑管家, 20001=荣耀智能体平台, 20002=小米应用商店；user_id（string）为该渠道下的访客唯一标识。
        :type ChannelType: int
        :param _FromId: 用户ID
        :type FromId: str
        :param _FromType: 消息发送者的用户来源类型：1=用户（访客/C端用户）, 2=机器人（AI回复）, 3=坐席（人工客服）；from_id（string）为该来源类型下的用户唯一标识 ID。
        :type FromType: int
        :param _UserAvatar: 用户头像
        :type UserAvatar: str
        :param _UserId: 访客ID
        :type UserId: str
        :param _UserNickname: 访客名称
        :type UserNickname: str
        """
        self._ChannelType = None
        self._FromId = None
        self._FromType = None
        self._UserAvatar = None
        self._UserId = None
        self._UserNickname = None

    @property
    def ChannelType(self):
        r"""对话消息的接入渠道类型：0=未指定, 1=坐席, 2=体验页面(腾讯云), 3=评测端对话, 4=体验页面(手机号), 5=对话端API接入, 6=评测任务对话, 10=工作流调试, 10000=微信公众号, 10001=微信服务号, 10002=企微应用, 10003=网页组件, 10004=微信客服, 10005=微信小程序, 10006=元器, 10007=应用宝, 10008=元宝, 10009=企微智能机器人, 10010=元器API, 10011=LINE, 10012=Telegram, 10100=电脑管家, 20001=荣耀智能体平台, 20002=小米应用商店；user_id（string）为该渠道下的访客唯一标识。
        :rtype: int
        """
        return self._ChannelType

    @ChannelType.setter
    def ChannelType(self, ChannelType):
        self._ChannelType = ChannelType

    @property
    def FromId(self):
        r"""用户ID
        :rtype: str
        """
        return self._FromId

    @FromId.setter
    def FromId(self, FromId):
        self._FromId = FromId

    @property
    def FromType(self):
        r"""消息发送者的用户来源类型：1=用户（访客/C端用户）, 2=机器人（AI回复）, 3=坐席（人工客服）；from_id（string）为该来源类型下的用户唯一标识 ID。
        :rtype: int
        """
        return self._FromType

    @FromType.setter
    def FromType(self, FromType):
        self._FromType = FromType

    @property
    def UserAvatar(self):
        r"""用户头像
        :rtype: str
        """
        return self._UserAvatar

    @UserAvatar.setter
    def UserAvatar(self, UserAvatar):
        self._UserAvatar = UserAvatar

    @property
    def UserId(self):
        r"""访客ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def UserNickname(self):
        r"""访客名称
        :rtype: str
        """
        return self._UserNickname

    @UserNickname.setter
    def UserNickname(self, UserNickname):
        self._UserNickname = UserNickname


    def _deserialize(self, params):
        self._ChannelType = params.get("ChannelType")
        self._FromId = params.get("FromId")
        self._FromType = params.get("FromType")
        self._UserAvatar = params.get("UserAvatar")
        self._UserId = params.get("UserId")
        self._UserNickname = params.get("UserNickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiAgentConfig(AbstractModel):
    r"""多智能体配置

    """

    def __init__(self):
        r"""
        :param _AgentCollaboration: Agent协同配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AgentCollaboration: :class:`tencentcloud.adp.v20260520.models.AgentCollaborationConfig`
        """
        self._AgentCollaboration = None

    @property
    def AgentCollaboration(self):
        r"""Agent协同配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentCollaborationConfig`
        """
        return self._AgentCollaboration

    @AgentCollaboration.setter
    def AgentCollaboration(self, AgentCollaboration):
        self._AgentCollaboration = AgentCollaboration


    def _deserialize(self, params):
        if params.get("AgentCollaboration") is not None:
            self._AgentCollaboration = AgentCollaborationConfig()
            self._AgentCollaboration._deserialize(params.get("AgentCollaboration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiModalQAModel(AbstractModel):
    r"""多模态问答模型配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MultiModalUnderstandingModel(AbstractModel):
    r"""多模态理解模型配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OAuthConfig(AbstractModel):
    r"""OAuth2.0授权信息

    """

    def __init__(self):
        r"""
        :param _AuthorizationUrl: OAuth服务方授权页url地址
        :type AuthorizationUrl: str
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _ClientSecret: 客户端密钥
        :type ClientSecret: str
        :param _ScopeList: 请求授权的数据范围
        :type ScopeList: list of str
        :param _TokenUrl: 获取access token的url地址
        :type TokenUrl: str
        """
        self._AuthorizationUrl = None
        self._ClientId = None
        self._ClientSecret = None
        self._ScopeList = None
        self._TokenUrl = None

    @property
    def AuthorizationUrl(self):
        r"""OAuth服务方授权页url地址
        :rtype: str
        """
        return self._AuthorizationUrl

    @AuthorizationUrl.setter
    def AuthorizationUrl(self, AuthorizationUrl):
        self._AuthorizationUrl = AuthorizationUrl

    @property
    def ClientId(self):
        r"""客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientSecret(self):
        r"""客户端密钥
        :rtype: str
        """
        return self._ClientSecret

    @ClientSecret.setter
    def ClientSecret(self, ClientSecret):
        self._ClientSecret = ClientSecret

    @property
    def ScopeList(self):
        r"""请求授权的数据范围
        :rtype: list of str
        """
        return self._ScopeList

    @ScopeList.setter
    def ScopeList(self, ScopeList):
        self._ScopeList = ScopeList

    @property
    def TokenUrl(self):
        r"""获取access token的url地址
        :rtype: str
        """
        return self._TokenUrl

    @TokenUrl.setter
    def TokenUrl(self, TokenUrl):
        self._TokenUrl = TokenUrl


    def _deserialize(self, params):
        self._AuthorizationUrl = params.get("AuthorizationUrl")
        self._ClientId = params.get("ClientId")
        self._ClientSecret = params.get("ClientSecret")
        self._ScopeList = params.get("ScopeList")
        self._TokenUrl = params.get("TokenUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OnceSchedule(AbstractModel):
    r"""OnceSchedule

    """

    def __init__(self):
        r"""
        :param _FireTime: 触发时间
        :type FireTime: str
        """
        self._FireTime = None

    @property
    def FireTime(self):
        r"""触发时间
        :rtype: str
        """
        return self._FireTime

    @FireTime.setter
    def FireTime(self, FireTime):
        self._FireTime = FireTime


    def _deserialize(self, params):
        self._FireTime = params.get("FireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseAppTriggerRequest(AbstractModel):
    r"""PauseAppTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerId: <p>应用触发器ID</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._Scope = None
        self._TriggerId = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerId(self):
        r"""<p>应用触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Scope = params.get("Scope")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseAppTriggerResponse(AbstractModel):
    r"""PauseAppTrigger返回参数结构体

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


class PlatformUsageSummary(AbstractModel):
    r"""平台资源用量聚合明细（PLATFORM 域专属）

    """

    def __init__(self):
        r"""
        :param _ResourceConsumptionList: <p>PLATFORM 域消耗计量列表（权威字段）：按单位+label 分项列出每类计量，label 取 PlatformBizType 枚举名称字符串；典型如 unit=TIMES + label=PLATFORM_BIZ_TYPE_SECURITY_AUDIT/WEB_SEARCH/OPEN_CLAW/APP_INVOKE，unit=ITEM + label=PLATFORM_BIZ_TYPE_LONG_TERM_MEMORY</p>
        :type ResourceConsumptionList: list of ResourceConsumption
        """
        self._ResourceConsumptionList = None

    @property
    def ResourceConsumptionList(self):
        r"""<p>PLATFORM 域消耗计量列表（权威字段）：按单位+label 分项列出每类计量，label 取 PlatformBizType 枚举名称字符串；典型如 unit=TIMES + label=PLATFORM_BIZ_TYPE_SECURITY_AUDIT/WEB_SEARCH/OPEN_CLAW/APP_INVOKE，unit=ITEM + label=PLATFORM_BIZ_TYPE_LONG_TERM_MEMORY</p>
        :rtype: list of ResourceConsumption
        """
        return self._ResourceConsumptionList

    @ResourceConsumptionList.setter
    def ResourceConsumptionList(self, ResourceConsumptionList):
        self._ResourceConsumptionList = ResourceConsumptionList


    def _deserialize(self, params):
        if params.get("ResourceConsumptionList") is not None:
            self._ResourceConsumptionList = []
            for item in params.get("ResourceConsumptionList"):
                obj = ResourceConsumption()
                obj._deserialize(item)
                self._ResourceConsumptionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Plugin(AbstractModel):
    r"""插件详情

    """

    def __init__(self):
        r"""
        :param _Config: 插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        :param _CreateTime: 创建时间，unix时间戳
        :type CreateTime: str
        :param _Operation: 插件运营管理信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: :class:`tencentcloud.adp.v20260520.models.PluginOperation`
        :param _PluginId: 插件id
        :type PluginId: str
        :param _PluginVersion: 插件版本号
        :type PluginVersion: int
        :param _Profile: 插件基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Profile: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        :param _Statistics: 插件统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Statistics: :class:`tencentcloud.adp.v20260520.models.PluginStatistics`
        :param _Status: <p>插件状态，1:可用，2:不可用 </p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li></ul>
        :type Status: int
        :param _ToolList: 工具列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolList: list of Tool
        :param _UpdateTime: 更新时间，Unix时间戳
        :type UpdateTime: str
        :param _UserState: 用户维度的插件状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserState: :class:`tencentcloud.adp.v20260520.models.PluginUserState`
        """
        self._Config = None
        self._CreateTime = None
        self._Operation = None
        self._PluginId = None
        self._PluginVersion = None
        self._Profile = None
        self._Statistics = None
        self._Status = None
        self._ToolList = None
        self._UpdateTime = None
        self._UserState = None

    @property
    def Config(self):
        r"""插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def CreateTime(self):
        r"""创建时间，unix时间戳
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Operation(self):
        r"""插件运营管理信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginOperation`
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PluginId(self):
        r"""插件id
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginVersion(self):
        r"""插件版本号
        :rtype: int
        """
        return self._PluginVersion

    @PluginVersion.setter
    def PluginVersion(self, PluginVersion):
        self._PluginVersion = PluginVersion

    @property
    def Profile(self):
        r"""插件基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Statistics(self):
        r"""插件统计信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginStatistics`
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Status(self):
        r"""<p>插件状态，1:可用，2:不可用 </p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ToolList(self):
        r"""工具列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tool
        """
        return self._ToolList

    @ToolList.setter
    def ToolList(self, ToolList):
        self._ToolList = ToolList

    @property
    def UpdateTime(self):
        r"""更新时间，Unix时间戳
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def UserState(self):
        r"""用户维度的插件状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginUserState`
        """
        return self._UserState

    @UserState.setter
    def UserState(self, UserState):
        self._UserState = UserState


    def _deserialize(self, params):
        if params.get("Config") is not None:
            self._Config = PluginConfig()
            self._Config._deserialize(params.get("Config"))
        self._CreateTime = params.get("CreateTime")
        if params.get("Operation") is not None:
            self._Operation = PluginOperation()
            self._Operation._deserialize(params.get("Operation"))
        self._PluginId = params.get("PluginId")
        self._PluginVersion = params.get("PluginVersion")
        if params.get("Profile") is not None:
            self._Profile = PluginProfile()
            self._Profile._deserialize(params.get("Profile"))
        if params.get("Statistics") is not None:
            self._Statistics = PluginStatistics()
            self._Statistics._deserialize(params.get("Statistics"))
        self._Status = params.get("Status")
        if params.get("ToolList") is not None:
            self._ToolList = []
            for item in params.get("ToolList"):
                obj = Tool()
                obj._deserialize(item)
                self._ToolList.append(obj)
        self._UpdateTime = params.get("UpdateTime")
        if params.get("UserState") is not None:
            self._UserState = PluginUserState()
            self._UserState._deserialize(params.get("UserState"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginConfig(AbstractModel):
    r"""插件配置

    """

    def __init__(self):
        r"""
        :param _ApiPluginConfig: API插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiPluginConfig: :class:`tencentcloud.adp.v20260520.models.ApiPluginConfig`
        :param _AppPluginConfig: 应用插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AppPluginConfig: :class:`tencentcloud.adp.v20260520.models.AppPluginConfig`
        :param _MCPPluginConfig: mcp插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :type MCPPluginConfig: :class:`tencentcloud.adp.v20260520.models.MCPPluginConfig`
        """
        self._ApiPluginConfig = None
        self._AppPluginConfig = None
        self._MCPPluginConfig = None

    @property
    def ApiPluginConfig(self):
        r"""API插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ApiPluginConfig`
        """
        return self._ApiPluginConfig

    @ApiPluginConfig.setter
    def ApiPluginConfig(self, ApiPluginConfig):
        self._ApiPluginConfig = ApiPluginConfig

    @property
    def AppPluginConfig(self):
        r"""应用插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppPluginConfig`
        """
        return self._AppPluginConfig

    @AppPluginConfig.setter
    def AppPluginConfig(self, AppPluginConfig):
        self._AppPluginConfig = AppPluginConfig

    @property
    def MCPPluginConfig(self):
        r"""mcp插件配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.MCPPluginConfig`
        """
        return self._MCPPluginConfig

    @MCPPluginConfig.setter
    def MCPPluginConfig(self, MCPPluginConfig):
        self._MCPPluginConfig = MCPPluginConfig


    def _deserialize(self, params):
        if params.get("ApiPluginConfig") is not None:
            self._ApiPluginConfig = ApiPluginConfig()
            self._ApiPluginConfig._deserialize(params.get("ApiPluginConfig"))
        if params.get("AppPluginConfig") is not None:
            self._AppPluginConfig = AppPluginConfig()
            self._AppPluginConfig._deserialize(params.get("AppPluginConfig"))
        if params.get("MCPPluginConfig") is not None:
            self._MCPPluginConfig = MCPPluginConfig()
            self._MCPPluginConfig._deserialize(params.get("MCPPluginConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginOperation(AbstractModel):
    r"""PluginOperation

    """

    def __init__(self):
        r"""
        :param _AllowExternalAccess: 是否允许外部调用
        :type AllowExternalAccess: bool
        :param _BillingType: <p>计费类型。</p><p>枚举值：</p><ul><li>0：免费</li><li>1：公测</li><li>2：官方收费</li></ul>
        :type BillingType: int
        :param _CategoryKey: 插件分类标识
        :type CategoryKey: str
        :param _Introduction: 插件概述
        :type Introduction: str
        :param _IsRecommended: 是否精选
        :type IsRecommended: bool
        """
        self._AllowExternalAccess = None
        self._BillingType = None
        self._CategoryKey = None
        self._Introduction = None
        self._IsRecommended = None

    @property
    def AllowExternalAccess(self):
        r"""是否允许外部调用
        :rtype: bool
        """
        return self._AllowExternalAccess

    @AllowExternalAccess.setter
    def AllowExternalAccess(self, AllowExternalAccess):
        self._AllowExternalAccess = AllowExternalAccess

    @property
    def BillingType(self):
        r"""<p>计费类型。</p><p>枚举值：</p><ul><li>0：免费</li><li>1：公测</li><li>2：官方收费</li></ul>
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def CategoryKey(self):
        r"""插件分类标识
        :rtype: str
        """
        return self._CategoryKey

    @CategoryKey.setter
    def CategoryKey(self, CategoryKey):
        self._CategoryKey = CategoryKey

    @property
    def Introduction(self):
        r"""插件概述
        :rtype: str
        """
        return self._Introduction

    @Introduction.setter
    def Introduction(self, Introduction):
        self._Introduction = Introduction

    @property
    def IsRecommended(self):
        r"""是否精选
        :rtype: bool
        """
        return self._IsRecommended

    @IsRecommended.setter
    def IsRecommended(self, IsRecommended):
        self._IsRecommended = IsRecommended


    def _deserialize(self, params):
        self._AllowExternalAccess = params.get("AllowExternalAccess")
        self._BillingType = params.get("BillingType")
        self._CategoryKey = params.get("CategoryKey")
        self._Introduction = params.get("Introduction")
        self._IsRecommended = params.get("IsRecommended")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginParam(AbstractModel):
    r"""MCP插件参数信息

    """

    def __init__(self):
        r"""
        :param _IsGlobalHidden: 参数配置是否隐藏不可见
        :type IsGlobalHidden: bool
        :param _IsRequired: 参数是否必填
        :type IsRequired: bool
        :param _Name: 参数名称
        :type Name: str
        :param _Value: 参数值
        :type Value: str
        """
        self._IsGlobalHidden = None
        self._IsRequired = None
        self._Name = None
        self._Value = None

    @property
    def IsGlobalHidden(self):
        r"""参数配置是否隐藏不可见
        :rtype: bool
        """
        return self._IsGlobalHidden

    @IsGlobalHidden.setter
    def IsGlobalHidden(self, IsGlobalHidden):
        self._IsGlobalHidden = IsGlobalHidden

    @property
    def IsRequired(self):
        r"""参数是否必填
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def Name(self):
        r"""参数名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

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
        self._IsGlobalHidden = params.get("IsGlobalHidden")
        self._IsRequired = params.get("IsRequired")
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginProfile(AbstractModel):
    r"""PluginProfile

    """

    def __init__(self):
        r"""
        :param _Author: 插件作者
        :type Author: str
        :param _Description: 插件描述
        :type Description: str
        :param _IconUrl: 插件图标url
        :type IconUrl: str
        :param _Name: 插件名称
        :type Name: str
        :param _PluginClass: <p>插件产品分类</p><p>枚举值：</p><ul><li>0：普通插件</li><li>1：连接器类插件</li></ul>
        :type PluginClass: int
        :param _PluginKind: <p>插件类型</p><p>枚举值：</p><ul><li>0：API接口</li><li>1：代码</li><li>2：MCP</li><li>3：应用</li></ul>
        :type PluginKind: int
        :param _PluginSource: <p>插件来源</p><p>枚举值：</p><ul><li>0：自定义插件</li><li>1：官方插件</li><li>2：第三方插件</li></ul>
        :type PluginSource: int
        """
        self._Author = None
        self._Description = None
        self._IconUrl = None
        self._Name = None
        self._PluginClass = None
        self._PluginKind = None
        self._PluginSource = None

    @property
    def Author(self):
        r"""插件作者
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def Description(self):
        r"""插件描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IconUrl(self):
        r"""插件图标url
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Name(self):
        r"""插件名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PluginClass(self):
        r"""<p>插件产品分类</p><p>枚举值：</p><ul><li>0：普通插件</li><li>1：连接器类插件</li></ul>
        :rtype: int
        """
        return self._PluginClass

    @PluginClass.setter
    def PluginClass(self, PluginClass):
        self._PluginClass = PluginClass

    @property
    def PluginKind(self):
        r"""<p>插件类型</p><p>枚举值：</p><ul><li>0：API接口</li><li>1：代码</li><li>2：MCP</li><li>3：应用</li></ul>
        :rtype: int
        """
        return self._PluginKind

    @PluginKind.setter
    def PluginKind(self, PluginKind):
        self._PluginKind = PluginKind

    @property
    def PluginSource(self):
        r"""<p>插件来源</p><p>枚举值：</p><ul><li>0：自定义插件</li><li>1：官方插件</li><li>2：第三方插件</li></ul>
        :rtype: int
        """
        return self._PluginSource

    @PluginSource.setter
    def PluginSource(self, PluginSource):
        self._PluginSource = PluginSource


    def _deserialize(self, params):
        self._Author = params.get("Author")
        self._Description = params.get("Description")
        self._IconUrl = params.get("IconUrl")
        self._Name = params.get("Name")
        self._PluginClass = params.get("PluginClass")
        self._PluginKind = params.get("PluginKind")
        self._PluginSource = params.get("PluginSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginStatistics(AbstractModel):
    r"""PluginStatistics

    """

    def __init__(self):
        r"""
        :param _CallCount: 插件调用量
        :type CallCount: int
        :param _ToolCount: 工具数量
        :type ToolCount: int
        """
        self._CallCount = None
        self._ToolCount = None

    @property
    def CallCount(self):
        r"""插件调用量
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def ToolCount(self):
        r"""工具数量
        :rtype: int
        """
        return self._ToolCount

    @ToolCount.setter
    def ToolCount(self, ToolCount):
        self._ToolCount = ToolCount


    def _deserialize(self, params):
        self._CallCount = params.get("CallCount")
        self._ToolCount = params.get("ToolCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginSummary(AbstractModel):
    r"""插件概要信息（用于插件列表）

    """

    def __init__(self):
        r"""
        :param _Operation: <p>插件运营管理信息</p>
        :type Operation: :class:`tencentcloud.adp.v20260520.models.PluginOperation`
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _Profile: <p>插件基础信息</p>
        :type Profile: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        :param _Statistics: <p>插件统计信息</p>
        :type Statistics: :class:`tencentcloud.adp.v20260520.models.PluginStatistics`
        :param _Status: <p>插件状态，1:可用，2:不可用 </p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li></ul>
        :type Status: int
        :param _UserState: <p>用户维度的插件状态信息</p>
        :type UserState: :class:`tencentcloud.adp.v20260520.models.PluginUserState`
        :param _Config: <p>插件配置信息</p>
        :type Config: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        :param _ToolList: <p>工具信息</p>
        :type ToolList: list of ToolSummary
        """
        self._Operation = None
        self._PluginId = None
        self._Profile = None
        self._Statistics = None
        self._Status = None
        self._UserState = None
        self._Config = None
        self._ToolList = None

    @property
    def Operation(self):
        r"""<p>插件运营管理信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginOperation`
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Profile(self):
        r"""<p>插件基础信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Statistics(self):
        r"""<p>插件统计信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginStatistics`
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Status(self):
        r"""<p>插件状态，1:可用，2:不可用 </p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li></ul>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def UserState(self):
        r"""<p>用户维度的插件状态信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginUserState`
        """
        return self._UserState

    @UserState.setter
    def UserState(self, UserState):
        self._UserState = UserState

    @property
    def Config(self):
        r"""<p>插件配置信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def ToolList(self):
        r"""<p>工具信息</p>
        :rtype: list of ToolSummary
        """
        return self._ToolList

    @ToolList.setter
    def ToolList(self, ToolList):
        self._ToolList = ToolList


    def _deserialize(self, params):
        if params.get("Operation") is not None:
            self._Operation = PluginOperation()
            self._Operation._deserialize(params.get("Operation"))
        self._PluginId = params.get("PluginId")
        if params.get("Profile") is not None:
            self._Profile = PluginProfile()
            self._Profile._deserialize(params.get("Profile"))
        if params.get("Statistics") is not None:
            self._Statistics = PluginStatistics()
            self._Statistics._deserialize(params.get("Statistics"))
        self._Status = params.get("Status")
        if params.get("UserState") is not None:
            self._UserState = PluginUserState()
            self._UserState._deserialize(params.get("UserState"))
        if params.get("Config") is not None:
            self._Config = PluginConfig()
            self._Config._deserialize(params.get("Config"))
        if params.get("ToolList") is not None:
            self._ToolList = []
            for item in params.get("ToolList"):
                obj = ToolSummary()
                obj._deserialize(item)
                self._ToolList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginUsageDetail(AbstractModel):
    r"""插件调用明细

    """

    def __init__(self):
        r"""
        :param _PluginName: <p>插件名称</p>
        :type PluginName: str
        :param _ResourceConsumptionList: <p>PLUGIN 域单次调用的消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*），label 为空表示 total_tokens</p>
        :type ResourceConsumptionList: list of ResourceConsumption
        :param _ToolName: <p>插件工具名（tool_name）</p>
        :type ToolName: str
        """
        self._PluginName = None
        self._ResourceConsumptionList = None
        self._ToolName = None

    @property
    def PluginName(self):
        r"""<p>插件名称</p>
        :rtype: str
        """
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def ResourceConsumptionList(self):
        r"""<p>PLUGIN 域单次调用的消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*），label 为空表示 total_tokens</p>
        :rtype: list of ResourceConsumption
        """
        return self._ResourceConsumptionList

    @ResourceConsumptionList.setter
    def ResourceConsumptionList(self, ResourceConsumptionList):
        self._ResourceConsumptionList = ResourceConsumptionList

    @property
    def ToolName(self):
        r"""<p>插件工具名（tool_name）</p>
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName


    def _deserialize(self, params):
        self._PluginName = params.get("PluginName")
        if params.get("ResourceConsumptionList") is not None:
            self._ResourceConsumptionList = []
            for item in params.get("ResourceConsumptionList"):
                obj = ResourceConsumption()
                obj._deserialize(item)
                self._ResourceConsumptionList.append(obj)
        self._ToolName = params.get("ToolName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginUsageSummary(AbstractModel):
    r"""插件资源用量聚合明细（PLUGIN 域专属）

    """

    def __init__(self):
        r"""
        :param _CallCount: <p>调用次数（业务调用维度的顶层计数）</p>
        :type CallCount: float
        :param _ResourceConsumptionList: <p>PLUGIN 域消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*），label 为空表示 total_tokens</p>
        :type ResourceConsumptionList: list of ResourceConsumption
        """
        self._CallCount = None
        self._ResourceConsumptionList = None

    @property
    def CallCount(self):
        r"""<p>调用次数（业务调用维度的顶层计数）</p>
        :rtype: float
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def ResourceConsumptionList(self):
        r"""<p>PLUGIN 域消耗计量列表（权威字段）：按单位+label 分项列出每类计量。unit=TOKEN 时 label 区分 Token 子类别（input/output/avg_*），label 为空表示 total_tokens</p>
        :rtype: list of ResourceConsumption
        """
        return self._ResourceConsumptionList

    @ResourceConsumptionList.setter
    def ResourceConsumptionList(self, ResourceConsumptionList):
        self._ResourceConsumptionList = ResourceConsumptionList


    def _deserialize(self, params):
        self._CallCount = params.get("CallCount")
        if params.get("ResourceConsumptionList") is not None:
            self._ResourceConsumptionList = []
            for item in params.get("ResourceConsumptionList"):
                obj = ResourceConsumption()
                obj._deserialize(item)
                self._ResourceConsumptionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginUserState(AbstractModel):
    r"""PluginUserState

    """

    def __init__(self):
        r"""
        :param _IsFavorite: 是否已收藏该插件
        :type IsFavorite: bool
        :param _IsInWhiteList: 是否在插件白名单内
        :type IsInWhiteList: bool
        :param _WhiteListType: <p>白名单类型，用于表示当前用户是否可直接使用该插件。</p><p>枚举值：</p><ul><li>0：非白名单插件，全量开放</li><li>1：当前用户在白名单内</li><li>2：当前用户不在白名单内，需提交申请</li></ul>
        :type WhiteListType: int
        """
        self._IsFavorite = None
        self._IsInWhiteList = None
        self._WhiteListType = None

    @property
    def IsFavorite(self):
        r"""是否已收藏该插件
        :rtype: bool
        """
        return self._IsFavorite

    @IsFavorite.setter
    def IsFavorite(self, IsFavorite):
        self._IsFavorite = IsFavorite

    @property
    def IsInWhiteList(self):
        r"""是否在插件白名单内
        :rtype: bool
        """
        return self._IsInWhiteList

    @IsInWhiteList.setter
    def IsInWhiteList(self, IsInWhiteList):
        self._IsInWhiteList = IsInWhiteList

    @property
    def WhiteListType(self):
        r"""<p>白名单类型，用于表示当前用户是否可直接使用该插件。</p><p>枚举值：</p><ul><li>0：非白名单插件，全量开放</li><li>1：当前用户在白名单内</li><li>2：当前用户不在白名单内，需提交申请</li></ul>
        :rtype: int
        """
        return self._WhiteListType

    @WhiteListType.setter
    def WhiteListType(self, WhiteListType):
        self._WhiteListType = WhiteListType


    def _deserialize(self, params):
        self._IsFavorite = params.get("IsFavorite")
        self._IsInWhiteList = params.get("IsInWhiteList")
        self._WhiteListType = params.get("WhiteListType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PromptRewriteModel(AbstractModel):
    r"""Prompt改写配置

    """

    def __init__(self):
        r"""
        :param _Model: 模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""模型配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseRecord(AbstractModel):
    r"""[数据结构定义] 发布记录

    """

    def __init__(self):
        r"""
        :param _CanExport: 是否可导出
        :type CanExport: bool
        :param _CanRollback: 是否可回滚
        :type CanRollback: bool
        :param _Description: 发布描述
        :type Description: str
        :param _FailCount: 发布失败数
        :type FailCount: int
        :param _Reason: 失败原因
        :type Reason: str
        :param _ReleaseId: 发布ID
        :type ReleaseId: str
        :param _ReleaseVersion: 发布版本
        :type ReleaseVersion: str
        :param _Status: 发布状态。枚举值: 1:待发布, 2:发布中, 3:发布成功, 4:发布失败, 5:审核中, 6:审核成功, 7:审核失败, 8:发布成功回调处理中, 9:发布暂停, 10:申诉审核中, 11:申诉审核通过, 12:申诉审核不通过
        :type Status: int
        :param _StatusDescription: 状态描述
        :type StatusDescription: str
        :param _SuccessCount: 发布成功数
        :type SuccessCount: int
        :param _UpdateTime: 更新时间 (Unix时间戳,秒级)
        :type UpdateTime: str
        :param _Updater: 发布人
        :type Updater: str
        """
        self._CanExport = None
        self._CanRollback = None
        self._Description = None
        self._FailCount = None
        self._Reason = None
        self._ReleaseId = None
        self._ReleaseVersion = None
        self._Status = None
        self._StatusDescription = None
        self._SuccessCount = None
        self._UpdateTime = None
        self._Updater = None

    @property
    def CanExport(self):
        r"""是否可导出
        :rtype: bool
        """
        return self._CanExport

    @CanExport.setter
    def CanExport(self, CanExport):
        self._CanExport = CanExport

    @property
    def CanRollback(self):
        r"""是否可回滚
        :rtype: bool
        """
        return self._CanRollback

    @CanRollback.setter
    def CanRollback(self, CanRollback):
        self._CanRollback = CanRollback

    @property
    def Description(self):
        r"""发布描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FailCount(self):
        r"""发布失败数
        :rtype: int
        """
        return self._FailCount

    @FailCount.setter
    def FailCount(self, FailCount):
        self._FailCount = FailCount

    @property
    def Reason(self):
        r"""失败原因
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def ReleaseId(self):
        r"""发布ID
        :rtype: str
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId

    @property
    def ReleaseVersion(self):
        r"""发布版本
        :rtype: str
        """
        return self._ReleaseVersion

    @ReleaseVersion.setter
    def ReleaseVersion(self, ReleaseVersion):
        self._ReleaseVersion = ReleaseVersion

    @property
    def Status(self):
        r"""发布状态。枚举值: 1:待发布, 2:发布中, 3:发布成功, 4:发布失败, 5:审核中, 6:审核成功, 7:审核失败, 8:发布成功回调处理中, 9:发布暂停, 10:申诉审核中, 11:申诉审核通过, 12:申诉审核不通过
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDescription(self):
        r"""状态描述
        :rtype: str
        """
        return self._StatusDescription

    @StatusDescription.setter
    def StatusDescription(self, StatusDescription):
        self._StatusDescription = StatusDescription

    @property
    def SuccessCount(self):
        r"""发布成功数
        :rtype: int
        """
        return self._SuccessCount

    @SuccessCount.setter
    def SuccessCount(self, SuccessCount):
        self._SuccessCount = SuccessCount

    @property
    def UpdateTime(self):
        r"""更新时间 (Unix时间戳,秒级)
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Updater(self):
        r"""发布人
        :rtype: str
        """
        return self._Updater

    @Updater.setter
    def Updater(self, Updater):
        self._Updater = Updater


    def _deserialize(self, params):
        self._CanExport = params.get("CanExport")
        self._CanRollback = params.get("CanRollback")
        self._Description = params.get("Description")
        self._FailCount = params.get("FailCount")
        self._Reason = params.get("Reason")
        self._ReleaseId = params.get("ReleaseId")
        self._ReleaseVersion = params.get("ReleaseVersion")
        self._Status = params.get("Status")
        self._StatusDescription = params.get("StatusDescription")
        self._SuccessCount = params.get("SuccessCount")
        self._UpdateTime = params.get("UpdateTime")
        self._Updater = params.get("Updater")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseSkillRequest(AbstractModel):
    r"""ReleaseSkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>SkillId</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        :param _VersionId: <p>版本ID</p>
        :type VersionId: str
        """
        self._SkillId = None
        self._SpaceId = None
        self._VersionId = None

    @property
    def SkillId(self):
        r"""<p>SkillId</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def VersionId(self):
        r"""<p>版本ID</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseSkillResponse(AbstractModel):
    r"""ReleaseSkill返回参数结构体

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


class ReleaseSummary(AbstractModel):
    r"""发布摘要信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: <p>创建时间 (Unix时间戳,秒级)</p>
        :type CreateTime: str
        :param _Description: <p>发布描述</p>
        :type Description: str
        :param _ReleaseId: <p>发布ID</p>
        :type ReleaseId: str
        :param _Status: <p>发布状态。枚举值: 1:待发布, 2:发布中, 3:发布成功, 4:发布失败, 5:审核中, 6:审核成功, 7:审核失败, 8:发布成功回调处理中, 9:发布暂停, 10:申诉审核中, 11:申诉审核通过, 12:申诉审核不通过</p>
        :type Status: int
        :param _StatusDescription: <p>状态描述</p>
        :type StatusDescription: str
        :param _AppShareAccessControl: <p>应用分享访问控制</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppShareAccessControl: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        :param _ChannelIdList: <p>发布渠道ID列表</p>
        :type ChannelIdList: list of str
        :param _CorpShareConfig: <p>企业共享配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CorpShareConfig: :class:`tencentcloud.adp.v20260520.models.CorpShareConfig`
        """
        self._CreateTime = None
        self._Description = None
        self._ReleaseId = None
        self._Status = None
        self._StatusDescription = None
        self._AppShareAccessControl = None
        self._ChannelIdList = None
        self._CorpShareConfig = None

    @property
    def CreateTime(self):
        r"""<p>创建时间 (Unix时间戳,秒级)</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        r"""<p>发布描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ReleaseId(self):
        r"""<p>发布ID</p>
        :rtype: str
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId

    @property
    def Status(self):
        r"""<p>发布状态。枚举值: 1:待发布, 2:发布中, 3:发布成功, 4:发布失败, 5:审核中, 6:审核成功, 7:审核失败, 8:发布成功回调处理中, 9:发布暂停, 10:申诉审核中, 11:申诉审核通过, 12:申诉审核不通过</p>
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusDescription(self):
        r"""<p>状态描述</p>
        :rtype: str
        """
        return self._StatusDescription

    @StatusDescription.setter
    def StatusDescription(self, StatusDescription):
        self._StatusDescription = StatusDescription

    @property
    def AppShareAccessControl(self):
        r"""<p>应用分享访问控制</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        """
        return self._AppShareAccessControl

    @AppShareAccessControl.setter
    def AppShareAccessControl(self, AppShareAccessControl):
        self._AppShareAccessControl = AppShareAccessControl

    @property
    def ChannelIdList(self):
        r"""<p>发布渠道ID列表</p>
        :rtype: list of str
        """
        return self._ChannelIdList

    @ChannelIdList.setter
    def ChannelIdList(self, ChannelIdList):
        self._ChannelIdList = ChannelIdList

    @property
    def CorpShareConfig(self):
        r"""<p>企业共享配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.CorpShareConfig`
        """
        return self._CorpShareConfig

    @CorpShareConfig.setter
    def CorpShareConfig(self, CorpShareConfig):
        self._CorpShareConfig = CorpShareConfig


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._ReleaseId = params.get("ReleaseId")
        self._Status = params.get("Status")
        self._StatusDescription = params.get("StatusDescription")
        if params.get("AppShareAccessControl") is not None:
            self._AppShareAccessControl = AppShareAccessControl()
            self._AppShareAccessControl._deserialize(params.get("AppShareAccessControl"))
        self._ChannelIdList = params.get("ChannelIdList")
        if params.get("CorpShareConfig") is not None:
            self._CorpShareConfig = CorpShareConfig()
            self._CorpShareConfig._deserialize(params.get("CorpShareConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestParam(AbstractModel):
    r"""RequestParam

    """

    def __init__(self):
        r"""
        :param _AnyOf: <p>AnyOf类型的参数</p>
        :type AnyOf: list of RequestParam
        :param _DefaultValue: <p>默认值</p>
        :type DefaultValue: str
        :param _Description: <p>参数描述</p>
        :type Description: str
        :param _IsGlobalHidden: <p>全局隐藏不可见（区别于Agent场景的agent_hidden），true-全局隐藏不可见，false-可见</p>
        :type IsGlobalHidden: bool
        :param _IsRequired: <p>是否必选</p>
        :type IsRequired: bool
        :param _Name: <p>参数名称</p>
        :type Name: str
        :param _OneOf: <p>OneOf类型的参数</p>
        :type OneOf: list of RequestParam
        :param _SubParams: <p>子参数,ParamType 是OBJECT 或 ARRAY&lt;&gt;类型有用</p>
        :type SubParams: list of RequestParam
        :param _Type: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>PARAM_TYPE_STRING</td><td>0</td><td>字符串</td></tr><tr><td>PARAM_TYPE_INT</td><td>1</td><td>整数</td></tr><tr><td>PARAM_TYPE_FLOAT</td><td>2</td><td>浮点数</td></tr><tr><td>PARAM_TYPE_BOOL</td><td>3</td><td>布尔值</td></tr><tr><td>PARAM_TYPE_OBJECT</td><td>4</td><td>对象</td></tr><tr><td>PARAM_TYPE_ARRAY_STRING</td><td>5</td><td>字符串数组</td></tr><tr><td>PARAM_TYPE_ARRAY_INT</td><td>6</td><td>整数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_FLOAT</td><td>7</td><td>浮点数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_BOOL</td><td>8</td><td>布尔值数组</td></tr><tr><td>PARAM_TYPE_ARRAY_OBJECT</td><td>9</td><td>对象数组</td></tr><tr><td>PARAM_TYPE_ARRAY_ARRAY</td><td>20</td><td>数组嵌套</td></tr><tr><td>PARAM_TYPE_NULL</td><td>99</td><td>空值</td></tr><tr><td>PARAM_TYPE_UNSPECIFIED</td><td>100</td><td>未指定类型，用于OneOf和AnyOf场景</td></tr></tbody></table>
        :type Type: int
        """
        self._AnyOf = None
        self._DefaultValue = None
        self._Description = None
        self._IsGlobalHidden = None
        self._IsRequired = None
        self._Name = None
        self._OneOf = None
        self._SubParams = None
        self._Type = None

    @property
    def AnyOf(self):
        r"""<p>AnyOf类型的参数</p>
        :rtype: list of RequestParam
        """
        return self._AnyOf

    @AnyOf.setter
    def AnyOf(self, AnyOf):
        self._AnyOf = AnyOf

    @property
    def DefaultValue(self):
        r"""<p>默认值</p>
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Description(self):
        r"""<p>参数描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IsGlobalHidden(self):
        r"""<p>全局隐藏不可见（区别于Agent场景的agent_hidden），true-全局隐藏不可见，false-可见</p>
        :rtype: bool
        """
        return self._IsGlobalHidden

    @IsGlobalHidden.setter
    def IsGlobalHidden(self, IsGlobalHidden):
        self._IsGlobalHidden = IsGlobalHidden

    @property
    def IsRequired(self):
        r"""<p>是否必选</p>
        :rtype: bool
        """
        return self._IsRequired

    @IsRequired.setter
    def IsRequired(self, IsRequired):
        self._IsRequired = IsRequired

    @property
    def Name(self):
        r"""<p>参数名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def OneOf(self):
        r"""<p>OneOf类型的参数</p>
        :rtype: list of RequestParam
        """
        return self._OneOf

    @OneOf.setter
    def OneOf(self, OneOf):
        self._OneOf = OneOf

    @property
    def SubParams(self):
        r"""<p>子参数,ParamType 是OBJECT 或 ARRAY&lt;&gt;类型有用</p>
        :rtype: list of RequestParam
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def Type(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>PARAM_TYPE_STRING</td><td>0</td><td>字符串</td></tr><tr><td>PARAM_TYPE_INT</td><td>1</td><td>整数</td></tr><tr><td>PARAM_TYPE_FLOAT</td><td>2</td><td>浮点数</td></tr><tr><td>PARAM_TYPE_BOOL</td><td>3</td><td>布尔值</td></tr><tr><td>PARAM_TYPE_OBJECT</td><td>4</td><td>对象</td></tr><tr><td>PARAM_TYPE_ARRAY_STRING</td><td>5</td><td>字符串数组</td></tr><tr><td>PARAM_TYPE_ARRAY_INT</td><td>6</td><td>整数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_FLOAT</td><td>7</td><td>浮点数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_BOOL</td><td>8</td><td>布尔值数组</td></tr><tr><td>PARAM_TYPE_ARRAY_OBJECT</td><td>9</td><td>对象数组</td></tr><tr><td>PARAM_TYPE_ARRAY_ARRAY</td><td>20</td><td>数组嵌套</td></tr><tr><td>PARAM_TYPE_NULL</td><td>99</td><td>空值</td></tr><tr><td>PARAM_TYPE_UNSPECIFIED</td><td>100</td><td>未指定类型，用于OneOf和AnyOf场景</td></tr></tbody></table>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("AnyOf") is not None:
            self._AnyOf = []
            for item in params.get("AnyOf"):
                obj = RequestParam()
                obj._deserialize(item)
                self._AnyOf.append(obj)
        self._DefaultValue = params.get("DefaultValue")
        self._Description = params.get("Description")
        self._IsGlobalHidden = params.get("IsGlobalHidden")
        self._IsRequired = params.get("IsRequired")
        self._Name = params.get("Name")
        if params.get("OneOf") is not None:
            self._OneOf = []
            for item in params.get("OneOf"):
                obj = RequestParam()
                obj._deserialize(item)
                self._OneOf.append(obj)
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = RequestParam()
                obj._deserialize(item)
                self._SubParams.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetConversationRequest(AbstractModel):
    r"""ResetConversation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ConversationId: <p>会话 ID</p>
        :type ConversationId: str
        :param _Type: <p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :type Type: int
        :param _AppKey: <p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :type AppKey: str
        :param _LoginSubAccountUin: <p>子用户Uin</p>
        :type LoginSubAccountUin: str
        :param _LoginUin: <p>主用户Uin</p>
        :type LoginUin: str
        :param _ShareCode: <p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :type ShareCode: str
        :param _UserId: <p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :type UserId: str
        """
        self._ConversationId = None
        self._Type = None
        self._AppKey = None
        self._LoginSubAccountUin = None
        self._LoginUin = None
        self._ShareCode = None
        self._UserId = None

    @property
    def ConversationId(self):
        r"""<p>会话 ID</p>
        :rtype: str
        """
        return self._ConversationId

    @ConversationId.setter
    def ConversationId(self, ConversationId):
        self._ConversationId = ConversationId

    @property
    def Type(self):
        r"""<p>会话类型 枚举值: 0-CONVERSATION_TYPE_UNSPECIFIED(未指定；列表查询时表示全部), 1-CONVERSATION_TYPE_VISITOR(访客端体验), 2-CONVERSATION_TYPE_EVALUATION(评测), 5-CONVERSATION_TYPE_API(API 接入), 10-CONVERSATION_TYPE_WORKFLOW(工作流调试), 20-CONVERSATION_TYPE_SHARE(分享链接)</p>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AppKey(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，应用密钥</p>
        :rtype: str
        """
        return self._AppKey

    @AppKey.setter
    def AppKey(self, AppKey):
        self._AppKey = AppKey

    @property
    def LoginSubAccountUin(self):
        r"""<p>子用户Uin</p>
        :rtype: str
        """
        return self._LoginSubAccountUin

    @LoginSubAccountUin.setter
    def LoginSubAccountUin(self, LoginSubAccountUin):
        self._LoginSubAccountUin = LoginSubAccountUin

    @property
    def LoginUin(self):
        r"""<p>主用户Uin</p>
        :rtype: str
        """
        return self._LoginUin

    @LoginUin.setter
    def LoginUin(self, LoginUin):
        self._LoginUin = LoginUin

    @property
    def ShareCode(self):
        r"""<p>Type=CONVERSATION_TYPE_SHARE 时必填，分享码</p>
        :rtype: str
        """
        return self._ShareCode

    @ShareCode.setter
    def ShareCode(self, ShareCode):
        self._ShareCode = ShareCode

    @property
    def UserId(self):
        r"""<p>Type=CONVERSATION_TYPE_API 时必填，访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ConversationId = params.get("ConversationId")
        self._Type = params.get("Type")
        self._AppKey = params.get("AppKey")
        self._LoginSubAccountUin = params.get("LoginSubAccountUin")
        self._LoginUin = params.get("LoginUin")
        self._ShareCode = params.get("ShareCode")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetConversationResponse(AbstractModel):
    r"""ResetConversation返回参数结构体

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


class ResourceConsumption(AbstractModel):
    r"""单项消耗计量

    """

    def __init__(self):
        r"""
        :param _Label: <p>功能标签，PLATFORM 场景取 PlatformBizType 枚举名称；MODEL/PLUGIN 场景为空</p>
        :type Label: str
        :param _Unit: <p>消耗计量单位</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>DOSAGE_UNIT_TOKEN</td><td>0</td><td>token（默认）</td></tr><tr><td>DOSAGE_UNIT_PAGE_COUNT</td><td>1</td><td>page_count（页数）</td></tr><tr><td>DOSAGE_UNIT_TIMES</td><td>2</td><td>times（次数）</td></tr><tr><td>DOSAGE_UNIT_SECOND</td><td>3</td><td>second（秒）</td></tr><tr><td>DOSAGE_UNIT_ITEM</td><td>4</td><td>item（条）</td></tr><tr><td>DOSAGE_UNIT_SHEET</td><td>5</td><td>sheet（张）</td></tr><tr><td>DOSAGE_UNIT_CHARACTER</td><td>6</td><td>character（字符）</td></tr><tr><td>DOSAGE_UNIT_GB</td><td>7</td><td>GB</td></tr><tr><td>DOSAGE_UNIT_NUMBER</td><td>8</td><td>number（个数）</td></tr><tr><td>DOSAGE_UNIT_MILL_SECOND</td><td>9</td><td>mill_second（毫秒）</td></tr></tbody></table>
        :type Unit: int
        :param _Value: <p>消耗数值</p>
        :type Value: float
        """
        self._Label = None
        self._Unit = None
        self._Value = None

    @property
    def Label(self):
        r"""<p>功能标签，PLATFORM 场景取 PlatformBizType 枚举名称；MODEL/PLUGIN 场景为空</p>
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Unit(self):
        r"""<p>消耗计量单位</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>DOSAGE_UNIT_TOKEN</td><td>0</td><td>token（默认）</td></tr><tr><td>DOSAGE_UNIT_PAGE_COUNT</td><td>1</td><td>page_count（页数）</td></tr><tr><td>DOSAGE_UNIT_TIMES</td><td>2</td><td>times（次数）</td></tr><tr><td>DOSAGE_UNIT_SECOND</td><td>3</td><td>second（秒）</td></tr><tr><td>DOSAGE_UNIT_ITEM</td><td>4</td><td>item（条）</td></tr><tr><td>DOSAGE_UNIT_SHEET</td><td>5</td><td>sheet（张）</td></tr><tr><td>DOSAGE_UNIT_CHARACTER</td><td>6</td><td>character（字符）</td></tr><tr><td>DOSAGE_UNIT_GB</td><td>7</td><td>GB</td></tr><tr><td>DOSAGE_UNIT_NUMBER</td><td>8</td><td>number（个数）</td></tr><tr><td>DOSAGE_UNIT_MILL_SECOND</td><td>9</td><td>mill_second（毫秒）</td></tr></tbody></table>
        :rtype: int
        """
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Value(self):
        r"""<p>消耗数值</p>
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Label = params.get("Label")
        self._Unit = params.get("Unit")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseParam(AbstractModel):
    r"""ResponseParam

    """

    def __init__(self):
        r"""
        :param _Description: <p>变量描述</p>
        :type Description: str
        :param _Name: <p>参数名称</p>
        :type Name: str
        :param _RenderMode: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>OUTPUT_RENDER_REPLACE</td><td>0</td><td>覆盖（全量替换）</td></tr><tr><td>OUTPUT_RENDER_APPEND</td><td>1</td><td>增量追加</td></tr></tbody></table>
        :type RenderMode: int
        :param _SubParams: <p>只对 OBJECT 或 ARRAY_OBJECT 类型有用</p>
        :type SubParams: list of ResponseParam
        :param _Type: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>PARAM_TYPE_STRING</td><td>0</td><td>字符串</td></tr><tr><td>PARAM_TYPE_INT</td><td>1</td><td>整数</td></tr><tr><td>PARAM_TYPE_FLOAT</td><td>2</td><td>浮点数</td></tr><tr><td>PARAM_TYPE_BOOL</td><td>3</td><td>布尔值</td></tr><tr><td>PARAM_TYPE_OBJECT</td><td>4</td><td>对象</td></tr><tr><td>PARAM_TYPE_ARRAY_STRING</td><td>5</td><td>字符串数组</td></tr><tr><td>PARAM_TYPE_ARRAY_INT</td><td>6</td><td>整数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_FLOAT</td><td>7</td><td>浮点数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_BOOL</td><td>8</td><td>布尔值数组</td></tr><tr><td>PARAM_TYPE_ARRAY_OBJECT</td><td>9</td><td>对象数组</td></tr><tr><td>PARAM_TYPE_ARRAY_ARRAY</td><td>20</td><td>数组嵌套</td></tr><tr><td>PARAM_TYPE_NULL</td><td>99</td><td>空值</td></tr><tr><td>PARAM_TYPE_UNSPECIFIED</td><td>100</td><td>未指定类型，用于OneOf和AnyOf场景</td></tr></tbody></table>
        :type Type: int
        """
        self._Description = None
        self._Name = None
        self._RenderMode = None
        self._SubParams = None
        self._Type = None

    @property
    def Description(self):
        r"""<p>变量描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""<p>参数名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RenderMode(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>OUTPUT_RENDER_REPLACE</td><td>0</td><td>覆盖（全量替换）</td></tr><tr><td>OUTPUT_RENDER_APPEND</td><td>1</td><td>增量追加</td></tr></tbody></table>
        :rtype: int
        """
        return self._RenderMode

    @RenderMode.setter
    def RenderMode(self, RenderMode):
        self._RenderMode = RenderMode

    @property
    def SubParams(self):
        r"""<p>只对 OBJECT 或 ARRAY_OBJECT 类型有用</p>
        :rtype: list of ResponseParam
        """
        return self._SubParams

    @SubParams.setter
    def SubParams(self, SubParams):
        self._SubParams = SubParams

    @property
    def Type(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>PARAM_TYPE_STRING</td><td>0</td><td>字符串</td></tr><tr><td>PARAM_TYPE_INT</td><td>1</td><td>整数</td></tr><tr><td>PARAM_TYPE_FLOAT</td><td>2</td><td>浮点数</td></tr><tr><td>PARAM_TYPE_BOOL</td><td>3</td><td>布尔值</td></tr><tr><td>PARAM_TYPE_OBJECT</td><td>4</td><td>对象</td></tr><tr><td>PARAM_TYPE_ARRAY_STRING</td><td>5</td><td>字符串数组</td></tr><tr><td>PARAM_TYPE_ARRAY_INT</td><td>6</td><td>整数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_FLOAT</td><td>7</td><td>浮点数数组</td></tr><tr><td>PARAM_TYPE_ARRAY_BOOL</td><td>8</td><td>布尔值数组</td></tr><tr><td>PARAM_TYPE_ARRAY_OBJECT</td><td>9</td><td>对象数组</td></tr><tr><td>PARAM_TYPE_ARRAY_ARRAY</td><td>20</td><td>数组嵌套</td></tr><tr><td>PARAM_TYPE_NULL</td><td>99</td><td>空值</td></tr><tr><td>PARAM_TYPE_UNSPECIFIED</td><td>100</td><td>未指定类型，用于OneOf和AnyOf场景</td></tr></tbody></table>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._RenderMode = params.get("RenderMode")
        if params.get("SubParams") is not None:
            self._SubParams = []
            for item in params.get("SubParams"):
                obj = ResponseParam()
                obj._deserialize(item)
                self._SubParams.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeAppTriggerRequest(AbstractModel):
    r"""ResumeAppTrigger请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerId: <p>应用触发器ID</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._Scope = None
        self._TriggerId = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerId(self):
        r"""<p>应用触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Scope = params.get("Scope")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeAppTriggerResponse(AbstractModel):
    r"""ResumeAppTrigger返回参数结构体

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


class RetryReleaseRequest(AbstractModel):
    r"""RetryRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _ReleaseId: 发布任务ID
        :type ReleaseId: str
        """
        self._AppId = None
        self._ReleaseId = None

    @property
    def AppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ReleaseId(self):
        r"""发布任务ID
        :rtype: str
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ReleaseId = params.get("ReleaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetryReleaseResponse(AbstractModel):
    r"""RetryRelease返回参数结构体

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


class RoleConfig(AbstractModel):
    r"""角色配置

    """

    def __init__(self):
        r"""
        :param _RoleDescription: 角色描述
        :type RoleDescription: str
        """
        self._RoleDescription = None

    @property
    def RoleDescription(self):
        r"""角色描述
        :rtype: str
        """
        return self._RoleDescription

    @RoleDescription.setter
    def RoleDescription(self, RoleDescription):
        self._RoleDescription = RoleDescription


    def _deserialize(self, params):
        self._RoleDescription = params.get("RoleDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackReleaseRequest(AbstractModel):
    r"""RollbackRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: app_id
        :type AppId: str
        :param _ReleaseId: release_id
        :type ReleaseId: str
        """
        self._AppId = None
        self._ReleaseId = None

    @property
    def AppId(self):
        r"""app_id
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def ReleaseId(self):
        r"""release_id
        :rtype: str
        """
        return self._ReleaseId

    @ReleaseId.setter
    def ReleaseId(self, ReleaseId):
        self._ReleaseId = ReleaseId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ReleaseId = params.get("ReleaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackReleaseResponse(AbstractModel):
    r"""RollbackRelease返回参数结构体

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


class RunAppTriggerNowRequest(AbstractModel):
    r"""RunAppTriggerNow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: <p>应用ID</p>
        :type AppId: str
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _TriggerId: <p>应用触发器ID</p>
        :type TriggerId: str
        :param _UserId: <p>访客ID</p>
        :type UserId: str
        """
        self._AppId = None
        self._Scope = None
        self._TriggerId = None
        self._UserId = None

    @property
    def AppId(self):
        r"""<p>应用ID</p>
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def TriggerId(self):
        r"""<p>应用触发器ID</p>
        :rtype: str
        """
        return self._TriggerId

    @TriggerId.setter
    def TriggerId(self, TriggerId):
        self._TriggerId = TriggerId

    @property
    def UserId(self):
        r"""<p>访客ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Scope = params.get("Scope")
        self._TriggerId = params.get("TriggerId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunAppTriggerNowResponse(AbstractModel):
    r"""RunAppTriggerNow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>应用触发器实例ID</p>
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        r"""<p>应用触发器实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class SearchResourceStatusInfo(AbstractModel):
    r"""搜索资源状态信息

    """

    def __init__(self):
        r"""
        :param _ResourceStatus: 搜索资源状态: AVAILABLE(1)=资源可用, EXHAUSTED(2)=资源已用尽。枚举值: 1:资源可用, 2:资源已用尽
        :type ResourceStatus: int
        """
        self._ResourceStatus = None

    @property
    def ResourceStatus(self):
        r"""搜索资源状态: AVAILABLE(1)=资源可用, EXHAUSTED(2)=资源已用尽。枚举值: 1:资源可用, 2:资源已用尽
        :rtype: int
        """
        return self._ResourceStatus

    @ResourceStatus.setter
    def ResourceStatus(self, ResourceStatus):
        self._ResourceStatus = ResourceStatus


    def _deserialize(self, params):
        self._ResourceStatus = params.get("ResourceStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SingleWorkflowConfig(AbstractModel):
    r"""单工作流配置

    """

    def __init__(self):
        r"""
        :param _AsyncWorkflow: <p>是否开启异步工作流</p>
        :type AsyncWorkflow: bool
        :param _Status: <p>状态 发布状态(UNPUBLISHED: 待发布 PUBLISHING: 发布中 PUBLISHED: 已发布 PUBLISHED_FAIL:发布失败；DRAFT：待调试)</p>
        :type Status: str
        :param _WorkflowDescription: <p>工作流描述</p>
        :type WorkflowDescription: str
        :param _WorkflowId: <p>工作流Id</p>
        :type WorkflowId: str
        :param _WorkflowName: <p>工作流名称</p>
        :type WorkflowName: str
        :param _Enabled: <p>工作流是否启用</p>
        :type Enabled: bool
        """
        self._AsyncWorkflow = None
        self._Status = None
        self._WorkflowDescription = None
        self._WorkflowId = None
        self._WorkflowName = None
        self._Enabled = None

    @property
    def AsyncWorkflow(self):
        r"""<p>是否开启异步工作流</p>
        :rtype: bool
        """
        return self._AsyncWorkflow

    @AsyncWorkflow.setter
    def AsyncWorkflow(self, AsyncWorkflow):
        self._AsyncWorkflow = AsyncWorkflow

    @property
    def Status(self):
        r"""<p>状态 发布状态(UNPUBLISHED: 待发布 PUBLISHING: 发布中 PUBLISHED: 已发布 PUBLISHED_FAIL:发布失败；DRAFT：待调试)</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WorkflowDescription(self):
        r"""<p>工作流描述</p>
        :rtype: str
        """
        return self._WorkflowDescription

    @WorkflowDescription.setter
    def WorkflowDescription(self, WorkflowDescription):
        self._WorkflowDescription = WorkflowDescription

    @property
    def WorkflowId(self):
        r"""<p>工作流Id</p>
        :rtype: str
        """
        return self._WorkflowId

    @WorkflowId.setter
    def WorkflowId(self, WorkflowId):
        self._WorkflowId = WorkflowId

    @property
    def WorkflowName(self):
        r"""<p>工作流名称</p>
        :rtype: str
        """
        return self._WorkflowName

    @WorkflowName.setter
    def WorkflowName(self, WorkflowName):
        self._WorkflowName = WorkflowName

    @property
    def Enabled(self):
        r"""<p>工作流是否启用</p>
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._AsyncWorkflow = params.get("AsyncWorkflow")
        self._Status = params.get("Status")
        self._WorkflowDescription = params.get("WorkflowDescription")
        self._WorkflowId = params.get("WorkflowId")
        self._WorkflowName = params.get("WorkflowName")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillAnalysisInfo(AbstractModel):
    r"""SkillAnalysisInfo Skill 安全扫描信息。

    """

    def __init__(self):
        r"""
        :param _AnalysisStatus: 安全检测状态

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 待检测 |
| 1 | 检测中 |
| 2 | 可用 |
| 3 | 不可用 |
| 4 | 检测失败 |
        :type AnalysisStatus: int
        :param _RiskDescription: 风险描述
        :type RiskDescription: str
        :param _RiskLevel: 风险等级

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 无风险 |
| 1 | 低风险 |
| 2 | 中风险 |
| 3 | 高风险 |
        :type RiskLevel: int
        :param _SecurityReportUrl: 安全报告跳转url;
        :type SecurityReportUrl: str
        """
        self._AnalysisStatus = None
        self._RiskDescription = None
        self._RiskLevel = None
        self._SecurityReportUrl = None

    @property
    def AnalysisStatus(self):
        r"""安全检测状态

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 待检测 |
| 1 | 检测中 |
| 2 | 可用 |
| 3 | 不可用 |
| 4 | 检测失败 |
        :rtype: int
        """
        return self._AnalysisStatus

    @AnalysisStatus.setter
    def AnalysisStatus(self, AnalysisStatus):
        self._AnalysisStatus = AnalysisStatus

    @property
    def RiskDescription(self):
        r"""风险描述
        :rtype: str
        """
        return self._RiskDescription

    @RiskDescription.setter
    def RiskDescription(self, RiskDescription):
        self._RiskDescription = RiskDescription

    @property
    def RiskLevel(self):
        r"""风险等级

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 无风险 |
| 1 | 低风险 |
| 2 | 中风险 |
| 3 | 高风险 |
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def SecurityReportUrl(self):
        r"""安全报告跳转url;
        :rtype: str
        """
        return self._SecurityReportUrl

    @SecurityReportUrl.setter
    def SecurityReportUrl(self, SecurityReportUrl):
        self._SecurityReportUrl = SecurityReportUrl


    def _deserialize(self, params):
        self._AnalysisStatus = params.get("AnalysisStatus")
        self._RiskDescription = params.get("RiskDescription")
        self._RiskLevel = params.get("RiskLevel")
        self._SecurityReportUrl = params.get("SecurityReportUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillCategory(AbstractModel):
    r"""SkillCategory Skill 分类信息。

    """

    def __init__(self):
        r"""
        :param _CategoryKey: 分类标识
        :type CategoryKey: str
        :param _CategoryName: 分类名称
        :type CategoryName: str
        """
        self._CategoryKey = None
        self._CategoryName = None

    @property
    def CategoryKey(self):
        r"""分类标识
        :rtype: str
        """
        return self._CategoryKey

    @CategoryKey.setter
    def CategoryKey(self, CategoryKey):
        self._CategoryKey = CategoryKey

    @property
    def CategoryName(self):
        r"""分类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName


    def _deserialize(self, params):
        self._CategoryKey = params.get("CategoryKey")
        self._CategoryName = params.get("CategoryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillClassification(AbstractModel):
    r"""SkillClassification Skill 分类与来源信息。

    """

    def __init__(self):
        r"""
        :param _BillingType: Skill 计费类型

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 免费 |
| 1 | 付费 |
        :type BillingType: int
        :param _BuiltinSource: Skill 内置来源，仅在 create_type 为 SKILL_CREATE_TYPE_BUILTIN 时生效

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | ADP 专有 |
| 2 | 腾讯专有 |
| 3 | SkillHub |
| 99 | 其他 |
        :type BuiltinSource: int
        :param _CategoryKey: Skill 分类
        :type CategoryKey: str
        :param _CreateType: Skill 创建方式

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 文件上传 |
| 2 | 由企业级共享流程生成 |
| 3 | AIGC 生成 |
| 99 | 内置 Skill |
        :type CreateType: int
        :param _ProviderType: Skill 提供方类型

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 官方 |
| 2 | 第三方 |
| 3 | 自定义 |
| 4 | 自定义企业级共享 |
        :type ProviderType: int
        :param _SourceLink: Skill 来源链接
        :type SourceLink: str
        """
        self._BillingType = None
        self._BuiltinSource = None
        self._CategoryKey = None
        self._CreateType = None
        self._ProviderType = None
        self._SourceLink = None

    @property
    def BillingType(self):
        r"""Skill 计费类型

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 免费 |
| 1 | 付费 |
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def BuiltinSource(self):
        r"""Skill 内置来源，仅在 create_type 为 SKILL_CREATE_TYPE_BUILTIN 时生效

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | ADP 专有 |
| 2 | 腾讯专有 |
| 3 | SkillHub |
| 99 | 其他 |
        :rtype: int
        """
        return self._BuiltinSource

    @BuiltinSource.setter
    def BuiltinSource(self, BuiltinSource):
        self._BuiltinSource = BuiltinSource

    @property
    def CategoryKey(self):
        r"""Skill 分类
        :rtype: str
        """
        return self._CategoryKey

    @CategoryKey.setter
    def CategoryKey(self, CategoryKey):
        self._CategoryKey = CategoryKey

    @property
    def CreateType(self):
        r"""Skill 创建方式

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 文件上传 |
| 2 | 由企业级共享流程生成 |
| 3 | AIGC 生成 |
| 99 | 内置 Skill |
        :rtype: int
        """
        return self._CreateType

    @CreateType.setter
    def CreateType(self, CreateType):
        self._CreateType = CreateType

    @property
    def ProviderType(self):
        r"""Skill 提供方类型

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 官方 |
| 2 | 第三方 |
| 3 | 自定义 |
| 4 | 自定义企业级共享 |
        :rtype: int
        """
        return self._ProviderType

    @ProviderType.setter
    def ProviderType(self, ProviderType):
        self._ProviderType = ProviderType

    @property
    def SourceLink(self):
        r"""Skill 来源链接
        :rtype: str
        """
        return self._SourceLink

    @SourceLink.setter
    def SourceLink(self, SourceLink):
        self._SourceLink = SourceLink


    def _deserialize(self, params):
        self._BillingType = params.get("BillingType")
        self._BuiltinSource = params.get("BuiltinSource")
        self._CategoryKey = params.get("CategoryKey")
        self._CreateType = params.get("CreateType")
        self._ProviderType = params.get("ProviderType")
        self._SourceLink = params.get("SourceLink")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillDetail(AbstractModel):
    r"""skill详情

    """

    def __init__(self):
        r"""
        :param _ReferenceSummaryList: 调用情况摘要
        :type ReferenceSummaryList: list of SkillReferenceSummary
        :param _SkillSummary: Skill 摘要
        :type SkillSummary: :class:`tencentcloud.adp.v20260520.models.SkillSummary`
        :param _VersionList: 版本列表
        :type VersionList: list of SkillVersion
        """
        self._ReferenceSummaryList = None
        self._SkillSummary = None
        self._VersionList = None

    @property
    def ReferenceSummaryList(self):
        r"""调用情况摘要
        :rtype: list of SkillReferenceSummary
        """
        return self._ReferenceSummaryList

    @ReferenceSummaryList.setter
    def ReferenceSummaryList(self, ReferenceSummaryList):
        self._ReferenceSummaryList = ReferenceSummaryList

    @property
    def SkillSummary(self):
        r"""Skill 摘要
        :rtype: :class:`tencentcloud.adp.v20260520.models.SkillSummary`
        """
        return self._SkillSummary

    @SkillSummary.setter
    def SkillSummary(self, SkillSummary):
        self._SkillSummary = SkillSummary

    @property
    def VersionList(self):
        r"""版本列表
        :rtype: list of SkillVersion
        """
        return self._VersionList

    @VersionList.setter
    def VersionList(self, VersionList):
        self._VersionList = VersionList


    def _deserialize(self, params):
        if params.get("ReferenceSummaryList") is not None:
            self._ReferenceSummaryList = []
            for item in params.get("ReferenceSummaryList"):
                obj = SkillReferenceSummary()
                obj._deserialize(item)
                self._ReferenceSummaryList.append(obj)
        if params.get("SkillSummary") is not None:
            self._SkillSummary = SkillSummary()
            self._SkillSummary._deserialize(params.get("SkillSummary"))
        if params.get("VersionList") is not None:
            self._VersionList = []
            for item in params.get("VersionList"):
                obj = SkillVersion()
                obj._deserialize(item)
                self._VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillNotice(AbstractModel):
    r"""Skill 异常通知。

    """

    def __init__(self):
        r"""
        :param _Level: 通知级别

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 成功，字符串面："success" |
| 2 | 警告，字符串面："warning" |
| 3 | 错误，字符串面："error" |
        :type Level: int
        :param _NoticeContent: 文案（i18n 后字符串）
        :type NoticeContent: str
        :param _TriggerVersionId: 触发本通知的 Skill 版本ID
        :type TriggerVersionId: str
        :param _Type: 通知类型 

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 发布失败 |
| 2 | 共享审批被拒 |
        :type Type: int
        """
        self._Level = None
        self._NoticeContent = None
        self._TriggerVersionId = None
        self._Type = None

    @property
    def Level(self):
        r"""通知级别

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 成功，字符串面："success" |
| 2 | 警告，字符串面："warning" |
| 3 | 错误，字符串面："error" |
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def NoticeContent(self):
        r"""文案（i18n 后字符串）
        :rtype: str
        """
        return self._NoticeContent

    @NoticeContent.setter
    def NoticeContent(self, NoticeContent):
        self._NoticeContent = NoticeContent

    @property
    def TriggerVersionId(self):
        r"""触发本通知的 Skill 版本ID
        :rtype: str
        """
        return self._TriggerVersionId

    @TriggerVersionId.setter
    def TriggerVersionId(self, TriggerVersionId):
        self._TriggerVersionId = TriggerVersionId

    @property
    def Type(self):
        r"""通知类型 

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 占位 |
| 1 | 发布失败 |
| 2 | 共享审批被拒 |
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._NoticeContent = params.get("NoticeContent")
        self._TriggerVersionId = params.get("TriggerVersionId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillProfile(AbstractModel):
    r"""SkillProfile Skill 基础展示信息。

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间（Unix秒）
        :type CreateTime: str
        :param _Creator: 创建者
        :type Creator: str
        :param _Description: Skill 描述
        :type Description: str
        :param _DisplayDescription: Skill 展示描述
        :type DisplayDescription: str
        :param _DisplayName: Skill 展示名称
        :type DisplayName: str
        :param _IconUrl: Skill 图标
        :type IconUrl: str
        :param _Name: Skill 名称
        :type Name: str
        :param _UpdateTime: 更新时间（Unix秒）
        :type UpdateTime: str
        """
        self._CreateTime = None
        self._Creator = None
        self._Description = None
        self._DisplayDescription = None
        self._DisplayName = None
        self._IconUrl = None
        self._Name = None
        self._UpdateTime = None

    @property
    def CreateTime(self):
        r"""创建时间（Unix秒）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Creator(self):
        r"""创建者
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def Description(self):
        r"""Skill 描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DisplayDescription(self):
        r"""Skill 展示描述
        :rtype: str
        """
        return self._DisplayDescription

    @DisplayDescription.setter
    def DisplayDescription(self, DisplayDescription):
        self._DisplayDescription = DisplayDescription

    @property
    def DisplayName(self):
        r"""Skill 展示名称
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def IconUrl(self):
        r"""Skill 图标
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Name(self):
        r"""Skill 名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def UpdateTime(self):
        r"""更新时间（Unix秒）
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._Creator = params.get("Creator")
        self._Description = params.get("Description")
        self._DisplayDescription = params.get("DisplayDescription")
        self._DisplayName = params.get("DisplayName")
        self._IconUrl = params.get("IconUrl")
        self._Name = params.get("Name")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillReferenceGroup(AbstractModel):
    r"""同一 SkillRefType 下的引用分组（含总数 + 引用详情列表）。 total_count 始终以未过滤的原始总量为准；reference_summary_list 受二次鉴权开关影响。

    """

    def __init__(self):
        r"""
        :param _ReferenceSummaryList: <p>该类型下的引用详情列表</p>
        :type ReferenceSummaryList: list of SkillReferenceSummary
        :param _ReferenceType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>SKILL_REF_UNKNOWN</td><td>0</td><td>占位</td></tr><tr><td>SKILL_REF_OPENCLAW</td><td>1</td><td>openclaw</td></tr><tr><td>SKILL_REF_AGENT</td><td>2</td><td>agent</td></tr><tr><td>SKILL_REF_CORP_ASSISTANT</td><td>3</td><td>企业助手</td></tr></tbody></table>
        :type ReferenceType: int
        :param _TotalCount: <p>该类型下的引用总数</p>
        :type TotalCount: int
        """
        self._ReferenceSummaryList = None
        self._ReferenceType = None
        self._TotalCount = None

    @property
    def ReferenceSummaryList(self):
        r"""<p>该类型下的引用详情列表</p>
        :rtype: list of SkillReferenceSummary
        """
        return self._ReferenceSummaryList

    @ReferenceSummaryList.setter
    def ReferenceSummaryList(self, ReferenceSummaryList):
        self._ReferenceSummaryList = ReferenceSummaryList

    @property
    def ReferenceType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>SKILL_REF_UNKNOWN</td><td>0</td><td>占位</td></tr><tr><td>SKILL_REF_OPENCLAW</td><td>1</td><td>openclaw</td></tr><tr><td>SKILL_REF_AGENT</td><td>2</td><td>agent</td></tr><tr><td>SKILL_REF_CORP_ASSISTANT</td><td>3</td><td>企业助手</td></tr></tbody></table>
        :rtype: int
        """
        return self._ReferenceType

    @ReferenceType.setter
    def ReferenceType(self, ReferenceType):
        self._ReferenceType = ReferenceType

    @property
    def TotalCount(self):
        r"""<p>该类型下的引用总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        if params.get("ReferenceSummaryList") is not None:
            self._ReferenceSummaryList = []
            for item in params.get("ReferenceSummaryList"):
                obj = SkillReferenceSummary()
                obj._deserialize(item)
                self._ReferenceSummaryList.append(obj)
        self._ReferenceType = params.get("ReferenceType")
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillReferenceSummary(AbstractModel):
    r"""引用摘要（用于详情页展示，对应DB t_skill_reference）

    """

    def __init__(self):
        r"""
        :param _ReferenceId: <p>关联ID</p>
        :type ReferenceId: str
        :param _ReferenceName: <p>关联名称</p>
        :type ReferenceName: str
        :param _ReferenceType: <p>关联类型</p><p>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 | 占位 |<br>| 1 | ClawPro |<br>| 2 | agent |</p>
        :type ReferenceType: int
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        :param _SpaceName: <p>空间名称</p>
        :type SpaceName: str
        :param _Owner: <p>Reference实例拥有者</p>
        :type Owner: str
        """
        self._ReferenceId = None
        self._ReferenceName = None
        self._ReferenceType = None
        self._SpaceId = None
        self._SpaceName = None
        self._Owner = None

    @property
    def ReferenceId(self):
        r"""<p>关联ID</p>
        :rtype: str
        """
        return self._ReferenceId

    @ReferenceId.setter
    def ReferenceId(self, ReferenceId):
        self._ReferenceId = ReferenceId

    @property
    def ReferenceName(self):
        r"""<p>关联名称</p>
        :rtype: str
        """
        return self._ReferenceName

    @ReferenceName.setter
    def ReferenceName(self, ReferenceName):
        self._ReferenceName = ReferenceName

    @property
    def ReferenceType(self):
        r"""<p>关联类型</p><p>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 | 占位 |<br>| 1 | ClawPro |<br>| 2 | agent |</p>
        :rtype: int
        """
        return self._ReferenceType

    @ReferenceType.setter
    def ReferenceType(self, ReferenceType):
        self._ReferenceType = ReferenceType

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def SpaceName(self):
        r"""<p>空间名称</p>
        :rtype: str
        """
        return self._SpaceName

    @SpaceName.setter
    def SpaceName(self, SpaceName):
        self._SpaceName = SpaceName

    @property
    def Owner(self):
        r"""<p>Reference实例拥有者</p>
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._ReferenceId = params.get("ReferenceId")
        self._ReferenceName = params.get("ReferenceName")
        self._ReferenceType = params.get("ReferenceType")
        self._SpaceId = params.get("SpaceId")
        self._SpaceName = params.get("SpaceName")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillShare(AbstractModel):
    r"""SkillShare Skill 企业共享信息。

    """

    def __init__(self):
        r"""
        :param _ApprovalId: 审批ID
        :type ApprovalId: str
        :param _ShareSkillId: 共享后关联的新 skill_id
        :type ShareSkillId: str
        :param _ShareVersion: 共享版本，如 1.0.0
        :type ShareVersion: str
        :param _ShareVersionId: 共享版本ID
        :type ShareVersionId: str
        :param _SkillId: 原 skill_id
        :type SkillId: str
        :param _Status: 共享状态

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 未共享 |
| 1 | 已共享 |
| 2 | 审批中 |
        :type Status: int
        """
        self._ApprovalId = None
        self._ShareSkillId = None
        self._ShareVersion = None
        self._ShareVersionId = None
        self._SkillId = None
        self._Status = None

    @property
    def ApprovalId(self):
        r"""审批ID
        :rtype: str
        """
        return self._ApprovalId

    @ApprovalId.setter
    def ApprovalId(self, ApprovalId):
        self._ApprovalId = ApprovalId

    @property
    def ShareSkillId(self):
        r"""共享后关联的新 skill_id
        :rtype: str
        """
        return self._ShareSkillId

    @ShareSkillId.setter
    def ShareSkillId(self, ShareSkillId):
        self._ShareSkillId = ShareSkillId

    @property
    def ShareVersion(self):
        r"""共享版本，如 1.0.0
        :rtype: str
        """
        return self._ShareVersion

    @ShareVersion.setter
    def ShareVersion(self, ShareVersion):
        self._ShareVersion = ShareVersion

    @property
    def ShareVersionId(self):
        r"""共享版本ID
        :rtype: str
        """
        return self._ShareVersionId

    @ShareVersionId.setter
    def ShareVersionId(self, ShareVersionId):
        self._ShareVersionId = ShareVersionId

    @property
    def SkillId(self):
        r"""原 skill_id
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def Status(self):
        r"""共享状态

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 未共享 |
| 1 | 已共享 |
| 2 | 审批中 |
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ApprovalId = params.get("ApprovalId")
        self._ShareSkillId = params.get("ShareSkillId")
        self._ShareVersion = params.get("ShareVersion")
        self._ShareVersionId = params.get("ShareVersionId")
        self._SkillId = params.get("SkillId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillSummary(AbstractModel):
    r"""SkillSummary 列表中的 Skill 摘要。

    """

    def __init__(self):
        r"""
        :param _ClassificationInfo: 分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClassificationInfo: :class:`tencentcloud.adp.v20260520.models.SkillClassification`
        :param _CurrentVersionInfo: 当前版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CurrentVersionInfo: :class:`tencentcloud.adp.v20260520.models.SkillVersion`
        :param _IsFavorite: 当前用户是否收藏
        :type IsFavorite: bool
        :param _Profile: 基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Profile: :class:`tencentcloud.adp.v20260520.models.SkillProfile`
        :param _SkillId: Skill ID
        :type SkillId: str
        :param _NoticeList: Skill 异常通知列表
        :type NoticeList: list of SkillNotice
        :param _PermissionIdList: 当前用户对该 Skill 的资源操作权限位列表；内置/共享 Skill 固定为空数组
        :type PermissionIdList: list of str
        :param _ShareList: 共享信息；可能有两条，一条是已共享的，一条是审核中的
        :type ShareList: list of SkillShare
        :param _SkillStatus: Skill状态 

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 初始化（无任何已发布版本，且最新版本处于 INITIALIZED/UNRELEASED） |
| 1 | 安全检测中（无任何已发布版本，且最新版本处于 AUDITING） |
| 2 | 待发布（无任何已发布版本，且最新版本处于 PENDING_RELEASE） |
| 3 | 已发布（存在任一 RELEASED 版本，吸收态） |
        :type SkillStatus: int
        """
        self._ClassificationInfo = None
        self._CurrentVersionInfo = None
        self._IsFavorite = None
        self._Profile = None
        self._SkillId = None
        self._NoticeList = None
        self._PermissionIdList = None
        self._ShareList = None
        self._SkillStatus = None

    @property
    def ClassificationInfo(self):
        r"""分类信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SkillClassification`
        """
        return self._ClassificationInfo

    @ClassificationInfo.setter
    def ClassificationInfo(self, ClassificationInfo):
        self._ClassificationInfo = ClassificationInfo

    @property
    def CurrentVersionInfo(self):
        r"""当前版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SkillVersion`
        """
        return self._CurrentVersionInfo

    @CurrentVersionInfo.setter
    def CurrentVersionInfo(self, CurrentVersionInfo):
        self._CurrentVersionInfo = CurrentVersionInfo

    @property
    def IsFavorite(self):
        r"""当前用户是否收藏
        :rtype: bool
        """
        return self._IsFavorite

    @IsFavorite.setter
    def IsFavorite(self, IsFavorite):
        self._IsFavorite = IsFavorite

    @property
    def Profile(self):
        r"""基础信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SkillProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def SkillId(self):
        r"""Skill ID
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def NoticeList(self):
        r"""Skill 异常通知列表
        :rtype: list of SkillNotice
        """
        return self._NoticeList

    @NoticeList.setter
    def NoticeList(self, NoticeList):
        self._NoticeList = NoticeList

    @property
    def PermissionIdList(self):
        r"""当前用户对该 Skill 的资源操作权限位列表；内置/共享 Skill 固定为空数组
        :rtype: list of str
        """
        return self._PermissionIdList

    @PermissionIdList.setter
    def PermissionIdList(self, PermissionIdList):
        self._PermissionIdList = PermissionIdList

    @property
    def ShareList(self):
        r"""共享信息；可能有两条，一条是已共享的，一条是审核中的
        :rtype: list of SkillShare
        """
        return self._ShareList

    @ShareList.setter
    def ShareList(self, ShareList):
        self._ShareList = ShareList

    @property
    def SkillStatus(self):
        r"""Skill状态 

枚举值:
| uint | 描述 |
| --- | --- |
| 0 | 初始化（无任何已发布版本，且最新版本处于 INITIALIZED/UNRELEASED） |
| 1 | 安全检测中（无任何已发布版本，且最新版本处于 AUDITING） |
| 2 | 待发布（无任何已发布版本，且最新版本处于 PENDING_RELEASE） |
| 3 | 已发布（存在任一 RELEASED 版本，吸收态） |
        :rtype: int
        """
        return self._SkillStatus

    @SkillStatus.setter
    def SkillStatus(self, SkillStatus):
        self._SkillStatus = SkillStatus


    def _deserialize(self, params):
        if params.get("ClassificationInfo") is not None:
            self._ClassificationInfo = SkillClassification()
            self._ClassificationInfo._deserialize(params.get("ClassificationInfo"))
        if params.get("CurrentVersionInfo") is not None:
            self._CurrentVersionInfo = SkillVersion()
            self._CurrentVersionInfo._deserialize(params.get("CurrentVersionInfo"))
        self._IsFavorite = params.get("IsFavorite")
        if params.get("Profile") is not None:
            self._Profile = SkillProfile()
            self._Profile._deserialize(params.get("Profile"))
        self._SkillId = params.get("SkillId")
        if params.get("NoticeList") is not None:
            self._NoticeList = []
            for item in params.get("NoticeList"):
                obj = SkillNotice()
                obj._deserialize(item)
                self._NoticeList.append(obj)
        self._PermissionIdList = params.get("PermissionIdList")
        if params.get("ShareList") is not None:
            self._ShareList = []
            for item in params.get("ShareList"):
                obj = SkillShare()
                obj._deserialize(item)
                self._ShareList.append(obj)
        self._SkillStatus = params.get("SkillStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SkillVersion(AbstractModel):
    r"""SkillVersion Skill 版本信息。

    """

    def __init__(self):
        r"""
        :param _AnalysisInfo: 检测信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AnalysisInfo: :class:`tencentcloud.adp.v20260520.models.SkillAnalysisInfo`
        :param _Version: 当前生效版本号
        :type Version: str
        :param _VersionId: 当前生效版本ID
        :type VersionId: str
        :param _VersionStatus:     Skill 版本发布流程状态：
      - 0 INITIALIZED      初始化（版本初始态）
      - 1 AUDITING         审核中（f_analysis_status ∈ {PENDING, RUNNING}）
      - 2 PENDING_RELEASE  待发布（低/中风险，等用户确认上架）
      - 3 RELEASED         已发布
      - 4 UNRELEASED       未发布（HIGH / UNAVAILABLE / FAILED / 用户放弃，含历史"不通过"语义）
    与 SkillAnalysisStatus 解耦：前者是用户视角发布生命周期，后者是安全检测阶段。
        :type VersionStatus: int
        :param _SkillMd5: Skill包的md5信息
        :type SkillMd5: str
        :param _SkillUrl: 版本包地址
        :type SkillUrl: str
        :param _CreateTime: 版本创建时间（Unix秒）
        :type CreateTime: str
        :param _SkillMarkdownUrl: skill md文档
        :type SkillMarkdownUrl: str
        :param _UpdateDesc: 版本变更说明
        :type UpdateDesc: str
        """
        self._AnalysisInfo = None
        self._Version = None
        self._VersionId = None
        self._VersionStatus = None
        self._SkillMd5 = None
        self._SkillUrl = None
        self._CreateTime = None
        self._SkillMarkdownUrl = None
        self._UpdateDesc = None

    @property
    def AnalysisInfo(self):
        r"""检测信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.SkillAnalysisInfo`
        """
        return self._AnalysisInfo

    @AnalysisInfo.setter
    def AnalysisInfo(self, AnalysisInfo):
        self._AnalysisInfo = AnalysisInfo

    @property
    def Version(self):
        r"""当前生效版本号
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def VersionId(self):
        r"""当前生效版本ID
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def VersionStatus(self):
        r"""    Skill 版本发布流程状态：
      - 0 INITIALIZED      初始化（版本初始态）
      - 1 AUDITING         审核中（f_analysis_status ∈ {PENDING, RUNNING}）
      - 2 PENDING_RELEASE  待发布（低/中风险，等用户确认上架）
      - 3 RELEASED         已发布
      - 4 UNRELEASED       未发布（HIGH / UNAVAILABLE / FAILED / 用户放弃，含历史"不通过"语义）
    与 SkillAnalysisStatus 解耦：前者是用户视角发布生命周期，后者是安全检测阶段。
        :rtype: int
        """
        return self._VersionStatus

    @VersionStatus.setter
    def VersionStatus(self, VersionStatus):
        self._VersionStatus = VersionStatus

    @property
    def SkillMd5(self):
        r"""Skill包的md5信息
        :rtype: str
        """
        return self._SkillMd5

    @SkillMd5.setter
    def SkillMd5(self, SkillMd5):
        self._SkillMd5 = SkillMd5

    @property
    def SkillUrl(self):
        r"""版本包地址
        :rtype: str
        """
        return self._SkillUrl

    @SkillUrl.setter
    def SkillUrl(self, SkillUrl):
        self._SkillUrl = SkillUrl

    @property
    def CreateTime(self):
        r"""版本创建时间（Unix秒）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SkillMarkdownUrl(self):
        r"""skill md文档
        :rtype: str
        """
        return self._SkillMarkdownUrl

    @SkillMarkdownUrl.setter
    def SkillMarkdownUrl(self, SkillMarkdownUrl):
        self._SkillMarkdownUrl = SkillMarkdownUrl

    @property
    def UpdateDesc(self):
        r"""版本变更说明
        :rtype: str
        """
        return self._UpdateDesc

    @UpdateDesc.setter
    def UpdateDesc(self, UpdateDesc):
        self._UpdateDesc = UpdateDesc


    def _deserialize(self, params):
        if params.get("AnalysisInfo") is not None:
            self._AnalysisInfo = SkillAnalysisInfo()
            self._AnalysisInfo._deserialize(params.get("AnalysisInfo"))
        self._Version = params.get("Version")
        self._VersionId = params.get("VersionId")
        self._VersionStatus = params.get("VersionStatus")
        self._SkillMd5 = params.get("SkillMd5")
        self._SkillUrl = params.get("SkillUrl")
        self._CreateTime = params.get("CreateTime")
        self._SkillMarkdownUrl = params.get("SkillMarkdownUrl")
        self._UpdateDesc = params.get("UpdateDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    r"""<p>排序条件</p>

    """

    def __init__(self):
        r"""
        :param _Name: <p>排序字段名，如 create_time</p>
        :type Name: str
        :param _Direction: <p>排序方向，1 升序，2 降序</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>SORT_ORDER_INVALID</td><td>0</td><td>无效</td></tr><tr><td>SORT_ORDER_ASC</td><td>1</td><td>升序</td></tr><tr><td>SORT_ORDER_DESC</td><td>2</td><td>降序</td></tr></tbody></table>
        :type Direction: int
        """
        self._Name = None
        self._Direction = None

    @property
    def Name(self):
        r"""<p>排序字段名，如 create_time</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Direction(self):
        r"""<p>排序方向，1 升序，2 降序</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>SORT_ORDER_INVALID</td><td>0</td><td>无效</td></tr><tr><td>SORT_ORDER_ASC</td><td>1</td><td>升序</td></tr><tr><td>SORT_ORDER_DESC</td><td>2</td><td>降序</td></tr></tbody></table>
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Space(AbstractModel):
    r"""空间信息

    """

    def __init__(self):
        r"""
        :param _SpaceId: 空间id
        :type SpaceId: str
        :param _Name: 空间名称
        :type Name: str
        :param _Description: 空间描述
        :type Description: str
        :param _PermissionIdList: 空间权限
        :type PermissionIdList: list of str
        """
        self._SpaceId = None
        self._Name = None
        self._Description = None
        self._PermissionIdList = None

    @property
    def SpaceId(self):
        r"""空间id
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Name(self):
        r"""空间名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""空间描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PermissionIdList(self):
        r"""空间权限
        :rtype: list of str
        """
        return self._PermissionIdList

    @PermissionIdList.setter
    def PermissionIdList(self, PermissionIdList):
        self._PermissionIdList = PermissionIdList


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._PermissionIdList = params.get("PermissionIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecialStatusInfo(AbstractModel):
    r"""特殊状态信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态 (0-不在特殊状态中, 1-在特殊状态中)。枚举值: 1:在特殊状态中
        :type Status: int
        """
        self._Status = None

    @property
    def Status(self):
        r"""状态 (0-不在特殊状态中, 1-在特殊状态中)。枚举值: 1:在特殊状态中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SupportedFileType(AbstractModel):
    r"""支持的文件类型

    """

    def __init__(self):
        r"""
        :param _Description: 文件类型描述(如"文本文档")
        :type Description: str
        :param _FileExt: 文件类型(如 txt、pdf、jpg, 建议用扩展名)
        :type FileExt: str
        :param _MaxSizeBytes: 文件大小限制(单位: 字节)
        :type MaxSizeBytes: str
        """
        self._Description = None
        self._FileExt = None
        self._MaxSizeBytes = None

    @property
    def Description(self):
        r"""文件类型描述(如"文本文档")
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def FileExt(self):
        r"""文件类型(如 txt、pdf、jpg, 建议用扩展名)
        :rtype: str
        """
        return self._FileExt

    @FileExt.setter
    def FileExt(self, FileExt):
        self._FileExt = FileExt

    @property
    def MaxSizeBytes(self):
        r"""文件大小限制(单位: 字节)
        :rtype: str
        """
        return self._MaxSizeBytes

    @MaxSizeBytes.setter
    def MaxSizeBytes(self, MaxSizeBytes):
        self._MaxSizeBytes = MaxSizeBytes


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._FileExt = params.get("FileExt")
        self._MaxSizeBytes = params.get("MaxSizeBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SystemVariable(AbstractModel):
    r"""系统变量

    """

    def __init__(self):
        r"""
        :param _Description: 变量描述
        :type Description: str
        :param _Name: 变量名称
        :type Name: str
        """
        self._Description = None
        self._Name = None

    @property
    def Description(self):
        r"""变量描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""变量名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ThinkModel(AbstractModel):
    r"""思考模型配置

    """

    def __init__(self):
        r"""
        :param _Model: 思考模型
注意：此字段可能返回 null，表示取不到有效值。
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        self._Model = None

    @property
    def Model(self):
        r"""思考模型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelDetailInfo`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelDetailInfo()
            self._Model._deserialize(params.get("Model"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimeRange(AbstractModel):
    r"""查询时间范围（Unix 秒）

    """

    def __init__(self):
        r"""
        :param _EndTime: <p>结束时间，Unix 秒</p>
        :type EndTime: str
        :param _StartTime: <p>开始时间，Unix 秒</p>
        :type StartTime: str
        """
        self._EndTime = None
        self._StartTime = None

    @property
    def EndTime(self):
        r"""<p>结束时间，Unix 秒</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def StartTime(self):
        r"""<p>开始时间，Unix 秒</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime


    def _deserialize(self, params):
        self._EndTime = params.get("EndTime")
        self._StartTime = params.get("StartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerPushConfig(AbstractModel):
    r"""TimerPushConfig

    """

    def __init__(self):
        r"""
        :param _PushChannel: <p>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 |  |<br>| 1 | 不推送 |<br>| 2 | 微信公众号 |<br>| 3 | 企业微信 AI 机器人 |</p>
        :type PushChannel: int
        :param _PushTargetId: <p>推送会话ID</p>
        :type PushTargetId: str
        :param _PushTargetType: <p>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 |  |<br>| 1 | 用户 (微信公众号 openid) |<br>| 2 | 群聊 (企微机器人 chat_id) |</p>
        :type PushTargetType: int
        :param _PushWebhookUrl: <p>推送webhook的url</p>
        :type PushWebhookUrl: str
        """
        self._PushChannel = None
        self._PushTargetId = None
        self._PushTargetType = None
        self._PushWebhookUrl = None

    @property
    def PushChannel(self):
        r"""<p>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 |  |<br>| 1 | 不推送 |<br>| 2 | 微信公众号 |<br>| 3 | 企业微信 AI 机器人 |</p>
        :rtype: int
        """
        return self._PushChannel

    @PushChannel.setter
    def PushChannel(self, PushChannel):
        self._PushChannel = PushChannel

    @property
    def PushTargetId(self):
        r"""<p>推送会话ID</p>
        :rtype: str
        """
        return self._PushTargetId

    @PushTargetId.setter
    def PushTargetId(self, PushTargetId):
        self._PushTargetId = PushTargetId

    @property
    def PushTargetType(self):
        r"""<p>枚举值:<br>| uint | 描述 |<br>| --- | --- |<br>| 0 |  |<br>| 1 | 用户 (微信公众号 openid) |<br>| 2 | 群聊 (企微机器人 chat_id) |</p>
        :rtype: int
        """
        return self._PushTargetType

    @PushTargetType.setter
    def PushTargetType(self, PushTargetType):
        self._PushTargetType = PushTargetType

    @property
    def PushWebhookUrl(self):
        r"""<p>推送webhook的url</p>
        :rtype: str
        """
        return self._PushWebhookUrl

    @PushWebhookUrl.setter
    def PushWebhookUrl(self, PushWebhookUrl):
        self._PushWebhookUrl = PushWebhookUrl


    def _deserialize(self, params):
        self._PushChannel = params.get("PushChannel")
        self._PushTargetId = params.get("PushTargetId")
        self._PushTargetType = params.get("PushTargetType")
        self._PushWebhookUrl = params.get("PushWebhookUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TimerScheduleConfig(AbstractModel):
    r"""TimerScheduleConfig

    """

    def __init__(self):
        r"""
        :param _Cron: cron配置
        :type Cron: :class:`tencentcloud.adp.v20260520.models.CronSchedule`
        :param _Daily: 每日触发
        :type Daily: :class:`tencentcloud.adp.v20260520.models.DailySchedule`
        :param _Interval: 固定间隔
        :type Interval: :class:`tencentcloud.adp.v20260520.models.IntervalSchedule`
        :param _ManualOnly: 仅手动
        :type ManualOnly: :class:`tencentcloud.adp.v20260520.models.ManualOnlySchedule`
        :param _Once: 单次
        :type Once: :class:`tencentcloud.adp.v20260520.models.OnceSchedule`
        :param _ScheduleType: 
枚举值:
| uint | 描述 |
| --- | --- |
| 0 |  |
| 1 | 仅手动 |
| 2 | 每天 |
| 3 | 每周 |
| 4 | 按间隔 |
| 5 | 一次性 |
| 6 | Cron |
        :type ScheduleType: int
        :param _Timezone: 时区
        :type Timezone: str
        :param _Weekly: 每周固定时间触发
        :type Weekly: :class:`tencentcloud.adp.v20260520.models.WeeklySchedule`
        """
        self._Cron = None
        self._Daily = None
        self._Interval = None
        self._ManualOnly = None
        self._Once = None
        self._ScheduleType = None
        self._Timezone = None
        self._Weekly = None

    @property
    def Cron(self):
        r"""cron配置
        :rtype: :class:`tencentcloud.adp.v20260520.models.CronSchedule`
        """
        return self._Cron

    @Cron.setter
    def Cron(self, Cron):
        self._Cron = Cron

    @property
    def Daily(self):
        r"""每日触发
        :rtype: :class:`tencentcloud.adp.v20260520.models.DailySchedule`
        """
        return self._Daily

    @Daily.setter
    def Daily(self, Daily):
        self._Daily = Daily

    @property
    def Interval(self):
        r"""固定间隔
        :rtype: :class:`tencentcloud.adp.v20260520.models.IntervalSchedule`
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def ManualOnly(self):
        r"""仅手动
        :rtype: :class:`tencentcloud.adp.v20260520.models.ManualOnlySchedule`
        """
        return self._ManualOnly

    @ManualOnly.setter
    def ManualOnly(self, ManualOnly):
        self._ManualOnly = ManualOnly

    @property
    def Once(self):
        r"""单次
        :rtype: :class:`tencentcloud.adp.v20260520.models.OnceSchedule`
        """
        return self._Once

    @Once.setter
    def Once(self, Once):
        self._Once = Once

    @property
    def ScheduleType(self):
        r"""
枚举值:
| uint | 描述 |
| --- | --- |
| 0 |  |
| 1 | 仅手动 |
| 2 | 每天 |
| 3 | 每周 |
| 4 | 按间隔 |
| 5 | 一次性 |
| 6 | Cron |
        :rtype: int
        """
        return self._ScheduleType

    @ScheduleType.setter
    def ScheduleType(self, ScheduleType):
        self._ScheduleType = ScheduleType

    @property
    def Timezone(self):
        r"""时区
        :rtype: str
        """
        return self._Timezone

    @Timezone.setter
    def Timezone(self, Timezone):
        self._Timezone = Timezone

    @property
    def Weekly(self):
        r"""每周固定时间触发
        :rtype: :class:`tencentcloud.adp.v20260520.models.WeeklySchedule`
        """
        return self._Weekly

    @Weekly.setter
    def Weekly(self, Weekly):
        self._Weekly = Weekly


    def _deserialize(self, params):
        if params.get("Cron") is not None:
            self._Cron = CronSchedule()
            self._Cron._deserialize(params.get("Cron"))
        if params.get("Daily") is not None:
            self._Daily = DailySchedule()
            self._Daily._deserialize(params.get("Daily"))
        if params.get("Interval") is not None:
            self._Interval = IntervalSchedule()
            self._Interval._deserialize(params.get("Interval"))
        if params.get("ManualOnly") is not None:
            self._ManualOnly = ManualOnlySchedule()
            self._ManualOnly._deserialize(params.get("ManualOnly"))
        if params.get("Once") is not None:
            self._Once = OnceSchedule()
            self._Once._deserialize(params.get("Once"))
        self._ScheduleType = params.get("ScheduleType")
        self._Timezone = params.get("Timezone")
        if params.get("Weekly") is not None:
            self._Weekly = WeeklySchedule()
            self._Weekly._deserialize(params.get("Weekly"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tool(AbstractModel):
    r"""Tool

    """

    def __init__(self):
        r"""
        :param _Billing: <p>工具计费信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Billing: :class:`tencentcloud.adp.v20260520.models.ToolBilling`
        :param _CallCount: <p>工具调用次数</p><p>单位：次数</p>
        :type CallCount: int
        :param _Description: <p>工具描述信息</p>
        :type Description: str
        :param _Name: <p>工具名称</p>
        :type Name: str
        :param _PluginId: <p>插件ID</p>
        :type PluginId: str
        :param _ToolAccessMode: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TOOL_ACCESS_MODE_UNKNOWN</td><td>0</td><td>未指定</td></tr><tr><td>TOOL_ACCESS_MODE_READ_ONLY</td><td>1</td><td>只读</td></tr><tr><td>TOOL_ACCESS_MODE_WRITE_DELETE</td><td>2</td><td>写/删除</td></tr></tbody></table>
        :type ToolAccessMode: int
        :param _ToolConfig: <p>工具配置信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolConfig: :class:`tencentcloud.adp.v20260520.models.ToolConfig`
        :param _ToolId: <p>工具ID</p>
        :type ToolId: str
        """
        self._Billing = None
        self._CallCount = None
        self._Description = None
        self._Name = None
        self._PluginId = None
        self._ToolAccessMode = None
        self._ToolConfig = None
        self._ToolId = None

    @property
    def Billing(self):
        r"""<p>工具计费信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ToolBilling`
        """
        return self._Billing

    @Billing.setter
    def Billing(self, Billing):
        self._Billing = Billing

    @property
    def CallCount(self):
        r"""<p>工具调用次数</p><p>单位：次数</p>
        :rtype: int
        """
        return self._CallCount

    @CallCount.setter
    def CallCount(self, CallCount):
        self._CallCount = CallCount

    @property
    def Description(self):
        r"""<p>工具描述信息</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        r"""<p>工具名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PluginId(self):
        r"""<p>插件ID</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ToolAccessMode(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>TOOL_ACCESS_MODE_UNKNOWN</td><td>0</td><td>未指定</td></tr><tr><td>TOOL_ACCESS_MODE_READ_ONLY</td><td>1</td><td>只读</td></tr><tr><td>TOOL_ACCESS_MODE_WRITE_DELETE</td><td>2</td><td>写/删除</td></tr></tbody></table>
        :rtype: int
        """
        return self._ToolAccessMode

    @ToolAccessMode.setter
    def ToolAccessMode(self, ToolAccessMode):
        self._ToolAccessMode = ToolAccessMode

    @property
    def ToolConfig(self):
        r"""<p>工具配置信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ToolConfig`
        """
        return self._ToolConfig

    @ToolConfig.setter
    def ToolConfig(self, ToolConfig):
        self._ToolConfig = ToolConfig

    @property
    def ToolId(self):
        r"""<p>工具ID</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId


    def _deserialize(self, params):
        if params.get("Billing") is not None:
            self._Billing = ToolBilling()
            self._Billing._deserialize(params.get("Billing"))
        self._CallCount = params.get("CallCount")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        self._PluginId = params.get("PluginId")
        self._ToolAccessMode = params.get("ToolAccessMode")
        if params.get("ToolConfig") is not None:
            self._ToolConfig = ToolConfig()
            self._ToolConfig._deserialize(params.get("ToolConfig"))
        self._ToolId = params.get("ToolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolBilling(AbstractModel):
    r"""ToolBilling

    """

    def __init__(self):
        r"""
        :param _BasicBilling: <p>基础计费信息</p>
        :type BasicBilling: :class:`tencentcloud.adp.v20260520.models.BasicBilling`
        :param _BillingType: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>BILLING_TYPE_FREE</td><td>0</td><td>免费</td></tr><tr><td>BILLING_TYPE_LIMITED_FREE</td><td>1</td><td>限时免费</td></tr><tr><td>BILLING_TYPE_OFFICIAL_PAID</td><td>2</td><td>官方收费</td></tr><tr><td>BILLING_TYPE_OFFICIAL_PAID_OLD_FREE</td><td>3</td><td>官方收费（新/升级用户收费，存量老用户限时免费）</td></tr></tbody></table>
        :type BillingType: int
        :param _ComplexBilling: <p>复合类型计费信息</p>
        :type ComplexBilling: :class:`tencentcloud.adp.v20260520.models.ComplexBilling`
        :param _DuplexBilling: <p>双向计费信息</p>
        :type DuplexBilling: :class:`tencentcloud.adp.v20260520.models.DuplexBilling`
        """
        self._BasicBilling = None
        self._BillingType = None
        self._ComplexBilling = None
        self._DuplexBilling = None

    @property
    def BasicBilling(self):
        r"""<p>基础计费信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.BasicBilling`
        """
        return self._BasicBilling

    @BasicBilling.setter
    def BasicBilling(self, BasicBilling):
        self._BasicBilling = BasicBilling

    @property
    def BillingType(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>BILLING_TYPE_FREE</td><td>0</td><td>免费</td></tr><tr><td>BILLING_TYPE_LIMITED_FREE</td><td>1</td><td>限时免费</td></tr><tr><td>BILLING_TYPE_OFFICIAL_PAID</td><td>2</td><td>官方收费</td></tr><tr><td>BILLING_TYPE_OFFICIAL_PAID_OLD_FREE</td><td>3</td><td>官方收费（新/升级用户收费，存量老用户限时免费）</td></tr></tbody></table>
        :rtype: int
        """
        return self._BillingType

    @BillingType.setter
    def BillingType(self, BillingType):
        self._BillingType = BillingType

    @property
    def ComplexBilling(self):
        r"""<p>复合类型计费信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ComplexBilling`
        """
        return self._ComplexBilling

    @ComplexBilling.setter
    def ComplexBilling(self, ComplexBilling):
        self._ComplexBilling = ComplexBilling

    @property
    def DuplexBilling(self):
        r"""<p>双向计费信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.DuplexBilling`
        """
        return self._DuplexBilling

    @DuplexBilling.setter
    def DuplexBilling(self, DuplexBilling):
        self._DuplexBilling = DuplexBilling


    def _deserialize(self, params):
        if params.get("BasicBilling") is not None:
            self._BasicBilling = BasicBilling()
            self._BasicBilling._deserialize(params.get("BasicBilling"))
        self._BillingType = params.get("BillingType")
        if params.get("ComplexBilling") is not None:
            self._ComplexBilling = ComplexBilling()
            self._ComplexBilling._deserialize(params.get("ComplexBilling"))
        if params.get("DuplexBilling") is not None:
            self._DuplexBilling = DuplexBilling()
            self._DuplexBilling._deserialize(params.get("DuplexBilling"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolConfig(AbstractModel):
    r"""ToolConfig

    """

    def __init__(self):
        r"""
        :param _ApiToolConfig: <p>API工具配置信息</p>
        :type ApiToolConfig: :class:`tencentcloud.adp.v20260520.models.ApiToolConfig`
        :param _AppToolConfig: <p>应用配置信息</p>
        :type AppToolConfig: :class:`tencentcloud.adp.v20260520.models.AppToolConfig`
        :param _CodeToolConfig: <p>代码工具配置信息</p>
        :type CodeToolConfig: :class:`tencentcloud.adp.v20260520.models.CodeToolConfig`
        :param _MCPToolConfig: <p>MCP工具配置信息</p>
        :type MCPToolConfig: :class:`tencentcloud.adp.v20260520.models.MCPToolConfig`
        """
        self._ApiToolConfig = None
        self._AppToolConfig = None
        self._CodeToolConfig = None
        self._MCPToolConfig = None

    @property
    def ApiToolConfig(self):
        r"""<p>API工具配置信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ApiToolConfig`
        """
        return self._ApiToolConfig

    @ApiToolConfig.setter
    def ApiToolConfig(self, ApiToolConfig):
        self._ApiToolConfig = ApiToolConfig

    @property
    def AppToolConfig(self):
        r"""<p>应用配置信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppToolConfig`
        """
        return self._AppToolConfig

    @AppToolConfig.setter
    def AppToolConfig(self, AppToolConfig):
        self._AppToolConfig = AppToolConfig

    @property
    def CodeToolConfig(self):
        r"""<p>代码工具配置信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.CodeToolConfig`
        """
        return self._CodeToolConfig

    @CodeToolConfig.setter
    def CodeToolConfig(self, CodeToolConfig):
        self._CodeToolConfig = CodeToolConfig

    @property
    def MCPToolConfig(self):
        r"""<p>MCP工具配置信息</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.MCPToolConfig`
        """
        return self._MCPToolConfig

    @MCPToolConfig.setter
    def MCPToolConfig(self, MCPToolConfig):
        self._MCPToolConfig = MCPToolConfig


    def _deserialize(self, params):
        if params.get("ApiToolConfig") is not None:
            self._ApiToolConfig = ApiToolConfig()
            self._ApiToolConfig._deserialize(params.get("ApiToolConfig"))
        if params.get("AppToolConfig") is not None:
            self._AppToolConfig = AppToolConfig()
            self._AppToolConfig._deserialize(params.get("AppToolConfig"))
        if params.get("CodeToolConfig") is not None:
            self._CodeToolConfig = CodeToolConfig()
            self._CodeToolConfig._deserialize(params.get("CodeToolConfig"))
        if params.get("MCPToolConfig") is not None:
            self._MCPToolConfig = MCPToolConfig()
            self._MCPToolConfig._deserialize(params.get("MCPToolConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolExample(AbstractModel):
    r"""ToolExample

    """

    def __init__(self):
        r"""
        :param _Request: <p>请求参数</p>
        :type Request: str
        :param _Response: <p>响应参数</p>
        :type Response: str
        """
        self._Request = None
        self._Response = None

    @property
    def Request(self):
        r"""<p>请求参数</p>
        :rtype: str
        """
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def Response(self):
        r"""<p>响应参数</p>
        :rtype: str
        """
        return self._Response

    @Response.setter
    def Response(self, Response):
        self._Response = Response


    def _deserialize(self, params):
        self._Request = params.get("Request")
        self._Response = params.get("Response")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolSummary(AbstractModel):
    r"""工具信息

    """

    def __init__(self):
        r"""
        :param _ToolId: <p>工具Id</p>
        :type ToolId: str
        """
        self._ToolId = None

    @property
    def ToolId(self):
        r"""<p>工具Id</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerConfig(AbstractModel):
    r"""TriggerConfig

    """

    def __init__(self):
        r"""
        :param _ScheduledConfig: <p>定时器配置</p>
        :type ScheduledConfig: :class:`tencentcloud.adp.v20260520.models.AppTriggerScheduleConfig`
        :param _WebhookConfig: <p>Webhook配置</p>
        :type WebhookConfig: :class:`tencentcloud.adp.v20260520.models.AppTriggerWebhookConfig`
        """
        self._ScheduledConfig = None
        self._WebhookConfig = None

    @property
    def ScheduledConfig(self):
        r"""<p>定时器配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerScheduleConfig`
        """
        return self._ScheduledConfig

    @ScheduledConfig.setter
    def ScheduledConfig(self, ScheduledConfig):
        self._ScheduledConfig = ScheduledConfig

    @property
    def WebhookConfig(self):
        r"""<p>Webhook配置</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerWebhookConfig`
        """
        return self._WebhookConfig

    @WebhookConfig.setter
    def WebhookConfig(self, WebhookConfig):
        self._WebhookConfig = WebhookConfig


    def _deserialize(self, params):
        if params.get("ScheduledConfig") is not None:
            self._ScheduledConfig = AppTriggerScheduleConfig()
            self._ScheduledConfig._deserialize(params.get("ScheduledConfig"))
        if params.get("WebhookConfig") is not None:
            self._WebhookConfig = AppTriggerWebhookConfig()
            self._WebhookConfig._deserialize(params.get("WebhookConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TriggerStatus(AbstractModel):
    r"""TriggerStatus

    """

    def __init__(self):
        r"""
        :param _ScheduledStatus: <p>定时器状态</p>
        :type ScheduledStatus: :class:`tencentcloud.adp.v20260520.models.AppTriggerScheduleStatus`
        :param _Scope: <table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :type Scope: int
        :param _UserId: <p>访客id</p>
        :type UserId: str
        :param _WebhookStatus: <p>Webhook状态</p>
        :type WebhookStatus: :class:`tencentcloud.adp.v20260520.models.AppTriggerWebhookStatus`
        """
        self._ScheduledStatus = None
        self._Scope = None
        self._UserId = None
        self._WebhookStatus = None

    @property
    def ScheduledStatus(self):
        r"""<p>定时器状态</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerScheduleStatus`
        """
        return self._ScheduledStatus

    @ScheduledStatus.setter
    def ScheduledStatus(self, ScheduledStatus):
        self._ScheduledStatus = ScheduledStatus

    @property
    def Scope(self):
        r"""<table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>APP_TRIGGER_SCOPE_UNSPECIFIED</td><td>0</td><td>未指定</td></tr><tr><td>APP_TRIGGER_SCOPE_APP</td><td>1</td><td>B 端管理员</td></tr><tr><td>APP_TRIGGER_SCOPE_USER</td><td>2</td><td>C 端访客</td></tr></tbody></table>
        :rtype: int
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def UserId(self):
        r"""<p>访客id</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def WebhookStatus(self):
        r"""<p>Webhook状态</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppTriggerWebhookStatus`
        """
        return self._WebhookStatus

    @WebhookStatus.setter
    def WebhookStatus(self, WebhookStatus):
        self._WebhookStatus = WebhookStatus


    def _deserialize(self, params):
        if params.get("ScheduledStatus") is not None:
            self._ScheduledStatus = AppTriggerScheduleStatus()
            self._ScheduledStatus._deserialize(params.get("ScheduledStatus"))
        self._Scope = params.get("Scope")
        self._UserId = params.get("UserId")
        if params.get("WebhookStatus") is not None:
            self._WebhookStatus = AppTriggerWebhookStatus()
            self._WebhookStatus._deserialize(params.get("WebhookStatus"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnfavoritePluginRequest(AbstractModel):
    r"""UnfavoritePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: <p>插件id</p>
        :type PluginId: str
        :param _SpaceId: <p>当前空间id</p>
        :type SpaceId: str
        """
        self._PluginId = None
        self._SpaceId = None

    @property
    def PluginId(self):
        r"""<p>插件id</p>
        :rtype: str
        """
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def SpaceId(self):
        r"""<p>当前空间id</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnfavoritePluginResponse(AbstractModel):
    r"""UnfavoritePlugin返回参数结构体

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


class UnfavoriteSkillRequest(AbstractModel):
    r"""UnfavoriteSkill请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SkillId: <p>SkillId</p>
        :type SkillId: str
        :param _SpaceId: <p>空间ID</p>
        :type SpaceId: str
        """
        self._SkillId = None
        self._SpaceId = None

    @property
    def SkillId(self):
        r"""<p>SkillId</p>
        :rtype: str
        """
        return self._SkillId

    @SkillId.setter
    def SkillId(self, SkillId):
        self._SkillId = SkillId

    @property
    def SpaceId(self):
        r"""<p>空间ID</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SkillId = params.get("SkillId")
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnfavoriteSkillResponse(AbstractModel):
    r"""UnfavoriteSkill返回参数结构体

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


class UsageDetail(AbstractModel):
    r"""资源调用时序明细

    """

    def __init__(self):
        r"""
        :param _CallSource: <p>调用来源</p>
        :type CallSource: :class:`tencentcloud.adp.v20260520.models.CallSource`
        :param _DosageId: <p>计量 ID，用于对账/回溯</p>
        :type DosageId: str
        :param _EventTime: <p>调用时间戳（Unix 秒）</p>
        :type EventTime: str
        :param _Model: <p>MODEL 域专属</p>
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelUsageDetail`
        :param _Plugin: <p>PLUGIN 域专属</p>
        :type Plugin: :class:`tencentcloud.adp.v20260520.models.PluginUsageDetail`
        :param _TraceId: <p>调用链路追踪 ID</p>
        :type TraceId: str
        :param _UserId: <p>用户 ID</p>
        :type UserId: str
        """
        self._CallSource = None
        self._DosageId = None
        self._EventTime = None
        self._Model = None
        self._Plugin = None
        self._TraceId = None
        self._UserId = None

    @property
    def CallSource(self):
        r"""<p>调用来源</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.CallSource`
        """
        return self._CallSource

    @CallSource.setter
    def CallSource(self, CallSource):
        self._CallSource = CallSource

    @property
    def DosageId(self):
        r"""<p>计量 ID，用于对账/回溯</p>
        :rtype: str
        """
        return self._DosageId

    @DosageId.setter
    def DosageId(self, DosageId):
        self._DosageId = DosageId

    @property
    def EventTime(self):
        r"""<p>调用时间戳（Unix 秒）</p>
        :rtype: str
        """
        return self._EventTime

    @EventTime.setter
    def EventTime(self, EventTime):
        self._EventTime = EventTime

    @property
    def Model(self):
        r"""<p>MODEL 域专属</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelUsageDetail`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Plugin(self):
        r"""<p>PLUGIN 域专属</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginUsageDetail`
        """
        return self._Plugin

    @Plugin.setter
    def Plugin(self, Plugin):
        self._Plugin = Plugin

    @property
    def TraceId(self):
        r"""<p>调用链路追踪 ID</p>
        :rtype: str
        """
        return self._TraceId

    @TraceId.setter
    def TraceId(self, TraceId):
        self._TraceId = TraceId

    @property
    def UserId(self):
        r"""<p>用户 ID</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        if params.get("CallSource") is not None:
            self._CallSource = CallSource()
            self._CallSource._deserialize(params.get("CallSource"))
        self._DosageId = params.get("DosageId")
        self._EventTime = params.get("EventTime")
        if params.get("Model") is not None:
            self._Model = ModelUsageDetail()
            self._Model._deserialize(params.get("Model"))
        if params.get("Plugin") is not None:
            self._Plugin = PluginUsageDetail()
            self._Plugin._deserialize(params.get("Plugin"))
        self._TraceId = params.get("TraceId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageSummary(AbstractModel):
    r"""资源用量聚合明细

    """

    def __init__(self):
        r"""
        :param _Model: <p>MODEL 域专属</p>
        :type Model: :class:`tencentcloud.adp.v20260520.models.ModelUsageSummary`
        :param _Platform: <p>PLATFORM 域专属</p>
        :type Platform: :class:`tencentcloud.adp.v20260520.models.PlatformUsageSummary`
        :param _Plugin: <p>PLUGIN 域专属</p>
        :type Plugin: :class:`tencentcloud.adp.v20260520.models.PluginUsageSummary`
        :param _SourceId: <p>来源 ID；CORP 视图=space_id（企业视图按 space 分组），SPACE 视图=app_id（uint64 字符串），APP 视图=app_id</p>
        :type SourceId: str
        :param _SourceName: <p>来源名称；CORP 视图=space_name，SPACE 视图=app_name，APP 视图=app_name</p>
        :type SourceName: str
        :param _ViewType: <p>视图类型，决定 SourceId/SourceName 的业务含义</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>VIEW_TYPE_UNSPECIFIED</td><td>0</td><td>未指定（无效值，请求勿传）</td></tr><tr><td>VIEW_TYPE_CORP</td><td>1</td><td>企业视图</td></tr><tr><td>VIEW_TYPE_SPACE</td><td>2</td><td>空间视图</td></tr><tr><td>VIEW_TYPE_APP</td><td>3</td><td>应用视图</td></tr></tbody></table>
        :type ViewType: int
        """
        self._Model = None
        self._Platform = None
        self._Plugin = None
        self._SourceId = None
        self._SourceName = None
        self._ViewType = None

    @property
    def Model(self):
        r"""<p>MODEL 域专属</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.ModelUsageSummary`
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Platform(self):
        r"""<p>PLATFORM 域专属</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PlatformUsageSummary`
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Plugin(self):
        r"""<p>PLUGIN 域专属</p>
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginUsageSummary`
        """
        return self._Plugin

    @Plugin.setter
    def Plugin(self, Plugin):
        self._Plugin = Plugin

    @property
    def SourceId(self):
        r"""<p>来源 ID；CORP 视图=space_id（企业视图按 space 分组），SPACE 视图=app_id（uint64 字符串），APP 视图=app_id</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceName(self):
        r"""<p>来源名称；CORP 视图=space_name，SPACE 视图=app_name，APP 视图=app_name</p>
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def ViewType(self):
        r"""<p>视图类型，决定 SourceId/SourceName 的业务含义</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>VIEW_TYPE_UNSPECIFIED</td><td>0</td><td>未指定（无效值，请求勿传）</td></tr><tr><td>VIEW_TYPE_CORP</td><td>1</td><td>企业视图</td></tr><tr><td>VIEW_TYPE_SPACE</td><td>2</td><td>空间视图</td></tr><tr><td>VIEW_TYPE_APP</td><td>3</td><td>应用视图</td></tr></tbody></table>
        :rtype: int
        """
        return self._ViewType

    @ViewType.setter
    def ViewType(self, ViewType):
        self._ViewType = ViewType


    def _deserialize(self, params):
        if params.get("Model") is not None:
            self._Model = ModelUsageSummary()
            self._Model._deserialize(params.get("Model"))
        if params.get("Platform") is not None:
            self._Platform = PlatformUsageSummary()
            self._Platform._deserialize(params.get("Platform"))
        if params.get("Plugin") is not None:
            self._Plugin = PluginUsageSummary()
            self._Plugin._deserialize(params.get("Plugin"))
        self._SourceId = params.get("SourceId")
        self._SourceName = params.get("SourceName")
        self._ViewType = params.get("ViewType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Variable(AbstractModel):
    r"""变量信息

    """

    def __init__(self):
        r"""
        :param _DefaultFileName: <p>默认文件名称</p>
        :type DefaultFileName: str
        :param _DefaultValue: <p>默认值</p>
        :type DefaultValue: str
        :param _Description: <p>变量描述</p>
        :type Description: str
        :param _ModuleType: <p>模块类型。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数</p>
        :type ModuleType: int
        :param _Name: <p>变量名称</p>
        :type Name: str
        :param _Type: <p>变量类型</p><p>枚举值：</p><ul><li>0： 字符串</li><li>1： 整数</li><li>2： 浮点数</li><li>3： 布尔值</li><li>4： 对象</li><li>5： 字符串数组</li><li>6： 整数数组</li><li>7： 浮点数数组</li><li>8： 布尔值数组</li><li>9： 对象数组</li><li>10： 文件</li><li>11： 文档</li><li>12： 图片</li><li>13： 音频</li><li>14： 视频</li><li>15： 文件数组</li><li>16： 文档数组</li><li>17： 图片数组</li><li>18： 音频数组</li><li>19： 视频数组</li><li>20： 数组的数组</li><li>21： 密钥</li></ul>
        :type Type: int
        :param _VariableId: <p>变量ID</p>
        :type VariableId: str
        :param _EnableEndpoints: <p>是否启用网络策略(仅环境变量生效)</p>
        :type EnableEndpoints: bool
        :param _EndpointList: <p>网络策略列表(支持: 精确域名、*.通配子域名、可带协议/端口/路径前缀)</p>
        :type EndpointList: list of str
        """
        self._DefaultFileName = None
        self._DefaultValue = None
        self._Description = None
        self._ModuleType = None
        self._Name = None
        self._Type = None
        self._VariableId = None
        self._EnableEndpoints = None
        self._EndpointList = None

    @property
    def DefaultFileName(self):
        r"""<p>默认文件名称</p>
        :rtype: str
        """
        return self._DefaultFileName

    @DefaultFileName.setter
    def DefaultFileName(self, DefaultFileName):
        self._DefaultFileName = DefaultFileName

    @property
    def DefaultValue(self):
        r"""<p>默认值</p>
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Description(self):
        r"""<p>变量描述</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ModuleType(self):
        r"""<p>模块类型。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数</p>
        :rtype: int
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType

    @property
    def Name(self):
        r"""<p>变量名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""<p>变量类型</p><p>枚举值：</p><ul><li>0： 字符串</li><li>1： 整数</li><li>2： 浮点数</li><li>3： 布尔值</li><li>4： 对象</li><li>5： 字符串数组</li><li>6： 整数数组</li><li>7： 浮点数数组</li><li>8： 布尔值数组</li><li>9： 对象数组</li><li>10： 文件</li><li>11： 文档</li><li>12： 图片</li><li>13： 音频</li><li>14： 视频</li><li>15： 文件数组</li><li>16： 文档数组</li><li>17： 图片数组</li><li>18： 音频数组</li><li>19： 视频数组</li><li>20： 数组的数组</li><li>21： 密钥</li></ul>
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VariableId(self):
        r"""<p>变量ID</p>
        :rtype: str
        """
        return self._VariableId

    @VariableId.setter
    def VariableId(self, VariableId):
        self._VariableId = VariableId

    @property
    def EnableEndpoints(self):
        r"""<p>是否启用网络策略(仅环境变量生效)</p>
        :rtype: bool
        """
        return self._EnableEndpoints

    @EnableEndpoints.setter
    def EnableEndpoints(self, EnableEndpoints):
        self._EnableEndpoints = EnableEndpoints

    @property
    def EndpointList(self):
        r"""<p>网络策略列表(支持: 精确域名、*.通配子域名、可带协议/端口/路径前缀)</p>
        :rtype: list of str
        """
        return self._EndpointList

    @EndpointList.setter
    def EndpointList(self, EndpointList):
        self._EndpointList = EndpointList


    def _deserialize(self, params):
        self._DefaultFileName = params.get("DefaultFileName")
        self._DefaultValue = params.get("DefaultValue")
        self._Description = params.get("Description")
        self._ModuleType = params.get("ModuleType")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._VariableId = params.get("VariableId")
        self._EnableEndpoints = params.get("EnableEndpoints")
        self._EndpointList = params.get("EndpointList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViewScope(AbstractModel):
    r"""视图范围

    """

    def __init__(self):
        r"""
        :param _ViewType: <p>视图类型；枚举值：VIEW_TYPE_CORP(1) 企业视图、VIEW_TYPE_SPACE(2) 空间视图、VIEW_TYPE_APP(3) 应用视图</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>VIEW_TYPE_UNSPECIFIED</td><td>0</td><td>未指定（无效值，请求勿传）</td></tr><tr><td>VIEW_TYPE_CORP</td><td>1</td><td>企业视图</td></tr><tr><td>VIEW_TYPE_SPACE</td><td>2</td><td>空间视图</td></tr><tr><td>VIEW_TYPE_APP</td><td>3</td><td>应用视图</td></tr></tbody></table>
        :type ViewType: int
        :param _ScopeId: <p>视图范围 ID；VIEW_TYPE_CORP 留空；VIEW_TYPE_SPACE 填 space_id；VIEW_TYPE_APP 填 app_id（uint64 雪花 ID 的十进制字符串）</p>
        :type ScopeId: str
        """
        self._ViewType = None
        self._ScopeId = None

    @property
    def ViewType(self):
        r"""<p>视图类型；枚举值：VIEW_TYPE_CORP(1) 企业视图、VIEW_TYPE_SPACE(2) 空间视图、VIEW_TYPE_APP(3) 应用视图</p><table><tbody><tr><td>枚举项</td><td>枚举值</td><td>描述</td></tr><tr><td>VIEW_TYPE_UNSPECIFIED</td><td>0</td><td>未指定（无效值，请求勿传）</td></tr><tr><td>VIEW_TYPE_CORP</td><td>1</td><td>企业视图</td></tr><tr><td>VIEW_TYPE_SPACE</td><td>2</td><td>空间视图</td></tr><tr><td>VIEW_TYPE_APP</td><td>3</td><td>应用视图</td></tr></tbody></table>
        :rtype: int
        """
        return self._ViewType

    @ViewType.setter
    def ViewType(self, ViewType):
        self._ViewType = ViewType

    @property
    def ScopeId(self):
        r"""<p>视图范围 ID；VIEW_TYPE_CORP 留空；VIEW_TYPE_SPACE 填 space_id；VIEW_TYPE_APP 填 app_id（uint64 雪花 ID 的十进制字符串）</p>
        :rtype: str
        """
        return self._ScopeId

    @ScopeId.setter
    def ScopeId(self, ScopeId):
        self._ScopeId = ScopeId


    def _deserialize(self, params):
        self._ViewType = params.get("ViewType")
        self._ScopeId = params.get("ScopeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VoiceConfig(AbstractModel):
    r"""VoiceConfig

    """

    def __init__(self):
        r"""
        :param _TimbreKey: 数智人音色key,需要和公有云音色id对齐
        :type TimbreKey: str
        :param _VoiceName: 音色名称
        :type VoiceName: str
        :param _VoiceType: 公有云音色id
        :type VoiceType: int
        """
        self._TimbreKey = None
        self._VoiceName = None
        self._VoiceType = None

    @property
    def TimbreKey(self):
        r"""数智人音色key,需要和公有云音色id对齐
        :rtype: str
        """
        return self._TimbreKey

    @TimbreKey.setter
    def TimbreKey(self, TimbreKey):
        self._TimbreKey = TimbreKey

    @property
    def VoiceName(self):
        r"""音色名称
        :rtype: str
        """
        return self._VoiceName

    @VoiceName.setter
    def VoiceName(self, VoiceName):
        self._VoiceName = VoiceName

    @property
    def VoiceType(self):
        r"""公有云音色id
        :rtype: int
        """
        return self._VoiceType

    @VoiceType.setter
    def VoiceType(self, VoiceType):
        self._VoiceType = VoiceType


    def _deserialize(self, params):
        self._TimbreKey = params.get("TimbreKey")
        self._VoiceName = params.get("VoiceName")
        self._VoiceType = params.get("VoiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklySchedule(AbstractModel):
    r"""WeeklySchedule

    """

    def __init__(self):
        r"""
        :param _Times: 定时配置（星期）
        :type Times: list of WeeklyTime
        """
        self._Times = None

    @property
    def Times(self):
        r"""定时配置（星期）
        :rtype: list of WeeklyTime
        """
        return self._Times

    @Times.setter
    def Times(self, Times):
        self._Times = Times


    def _deserialize(self, params):
        if params.get("Times") is not None:
            self._Times = []
            for item in params.get("Times"):
                obj = WeeklyTime()
                obj._deserialize(item)
                self._Times.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WeeklyTime(AbstractModel):
    r"""WeeklyTime

    """

    def __init__(self):
        r"""
        :param _TimeOfDay: 时间
        :type TimeOfDay: str
        :param _Weekday: 周几
        :type Weekday: int
        """
        self._TimeOfDay = None
        self._Weekday = None

    @property
    def TimeOfDay(self):
        r"""时间
        :rtype: str
        """
        return self._TimeOfDay

    @TimeOfDay.setter
    def TimeOfDay(self, TimeOfDay):
        self._TimeOfDay = TimeOfDay

    @property
    def Weekday(self):
        r"""周几
        :rtype: int
        """
        return self._Weekday

    @Weekday.setter
    def Weekday(self, Weekday):
        self._Weekday = Weekday


    def _deserialize(self, params):
        self._TimeOfDay = params.get("TimeOfDay")
        self._Weekday = params.get("Weekday")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        