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
        """
        self._AgentId = None
        self._Profile = None
        self._Instructions = None
        self._Model = None
        self._ToolList = None
        self._PluginList = None
        self._SkillList = None
        self._AdvancedConfig = None

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
        :param _Config: 插件基本配置
        :type Config: :class:`tencentcloud.adp.v20260520.models.AgentPluginConfig`
        :param _Name: 插件名称
        :type Name: str
        :param _IconUrl: 插件图标url
        :type IconUrl: str
        :param _Description: 插件描述
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
        r"""插件基本配置
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentPluginConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

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
    def IconUrl(self):
        r"""插件图标url
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

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
        :param _OAuthConsent: OAuth 授权同意模式；0-开发者授权；1-使用者授权（仅在auth_type=3时生效）
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
        r"""OAuth 授权同意模式；0-开发者授权；1-使用者授权（仅在auth_type=3时生效）
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
        :param _Instructions: 系统提示词
        :type Instructions: str
        :param _Model: 主模型配置
        :type Model: :class:`tencentcloud.adp.v20260520.models.AgentModelConfig`
        :param _ToolList: <p>工具信息</p>
        :type ToolList: list of AgentToolConfig
        :param _PluginList: <p>插件信息</p>
        :type PluginList: list of AgentPluginConfig
        :param _SkillList: <p>技能信息</p>
        :type SkillList: list of AgentSkillConfig
        :param _AdvancedConfig: 高级设置
        :type AdvancedConfig: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        """
        self._Profile = None
        self._Instructions = None
        self._Model = None
        self._ToolList = None
        self._PluginList = None
        self._SkillList = None
        self._AdvancedConfig = None

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
        r"""系统提示词
        :rtype: str
        """
        return self._Instructions

    @Instructions.setter
    def Instructions(self, Instructions):
        self._Instructions = Instructions

    @property
    def Model(self):
        r"""主模型配置
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
        r"""高级设置
        :rtype: :class:`tencentcloud.adp.v20260520.models.AgentAdvancedConfig`
        """
        return self._AdvancedConfig

    @AdvancedConfig.setter
    def AdvancedConfig(self, AdvancedConfig):
        self._AdvancedConfig = AdvancedConfig


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
        :param _AuxiliaryInfo: 辅助信息(子状态/审批/申诉/搜索资源/特殊状态等)
注意：此字段可能返回 null，表示取不到有效值。
        :type AuxiliaryInfo: :class:`tencentcloud.adp.v20260520.models.AppAuxiliaryInfo`
        :param _Config: 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        :param _Metadata: 元数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: :class:`tencentcloud.adp.v20260520.models.AppMetadata`
        :param _SecretInfo: 应用密钥信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretInfo: :class:`tencentcloud.adp.v20260520.models.AppSecretInfo`
        :param _ShareUrlInfo: 分享链接信息(含访问控制)
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareUrlInfo: :class:`tencentcloud.adp.v20260520.models.AppShareURLInfo`
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: :class:`tencentcloud.adp.v20260520.models.AppStatusInfo`
        :param _SharedKbList: 应用引用的共享知识库列表
        :type SharedKbList: list of AppSharedKbInfo
        """
        self._AuxiliaryInfo = None
        self._Config = None
        self._Metadata = None
        self._SecretInfo = None
        self._ShareUrlInfo = None
        self._Status = None
        self._SharedKbList = None

    @property
    def AuxiliaryInfo(self):
        r"""辅助信息(子状态/审批/申诉/搜索资源/特殊状态等)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppAuxiliaryInfo`
        """
        return self._AuxiliaryInfo

    @AuxiliaryInfo.setter
    def AuxiliaryInfo(self, AuxiliaryInfo):
        self._AuxiliaryInfo = AuxiliaryInfo

    @property
    def Config(self):
        r"""配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Metadata(self):
        r"""元数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def SecretInfo(self):
        r"""应用密钥信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppSecretInfo`
        """
        return self._SecretInfo

    @SecretInfo.setter
    def SecretInfo(self, SecretInfo):
        self._SecretInfo = SecretInfo

    @property
    def ShareUrlInfo(self):
        r"""分享链接信息(含访问控制)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppShareURLInfo`
        """
        return self._ShareUrlInfo

    @ShareUrlInfo.setter
    def ShareUrlInfo(self, ShareUrlInfo):
        self._ShareUrlInfo = ShareUrlInfo

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppStatusInfo`
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SharedKbList(self):
        r"""应用引用的共享知识库列表
        :rtype: list of AppSharedKbInfo
        """
        return self._SharedKbList

    @SharedKbList.setter
    def SharedKbList(self, SharedKbList):
        self._SharedKbList = SharedKbList


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
        :param _EnableContextRewrite: 是否开启上下文改写
        :type EnableContextRewrite: bool
        :param _EnableImageTextRetrieval: 是否开启图文检索
        :type EnableImageTextRetrieval: bool
        :param _ReplyFlexibility: 回复灵活度
        :type ReplyFlexibility: int
        :param _IntentAchievement: 意图达成优先级
        :type IntentAchievement: list of IntentAchievementInfo
        """
        self._EnableContextRewrite = None
        self._EnableImageTextRetrieval = None
        self._ReplyFlexibility = None
        self._IntentAchievement = None

    @property
    def EnableContextRewrite(self):
        r"""是否开启上下文改写
        :rtype: bool
        """
        return self._EnableContextRewrite

    @EnableContextRewrite.setter
    def EnableContextRewrite(self, EnableContextRewrite):
        self._EnableContextRewrite = EnableContextRewrite

    @property
    def EnableImageTextRetrieval(self):
        r"""是否开启图文检索
        :rtype: bool
        """
        return self._EnableImageTextRetrieval

    @EnableImageTextRetrieval.setter
    def EnableImageTextRetrieval(self, EnableImageTextRetrieval):
        self._EnableImageTextRetrieval = EnableImageTextRetrieval

    @property
    def ReplyFlexibility(self):
        r"""回复灵活度
        :rtype: int
        """
        return self._ReplyFlexibility

    @ReplyFlexibility.setter
    def ReplyFlexibility(self, ReplyFlexibility):
        self._ReplyFlexibility = ReplyFlexibility

    @property
    def IntentAchievement(self):
        r"""意图达成优先级
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
        :param _Greeting: 欢迎语内容
        :type Greeting: str
        :param _OpeningQuestionList: 开场问题列表
        :type OpeningQuestionList: list of str
        """
        self._Greeting = None
        self._OpeningQuestionList = None

    @property
    def Greeting(self):
        r"""欢迎语内容
        :rtype: str
        """
        return self._Greeting

    @Greeting.setter
    def Greeting(self, Greeting):
        self._Greeting = Greeting

    @property
    def OpeningQuestionList(self):
        r"""开场问题列表
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
    r"""应用分享访问控制配置

    """

    def __init__(self):
        r"""
        :param _AccessType: 访问控制类型。枚举值: 1:公开访问(所有用户都可访问), 2:内部访问(仅企业用户可访问), 3:账号白名单(指定UIN/手机/邮箱/IP可访问)
        :type AccessType: int
        :param _Enabled: 体验链接开关
        :type Enabled: bool
        :param _Whitelist: 白名单(仅 access_type=ACCOUNT_WHITELIST 时生效)
        :type Whitelist: list of AppShareWhitelistItem
        """
        self._AccessType = None
        self._Enabled = None
        self._Whitelist = None

    @property
    def AccessType(self):
        r"""访问控制类型。枚举值: 1:公开访问(所有用户都可访问), 2:内部访问(仅企业用户可访问), 3:账号白名单(指定UIN/手机/邮箱/IP可访问)
        :rtype: int
        """
        return self._AccessType

    @AccessType.setter
    def AccessType(self, AccessType):
        self._AccessType = AccessType

    @property
    def Enabled(self):
        r"""体验链接开关
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Whitelist(self):
        r"""白名单(仅 access_type=ACCOUNT_WHITELIST 时生效)
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
    r"""应用分享白名单项

    """

    def __init__(self):
        r"""
        :param _Type: 白名单类型。枚举值: 1:UIN账号, 2:手机号码, 3:邮箱地址, 4:IP地址
        :type Type: int
        :param _Values: 白名单值列表(UIN/手机号/邮箱/IP等)
        :type Values: list of str
        """
        self._Type = None
        self._Values = None

    @property
    def Type(self):
        r"""白名单类型。枚举值: 1:UIN账号, 2:手机号码, 3:邮箱地址, 4:IP地址
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Values(self):
        r"""白名单值列表(UIN/手机号/邮箱/IP等)
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
        :param _Status: 应用状态 (OFFLINE:未上线, RUNNING:运行中, DISABLED:停用)。枚举值: 1:未上线, 2:运行中, 3:停用
        :type Status: int
        :param _StatusDescription: 状态描述
        :type StatusDescription: str
        """
        self._Status = None
        self._StatusDescription = None

    @property
    def Status(self):
        r"""应用状态 (OFFLINE:未上线, RUNNING:运行中, DISABLED:停用)。枚举值: 1:未上线, 2:运行中, 3:停用
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
        


class ClawAgentConfig(AbstractModel):
    r"""ClawAgent配置

    """

    def __init__(self):
        r"""
        :param _CustomConfig: 调用方自定义配置(控制C端用户在对话时可动态传入哪些自定义配置)
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomConfig: :class:`tencentcloud.adp.v20260520.models.ClawAgentCustomConfig`
        """
        self._CustomConfig = None

    @property
    def CustomConfig(self):
        r"""调用方自定义配置(控制C端用户在对话时可动态传入哪些自定义配置)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.adp.v20260520.models.ClawAgentCustomConfig`
        """
        return self._CustomConfig

    @CustomConfig.setter
    def CustomConfig(self, CustomConfig):
        self._CustomConfig = CustomConfig


    def _deserialize(self, params):
        if params.get("CustomConfig") is not None:
            self._CustomConfig = ClawAgentCustomConfig()
            self._CustomConfig._deserialize(params.get("CustomConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClawAgentCustomConfig(AbstractModel):
    r"""ClawAgent调用方自定义配置开关集合

    """

    def __init__(self):
        r"""
        :param _Enabled: <p>是否允许C端用户在对话时动态传入自定义Agent配置</p>
        :type Enabled: bool
        """
        self._Enabled = None

    @property
    def Enabled(self):
        r"""<p>是否允许C端用户在对话时动态传入自定义Agent配置</p>
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


class CreateReleaseRequest(AbstractModel):
    r"""CreateRelease请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _ChannelIdList: 渠道ID列表
        :type ChannelIdList: list of str
        :param _Description: 发布描述
        :type Description: str
        :param _IsDevToRelease: 将默认知识库中，仅调试生效的知识批量变更为"调试/发布都生效"
        :type IsDevToRelease: bool
        :param _IsPublishAsTemplate: 是否同步发布为应用模板
        :type IsPublishAsTemplate: bool
        """
        self._AppId = None
        self._ChannelIdList = None
        self._Description = None
        self._IsDevToRelease = None
        self._IsPublishAsTemplate = None

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
    def ChannelIdList(self):
        r"""渠道ID列表
        :rtype: list of str
        """
        return self._ChannelIdList

    @ChannelIdList.setter
    def ChannelIdList(self, ChannelIdList):
        self._ChannelIdList = ChannelIdList

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
    def IsDevToRelease(self):
        r"""将默认知识库中，仅调试生效的知识批量变更为"调试/发布都生效"
        :rtype: bool
        """
        return self._IsDevToRelease

    @IsDevToRelease.setter
    def IsDevToRelease(self, IsDevToRelease):
        self._IsDevToRelease = IsDevToRelease

    @property
    def IsPublishAsTemplate(self):
        r"""是否同步发布为应用模板
        :rtype: bool
        """
        return self._IsPublishAsTemplate

    @IsPublishAsTemplate.setter
    def IsPublishAsTemplate(self, IsPublishAsTemplate):
        self._IsPublishAsTemplate = IsPublishAsTemplate


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._ChannelIdList = params.get("ChannelIdList")
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
        :param _NeedApproval: need_approval
        :type NeedApproval: bool
        :param _ReleaseId: release_id
        :type ReleaseId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NeedApproval = None
        self._ReleaseId = None
        self._RequestId = None

    @property
    def NeedApproval(self):
        r"""need_approval
        :rtype: bool
        """
        return self._NeedApproval

    @NeedApproval.setter
    def NeedApproval(self, NeedApproval):
        self._NeedApproval = NeedApproval

    @property
    def ReleaseId(self):
        r"""release_id
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


class DeleteAppRequest(AbstractModel):
    r"""DeleteApp请求参数结构体

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


class DescribeAppRequest(AbstractModel):
    r"""DescribeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 应用ID
        :type AppId: str
        :param _Domain: 应用域: ADP_DOMAIN_DEV(1)=开发域, ADP_DOMAIN_PROD(2)=发布域。枚举值: 1:开发域, 2:生产域
        :type Domain: int
        :param _FieldMask: 字段掩码，指定需要返回的字段(Paths为空则返回所有字段)。Paths枚举值：AppConfig(应用配置), SecretInfo(应用密钥信息), ShareUrlInfo(分享链接信息), SpecialStatusInfo(特殊状态信息), SearchResourceStatus(搜索资源状态), SharedKbList(应用引用的共享知识库列表)
        :type FieldMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        :param _StatusType: 特殊状态类型(当FieldMask包含SpecialStatusInfo时必填)。枚举值: 1:回滚状态, 2:首次导入状态
        :type StatusType: int
        """
        self._AppId = None
        self._Domain = None
        self._FieldMask = None
        self._StatusType = None

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
    def Domain(self):
        r"""应用域: ADP_DOMAIN_DEV(1)=开发域, ADP_DOMAIN_PROD(2)=发布域。枚举值: 1:开发域, 2:生产域
        :rtype: int
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def FieldMask(self):
        r"""字段掩码，指定需要返回的字段(Paths为空则返回所有字段)。Paths枚举值：AppConfig(应用配置), SecretInfo(应用密钥信息), ShareUrlInfo(分享链接信息), SpecialStatusInfo(特殊状态信息), SearchResourceStatus(搜索资源状态), SharedKbList(应用引用的共享知识库列表)
        :rtype: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        return self._FieldMask

    @FieldMask.setter
    def FieldMask(self, FieldMask):
        self._FieldMask = FieldMask

    @property
    def StatusType(self):
        r"""特殊状态类型(当FieldMask包含SpecialStatusInfo时必填)。枚举值: 1:回滚状态, 2:首次导入状态
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
        :param _App: 应用详情
        :type App: :class:`tencentcloud.adp.v20260520.models.App`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._App = None
        self._RequestId = None

    @property
    def App(self):
        r"""应用详情
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FirstRecordId = None
        self._HasMoreAfter = None
        self._HasMoreBefore = None
        self._LastRecordId = None
        self._MessageList = None
        self._Messages = None
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
        r"""<p>消息列表</p>
        :rtype: list of ConversationMessage
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

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
        """
        self._PluginId = None
        self._SpaceId = None
        self._FieldMask = None

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


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
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
        """
        self._ExternalMCPServerUrl = None
        self._MCPServerUrl = None
        self._MCPTransport = None
        self._PluginHeader = None
        self._PluginQuery = None
        self._SSEReadTimeout = None
        self._Timeout = None
        self._AuthConfig = None

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
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        :param _EnumValueList: 可选值列表
        :type EnumValueList: list of str
        :param _MaxValue: 最大值（仅数值类型有效）
        :type MaxValue: float
        :param _MinValue: 最小值（仅数值类型有效）
        :type MinValue: float
        :param _Name: 超参名称
        :type Name: str
        :param _Type: 超参类型。1-浮点数, 2-整数, 3-字符串
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
        r"""默认值
        :rtype: str
        """
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def EnumValueList(self):
        r"""可选值列表
        :rtype: list of str
        """
        return self._EnumValueList

    @EnumValueList.setter
    def EnumValueList(self, EnumValueList):
        self._EnumValueList = EnumValueList

    @property
    def MaxValue(self):
        r"""最大值（仅数值类型有效）
        :rtype: float
        """
        return self._MaxValue

    @MaxValue.setter
    def MaxValue(self, MaxValue):
        self._MaxValue = MaxValue

    @property
    def MinValue(self):
        r"""最小值（仅数值类型有效）
        :rtype: float
        """
        return self._MinValue

    @MinValue.setter
    def MinValue(self, MinValue):
        self._MinValue = MinValue

    @property
    def Name(self):
        r"""超参名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""超参类型。1-浮点数, 2-整数, 3-字符串
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
        :param _AppId: 应用ID
        :type AppId: str
        :param _AppMode: 应用模式。枚举值: 1:标准模式, 2:Agent模式, 3:单工作流模式, 4:ClawAgent模式
        :type AppMode: int
        :param _Avatar: 应用头像
        :type Avatar: str
        :param _Config: 应用配置
        :type Config: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        :param _Description: 应用描述
        :type Description: str
        :param _Name: 应用名称
        :type Name: str
        :param _ShareConfig: 分享配置
        :type ShareConfig: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        :param _SharedKbIdList: 引用的共享知识库ID列表(全量覆盖)
        :type SharedKbIdList: list of str
        :param _UpdateMask: 字段掩码，指定需要更新的字段(Paths为空则不更新任何字段)。Paths枚举值：
【顶层】Name, Avatar, Description, AppMode, ShareConfig, SharedKbIdList
【Greeting】Config.Greeting, Config.Greeting.Greeting, Config.Greeting.OpeningQuestionList
【Model】Config.Model, Config.Model.ThinkModel, Config.Model.GenerateModel, Config.Model.AiOptimizeModel, Config.Model.FileParseModel, Config.Model.PromptRewriteModel, Config.Model.MultiModalQaModel, Config.Model.MultiModalUnderstandingModel
【WebSearch】Config.WebSearch
【Memory】Config.Memory, Config.Memory.Enabled, Config.Memory.LongMemoryDay, Config.Memory.Model, Config.Memory.PromptMode, Config.Memory.PromptContent
【Mode】Config.Mode, Config.Mode.MultiAgentConfig, Config.Mode.SingleWorkflowConfig
【Experience】Config.Experience, Config.Experience.Conversation, Config.Experience.Role, Config.Experience.Advanced
【Experience.Conversation】Config.Experience.Conversation.AiCall, Config.Experience.Conversation.BackgroundImage, Config.Experience.Conversation.Method, Config.Experience.Conversation.FallbackReply, Config.Experience.Conversation.Recommended, Config.Experience.Conversation.InputBoxConfig, Config.Experience.Conversation.WebSearch
【Experience.Conversation.AiCall】Config.Experience.Conversation.AiCall.VoiceInteract, Config.Experience.Conversation.AiCall.VoiceCall, Config.Experience.Conversation.AiCall.DigitalHuman
【Experience.Advanced】Config.Experience.Advanced.ContextRewrite, Config.Experience.Advanced.ImageTextRetrieval, Config.Experience.Advanced.IntentAchievement, Config.Experience.Advanced.ReplyFlexibility
        :type UpdateMask: :class:`tencentcloud.adp.v20260520.models.FieldMask`
        """
        self._AppId = None
        self._AppMode = None
        self._Avatar = None
        self._Config = None
        self._Description = None
        self._Name = None
        self._ShareConfig = None
        self._SharedKbIdList = None
        self._UpdateMask = None

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
    def Config(self):
        r"""应用配置
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

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
    def ShareConfig(self):
        r"""分享配置
        :rtype: :class:`tencentcloud.adp.v20260520.models.AppShareAccessControl`
        """
        return self._ShareConfig

    @ShareConfig.setter
    def ShareConfig(self, ShareConfig):
        self._ShareConfig = ShareConfig

    @property
    def SharedKbIdList(self):
        r"""引用的共享知识库ID列表(全量覆盖)
        :rtype: list of str
        """
        return self._SharedKbIdList

    @SharedKbIdList.setter
    def SharedKbIdList(self, SharedKbIdList):
        self._SharedKbIdList = SharedKbIdList

    @property
    def UpdateMask(self):
        r"""字段掩码，指定需要更新的字段(Paths为空则不更新任何字段)。Paths枚举值：
【顶层】Name, Avatar, Description, AppMode, ShareConfig, SharedKbIdList
【Greeting】Config.Greeting, Config.Greeting.Greeting, Config.Greeting.OpeningQuestionList
【Model】Config.Model, Config.Model.ThinkModel, Config.Model.GenerateModel, Config.Model.AiOptimizeModel, Config.Model.FileParseModel, Config.Model.PromptRewriteModel, Config.Model.MultiModalQaModel, Config.Model.MultiModalUnderstandingModel
【WebSearch】Config.WebSearch
【Memory】Config.Memory, Config.Memory.Enabled, Config.Memory.LongMemoryDay, Config.Memory.Model, Config.Memory.PromptMode, Config.Memory.PromptContent
【Mode】Config.Mode, Config.Mode.MultiAgentConfig, Config.Mode.SingleWorkflowConfig
【Experience】Config.Experience, Config.Experience.Conversation, Config.Experience.Role, Config.Experience.Advanced
【Experience.Conversation】Config.Experience.Conversation.AiCall, Config.Experience.Conversation.BackgroundImage, Config.Experience.Conversation.Method, Config.Experience.Conversation.FallbackReply, Config.Experience.Conversation.Recommended, Config.Experience.Conversation.InputBoxConfig, Config.Experience.Conversation.WebSearch
【Experience.Conversation.AiCall】Config.Experience.Conversation.AiCall.VoiceInteract, Config.Experience.Conversation.AiCall.VoiceCall, Config.Experience.Conversation.AiCall.DigitalHuman
【Experience.Advanced】Config.Experience.Advanced.ContextRewrite, Config.Experience.Advanced.ImageTextRetrieval, Config.Experience.Advanced.IntentAchievement, Config.Experience.Advanced.ReplyFlexibility
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
        if params.get("ShareConfig") is not None:
            self._ShareConfig = AppShareAccessControl()
            self._ShareConfig._deserialize(params.get("ShareConfig"))
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
        :param _AppId: app_id
        :type AppId: str
        :param _UpdateTime: 更新时间 (Unix时间戳,秒级)
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._UpdateTime = None
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
    def UpdateTime(self):
        r"""更新时间 (Unix时间戳,秒级)
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
        :type Operation: :class:`tencentcloud.adp.v20260520.models.PluginOperation`
        :param _PluginId: 插件id
        :type PluginId: str
        :param _PluginVersion: 插件版本号
        :type PluginVersion: int
        :param _Profile: 插件基础信息
        :type Profile: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        :param _Statistics: 插件统计信息
        :type Statistics: :class:`tencentcloud.adp.v20260520.models.PluginStatistics`
        :param _Status: <p>插件状态，1:可用，2:不可用 </p><p>枚举值：</p><ul><li>1： 可用</li><li>2： 不可用</li></ul>
        :type Status: int
        :param _ToolList: 工具列表
        :type ToolList: list of Tool
        :param _UpdateTime: 更新时间，Unix时间戳
        :type UpdateTime: str
        :param _UserState: 用户维度的插件状态信息
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
        :rtype: :class:`tencentcloud.adp.v20260520.models.PluginProfile`
        """
        return self._Profile

    @Profile.setter
    def Profile(self, Profile):
        self._Profile = Profile

    @property
    def Statistics(self):
        r"""插件统计信息
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
        """
        self._Operation = None
        self._PluginId = None
        self._Profile = None
        self._Statistics = None
        self._Status = None
        self._UserState = None
        self._Config = None

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
        


class ReleaseSummary(AbstractModel):
    r"""发布摘要信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间 (Unix时间戳,秒级)
        :type CreateTime: str
        :param _Description: 发布描述
        :type Description: str
        :param _ReleaseId: 发布ID
        :type ReleaseId: str
        :param _Status: 发布状态。枚举值: 1:待发布, 2:发布中, 3:发布成功, 4:发布失败, 5:审核中, 6:审核成功, 7:审核失败, 8:发布成功回调处理中, 9:发布暂停, 10:申诉审核中, 11:申诉审核通过, 12:申诉审核不通过
        :type Status: int
        :param _StatusDescription: 状态描述
        :type StatusDescription: str
        :param _ChannelIdList: 发布渠道ID列表
        :type ChannelIdList: list of str
        """
        self._CreateTime = None
        self._Description = None
        self._ReleaseId = None
        self._Status = None
        self._StatusDescription = None
        self._ChannelIdList = None

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
        r"""发布描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def ChannelIdList(self):
        r"""发布渠道ID列表
        :rtype: list of str
        """
        return self._ChannelIdList

    @ChannelIdList.setter
    def ChannelIdList(self, ChannelIdList):
        self._ChannelIdList = ChannelIdList


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._ReleaseId = params.get("ReleaseId")
        self._Status = params.get("Status")
        self._StatusDescription = params.get("StatusDescription")
        self._ChannelIdList = params.get("ChannelIdList")
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
        


class Variable(AbstractModel):
    r"""变量信息

    """

    def __init__(self):
        r"""
        :param _DefaultFileName: 默认文件名称
        :type DefaultFileName: str
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        :param _Description: 变量描述
        :type Description: str
        :param _ModuleType: 模块类型。枚举值: 1:环境参数, 2:应用参数, 3:系统参数, -1:所有参数
        :type ModuleType: int
        :param _Name: 变量名称
        :type Name: str
        :param _Type: 变量类型。枚举值: 1:字符串, 2:整数, 3:浮点数, 4:布尔值, 5:对象, 6:字符串数组, 7:整数数组, 8:浮点数数组, 9:布尔值数组, 10:对象数组, 11:文件, 12:文档, 13:图片, 14:音频, 15:视频, 16:文件数组, 17:文档数组, 18:图片数组, 19:音频数组, 20:视频数组, 21:数组的数组, 22:密钥/敏感信息, 99:空值
        :type Type: int
        :param _VariableId: 变量ID
        :type VariableId: str
        """
        self._DefaultFileName = None
        self._DefaultValue = None
        self._Description = None
        self._ModuleType = None
        self._Name = None
        self._Type = None
        self._VariableId = None

    @property
    def DefaultFileName(self):
        r"""默认文件名称
        :rtype: str
        """
        return self._DefaultFileName

    @DefaultFileName.setter
    def DefaultFileName(self, DefaultFileName):
        self._DefaultFileName = DefaultFileName

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
        r"""变量描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
    def Name(self):
        r"""变量名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""变量类型。枚举值: 1:字符串, 2:整数, 3:浮点数, 4:布尔值, 5:对象, 6:字符串数组, 7:整数数组, 8:浮点数数组, 9:布尔值数组, 10:对象数组, 11:文件, 12:文档, 13:图片, 14:音频, 15:视频, 16:文件数组, 17:文档数组, 18:图片数组, 19:音频数组, 20:视频数组, 21:数组的数组, 22:密钥/敏感信息, 99:空值
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def VariableId(self):
        r"""变量ID
        :rtype: str
        """
        return self._VariableId

    @VariableId.setter
    def VariableId(self, VariableId):
        self._VariableId = VariableId


    def _deserialize(self, params):
        self._DefaultFileName = params.get("DefaultFileName")
        self._DefaultValue = params.get("DefaultValue")
        self._Description = params.get("Description")
        self._ModuleType = params.get("ModuleType")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._VariableId = params.get("VariableId")
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
        